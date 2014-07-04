#include "MNTriggerStudies/MNTriggerAna/interface/GenTrackView.h"
#include "SimDataFormats/GeneratorProducts/interface/GenEventInfoProduct.h"
#include "SimDataFormats/PileupSummaryInfo/interface/PileupSummaryInfo.h"

GenTrackView::GenTrackView(const edm::ParameterSet& iConfig, TTree * tree){
    registerVecP4("genTracks", tree);
    m_maxEta = iConfig.getUntrackedParameter<double>("maxEta", 6);
    m_charge = iConfig.getUntrackedParameter<int>("charge", 1);

}


void GenTrackView::fill(const edm::Event& iEvent, const edm::EventSetup& iSetup){

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
