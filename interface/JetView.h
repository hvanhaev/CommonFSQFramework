#ifndef JetView_h
#define JetView_h

#include "MNTriggerStudies/MNTriggerAna/interface/EventViewBase.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "PhysicsTools/SelectorUtils/interface/PFJetIDSelectionFunctor.h"
#include "PhysicsTools/SelectorUtils/interface/JetIDSelectionFunctor.h"

#include "CondFormats/JetMETObjects/interface/JetCorrectionUncertainty.h"


class JetView: public EventViewBase{
    public:
       JetView(const edm::ParameterSet& ps, TTree * tree);

    private:
      virtual void fillSpecific(const edm::Event&, const edm::EventSetup&);
      float m_maxEta; // 
      float m_minPt;
      float m_maxnum; // 
      std::vector<std::vector<float> > m_JER;
      std::vector<std::string> m_variations;
 

      edm::InputTag m_inputCol;


      int jetID(const pat::Jet & jet, const edm::Event& iEvent);
      PFJetIDSelectionFunctor pfJetID;
      JetIDSelectionFunctor caloJetID;
      reco::Candidate::LorentzVector getMomentum(const pat::Jet & jet, std::string variation);
      reco::Candidate::LorentzVector smear(const reco::Candidate::LorentzVector & gen, 
                                           const reco::Candidate::LorentzVector & reco,
                                           std::string variation);
      JetCorrectionUncertainty  * m_jecUnc;
      reco::Candidate::LorentzVector shiftJEC(const reco::Candidate::LorentzVector &rec,  std::string variation);

      edm::InputTag m_caloBase;
      edm::InputTag m_caloBaseID;
      bool m_disableJetID;

      int m_storageVersion; // 0 - use p4; 1 - use floats for pt, eta, phi


};
#endif
