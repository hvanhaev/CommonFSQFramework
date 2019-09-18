#include "CommonFSQFramework/Core/interface/RecoTrackView.h"
#include <DataFormats/TrackReco/interface/Track.h>
#include <DataFormats/VertexReco/interface/Vertex.h>
#include "CommonFSQFramework/Core/interface/TestTrackData.h"


RecoTrackView::RecoTrackView(const edm::ParameterSet& iConfig, TTree * tree, edm::ConsumesCollector && iC):
EventViewBase(iConfig,  tree)
{
    registerVecP4("P4", tree);
    registerVecFloat("Dz", tree);
    registerVecFloat("D0", tree);
    registerVecFloat("DzErr", tree);
    registerVecFloat("D0Err", tree);
    registerVecFloat("Vx", tree);
    registerVecFloat("Vy", tree);
    registerVecFloat("Vz", tree);

    registerVecInt(  "HighPurity", tree);
    registerVecInt(  "Algo", tree);
    registerVecInt(  "NValidHits", tree);
    registerVecInt(  "NLostHits", tree);
    registerVecInt(  "Charge", tree);
    registerVecFloat(  "Chi2n", tree);
    registerVecFloat(  "PtErr", tree);

    m_maxEta = iConfig.getParameter<double>("maxEta");
    m_minPt = iConfig.getParameter<double>("minPt");
    //m_maxDZ = iConfig.getParameter<double>("maxDZ");


    m_inputCol = iConfig.getParameter<edm::InputTag>("tracks");

    m_testTrackData[getPrefix()+"testTrkData"] = std::vector<tmf::TestTrackData>();
    tree->Branch((getPrefix()+"testTrkData").c_str(), "std::vector< tmf::TestTrackData >", &m_testTrackData[getPrefix()+"testTrkData"]);

    // register consumes
    iC.consumes< std::vector<reco::Vertex> >(edm::InputTag("offlinePrimaryVerticesWithBS"));
    iC.consumes< std::vector<reco::Track> >(m_inputCol);

    

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

    /* not used any more
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
    */

    edm::Handle<std::vector<reco::Track> > tracksData;
    iEvent.getByLabel(m_inputCol, tracksData);
    for (unsigned int i = 0; i< tracksData->size();++i){
        if (tracksData->at(i).pt() < m_minPt ) {
	  continue;
	}
	if (std::abs(tracksData->at(i).eta()) > m_maxEta ) {
	  continue;
	}
        // const float dz = tracksData->at(i).dz( hVtx->at(bestVtx).position() );
        const float dz = tracksData->at(i).dz();
        /*if (std::abs(dz)  > m_maxDZ) {
	  std::cout << "skip dz=" << tracksData->at(i).dz() << std::endl;
	  continue;
	  }*/
        // const float dxy = tracksData->at(i).dxy( hVtx->at(bestVtx).position() );
	const float dxy = tracksData->at(i).dxy();

        const double px = tracksData->at(i).px();
        const double py = tracksData->at(i).py();
        const double pz = tracksData->at(i).pz();
        const double E = px*px + py*py + pz*pz;

        // Note: all fills (below) should be done consistently after all cuts are applied
        addToP4Vec("P4", reco::Candidate::LorentzVector(px,py,pz,E));
        //addToFVec("Dxy", dxy);
        //addToFVec("Dz", dz);
        addToFVec("Dz", tracksData->at(i).dz());
        addToFVec("DzErr", tracksData->at(i).dzError());
        addToFVec("D0", tracksData->at(i).d0());
        addToFVec("D0Err", tracksData->at(i).d0Error());

        addToFVec("Vx", tracksData->at(i).vx());
        addToFVec("Vy", tracksData->at(i).vy());
        addToFVec("Vz", tracksData->at(i).vz());

        int highpurity = 1;
        if (!tracksData->at(i).quality(reco::TrackBase::highPurity)) highpurity = 0;
        addToIVec("HighPurity", highpurity);
        addToIVec("Algo", tracksData->at(i).algo() );
        addToIVec("NValidHits", tracksData->at(i).numberOfValidHits() );
        addToIVec("NLostHits", tracksData->at(i).numberOfLostHits() );
        addToFVec("Chi2n", tracksData->at(i).normalizedChi2() );
        addToFVec("PtErr", tracksData->at(i).ptError() );
        tmf::TestTrackData t;
        t.dxy = dxy;
        t.dz = dz;
        m_testTrackData[getPrefix()+"testTrkData"].push_back(t);
        


    }

}
