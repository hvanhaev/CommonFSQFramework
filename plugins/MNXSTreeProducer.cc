// -*- C++ -*-
//
// Package:    MNXSTreeProducer
// Class:      MNXSTreeProducer
// 
/**\class MNXSTreeProducer MNXSTreeProducer.cc MNTriggerStudies/MNXSTreeProducer/plugins/MNXSTreeProducer.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Tomasz Fruboes
//         Created:  Thu, 17 Apr 2014 16:06:29 GMT
// $Id$
//
//




// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "TTree.h"

#include "DataFormats/PatCandidates/interface/Jet.h"
#include "SimDataFormats/GeneratorProducts/interface/GenEventInfoProduct.h"
#include "SimDataFormats/PileupSummaryInfo/interface/PileupSummaryInfo.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/PatCandidates/interface/TriggerEvent.h"

#include <algorithm>

#include "PhysicsTools/SelectorUtils/interface/PFJetIDSelectionFunctor.h"
#include "PhysicsTools/SelectorUtils/interface/JetIDSelectionFunctor.h"
#include <DataFormats/Math/interface/deltaR.h>

#include "MNTriggerStudies/MNTriggerAna/interface/JetView.h"
#include "MNTriggerStudies/MNTriggerAna/interface/EventIdData.h"
#include "MNTriggerStudies/MNTriggerAna/interface/TriggerResultsView.h"

//
// class declaration
//

bool ptSort(const reco::Candidate::LorentzVector & p1, const reco::Candidate::LorentzVector & p2) {
    return p1.pt() > p2.pt();
}



class MNXSTreeProducer : public edm::EDAnalyzer {
   public:
      explicit MNXSTreeProducer(const edm::ParameterSet&);
      ~MNXSTreeProducer();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);


   private:
      void resetTrees();
      virtual void beginJob();
      virtual void analyze(const edm::Event&, const edm::EventSetup&);
      virtual void endJob();
      reco::Candidate::LorentzVector smear(const pat::Jet & jet);
      bool jetID(const pat::Jet & jet, const edm::Event& iEvent);

      TTree *m_tree;
      std::map<std::string, int> m_integerBranches;
      std::map<std::string, float> m_floatBranches;
      std::map<std::string, std::vector<reco::Candidate::LorentzVector> > m_vectorBranches;
      std::map<std::string, std::vector<int> > m_vecIntBranches;

      std::map<std::string, edm::InputTag> m_todo;
      std::map<std::string, std::vector<std::string> > m_todoTriggers;

      PFJetIDSelectionFunctor pfJetID;
      JetIDSelectionFunctor caloJetID;

      float  m_minGenPT;
      //virtual void beginRun(edm::Run const&, edm::EventSetup const&) override;
      //virtual void endRun(edm::Run const&, edm::EventSetup const&) override;
      //virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;
      //virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;

      // ----------member data ---------------------------
      std::vector<EventViewBase *> m_views;
};

//
// constants, enums and typedefs
//

//
// static data member definitions
//

//
// constructors and destructor
//
MNXSTreeProducer::MNXSTreeProducer(const edm::ParameterSet& iConfig):
pfJetID(PFJetIDSelectionFunctor::FIRSTDATA, PFJetIDSelectionFunctor::LOOSE),
caloJetID(JetIDSelectionFunctor::PURE09,  JetIDSelectionFunctor::LOOSE)
{

    m_minGenPT = iConfig.getParameter<double>("minGenPT");

    edm::Service<TFileService> tFileService;
    m_tree = tFileService->make<TTree>("data", "data");
    m_views.push_back(new EventIdData(iConfig, m_tree));
    m_views.push_back(new JetView(iConfig.getParameter< edm::ParameterSet >("JetViewPF"), m_tree));
    m_views.push_back(new JetView(iConfig.getParameter< edm::ParameterSet >("JetViewCalo"), m_tree));
    m_views.push_back(new TriggerResultsView(iConfig.getParameter< edm::ParameterSet >("TriggerResultsView"), m_tree));


    m_todoTriggers["doubleJ15FB"] = std::vector<std::string>();
    m_todoTriggers["doubleJ15FB"].push_back("HLT_DoubleJet15U_ForwardBackward");
    m_todoTriggers["doubleJ15FB"].push_back("HLT_DoubleJet15U_ForwardBackward_v3");
    m_todoTriggers["jet15"] = std::vector<std::string>();
    m_todoTriggers["jet15"].push_back("HLT_Jet15U");
    m_todoTriggers["jet15"].push_back("HLT_Jet15U_v3");

    m_todoTriggers["djAve15"] = std::vector<std::string>();
    m_todoTriggers["djAve15"].push_back("HLT_DiJetAve15U");
    m_todoTriggers["djAve15"].push_back("HLT_DiJetAve15U_8E29");
    m_todoTriggers["djAve15"].push_back("HLT_DiJetAve15U_v3");


    // define your branches. Registration will be made automagically
    //
    //  note: verify, that your data is filled in the tree. If you will
    //        define your variable name as m_floatBranches["leadJetPt"]
    //        and than missspell the name in the analyze method:
    //          m_floatBranches["leadJetPT"] = 123; // note the wrong case in PT/Pt
    //        program will continue to run not filling your variable
    //
    // use m_integerBranches for integer values
    m_integerBranches["ngoodVTX"] = 0;
    m_integerBranches["HBHENoiseFilterResult"] = 0;
    m_integerBranches["HBHENoiseFilterResult2"] = 0;

    std::map<std::string, std::vector<std::string> >::iterator itTrg = m_todoTriggers.begin();
    for (;itTrg != m_todoTriggers.end(); ++itTrg){
            m_integerBranches[itTrg->first] = 0;
    }


    // use m_floatBranches for float values


    m_vectorBranches["genJets"] = std::vector<reco::Candidate::LorentzVector>();

    // 

    // integer branches auto registration
    {
        std::map<std::string, int>::iterator it =  m_integerBranches.begin();
        std::map<std::string, int>::iterator itE =  m_integerBranches.end();
        for (;it != itE;++it){
            m_tree->Branch(it->first.c_str(), &it->second, (it->first+"/I").c_str());
        }
    }

    // float branches auto registration
    {
        std::map<std::string, float>::iterator it =  m_floatBranches.begin();
        std::map<std::string, float>::iterator itE =  m_floatBranches.end();
        for (;it != itE;++it){
            m_tree->Branch(it->first.c_str(), &it->second, (it->first+"/F").c_str());
        }

    }


    // p4 vector branches autoreg
    {   
        std::map<std::string, std::vector<reco::Candidate::LorentzVector> >::iterator it =  m_vectorBranches.begin();
        std::map<std::string, std::vector<reco::Candidate::LorentzVector> >::iterator itE =  m_vectorBranches.end();
        for (;it != itE;++it){
            m_tree->Branch(it->first.c_str(), &it->second);//#;, (it->first+"/I").c_str());
        }
    }

    // int vector branches autoreg
    {
        std::map<std::string, std::vector<int> >::iterator it =  m_vecIntBranches.begin();
        std::map<std::string, std::vector<int> >::iterator itE =  m_vecIntBranches.end();
        for (;it != itE;++it){
            m_tree->Branch(it->first.c_str(), "std::vector< int >", &it->second);//#;, (it->first+"/I").c_str());
        }
    }




}
void MNXSTreeProducer::resetTrees(){

    // int branches
    {
        std::map<std::string, int>::iterator it =  m_integerBranches.begin();
        std::map<std::string, int>::iterator itE =  m_integerBranches.end();
        for (;it != itE;++it){
                m_integerBranches[it->first]=0;
        }
    }

    // float branches
    {
        std::map<std::string, float>::iterator it =  m_floatBranches.begin();
        std::map<std::string, float>::iterator itE =  m_floatBranches.end();
        for (;it != itE;++it){
                m_floatBranches[it->first]=0;
        }
    }


    //
    {
        std::map<std::string, std::vector<reco::Candidate::LorentzVector> >::iterator it =  m_vectorBranches.begin();
        std::map<std::string, std::vector<reco::Candidate::LorentzVector> >::iterator itE =  m_vectorBranches.end();
        for (;it != itE;++it){
            m_vectorBranches[it->first].clear();
        }
    }


    // int vector branches autoreg
    {   
        std::map<std::string, std::vector<int> >::iterator it =  m_vecIntBranches.begin();
        std::map<std::string, std::vector<int> >::iterator itE =  m_vecIntBranches.end();
        for (;it != itE;++it){
            m_vecIntBranches[it->first].clear();
        }
    }


}
//%
MNXSTreeProducer::~MNXSTreeProducer()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called for each event  ------------
void
MNXSTreeProducer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{

        
    resetTrees();
    using namespace edm;

    edm::Handle< std::vector<reco::Vertex> > hVTX;
    iEvent.getByLabel(edm::InputTag("offlinePrimaryVertices"), hVTX);
    int vtxCnt = 0;
    for (unsigned int i = 0; i < hVTX->size(); ++i){
        if (!hVTX->at(i).isValid() ) continue;
        if (hVTX->at(i).isFake() ) continue;
        if (hVTX->at(i).ndof()<5 ) continue;
        if (std::abs(hVTX->at(i).z())>24. ) continue;
        if (std::abs(hVTX->at(i).position().rho())>2. ) continue;
        vtxCnt += 1;
    }
    m_integerBranches["ngoodVTX"] = vtxCnt;

    edm::Handle< bool > hHBHENoise;
    iEvent.getByLabel(edm::InputTag("HBHENoiseFilterResultProducer", "HBHENoiseFilterResult"), hHBHENoise);
    if (*hHBHENoise == true) 
        m_integerBranches["HBHENoiseFilterResult"] = 1;
    else
        m_integerBranches["HBHENoiseFilterResult"] = 0;
    edm::Handle< bool > hHBHENoise2;
    iEvent.getByLabel(edm::InputTag("HBHENoiseFilterResultProducer2", "HBHENoiseFilterResult"), hHBHENoise2);
    if (*hHBHENoise2 == true) 
        m_integerBranches["HBHENoiseFilterResult2"] = 1;
    else
        m_integerBranches["HBHENoiseFilterResult2"] = 0;

    bool isMC = iEvent.eventAuxiliary().run() < 100;

    if (!isMC){ // check triggers. No trigger simulation in MC
        edm::Handle< pat::TriggerEvent > hTrgEvent;
        iEvent.getByLabel(edm::InputTag("patTriggerEvent"), hTrgEvent);

        std::map<std::string, std::vector<std::string> >::iterator itTrg = m_todoTriggers.begin();
        for (;itTrg != m_todoTriggers.end(); ++itTrg){
            bool pathFound = false;
            for (unsigned int i = 0; i < itTrg->second.size();++i){
                const pat::TriggerPath * pth = hTrgEvent->path(itTrg->second.at(i));
                if (pth){
                    pathFound = true;
                    if (pth->wasAccept()){
                        m_integerBranches[itTrg->first] = 1;
                    }
                }
                
            } // end paths iter
            if (!pathFound) m_integerBranches[itTrg->first] = -1;  // no path was found. Probably somehting wrong in config.
        } // end trigger class iter
    } // data only part end



    if (isMC) { // MC only part
        edm::Handle< std::vector<reco::GenJet> > hGJ;
        iEvent.getByLabel(edm::InputTag("ak5GenJets","","SIM"), hGJ);
        for (unsigned int i =0; i< hGJ->size();++i){
            if (hGJ->at(i).pt() < m_minGenPT) continue;
            m_vectorBranches["genJets"].push_back(hGJ->at(i).p4());

        }
    }
        

    for (unsigned int i = 0; i < m_views.size(); ++i){
        m_views[i]->fill(iEvent, iSetup);
    }
    m_tree->Fill();
}


// ------------ method called once each job just before starting event loop  ------------
void 
MNXSTreeProducer::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
MNXSTreeProducer::endJob() 
{
}

// ------------ method called when starting to processes a run  ------------
/*
void 
MNXSTreeProducer::beginRun(edm::Run const&, edm::EventSetup const&)
{
}
*/

