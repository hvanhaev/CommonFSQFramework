#!/usr/bin/env python


import sys, os, time
sys.path.append(os.path.dirname(__file__))

import ROOT
ROOT.gROOT.SetBatch(True)
from ROOT import *

from array import *
#import cProfile

# please note that python selector class name (here: DiJetBalanceTreeProducer) 
# should be consistent with this file name (DiJetBalanceTreeProducer.py)

# you have to run this file from directory where it is saved


from MNTriggerStudies.MNTriggerAna.ExampleProofReader import ExampleProofReader

#import DiJetBalancePlugin

class DiJetBalanceTreeProducer(ExampleProofReader):
    def configureAnalyzer( self):

        self.tree = ROOT.TTree("data", "data")
        self.GetOutputList().Add(self.tree)

        self.var = {}
        self.var["tagPt"] = array('f', [0])
        self.var["tagEta"] = array('f', [0])

        for v in self.var:
            self.tree.Branch(v, self.var[v], v+"/F")

        self.todoShifts = ["_central"]
        if hasattr(self, "jetUncFile") and not self.isData and self.doPtShifts:
            self.todoShifts.append("_ptUp")
            self.todoShifts.append("_ptDown")
            self.jetUnc = JetCorrectionUncertainty(self.jetUncFile)

        
        

        jet15FileV2 = edm.FileInPath("MNTriggerStudies/MNTriggerAna/test/MNxsectionAna/data/PUJet15V2.root").fullPath()   # MC gen distribution
        puFiles = {}
        puFiles["dj15_1"] = edm.FileInPath("MNTriggerStudies/MNTriggerAna/test/MNxsectionAna/data/pu_dj15_1_0.root").fullPath()
        puFiles["dj15_1_05"] = edm.FileInPath("MNTriggerStudies/MNTriggerAna/test/MNxsectionAna/data/pu_dj15_1_05.root").fullPath()
        puFiles["dj15_0_95"] = edm.FileInPath("MNTriggerStudies/MNTriggerAna/test/MNxsectionAna/data/pu_dj15_0_95.root").fullPath()
        puFiles["j15_1"] = edm.FileInPath("MNTriggerStudies/MNTriggerAna/test/MNxsectionAna/data/pu_j15_1_0.root").fullPath()
        puFiles["j15_1_05"] = edm.FileInPath("MNTriggerStudies/MNTriggerAna/test/MNxsectionAna/data/pu_j15_1_05.root").fullPath()
        puFiles["j15_0_95"] = edm.FileInPath("MNTriggerStudies/MNTriggerAna/test/MNxsectionAna/data/pu_j15_0_95.root").fullPath()

        self.lumiWeighters = {}
        self.lumiWeighters["_jet15_central"] = edm.LumiReWeighting(jet15FileV2, puFiles["j15_1"], "MC", "pileup")
        self.lumiWeighters["_jet15_puUp"] = edm.LumiReWeighting(jet15FileV2, puFiles["j15_1_05"], "MC", "pileup")
        self.lumiWeighters["_jet15_puDown"] = edm.LumiReWeighting(jet15FileV2, puFiles["j15_0_95"], "MC", "pileup")

        self.lumiWeighters["_dj15fb_central"] = edm.LumiReWeighting(jet15FileV2, puFiles["dj15_1"], "MC", "pileup")
        self.lumiWeighters["_dj15fb_puUp"] = edm.LumiReWeighting(jet15FileV2, puFiles["dj15_1_05"], "MC", "pileup")
        self.lumiWeighters["_dj15fb_puDown"] = edm.LumiReWeighting(jet15FileV2, puFiles["dj15_0_95"], "MC", "pileup")


    def ptShifted(self, jet, shift):
        if not shift.startswith("_pt"): return jet.pt()
        if self.isData:
            raise Exception("pt shift for data called")


        pt = jet.pt()
        self.jetUnc.setJetEta(jet.eta())
        self.jetUnc.setJetPt(pt) # corrected pt
        unc = self.jetUnc.getUncertainty(true)
        if "_ptUp" == shift:
            ptFactor = 1.
        elif "_ptDown" == shift:
            ptFactor = -1.
        pt *= (1. + ptFactor*unc)

        if pt < 0: return 0
        return pt 



    #def analyzeTT(self):
    def analyze(self):
            
        #if self.fChain.jet15 > 0.5:
        #    print "XXX", self.fChain.run, self.fChain.lumi
        #    sys.stdout.flush()
        #print "testXX", self.datasetName, self.isData
        #sys.stdout.flush()
        #event = self.fChain.event
        #run = self.fChain.run
        #lumi = self.fChain.lumi
        #print event

        #print "XXDS", self.datasetName, self.isData
        if self.fChain.ngoodVTX == 0: return

        recoJets = getattr(self.fChain, self.recoJetCollection)

        for shift in self.todoShifts:
            weightBase = 1. 
            if not self.isData:
                weightBase *= self.fChain.genWeight # keep inside shift iter


            fill = False
            for i in xrange(0, recoJets.size()):
                jet = recoJets.at(i)
                pt = self.ptShifted(jet, shift)
                if pt < 30: continue
                eta = abs(jet.eta())
                if eta < 1.4:
                    self.var["tagPt"][0] = pt
                    self.var["tagEta"][0] = eta
                    fill = True
                
            if fill:
                print "Filll!"
                self.tree.Fill()

        return 1


if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    ROOT.gSystem.Load("libFWCoreFWLite.so")
    AutoLibraryLoader.enable()

    sampleList = None
    maxFiles = None
    nWorkers = None # Use all

    # debug config:
    sampleList= ["QCD_Pt-15to3000_TuneZ2star_Flat_HFshowerLibrary_7TeV_pythia6"]
    #sampleList=  ["JetMETTau-Run2010A-Apr21ReReco-v1"]
    #sampleList=  ["Jet-Run2010B-Apr21ReReco-v1"] 
    #sampleList = ["JetMET-Run2010A-Apr21ReReco-v1"]
    #sampleList = ["JetMETTau-Run2010A-Apr21ReReco-v1", "Jet-Run2010B-Apr21ReReco-v1", "JetMET-Run2010A-Apr21ReReco-v1", "METFwd-Run2010B-Apr21ReReco-v1"]
    #maxFiles = 2
    maxFiles = 1
    nWorkers = 1


    slaveParams = {}
    slaveParams["threshold"] = 35.
    #slaveParams["doPtShifts"] = False
    slaveParams["doPtShifts"] = True
    #slaveParams["recoJetCollection"] = "pfJets"
    slaveParams["recoJetCollection"] = "pfJetsSmear"
    #slaveParams["recoJetCollection"] = "caloJets"
    #slaveParams["recoJetCollection"] = "caloJetsSmear"

    #jetUncFile = "START42_V11_AK5PF_Uncertainty.txt"
    jetUncFile = "START41_V0_AK5PF_Uncertainty.txt"


    slaveParams["jetUncFile"] =  edm.FileInPath("MNTriggerStudies/MNTriggerAna/test/MNxsectionAna/"+jetUncFile).fullPath()


    DiJetBalanceTreeProducer.runAll(treeName="mnXS",
                               slaveParameters=slaveParams,
                               sampleList=sampleList,
                               maxFiles = maxFiles,
                               nWorkers=nWorkers,
                               outFile = "~/treeDiJetBalance.root" )



