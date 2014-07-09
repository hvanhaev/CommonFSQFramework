#ifndef RecoTrackView_h
#define RecoTrackView_h

#include "MNTriggerStudies/MNTriggerAna/interface/EventViewBase.h"
#include "MNTriggerStudies/MNTriggerAna/interface/TestTrackData.h"

class RecoTrackView: public EventViewBase{
    public:
       RecoTrackView(const edm::ParameterSet& ps, TTree * tree);

    private:
      virtual void fillSpecific(const edm::Event&, const edm::EventSetup&);
      float m_maxEta; // 
      float m_maxDZ; // 
      float m_minPt;
      int   m_charge; // -1 - take all, 0 - neutral, +1 - charged  
      edm::InputTag m_inputCol;


      std::map<std::string, std::vector<tmf::TestTrackData> > m_testTrackData;
      void resetLocal();



};
#endif
