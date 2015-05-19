#include "CommonFSQFramework/Core/interface/CastorRecHitView.h"
#include "DataFormats/HcalRecHit/interface/CastorRecHit.h"
#include "DataFormats/HcalRecHit/interface/HcalRecHitCollections.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "CondFormats/CastorObjects/interface/CastorChannelQuality.h"
#include "CondFormats/CastorObjects/interface/CastorChannelStatus.h"
#include "CondFormats/DataRecord/interface/CastorChannelQualityRcd.h"

CastorRecHitView::CastorRecHitView(const edm::ParameterSet& iConfig, TTree * tree):
EventViewBase(iConfig,  tree)
{
   registerVecFloat("Energy", tree);
   registerVecInt("Sector", tree);
   registerVecInt("Module", tree);
   registerVecInt("isBad", tree);
}

void CastorRecHitView::fillSpecific(const edm::Event& iEvent, const edm::EventSetup& iSetup){

   edm::Handle< edm::SortedCollection<CastorRecHit,edm::StrictWeakOrdering<CastorRecHit> > > castorRecHits;
   iEvent.getByLabel("castorreco",castorRecHits);  

   // retrieve the channel quality lists from database
   edm::ESHandle<CastorChannelQuality> p;
   iSetup.get<CastorChannelQualityRcd>().get(p);
   std::vector<DetId> channels = p->getAllChannels();

   // add rechits to tree
    for (unsigned int iRecHit=0; iRecHit < castorRecHits->size(); ++iRecHit) {
        CastorRecHit rh = (*castorRecHits)[iRecHit];
        HcalCastorDetId castorid = rh.id();
        DetId genericID=(DetId)castorid;

        bool RechitIsBad = false;
        for (std::vector<DetId>::iterator channel = channels.begin();channel != channels.end();channel++) {
            if (channel->rawId() == genericID.rawId()) {
                // if the rechit is found in the list, mark it bad
                RechitIsBad=true;
                break;
                }
        }

        addToFVec("Energy", rh.energy());
        addToIVec("Sector", castorid.sector());
        addToIVec("Module", castorid.module());
        addToIVec("isBad", (int)RechitIsBad);

    }
}
