#include "MNTriggerStudies/MNTriggerAna/interface/JetsJEC.h"

#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/Framework/interface/EventSetup.h"

#include "CondFormats/JetMETObjects/interface/JetCorrectionUncertainty.h"
#include "JetMETCorrections/Objects/interface/JetCorrectionsRecord.h"
#include "CondFormats/JetMETObjects/interface/JetCorrectorParameters.h"
#include "CondFormats/JetMETObjects/interface/FactorizedJetCorrector.h"

#include "DataFormats/PatCandidates/interface/Jet.h"
#include <algorithm>

JetsJEC::JetsJEC(const edm::ParameterSet& iConfig, TTree * tree):
EventViewBase(iConfig,  tree)
{
    std::cout << "Warning: this view is of specific use and lacks many features present in the standard view for jets - the JetView\n" ;
    registerVecP4("p4", tree);
    m_todo =    iConfig.getParameter< edm::InputTag  >("src");
    m_rho =    iConfig.getParameter< edm::InputTag  >("rho");
    m_label = iConfig.getParameter< std::string >("label");

}

namespace xxx{
    bool ptSort(const reco::Candidate::LorentzVector & p1, 
                const reco::Candidate::LorentzVector & p2) {
        return p1.pt() > p2.pt();
    }
}


void JetsJEC::fillSpecific(const edm::Event& iEvent, const edm::EventSetup& iSetup){

   edm::ESHandle<JetCorrectorParametersCollection> parameters;
   //iSetup.get<JetCorrectionsRecord>().get(mPayloadName, parameters);
   iSetup.get<JetCorrectionsRecord>().get(m_label, parameters);

   std::vector<std::string> todo;
   todo.push_back("L1FastJet");
   todo.push_back("L2Relative");
   todo.push_back("L3Absolute");
   std::vector<JetCorrectorParameters> params;
   for(std::vector<std::string>::const_iterator level=todo.begin(); level!=todo.end(); ++level){
     const JetCorrectorParameters& ip = (*parameters)[*level]; //ip.printScreen();
     ///std::cout << "Adding level " << *level << std::endl;
     params.push_back(ip);
   }
   boost::shared_ptr<FactorizedJetCorrector> corrector ( new FactorizedJetCorrector(params));

    edm::Handle<double> hRho;
    iEvent.getByLabel(m_rho, hRho);
    double rho = *hRho;

    edm::Handle< std::vector<reco::PFJet> > hJets;
    iEvent.getByLabel(m_todo, hJets);
    for (unsigned int i = 0; i<hJets->size(); ++i) {
        if (std::abs(hJets->at(i).eta()) >  5.) continue; // TODO
        corrector->setJetEta(hJets->at(i).eta());
        corrector->setJetPt(hJets->at(i).pt());
        corrector->setJetE(hJets->at(i).p4().E());
        corrector->setJetA(hJets->at(i).jetArea());
        corrector->setRho(rho);
        double jec = corrector->getCorrection();
        if (jec < 0) {
            std::cout << "XXX Warning: correction < 0\n";
            jec = 0;
            std::cout << hJets->at(i).eta()
                    << " pt " << hJets->at(i).pt()
                    << " area " << hJets->at(i).jetArea()
                    << " rho " << rho
                    << " cor " << jec
                    << " ptcor " << (jec*hJets->at(i).p4()).pt()
                    << std::endl;
        }
        if (jec*hJets->at(i).pt() <  3) continue; // TODO
        addToP4Vec("p4", jec*hJets->at(i).p4());
    }
    std::sort(getP4VecStore("p4").begin(), getP4VecStore("p4").end(), xxx::ptSort);
    /*
    std::cout << getP4VecStore("p4").at(0).pt()
              << " " << getP4VecStore("p4").at(1).pt()
              << std::endl;
    // */
    //while (getP4VecStore("p4").size() > 3) getP4VecStore("p4").pop_back();
}

