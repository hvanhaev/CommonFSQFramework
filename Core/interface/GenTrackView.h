#ifndef GenTrackView_h
#define GenTrackView_h

#include "MNTriggerStudies/MNTriggerAna/interface/EventViewBase.h"

class GenTrackView: public EventViewBase{
    public:
       GenTrackView(const edm::ParameterSet& ps, TTree * tree);

    private:
      virtual void fillSpecific(const edm::Event&, const edm::EventSetup&);
      float m_maxEta; // 
      float m_minPt;
      int   m_charge; // -1 - take all, 0 - neutral, +1 - charged  
      edm::InputTag m_genTracks;



};
#endif
