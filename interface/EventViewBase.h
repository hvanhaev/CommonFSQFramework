#ifndef EventViewBase_h
#define EventViewBase_h

#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "TTree.h"
#include <algorithm>
#include "DataFormats/Candidate/interface/Candidate.h"


class EventViewBase {
   public:
      EventViewBase() {};
      EventViewBase(const edm::ParameterSet&, TTree * tree);
      void fill(const edm::Event&, const edm::EventSetup&);
      ~EventViewBase();

      void resetVariables();
      // TODO: add protection against booking two branches with same name
      void registerInt(std::string name,  TTree * tree);
      void registerFloat(std::string name, TTree * tree);
      void registerVecP4(std::string name,  TTree * tree);
      void registerVecInt(std::string name,  TTree * tree);

      void setI(std::string name, int val);
      void setF(std::string name, float val);
      void addToIVec(std::string name, int val);
      void addToP4Vec(std::string name, reco::Candidate::LorentzVector val);


   private:
      virtual void fillSpecific(const edm::Event&, const edm::EventSetup&) = 0;
      std::map<std::string, int> m_integerBranches;
      std::map<std::string, float> m_floatBranches;
      std::map<std::string, std::vector<reco::Candidate::LorentzVector> > m_vectorBranches;
      std::map<std::string, std::vector<int> > m_vecIntBranches;

      std::string m_branchPrefix;  


};
#endif
