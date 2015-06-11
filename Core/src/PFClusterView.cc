#include "CommonFSQFramework/Core/interface/PFClusterView.h"
#include <TMath.h>


PFClusterView::PFClusterView(const edm::ParameterSet& iConfig, TTree * tree):
EventViewBase(iConfig,  tree)
{
    registerVecFloat("energy", tree);
    registerVecFloat("correctedEnergy",tree);
    registerVecFloat("correctedEnergyUncertainty",tree);
    registerVecFloat("time", tree);
    registerVecFloat("depth",tree);
    
    registerVecFloat("pt",tree);
    registerVecFloat("Et",tree);
    registerVecFloat("eta",tree);
    registerVecFloat("phi",tree);
    
    registerVecInt("size",tree);
    registerVecInt("isInClean",tree);
    registerVecInt("isInUnClean",tree);

    m_inputCol = iConfig.getParameter<edm::InputTag>("inputcoll");
    

}


void PFClusterView::fillSpecific(const edm::Event& iEvent, const edm::EventSetup& iSetup){

    edm::Handle<reco::PFClusterCollection> PFClusters;
    iEvent.getByLabel(m_inputCol,PFClusters);
    
    for (reco::PFClusterCollection::const_iterator i = PFClusters->begin(); i != PFClusters->end(); ++i) {
        
        addToFVec("energy", i->energy() );
	addToFVec("correctedEnergy",i->correctedEnergy());
	addToFVec("correctedEnergyUncertainty",i->correctedEnergyUncertainty());
	addToFVec("time",i->time());
	addToFVec("depth",i->depth());
	
	addToFVec("pt",i->pt());
	addToFVec("Et",(i->energy()/(TMath::CosH(i->eta()))));
	addToFVec("eta",i->eta());
	addToFVec("phi",i->phi());
	
	addToIVec("size",i->size());
	addToIVec("isInClean",(int)i->isInClean());
	addToIVec("isInUnClean",(int)i->isInUnclean());
	

    }

}
