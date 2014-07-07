#ifndef RecoTrackView_h
#define RecoTrackView_h

#include "MNTriggerStudies/MNTriggerAna/interface/EventViewBase.h"

class RecoTrackView: public EventViewBase{
    public:
       RecoTrackView(const edm::ParameterSet& ps, TTree * tree);
       virtual void fill(const edm::Event&, const edm::EventSetup&);

    private:
      float m_maxEta; // 
      float m_minPt;
      int   m_charge; // -1 - take all, 0 - neutral, +1 - charged  
      edm::InputTag m_inputCol;



};
#endif
