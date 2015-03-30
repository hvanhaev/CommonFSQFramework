#ifndef TriggerResultsView_h
#define TriggerResultsView_h

#include "MNTriggerStudies/MNTriggerAna/interface/EventViewBase.h"

class TriggerResultsView: public EventViewBase{
    public:
       TriggerResultsView(const edm::ParameterSet& ps, TTree * tree);

    private:
      virtual void fillSpecific(const edm::Event&, const edm::EventSetup&);
      std::string m_process;
      std::vector<std::string > m_triggerNames;
      std::map<std::string, std::vector<std::string > > m_triggerClasses;



};
#endif
