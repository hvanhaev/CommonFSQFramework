#include "CommonFSQFramework/Core/interface/ZeroTeslaVertexView.h"
#include <cmath>

#include "../interface/LineTrackingProducer.h"

#include "Geometry/TrackerGeometryBuilder/interface/TrackerGeometry.h"
#include "Geometry/Records/interface/TrackerDigiGeometryRecord.h"
#include "Geometry/CommonDetUnit/interface/GeomDet.h"

#include "DataFormats/TrackerRecHit2D/interface/SiPixelRecHitCollection.h"
#include "DataFormats/TrackerRecHit2D/interface/SiStripMatchedRecHit2DCollection.h"
#include "DataFormats/TrackerRecHit2D/interface/SiStripRecHit2DCollection.h"

#include "Geometry/TrackerGeometryBuilder/interface/StripGeomDetUnit.h"

#include "FWCore/Framework/interface/ESHandle.h"

#include <vector>

#include "DataFormats/BeamSpot/interface/BeamSpot.h"

using namespace std;

struct RawPixelRecHit;
struct RawStripRecHit;

ZeroTeslaVertexView::ZeroTeslaVertexView(const edm::ParameterSet& iConfig, TTree * tree, edm::ConsumesCollector && iC):
EventViewBase(iConfig,  tree)
{
    m_usePixels = iConfig.getParameter<bool>("usePixel");
    m_src = iConfig.getParameter<edm::InputTag>("src");

    iC.consumes<reco::BeamSpot >(edm::InputTag("offlineBeamSpot"));    
    if(m_usePixels) iC.consumes<SiPixelRecHitCollection >(m_src);
    else iC.consumesMany<SiStripMatchedRecHit2DCollection >();

    registerVecFloat("PixelRecHitX",tree);
    registerVecFloat("PixelRecHitY",tree);
    registerVecFloat("PixelRecHitZ",tree);

    registerVecFloat("VtxX",tree);
    registerVecFloat("VtxY",tree);
    registerVecFloat("VtxZ",tree);
    registerVecInt("VtxNtracks", tree);    

    registerVecFloat("TrackTheta", tree);
    registerVecFloat("TrackPhi", tree);
    registerVecFloat("TrackZ0", tree);
    registerVecFloat("TrackD0", tree);
    registerVecFloat("TrackSigmaZ", tree);
	registerVecInt("TrackIvtx", tree);

}


