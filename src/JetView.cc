#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/Framework/interface/EventSetup.h"


#include "MNTriggerStudies/MNTriggerAna/interface/JetView.h"
#include <boost/foreach.hpp>
#include <boost/algorithm/string.hpp>
#include <cmath>
#include <sstream>
#include <algorithm>
//#include "JetMETCorrections/Objects/interface/JetCorrectionsRecord.h"
//#include "DataFormats/FWLite/interface/EventSetup.h"
//#include "FWCore/Framework/interface/ESHandle.h"
#include "CondFormats/JetMETObjects/interface/JetCorrectorParameters.h"
//#include "JetMETCorrections/Objects/interface/JetCorrector.h"
#include "JetMETCorrections/Objects/interface/JetCorrectionsRecord.h"
#include <DataFormats/Math/interface/deltaR.h>



// https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuidePhysicsCutParser - should I ?

namespace xx {
    float stof(std::string s){
        std::stringstream ss(s);
        float ret;
        ss >> ret;
        return ret;
    }

    struct TempJetHolder {
        reco::Candidate::LorentzVector p4;
        reco::Candidate::LorentzVector p4Gen;
        int jetId;
    };
    bool ptSort(const xx::TempJetHolder & p1, const xx::TempJetHolder & p2) {
        return p1.p4.pt() > p2.p4.pt();
    }

}




JetView::JetView(const edm::ParameterSet& iConfig, TTree * tree):
EventViewBase(iConfig, tree),
pfJetID(PFJetIDSelectionFunctor::FIRSTDATA, PFJetIDSelectionFunctor::LOOSE),
caloJetID(JetIDSelectionFunctor::PURE09,  JetIDSelectionFunctor::LOOSE),
m_jecUnc(0)

{

    m_storageVersion =  iConfig.getUntrackedParameter<int>("storeageVersion", 0);
    m_maxEta = iConfig.getParameter<double>("maxEta");
    m_minPt = iConfig.getParameter<double>("minPt");
    m_maxnum = iConfig.getParameter<int>("maxnum"); // save maxnum hardest jets

    m_caloBase = iConfig.getParameter<edm::InputTag>("optionalCaloJets4ID");
    m_caloBaseID = iConfig.getParameter<edm::InputTag>("optionalCaloID4ID");
    m_disableJetID = iConfig.getParameter<bool>("disableJetID");

    m_inputCol = iConfig.getParameter<edm::InputTag>("input");
    m_variations = iConfig.getParameter<std::vector<std::string> >("variations"); // "" (central), _jecUp/Down, _jerUp/Down
    std::set<std::string> knownVars;
    knownVars.insert(""); // central value (no variation)
    knownVars.insert("jecUp");
    knownVars.insert("jecDown");
    knownVars.insert("jerUp");
    knownVars.insert("jerDown");
    // TODO register branches
    //registerVecP4("recoTracks", tree);
    //registerVecFloat("dz", tree);
    //registerVecFloat("dxy", tree);



    BOOST_FOREACH( std::string s, m_variations){
        if (knownVars.find(s)==knownVars.end()){
            throw "Variation not known "+s + "\n";
        }
        if (s != "") s = "_" + s;
        if (m_storageVersion == 0) {
            registerVecP4("newjets"+s, tree);
            registerVecP4("newgenjets"+s, tree);
            registerVecInt("newjetid"+s, tree);
        } else if (m_storageVersion == 1){
            registerVecInt("jetid"+s, tree);
            registerVecFloat("pt"+s, tree);
            registerVecFloat("eta"+s, tree);
            registerVecFloat("phi"+s, tree);
            registerVecFloat("genpt"+s, tree);
            registerVecFloat("geneta"+s, tree);
            registerVecFloat("genphi"+s, tree);



        } else {
            throw cms::Exception("Storage version not known");
        }


    }

    std::vector<std::string> JERdesc = iConfig.getParameter<std::vector<std::string> >("jerFactors");
    BOOST_FOREACH( std::string s, JERdesc){
        std::vector<std::string> floatsAsStrings;
        boost::split(floatsAsStrings, s, boost::is_any_of("\t "));
        //
        // 0.5 1.052 0.012 0.062 0.061
        if (floatsAsStrings.size() != 5) {
            throw "Wrong size of JER factors string\n";
        }
            float etaMax = xx::stof(floatsAsStrings[0]);
            float jer = xx::stof(floatsAsStrings[1]);
            float err = xx::stof(floatsAsStrings[2]);
            float errUp = xx::stof(floatsAsStrings[3]);
            float errDown  = xx::stof(floatsAsStrings[4]);
            float jerUp   = jer + sqrt(err*err+errUp*errUp);
            float jerDown = jer - sqrt(err*err+errDown*errDown);
            std::vector<float> JER;
            JER.push_back(etaMax);
            JER.push_back(jer);
            JER.push_back(jerUp);
            JER.push_back(jerDown);
            m_JER.push_back(JER);
            //print "JER factors:", etaMax, jer, jerUp, jerDown, "|", err, errUp, errDown
    }

}


