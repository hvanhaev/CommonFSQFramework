#include "CommonFSQFramework/Core/interface/HBHERecHitView.h"

HBHERecHitView::HBHERecHitView(const edm::ParameterSet& iConfig, TTree * tree):
EventViewBase(iConfig,  tree)
{

    registerVecFloat("energy", tree);
    registerVecFloat("time", tree);
    registerVecInt("ieta", tree);
    registerVecInt("iphi", tree);
    registerVecInt("depth", tree);
}


void HBHERecHitView::fillSpecific(const edm::Event& iEvent, const edm::EventSetup& iSetup){


     edm::Handle<HBHERecHitCollection> hbheRecHits;
     iEvent.getByLabel("hbhereco","",hbheRecHits); // specifically ask that the product instance name is an empty string to get correct collection
     
     for (HBHERecHitCollection::const_iterator j = hbheRecHits->begin(); j != hbheRecHits->end(); j++) {
	addToFVec("energy", j->energy());
	addToFVec("time", j->time());
	addToIVec("ieta", j->id().ieta());
	addToIVec("iphi", j->id().iphi());
	addToIVec("depth", j->id().depth());
     }
}
