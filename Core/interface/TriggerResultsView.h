#ifndef TriggerResultsView_h
#define TriggerResultsView_h

#include "CommonFSQFramework/Core/interface/EventViewBase.h"
#include "HLTrigger/HLTcore/interface/HLTPrescaleProvider.h"

#include "DataFormats/L1TGlobal/interface/GlobalAlgBlk.h"
#include "DataFormats/L1TGlobal/interface/GlobalExtBlk.h"
#include "DataFormats/L1Trigger/interface/BXVector.h"
#include "L1Trigger/L1TGlobal/interface/L1TGlobalUtil.h"

#include <memory>
#include <utility>
#include <vector>

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
      
      edm::EDGetTokenT<GlobalAlgBlkBxCollection> m_l1tStage2uGtToken; // input tag for L1 uGT DAQ readout record
      edm::EDGetTokenT<L1GlobalTriggerReadoutRecord> m_l1GtToken; // input tag for L1 uGT DAQ readout record
      edm::EDGetTokenT<edm::TriggerResults> m_HLTtoken;

      // To get the number of algorithms
      std::shared_ptr<l1t::L1TGlobalUtil> m_gtUtil;
      int m_numAlgs; // number of algorithms
};
#endif
