#include "MNTriggerStudies/MNTriggerAna/interface/GenTrackView.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"

GenTrackView::GenTrackView(const edm::ParameterSet& iConfig, TTree * tree):
EventViewBase(iConfig,  tree)
{

    // register branches
    registerVecP4("genTracks", tree);
    registerVecInt("charge", tree);
    registerVecInt("pdg", tree);
    registerVecInt("status", tree);

    // fetch config data
    m_maxEta = iConfig.getParameter<double>("maxEta");
    m_minPt = iConfig.getParameter<double>("minPt");
    m_charge = iConfig.getParameter<int>("charge");
    m_genTracks = iConfig.getParameter<edm::InputTag>("genTracks");

    if (m_charge != 0 && m_charge != 1 && m_charge != -1){
        throw "charge parameter not equal to -1(save all)/0(save neutrals)/1(save charded)\n";
    }




    //std::cout << "XX "  << m_maxEta << " " << m_charge << std::endl;

}


void GenTrackView::fillSpecific(const edm::Event& iEvent, const edm::EventSetup& iSetup){

    // vector<reco::GenParticle>             "genParticles"              ""                "SIM"          recoGenParticles_genParticles__SIM
    edm::Handle<std::vector<reco::GenParticle> > hIn;
    iEvent.getByLabel(m_genTracks, hIn);
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
        if (std::abs(hIn->at(i).eta()) > m_maxEta ) continue;
        addToP4Vec("genTracks", hIn->at(i).p4());
        addToIVec("charge", hIn->at(i).charge());
        addToIVec("pdg", hIn->at(i).pdgId());
        addToIVec("status", hIn->at(i).status());

    }

}
