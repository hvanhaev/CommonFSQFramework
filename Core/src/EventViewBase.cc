#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "TTree.h"
#include <algorithm>
#include "DataFormats/Candidate/interface/Candidate.h"
#include "CommonFSQFramework/Core/interface/EventViewBase.h"

// Note: in c++ a reference to a map element is guaranteed to stay valid 
// (ie the element wont change place in the memory) - AKA "this is a safe 
// approach to doing root trees
void EventViewBase::registerInt(std::string name,  TTree * tree){
    m_integerBranches[m_branchPrefix+name] = 0;
    tree->Branch((m_branchPrefix+name).c_str(), & m_integerBranches[m_branchPrefix+name], (m_branchPrefix+name+"/I").c_str());
}
void EventViewBase::registerFloat(std::string name,  TTree * tree){
    m_floatBranches[m_branchPrefix+name] = 0;
    tree->Branch((m_branchPrefix+name).c_str(), & m_floatBranches[m_branchPrefix+name], (m_branchPrefix+name+"/F").c_str());
}
void EventViewBase::registerVecP4(std::string name,  TTree * tree){
    m_vectorBranches[m_branchPrefix+name] = std::vector<reco::Candidate::LorentzVector>();
    tree->Branch((m_branchPrefix+name).c_str(), &m_vectorBranches[m_branchPrefix+name]);
}
void EventViewBase::registerVecInt(std::string name,  TTree * tree){
    m_vecIntBranches[m_branchPrefix+name] = std::vector<int>();
    tree->Branch((m_branchPrefix+name).c_str(), "std::vector< int >", &m_vecIntBranches[m_branchPrefix+name]);
}


void EventViewBase::registerVecFloat(std::string name,  TTree * tree){
    m_vecFloatBranches[m_branchPrefix+name] = std::vector<float>();
    tree->Branch((m_branchPrefix+name).c_str(), "std::vector< float >", &m_vecFloatBranches[m_branchPrefix+name]);
}



void EventViewBase::setI(std::string name, int val){
    m_integerBranches[m_branchPrefix+name] = val;
}

void EventViewBase::setF(std::string name, float val){
    m_floatBranches[m_branchPrefix+name] = val;
}

void EventViewBase::addToIVec(std::string name, int val){
    m_vecIntBranches[m_branchPrefix+name].push_back(val);
}

void EventViewBase::addToFVec(std::string name, float val){
    m_vecFloatBranches[m_branchPrefix+name].push_back(val);
}

void EventViewBase::addToP4Vec(std::string name, reco::Candidate::LorentzVector val){
    m_vectorBranches[m_branchPrefix+name].push_back(val);
}

EventViewBase::EventViewBase(const edm::ParameterSet& iConfig, TTree * tree){
    m_branchPrefix = iConfig.getUntrackedParameter<std::string>("branchPrefix","");
}


void EventViewBase::fill(const edm::Event& iEvent, const edm::EventSetup& iSetup){
    resetVariables();
    fillSpecific(iEvent, iSetup);
}

void EventViewBase::doBeginRun(const edm::Run& r, const edm::EventSetup& es) {
    // do nothing here, overwrite this in derived miniView class

}

void EventViewBase::doEndRun(const edm::Run& r, const edm::EventSetup& es) {
    // do nothing here, overwrite this in derived miniView class
    
}


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
    // 
    {   
        std::map<std::string, std::vector<int> >::iterator it =  m_vecIntBranches.begin();
        std::map<std::string, std::vector<int> >::iterator itE =  m_vecIntBranches.end();
        for (;it != itE;++it){
            m_vecIntBranches[it->first].clear();
        }
    }

    // 
    {   
        std::map<std::string, std::vector<float> >::iterator it =  m_vecFloatBranches.begin();
        std::map<std::string, std::vector<float> >::iterator itE =  m_vecFloatBranches.end();
        for (;it != itE;++it){
            m_vecFloatBranches[it->first].clear();
        }
    }




}

EventViewBase::~EventViewBase()
{
 

}

