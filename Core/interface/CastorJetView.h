#ifndef CastorJetView_h
#define CastorJetView_h

#include "CommonFSQFramework/Core/interface/EventViewBase.h"
#include "DataFormats/CastorReco/interface/CastorTower.h"
#include "DataFormats/JetReco/interface/BasicJet.h"

class CastorJetView: public EventViewBase {
    public:
       CastorJetView(const edm::ParameterSet& ps, TTree * tree, edm::ConsumesCollector && iC);

    private:
      virtual void fillSpecific(const edm::Event&, const edm::EventSetup&);  
      double m_minCastorJetEnergy;
      double m_jetRadius;
};

#endif
