#include "CommonFSQFramework/Core/interface/GenPartView.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"

GenPartView::GenPartView(const edm::ParameterSet& iConfig, TTree * tree, edm::ConsumesCollector && iC):
EventViewBase(iConfig,  tree)
{

    // register branches
    registerVecP4("p4", tree);
    registerVecInt("charge", tree);
    registerVecInt("pdg", tree);
    registerVecInt("status", tree);

    // fetch config data
    m_maxEta = iConfig.getParameter<double>("maxEta");
    m_minPt = iConfig.getParameter<double>("minPt");
    m_charge = iConfig.getParameter<int>("charge");
    m_GenParts = iConfig.getParameter<edm::InputTag>("genParticles");

    if (m_charge != 0 && m_charge != 1 && m_charge != -1){
        throw "charge parameter not equal to -1(save all)/0(save neutrals)/1(save charded)\n";
    }

    // register consumes
    iC.consumes<std::vector<reco::GenParticle> >(m_GenParts);
}


void GenPartView::fillSpecific(const edm::Event& iEvent, const edm::EventSetup& iSetup){

    // vector<reco::GenParticle>             "genParticles"              ""                "SIM"          recoGenParticles_genParticles__SIM
    edm::Handle<std::vector<reco::GenParticle> > hIn;
    iEvent.getByLabel(m_GenParts, hIn);
    for (unsigned int i = 0; i< hIn->size();++i){
        if (hIn->at(i).status() != 1  ) continue;
        if (m_charge != -1){   // -1 - save all particles
            int c = hIn->at(i).charge();
            bool good = false;
            if ( m_charge == 1 and c != 0 ) // m_charge==1 - drop neutrals, save charged
                good = true;
            if ( m_charge == 0 and c == 0 )
                good = true;
            if (!good) continue;
        }
        if (hIn->at(i).pt() < m_minPt ) continue;
        // maxEta = -1: all genparticles are accepted
        if (m_maxEta != -1 && std::abs(hIn->at(i).eta()) > m_maxEta ) continue;
        addToP4Vec("p4", hIn->at(i).p4());
        addToIVec("charge", hIn->at(i).charge());
        addToIVec("pdg", hIn->at(i).pdgId());
        addToIVec("status", hIn->at(i).status());

    }

}
