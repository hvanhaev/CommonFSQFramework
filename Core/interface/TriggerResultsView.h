#ifndef TriggerResultsView_h
#define TriggerResultsView_h

#include "CommonFSQFramework/Core/interface/EventViewBase.h"
#include "HLTrigger/HLTcore/interface/HLTPrescaleProvider.h"

class TriggerResultsView: public EventViewBase{
    public:
       TriggerResultsView(const edm::ParameterSet& ps, TTree * tree, edm::ConsumesCollector && iC, edm::EDAnalyzer* module);
       void doBeginRun(const edm::Run&, const edm::EventSetup&);

    private:
      virtual void fillSpecific(const edm::Event&, const edm::EventSetup&);
      std::string m_process;
      std::vector<std::string > m_triggerNames;
      std::map<std::string, std::vector<std::string > > m_triggerClasses;
      bool m_storePrescales;

      HLTPrescaleProvider hltprovider_;
      bool isValidHLTConfig_;

      bool isStage1_;

      edm::EDGetTokenT<edm::TriggerResults> m_HLTtoken;
};
#endif
