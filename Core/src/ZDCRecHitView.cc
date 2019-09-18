#include "CommonFSQFramework/Core/interface/ZDCRecHitView.h"

// HCAL Rechit
#include "DataFormats/Common/interface/Handle.h"
//#include "DataFormats/HcalRecHit/interface/HcalRecHitCollections.h"
//#include "DataFormats/HcalRecHit/interface/HcalSourcePositionData.h"
#include "DataFormats/HcalDetId/interface/HcalSubdetector.h"
#include "Geometry/CaloGeometry/interface/CaloGeometry.h"
//#include "CalibFormats/HcalObjects/interface/HcalDbRecord.h"
#include "Geometry/Records/interface/CaloGeometryRecord.h"
//#include "CalibFormats/HcalObjects/interface/HcalDbService.h"
#include "DataFormats/HcalRecHit/interface/HFRecHit.h"
#include "DataFormats/GeometryVector/interface/GlobalPoint.h"

#include "CalibFormats/HcalObjects/interface/HcalCoderDb.h"
#include "CalibFormats/HcalObjects/interface/HcalDbService.h"
#include "CalibFormats/HcalObjects/interface/HcalDbRecord.h"
#include "CalibCalorimetry/HcalAlgos/interface/HcalPulseShapes.h"
#include "Geometry/Records/interface/HcalRecNumberingRecord.h"


// Calibration constants for negative side
double WEIGHT[2][5] = {
                       {0.19427,0.19427,0.19427,0.19427,0.19427},
                       {1.49397,0.95613,0.40337,0.34362,0.0} 
                      };

ZDCRecHitView::ZDCRecHitView(const edm::ParameterSet& iConfig, TTree * tree, edm::ConsumesCollector && iC):
EventViewBase(iConfig,  tree){
    // register data access
    m_inputlabel = iConfig.getParameter<edm::InputTag>("inputcoll");
    iC.consumes< edm::SortedCollection<ZDCDataFrame,edm::StrictWeakOrdering<ZDCDataFrame> > >(m_inputlabel);

    registerVecFloat("Energy", tree);
    registerVecInt("Zside", tree);   // +/-1 for ZDC+/-
    registerVecInt("Section", tree); // 1 for EM, 2 for HAD
    registerVecInt("Channel", tree); // 1-5 for EM, 1-4 for HAD
}


void ZDCRecHitView::fillSpecific(const edm::Event& iEvent, const edm::EventSetup& iSetup){

  iSetup.get < HcalDbRecord > ().get(fConditions);
  edm::ESHandle < CaloGeometry > caloGeom;
  iSetup.get < CaloGeometryRecord > ().get(caloGeom);
  edm::Handle<edm::SortedCollection<ZDCDataFrame,edm::StrictWeakOrdering<ZDCDataFrame> > > zdcDigis;
  iEvent.getByLabel(m_inputlabel, zdcDigis); // specifically ask that the product instance name is an empty string to get correct collection
     
  for (ZDCDigiCollection::const_iterator it = zdcDigis->begin(); it != zdcDigis->end(); it++) {	  
    // fix emap mistakes (only on neg side now)
    addToIVec("Zside", it->id().zside());
    bool remap = false;
    if(it->id().zside() == -1){
      // EM-5 => EM-4
      if(it->id().section() == 1 && it->id().channel() == 5){
	remap = true;
        addToIVec("Section", 1);
	addToIVec("Channel", 4);
	addToFVec("Energy", getEnergy(it,1,4));
      }
      // HAD-1 => EM-5
      else if(it->id().section() == 2 && it->id().channel() == 1){
	remap = true;
        addToIVec("Section", 1);
	addToIVec("Channel", 5);
	addToFVec("Energy", getEnergy(it,1,5));
      }
      // EM-4 => HAD-1
      else if(it->id().section() == 1 && it->id().channel() == 4){
	remap = true;
        addToIVec("Section", 2);
	addToIVec("Channel", 1);
	addToFVec("Energy", getEnergy(it,2,1));
      }
    }
    if (!remap) {
      addToIVec("Section", it->id().section());
      addToIVec("Channel", it->id().channel());
      addToFVec("Energy", getEnergy(it,it->id().section(),it->id().channel()));
    }
  }
}

float ZDCRecHitView::getEnergy(ZDCDigiCollection::const_iterator it, int section, int channel){
  const HcalQIECoder* qiecoder = fConditions->getHcalCoder(it->id());
  const HcalQIEShape* qieshape = fConditions->getHcalShape(qiecoder);
  HcalCoderDb coder(*qiecoder, *qieshape);
  CaloSamples caldigi;
  coder.adc2fC(*it,caldigi);

  return WEIGHT[section-1][channel-1] * (caldigi[3] - 0.5 * (caldigi[2]+caldigi[6]) );
}
