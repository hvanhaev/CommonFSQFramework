#include "MNTriggerStudies/MNTriggerAna/interface/L1JetsView.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"

L1JetsView::L1JetsView(const edm::ParameterSet& iConfig, TTree * tree):
EventViewBase(iConfig,  tree)
{
    registerVecP4("L1Jets", tree);
}


void L1JetsView::fillSpecific(const edm::Event& iEvent, const edm::EventSetup& iSetup){

}