void JetView::fillSpecific(const edm::Event& iEvent, const edm::EventSetup& iSetup){
    edm::Handle<pat::JetCollection> hJets;
    iEvent.getByLabel(m_inputCol, hJets);

    if (m_jecUnc == 0 && hJets->size()>0 ) { // couldnt find better place..
        edm::ESHandle<JetCorrectorParametersCollection> JetCorParColl;
        std::string payload("AK5PF");
        if (hJets->at(0).isCaloJet()) {
            payload == "AK5Calo";
        }
        iSetup.get<JetCorrectionsRecord>().get(payload,JetCorParColl); 
        JetCorrectorParameters const & JetCorPar = (*JetCorParColl)["Uncertainty"];
        m_jecUnc = new JetCorrectionUncertainty(JetCorPar);
    }


    // save indices of jets, that have non-nonsense JEC (no negative values)
    std::vector<int> goodJets;
    for (unsigned int i = 0; i<hJets->size(); ++i){
        if ( std::abs(hJets->at(i).eta()) > m_maxEta) continue;
        if ( hJets->at(i).pt() <  m_minPt) continue;

        std::vector<std::string> jecs = hJets->at(i).availableJECLevels(0);
        bool badJet = false;

        for (unsigned int aa = 0; aa < jecs.size(); ++aa){
            if (hJets->at(i).jecFactor(jecs[aa])<0) {
                badJet = true;
                break;
            }
        }
        if (badJet) continue;
        goodJets.push_back(i);
    }

    BOOST_FOREACH( std::string variation, m_variations){
        std::vector<xx::TempJetHolder> tj;
        BOOST_FOREACH(int i, goodJets){
            xx::TempJetHolder t;
            t.p4Gen = reco::Candidate::LorentzVector();
            if (hJets->at(i).genJet()){
               t.p4Gen = hJets->at(i).genJet()->p4();
            }
            t.jetId = jetID(hJets->at(i), iEvent);
            t.p4 = getMomentum(hJets->at(i), variation);
            tj.push_back(t);

        }
        std::sort(tj.begin(), tj.end(), xx::ptSort);
        while (tj.size() > m_maxnum) tj.pop_back();
        if (variation != "") variation = "_" + variation;
        BOOST_FOREACH(xx::TempJetHolder t, tj){
            if (m_storageVersion == 0) {
                addToP4Vec("newjets"+variation, t.p4);
                addToP4Vec("newgenjets"+variation, t.p4Gen);
                addToIVec("newjetid"+variation, t.jetId);
            } else {
                addToIVec("jetid"+variation, t.jetId);
                addToFVec("pt"+variation, t.p4.pt());
                addToFVec("eta"+variation, t.p4.eta());
                addToFVec("phi"+variation, t.p4.phi());
                addToFVec("genpt"+variation, t.p4Gen.pt());
                addToFVec("geneta"+variation, t.p4Gen.eta());
                addToFVec("genphi"+variation, t.p4Gen.phi());
            }
        }
    }
}

reco::Candidate::LorentzVector JetView::getMomentum(const pat::Jet & jet, std::string variation) {
    reco::Candidate::LorentzVector gen;
    if (jet.genJet()){
       gen  = jet.genJet()->p4();
    }
    // at this point jet momentum has JEC fully applied
    if (variation == "" or  variation.find("jer") != std::string::npos) {
        return smear(gen, jet.p4(), variation);
    }
    else if (  variation.find("jec") != std::string::npos) {
        // Note: first apply JEC shift, than central JER shift
        reco::Candidate::LorentzVector jecShifted = shiftJEC(jet.p4(), variation);
        return smear(gen, jecShifted, ""); // here we want to have the central value of JER smear
    }

    throw "Variation not known: " + variation + "\n";
    return jet.p4();
} 