// ------------ method called when ending the processing of a run  ------------
/*
void 
MNXSTreeProducer::endRun(edm::Run const&, edm::EventSetup const&)
{
}
*/

// ------------ method called when starting to processes a luminosity block  ------------
/*
void 
MNXSTreeProducer::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}
*/

// ------------ method called when ending the processing of a luminosity block  ------------
/*
void 
MNXSTreeProducer::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}
*/

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
MNXSTreeProducer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

bool MNXSTreeProducer::jetID(const pat::Jet & jet, const edm::Event& iEvent) {
    bool ret = true;
    if (jet.isCaloJet()) {  
        // We are doing this in a wicked way, since having jetID and jetArea in calo jets is not possible at same time (4_2 series)
        JetIDSelectionFunctor jetIDSelector( JetIDSelectionFunctor::PURE09, JetIDSelectionFunctor::LOOSE); //loose
        pat::strbitset bset = jetIDSelector.getBitTemplate();
        edm::Handle<edm::View< reco::CaloJet > > hJets;
        edm::Handle<reco::JetIDValueMap> hJetIDMap;
        iEvent.getByLabel(edm::InputTag("ak5CaloJets","","RECO"), hJets );
        iEvent.getByLabel( "ak5JetID", hJetIDMap );

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
        ret = passed;

    } else if (jet.isPFJet()) {
        pat::strbitset bs = pfJetID.getBitTemplate(); 
        ret = pfJetID(jet, bs);

    }else{
        throw "Jet type not known";

    }


    return ret;
}



