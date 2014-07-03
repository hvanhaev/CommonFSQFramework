#ifndef EventIdData_h
#define EventIdData_h

#include "MNTriggerStudies/MNTriggerAna/interface/EventViewBase.h"

class EventIdData: protected EventViewBase{
   public:
      EventIdData(const edm::ParameterSet&, TTree * tree);
      virtual void fill(const edm::Event&, const edm::EventSetup&);


};
#endif
