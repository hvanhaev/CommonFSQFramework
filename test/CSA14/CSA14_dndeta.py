#!/usr/bin/env python
import MNTriggerStudies.MNTriggerAna.ExampleProofReader
from  MNTriggerStudies.MNTriggerAna.RecoTracksGetter import RecoTracksGetter

import sys, os, time
sys.path.append(os.path.dirname(__file__))

import ROOT
ROOT.gROOT.SetBatch(True)

class CSA14_dndeta(MNTriggerStudies.MNTriggerAna.ExampleProofReader.ExampleProofReader):
    def init( self):
        #self.triggers   = ["minbias", "zerobias"]
        self.triggers   = ["minbias", ]
        self.variations = ["central"] # only a central value now
        
        self.hist = {}
        for t in self.triggers:
            for v in self.variations:
                histPostfix = "_" + v + "_" + t
                ptName = "pt"+histPostfix
                self.hist[ptName] =  ROOT.TH1F(ptName, ptName+";p_T [GeV]",  100,  0, 10)
                etaName = "eta"+histPostfix
                self.hist[etaName] =  ROOT.TH1F(etaName, etaName+"; #eta",  100, -2.7, 2.7)

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
        self.tracks.newEvent(self.fChain) # 

        for trg in self.triggers: # iterate over all triggers we use
            trigger = False
            if trg == "minbias":
                trigger = True  # TODO in future versions: actually check for trigger
            elif trg == "zerobias":
                trigger = True  # TODO: as above

            if not trigger: continue

            # iterate over all variations (again - placs is a placeeholder for future)
            #  eg.  if we would use jets our variations would look like
            #   ["central", "jecUp", "jecDown"]  
            #   our JetGetter (not used here) is smart enough to give jets with momentum variaed for +1sigma
            #     when calling self.jetGetter.get("jecUp") (and -1sigma for jecDown)
            for variation in self.variations: 
                histPostfix = "_" + variation + "_" + trg
                for track in self.tracks.get(variation):
                    trackp4 = track.recoTracks # wrong naming in Samples_CSA14_Tracks_20140904 skim. 
                                               # this will evolve to trackp4 = track.p4 in next version 
                    eta = trackp4.eta()
                    pt =    trackp4.pt()
                    self.hist["pt"+histPostfix].Fill(pt, weight) # always use weight when filling
                    self.hist["eta"+histPostfix].Fill(eta, weight) # always use weight when filling

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
    #quickTest = True
    
    if quickTest:
        # Run printTTree.py alone to get the samples list
        #sampleList = []
        #sampleList.append("data_MinBias_TuneCUETP8S1-HERAPDF_13TeV-pythia8")
        maxFilesMC = 1
        maxFilesData = 1
        nWorkers = 1

    # another possibility to process bit faster: process only part of MC
    maxFilesMC = 12
    #maxFilesData = 12
    #nWorkers = 12

    # only processin part of data will lead to wrong normalization of the data histograms
    # - since lumi values are not automatically updated to reflect the fact that only
    # part of sample was processed
    #
    # This is not a problem for MC, while here normalization factor is calculated using
    # number of processed events


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



