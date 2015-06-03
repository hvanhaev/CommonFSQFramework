#include "CommonFSQFramework/Core/interface/CaloTowerView.h"



CaloTowerView::CaloTowerView(const edm::ParameterSet& iConfig, TTree * tree):
EventViewBase(iConfig,  tree)
{
    registerVecP4("p4", tree);
    
    registerVecFloat("emEnergy", tree);
    registerVecFloat("hadEnergy", tree);

    registerVecInt("hasEB", tree);
    registerVecInt("hasEE", tree);
    registerVecInt("hasHB", tree);
    registerVecInt("hasHE", tree);
    registerVecInt("hasHF", tree);


    m_inputCol = iConfig.getParameter<edm::InputTag>("inputcoll");
    

}


void CaloTowerView::fillSpecific(const edm::Event& iEvent, const edm::EventSetup& iSetup){

    edm::Handle<CaloTowerCollection> towers;
    iEvent.getByLabel(m_inputCol, towers);
    
    for (CaloTowerCollection::const_iterator iCT = towers->begin(); iCT != towers->end(); ++iCT) {
        
        addToP4Vec("p4", reco::Candidate::LorentzVector(iCT->px(),iCT->py(),iCT->pz(),iCT->energy()));
        addToFVec("emEnergy", iCT->emEnergy());
        addToFVec("hadEnergy", iCT->hadEnergy());

	int hasEB = 0;
	int hasEE = 0;
	int hasHB = 0;
	int hasHE = 0;
	int hasHF = 0;
	
	//-- loop over CaloTower constituents
    	for(size_t iconst = 0; iconst < iCT->constituentsSize(); iconst++) {
     
      		DetId detId = iCT->constituent(iconst);

      		if(detId.det() == DetId::Ecal) {
			EcalSubdetector ecalSubDet = (EcalSubdetector)detId.subdetId();
			if (ecalSubDet == EcalBarrel) hasEB = 1;
			if (ecalSubDet == EcalEndcap) hasEE = 1;
      		}

      		if(detId.det() == DetId::Hcal) {
			HcalDetId hcalDetId(detId);
			if (hcalDetId.subdet() == HcalBarrel) hasHB = 1;
			if (hcalDetId.subdet() == HcalEndcap) hasHE = 1;
			if (hcalDetId.subdet() == HcalForward) hasHF = 1;
      		} 

    	}
	
	addToIVec("hasEB",hasEB);
	addToIVec("hasEE",hasEE);
	addToIVec("hasHB",hasHB);
	addToIVec("hasHE",hasHE);
	addToIVec("hasHF",hasHF);

    }

}
