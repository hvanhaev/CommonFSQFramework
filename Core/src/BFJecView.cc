#include "MNTriggerStudies/MNTriggerAna/interface/BFJecView.h"
#include "DataFormats/JetReco/interface/Jet.h"
#include <DataFormats/Math/interface/deltaR.h>

BFJecView::BFJecView(const edm::ParameterSet& iConfig, TTree * tree):
EventViewBase(iConfig,  tree)
{
    //registerVecP4("L1Jets", tree);
    m_todoJets = iConfig.getParameter<std::vector<std::string> >("todoJets");
    m_minPT = iConfig.getParameter<double>("minPT");
    m_minPTGen = iConfig.getParameter<double>("minPTGen");
    m_maxEta = iConfig.getParameter<double>("maxEta");

    // minPt, maxEta
    for (unsigned int i=0; i < m_todoJets.size();++i){
        if (iConfig.exists(m_todoJets.at(i))) {
            std::vector<edm::InputTag> itag = iConfig.getParameter<std::vector<edm::InputTag> >(m_todoJets.at(i));
            if (itag.size()!=3) {
                throw "Parameter " + m_todoJets.at(i) + " should have three inputtags";
            }

           registerFloat(m_todoJets.at(i)+"rho", tree);
           registerVecFloat(m_todoJets.at(i)+"pt", tree);
           registerVecFloat(m_todoJets.at(i)+"ptGenRatio", tree);
           registerVecFloat(m_todoJets.at(i)+"ptGen", tree);
           registerVecFloat(m_todoJets.at(i)+"bestdr", tree);
           registerVecFloat(m_todoJets.at(i)+"eta", tree);
           registerVecFloat(m_todoJets.at(i)+"area", tree);
 
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

        if (m_rhos.at(i).label() != ""){
            iEvent.getByLabel(m_rhos.at(i), hRho);
            double rho = *hRho;
            //std::cout << rho << std::endl;
            setF(m_todoJets.at(i)+"rho", rho);
            //addToIVec
        }

        edm::Handle<edm::View<reco::Jet> > hRecoJets;
        iEvent.getByLabel(m_todoRecoJets.at(i), hRecoJets);

        edm::Handle<edm::View<reco::Jet> > hGenJets;
        iEvent.getByLabel(m_todoGenJets.at(i), hGenJets);
        for (unsigned int iJet = 0; iJet < hRecoJets->size(); ++iJet){
            float pt = hRecoJets->at(iJet).pt();
            if (pt < m_minPT) continue; 

            float bestDR = 99;
            float bestPtGen = -1;
            for(unsigned int iGen = 0; iGen < hGenJets->size(); ++iGen){
                float dr = reco::deltaR(hGenJets->at(iGen).p4(),  hRecoJets->at(iJet).p4());
                if (dr < bestDR){
                    bestDR = dr;
                    bestPtGen = hGenJets->at(iGen).pt();
                }
            }
            if (bestPtGen < m_minPTGen) continue;


            float eta = hRecoJets->at(iJet).eta();
            if (eta > std::abs(m_maxEta)) continue; // gen or rec??

            float area = hRecoJets->at(iJet).jetArea();


            addToFVec(m_todoJets.at(i)+"pt", pt);
            float ratio = -1;
            if (bestPtGen > 0){
                ratio = bestPtGen/pt;
            }
            addToFVec(m_todoJets.at(i)+"bestdr", bestDR);
            addToFVec(m_todoJets.at(i)+"ptGenRatio", ratio);
            addToFVec(m_todoJets.at(i)+"ptGen", bestPtGen);
            addToFVec(m_todoJets.at(i)+"eta", eta);
            addToFVec(m_todoJets.at(i)+"area", area);

            

            /*
            std::cout << m_todoJets.at(i) 
                << " " << pt
                << " " << eta
                << " " << area
                << std::endl;*/
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
