#include "MNTriggerStudies/MNTriggerAna/interface/VerticesView.h"
#include "DataFormats/VertexReco/interface/Vertex.h"



VerticesView::VerticesView(const edm::ParameterSet& iConfig, TTree * tree):
EventViewBase(iConfig,  tree)
{

    // register branches
    registerVecFloat("x", tree);
    registerVecFloat("y", tree);
    registerVecFloat("z", tree);
    registerVecFloat("xErr", tree);
    registerVecFloat("yErr", tree);
    registerVecFloat("zErr", tree);

    registerVecInt("isValid", tree);
    registerVecInt("isFake", tree);
    registerVecFloat("chi2", tree);
    registerVecInt("ndof", tree);
    registerVecInt("nTracks", tree);


    m_src = iConfig.getParameter<edm::InputTag>("src");







}


void VerticesView::fillSpecific(const edm::Event& iEvent, const edm::EventSetup& iSetup){

    edm::Handle<std::vector<reco::Vertex> > hIn;
    iEvent.getByLabel(m_src, hIn);
    for (unsigned int i = 0; i< hIn->size();++i){
        addToFVec("x", hIn->at(i).x());
        addToFVec("y", hIn->at(i).y());
        addToFVec("z", hIn->at(i).z());
        addToFVec("xErr", hIn->at(i).xError());
        addToFVec("yErr", hIn->at(i).yError());
        addToFVec("zErr", hIn->at(i).zError());
        addToIVec("isValid", hIn->at(i).isValid());
        addToIVec("isFake", hIn->at(i).isFake());
        addToFVec("chi2", hIn->at(i).chi2());
        addToIVec("ndof", hIn->at(i).ndof());
        addToIVec("nTracks", hIn->at(i).nTracks());
    }

}
