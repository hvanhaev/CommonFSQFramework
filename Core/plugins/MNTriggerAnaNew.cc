// -*- C++ -*-
//
// Package:    MNTriggerAnaNew
// Class:      MNTriggerAnaNew
// 
/**\class MNTriggerAnaNew MNTriggerAnaNew.cc MNTriggerStudies/MNTriggerAnaNew/plugins/MNTriggerAnaNew.cc

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
#include <DataFormats/PatCandidates/interface/TriggerEvent.h>

#include "MNTriggerStudies/MNTriggerAna/interface/EventIdData.h"
#include "MNTriggerStudies/MNTriggerAna/interface/JetView.h"
#include "MNTriggerStudies/MNTriggerAna/interface/JetsJEC.h"

#include "MNTriggerStudies/MNTriggerAna/interface/L1JetsView.h"
#include "MNTriggerStudies/MNTriggerAna/interface/GenericCandidateViewP4.h"
#include "MNTriggerStudies/MNTriggerAna/interface/TriggerResultsView.h"
//
// class declaration
//

class MNTriggerAnaNew : public edm::EDAnalyzer {
   public:
      explicit MNTriggerAnaNew(const edm::ParameterSet&);
      ~MNTriggerAnaNew();

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
MNTriggerAnaNew::MNTriggerAnaNew(const edm::ParameterSet& iConfig)

{
    edm::Service<TFileService> tFileService;
    m_tree = tFileService->make<TTree>("data", "data");

    m_views.push_back(new EventIdData(iConfig, m_tree));
    //*
    //
    if (iConfig.exists("recoPFAK4ChsCorrected")){
        m_views.push_back(new JetsJEC(iConfig.getParameter< edm::ParameterSet >("recoPFAK4ChsCorrected"), m_tree));
    } else {
        std::cout << "Disabling recoPFAK4ChsCorrected" << std::endl;
    }
    if (iConfig.exists("recoPFAK4ChsCorrectedMyRho")){
        m_views.push_back(new JetsJEC(iConfig.getParameter< edm::ParameterSet >("recoPFAK4ChsCorrectedMyRho"), m_tree));
    } else {
        std::cout << "Disabling recoPFAK4ChsCorrectedMyRho" << std::endl;
    }


    if (iConfig.exists("JetViewCalo"))
    {
        m_views.push_back(new JetView(iConfig.getParameter< edm::ParameterSet >("JetViewCalo"), m_tree));
    } else {
        std::cout << "Disabling JetViewCalo" << std::endl;
    }
    //m_views.push_back(new JetView(iConfig.getParameter< edm::ParameterSet >("JetViewPF"), m_tree));
    if (iConfig.exists("JetViewPFAK4CHS")){
        m_views.push_back(new JetView(iConfig.getParameter< edm::ParameterSet >("JetViewPFAK4CHS"), m_tree));
    } else {
        std::cout << "Disabling JetViewPFAK4CHS" << std::endl;
    }
    //m_views.push_back(new JetView(iConfig.getParameter< edm::ParameterSet >("JetViewPFAK5CHS"), m_tree));*/
    if (iConfig.exists("L1JetsView")){
        m_views.push_back(new L1JetsView(iConfig.getParameter< edm::ParameterSet >("L1JetsView"), m_tree));
    } else {
        std::cout << "Disabling L1JetsView (legacy l1)" << std::endl;
    }
    if (iConfig.exists("L1JetsViewStage1")){
        m_views.push_back(new L1JetsView(iConfig.getParameter< edm::ParameterSet >("L1JetsViewStage1"), m_tree));
    } else {
        std::cout << "Disabling L1JetsViewStage1 " << std::endl;
    }

    if (iConfig.exists("L1JetsViewRedone")){
        m_views.push_back(new L1JetsView(iConfig.getParameter< edm::ParameterSet >("L1JetsViewRedone"), m_tree));
    } else {
        std::cout << "Disabling L1JetsViewRedone " << std::endl;
    }

    //m_views.push_back(new L1JetsView(iConfig.getParameter< edm::ParameterSet >("L1JetsViewStage1Tau"), m_tree));
    //m_views.push_back(new L1JetsView(iConfig.getParameter< edm::ParameterSet >("L1JetsViewStage1All"), m_tree));
    if (iConfig.exists("TriggerResultsView")){
        m_views.push_back(new TriggerResultsView(iConfig.getParameter< edm::ParameterSet >("TriggerResultsView"), m_tree));
    } else {
        std::cout << "Disabling TriggerResultsView " << std::endl;
    }
    ///m_views.push_back(new JetView(iConfig.getParameter< edm::ParameterSet >("JetViewCalo"), m_tree));

    // use m_floatBranches for float values
    //  handled by views
    //m_vectorBranches["l1Jets"] = std::vector<reco::Candidate::LorentzVector>();
    //m_vectorBranches["hltJets"] = std::vector<reco::Candidate::LorentzVector>();

    //* XXX
    //std::cout << "Note: ak5 gen jet collections are temporarly disabled" << std::endl;
    //m_todoHltCollections["ak5GenJets"] = edm::InputTag("ak5GenJets", "", "SIM");
    //m_todoHltCollections["ak4GenJets"] = edm::InputTag("ak4GenJets");

    //std::cout << "Note: HLT jet collections are temporarly disabled" << std::endl;
    //"hltAK5PFJetL1FastL2L3Corrected"   ""                "PAT"
    //m_todoHltCollections["hltAK5PFJetL1FastL2L3Corrected"] = edm::InputTag("hltAK5PFJetL1FastL2L3Corrected", "", "PAT");
    
    std::vector<std::string> todoGeneric;
    todoGeneric.push_back("hltAK4PFJets");
    todoGeneric.push_back("hltAK4PFJetsCorrected");
    todoGeneric.push_back("hltAK5PFJets");
    todoGeneric.push_back("hltAK5PFJetsCorrected");
    todoGeneric.push_back("hltAK4CaloJets");
    todoGeneric.push_back("hltAK4CaloJetsCorrected");
    todoGeneric.push_back("hltAK4CaloJetsCorrectedIDPassed");
    todoGeneric.push_back("ak4GenJets");
    todoGeneric.push_back("ak5GenJets");
    for (size_t i = 0; i < todoGeneric.size(); ++i){
        if (iConfig.exists(todoGeneric.at(i))){
            std::cout << "Enabling " << todoGeneric.at(i) << std::endl;
            m_views.push_back(new GenericCandidateViewP4(iConfig.getParameter< edm::ParameterSet >(todoGeneric.at(i)), m_tree));
        } else {
            std::cout << "Disabling " << todoGeneric.at(i) << std::endl;
        }
    }


        /*
        m_todoHltCollections["hltAK4PFJets"] = edm::InputTag("hltAK4PFJets");
        m_todoHltCollections["hltAK4PFJetsCorrected"]  = edm::InputTag("hltAK4PFJetsCorrected", "", "TEST");
        //m_todoHltCollections["hltAK5PFJets"] = edm::InputTag("hltAK5PFJets", "", "TEST");
        //m_todoHltCollections["hltAK5PFJetsCorrected"]  = edm::InputTag("hltAK5PFJetsCorrected", "", "TEST");
        m_todoHltCollections["hltAK4CaloJets"]  = edm::InputTag("hltAK4CaloJets", "", "TEST");
        m_todoHltCollections["hltAK4CaloJetsCorrected"]  = edm::InputTag("hltAK4CaloJetsCorrected", "", "TEST");
        m_todoHltCollections["hltAK4CaloJetsCorrectedIDPassed"]  = edm::InputTag("hltAK4CaloJetsCorrectedIDPassed", "", "TEST");*/


        //#m_todoHltCollections["hltPFJetsCorrectedMatchedToL1"]  = edm::InputTag("hltPFJetsCorrectedMatchedToL1", "", "TEST");
        //*/


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
    }



}
void MNTriggerAnaNew::resetTrees(){

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




}

MNTriggerAnaNew::~MNTriggerAnaNew()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called for each event  ------------
void
MNTriggerAnaNew::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
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


    m_tree->Fill();

}


// ------------ method called once each job just before starting event loop  ------------
void 
MNTriggerAnaNew::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
MNTriggerAnaNew::endJob() 
{
}

// ------------ method called when starting to processes a run  ------------
/*
void 
MNTriggerAnaNew::beginRun(edm::Run const&, edm::EventSetup const&)
{
}
*/

// ------------ method called when ending the processing of a run  ------------
/*
void 
MNTriggerAnaNew::endRun(edm::Run const&, edm::EventSetup const&)
{
}
*/

// ------------ method called when starting to processes a luminosity block  ------------
/*
void 
MNTriggerAnaNew::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}
*/

// ------------ method called when ending the processing of a luminosity block  ------------
/*
void 
MNTriggerAnaNew::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}
*/

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
MNTriggerAnaNew::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}




//define this as a plug-in
DEFINE_FWK_MODULE(MNTriggerAnaNew);
