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


    // use m_floatBranches for float values
    m_floatBranches["leadJetPt"] = 0;
    m_floatBranches["leadJetEta"] = 0;
    m_floatBranches["subleadJetPt"] = 0;
    m_floatBranches["subleadJetEta"] = 0;


    // 
    m_vectorBranches["pfJets"] = std::vector<reco::Candidate::LorentzVector>();
    m_vectorBranches["l1Jets"] = std::vector<reco::Candidate::LorentzVector>();
    //m_vectorBranches["hltJets"] = std::vector<reco::Candidate::LorentzVector>();

    m_todoHltCollections["ak5GenJets"] = edm::InputTag("ak5GenJets", "", "SIM");
    //"hltAK5PFJetL1FastL2L3Corrected"   ""                "PAT"
    //m_todoHltCollections["hltAK5PFJetL1FastL2L3Corrected"] = edm::InputTag("hltAK5PFJetL1FastL2L3Corrected", "", "PAT");
    
    m_todoHltCollections["hltAK4PFJets"] = edm::InputTag("hltAK4PFJets", "", "TTT");
    m_todoHltCollections["hltAK4PFJetsCorrected"]  = edm::InputTag("hltAK4PFJetsCorrected", "", "TTT");


    


    /*
    m_todoHltCollections["hltAntiKT5CaloJets"] = edm::InputTag("hltAntiKT5CaloJets", "", "PAT");
    m_todoHltCollections["hltAntiKT5CaloJetsRegional"] = edm::InputTag("hltAntiKT5CaloJetsRegional", "", "PAT");
    m_todoHltCollections["hltAntiKT5L2L3CorrCaloJetsL1FastJetPt60Eta2"] = edm::InputTag("hltAntiKT5L2L3CorrCaloJetsL1FastJetPt60Eta2", "", "PAT");
    m_todoHltCollections["hltCaloJetCorrected"] = edm::InputTag("hltCaloJetCorrected", "", "PAT");
    m_todoHltCollections["hltCaloJetCorrectedRegional"] = edm::InputTag("hltCaloJetCorrectedRegional", "", "PAT");
    m_todoHltCollections["hltCaloJetCorrectedRegionalNoJetID"] = edm::InputTag("hltCaloJetCorrectedRegionalNoJetID", "", "PAT");
    m_todoHltCollections["hltCaloJetL1FastJetCorrected"] = edm::InputTag("hltCaloJetL1FastJetCorrected", "", "PAT");
    m_todoHltCollections["hltAK5PFJetL1FastL2L3CorrectedNoPU"] = edm::InputTag("hltAK5PFJetL1FastL2L3CorrectedNoPU", "", "PAT");
    m_todoHltCollections["hltAntiKT5PFJets"] = edm::InputTag("hltAntiKT5PFJets", "", "PAT");
    */


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


    for (unsigned int i = 0; i < m_views.size(); ++i){
        m_views[i]->fill(iEvent, iSetup);
    }

    float minPT = 15; // TODO!



    std::map<std::string, edm::InputTag>::iterator it = m_todoHltCollections.begin();
    for (;it != m_todoHltCollections.end(); ++it){
        edm::Handle< edm::View<reco::Candidate> > hHLTJets;
        iEvent.getByLabel(it->second, hHLTJets);
        for (unsigned int i = 0; i<hHLTJets->size(); ++i) {
            if (hHLTJets->at(i).pt() <  minPT) continue;
            m_vectorBranches[it->first].push_back(hHLTJets->at(i).p4());
        }
    }


    edm::Handle<edm::View<pat::Jet> > hJets;
    iEvent.getByLabel(edm::InputTag("selectedPatJets"), hJets);  // TODO/Fixme - inputTag from python cfg
    for (unsigned int i = 0; i<hJets->size(); ++i) {
        if (hJets->at(i).pt() <  minPT) continue;
        m_vectorBranches["pfJets"].push_back(hJets->at(i).p4());

        /*
        edm::RefToBase<pat::Jet> jetRef = hJets->refAt(i);
        edm::Ref<pat::TriggerObjectCollection > hltRefVec = (*trMatches)[jetRef];

        reco::Candidate::LorentzVector hltp4;
        if (hltRefVec.isNonnull()){
            hltp4 = hltRefVec->p4();

            std::cout << "Reference came from:" << hltRefVec->collection() << std::endl;
        }

        std::cout << "J: " <<  hJets->at(i).pt() << " " << hltp4.pt() << std::endl;
        */


        /*
        std::cout   << "Jet:"  
                    << " " <<  hJets->at(i).pt()  // by default gives you pt with JEC applied
                    << " " <<  hJets->at(i).eta() // 
                    << std::endl;
        // */
    }


    //* L1extra part
    std::vector<edm::InputTag> todo;
    todo.push_back(edm::InputTag("l1extraParticles", "Central", "RECO"));
    todo.push_back(edm::InputTag("l1extraParticles", "Forward", "RECO"));
    todo.push_back(edm::InputTag("l1extraParticles", "Tau", "RECO"));
    for (unsigned int i = 0; i < todo.size();++i){
        edm::Handle<std::vector<l1extra::L1JetParticle> > hL1;
        iEvent.getByLabel(todo.at(i), hL1);
        for (unsigned iL1 = 0; iL1< hL1->size();++iL1){
            //std::cout << "L1 cand: " << hL1->at(iL1).pt() << " " << hL1->at(iL1).bx() << std::endl;
            if (hL1->at(iL1).bx()!=0){
                std::cout << "Warningn!  L1 cand with bx!=0: " << hL1->at(iL1).pt() << " " << hL1->at(iL1).bx() << std::endl;
            } else {
                m_vectorBranches["l1Jets"].push_back(hL1->at(iL1).p4());
            }
        }
    }



    // jets are pt ordered by default
    // TODO: CHECKME - this was in 4_2, shouldnt change, but who knows...
    int nJets =  hJets->size();
    if (nJets>0){
        m_floatBranches["leadJetPt"] = hJets->at(0).pt();
        m_floatBranches["leadJetEta"] = hJets->at(0).eta();
    }
    if (nJets>1){
        m_floatBranches["subleadJetPt"] = hJets->at(1).pt();
        m_floatBranches["subleadJetEta"] = hJets->at(1).eta();
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
