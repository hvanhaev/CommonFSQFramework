#!/usr/bin/env python
import MNTriggerStudies.MNTriggerAna.ExampleProofReader
from  MNTriggerStudies.MNTriggerAna.RecoTracksGetter import RecoTracksGetter


import sys, os, time
sys.path.append(os.path.dirname(__file__))

import ROOT
ROOT.gROOT.SetBatch(True)

#from array import *

class CSA14_dndeta(MNTriggerStudies.MNTriggerAna.ExampleProofReader.ExampleProofReader):
    def init( self):
        self.hist = {}
        self.hist["pt"] =  ROOT.TH1F("pt", "pt;p_T [GeV]",  100, -2.6, 2.6)
        self.hist["eta"] =  ROOT.TH1F("eta",   "eta; #eta",  100, -2.6, 2.6)
        for h in self.hist:
            self.hist[h].Sumw2()
            self.GetOutputList().Add(self.hist[h])

        self.tracks = RecoTracksGetter("recoTracks")

    def analyze(self):
        weight = 1 # 
        # weight = self.fChain.genWeight to obtain gen level weight. For min bias datasets we are using for CSA14 always eq to 1

        # direct access to branch to compare efficiency as when getter is used:
        #for i in xrange(self.fChain.recoTracksrecoTracks.size()):
        #    trackp4 = self.fChain.recoTracksrecoTracks.at(i)
        self.tracks.newEvent(self.fChain)
        for track in self.tracks.get():
            trackp4 = track.recoTracks # note : in next skim this will become: trackp4 = track.p4
            eta = trackp4.eta()
            pt =    trackp4.pt()
            self.hist["pt"].Fill(pt, weight) # always use weight when filling
            self.hist["eta"].Fill(eta, weight) # always use weight when filling
            


        return 1

    # note: this is executed on the slave (ie output will appear in logs),
    #       - before merging the histograms. Here we should apply the histogram 
    #         normalization factor (since this depend on how many events were processed
    #         by given slave)
    def finalize(self):
        print "Finalize:"
        normFactor = self.getNormalizationFactor()
        print "  isData", self.isData
        print "  applying norm",  normFactor
        for h in self.hist:
            self.hist[h].Scale(normFactor)

    # this is executed once at the master after merging the histograms from slaves
    # (note: all histograms registered via self.GetOutputList().Add above are merged)
    def finalizeWhenMerged(self):
        #olist =  self.GetOutputList() # rebuild the histos list
        #histos = {}
        #for o in olist:
        #    if not "TH1" in o.ClassName(): continue
        #    histos[o.GetName()]=o

        #
        # you can save further histograms to the output file by calling:
        #self.GetOutputList().Add(myNewHisto)
        #
        pass


if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    ROOT.gSystem.Load("libFWCoreFWLite.so")
    ROOT.AutoLibraryLoader.enable()

    sampleList = None
    maxFilesMC = None
    maxFilesData = None
    nWorkers = None # Use all cores

    quickTest = False
    quickTest = True
    
    if quickTest:
        # Run printTTree.py alone to get the samples list
        sampleList = []
        sampleList.append("data_MinBias_TuneCUETP8S1-HERAPDF_13TeV-pythia8")
        maxFilesMC = 1
        maxFilesData = 1
        nWorkers = 1


    slaveParams = {}
    slaveParams["maxEta"] = 2.


    # use printTTree.py <sampleName> to see what trees are avaliable inside the skim file
    CSA14_dndeta.runAll(treeName="tracksTree",
                               slaveParameters=slaveParams,
                               sampleList=sampleList,
                               maxFilesMC = maxFilesMC,
                               maxFilesData = maxFilesData,
                               nWorkers=nWorkers,
                               outFile = "plotsCSA14_dndeta.root" )



