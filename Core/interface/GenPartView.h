#ifndef GenPartView_h
#define GenPartView_h

#include "CommonFSQFramework/Core/interface/EventViewBase.h"

class GenPartView: public EventViewBase{
    public:
       GenPartView(const edm::ParameterSet& ps, TTree * tree, edm::ConsumesCollector && iC);

    private:
      virtual void fillSpecific(const edm::Event&, const edm::EventSetup&);
      float m_maxEta; // 
      float m_minPt;
      int   m_charge; // -1 - take all, 0 - neutral, +1 - charged  
      edm::InputTag m_GenParts;



};
#endif
