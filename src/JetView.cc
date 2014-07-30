#include "MNTriggerStudies/MNTriggerAna/interface/JetView.h"
#include <DataFormats/TrackReco/interface/Track.h>
#include <DataFormats/VertexReco/interface/Vertex.h>
#include "MNTriggerStudies/MNTriggerAna/interface/TestTrackData.h"

// https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuidePhysicsCutParser - should I ?

JetView::JetView(const edm::ParameterSet& iConfig, TTree * tree){
    registerVecP4("recoTracks", tree);
    registerVecFloat("dz", tree);
    registerVecFloat("dxy", tree);

    m_maxEta = iConfig.getParameter<double>("maxEta");
    m_minPt = iConfig.getParameter<double>("minPt");
    m_maxnum = iConfig.getParameter<double>("maxnum"); // save maxnum hardest jets

    m_inputCol = iConfig.getParameter<edm::InputTag>("input");

    std::vector<std::string> JERdesc = iConfig.getParameter<std::vector<std::string> >("jerFactors");

    /*         for line in todo:
            spl = line.split()
            etaMax = float(spl[0])
            jer = float(spl[1])
            err = float(spl[2])
            errUp = float(spl[3])
            errDown = float(spl[4])
            jerUp   = jer + ROOT.TMath.Sqrt(err*err+errUp*errUp)
            jerDown = jer - ROOT.TMath.Sqrt(err*err+errDown*errDown)
            print "JER factors:", etaMax, jer, jerUp, jerDown, "|", err, errUp, errDown
            self.JER.append( [etaMax, jer, jerUp, jerDown] )
    */

    

}


void JetView::fillSpecific(const edm::Event& iEvent, const edm::EventSetup& iSetup){
}
