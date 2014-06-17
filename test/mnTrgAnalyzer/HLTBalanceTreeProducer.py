#!/usr/bin/env python

import sys, os, time
sys.path.append(os.path.dirname(__file__))

import ROOT
ROOT.gROOT.SetBatch(True)
ROOT.gSystem.Load("libFWCoreFWLite.so")
ROOT.AutoLibraryLoader.enable()
from ROOT import edm, JetCorrectionUncertainty

#from array import *


# Following import breaks things. Why???
#import math

# please note that python selector class name (here: BalanceTreeProducer) 
# should be consistent with this file name (BalanceTreeProducer.py)

# you have to run this file from directory where it is saved


# TODO:
# ln -s ../MNxsectionAna/BalanceTreeProducer.py
from BalanceTreeProducer import BalanceTreeProducer as EE
#from MNTriggerStudies.MNTriggerAna.ExampleProofReader import ExampleProofReader as EE
from MNTriggerStudies.MNTriggerAna.JetGetter import JetGetter

class HLTBalanceTreeProducer(EE):
    #def init(self):
    #    print "XX2!"
        #self.balanceProd =  BalanceTreeProducer()
        #self.GetOutputList().Add(self.tree)

    def analyze(self):
        print "XAXA" ,  self.HLTptAve
        # hltAK5PFJetL1FastL2L3Corrected
        #setattr(self.fChain, "ngoodVTX", 2) # TODO: fChain proxy ?!?

        hltJets = self.fChain.hltAK5PFJetL1FastL2L3Corrected
        probe = None
        tag = None

        for j in hltJets:
            pt = j.pt()
            eta = abs(j.eta())
            tagCand = eta < 1.4
            probeCand = eta > 2.8 and eta < 5.2

            if probeCand and (probe == None or probe.pt() < pt): probe = j
            if tagCand and (tag == None or tag.pt() < pt): tag = j

        if probe != None and tag!=None  and probe != tag:
            ptAve = (tag.pt() + probe.pt())/2.
            if ptAve > self.HLTptAve:
                #print "XX"
                EE.analyze(self)

    def finalize(self):
        print "Finalize HLTBala:"




if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    #ROOT.gSystem.Load("libFWCoreFWLite.so")
    #ROOT.AutoLibraryLoader.enable()

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

    #slaveParams["HLTptAve"] = 15

    sampleList=["QCD_Pt-300to470_Tune4C_13TeV_pythia8"]
    nWorkers = 1
    maxFilesMC = 1
    #treeName = "mnTriggerAna"


    todo = [300, 400]
    o = HLTBalanceTreeProducer()
    for t in todo:
        out = "treeDiJetBalance_"+str(t)+".root"
        slaveParams["HLTptAve"] = t
        o.runAll(treeName="mnTriggerAna",
                               slaveParameters=slaveParams,
                               sampleList=sampleList,
                               maxFilesMC = maxFilesMC,
                               maxFilesData = maxFilesData,
                               nWorkers=nWorkers,
                               outFile = out )
        del o


