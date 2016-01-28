#include "CommonFSQFramework/Core/interface/GenJetView.h"
#include "DataFormats/JetReco/interface/GenJet.h"

GenJetView::GenJetView(const edm::ParameterSet& iConfig, TTree * tree, edm::ConsumesCollector && iC):
EventViewBase(iConfig,  tree)
{

    // register branches
    registerVecP4("p4", tree);
    registerVecInt("nConst", tree);
    registerVecFloat("emE", tree);
    registerVecFloat("hadE", tree);

    // fetch config data
    m_maxEta = iConfig.getParameter<double>("maxEta");
    m_minPt = iConfig.getParameter<double>("minPt");
    m_genJets = iConfig.getParameter<edm::InputTag>("genJets");

    // register consumes
    iC.consumes<std::vector<reco::GenJet> >(m_genJets);
}


void GenJetView::fillSpecific(const edm::Event& iEvent, const edm::EventSetup& iSetup){

    // vector<reco::GenJet> "GenJets"  ""  "SIM"          recoGenJets_ak4GenJets__SIM
    edm::Handle<std::vector<reco::GenJet> > hIn;
    iEvent.getByLabel(m_genJets, hIn);
    for (unsigned int i = 0; i< hIn->size();++i){
        if (hIn->at(i).pt() < m_minPt ) continue;
        if (std::abs(hIn->at(i).eta()) > m_maxEta ) continue;
        addToP4Vec("p4", hIn->at(i).p4());
        addToIVec("nConst", hIn->at(i).nConstituents());
        addToFVec("emE", hIn->at(i).emEnergy());
        addToFVec("hadE", hIn->at(i).hadEnergy());

    }

}
