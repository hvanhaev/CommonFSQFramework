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


  
     std::vector<edm::Handle<HFRecHitCollection> > colls;
     iEvent.getManyByType(colls);
     std::vector<edm::Handle<HFRecHitCollection> >::iterator i;
     for (i=colls.begin(); i!=colls.end(); i++) {
        
       for (HFRecHitCollection::const_iterator j=(*i)->begin(); j!=(*i)->end(); j++) {
	 if (j->id().subdet() == HcalForward) {
	   
	   addToFVec("energy", j->energy());
	   addToFVec("time", j->time());
	   addToIVec("ieta", j->id().ieta());
	   addToIVec("iphi", j->id().iphi());
	   addToIVec("depth", j->id().depth());
	    }
       }
     }
}
