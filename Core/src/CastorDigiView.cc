#include "CommonFSQFramework/Core/interface/CastorDigiView.h"

#include <boost/format.hpp>

#include <cmath>
#include <iostream>
#include <map>
#include <iomanip>
#include <fstream>
#include <vector>
#include <string>


#include <map>
#include <string>
#include "boost/tuple/tuple.hpp"

CastorDigiView::CastorDigiView(const edm::ParameterSet& iConfig, TTree * tree, edm::ConsumesCollector && iC):
EventViewBase(iConfig,  tree)
{
    using namespace std;
    using namespace edm;
    using namespace reco;
    
    // register branches    
    for (int iSector=0;iSector<17;iSector++) {
	    for (int iModule=0;iModule<15;iModule++) {
			const string ADCallTS = (boost::format("ADCallTS_Sect%i_Mod%i") % iSector % iModule).str();
			const string fCallTS = (boost::format("fCallTS_Sect%i_Mod%i") % iSector % iModule).str();
			
			registerVecFloat(ADCallTS.c_str(), tree);
			registerVecFloat(fCallTS.c_str(), tree);
		}     
	}

    // fetch config data
    m_Digis = iConfig.getParameter<edm::InputTag>("input");
    
    m_firstTS = iConfig.getParameter<int>("firstTS");
    m_lastTS = iConfig.getParameter<int>("lastTS");

    // register consumes
    iC.consumes<CastorDigiCollection>(m_Digis);
    
    EDGetTokenT<CastorDigiCollection> tok_input0;
    tok_input0 = iC.consumes<CastorDigiCollection>(m_Digis); 
  
    TokenTuple myTuple(tok_input0);
  
    m_Tokens = myTuple;
    
    
	  
	
	
	
}

void CastorDigiView::fillSpecific(const edm::Event& iEvent, const edm::EventSetup& iSetup){
	
  using namespace std;
  using namespace edm;
  using namespace reco;
  
  Handle<CastorDigiCollection> digis;
  iEvent.getByToken(m_Tokens.get<0>(), digis);
  
  edm::ESHandle<CastorDbService> conditions;
  iSetup.get<CastorDbRecord>().get(conditions);
  
  const CastorQIEShape* shape = conditions->getCastorShape();

   
  for (CastorDigiCollection::const_iterator it = digis->begin(); it != digis->end(); it++) {
    
    const CastorDataFrame digi = (const CastorDataFrame)(*it);
    
    const CastorQIECoder* coder = conditions->getCastorCoder(digi.id().rawId());

    const int sector = digi.id().sector();     // range 1...16
    const int module = digi.id().module();     // range 1...14
    
    const string ADCallTS = (boost::format("ADCallTS_Sect%i_Mod%i") % sector % module).str();
	const string fCallTS = (boost::format("fCallTS_Sect%i_Mod%i") % sector % module).str();
    
    for (int ts=m_firstTS; ts<m_lastTS; ++ts) {

      const int capid = digi.sample(ts).capid(); // range 0..3
      const int adc = digi.sample(ts).adc();
      const double charge = coder->charge(*shape, adc, capid);
      
      addToFVec(ADCallTS.c_str(), adc);
      addToFVec(fCallTS.c_str(), charge);      
    }
  } 
}





