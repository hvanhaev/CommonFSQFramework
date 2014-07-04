#ifndef GenTrackView_h
#define GenTrackView_h

#include "MNTriggerStudies/MNTriggerAna/interface/EventViewBase.h"

class GenTrackView: public EventViewBase{
    public:
       GenTrackView(const edm::ParameterSet& ps, TTree * tree);
       virtual void fill(const edm::Event&, const edm::EventSetup&);

    private:
      float m_maxEta; // 
      int   m_charge; // -1 - take all, 0 - neutral, +1 - charged  



};
#endif
