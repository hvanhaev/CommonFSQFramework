#include "CommonFSQFramework/Core/interface/CastorDigiView.h"

#include "CalibFormats/CastorObjects/interface/CastorDbRecord.h"
#include "CalibFormats/CastorObjects/interface/CastorDbService.h"
#include "CalibFormats/CastorObjects/interface/CastorCalibrationWidthsSet.h"

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

CastorDigiView::CastorDigiView(const edm::ParameterSet& iConfig, 
			       TTree * tree, 
			       edm::ConsumesCollector && iC) :
  EventViewBase(iConfig,  tree)
{
    using namespace std;
    using namespace edm;
    using namespace reco;
    
    // fetch config data
    m_Digis = iConfig.getParameter<edm::InputTag>("inputcoll");
    
    m_firstTS = iConfig.getParameter<int>("firstTS");
    m_lastTS = iConfig.getParameter<int>("lastTS");

    // register consumes
    m_tok_input = iC.consumes<CastorDigiCollection>(m_Digis); 
    
    // register branches 
    for (int ts=m_firstTS; ts<=m_lastTS; ++ts) {
    	const string ADCallTS = (boost::format("ADC_TS%i") % ts).str();
	const string fCallTS = (boost::format("Charge_TS%i") % ts).str();

	registerVecFloat(ADCallTS.c_str(), tree);
	registerVecFloat(fCallTS.c_str(), tree);
    }	
}


void 
CastorDigiView::fillSpecific(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{	
  using namespace std;
  using namespace edm;
  using namespace reco;
  
  Handle<CastorDigiCollection> digis;
  iEvent.getByToken(m_tok_input, digis);
  
  edm::ESHandle<CastorDbService> conditions;
  iSetup.get<CastorDbRecord>().get(conditions);
  
  const CastorQIEShape* shape = conditions->getCastorShape();
  
  for (int ts=m_firstTS; ts<=m_lastTS; ++ts) { 
  
    const string ADCallTS = (boost::format("ADC_TS%i") % ts).str();
    const string fCallTS = (boost::format("Charge_TS%i") % ts).str();
    
    for (CastorDigiCollection::const_iterator it = digis->begin(); it != digis->end(); it++) {

      const CastorDataFrame digi = (const CastorDataFrame)(*it);    
      const CastorQIECoder* coder = conditions->getCastorCoder(digi.id().rawId());

      const int capid = digi.sample(ts).capid(); // range 0..3
      const int adc = digi.sample(ts).adc();
      const double charge = coder->charge(*shape, adc, capid);
      
      addToFVec(ADCallTS.c_str(), adc);
      addToFVec(fCallTS.c_str(), charge);      
    }
  } 
}





