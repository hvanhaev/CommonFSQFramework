#include "CommonFSQFramework/Core/interface/HFRecHitView.h"
#include "DataFormats/JetReco/interface/GenJet.h"

HFRecHitView::HFRecHitView(const edm::ParameterSet& iConfig, TTree * tree):
EventViewBase(iConfig,  tree)
{

    registerVecFloat("energy", tree);
    registerVecFloat("time", tree);
    registerVecInt("ieta", tree);
    registerVecInt("iphi", tree);
    registerVecInt("depth", tree);
}


void HFRecHitView::fillSpecific(const edm::Event& iEvent, const edm::EventSetup& iSetup){


     edm::Handle<HFRecHitCollection> hfRecHits;
     iEvent.getByLabel("hfreco","",hfRecHits); // specifically ask that the product instance name is an empty string to get correct collection
     
     for (HFRecHitCollection::const_iterator j = hfRecHits->begin(); j != hfRecHits->end(); j++) {
	if (j->id().subdet() == HcalForward) {
	   
	   addToFVec("energy", j->energy());
	   addToFVec("time", j->time());
	   addToIVec("ieta", j->id().ieta());
	   addToIVec("iphi", j->id().iphi());
	   addToIVec("depth", j->id().depth());
	}
     }
}
