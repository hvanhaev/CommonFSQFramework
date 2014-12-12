#include "MNTriggerStudies/MNTriggerAna/interface/GenericCandidateView.h"
#include "DataFormats/L1Trigger/interface/L1JetParticle.h"

GenericCandidateView::GenericCandidateView(const edm::ParameterSet& iConfig, TTree * tree):
EventViewBase(iConfig,  tree)
{
    registerVecP4("L1Jets", tree);
    m_todo = iConfig.getParameter< std::vector<edm::InputTag > >("src");
}


void GenericCandidateView::fillSpecific(const edm::Event& iEvent, const edm::EventSetup& iSetup){


    for (unsigned int i = 0; i < m_todo.size();++i){
        edm::Handle<std::vector<l1extra::L1JetParticle> > hL1;
        iEvent.getByLabel(m_todo.at(i), hL1);
        for (unsigned iL1 = 0; iL1< hL1->size();++iL1){
            if (hL1->at(iL1).bx()!=0){
                std::cout << "Warningn!  L1 cand with bx!=0: " << hL1->at(iL1).pt() << " " << hL1->at(iL1).bx() << std::endl;
            } else {
                addToP4Vec("L1Jets", hL1->at(iL1).p4());
            }
        }
    }


}
