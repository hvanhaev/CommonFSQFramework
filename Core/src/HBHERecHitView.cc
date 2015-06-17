#include "CommonFSQFramework/Core/interface/HBHERecHitView.h"

HBHERecHitView::HBHERecHitView(const edm::ParameterSet& iConfig, TTree * tree):
EventViewBase(iConfig,  tree)
{

    registerVecFloat("energy", tree);
    registerVecFloat("Et", tree);
    registerVecFloat("time", tree);
    registerVecInt("ieta", tree);
    registerVecInt("iphi", tree);
    registerVecInt("depth", tree);
    registerVecFloat("eta", tree);
    registerVecFloat("phi", tree);
}


void HBHERecHitView::fillSpecific(const edm::Event& iEvent, const edm::EventSetup& iSetup){

     //For ETA - PHI info
     iSetup.get < HcalDbRecord > ().get(conditions);
     edm::ESHandle < CaloGeometry > caloGeom;
     iSetup.get < CaloGeometryRecord > ().get(caloGeom);
     fGeo = caloGeom.product();

     edm::Handle<HBHERecHitCollection> hbheRecHits;
     iEvent.getByLabel("hbhereco","",hbheRecHits); // specifically ask that the product instance name is an empty string to get correct collection
     
     for (HBHERecHitCollection::const_iterator j = hbheRecHits->begin(); j != hbheRecHits->end(); j++) {
        GlobalPoint fPos = fGeo->getPosition(j->id());    //For ETA - PHI info
	addToFVec("energy", j->energy());
        addToFVec("Et",(j->energy()/(TMath::CosH(fPos.eta()))));
	addToFVec("time", j->time());
	addToIVec("ieta", j->id().ieta());
	addToIVec("iphi", j->id().iphi());
	addToIVec("depth", j->id().depth());
        addToFVec("eta", fPos.eta());
        addToFVec("phi",fPos.phi());
     }
}
