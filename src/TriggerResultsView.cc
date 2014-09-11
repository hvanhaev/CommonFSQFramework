#include "MNTriggerStudies/MNTriggerAna/interface/TriggerResultsView.h"

TriggerResultsView::TriggerResultsView(const edm::ParameterSet& iConfig, TTree * tree):
EventViewBase(iConfig,  tree)
{
    // fetch config data
    m_process = iConfig.getParameter<std::string>("process");
    m_triggerNames = iConfig.getParameter<std::vector<std::string> >("triggers");
    for (unsigned int i=0; i < m_triggerNames.size();++i){
        if (iConfig.exists(m_triggerNames.at(i))) {
            std::vector<std::string> triggerClass =  iConfig.getParameter<std::vector<std::string> >(m_triggerNames.at(i));
            m_triggerClasses[m_triggerNames.at(i)] = triggerClass;
        } else {
            std::string keyName = m_triggerNames.at(i);
            if (m_triggerNames.at(i).at(m_triggerNames.at(i).size()-1 ) == '*'){
                std::cout << "Star: " << m_triggerNames.at(i) << std::endl;
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
    for(;it != itE;++it){
        registerInt(it->first, tree);
    }
}


void TriggerResultsView::fillSpecific(const edm::Event& iEvent, const edm::EventSetup& iSetup){

    std::map<std::string, std::vector<std::string> >::const_iterator it, itE;
    it = m_triggerClasses.begin();
    itE = m_triggerClasses.end();
    for(;it != itE;++it){
        //registerInt(it->first, tree);
    }




}
