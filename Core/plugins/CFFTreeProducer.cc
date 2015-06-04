// -*- C++ -*-
//
// Package:    CFFTreeProducer
// Class:      CFFTreeProducer
// 
/**\class CFFTreeProducer CFFTreeProducer.cc MNTriggerStudies/CFFTreeProducer/plugins/CFFTreeProducer.cc
*/



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

#include "CommonFSQFramework/Core/interface/EventIdData.h"
#include "CommonFSQFramework/Core/interface/GenPartView.h"
#include "CommonFSQFramework/Core/interface/GenJetView.h"
#include "CommonFSQFramework/Core/interface/RecoTrackView.h"
#include "CommonFSQFramework/Core/interface/VerticesView.h"
#include "CommonFSQFramework/Core/interface/CastorRecHitView.h"
#include "CommonFSQFramework/Core/interface/CastorJetView.h"

#include "CommonFSQFramework/Core/interface/JetView.h"
#include "CommonFSQFramework/Core/interface/TriggerResultsView.h"
#include "CommonFSQFramework/Core/interface/GenericCandidateView.h"
#include "CommonFSQFramework/Core/interface/HFRecHitView.h"
#include "CommonFSQFramework/Core/interface/HBHERecHitView.h"
#include "CommonFSQFramework/Core/interface/CaloTowerView.h"
#include "CommonFSQFramework/Core/interface/PFCandidateView.h"

//
// class declaration
//

class CFFTreeProducer : public edm::EDAnalyzer {
   public:
      explicit CFFTreeProducer(const edm::ParameterSet&);
      ~CFFTreeProducer();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);


   private:
      virtual void beginJob();
      virtual void analyze(const edm::Event&, const edm::EventSetup&);
      virtual void endJob();

      TTree *m_tree;
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
CFFTreeProducer::CFFTreeProducer(const edm::ParameterSet& iConfig)

{
    edm::Service<TFileService> tFileService;
    m_tree = tFileService->make<TTree>("data", "data");

    std::vector< std::string > allParams = iConfig.getParameterNames();

    std::set< std::string> prefixes;
    for (size_t i = 0; i < allParams.size();++i){
        std::string name = allParams.at(i);
        if (name.find("@") != std::string::npos) continue; // remove some CMSSW artifacts

        if (!iConfig.existsAs<edm::ParameterSet>(name)) {
            throw "Parameter " + name + " is not a pset as expected";
        }

        edm::ParameterSet pset = iConfig.getParameter< edm::ParameterSet >(name);
        if (!pset.existsAs<std::string>("miniView")){
            throw "Provide miniView (tell me what miniView to create) in pset " +  name;
        }
        std::string miniViewType = pset.getParameter<std::string>("miniView");


        if (!pset.existsAs<std::string>("branchPrefix", false)){
            throw "Provide branchPrefix in pset " +  name;
        }

        std::string prefix = pset.getUntrackedParameter<std::string>("branchPrefix");
        if (prefixes.count(prefix)!=0)
            throw "Multiple prefixes (?) - "+prefix;

        prefixes.insert(prefix);


        if (miniViewType == "JetView") {
            m_views.push_back(new JetView(pset, m_tree));
        }
        else if (miniViewType == "TriggerResultsView") {
            m_views.push_back(new TriggerResultsView(pset, m_tree));
        }
        else if (miniViewType == "GenericCandidateView") {
            m_views.push_back(new GenericCandidateView(pset, m_tree));
        }
        else if (miniViewType == "GenPartView") {
            m_views.push_back(new GenPartView(pset, m_tree));
        }
	else if (miniViewType == "GenJetView") {
	    m_views.push_back(new GenJetView(pset, m_tree));
	}
        else if (miniViewType == "RecoTrackView") {
            m_views.push_back(new RecoTrackView(pset, m_tree));
        }
        else if (miniViewType == "VerticesView") {
            m_views.push_back(new VerticesView(pset, m_tree));
        }
        else if (miniViewType == "CastorRecHitView") {
            m_views.push_back(new CastorRecHitView(pset, m_tree));
        }
        else if (miniViewType == "CastorJetView") {
            m_views.push_back(new CastorJetView(pset, m_tree));
        }
	else if (miniViewType == "HFRecHitView") {
	    m_views.push_back(new HFRecHitView(pset, m_tree));
	}
	else if (miniViewType == "HBHERecHitView") {
            m_views.push_back(new HBHERecHitView(pset, m_tree));
        }
	else if (miniViewType == "CaloTowerView") {
            m_views.push_back(new CaloTowerView(pset, m_tree));
        }
	else if (miniViewType == "PFCandidateView") {
            m_views.push_back(new PFCandidateView(pset, m_tree));
        }
        else {
            throw "Miniview not known: "+ miniViewType;
        }

    }

    // run/event number
    m_views.push_back(new EventIdData(edm::ParameterSet(), m_tree));


}

CFFTreeProducer::~CFFTreeProducer() {}

void
CFFTreeProducer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup){

    using namespace edm;
    for (unsigned int i = 0; i < m_views.size(); ++i){
        m_views[i]->fill(iEvent, iSetup);
    }
    m_tree->Fill();

}


// ------------ method called once each job just before starting event loop  ------------
void 
CFFTreeProducer::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
CFFTreeProducer::endJob() 
{
}

// ------------ method called when starting to processes a run  ------------
/*
void 
CFFTreeProducer::beginRun(edm::Run const&, edm::EventSetup const&)
{
}
*/

// ------------ method called when ending the processing of a run  ------------
/*
void 
CFFTreeProducer::endRun(edm::Run const&, edm::EventSetup const&)
{
}
*/

// ------------ method called when starting to processes a luminosity block  ------------
/*
void 
CFFTreeProducer::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}
*/

// ------------ method called when ending the processing of a luminosity block  ------------
/*
void 
CFFTreeProducer::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}
*/

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
CFFTreeProducer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}




//define this as a plug-in
DEFINE_FWK_MODULE(CFFTreeProducer);
