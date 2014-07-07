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


void EventIdData::fillSpecific(const edm::Event& iEvent, const edm::EventSetup& iSetup){

    setI("run", iEvent.eventAuxiliary().run());
    setI("lumi", iEvent.eventAuxiliary().luminosityBlock());
    setI("event", iEvent.eventAuxiliary().event());

    edm::Handle<GenEventInfoProduct> hGW; 
    iEvent.getByLabel(edm::InputTag("generator"), hGW);
    setF("genWeight", hGW->weight());

    edm::Handle< std::vector<PileupSummaryInfo> > hPU;
    iEvent.getByLabel(edm::InputTag("addPileupInfo"), hPU);
    for (unsigned int i = 0; i< hPU->size();++i){
        if (hPU->at(i).getBunchCrossing() == 0) {
            setF("puTrueNumInteractions",  hPU->at(i).getTrueNumInteractions());
            break;
        }
    }

}
