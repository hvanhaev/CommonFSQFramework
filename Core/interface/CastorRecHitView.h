#ifndef CastorRecHitView_h
#define CastorRecHitView_h

#include "CommonFSQFramework/Core/interface/EventViewBase.h"

class CastorRecHitView: public EventViewBase {
    public:
       CastorRecHitView(const edm::ParameterSet& ps, TTree * tree, edm::ConsumesCollector && iC);

    private:
      virtual void fillSpecific(const edm::Event&, const edm::EventSetup&);
      bool m_onlyGoodRecHits;
      bool m_saturationInfo;
      edm::InputTag m_inputlabel;
};

#endif
