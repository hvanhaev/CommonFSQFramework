#ifndef CastorTowerView_h
#define CastorTowerView_h

#include "CommonFSQFramework/Core/interface/EventViewBase.h"

#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "DataFormats/CastorReco/interface/CastorTower.h"


class CastorTowerView: public EventViewBase{
    public:
       CastorTowerView(const edm::ParameterSet& ps, TTree * tree);

    private:
      virtual void fillSpecific(const edm::Event&, const edm::EventSetup&);
      
      edm::InputTag m_inputCol;




};
#endif
