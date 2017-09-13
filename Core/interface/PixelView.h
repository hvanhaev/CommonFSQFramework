#ifndef PixelView_h
#define PixelView_h

#include "CommonFSQFramework/Core/interface/EventViewBase.h"

class PixelView: public EventViewBase {
    public:
       PixelView(const edm::ParameterSet& ps, TTree * tree, edm::ConsumesCollector && iC);

    private:
      virtual void fillSpecific(const edm::Event&, const edm::EventSetup&);
      edm::InputTag m_src;
};

#endif
