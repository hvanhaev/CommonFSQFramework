#ifndef HFRecHitView_h
#define HFRecHitView_h

#include "CommonFSQFramework/Core/interface/EventViewBase.h"
// HCAL Rechit
#include "DataFormats/Common/interface/Handle.h"
#include "DataFormats/HcalRecHit/interface/HcalRecHitCollections.h"
#include "DataFormats/HcalRecHit/interface/HcalSourcePositionData.h"
#include "DataFormats/HcalDetId/interface/HcalSubdetector.h"


class HFRecHitView: public EventViewBase{
    public:
       HFRecHitView(const edm::ParameterSet& ps, TTree * tree);

    private:
      virtual void fillSpecific(const edm::Event&, const edm::EventSetup&);


};
#endif
