#include "CommonFSQFramework/Core/interface/EcalRecHitView.h"

EcalRecHitView::EcalRecHitView(const edm::ParameterSet& iConfig, TTree * tree):
EventViewBase(iConfig,  tree)
{

    registerVecFloat("energy", tree);
    registerVecFloat("Et", tree);
    registerVecFloat("time", tree);
    registerVecInt("ieta", tree);
    registerVecInt("iphi", tree);
    registerVecFloat("eta", tree);
    registerVecFloat("phi", tree);
}


void EcalRecHitView::fillSpecific(const edm::Event& iEvent, const edm::EventSetup& iSetup){

     edm::ESHandle<CaloGeometry> caloGeom;
     iSetup.get<CaloGeometryRecord>().get(caloGeom);
     fGeo = caloGeom.product();

     edm::Handle<EBRecHitCollection> EBRecHits;
     iEvent.getByLabel("ecalRecHit","EcalRecHitsEB",EBRecHits); 
     
     for (EcalRecHitCollection::const_iterator j = EBRecHits->begin(); j != EBRecHits->end(); j++) {
        
	EBDetId EBid = EBDetId(j->id());
	GlobalPoint fPos = fGeo->getPosition(j->id());    //For ETA - PHI info
	
	addToFVec("energy", j->energy());
        addToFVec("Et",(j->energy()/(TMath::CosH(fPos.eta()))));
	addToFVec("time", j->time());
	addToIVec("ieta", EBid.tower_ieta());
	addToIVec("iphi", EBid.tower_iphi());
        addToFVec("eta", fPos.eta());
        addToFVec("phi",fPos.phi());
	
     }
     
     
     edm::Handle<EERecHitCollection> EERecHits;
     iEvent.getByLabel("ecalRecHit","EcalRecHitsEE",EERecHits);

     for (EcalRecHitCollection::const_iterator j = EERecHits->begin(); j != EERecHits->end(); j++) {

        EEDetId EEid = EEDetId(j->id());
	GlobalPoint fPos = fGeo->getPosition(j->id());
	
	//get tower id
        edm::ESHandle<EcalTrigTowerConstituentsMap> eTTmap_;
        iSetup.get<IdealGeometryRecord>().get(eTTmap_);
        EcalTrigTowerDetId towid= (*eTTmap_).towerOf(EEid);

        addToFVec("energy", j->energy());
        addToFVec("Et",(j->energy()/(TMath::CosH(fPos.eta()))));
        addToFVec("time", j->time());
        addToIVec("ieta", towid.ieta());
        addToIVec("iphi", towid.iphi());
        addToFVec("eta", fPos.eta());
        addToFVec("phi",fPos.phi());

     }     

}
