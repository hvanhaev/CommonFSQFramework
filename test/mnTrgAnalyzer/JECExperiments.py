#!/usr/bin/env python
import MNTriggerStudies.MNTriggerAna.ExampleProofReader
from  MNTriggerStudies.MNTriggerAna.GenericGetter import GenericGetter

import sys, os, time
sys.path.append(os.path.dirname(__file__))

import ROOT
ROOT.gROOT.SetBatch(True)
from ROOT import edm

from array import *

class JECExperiments(MNTriggerStudies.MNTriggerAna.ExampleProofReader.ExampleProofReader):
    def init( self):
        self.jets = GenericGetter("hltAK4PFJetsCorrected", "eta") 

        self.hist = {}
        self.hist["pt"] =  ROOT.TH1F("pt",   "pt",  100, -0.5, 99.5)
        self.hist["eta"] =  ROOT.TH1F("eta",   "eta",  100, -5.5, 5.5)
        '''
            area
            bestdr
            eta
            pt
            ptGen
            ptGenRatio
            rho
        '''

        for h in self.hist:
            self.hist[h].Sumw2()
            self.GetOutputList().Add(self.hist[h])

    def analyze(self):
        weight = 1
        self.jets.newEvent(self.fChain)
        if self.jets:
            hardestJet = max(self.jets.get(""), key = lambda j: j.pt)
            self.hist["pt"].Fill(hardestJet.pt, weight)
            self.hist["eta"].Fill(hardestJet.eta, weight)

        return


    def finalize(self):
        print "Finalize:"
        normFactor = self.getNormalizationFactor()
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
    #sampleList = []
    #sampleList.append("QCD_Pt-15to3000_TuneZ2star_Flat_HFshowerLibrary_7TeV_pythia6")
    maxFilesMC = 1
    maxFilesData = 1
    nWorkers = 1


    slaveParams = {}
    slaveParams["maxEta"] = 2.


    # use printTTree.py <sampleName> to see what trees are avaliable inside the skim file
    JECExperiments.runAll(treeName="BFJecTreeProducerHighPT",
           slaveParameters=slaveParams,
           sampleList=sampleList,
           maxFilesMC = maxFilesMC,
           maxFilesData = maxFilesData,
           nWorkers=nWorkers,
           outFile = "plotsJECExperiments.root" )
