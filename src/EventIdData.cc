#include "MNTriggerStudies/MNTriggerAna/interface/EventIdData.h"
#include "SimDataFormats/GeneratorProducts/interface/GenEventInfoProduct.h"
#include "SimDataFormats/PileupSummaryInfo/interface/PileupSummaryInfo.h"

EventIdData::EventIdData(const edm::ParameterSet& iConfig, TTree * tree){

    registerInt("run", tree);
    registerInt("lumi", tree);
    registerInt("event", tree);
    registerFloat("genWeight", tree);
    registerFloat("puTrueNumInteractions", tree);


}


void EventIdData::fill(const edm::Event& iEvent, const edm::EventSetup& iSetup){

    set("run", iEvent.eventAuxiliary().run());
    set("lumi", iEvent.eventAuxiliary().luminosityBlock());
    set("event", iEvent.eventAuxiliary().event());
    /*
    m_integerBranches["run"] = iEvent.eventAuxiliary().run();
    m_integerBranches["lumi"] = iEvent.eventAuxiliary().luminosityBlock();
    m_integerBranches["event"] = iEvent.eventAuxiliary().event();
        edm::Handle<GenEventInfoProduct> hGW; 
        iEvent.getByLabel(edm::InputTag("generator"), hGW);
        m_floatBranches["genWeight"] = hGW->weight();

        edm::Handle< std::vector<PileupSummaryInfo> > hPU;
        iEvent.getByLabel(edm::InputTag("addPileupInfo"), hPU);
        for (unsigned int i = 0; i< hPU->size();++i){
            if (hPU->at(i).getBunchCrossing() == 0) {
                m_floatBranches["puTrueNumInteractions"] = hPU->at(i).getTrueNumInteractions();
                break;
            }
        }

    */
}
