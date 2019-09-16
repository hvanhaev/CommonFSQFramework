#include "CommonFSQFramework/Core/interface/ZDCRecHitView.h"

// Calibration constants for negative side
double WEIGHT[2][5] = {
                       {0.19427,0.19427,0.19427,0.19427,0.19427},
                       {1.49397,0.95613,0.40337,0.34362,0.0} 
                      };

ZDCRecHitView::ZDCRecHitView(const edm::ParameterSet& iConfig, TTree * tree, edm::ConsumesCollector && iC):
EventViewBase(iConfig,  tree){
    // register data access
    iC.consumes< ZDCDigiCollection >(edm::InputTag("castorDigis",""));

    registerVecFloat("energy", tree);
    registerVecInt("zside", tree);   // +/-1 for ZDC+/-
    registerVecInt("section", tree); // 1 for EM, 2 for HAD
    registerVecInt("channel", tree); // 1-5 for EM, 1-4 for HAD
}


void ZDCRecHitView::fillSpecific(const edm::Event& iEvent, const edm::EventSetup& iSetup){

  //For ETA - PHI info
  iSetup.get < HcalDbRecord > ().get(conditions);
  edm::ESHandle < CaloGeometry > caloGeom;
  iSetup.get < CaloGeometryRecord > ().get(caloGeom);
  fGeo = caloGeom.product();
     
  edm::Handle<ZDCDigiCollection> zdcDigis;
  iEvent.getByLabel("castorDigis","",zdcDigis); // specifically ask that the product instance name is an empty string to get correct collection
     
  for (ZDCDigiCollection::const_iterator it = zdcDigis->begin(); it != zdcDigis->end(); it++) {	  
    // fix emap mistakes (only on neg side now)
    if(it->id().zside() == -1){
	    addToIVec("zside", it->id().zside());
      // EM-5 => EM-4
      if(it->id().section() == 1 && it->id().channel() == 5){
        addToIVec("section", 1);
	      addToIVec("channel", 4);
	      addToFVec("energy", getEnergy(it,1,4));
      }
      // HAD-1 => EM-5
      else if(it->id().section() == 2 && it->id().channel() == 1){
        addToIVec("section", 1);
	      addToIVec("channel", 5);
	      addToFVec("energy", getEnergy(it,1,5));
      }
      // EM-4 => HAD-1
      else if(it->id().section() == 1 && it->id().channel() == 4){
        addToIVec("section", 2);
	      addToIVec("channel", 1);
	      addToFVec("energy", getEnergy(it,2,1));
      }
      else{
        addToIVec("section", it->id().section());
	      addToIVec("channel", it->id().channel());
	      addToFVec("energy", getEnergy(it,it->id().section(),it->id().channel()));
      }
    }
  }
}

float ZDCRecHitView::getEnergy(ZDCDigiCollection::const_iterator it, int section, int channel){
  const HcalQIECoder* qiecoder = conditions->getHcalCoder(it->id());
  const HcalQIEShape* qieshape = conditions->getHcalShape(qiecoder);
  HcalCoderDb coder(*qiecoder,*qieshape);
  CaloSamples caldigi;
  coder.adc2fC(*it,caldigi);

  return WEIGHT[section-1][channel-1] * (caldigi[3] - 0.5 * (caldigi[2]+caldigi[6]) );
}
