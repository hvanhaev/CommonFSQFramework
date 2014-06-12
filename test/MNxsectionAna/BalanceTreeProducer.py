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


from MNTriggerStudies.MNTriggerAna.ExampleProofReader import ExampleProofReader
from MNTriggerStudies.MNTriggerAna.JetGetter import JetGetter

class BalanceTreeProducer(ExampleProofReader):
    def init( self):

        self.tree = ROOT.TTree("data", "data")
        self.GetOutputList().Add(self.tree)

        self.var = {}
        self.todoShifts = ["_central"]

        if not self.isData and self.doPtShiftsJEC:
            self.todoShifts.append("_ptUp")
            self.todoShifts.append("_ptDown")

        if not self.isData and self.doPtShiftsJER:
            self.todoShifts.append("_jerUp")
            self.todoShifts.append("_jerDown")

        for t in self.todoShifts:
            self.var["tagPt"+t] = array('d', [0])
            self.var["tagEta"+t] = array('d', [0])
            self.var["probePt"+t] = array('d', [0])
            self.var["probeEta"+t] = array('d', [0])
            self.var["ptAve"+t] = array('d', [0])
            self.var["balance"+t] = array('d', [0])

        self.var["weight"] = array('d', [0])
        
        for v in self.var:
            self.tree.Branch(v, self.var[v], v+"/D")
        
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


        self.jetGetter = JetGetter("PF")
        if hasattr(self, "jetUncFile"):
            self.jetGetter.setJecUncertainty(self.jetUncFile)

        sys.stdout.flush()

    def analyze(self):
        #print "----"
        if self.fChain.ngoodVTX == 0: return
        if self.isData:
            if self.fChain.jet15 < 0.5:
                return 1
            
        for v in self.var:
            self.var[v][0] = 0
    


        self.jetGetter.newEvent(self.fChain)
        # recoJets = getattr(self.fChain, self.recoJetCollection)



        fill = False
        for shift in self.todoShifts:
            weight = 1. 
            if not self.isData:
                weight *= self.fChain.genWeight # keep inside shift iter
                truePU = self.fChain.puTrueNumInteractions
                puWeight =  self.lumiWeighters["_jet15_central"].weight(truePU)
                weight *= puWeight

            self.var["weight"][0] = weight


            tagJet = None
            probeJet = None
            probePT = None
            tagPT = None


            #dbgCnt = 0
            for jet in self.jetGetter.get(shift):
            #for i in xrange(0, recoJets.size()):
            #    jet = recoJets.at(i)
                #dbgJet = recoJets.at(dbgCnt)
                #dbgCnt+=1
                #print shift, dbgCnt,"|", jet.pt(), jet.eta(), "|", dbgJet.pt(), dbgJet.eta()

                pt = jet.pt()
                if pt < 35: continue
                eta = abs(jet.eta())
                if eta > 4.7: continue
                if eta < 1.4:
                    tagJet = jet
                    tagPT = pt
                else:
                    probeJet = jet
                    probePT = pt

            if tagJet != None and probeJet != None:
                # check veto:
                badEvent = False
                ptAve = (probePT+tagPT)/2
                for jet in self.jetGetter.get(shift):
                #for i in xrange(0, recoJets.size()):
                    if jet == tagJet or probeJet == jet: continue
                    eta = abs(jet.eta())
                    if eta > 4.7: continue
                    veto =  jet.pt()/ptAve
                    if veto > 0.2:
                        badEvent = True
                        break
                if not badEvent:
                    self.var["tagPt"+shift][0] = tagPT 
                    self.var["tagEta"+shift][0] =  abs(tagJet.eta())
                    self.var["probePt"+shift][0] = probePT
                    self.var["probeEta"+shift][0] = abs(probeJet.eta())
                    self.var["ptAve"+shift][0] = ptAve
                    self.var["balance"+shift][0] = (probePT-tagPT)/ptAve
                    fill = True

   
        # at least one variation ok.
        if fill:
            #print "Filll!"
            self.tree.Fill()

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
    sampleList=[]
    sampleList.append("QCD_Pt-15to3000_TuneZ2star_Flat_HFshowerLibrary_7TeV_pythia6")
    #sampleList.append("JetMETTau-Run2010A-Apr21ReReco-v1")
    #sampleList.append("Jet-Run2010B-Apr21ReReco-v1")
    #sampleList = ["JetMET-Run2010A-Apr21ReReco-v1"]
    #sampleList = ["JetMETTau-Run2010A-Apr21ReReco-v1", "Jet-Run2010B-Apr21ReReco-v1", "JetMET-Run2010A-Apr21ReReco-v1", "METFwd-Run2010B-Apr21ReReco-v1"]
    maxFilesData = 1
    maxFilesMC = 1
    nWorkers = 1
    #'''

    slaveParams = {}
    slaveParams["threshold"] = 35.
    #slaveParams["doPtShiftsJEC"] = False
    slaveParams["doPtShiftsJEC"] = True

    #slaveParams["doPtShiftsJER"] = False
    slaveParams["doPtShiftsJER"] = True


    #slaveParams["recoJetCollection"] = "pfJets"
    slaveParams["recoJetCollection"] = "pfJetsSmear"
    slaveParams["recoJetCollectionBaseReco"] = "pfJets"
    slaveParams["recoJetCollectionGEN"] = "pfJets2Gen"
    #slaveParams["recoJetCollection"] = "caloJets"
    #slaveParams["recoJetCollection"] = "caloJetsSmear"

    #jetUncFile = "START42_V11_AK5PF_Uncertainty.txt"
    jetUncFile = "START41_V0_AK5PF_Uncertainty.txt"


    slaveParams["jetUncFile"] =  edm.FileInPath("MNTriggerStudies/MNTriggerAna/test/MNxsectionAna/"+jetUncFile).fullPath()


    BalanceTreeProducer.runAll(treeName="mnXS",
                               slaveParameters=slaveParams,
                               sampleList=sampleList,
                               maxFilesMC = maxFilesMC,
                               nWorkers=nWorkers,
                               outFile = "treeDiJetBalance.root" )


