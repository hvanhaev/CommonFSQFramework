#include "MNTriggerStudies/MNTriggerAna/interface/RecoTrackView.h"
#include <DataFormats/TrackReco/interface/Track.h>
#include <DataFormats/VertexReco/interface/Vertex.h>
#include "MNTriggerStudies/MNTriggerAna/interface/TestTrackData.h"



RecoTrackView::RecoTrackView(const edm::ParameterSet& iConfig, TTree * tree):
EventViewBase(iConfig,  tree)
{
    registerVecP4("recoTracks", tree);
    registerVecFloat("dz", tree);
    registerVecFloat("d0", tree);
    registerVecFloat("dzErr", tree);
    registerVecFloat("d0Err", tree);
    registerVecFloat("vx", tree);
    registerVecFloat("vy", tree);
    registerVecFloat("vz", tree);

    registerVecInt(  "highpurity", tree);
    registerVecInt(  "algo", tree);
    registerVecInt(  "nvhits", tree);
    registerVecInt(  "nlhits", tree);
    registerVecInt(  "charge", tree);
    registerVecFloat(  "chi2n", tree);
    registerVecFloat(  "pterr", tree);

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
        //addToFVec("dxy", dxy);
        //addToFVec("dz", dz);
        addToFVec("dz", hIn->at(i).dz());
        addToFVec("dzErr", hIn->at(i).dzError());
        addToFVec("d0", hIn->at(i).d0());
        addToFVec("d0Err", hIn->at(i).d0Error());

        addToFVec("vx", hIn->at(i).vx());
        addToFVec("vy", hIn->at(i).vy());
        addToFVec("vz", hIn->at(i).vz());

        int highpurity = 1;
        if (!hIn->at(i).quality(reco::TrackBase::highPurity)) highpurity = 0;
        addToIVec("highpurity", highpurity);
        addToIVec("algo", hIn->at(i).algo() );
        addToIVec("nvhits", hIn->at(i).numberOfValidHits() );
        addToIVec("nlhits", hIn->at(i).numberOfLostHits() );
        addToFVec("chi2n", hIn->at(i).normalizedChi2() );
        addToFVec("pterr", hIn->at(i).ptError() );
        tmf::TestTrackData t;
        t.dxy = dxy;
        t.dz = dz;
        m_testTrackData[getPrefix()+"testTrkData"].push_back(t);
        


    }

}