reco::Candidate::LorentzVector JetView::smear(const reco::Candidate::LorentzVector & gen, 
                                              const reco::Candidate::LorentzVector & rec,
                                              std::string variation)
{
    if (gen.pt() < 0.01) return rec; // no gen jet, no smear possible
    if (rec.pt() < 0.01) return rec; // no rec jet, possible in some cases when JEC variation applied earlier

    float eta = std::abs(rec.eta());
    if (eta > 5) return rec; // no smearing factors for higher values
    float factor = -1;
    for(unsigned int i = 0; i < m_JER.size(); ++i){
        if (eta < m_JER[i][0]){
            if (variation == "") factor = m_JER[i].at(1);
            else if (variation == "jerDown") factor = m_JER[i].at(2);
            else if (variation == "jerUp") factor = m_JER[i].at(3);
            else throw "Unexpected variation: "+ variation + "\n";
            break;
        }
    }
    if (factor < 0){
        throw "Cannot determine JER factor for jet\n";
    }

    float ptRec = rec.pt();
    float ptGen = gen.pt();
    float diff = ptRec-ptGen;
    float ptRet = std::max(float(0.), ptGen+factor*diff);
    if (ptRet < 0.01){
        return  reco::Candidate::LorentzVector();
    }

    float scaleFactor = ptRet/ptRec;
    return rec*scaleFactor;

}

reco::Candidate::LorentzVector JetView::shiftJEC(const reco::Candidate::LorentzVector &rec,  std::string variation) {
    if (variation != "jecUp" and variation != "jecDown"){
        throw "JetView::shiftJEC:  Unecpected variation " + variation + "\n";
    }

    m_jecUnc->setJetEta(rec.eta());
    m_jecUnc->setJetPt(rec.eta());
    float unc = m_jecUnc->getUncertainty(true);
    float ptFactor = 1.;
    if (variation == "jecDown") ptFactor = -1;
    float factor = 1. + ptFactor*unc;
    if (factor <= 0) return reco::Candidate::LorentzVector();
    return rec*factor;

}





int JetView::jetID(const pat::Jet & jet, const edm::Event& iEvent) {
    if (m_disableJetID) return 1;
    int ret = 1;
    if (jet.isCaloJet()) {
        // We are doing this in a wicked way, since having jetID and jetArea in calo jets is not possible at same time (4_2 series)
        JetIDSelectionFunctor jetIDSelector( JetIDSelectionFunctor::PURE09, JetIDSelectionFunctor::LOOSE); //loose
        pat::strbitset bset = jetIDSelector.getBitTemplate();
        edm::Handle<edm::View< reco::CaloJet > > hJets;
        edm::Handle<reco::JetIDValueMap> hJetIDMap;
        //m_caloBase = iConfig.getParameter<edm::InputTag>("optionalCaloJets4ID");
        //m_caloBaseID = iConfig.getParameter<edm::InputTag>("optionalCaloID4ID");
        //iEvent.getByLabel(edm::InputTag("ak5CaloJets","","RECO"), hJets );
        //iEvent.getByLabel( "ak5JetID", hJetIDMap );
        iEvent.getByLabel(m_caloBase, hJets );
        iEvent.getByLabel(m_caloBaseID, hJetIDMap );

        bool passed = false;
        float bestDR = 99;
        for ( edm::View<reco::CaloJet>::const_iterator ibegin = hJets->begin(),
                iend = hJets->end(), ijet = ibegin; ijet != iend; ++ijet )
        {

                float dr = reco::deltaR(ijet->p4(), jet.p4());
                if (dr > 0.5 ) continue;
                if (dr > bestDR) continue;
                bestDR = dr;
                unsigned int idx = ijet - ibegin;
                edm::RefToBase<reco::CaloJet> jetRef = hJets->refAt(idx);
                const reco::CaloJet *calojet = dynamic_cast<const reco::CaloJet *>(jetRef.get());
                reco::JetID jetId = (*hJetIDMap)[ jetRef ];
                bset.set(false);
                passed = jetIDSelector(*calojet,jetId, bset);
        }
        if (!passed) ret = 0;
    } else if (jet.isPFJet()) {
        pat::strbitset bs = pfJetID.getBitTemplate(); 
        if (!pfJetID(jet, bs)) ret = 0;
    }

    return ret;

}


