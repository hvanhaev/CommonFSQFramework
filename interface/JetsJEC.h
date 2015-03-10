#ifndef JetsJEC_h
#define JetsJEC_h

#include "MNTriggerStudies/MNTriggerAna/interface/EventViewBase.h"

class JetsJEC: public EventViewBase{
    public:
       JetsJEC(const edm::ParameterSet& ps, TTree * tree);

    private:
      virtual void fillSpecific(const edm::Event&, const edm::EventSetup&);
      edm::InputTag  m_todo;
      edm::InputTag  m_rho;
      std::string m_label;



};
#endif
