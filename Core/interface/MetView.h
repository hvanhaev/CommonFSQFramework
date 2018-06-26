#ifndef MetView_h
#define MetView_h

#include "CommonFSQFramework/Core/interface/EventViewBase.h"

class MetView: public EventViewBase{
    public:
      MetView(const edm::ParameterSet& ps, TTree * tree, edm::ConsumesCollector && iC);

    private:
      virtual void fillSpecific(const edm::Event&, const edm::EventSetup&);
      edm::InputTag m_Met;
};
#endif
