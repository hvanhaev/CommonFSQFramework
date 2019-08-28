#ifndef ZDCRecHitView_h
#define ZDCRecHitView_h

#include "CommonFSQFramework/Core/interface/EventViewBase.h"
// HCAL Rechit
#include "DataFormats/Common/interface/Handle.h"
//#include "DataFormats/HcalRecHit/interface/HcalRecHitCollections.h"
//#include "DataFormats/HcalRecHit/interface/HcalSourcePositionData.h"
#include "DataFormats/HcalDigi/interface/HcalDigiCollections.h"
#include "DataFormats/HcalDetId/interface/HcalSubdetector.h"
#include "Geometry/CaloGeometry/interface/CaloGeometry.h"
//#include "CalibFormats/HcalObjects/interface/HcalDbRecord.h"
#include "Geometry/Records/interface/CaloGeometryRecord.h"
#include "FWCore/Framework/interface/ESHandle.h"
//#include "CalibFormats/HcalObjects/interface/HcalDbService.h"
#include "DataFormats/HcalRecHit/interface/HFRecHit.h"
#include "DataFormats/GeometryVector/interface/GlobalPoint.h"

#include "CalibFormats/HcalObjects/interface/HcalCoderDb.h"
#include "CalibFormats/HcalObjects/interface/HcalDbService.h"
#include "CalibFormats/HcalObjects/interface/HcalDbRecord.h"
#include "CalibCalorimetry/HcalAlgos/interface/HcalPulseShapes.h"
#include "Geometry/Records/interface/HcalRecNumberingRecord.h"

#include "TMath.h"

class ZDCRecHitView: public EventViewBase{
    public:
       ZDCRecHitView(const edm::ParameterSet& ps, TTree * tree, edm::ConsumesCollector && iC);

    private:
      virtual void fillSpecific(const edm::Event&, const edm::EventSetup&);
      int getEnergy(ZDCDigiCollection::const_iterator, int, int);
      const CaloGeometry* fGeo;  //For ETA - PHI info
      edm::ESHandle<HcalDbService> conditions;   //For ETA - PHI info
      const HcalQIECoder* qiecoder;
      const HcalQIEShape* qieshape;
};
#endif
