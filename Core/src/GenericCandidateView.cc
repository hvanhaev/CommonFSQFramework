#include "CommonFSQFramework/Core/interface/GenericCandidateView.h"
#include "DataFormats/L1Trigger/interface/L1JetParticle.h"

GenericCandidateView::GenericCandidateView(const edm::ParameterSet& iConfig, TTree * tree, edm::ConsumesCollector && iC):
EventViewBase(iConfig,  tree)
{
    registerVecFloat("pt", tree);
    registerVecFloat("eta", tree);
    registerVecFloat("phi", tree);
    m_todo = iConfig.getParameter< std::vector<edm::InputTag > >("src");

    // register consumes
    for (unsigned int i = 0; i < m_todo.size();++i) 
        iC.consumes<edm::View<reco::Candidate> >(m_todo.at(i));
}


void GenericCandidateView::fillSpecific(const edm::Event& iEvent, const edm::EventSetup& iSetup){


    for (unsigned int i = 0; i < m_todo.size();++i){
        edm::Handle<edm::View<reco::Candidate> > handle;
        iEvent.getByLabel(m_todo.at(i), handle);
        for (unsigned i = 0; i< handle->size();++i){
                addToFVec("pt", handle->at(i).pt());
                addToFVec("eta", handle->at(i).eta());
                addToFVec("phi", handle->at(i).phi());
        }
    }
}
