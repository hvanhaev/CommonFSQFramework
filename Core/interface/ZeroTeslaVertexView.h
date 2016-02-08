#ifndef ZeroTeslaVertexView_h
#define ZeroTeslaVertexView_h

#include "CommonFSQFramework/Core/interface/EventViewBase.h"

class ZeroTeslaVertexView: public EventViewBase {
    public:
       ZeroTeslaVertexView(const edm::ParameterSet& ps, TTree * tree, edm::ConsumesCollector && iC);

    private:
      virtual void fillSpecific(const edm::Event&, const edm::EventSetup&);
      bool m_usePixels;
      edm::InputTag m_src;
};

#endif
