#include "CommonFSQFramework/Core/interface/TriggerResultsView.h"

#include "FWCore/Common/interface/TriggerResultsByName.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"

#include "DataFormats/Common/interface/TriggerResults.h"
#include "DataFormats/L1GlobalTrigger/interface/L1GlobalTriggerReadoutRecord.h"


TriggerResultsView::TriggerResultsView(const edm::ParameterSet& iConfig,
				       TTree * tree,
				       edm::ConsumesCollector && iC,
				       edm::EDAnalyzer* module):
  EventViewBase(iConfig,  tree), hltprovider_(iConfig, iC, *module),
  m_l1tStage2uGtToken(iC.consumes<GlobalAlgBlkBxCollection>(edm::InputTag("gtStage2Digis"))),
  m_gtUtil(new l1t::L1TGlobalUtil(iConfig, iC, *module,
				  edm::InputTag("gtStage2Digis"), // 2018
				  edm::InputTag("gtStage2Digis"))), // 2018
  m_numAlgs(0)
{
    // fetch config data
    // m_process = iConfig.getParameter<std::string>("process");
    m_triggerNames = iConfig.getParameter<std::vector<std::string> >("triggers");
    m_storePrescales = iConfig.getParameter<bool>("storePrescales");
    
    for (unsigned int i=0; i < m_triggerNames.size();++i){
        // check, if it's for L1GT readout
        if (m_triggerNames.at(i).find("L1GT") != std::string::npos) {
            m_triggerClasses[m_triggerNames.at(i)] = std::vector<std::string>();

        } else if (iConfig.exists(m_triggerNames.at(i))) {
            std::vector<std::string> triggerClass =  iConfig.getParameter<std::vector<std::string> >(m_triggerNames.at(i));
            m_triggerClasses[m_triggerNames.at(i)] = triggerClass;

        } else {
            //  '*' supported at the end only
            std::string keyName = m_triggerNames.at(i);
            if (m_triggerNames.at(i).at(m_triggerNames.at(i).size()-1 ) == '*'){
                keyName = std::string(m_triggerNames.at(i), 0, m_triggerNames.at(i).size()-1);
            } 
            std::vector<std::string > vec;
            vec.push_back( m_triggerNames.at(i));
            m_triggerClasses[keyName]= vec;
        }
    }

    // register branches
    std::map<std::string, std::vector<std::string> >::const_iterator it, itE;
    it = m_triggerClasses.begin();
    itE = m_triggerClasses.end();
    for(;it != itE;++it) {
        if (it->first.find("L1GT") != std::string::npos) {
            registerVecInt(it->first, tree);
        } else {
            registerInt(it->first, tree);
	    
            if (m_storePrescales) {
                if (it->second.size() == 1) {
                    std::string name = it->second.at(0);
                    if (name.find("*")!= std::string::npos){ // wildcard entry
                        // do nothing
                    } else {
                        registerInt("L1PS_" + it->first, tree);
                        registerInt("HLTPS_" + it->first, tree);
                    }
                } else {
                    for (unsigned int i=0; i < it->second.size();++i) {
                        std::string name = it->second.at(i);
                        if (name.find("*")!= std::string::npos){ // wildcard entry
                            // do not store prescales for wildcard triggers as we can not easily fetch the complete trigger name.
                        } else { // normal entry
                            registerInt("L1PS_" + name, tree);
                            registerInt("HLTPS_" + name, tree);
                        }
                    }
                }
            }
        }
    }
    
        
    m_HLTtoken = iC.consumes<edm::TriggerResults>(edm::InputTag("TriggerResults", "", "HLT"));
}

void TriggerResultsView::doBeginRun(const edm::Run& r, const edm::EventSetup& es) {
    
    bool changed = true;
    isValidHLTConfig_ = hltprovider_.init(r, es, "*", changed);

    // Get the trigger menu information
    m_gtUtil->retrieveL1Setup(es);
    // Find the number of algos defined
    m_numAlgs = static_cast<int>(m_gtUtil->decisionsInitial().size());
    edm::LogWarning("TriggerResultsView: number of L1 bits=") << m_numAlgs << std::endl;
}


void TriggerResultsView::fillSpecific(const edm::Event& iEvent, const edm::EventSetup& iSetup) {

    edm::Handle<edm::TriggerResults> trigres;
    iEvent.getByToken(m_HLTtoken, trigres);
    edm::TriggerResultsByName trbn = iEvent.triggerResultsByName(*trigres);
    if (!trbn.isValid()) {
        edm::LogWarning(" TriggerResultsByName ") << " Cannot read TriggerResultsByName (HLT) " << std::endl;
        return; 
    }

    const std::vector< std::string > names = trbn.triggerNames(); 
    

    // this is for stage2 L1 trigger *************************************
      
    // Open uGT readout record
    edm::Handle<GlobalAlgBlkBxCollection> uGtAlgs;
    iEvent.getByToken(m_l1tStage2uGtToken, uGtAlgs);      
    
    
    if (!uGtAlgs.isValid()) {
      edm::LogWarning("TriggerResultsView") << "Cannot find uGT readout record.";
      return;
    }
    
    std::map<std::string, std::vector<std::string> >::const_iterator it, itE;
    it = m_triggerClasses.begin();
    itE = m_triggerClasses.end();
    for(;it != itE; ++it) {

      if (it->first == "L1GTAlgo") {
	const int bxInEvent = 0;
	auto itr = uGtAlgs->begin(bxInEvent);

	for(int algoBit = 0; algoBit < m_numAlgs; ++algoBit) {	    
	  //         prescaleFactorSet_->Fill(lumi, itr->getPreScColumn());
	  addToIVec(it->first, itr->getAlgoDecisionInitial(algoBit)); // Algorithm bits before AlgoBX mask
	}
	continue;
      }
      
      int accept = 0;
      
      if (m_storePrescales && it->second.size() == 1) {
	std::string name = it->second.at(0);
	if (name.find("*")!= std::string::npos) { // wildcard entry
	  // do nothing
	} else {
	  setI("L1PS_" + it->first, (hltprovider_.prescaleValues(iEvent, iSetup, name)).first );
	  setI("HLTPS_" + it->first, (hltprovider_.prescaleValues(iEvent, iSetup, name)).second );
	}
      }
      
      for (unsigned int i=0; i < it->second.size();++i) {
	std::string name = it->second.at(i);
	if (name.find("*")!= std::string::npos) { // wildcard entry
	  for (unsigned iName = 0; iName < names.size(); ++iName) {
	    std::string nameForSearch = std::string(it->second.at(i), 0, it->second.at(i).size()-1); // strip the star
	    if (names.at(iName).find(nameForSearch)==0) { // starts with
	      if (trbn.accept(names.at(iName)))
		accept = 1;
	    }
	  }
	} else { // normal entry
	  if (trbn.accept( it->second.at(i)))
	    accept = 1;
	  if (m_storePrescales) {
	    setI("L1PS_" + name, (hltprovider_.prescaleValues(iEvent, iSetup, name)).first );
	    setI("HLTPS_" + name, (hltprovider_.prescaleValues(iEvent, iSetup, name)).second );
	  }
	}
	setI(it->first, accept);
      }
    }
}
