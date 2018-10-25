#include "CommonFSQFramework/Core/interface/PixelView.h"
#include <cmath>

#include "../interface/LineTrackingProducer.h"

#include "Geometry/TrackerGeometryBuilder/interface/TrackerGeometry.h"
#include "Geometry/Records/interface/TrackerDigiGeometryRecord.h"
#include "Geometry/CommonDetUnit/interface/GeomDet.h"

#include "DataFormats/TrackerRecHit2D/interface/SiPixelRecHitCollection.h"

#include "FWCore/Framework/interface/ESHandle.h"

#include <vector>

#include "DataFormats/BeamSpot/interface/BeamSpot.h"

using namespace std;


PixelView::PixelView(const edm::ParameterSet& iConfig, TTree * tree, edm::ConsumesCollector && iC):
EventViewBase(iConfig,  tree)
{
    iC.consumes<reco::BeamSpot >(edm::InputTag("offlineBeamSpot"));    

    m_src = iConfig.getParameter<edm::InputTag>("src");
    iC.consumes<SiPixelRecHitCollection >(m_src);
    registerVecFloat("PixelRecHitX",tree);
    registerVecFloat("PixelRecHitY",tree);
    registerVecFloat("PixelRecHitZ",tree);
}


void PixelView::fillSpecific(const edm::Event& iEvent, const edm::EventSetup& iSetup){

    // Get tracker geometry
    edm::ESHandle<TrackerGeometry> trackerHandle;
    iSetup.get<TrackerDigiGeometryRecord>().get(trackerHandle);
    const TrackerGeometry* theTracker = trackerHandle.product();

    edm::Handle<SiPixelRecHitCollection> pixelColl;
    iEvent.getByLabel(m_src, pixelColl);
    const SiPixelRecHitCollection* thePixelHits = pixelColl.product();
    
    for(SiPixelRecHitCollection::DataContainer::const_iterator recHit = thePixelHits->data().begin(); recHit!= thePixelHits->data().end(); recHit++) {
      if(recHit->isValid()){
	DetId id = recHit->geographicalId();
	LocalPoint lpos = recHit->localPosition();
	GlobalPoint p = theTracker->idToDet(id)->toGlobal(lpos);
	SiPixelRecHit::ClusterRef const & cluster = recHit->cluster();
	
	bool isFirst = true;
	unsigned int xmin=0, xmax=0, ymin=0, ymax=0;

	// eventually move to pixel(int id) interface
	const vector<SiPixelCluster::Pixel>& pixels = cluster->pixels();
	for(vector<SiPixelCluster::Pixel>::const_iterator pixel = pixels.begin(); pixel!= pixels.end(); pixel++) {
	  if(pixel->x > xmax || isFirst) xmax = pixel->x;
	  if(pixel->x < xmin || isFirst) xmin = pixel->x;
	  if(pixel->y > ymax || isFirst) ymax = pixel->y;
	  if(pixel->y < ymin || isFirst) ymin = pixel->y;
	  isFirst = false;
	}
	
	/*
	RawPixelRecHit RecHit;
	RecHit.x = p.x();
	RecHit.y = p.y();
	RecHit.z = p.z();
	RecHit.nx = int(xmax-xmin)+1;
	RecHit.ny = int(ymax-ymin)+1;
	RecHit.id = id;
	*/

	addToFVec("PixelRecHitX", p.x());
	addToFVec("PixelRecHitY", p.y());
	addToFVec("PixelRecHitZ", p.z());
	
      }
    }
}