void ZeroTeslaVertexView::fillSpecific(const edm::Event& iEvent, const edm::EventSetup& iSetup){

    // get the beamspot
    reco::BeamSpot beamSpot;
    edm::Handle<reco::BeamSpot> beamSpotHandle;
    iEvent.getByLabel("offlineBeamSpot", beamSpotHandle);
    if ( beamSpotHandle.isValid() )
    {
        beamSpot = *beamSpotHandle;
    }

    // Get tracker geometry
    edm::ESHandle<TrackerGeometry> trackerHandle;
    iSetup.get<TrackerDigiGeometryRecord>().get(trackerHandle);
    const TrackerGeometry* theTracker = trackerHandle.product();

    std::vector<RawPixelRecHit> RawPixelRecHits;
    std::vector<RawStripRecHit> RawStripRecHits;

    // get Pixel RecHits and save them in a format that the LineTrackingProducer can deal with
    if (m_usePixels) {
        edm::Handle<SiPixelRecHitCollection> pixelColl;
        iEvent.getByLabel(m_src, pixelColl);
        const SiPixelRecHitCollection* thePixelHits = pixelColl.product();

        for(SiPixelRecHitCollection::DataContainer::const_iterator recHit = thePixelHits->data().begin(); recHit!= thePixelHits->data().end(); recHit++) {
            if(recHit->isValid()){
                DetId id = recHit->geographicalId();
                LocalPoint lpos = recHit->localPosition();
                GlobalPoint p = theTracker->idToDet(id)->toGlobal(lpos);
                SiPixelRecHit::ClusterRef const & cluster = recHit->cluster();
                vector<SiPixelCluster::Pixel> pixels = cluster->pixels();
  
                bool isFirst = true;
                unsigned int xmin=0, xmax=0, ymin=0, ymax=0;
                for(vector<SiPixelCluster::Pixel>::const_iterator pixel = pixels.begin(); pixel!= pixels.end(); pixel++) {
                    if(pixel->x > xmax || isFirst) xmax = pixel->x;
                    if(pixel->x < xmin || isFirst) xmin = pixel->x;
                    if(pixel->y > ymax || isFirst) ymax = pixel->y;
                    if(pixel->y < ymin || isFirst) ymin = pixel->y;
                    isFirst = false;
                }
    
                RawPixelRecHit tmp;
                tmp.x = p.x();
                tmp.y = p.y();
                tmp.z = p.z();
                tmp.nx = int(xmax-xmin)+1;
                tmp.ny = int(ymax-ymin)+1;
                tmp.id = id;

                RawPixelRecHits.push_back(tmp);
            }
        }
    }

    // get Strip RecHits and save them in a format that the LineTrackingProducer can deal with
    if (!m_usePixels) {
        vector<edm::Handle<SiStripMatchedRecHit2DCollection> > stripColls;
        iEvent.getManyByType(stripColls);
    
        for(vector<edm::Handle<SiStripMatchedRecHit2DCollection> >::const_iterator stripColl = stripColls.begin(); stripColl!= stripColls.end(); stripColl++){
            const SiStripMatchedRecHit2DCollection* theStripHits = (*stripColl).product();
            for(SiStripMatchedRecHit2DCollection::DataContainer::const_iterator recHit = theStripHits->data().begin(); recHit!= theStripHits->data().end(); recHit++){
                DetId id = recHit->geographicalId();
                LocalPoint lpos = recHit->localPosition();
                GlobalPoint p = theTracker->idToDet(id)->toGlobal(lpos);
    
                RawStripRecHit tmp;
                tmp.x = p.x();
                tmp.y = p.y();
                tmp.z = p.z();
                tmp.monoSize = recHit->monoHit().cluster()->amplitudes().size();
                tmp.stereoSize = recHit->stereoHit().cluster()->amplitudes().size();
                tmp.monoId = recHit->monoHit().geographicalId();
                tmp.stereoId = recHit->stereoHit().geographicalId();

                RawStripRecHits.push_back(tmp);
            }
        }
    }

    // save Pixel RecHits
    if (m_usePixels) {
        for(std::vector<RawPixelRecHit>::iterator RecHit = RawPixelRecHits.begin(); RecHit != RawPixelRecHits.end(); ++RecHit){
            addToFVec("PixelRecHitX",RecHit->x);
            addToFVec("PixelRecHitY",RecHit->y);
            addToFVec("PixelRecHitZ",RecHit->z);
        }
    }

    // Calculate vertices
    LineTrackingProducer theProducer(m_usePixels, beamSpot.x0(), beamSpot.y0());
    if (m_usePixels) theProducer.run(RawPixelRecHits);
    if (!m_usePixels) theProducer.run(RawStripRecHits);

    // Get result
    std::vector<double> VerticesX, VerticesY, VerticesZ;
    std:: vector<int> VtxNtracks;
    int nVertices = theProducer.getVertices(VerticesX, VerticesY, VerticesZ, VtxNtracks);

    std::vector<double> TracksTheta, TracksPhi, TracksZ0, TracksD0, TracksSigmaZ;
    std:: vector<int> TracksiVertex;
    int nTracks = theProducer.getTracks(TracksTheta, TracksPhi, TracksZ0, TracksD0, TracksSigmaZ, TracksiVertex);

    // fill trees
    for ( int i=0; i<nVertices; i++){
    	addToFVec("VtxX",VerticesX[i]);
	    addToFVec("VtxY",VerticesY[i]);
	    addToFVec("VtxZ",VerticesZ[i]);
	    addToIVec("VtxNtracks",VtxNtracks[i]);
    }

    for ( int i=0; i<nTracks; i++){
    	addToFVec("TrackTheta",TracksTheta[i]);
	    addToFVec("TrackPhi",TracksPhi[i]);
	    addToFVec("TrackZ0",TracksZ0[i]);
	    addToFVec("TrackD0",TracksD0[i]);
	    addToFVec("TrackSigmaZ",TracksSigmaZ[i]);
	    addToIVec("TrackIvtx",TracksiVertex[i]);
    }
}
