#include "MNTriggerStudies/MNTriggerAna/interface/EventIdData.h"

EventIdData::EventIdData(const edm::ParameterSet& iConfig, TTree * tree){

    registerInt("run", tree);
    registerInt("lumi", tree);
    registerInt("event", tree);
    registerFloat("genWeight", tree);
    registerFloat("puTrueNumInteractions", tree);


}


void EventIdData::fill(const edm::Event&, const edm::EventSetup&){


}
