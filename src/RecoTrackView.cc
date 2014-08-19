#include "MNTriggerStudies/MNTriggerAna/interface/RecoTrackView.h"
#include <DataFormats/TrackReco/interface/Track.h>
#include <DataFormats/VertexReco/interface/Vertex.h>
#include "MNTriggerStudies/MNTriggerAna/interface/TestTrackData.h"



RecoTrackView::RecoTrackView(const edm::ParameterSet& iConfig, TTree * tree):
EventViewBase(iConfig,  tree)
{
    registerVecP4("recoTracks", tree);
    registerVecFloat("dz", tree);
    registerVecFloat("dxy", tree);

    m_maxEta = iConfig.getParameter<double>("maxEta");
    m_minPt = iConfig.getParameter<double>("minPt");
    m_maxDZ = iConfig.getParameter<double>("maxDZ");


    m_inputCol = iConfig.getParameter<edm::InputTag>("tracks");

    m_testTrackData[getPrefix()+"testTrkData"] = std::vector<tmf::TestTrackData>();
    tree->Branch((getPrefix()+"testTrkData").c_str(), "std::vector< tmf::TestTrackData >", &m_testTrackData[getPrefix()+"testTrkData"]);



    

}
void RecoTrackView::resetLocal(){
    std::map<std::string, std::vector<tmf::TestTrackData> >::iterator it, itE;
    it = m_testTrackData.begin();
    itE = m_testTrackData.end();
    for (; it!= itE; ++it){
        it->second.clear();
    }

}



void RecoTrackView::fillSpecific(const edm::Event& iEvent, const edm::EventSetup& iSetup){
    resetLocal();

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
        if (std::abs(dz)  > m_maxDZ) continue;
        float dxy = hIn->at(i).dxy( hVtx->at(bestVtx).position() );

        double px = hIn->at(i).px();
        double py = hIn->at(i).py();
        double pz = hIn->at(i).pz();
        double E = px*px + py*py + pz*pz;

        // Note: all fills (below) should be done consistently after all cuts are applied
        addToP4Vec("recoTracks", reco::Candidate::LorentzVector(px,py,pz,E));
        addToFVec("dxy", dxy);
        addToFVec("dz", dz);
        tmf::TestTrackData t;
        t.dxy = dxy;
        t.dz = dz;
        m_testTrackData[getPrefix()+"testTrkData"].push_back(t);
        


    }

}
