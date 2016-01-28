#ifndef GenericCandidateViewP4_h
#define GenericCandidateViewP4_h

#include "CommonFSQFramework/Core/interface/EventViewBase.h"

class GenericCandidateViewP4: public EventViewBase{
    public:
       GenericCandidateViewP4(const edm::ParameterSet& ps, TTree * tree, edm::ConsumesCollector && iC);

    private:
      virtual void fillSpecific(const edm::Event&, const edm::EventSetup&);
      std::vector<edm::InputTag > m_todo;
      float  m_ptmin;



};
#endif
