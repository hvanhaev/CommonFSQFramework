#include "CommonFSQFramework/Core/interface/PFCandidateView.h"



PFCandidateView::PFCandidateView(const edm::ParameterSet& iConfig, TTree * tree):
EventViewBase(iConfig,  tree)
{
    registerVecP4("p4", tree);
    registerVecFloat("rawEcalEnergy",tree);
    registerVecFloat("rawHcalEnergy",tree);
    registerVecInt("particleId", tree);


    m_inputCol = iConfig.getParameter<edm::InputTag>("inputcoll");
    

}


void PFCandidateView::fillSpecific(const edm::Event& iEvent, const edm::EventSetup& iSetup){

    edm::Handle<reco::PFCandidateCollection> pfCandidates;
    iEvent.getByLabel(m_inputCol,pfCandidates);
    
    for (reco::PFCandidateCollection::const_iterator i = pfCandidates->begin(); i != pfCandidates->end(); ++i) {
        
        addToP4Vec("p4", reco::Candidate::LorentzVector(i->px(),i->py(),i->pz(),i->energy()));
	addToFVec("rawEcalEnergy",i->rawEcalEnergy());
	addToFVec("rawHcalEnergy",i->rawHcalEnergy());
	addToIVec("particleId",i->particleId());
	

    }

}
