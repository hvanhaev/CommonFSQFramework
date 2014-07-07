#include "MNTriggerStudies/MNTriggerAna/interface/RecoTrackView.h"
#include <DataFormats/TrackReco/interface/Track.h>

RecoTrackView::RecoTrackView(const edm::ParameterSet& iConfig, TTree * tree){
    registerVecP4("recoTracks", tree);

    m_maxEta = iConfig.getParameter<double>("maxEta");
    m_minPt = iConfig.getParameter<double>("minPt");
    m_inputCol = iConfig.getParameter<edm::InputTag>("tracks");
}


void RecoTrackView::fill(const edm::Event& iEvent, const edm::EventSetup& iSetup){
    edm::Handle<std::vector<reco::Track> > hIn;
    iEvent.getByLabel(m_inputCol, hIn);
    for (unsigned int i = 0; i< hIn->size();++i){
        if (hIn->at(i).pt() < m_minPt ) continue;
        if (std::abs(hIn->at(i).eta()) > m_maxEta ) continue;
        double px = hIn->at(i).px();
        double py = hIn->at(i).py();
        double pz = hIn->at(i).pz();
        double E = px*px + py*py + pz*pz;

        addToP4Vec("recoTracks", reco::Candidate::LorentzVector(px,py,pz,E));

    }

}
