#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "TTree.h"
#include <algorithm>
#include "DataFormats/Candidate/interface/Candidate.h"
#include "EventViewBase.h"

// Note: in c++ a reference to a map element is guaranteed to stay valid 
// (ie the element wont change place in the memory) - AKA "this is a safe 
// approach to doing root trees
void EventViewBase::registerInt(std::string name,  TTree * tree){
    m_integerBranches[name] = 0;
    tree->Branch(name.c_str(), & m_integerBranches[name], (name+"/I").c_str());
}
void EventViewBase::registerFloat(std::string name,  TTree * tree){
    m_floatBranches[name] = 0;
    tree->Branch(name.c_str(), & m_floatBranches[name], (name+"/F").c_str());
}
void EventViewBase::registerVecP4(std::string name,  TTree * tree){
    m_vectorBranches[name] = std::vector<reco::Candidate::LorentzVector>();
    tree->Branch(name.c_str(), &m_vectorBranches[name]);
}
void EventViewBase::registerVecInt(std::string name,  TTree * tree){
    m_vecIntBranches[name] = std::vector<int>();
    tree->Branch(name.c_str(), "std::vector< int >", &m_vecIntBranches[name]);
}

EventViewBase::EventViewBase(const edm::ParameterSet& iConfig){}


void EventViewBase::resetVariables(){
    // int branches
    {
        std::map<std::string, int>::iterator it =  m_integerBranches.begin();
        std::map<std::string, int>::iterator itE =  m_integerBranches.end();
        for (;it != itE;++it){
                m_integerBranches[it->first]=0;
        }
    }
    // float branches
    {
        std::map<std::string, float>::iterator it =  m_floatBranches.begin();
        std::map<std::string, float>::iterator itE =  m_floatBranches.end();
        for (;it != itE;++it){
                m_floatBranches[it->first]=0;
        }
    }
    //
    {
        std::map<std::string, std::vector<reco::Candidate::LorentzVector> >::iterator it =  m_vectorBranches.begin();
        std::map<std::string, std::vector<reco::Candidate::LorentzVector> >::iterator itE =  m_vectorBranches.end();
        for (;it != itE;++it){
            m_vectorBranches[it->first].clear();
        }
    }
    // int vector branches autoreg
    {   
        std::map<std::string, std::vector<int> >::iterator it =  m_vecIntBranches.begin();
        std::map<std::string, std::vector<int> >::iterator itE =  m_vecIntBranches.end();
        for (;it != itE;++it){
            m_vecIntBranches[it->first].clear();
        }
    }

}

EventViewBase::~EventViewBase()
{
 

}

