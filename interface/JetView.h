#ifndef JetView_h
#define JetView_h

#include "MNTriggerStudies/MNTriggerAna/interface/EventViewBase.h"
#include "MNTriggerStudies/MNTriggerAna/interface/TestTrackData.h"

class JetView: public EventViewBase{
    public:
       JetView(const edm::ParameterSet& ps, TTree * tree);

    private:
      virtual void fillSpecific(const edm::Event&, const edm::EventSetup&);
      float m_maxEta; // 
      float m_minPt;
      float m_maxnum; // 
      edm::InputTag m_inputCol;





};
#endif
