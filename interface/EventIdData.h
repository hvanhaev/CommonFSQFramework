#ifndef EventIdData_h
#define EventIdData_h

#include "MNTriggerStudies/MNTriggerAna/interface/EventViewBase.h"

class EventIdData: public EventViewBase{
   public:
      EventIdData(const edm::ParameterSet& ps, TTree * tree);
   private:
      virtual void fillSpecific(const edm::Event&, const edm::EventSetup&);


};
#endif
