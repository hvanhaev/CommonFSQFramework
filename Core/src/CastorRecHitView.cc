#include "CommonFSQFramework/Core/interface/CastorRecHitView.h"
#include "DataFormats/HcalRecHit/interface/CastorRecHit.h"
#include "DataFormats/HcalRecHit/interface/HcalRecHitCollections.h"

CastorRecHitView::CastorRecHitView(const edm::ParameterSet& iConfig, TTree * tree):
EventViewBase(iConfig,  tree)
{
   registerVecFloat("Energy", tree);
   registerVecInt("Sector", tree);
   registerVecInt("Module", tree);
}

void CastorRecHitView::fillSpecific(const edm::Event& iEvent, const edm::EventSetup& iSetup){

   edm::Handle< edm::SortedCollection<CastorRecHit,edm::StrictWeakOrdering<CastorRecHit> > > castorRecHits;
   iEvent.getByLabel("castorreco",castorRecHits);  

   // add rechits to tree
    for (unsigned int iRecHit=0; iRecHit < castorRecHits->size(); ++iRecHit) {
        CastorRecHit rh = (*castorRecHits)[iRecHit];
        addToFVec("Energy", rh.energy());
        addToIVec("Sector", rh.id().sector());
        addToIVec("Module", rh.id().module());
    }
}
