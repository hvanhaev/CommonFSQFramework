#ifndef EventIdData_h
#define EventIdData_h

#include "CommonFSQFramework/Core/interface/EventViewBase.h"

class EventIdData: public EventViewBase{
   public:
      EventIdData(const edm::ParameterSet& ps, TTree * tree, edm::ConsumesCollector && iC);
   private:
      virtual void fillSpecific(const edm::Event&, const edm::EventSetup&);
      int localcount;
   
};
#endif
