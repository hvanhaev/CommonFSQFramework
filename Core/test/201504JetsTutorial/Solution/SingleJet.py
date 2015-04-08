#!/usr/bin/env python

# to be used with SmallXAnaVersion=CommonFSQFramework.Core.samples.Samples_DiJet_20140122_MN2010
import CommonFSQFramework.Core.ExampleProofReader

import sys, os, time
sys.path.append(os.path.dirname(__file__))

import ROOT
ROOT.gROOT.SetBatch(True)
from ROOT import edm

from array import *

# EX 8.0
from  CommonFSQFramework.Core.BetterJetGetter import BetterJetGetter


class SingleJet(CommonFSQFramework.Core.ExampleProofReader.ExampleProofReader):
    def init( self):
        self.hist = {}
        self.hist["numGenTracks"] =  ROOT.TH1F("numGenTracks",   "numGenTracks",  100, -0.5, 99.5)

        # EX3
        self.hist["numVtx"] =  ROOT.TH1F("numVtx",   "numVtx",  5, -0.5, 4.5)
        self.hist["jetPT"] =  ROOT.TH1F("jetPT",   "jetPT",  100, 0, 100)

        # EX9 
        self.hist["jetBelowEta3PT"] =  ROOT.TH1F("jetBelowEta3PT", "jetBelowEta3PT",  100, 0, 100)
        self.hist["jetBelowEta3Eta"] =  ROOT.TH1F("jetBelowEta3Eta",   "jetBelowEta3Eta" ,  100, -5, 5)
        for h in self.hist:
            self.hist[h].Sumw2()
            self.GetOutputList().Add(self.hist[h])

        # EX 8.0
        self.jetGetter = BetterJetGetter("PFAK5") 

    def analyze(self):
        # ex 4.5
        if self.isData and self.fChain.jet15 < 0.5:
            return 

        weight = 1.
        # EX 6.
        if not self.isData:
            weight *= self.fChain.genWeight

        num = 0

        # genTracks
        #num = self.fChain.genTracks.size()
        #print num
        #print self.maxEta # see slaveParams below
        self.hist["numGenTracks"].Fill(num, weight)

        # EX2.0
        #print "vtx", self.fChain.ngoodVTX

        # EX3.0
        self.hist["numVtx"].Fill(self.fChain.ngoodVTX, weight)

        # EX5.0
        for i in xrange(self.fChain.PFAK5pt.size()):
            pt = self.fChain.PFAK5pt.at(i)
            if pt < 35: continue
            self.hist["jetPT"].Fill(pt, weight)

        # EX 8.0
        self.jetGetter.newEvent(self.fChain)
        #print "New event!"
        for j in self.jetGetter.get("_central"):
             if j.pt()<35.: continue
             #print "A jet: ", j.pt(), j.eta()


        # EX 9.0
        for j in self.jetGetter.get("_central"):
             if j.pt()<35.: continue
             if abs(j.eta())>3.: continue
             self.hist["jetBelowEta3Eta"].Fill(j.eta(), weight)
             self.hist["jetBelowEta3PT"].Fill(j.pt(), weight)


        return 1

    def finalize(self):
        print "Finalize:"
        normFactor = self.getNormalizationFactor()
        # exercise A.2
        #  this is the lumi for jet15 trigger in JetMETtau
        if self.isData:
            print "Expected norm factor is 1. Got", normFactor
            print "Changeing norm factor to have properly normalized data histo"
            normFactor = 1/0.013781

        print "  applying norm", normFactor
        for h in self.hist:
            self.hist[h].Scale(normFactor)

if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    ROOT.gSystem.Load("libFWCoreFWLite.so")
    ROOT.AutoLibraryLoader.enable()

    sampleList = None # run through all
    maxFilesMC = None # run through all ffiles found
    maxFilesData = None # same
    nWorkers = None # Use all cpu cores

    # debug config:
    # Run printTTree.py alone to get the samples list

    # Exercise A.1
    sampleList = []
    sampleList.append("QCD_Pt-15to3000_TuneZ2star_Flat_HFshowerLibrary_7TeV_pythia6")
    sampleList.append("QCD_Pt-15to1000_TuneEE3C_Flat_7TeV_herwigpp")
    sampleList.append("JetMETTau-Run2010A-Apr21ReReco-v1")

    maxFilesMC = 1
    #maxFilesData = 1
    nWorkers = 4


    slaveParams = {}
    slaveParams["maxEta"] = 2.


    # use printTTree.py <sampleName> to see what trees are avaliable inside the skim file
    SingleJet.runAll(treeName="mnXS",
           slaveParameters=slaveParams,
           sampleList=sampleList,
           maxFilesMC = maxFilesMC,
           maxFilesData = maxFilesData,
           nWorkers=nWorkers,
           outFile = "plotsSingleJet.root" )
