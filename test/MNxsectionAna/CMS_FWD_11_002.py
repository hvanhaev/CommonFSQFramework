#!/usr/bin/env python
# http://cdsweb.cern.ch/record/1347749
# http://cdsweb.cern.ch/record/1347515
# http://cdsweb.cern.ch/record/1421692?ln=en
# http://arxiv.org/abs/arXiv:1202.0704
# http://rivet.hepforge.org/code/2.1.0/a00543_source.html
from MNTriggerStudies.MNTriggerAna.ExampleProofReader import ExampleProofReader

import sys, os, time
sys.path.append(os.path.dirname(__file__))

import ROOT
ROOT.gROOT.SetBatch(True)
from ROOT import edm, JetCorrectionUncertainty

from array import *

# please note that python selector class name (here: CMS_FWD_11_002) 
# should be consistent with this file name (CMS_FWD_11_002.py)
# you have to run this file from directory where it is saved

from MNTriggerStudies.MNTriggerAna.JetGetter import JetGetter

class CMS_FWD_11_002(ExampleProofReader):
    def init( self):
        print "XXX init - CMS_FWD_11_002", self.datasetName, self.isData

        self.todoShifts = ["_central"]
        if not self.isData and self.doPtShiftsJEC:
            self.todoShifts.append("_ptUp")
            self.todoShifts.append("_ptDown")

        if not self.isData and self.doPtShiftsJER:
            self.todoShifts.append("_jerUp")
            self.todoShifts.append("_jerDown")

        self.hist = {}
        todoTrg = ["_jet15"]

        pedroPtBins = array('d', [35, 45, 57, 72, 90, 120, 150, 200])
        for shift in self.todoShifts:
            for trg in todoTrg:
                t = shift+trg
                self.hist["etaFwd"+t] =  ROOT.TH1F("etaFwd"+t,   "etaFwd"+t,  100, -5, 5)
                self.hist["etaCen"+t] =  ROOT.TH1F("etaCen"+t,   "etaCen"+t,  100, -5, 5)
                self.hist["vtx"+t] =  ROOT.TH1F("vtx"+t,   "vtx"+t,  10, -0.5, 9.5)
                self.hist["ptFwd"+t] = ROOT.TH1F("ptFwd"+t, "ptFwd"+t, len(pedroPtBins)-1, pedroPtBins)
                self.hist["ptCen"+t] =  ROOT.TH1F("ptCen"+t,   "ptCen"+t,   len(pedroPtBins)-1, pedroPtBins)
                

        # follow the histogram naming convention even if it makes no sense for gen - needed for drawPlots.py
        self.hist["genFwd"] = ROOT.TH1F("genJetFwd_central_jet15", "genJetFwd_central_jet15", len(pedroPtBins)-1, pedroPtBins)
        self.hist["genCen"] = ROOT.TH1F("genJetCen_central_jet15", "genJetCen_central_jet15", len(pedroPtBins)-1, pedroPtBins)

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

        self.jetGetter = JetGetter("PF")
        if hasattr(self, "jetUncFile"):
            self.jetGetter.setJecUncertainty(self.jetUncFile)

    def analyze(self):
        # generator level plots
        if not self.isData:
            fwdPt = None
            cenPt = None
            genJets = self.fChain.genJets
            for i in xrange(genJets.size()):
                j = genJets.at(i)
                pt = j.pt()
                if pt < 35. : continue
                eta = abs(j.eta())
                if eta > 4.7: continue
                if fwdPt == None and eta > 3.2 and eta < 4.7:
                    fwdPt = pt
                if cenPt == None and eta < 2.8:
                    cenPt = pt
            if cenPt != None and fwdPt != None:
                weight = self.fChain.genWeight
                binN =  self.hist["genFwd"].FindBin(pt)
                binWidthFactor = self.hist["genFwd"].GetBinWidth(binN)
                self.hist["genFwd"].Fill(fwdPt, weight/(3.*binWidthFactor))

                binN =  self.hist["genCen"].FindBin(pt)
                binWidthFactor = self.hist["genCen"].GetBinWidth(binN)
                self.hist["genCen"].Fill(cenPt, weight/(5.6*binWidthFactor))



        if self.fChain.ngoodVTX == 0: return
        #jetID = getattr(self.fChain, self.jetID)

        self.jetGetter.newEvent(self.fChain)
        for shift in self.todoShifts:
            triggerToUse = "_jet15"
            histoName = shift +triggerToUse

            if self.isData:
                if self.fChain.jet15 < 0.5:
                    continue

            # find best fwd-central pair
            fwdPt = None
            cenPt = None
            fwdEta = None
            cenEta = None
            for jet in self.jetGetter.get(shift):
                eta = abs(jet.eta())
                if eta > 4.7: continue
                pt = jet.pt()
                if pt < 35. : continue
                #if jetID.at(i) < 0.5: continue
                #print "XA", pt, eta
                if fwdPt == None and eta > 3.2 and eta < 4.7:
                    fwdPt = pt
                    fwdEta = jet.eta()
                if cenPt == None and eta < 2.8:
                    cenPt = pt
                    cenEta = jet.eta()

            if cenPt != None and fwdPt != None:
                if not self.isData:
                    weightBase = self.fChain.genWeight # keep inside shift iter
                    truePU = self.fChain.puTrueNumInteractions
                    puWeight =  self.lumiWeighters[triggerToUse+"_central"].weight(truePU)
                    weight = puWeight*weightBase
                else:
                    weight = 1.

                etaFactor = 3.
                binN =  self.hist["ptFwd"+histoName].FindBin(fwdPt)
                binWidthFactor = self.hist["ptFwd"+histoName].GetBinWidth(binN)
                factor = etaFactor*binWidthFactor
                self.hist["ptFwd"+histoName].Fill(fwdPt, weight/factor)
                self.hist["etaFwd"+histoName].Fill(fwdEta , weight/factor)

                etaFactor = 5.6
                binN =  self.hist["ptCen"+histoName].FindBin(cenPt)
                binWidthFactor = self.hist["ptCen"+histoName].GetBinWidth(binN)
                factor = etaFactor*binWidthFactor
                self.hist["ptCen"+histoName].Fill(cenPt, weight/factor)
                self.hist["etaCen"+histoName].Fill(cenEta, weight/factor)

                self.hist["vtx"+histoName].Fill(self.fChain.ngoodVTX, weight)
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
    '''
    sampleList = []
    sampleList.append("QCD_Pt-15to3000_TuneZ2star_Flat_HFshowerLibrary_7TeV_pythia6")
    #sampleList.append("JetMETTau-Run2010A-Apr21ReReco-v1")
    #sampleList=  ["Jet-Run2010B-Apr21ReReco-v1"] 
    #sampleList = ["JetMET-Run2010A-Apr21ReReco-v1"]
    #sampleList = ["JetMETTau-Run2010A-Apr21ReReco-v1", "Jet-Run2010B-Apr21ReReco-v1", "JetMET-Run2010A-Apr21ReReco-v1", "METFwd-Run2010B-Apr21ReReco-v1"]
    maxFilesMC = 1
    maxFilesData = 1
    #nWorkers = 16
    #maxFilesData = 1
    nWorkers = 1
    # '''


    slaveParams = {}
    slaveParams["threshold"] = 35.
    #slaveParams["doPtShiftsJEC"] = False
    slaveParams["doPtShiftsJEC"] = True

    #slaveParams["doPtShiftsJER"] = False
    slaveParams["doPtShiftsJER"] = True

    slaveParams["recoJetCollection"] = "pfJets"
    #slaveParams["recoJetCollection"] = "pfJetsSmear" 
    slaveParams["recoJetCollectionBaseReco"] = "pfJets"
    slaveParams["recoJetCollectionGEN"] = "pfJets2Gen"


    slaveParams["jetID"] = "pfJets_jetID"



    #slaveParams["recoJetCollection"] = "caloJets"
    #slaveParams["recoJetCollection"] = "caloJetsSmear"

    #jetUncFile = "START42_V11_AK5PF_Uncertainty.txt"
    jetUncFile = "START41_V0_AK5PF_Uncertainty.txt"


    slaveParams["jetUncFile"] =  edm.FileInPath("MNTriggerStudies/MNTriggerAna/test/MNxsectionAna/"+jetUncFile).fullPath()


    CMS_FWD_11_002.runAll(treeName="mnXS",
                               slaveParameters=slaveParams,
                               sampleList=sampleList,
                               maxFilesMC = maxFilesMC,
                               maxFilesData = maxFilesData,
                               nWorkers=nWorkers,
                               outFile = "plotsCMS_FWD_11_002.root" )



