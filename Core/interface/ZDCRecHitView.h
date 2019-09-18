#ifndef ZDCRecHitView_h
#define ZDCRecHitView_h

#include "CommonFSQFramework/Core/interface/EventViewBase.h"
#include "DataFormats/HcalDigi/interface/HcalDigiCollections.h"
#include "CalibFormats/HcalObjects/interface/HcalDbService.h"
#include "FWCore/Framework/interface/ESHandle.h"

class ZDCRecHitView: public EventViewBase{
    public:
       ZDCRecHitView(const edm::ParameterSet& ps, TTree * tree, edm::ConsumesCollector && iC);

    private:
      virtual void fillSpecific(const edm::Event&, const edm::EventSetup&);
      float getEnergy(ZDCDigiCollection::const_iterator, int, int);
      edm::InputTag m_inputlabel;
      edm::ESHandle<HcalDbService> fConditions;
};
#endif
