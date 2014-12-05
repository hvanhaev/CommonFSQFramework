#!/usr/bin/env python


import sys, os, time
sys.path.append(os.path.dirname(__file__))

import ROOT
ROOT.gROOT.SetBatch(True)
ROOT.gSystem.Load("libFWCoreFWLite.so")
ROOT.AutoLibraryLoader.enable()
from ROOT import edm, JetCorrectionUncertainty

from array import *
import cProfile

# please note that python selector class name (here: MNxsAnalyzer) 
# should be consistent with this file name (MNxsAnalyzer.py)

# you have to run this file from directory where it is saved


import MNTriggerStudies.MNTriggerAna.ExampleProofReader
from  MNTriggerStudies.MNTriggerAna.BetterJetGetter import BetterJetGetter

#import DiJetBalancePlugin

class MNxsAnalyzer(MNTriggerStudies.MNTriggerAna.ExampleProofReader.ExampleProofReader):
    def init( self):

        #sys.stdout = sys.stderr
        #self.pr = cProfile.Profile()
        print "XXX init - MNxsAnalyzer", self.datasetName, self.isData

        self.todoShifts = ["_central"]
        if not self.isData and self.doPtShiftsJEC:
            self.todoShifts.append("_jecUp")
            self.todoShifts.append("_jecDown")

        if not self.isData and self.doPtShiftsJER:
            self.todoShifts.append("_jerUp")
            self.todoShifts.append("_jerDown")

        self.hist = {}
        todoTrg = ["_jet15", "_dj15fb"]

        for shift in self.todoShifts:
            for trg in todoTrg:
                t = shift+trg
                self.hist["ptLead"+t] =  ROOT.TH1F("ptLead"+t,   "ptLead"+t,  100, 0, 100)
                self.hist["ptSublead"+t] =  ROOT.TH1F("ptSublead"+t,   "ptSublead"+t,  100, 0, 100)
                self.hist["etaLead"+t] =  ROOT.TH1F("etaLead"+t,   "etaLead"+t,  100, -5, 5)
                self.hist["etaSublead"+t] =  ROOT.TH1F("etaSublead"+t,   "etaSublead"+t,  100, -5, 5)
                self.hist["xsVsDeltaEta"+t] =  ROOT.TH1F("xs"+t,   "xs"+t,  100, 0, 9.4)
                self.hist["vtx"+t] =  ROOT.TH1F("vtx"+t,   "vtx"+t,  10, -0.5, 9.5)

        for h in self.hist:
            self.hist[h].Sumw2()
            self.GetOutputList().Add(self.hist[h])


        puFiles = {}
        # MNTriggerStudies/MNTriggerAna/test/MNxsectionAna/
        jet15FileV2 = edm.FileInPath("MNTriggerStudies/MNTriggerAna/test/MNxsectionAna/data/PUJet15V2.root").fullPath()   # MC gen distribution

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

        #self.jetGetter = JetGetter("PF")
        #if hasattr(self, "jetUncFile"):
        #    self.jetGetter.setJecUncertainty(self.jetUncFile)

        self.jetGetter = BetterJetGetter("PFAK5") 


    def analyze(self):
        if self.fChain.ngoodVTX == 0: return
        self.jetGetter.newEvent(self.fChain)
        for shift in self.todoShifts:
            weightBase = 1. 
            if not self.isData:
                weightBase *= self.fChain.genWeight # keep inside shift iter

            # find best dijet pair
            mostFwdJet = None
            mostBkgJet = None
            mostFwdJetEta = None
            mostBkgJetEta = None
            mostFwdJetPt = None
            mostBkgJetPt = None
            for jet in self.jetGetter.get(shift):
                #if jetID.at(i) < 0.5: continue
                if not jet.jetid(): continue
                eta =  jet.eta()
                if abs(eta) > 4.7: continue

                ptShifted = jet.pt()
                if ptShifted < self.threshold: continue

                if  mostFwdJet == None or mostFwdJetEta < eta:
                    mostFwdJet = jet
                    mostFwdJetEta = eta
                    mostFwdJetPt = ptShifted
                if  mostBkgJet == None or mostBkgJetEta > eta:
                    mostBkgJet = jet
                    mostBkgJetEta = eta
                    mostBkgJetPt = ptShifted

            pairFound = False
            if mostFwdJet != None and mostBkgJet != mostFwdJet:
                pairFound = True

            # A dijet pair was found. Check trigger for data, calculate weight for MC
            # fill histograms
            if pairFound:
                deta = abs(mostFwdJetEta - mostBkgJetEta)
                triggerToUse = "_jet15"
                if abs(mostFwdJetEta) > 3 and abs(mostBkgJetEta) > 3 and mostFwdJetEta*mostBkgJetEta<0:
                    triggerToUse = "_dj15fb"

                gotTrigger = True
                if self.isData: # check trigger
                    if triggerToUse == "_jet15":
                        gotTrigger = self.fChain.jet15 > 0.5
                    elif triggerToUse == "_dj15fb":
                        gotTrigger = self.fChain.doubleJ15FB > 0.5
                    else:
                        raise Exception("Trigger not known??? "+triggerToUse)

                if gotTrigger:
                    weight = weightBase
                    if not self.isData:
                        truePU = self.fChain.puTrueNumInteractions
                        puWeight =  self.lumiWeighters[triggerToUse+"_central"].weight(truePU)
                        weight *= puWeight

                    histoName = shift +triggerToUse
                    self.hist["xsVsDeltaEta"+histoName].Fill(deta, weight)

                    # fill also some control plots
                    leadJet = mostBkgJet
                    subleadJet = mostFwdJet
                    ptLead =  mostBkgJetPt 
                    ptSublead = mostFwdJetPt
                    etaLead = mostBkgJetEta
                    etaSublead = mostFwdJetEta

                    if ptSublead > ptLead:
                        leadJet, subleadJet = subleadJet, leadJet
                        ptLead, ptSublead = ptSublead, ptLead
                        etaLead, etaSublead = etaSublead, etaLead

                    self.hist["vtx"+histoName].Fill(self.fChain.ngoodVTX, weight)
                    self.hist["ptLead"+histoName].Fill(ptLead, weight)
                    self.hist["ptSublead"+histoName].Fill(ptSublead, weight)
                    self.hist["etaLead"+histoName].Fill(etaLead, weight)
                    self.hist["etaSublead"+histoName].Fill(etaSublead, weight)

    def finalize(self):
        print "Finalize:"
        normFactor = self.getNormalizationFactor()
        print "  applying norm", normFactor
        for h in self.hist:
            self.hist[h].Scale(normFactor)

