#ifndef VerticesView_h
#define VerticesView_h

#include "CommonFSQFramework/Core/interface/EventViewBase.h"

class VerticesView: public EventViewBase{
    public:
       VerticesView(const edm::ParameterSet& ps, TTree * tree, edm::ConsumesCollector && iC);

    private:
      virtual void fillSpecific(const edm::Event&, const edm::EventSetup&);
      edm::InputTag m_src;



};
#endif
