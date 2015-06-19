#ifndef TrackJetView_h
#define TrackJetView_h

#include "CommonFSQFramework/Core/interface/EventViewBase.h"

class TrackJetView: public EventViewBase{
    public:
       TrackJetView(const edm::ParameterSet& ps, TTree * tree);

    private:
      virtual void fillSpecific(const edm::Event&, const edm::EventSetup&);
      float m_maxEta; // 
      float m_minPt;
      edm::InputTag m_TrackJets;



};
#endif