reco::Candidate::LorentzVector MNXSTreeProducer::smear(const pat::Jet & jet) {
    if (!jet.genJet()){
        return jet.p4();
    }
    static float V_PF[] = {1.066, 1.191, 1.096, 1.166};
    static float E_PF[] = {1.1,  1.7, 2.3, 5.};

    static float V_calo[] = {1.088, 1.139, 1.082, 1.065};
    static float E_calo[] = {1.1,  1.7, 2.3, 5.};


    static std::vector<float> smearV_pf(V_PF, V_PF+sizeof(V_PF)/sizeof(float));
    static std::vector<float> smearE_pf(E_PF, E_PF+sizeof(E_PF)/sizeof(float));

    static std::vector<float> smearV_calo(V_calo, V_calo+sizeof(V_calo)/sizeof(float));
    static std::vector<float> smearE_calo(E_calo, E_calo+sizeof(E_calo)/sizeof(float));

    float eta = std::abs(jet.eta());
    float factor = 1;
    std::vector<float> *smearV, *smearE;
    if (jet.isCaloJet()) {
        smearV = &smearV_calo;
        smearE = &smearE_calo;

    } else if (jet.isPFJet()) {
        smearV = &smearV_pf;
        smearE = &smearE_pf;
    }
    else {
        throw "Jet type not known";
    }

    for (unsigned int i = 0; i < smearV->size(); ++i){
        if (eta < smearE->at(i)){
            factor = smearV->at(i);
            break;
        }
    }

    /*
    std::cout << "Jet: "<< jet.isPFJet() 
            << " " << jet.pt()
            << " " << jet.eta() 
            << " " << factor
            << std::endl;

   */

    /*
    if (factor < 0) {
            std::cout << "Cannot calculate factor!" 
                <<  " " << eta
                << std::endl;
            std::cout.flush();
            throw "Cannot calculate factor!";
    }*/ 
    float ptGen = jet.genJet()->pt(); // not: we check for genJet presence earlier
    float ptScaled = std::max(double(0.), double(ptGen + factor*(jet.pt()-ptGen)));
    float scale = ptScaled/jet.pt();

    //std::cout << scale << " " << jet.p4().pt() << " " << (jet.p4()*scale).pt() << std::endl;
    return jet.p4()*scale;
}


//define this as a plug-in
DEFINE_FWK_MODULE(MNXSTreeProducer);
