#ifndef GenJetView_h
#define GenJetView_h

#include "CommonFSQFramework/Core/interface/EventViewBase.h"

class GenJetView: public EventViewBase{
    public:
       GenJetView(const edm::ParameterSet& ps, TTree * tree, edm::ConsumesCollector && iC);

    private:
      virtual void fillSpecific(const edm::Event&, const edm::EventSetup&);
      float m_maxEta; // 
      float m_minPt;
      edm::InputTag m_genJets;



};
#endif
