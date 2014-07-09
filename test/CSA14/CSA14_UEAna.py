#!/usr/bin/env python
import MNTriggerStudies.MNTriggerAna.ExampleProofReader

import sys, os, time
sys.path.append(os.path.dirname(__file__))

import ROOT
ROOT.gROOT.SetBatch(True)
from ROOT import edm, JetCorrectionUncertainty

from array import *

class CSA14_UEAna(MNTriggerStudies.MNTriggerAna.ExampleProofReader.ExampleProofReader):
    def init( self):

        self.hist = {}
        self.hist["numGenTracks"] =  ROOT.TH1F("numGenTracks",   "numGenTracks",  100, -0.5, 99.5)
        self.hist["etaGenTracks"] =  ROOT.TH1F("etaGenTracks",   "etaGenTracks",  100, -2.5, 2.5)
        self.hist["etaRecoTracks"] =  ROOT.TH1F("etaRecoTracks",   "etaRecoTracks",  100, -2.5, 2.5)
        for h in self.hist:
            self.hist[h].Sumw2()
            self.GetOutputList().Add(self.hist[h])

    def analyze(self):
        weight = 1 # 
        num = 0
        num = self.fChain.genTracks.size()
        self.hist["numGenTracks"].Fill(num, weight)
        for t in self.fChain.genTracks: # this collection contains four-momenta of charged genparticles
            self.hist["etaGenTracks"].Fill(t.eta(), weight)

        return 1

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

    sampleList = None
    maxFilesMC = None
    maxFilesData = None
    nWorkers = None # Use all

    # debug config:
    #'''
    # Run printTTree.py alone to get the samples list
    #sampleList = []
    #sampleList.append("QCD_Pt-15to3000_TuneZ2star_Flat_HFshowerLibrary_7TeV_pythia6")
    maxFilesMC = 1
    maxFilesData = 1
    #nWorkers = 16
    #maxFilesData = 1
    nWorkers = 1
    # '''


    slaveParams = {}
    slaveParams["maxEta"] = 2.


    # use printTTree.py <sampleName> to see what trees are avaliable inside the skim file
    CSA14_UEAna.runAll(treeName="tracksTree",
                               slaveParameters=slaveParams,
                               sampleList=sampleList,
                               maxFilesMC = maxFilesMC,
                               maxFilesData = maxFilesData,
                               nWorkers=nWorkers,
                               outFile = "plotsCSA14_UEAna.root" )



