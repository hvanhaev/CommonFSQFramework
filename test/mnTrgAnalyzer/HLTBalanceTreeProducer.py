#!/usr/bin/env python

import sys, os, time
sys.path.append(os.path.dirname(__file__))

import ROOT
ROOT.gROOT.SetBatch(True)
ROOT.gSystem.Load("libFWCoreFWLite.so")
ROOT.AutoLibraryLoader.enable()
from ROOT import edm, JetCorrectionUncertainty

from array import *


# Following import breaks things. Why???
#import math

# please note that python selector class name (here: BalanceTreeProducer) 
# should be consistent with this file name (BalanceTreeProducer.py)

# you have to run this file from directory where it is saved


# TODO:
# ln -s ../MNxsectionAna/BalanceTreeProducer.py
from BalanceTreeProducer import BalanceTreeProducer
from MNTriggerStudies.MNTriggerAna.JetGetter import JetGetter

class HLTBalanceTreeProducer(BalanceTreeProducer):
    pass
#    def init(self):
#        pass



if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    ROOT.gSystem.Load("libFWCoreFWLite.so")
    ROOT.AutoLibraryLoader.enable()

    sampleList = None
    maxFilesMC = None
    maxFilesData = None
    nWorkers = None # Use all

    slaveParams = {}
    slaveParams["threshold"] = 35.

    #slaveParams["recoJetCollection"] = "pfJets"
    #slaveParams["recoJetCollection"] = "pfJetsSmear"
    #slaveParams["recoJetCollectionBaseReco"] = "pfJets"
    #slaveParams["recoJetCollectionGEN"] = "pfJets2Gen"
    #slaveParams["recoJetCollection"] = "caloJets"
    #slaveParams["recoJetCollection"] = "caloJetsSmear"

    # TODO: correct JEC uncertainty
    #jetUncFile = "START42_V11_AK5PF_Uncertainty.txt"
    jetUncFile = "START41_V0_AK5PF_Uncertainty.txt"


    slaveParams["jetUncFile"] =  edm.FileInPath("MNTriggerStudies/MNTriggerAna/test/MNxsectionAna/"+jetUncFile).fullPath()
    slaveParams["HLT2015TempWorkaround"] =  True
    slaveParams["doPtShiftsJER"] = False
    slaveParams["doPtShiftsJEC"] = False
    sampleList=["QCD_Pt-300to470_Tune4C_13TeV_pythia8"]
    maxFilesMC = 10
    treeName = "mnTriggerAna"




    HLTBalanceTreeProducer.runAll(treeName=treeName,
                               slaveParameters=slaveParams,
                               sampleList=sampleList,
                               maxFilesMC = maxFilesMC,
                               maxFilesData = maxFilesData,
                               nWorkers=nWorkers,
                               outFile = "treeDiJetBalance.root" )


