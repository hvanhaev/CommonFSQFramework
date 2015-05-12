#include "CommonFSQFramework/Core/interface/CastorJetView.h"
#include "DataFormats/JetReco/interface/BasicJet.h"
#include "DataFormats/JetReco/interface/CastorJetID.h"
#include <sstream>


CastorJetView::CastorJetView(const edm::ParameterSet& iConfig, TTree * tree):
EventViewBase(iConfig,  tree)
{
    registerVecP4("P4", tree);
    registerVecInt("nTowers", tree);
    registerVecFloat("fem", tree);
    registerVecFloat("width", tree);
    registerVecFloat("depth", tree);

    // fetch config data
    m_minCastorJetEnergy = iConfig.getParameter<double>("minCastorJetEnergy");
    m_jetRadius = iConfig.getParameter<double>("jetRadius");
}


void CastorJetView::fillSpecific(const edm::Event& iEvent, const edm::EventSetup& iSetup){


   edm::Handle<edm::View<reco::BasicJet> > jetsIn;
   edm::Handle<reco::CastorJetIDValueMap> jetIdMap;

   std::ostringstream JetLabel, JetIdLabel;
   JetLabel << "ak" << int(m_jetRadius*10) << "CastorJets";
   JetIdLabel << "ak" << int(m_jetRadius*10) << "CastorJetID";

   iEvent.getByLabel(JetLabel.str().c_str(), jetsIn);
   iEvent.getByLabel(JetIdLabel.str().c_str(),jetIdMap);

   // add jets to tree
   for (edm::View<reco::BasicJet>::const_iterator ibegin = jetsIn->begin(), iend = jetsIn->end(), ijet = ibegin; ijet != iend; ++ijet) 
   {
       unsigned int idx = ijet - ibegin;
 	   const reco::BasicJet &basicjet = (*jetsIn)[idx];
       edm::RefToBase<reco::BasicJet> jetRef = jetsIn->refAt(idx);
       reco::CastorJetID const & jetId = (*jetIdMap)[jetRef];
       if (basicjet.p4().energy()>=m_minCastorJetEnergy) {
           addToP4Vec("P4",basicjet.p4());
           addToIVec("nTowers", jetId.nTowers);
           addToFVec("fem", jetId.fem);
           addToFVec("width", jetId.width);
           addToFVec("depth", jetId.depth);

      }
   }
}
