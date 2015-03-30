#include "MNTriggerStudies/MNTriggerAna/interface/GenericCandidateViewP4.h"
#include "DataFormats/L1Trigger/interface/L1JetParticle.h"

GenericCandidateViewP4::GenericCandidateViewP4(const edm::ParameterSet& iConfig, TTree * tree):
EventViewBase(iConfig,  tree)
{
    registerVecP4("p4", tree);
    m_todo = iConfig.getParameter< std::vector<edm::InputTag > >("src");
    m_ptmin = iConfig.getParameter< double >("ptmin");
}


void GenericCandidateViewP4::fillSpecific(const edm::Event& iEvent, const edm::EventSetup& iSetup){


    for (unsigned int i = 0; i < m_todo.size();++i){
        edm::Handle<edm::View<reco::Candidate> > handle;
        iEvent.getByLabel(m_todo.at(i), handle);
        for (unsigned i = 0; i< handle->size();++i){
                if (handle->at(i).pt() > m_ptmin){
                    addToP4Vec("p4", handle->at(i).p4());
                }
        }
    }
}
