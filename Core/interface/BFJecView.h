#ifndef BFJecView_h
#define BFJecView_h

#include "MNTriggerStudies/MNTriggerAna/interface/EventViewBase.h"

class BFJecView: public EventViewBase{
    public:
       BFJecView(const edm::ParameterSet& ps, TTree * tree);

    private:
      virtual void fillSpecific(const edm::Event&, const edm::EventSetup&);
      std::vector< std::string > m_todoJets;
      std::vector<edm::InputTag> m_todoRecoJets;
      std::vector<edm::InputTag> m_todoGenJets;
      std::vector<edm::InputTag> m_rhos;


      float m_minPT ;
      float m_minPTGen ;
      float m_maxEta; 



};
#endif
