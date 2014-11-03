#include "MNTriggerStudies/MNTriggerAna/interface/BFJecView.h"
#include "DataFormats/JetReco/interface/Jet.h"

BFJecView::BFJecView(const edm::ParameterSet& iConfig, TTree * tree):
EventViewBase(iConfig,  tree)
{
    //registerVecP4("L1Jets", tree);
    m_todoJets = iConfig.getParameter<std::vector<std::string> >("todoJets");
    // minPt, maxEta
    for (unsigned int i=0; i < m_todoJets.size();++i){
        if (iConfig.exists(m_todoJets.at(i))) {
            std::vector<edm::InputTag> itag = iConfig.getParameter<std::vector<edm::InputTag> >(m_todoJets.at(i));
            if (itag.size()!=3) {
                throw "Parameter " + m_todoJets.at(i) + " should have three inputtags";
            }
           m_todoRecoJets.push_back(itag[0]);
           m_todoGenJets.push_back(itag[1]);
           m_rhos.push_back(itag[2]);

        } else {
            throw "Expected parameter not found: " + m_todoJets.at(i);
        }
    }

}


void BFJecView::fillSpecific(const edm::Event& iEvent, const edm::EventSetup& iSetup){


    for (unsigned int i = 0; i < m_todoJets.size();++i){
        edm::Handle<double> hRho;
        iEvent.getByLabel(m_rhos.at(i), hRho);
        double rho = *hRho;
        std::cout << rho << std::endl;
        edm::Handle<edm::View<reco::Jet> > hRecoJets;
        iEvent.getByLabel(m_todoRecoJets.at(i), hRecoJets);
        for (unsigned int iJet = 0; iJet < hRecoJets->size(); ++iJet){
            float pt = hRecoJets->at(iJet).pt();
            float eta = hRecoJets->at(iJet).eta();
            float area = hRecoJets->at(iJet).jetArea();
            std::cout << m_todoJets.at(i) 
                << " " << pt
                << " " << eta
                << " " << area
                << std::endl;
        }

        


    }

    /*
    for (unsigned int i = 0; i < m_todo.size();++i){
        edm::Handle<std::vector<l1extra::L1JetParticle> > hL1;
        iEvent.getByLabel(m_todo.at(i), hL1);
        for (unsigned iL1 = 0; iL1< hL1->size();++iL1){
            if (hL1->at(iL1).bx()!=0){
                std::cout << "Warningn!  L1 cand with bx!=0: " << hL1->at(iL1).pt() << " " << hL1->at(iL1).bx() << std::endl;
            } else {
                addToP4Vec("L1Jets", hL1->at(iL1).p4());
            }
        }
    }*/


}
