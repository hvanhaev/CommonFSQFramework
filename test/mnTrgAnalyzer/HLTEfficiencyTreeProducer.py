#!/usr/bin/env python

import sys, os, time
sys.path.append(os.path.dirname(__file__))

import ROOT
ROOT.gROOT.SetBatch(True)
ROOT.gSystem.Load("libFWCoreFWLite.so")
ROOT.AutoLibraryLoader.enable()
from ROOT import edm, JetCorrectionUncertainty

# please note that python selector class name (here: HLTEfficiencyTreeProducer) 
# should be consistent with this file name (HLTEfficiencyTreeProducer.py)

# you have to run this file from directory where it is saved

import MNTriggerStudies.MNTriggerAna.ExampleProofReader
from MNTriggerStudies.MNTriggerAna.JetGetter import JetGetter
from array import *

class HLTEfficiencyTreeProducer(MNTriggerStudies.MNTriggerAna.ExampleProofReader.ExampleProofReader):
    def init(self):
        self.jetGetter = JetGetter("PFAK4CHS")
        self.dr = ROOT.Math.VectorUtil.DeltaR
        self.normFactor = self.getNormalizationFactor()

        self.var = {}
        self.var["recoEta"] = array('d', [0])
        self.var["recoPt"] = array('d', [0])
        #self.var["hltEta"] = array('d', [0])
        self.var["hltPt"] = array('d', [0])
        #self.var["l1Eta"] = array('d', [0])
        self.var["l1Pt"] = array('d', [0])
        #self.var["s1l1Eta"] = array('d', [0])
        self.var["s1l1Pt"] = array('d', [0])
        self.var["PUNumInteractions"] = array('d', [0])
        self.var["puTrueNumInteractions"] = array('d', [0])
        self.var["weight"] = array('d', [0])


        # for the PU file run
        # utils/GetFlatPUDist.py
        puFile = edm.FileInPath("MNTriggerStudies/MNTriggerAna/test/mnTrgAnalyzer/PUhists.root").fullPath()

        self.newlumiWeighters = {}
        #'''
        self.newlumiWeighters["flat010toflat010"] = edm.LumiReWeighting(puFile, puFile, "Flat0to10/pileup", "Flat0to10/pileup")
        self.newlumiWeighters["flat010toPU1"] = edm.LumiReWeighting(puFile, puFile, "Flat0to10/pileup", "PU1/pileup")
        #self.newlumiWeighters["flat010toPU2"] = edm.LumiReWeighting(puFile, puFile, "Flat0to10/pileup", "PU2/pileup")
        #self.newlumiWeighters["flat010toPU3"] = edm.LumiReWeighting(puFile, puFile, "Flat0to10/pileup", "PU3/pileup")
        #self.newlumiWeighters["flat010toPU4"] = edm.LumiReWeighting(puFile, puFile, "Flat0to10/pileup", "PU4/pileup")
        self.newlumiWeighters["flat010toPU5"] = edm.LumiReWeighting(puFile, puFile, "Flat0to10/pileup", "PU5/pileup")
        self.newlumiWeighters["flat010toPU10"] = edm.LumiReWeighting(puFile, puFile, "Flat0to10/pileup", "PU10/pileup")
        #'''
        '''
        self.newlumiWeighters["flat2050toPU20"] = edm.LumiReWeighting(puFile, puFile, "Flat20to50/pileup", "PU20/pileup")
        self.newlumiWeighters["flat2050toPU25"] = edm.LumiReWeighting(puFile, puFile, "Flat20to50/pileup", "PU25/pileup")
        self.newlumiWeighters["flat2050toPU30"] = edm.LumiReWeighting(puFile, puFile, "Flat20to50/pileup", "PU30/pileup")
        #'''

        '''
        self.newlumiWeighters["PU20to15"] = edm.LumiReWeighting(puFile, puFile, "PU20/pileup", "PU15/pileup")
        self.newlumiWeighters["PU20to18"] = edm.LumiReWeighting(puFile, puFile, "PU20/pileup", "PU18/pileup")
        self.newlumiWeighters["PU20to19"] = edm.LumiReWeighting(puFile, puFile, "PU20/pileup", "PU19/pileup")
        self.newlumiWeighters["PU20to21"] = edm.LumiReWeighting(puFile, puFile, "PU20/pileup", "PU21/pileup")
        self.newlumiWeighters["PU20to22"] = edm.LumiReWeighting(puFile, puFile, "PU20/pileup", "PU22/pileup")
        self.newlumiWeighters["PU20to20"] = edm.LumiReWeighting(puFile, puFile, "PU20/pileup", "PU20/pileup")
        self.newlumiWeighters["PU20to25"] = edm.LumiReWeighting(puFile, puFile, "PU20/pileup", "PU25/pileup")
        #'''
        for l in self.newlumiWeighters.keys():
            self.var[l] =  array('d', [0])

        self.tree = ROOT.TTree("data", "data")
        self.GetOutputList().Add(self.tree)

        for v in self.var:
            self.tree.Branch(v, self.var[v], v+"/D")


    def match(self, jetReco, jets):
        bestMatch = None
        for jet in jets:
            dr = self.dr(jetReco.p4(), jet)
            if dr < 0.3:
                if bestMatch == None or bestMatch.pt() < jet.pt():
                    bestMatch = jet

        return bestMatch

    def genWeight(self):
        return self.fChain.genWeight*self.normFactor

    def analyze(self):
        self.jetGetter.newEvent(self.fChain)
        self.var["PUNumInteractions"][0] = self.fChain.PUNumInteractions
        self.var["puTrueNumInteractions"][0] = self.fChain.puTrueNumInteractions

        pu = self.fChain.PUNumInteractions
        genW = self.genWeight()
        self.var["weight"][0]=genW
        for l in self.newlumiWeighters:
            w = self.newlumiWeighters[l].weight(pu)
            #print pu, l, w, genW
            self.var[l][0] = w*genW


        todo = {}
        todo["l1"] = self.fChain.l1Jets
        todo["s1l1"] = self.fChain.stage1L1Jets
        todo["hlt"] = self.fChain.hltAK4PFJetsCorrected
        for jet in self.jetGetter.get("_central"):
            if jet.pt() < 30: continue
            self.var["recoPt"][0] = jet.pt()
            self.var["recoEta"][0] = jet.eta()
            for t in todo.keys(): # reset subset of variables (rest is filled each time in loop)
                self.var[t+"Pt"][0] = 0

            for t in todo:
                ptMatch = 0
                match = self.match(jet, todo[t])
                if match != None:
                    self.var[t+"Pt"][0] = match.pt()
            self.tree.Fill()


        # self.fChain.hltAK4PFJetsCorrected




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


    '''
    sampleList=["QCD_Pt-300to470_Tune4C_13TeV_pythia8"]
    nWorkers = 1
    maxFilesMC = 12
    #'''
    maxFilesMC = 24
    #nWorkers=1
    #treeName = "mnTriggerAna"
    #slaveParams["ptMin"] = 20
    #slaveParams["etaMax"] = 5

    out = "treeJetTrgEff.root"
    HLTEfficiencyTreeProducer().runAll(treeName="MNTriggerAnaNew",
                           slaveParameters=slaveParams,
                           sampleList=sampleList,
                           maxFilesMC = maxFilesMC,
                           maxFilesData = maxFilesData,
                           nWorkers=nWorkers,
                           outFile = out )


