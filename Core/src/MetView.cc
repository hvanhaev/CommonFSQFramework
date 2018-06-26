#include "CommonFSQFramework/Core/interface/MetView.h"
#include "DataFormats/Common/interface/Handle.h"
#include "DataFormats/PatCandidates/interface/MET.h"

MetView::MetView(const edm::ParameterSet& iConfig, TTree * tree, edm::ConsumesCollector && iC):
EventViewBase(iConfig,  tree)
{
    // register branches
    registerVecFloat("met", tree);
    registerVecFloat("mphi", tree);
    // fetch config data
    m_Met = iConfig.getParameter<edm::InputTag>("input");

    // register consumes
    iC.consumes<pat::METCollection>(m_Met);
}


void MetView::fillSpecific(const edm::Event& iEvent, const edm::EventSetup& iSetup){

    edm::Handle<pat::METCollection> pfmet;
    iEvent.getByLabel(m_Met, pfmet); 
    for (unsigned int i = 0; i< pfmet->size();++i){
        addToFVec("met", pfmet->at(i).et());
        addToFVec("mphi", pfmet->at(i).phi());
    }
}
