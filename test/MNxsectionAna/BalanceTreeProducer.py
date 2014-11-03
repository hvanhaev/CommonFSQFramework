#!/usr/bin/env python

import sys, os, time
sys.path.append(os.path.dirname(__file__))

import ROOT
ROOT.gROOT.SetBatch(True)
ROOT.gSystem.Load("libFWCoreFWLite.so")
ROOT.AutoLibraryLoader.enable()
from ROOT import edm, JetCorrectionUncertainty

from array import *

# please note that python selector class name (here: BalanceTreeProducer) 
# should be consistent with this file name (BalanceTreeProducer.py)

# you have to run this file from directory where it is saved
import MNTriggerStudies.MNTriggerAna.ExampleProofReader 
from MNTriggerStudies.MNTriggerAna.JetGetter import JetGetter

class Proxy():
    def __init__(self, obj):
        self.obj = obj

    def p4(self):
        return self.obj

    def __getattr__(self, name):
        return getattr(self.obj, name)

class GenJetProxy():
    def newEvent(self, chain):
        self.chain = chain

    def get(self, shift):
        jets = self.chain.ak4GenJets
        size = jets.size()
        index = 0
        while index < size:
            yield Proxy(jets.at(index))
            index += 1



class BalanceTreeProducer(MNTriggerStudies.MNTriggerAna.ExampleProofReader.ExampleProofReader):
    def init(self):

        print "Params:", self.etaMax, self.ptMin
        self.normFactor = self.getNormalizationFactor()
        self.dphi = ROOT.Math.VectorUtil.DeltaPhi

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
            #//self.var["veto1"+t] = array('d', [0])
            self.var["veto2"+t] = array('d', [0])

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



        if self.HLT2015TempWorkaround:
            self.jetGetter = JetGetter("PFAK4CHS")
            #self.jetGetter = JetGetter("PFAK5CHS")
            #self.jetGetter = JetGetter("PF")
            self.jetGetter.disableGenJet()
            #self.jetGetter = GenJetProxy()
        else:
            self.jetGetter = JetGetter("PFAK5")
            self.jetGetter.disableGenJet()

        self.varE = {}
        sys.stdout.flush()

    def addExternalVar(self, names):
        for name in names:
            self.varE[name] =  0.
            self.var[name] = array('d', [0])
            self.tree.Branch(name, self.var[name], name+"/D")

    def setExternals(self):
        for v in self.varE:
            self.var[v][0] = self.varE[v]
    def fill(self):
            self.tree.Fill()
    def resetExternals(self):
        for v in self.varE: 
            self.varE[v] = 0

    def fillGenWeight(self):
        weight = self.genWeight()
        self.var["weight"][0] = weight


    def setExternalVar(self, name, val):
        self.varE[name] = val

    def genWeight(self):
        #print "ASDFASD", self.fChain.genWeight
        return self.fChain.genWeight*self.normFactor

    def analyze(self):
        if not self.HLT2015TempWorkaround and self.fChain.ngoodVTX == 0: return

        if self.isData:
            if self.fChain.jet15 < 0.5:
                return 1
            
        for v in self.var:
            self.var[v][0] = 0

        # reset is done after fill
        self.setExternals()

        self.jetGetter.newEvent(self.fChain)

        weight = self.genWeight()
        if not self.isData and not self.HLT2015TempWorkaround:
            truePU = self.fChain.puTrueNumInteractions
            puWeight =  self.lumiWeighters["_jet15_central"].weight(truePU)
            weight *= puWeight

        self.var["weight"][0] = weight

        fill = False
        for shift in self.todoShifts:
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
                #print pt, jet.eta()

                pt = jet.pt()
                #print "XXX", shift, dbgCnt, pt, jet.eta()
                #dbgCnt += 1

                if pt < self.ptMin: continue
                eta = abs(jet.eta())
                if eta > self.etaMax: continue

                if not self.HLT2015TempWorkaround:
                    if not jet.looseId(): continue
                if eta < 1.4:
                    tagJet = jet
                    tagPT = pt
                else:
                    probeJet = jet
                    probePT = pt

            if tagJet != None and probeJet != None:
                dphi = self.dphi(tagJet.p4(), probeJet.p4())
                if dphi < 2.7: continue
                
                # check veto:
                ptAve = (probePT+tagPT)/2

                veto2 = -1
                for jet in self.jetGetter.get(shift):
                    if jet == tagJet or probeJet == jet: continue
                    eta = abs(jet.eta())
                    if eta > self.etaMax: continue
                    veto2 =  jet.pt()/ptAve

                self.var["tagPt"+shift][0] = tagPT 
                self.var["tagEta"+shift][0] =  abs(tagJet.eta())
                self.var["probePt"+shift][0] = probePT
                self.var["probeEta"+shift][0] = abs(probeJet.eta())
                self.var["ptAve"+shift][0] = ptAve
                self.var["balance"+shift][0] = (probePT-tagPT)/ptAve
                #self.var["veto1"+shift][0] = veto1
                self.var["veto2"+shift][0] = veto2
                fill = True

   
        # at least one variation ok.
        if fill:
            self.fill()

        self.resetExternals()

        return 1

    def finalize(self):
        print "Finalize:"
        #normFactor = self.getNormalizationFactor()
        #print "  applying norm", normFactor
        #for h in self.hist:
        #    self.hist[h].Scale(normFactor)

if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    ROOT.gSystem.Load("libFWCoreFWLite.so")
    ROOT.AutoLibraryLoader.enable()

    sampleList = None
    maxFilesMC = None
    maxFilesData = None
    nWorkers = None # Use all
    treeName = "mnXS"

    # debug config:
    '''
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
    #slaveParams["doPtShiftsJEC"] = False
    slaveParams["doPtShiftsJEC"] = True

    #slaveParams["doPtShiftsJER"] = False
    slaveParams["doPtShiftsJER"] = True

    slaveParams["ptMin"] = 35
    slaveParams["etaMax"] = 4.7



    BalanceTreeProducer.runAll(treeName=treeName,
                               slaveParameters=slaveParams,
                               sampleList=sampleList,
                               maxFilesMC = maxFilesMC,
                               maxFilesData = maxFilesData,
                               nWorkers=nWorkers,
                               outFile = "treeDiJetBalance.root" )

