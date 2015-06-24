#ifndef HFRecHitView_h
#define HFRecHitView_h

#include "CommonFSQFramework/Core/interface/EventViewBase.h"
// HCAL Rechit
#include "DataFormats/Common/interface/Handle.h"
#include "DataFormats/HcalRecHit/interface/HcalRecHitCollections.h"
#include "DataFormats/HcalRecHit/interface/HcalSourcePositionData.h"
#include "DataFormats/HcalDetId/interface/HcalSubdetector.h"
#include "Geometry/CaloGeometry/interface/CaloGeometry.h"
#include "CalibFormats/HcalObjects/interface/HcalDbRecord.h"
#include "Geometry/Records/interface/CaloGeometryRecord.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "CalibFormats/HcalObjects/interface/HcalDbService.h"
#include "DataFormats/HcalRecHit/interface/HFRecHit.h"
#include "DataFormats/GeometryVector/interface/GlobalPoint.h"
#include "TMath.h"

class HFRecHitView: public EventViewBase{
    public:
       HFRecHitView(const edm::ParameterSet& ps, TTree * tree);

    private:
      virtual void fillSpecific(const edm::Event&, const edm::EventSetup&);
      const CaloGeometry* fGeo;  //For ETA - PHI info
      edm::ESHandle<HcalDbService> conditions;   //For ETA - PHI info

};
#endif
