#!/usr/bin/env python

import sys, os, time
sys.path.append(os.path.dirname(__file__))

import ROOT
ROOT.gROOT.SetBatch(True)
from ROOT import *

from array import *


# please note that python selector class name (here: BalanceTreeProducer) 
# should be consistent with this file name (BalanceTreeProducer.py)

# you have to run this file from directory where it is saved


from MNTriggerStudies.MNTriggerAna.ExampleProofReader import ExampleProofReader


class BalanceTreeProducer(ExampleProofReader):
    def configureAnalyzer( self):

        self.tree = ROOT.TTree("data", "data")
        self.GetOutputList().Add(self.tree)

        self.var = {}
        self.todoShifts = ["_central"]
        if hasattr(self, "jetUncFile") and not self.isData and self.doPtShifts:
            self.todoShifts.append("_ptUp")
            self.todoShifts.append("_ptDown")
            self.jetUnc = JetCorrectionUncertainty(self.jetUncFile)

        for t in self.todoShifts:
            self.var["tagPt"+t] = array('f', [0])
            self.var["tagEta"+t] = array('f', [0])
            self.var["probePt"+t] = array('f', [0])
            self.var["probeEta"+t] = array('f', [0])
            self.var["ptAve"+t] = array('f', [0])

        self.var["weight"] = array('f', [0])
        
        for v in self.var:
            self.tree.Branch(v, self.var[v], v+"/F")
        
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


    def analyze(self):
        if self.fChain.ngoodVTX == 0: return
        if self.isData:
            if self.fChain.jet15 < 0.5:
                return 1
            
        for v in self.var:
            self.var[v][0] = 0
    

        #print "XXDS", self.datasetName, self.isData

        recoJets = getattr(self.fChain, self.recoJetCollection)


        fill = False
        for shift in self.todoShifts:
            weight = 1. 
            if not self.isData:
                weight *= self.fChain.genWeight # keep inside shift iter
                truePU = self.fChain.puTrueNumInteractions
                puWeight =  self.lumiWeighters["_jet15_central"].weight(truePU)
                weight *= puWeight

            self.var["weight"][0] = weight


            tagI = None
            probeI = None

            for i in xrange(0, recoJets.size()):
                jet = recoJets.at(i)
                pt = self.ptShifted(jet, shift)
                if pt < 35: continue
                eta = abs(jet.eta())
                if eta > 4.7: continue
                if eta < 1.4:
                    tagI = i
                else:
                    probeI = i

            if tagI != None and probeI != None:
                # check veto:
                badEvent = False
                ptAve = (recoJets.at(probeI).pt() + recoJets.at(tagI).pt())/2
                for i in xrange(0, recoJets.size()):
                    if i == tagI or probeI == i: continue
                    eta = abs(jet.eta())
                    if eta > 4.7: continue
                    veto =  recoJets.at(i).pt()/ptAve
                    if veto > 0.2:
                        badEvent = True
                        break
                if not badEvent:
                    self.var["tagPt"+shift][0] =  recoJets.at(tagI).pt()
                    self.var["tagEta"+shift][0] =  abs(recoJets.at(tagI).eta())
                    self.var["probePt"+shift][0] = recoJets.at(probeI).pt()
                    self.var["probeEta"+shift][0] = abs(recoJets.at(probeI).eta())
                    self.var["ptAve"+shift][0] = ptAve
                    fill = True

   
        # at least one variation ok.
        if fill:
            #print "Filll!"
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
    #sampleList= ["QCD_Pt-15to3000_TuneZ2star_Flat_HFshowerLibrary_7TeV_pythia6"]
    #sampleList=  ["JetMETTau-Run2010A-Apr21ReReco-v1"]
    #sampleList=  ["Jet-Run2010B-Apr21ReReco-v1"] 
    #sampleList = ["JetMET-Run2010A-Apr21ReReco-v1"]
    #sampleList = ["JetMETTau-Run2010A-Apr21ReReco-v1", "Jet-Run2010B-Apr21ReReco-v1", "JetMET-Run2010A-Apr21ReReco-v1", "METFwd-Run2010B-Apr21ReReco-v1"]
    #maxFiles = 2
    #maxFiles = 1
    #nWorkers = 1


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


    BalanceTreeProducer.runAll(treeName="mnXS",
                               slaveParameters=slaveParams,
                               sampleList=sampleList,
                               maxFiles = maxFiles,
                               nWorkers=nWorkers,
                               outFile = "treeDiJetBalance.root" )



