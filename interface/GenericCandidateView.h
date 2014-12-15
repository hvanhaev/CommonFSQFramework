#ifndef GenericCandidateView_h
#define GenericCandidateView_h

#include "MNTriggerStudies/MNTriggerAna/interface/EventViewBase.h"

class GenericCandidateView: public EventViewBase{
    public:
       GenericCandidateView(const edm::ParameterSet& ps, TTree * tree);

    private:
      virtual void fillSpecific(const edm::Event&, const edm::EventSetup&);
      std::vector<edm::InputTag > m_todo;



};
#endif
