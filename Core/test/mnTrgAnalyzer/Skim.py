#!/usr/bin/env python

import sys, os, time
sys.path.append(os.path.dirname(__file__))

import ROOT
ROOT.gROOT.SetBatch(True)
ROOT.gSystem.Load("libFWCoreFWLite.so")
ROOT.AutoLibraryLoader.enable()
from ROOT import edm, JetCorrectionUncertainty

from array import *

# please note that python selector class name (here: Skim) 
# should be consistent with this file name (Skim.py)

# you have to run this file from directory where it is saved
import MNTriggerStudies.MNTriggerAna.ExampleProofReader 
from MNTriggerStudies.MNTriggerAna.JetGetter import JetGetter

class Skim(MNTriggerStudies.MNTriggerAna.ExampleProofReader.ExampleProofReader):
    def init(self):
        self.initialized = False
        pass

    def analyze(self):
        if not self.initialized:
            self.initialized = True
            self.tree = self.fChain.CloneTree(0)
            self.GetOutputList().Add(self.tree)

        if self.fChain.PUNumInteractions == 0:
            self.tree.Fill()

if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    ROOT.gSystem.Load("libFWCoreFWLite.so")
    ROOT.AutoLibraryLoader.enable()

    sampleList = None
    maxFilesMC = None
    maxFilesData = None
    nWorkers = None # Use all

    # debug config:
    '''
    sampleList=[]
    sampleList.append("QCD_Pt-15to3000_TuneZ2star_Flat_HFshowerLibrary_7TeV_pythia6")
    maxFilesData = 1
    '''
    sampleList=[]
    sampleList.append("QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8")
    maxFilesMC = 1
    nWorkers = 1
    #'''

    slaveParams = {}

    Skim.runAll(treeName="MNTriggerAnaNew",
                               slaveParameters=slaveParams,
                               sampleList=sampleList,
                               maxFilesMC = maxFilesMC,
                               maxFilesData = maxFilesData,
                               nWorkers=nWorkers,
                               outFile = "skimmed.root" )

