#include "CommonFSQFramework/Core/interface/TrackJetView.h"
#include "DataFormats/JetReco/interface/TrackJetCollection.h"

TrackJetView::TrackJetView(const edm::ParameterSet& iConfig, TTree * tree):
EventViewBase(iConfig,  tree)
{

    // register branches
    registerVecP4("p4", tree);
    registerVecInt("nConst", tree);
    registerVecFloat("vx", tree);
    registerVecFloat("vy", tree);
    registerVecFloat("vz", tree);
    registerVecInt(  "fromVertex", tree);
    // fetch config data
    m_maxEta = iConfig.getParameter<double>("maxEta");
    m_minPt = iConfig.getParameter<double>("minPt");
    m_TrackJets =iConfig.getParameter<edm::InputTag>("input");


}


void TrackJetView::fillSpecific(const edm::Event& iEvent, const edm::EventSetup& iSetup){

    edm::Handle<reco::TrackJetCollection> hIn;
    iEvent.getByLabel(m_TrackJets, hIn); 
    for (unsigned int i = 0; i< hIn->size();++i){
        if (hIn->at(i).pt() < m_minPt ) continue;
        if (std::abs(hIn->at(i).eta()) > m_maxEta ) continue;
        addToP4Vec("p4", hIn->at(i).p4());
        addToIVec("nConst", hIn->at(i).numberOfTracks());
        addToFVec("vx", hIn->at(i).vx());
        addToFVec("vy", hIn->at(i).vy());
        addToFVec("vz", hIn->at(i).vz());

    }
}

