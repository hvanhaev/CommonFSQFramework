#include "MNTriggerStudies/MNTriggerAna/interface/RecoTrackView.h"
#include <DataFormats/TrackReco/interface/Track.h>
#include <DataFormats/VertexReco/interface/Vertex.h>


RecoTrackView::RecoTrackView(const edm::ParameterSet& iConfig, TTree * tree){
    registerVecP4("recoTracks", tree);

    m_maxEta = iConfig.getParameter<double>("maxEta");
    m_minPt = iConfig.getParameter<double>("minPt");
    m_maxDZ = iConfig.getParameter<double>("maxDZ");
    

    m_inputCol = iConfig.getParameter<edm::InputTag>("tracks");
}


void RecoTrackView::fillSpecific(const edm::Event& iEvent, const edm::EventSetup& iSetup){
    edm::Handle<std::vector<reco::Vertex> > hVtx;
    iEvent.getByLabel(edm::InputTag("offlinePrimaryVerticesWithBS"), hVtx); // TODO: take from config


    float bestSum = 0;
    int bestVtx = -1;
    for (unsigned int i = 0; i< hVtx->size();++i){
        reco::Vertex::trackRef_iterator it = hVtx->at(i).tracks_begin();
        reco::Vertex::trackRef_iterator itE = hVtx->at(i).tracks_end();
        float sum= 0;
        for (;it!=itE;++it ){ // TODO: come quality criteria?
            sum+=(*it)->pt();
        }
        if (bestSum < sum){
            bestSum = sum;
            bestVtx = i;
        }
    }
    if (bestVtx < 0) return; // leaves empty tracks collection (filled below)

    edm::Handle<std::vector<reco::Track> > hIn;
    iEvent.getByLabel(m_inputCol, hIn);
    for (unsigned int i = 0; i< hIn->size();++i){
        if (hIn->at(i).pt() < m_minPt ) continue;
        if (std::abs(hIn->at(i).eta()) > m_maxEta ) continue;
        float dz = hIn->at(i).dz( hVtx->at(bestVtx).position() );
        if (dz  > m_maxDZ) continue;

        double px = hIn->at(i).px();
        double py = hIn->at(i).py();
        double pz = hIn->at(i).pz();
        double E = px*px + py*py + pz*pz;

        addToP4Vec("recoTracks", reco::Candidate::LorentzVector(px,py,pz,E));

    }

}
