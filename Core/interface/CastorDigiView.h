#ifndef CastorDigiView_h
#define CastorDigiView_h

#include "CommonFSQFramework/Core/interface/EventViewBase.h"

#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "FWCore/Utilities/interface/InputTag.h"

#include "DataFormats/Common/interface/Handle.h"
//#include "DataFormats/HcalDigi/interface/HcalDigiCollections.h" // for CastorDigiCollection
#include "DataFormats/DetId/interface/DetId.h"

//#include "CondFormats/CastorObjects/interface/CastorPedestals.h"
//#include "CondFormats/CastorObjects/interface/CastorPedestalWidths.h"
#include "CondFormats/CastorObjects/interface/CastorQIECoder.h"
#include "CondFormats/CastorObjects/interface/CastorQIEData.h"
//#include "CondFormats/CastorObjects/interface/CastorQIEShape.h"
#include "CondFormats/CastorObjects/interface/CastorElectronicsMap.h"
#include "CondFormats/CastorObjects/interface/AllObjects.h"


#include "DataFormats/HcalDigi/interface/CastorDataFrame.h"

#include "CalibFormats/CastorObjects/interface/CastorCalibrations.h"
#include "CalibFormats/CastorObjects/interface/CastorCalibrationWidths.h"

//#include "CalibCalorimetry/CastorCalib/interface/CastorDbASCIIIO.h"

#include "DataFormats/Common/interface/SortedCollection.h"

#include <map>
#include <string>
#include "boost/tuple/tuple.hpp"

typedef edm::SortedCollection<CastorDataFrame> CastorDigiCollection;


class CastorDigiView: public EventViewBase {
    public:
       CastorDigiView(const edm::ParameterSet& ps, TTree * tree, edm::ConsumesCollector && iC);

    private:
      virtual void fillSpecific(const edm::Event&, const edm::EventSetup&);
            
      int m_firstTS;
      int m_lastTS;

      edm::InputTag m_Digis;
      edm::EDGetTokenT<CastorDigiCollection> m_tok_input;
     
      
};

#endif