if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)

    sampleList = None
    maxFilesMC = None
    maxFilesData = None
    nWorkers = 15 

    # debug config:
    '''
    sampleList= ["QCD_Pt-15to3000_TuneZ2star_Flat_HFshowerLibrary_7TeV_pythia6"]
    #sampleList=  ["JetMETTau-Run2010A-Apr21ReReco-v1"]
    #sampleList=  ["Jet-Run2010B-Apr21ReReco-v1"] 
    #sampleList = ["JetMET-Run2010A-Apr21ReReco-v1"]
    #sampleList = ["JetMETTau-Run2010A-Apr21ReReco-v1", "Jet-Run2010B-Apr21ReReco-v1", "JetMET-Run2010A-Apr21ReReco-v1", "METFwd-Run2010B-Apr21ReReco-v1"]
    # '''
    #maxFilesMC = 2
    #maxFilesData = 2
    #nWorkers = 2
    #maxFilesMC = 16
    #nWorkers = 12

    slaveParams = {}
    slaveParams["threshold"] = 35.
    #slaveParams["doPtShiftsJEC"] = False
    slaveParams["doPtShiftsJEC"] = True

    #slaveParams["doPtShiftsJER"] = False
    slaveParams["doPtShiftsJER"] = True

    #slaveParams["jetID"] = "pfJets_jetID" # TODO


    MNxsAnalyzer.runAll(treeName="mnXS",
                               slaveParameters=slaveParams,
                               sampleList=sampleList,
                               maxFilesMC = maxFilesMC,
                               maxFilesData = maxFilesData,
                               nWorkers=nWorkers,
                               usePickle = True,
                               outFile = "plotsMNxs.root" )



