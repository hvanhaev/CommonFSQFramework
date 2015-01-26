// -*- C++ -*-
//
// Package:    MNTriggerAnaHLTJECOnFly
// Class:      MNTriggerAnaHLTJECOnFly
// 
/**\class MNTriggerAnaHLTJECOnFly MNTriggerAnaHLTJECOnFly.cc MNTriggerStudies/MNTriggerAnaHLTJECOnFly/plugins/MNTriggerAnaHLTJECOnFly.cc

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
#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/Framework/interface/EventSetup.h"


#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "TTree.h"

#include "DataFormats/PatCandidates/interface/Jet.h"
#include <DataFormats/PatCandidates/interface/TriggerEvent.h>

#include "MNTriggerStudies/MNTriggerAna/interface/EventIdData.h"
#include "MNTriggerStudies/MNTriggerAna/interface/JetView.h"

#include "MNTriggerStudies/MNTriggerAna/interface/L1JetsView.h"
#include "MNTriggerStudies/MNTriggerAna/interface/TriggerResultsView.h"


#include "CondFormats/JetMETObjects/interface/JetCorrectionUncertainty.h"
#include "JetMETCorrections/Objects/interface/JetCorrectionsRecord.h"
#include "CondFormats/JetMETObjects/interface/JetCorrectorParameters.h"
#include "CondFormats/JetMETObjects/interface/FactorizedJetCorrector.h"

//
// class declaration
//

class MNTriggerAnaHLTJECOnFly : public edm::EDAnalyzer {
   public:
      explicit MNTriggerAnaHLTJECOnFly(const edm::ParameterSet&);
      ~MNTriggerAnaHLTJECOnFly();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);


   private:
      void resetTrees();
      virtual void beginJob();
      virtual void analyze(const edm::Event&, const edm::EventSetup&);
      virtual void endJob();

      TTree *m_tree;
      std::map<std::string, int> m_integerBranches;
      std::map<std::string, float> m_floatBranches;
      std::map<std::string, std::vector<reco::Candidate::LorentzVector> > m_vectorBranches;
      std::map<std::string, edm::InputTag> m_todoHltCollections;


      std::vector<reco::Candidate::LorentzVector> m_correctedHLTJets;

      std::vector<EventViewBase *> m_views;

      //virtual void beginRun(edm::Run const&, edm::EventSetup const&) override;
      //virtual void endRun(edm::Run const&, edm::EventSetup const&) override;
      //virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;
      //virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;

      // ----------member data ---------------------------
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
MNTriggerAnaHLTJECOnFly::MNTriggerAnaHLTJECOnFly(const edm::ParameterSet& iConfig)

{
    edm::Service<TFileService> tFileService;
    m_tree = tFileService->make<TTree>("data", "data");

    m_views.push_back(new EventIdData(iConfig, m_tree));
    m_todoHltCollections["ak4GenJets"] = edm::InputTag("ak4GenJets");
    m_todoHltCollections["hltAK4PFJets"] = edm::InputTag("hltAK4PFJets");
    m_todoHltCollections["hltAK4PFJetsCorrected"]  = edm::InputTag("hltAK4PFJetsCorrected", "", "TEST");
    std::map<std::string, edm::InputTag>::iterator it = m_todoHltCollections.begin();
    for (;it != m_todoHltCollections.end(); ++it){
        m_vectorBranches[it->first] =  std::vector<reco::Candidate::LorentzVector>();
    }

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


    // vector branches autoreg
    {   
        std::map<std::string, std::vector<reco::Candidate::LorentzVector> >::iterator it =  m_vectorBranches.begin();
        std::map<std::string, std::vector<reco::Candidate::LorentzVector> >::iterator itE =  m_vectorBranches.end();
        for (;it != itE;++it){
            m_tree->Branch(it->first.c_str(), &it->second);//#;, (it->first+"/I").c_str());
        }
        m_tree->Branch("hlt_EcalMultifit_HCALMethod2", &m_correctedHLTJets);//#;, (it->first+"/I").c_str());
    }



}
void MNTriggerAnaHLTJECOnFly::resetTrees(){

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
        m_correctedHLTJets.clear();
    }




}

MNTriggerAnaHLTJECOnFly::~MNTriggerAnaHLTJECOnFly()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called for each event  ------------
void
MNTriggerAnaHLTJECOnFly::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
    resetTrees();
    using namespace edm;
    float minPT = 5;


    for (unsigned int i = 0; i < m_views.size(); ++i){
        m_views[i]->fill(iEvent, iSetup);
    }

    //std::cout << "---" << std::endl;
    std::map<std::string, edm::InputTag>::iterator it = m_todoHltCollections.begin();
    for (;it != m_todoHltCollections.end(); ++it){
        edm::Handle< edm::View<reco::Candidate> > hHLTJets;
        iEvent.getByLabel(it->second, hHLTJets);
        for (unsigned int i = 0; i<hHLTJets->size(); ++i) {
            if (hHLTJets->at(i).pt() <  minPT) continue;
            m_vectorBranches[it->first].push_back(hHLTJets->at(i).p4());
        }
        //std::cout << hHLTJets->size() << " " << m_vectorBranches[it->first].size() << std::endl;
    }   

   edm::ESHandle<JetCorrectorParametersCollection> parameters;
   //iSetup.get<JetCorrectionsRecord>().get(mPayloadName, parameters);
   iSetup.get<JetCorrectionsRecord>().get("AK4PFTMF", parameters);

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
    iEvent.getByLabel(edm::InputTag("hltFixedGridRhoFastjetAll"), hRho);
    double rho = *hRho;

    edm::Handle< std::vector<reco::PFJet> > hHLTJets;
    iEvent.getByLabel(m_todoHltCollections["hltAK4PFJets"], hHLTJets);
    for (unsigned int i = 0; i<hHLTJets->size(); ++i) {
        if (hHLTJets->at(i).pt() <  minPT) continue;
        corrector->setJetEta(hHLTJets->at(i).eta());
        corrector->setJetPt(hHLTJets->at(i).pt());
        corrector->setJetE(hHLTJets->at(i).p4().E());
        corrector->setJetA(hHLTJets->at(i).jetArea());
        corrector->setRho(rho);
        double jec = corrector->getCorrection();
        if (jec < 0) {
            std::cout << "XXX Warning: correction < 0\n";
            jec = 0;
            std::cout << hHLTJets->at(i).eta()
                    << " pt " << hHLTJets->at(i).pt()
                    << " area " << hHLTJets->at(i).jetArea()
                    << " rho " << rho
                    << " cor " << jec
                    << " ptcor " << (jec*hHLTJets->at(i).p4()).pt()
                    << std::endl;
        }
        m_correctedHLTJets.push_back(jec*hHLTJets->at(i).p4());
        //m_vectorBranches[it->first].push_back(hHLTJets->at(i).p4());
    }





    // TODO: save rho
    // TODO: apply JEC and save

    m_tree->Fill();

}


// ------------ method called once each job just before starting event loop  ------------
void 
MNTriggerAnaHLTJECOnFly::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
MNTriggerAnaHLTJECOnFly::endJob() 
{
}

// ------------ method called when starting to processes a run  ------------
/*
void 
MNTriggerAnaHLTJECOnFly::beginRun(edm::Run const&, edm::EventSetup const&)
{
}
*/

// ------------ method called when ending the processing of a run  ------------
/*
void 
MNTriggerAnaHLTJECOnFly::endRun(edm::Run const&, edm::EventSetup const&)
{
}
*/

// ------------ method called when starting to processes a luminosity block  ------------
/*
void 
MNTriggerAnaHLTJECOnFly::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}
*/

// ------------ method called when ending the processing of a luminosity block  ------------
/*
void 
MNTriggerAnaHLTJECOnFly::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}
*/

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
MNTriggerAnaHLTJECOnFly::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}




//define this as a plug-in
DEFINE_FWK_MODULE(MNTriggerAnaHLTJECOnFly);
