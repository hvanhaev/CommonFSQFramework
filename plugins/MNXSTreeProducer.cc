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
//
// class declaration
//

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

      TTree *m_tree;
      std::map<std::string, int> m_integerBranches;
      std::map<std::string, float> m_floatBranches;
      std::map<std::string, std::vector<reco::Candidate::LorentzVector> > m_vectorBranches;


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
MNXSTreeProducer::MNXSTreeProducer(const edm::ParameterSet& iConfig)

{

    edm::Service<TFileService> tFileService;
    m_tree = tFileService->make<TTree>("data", "data");

    // define your branches. Registration will be made automagically
    //
    //  note: verify, that your data is filled in the tree. If you will
    //        define your variable name as m_floatBranches["leadJetPt"]
    //        and than missspell the name in the analyze method:
    //          m_floatBranches["leadJetPT"] = 123; // note the wrong case in PT/Pt
    //        program will continue to run not filling your variable
    //
    // use m_integerBranches for integer values
    m_integerBranches["run"] = 0;
    m_integerBranches["lumi"] = 0;
    m_integerBranches["event"] = 0;

    // use m_floatBranches for float values
    m_floatBranches["leadJetPt"] = 0;
    m_floatBranches["leadJetEta"] = 0;
    m_floatBranches["subleadJetPt"] = 0;
    m_floatBranches["subleadJetEta"] = 0;


    // 
    m_vectorBranches["pfJets"] = std::vector<reco::Candidate::LorentzVector>();
    m_vectorBranches["genJets"] = std::vector<reco::Candidate::LorentzVector>();

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

    m_integerBranches["run"] = iEvent.eventAuxiliary().run();
    m_integerBranches["lumi"] = iEvent.eventAuxiliary().luminosityBlock();
    m_integerBranches["event"] = iEvent.eventAuxiliary().event();

    std::map<std::string, edm::InputTag> todo;
    todo["pf"] = edm::InputTag("selectedPatJets");
    todo["calo"] = edm::InputTag("selectedPatJetsAK5Calo");

    std::map<std::string, edm::InputTag>::iterator itBegin = todo.begin(), itEnd = todo.end() ;

    
    for (;itBegin != itEnd; ++itBegin){
        edm::Handle<pat::JetCollection> hJets;
        iEvent.getByLabel(edm::InputTag("selectedPatJets"), hJets);  // TODO/Fixme - inputTag from python cfg

        float ptMin = 15;

        for (unsigned int i = 0; i<hJets->size(); ++i){
            if (hJets->at(i).pt() < ptMin) continue;
            m_vectorBranches["pfJets"].push_back(hJets->at(i).p4());
            reco::Candidate::LorentzVector genP4;
            if (hJets->at(i).genJet()){
                genP4 = hJets->at(i).genJet()->p4();
            }
            m_vectorBranches["genJets"].push_back(genP4);

            /*
            std::cout   << "Jet:"  
                        << " " <<  hJets->at(i).pt()  // by default gives you pt with JEC applied
                        << " " <<  hJets->at(i).eta() // 
                        << std::endl;
            // */
        }
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

//define this as a plug-in
DEFINE_FWK_MODULE(MNXSTreeProducer);
