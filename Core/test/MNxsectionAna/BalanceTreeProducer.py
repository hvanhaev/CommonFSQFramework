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
from  MNTriggerStudies.MNTriggerAna.BetterJetGetter import BetterJetGetter


from HLTMCWeighter import HLTMCWeighter
#import cProfile

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
        #self.pr = cProfile.Profile()

        print "Params:", self.etaMax, self.ptMin

        if not self.isData:
            #self.hltMCWeighter = HLTMCWeighter("HLT_Jet15U")
            self.HLTMCWeighterJ15Raw = HLTMCWeighter("HLT_Jet15U_raw")
            self.HLTMCWeighterJ15L1Raw = HLTMCWeighter("HLT_Jet15U_L1Seeding_raw")
            #self.HLTMCWeighterDJ15FBRaw = HLTMCWeighter("HLT_DoubleJet15U_ForwardBackward_raw")
            #self.HLTMCWeighterDJ15L1FBRaw = HLTMCWeighter("HLT_DoubleJet15U_ForwardBackward_L1Seeding_raw")

        self.normFactor = self.getNormalizationFactor()
        self.dphi = ROOT.Math.VectorUtil.DeltaPhi

        self.tree = ROOT.TTree("data", "data")
        #self.GetOutputList().Add(self.tree)
        self.addToOutput(self.tree)

        self.var = {}
        self.histos = {}
        self.histos["evcnt"] =  ROOT.TH1F("evcnt_central_jet15", "evcnt_central_jet15",  1, -0.5, 0.5)

        self.todoShifts = ["_central"]

        if not self.isData and self.doPtShiftsJEC:
            #self.todoShifts.append("_ptUp")
            #self.todoShifts.append("_ptDown")
            self.todoShifts.append("_jecUp")
            self.todoShifts.append("_jecDown")

        if not self.isData and self.doPtShiftsJER:
            self.todoShifts.append("_jerUp")
            self.todoShifts.append("_jerDown")


        trg = "_jet15"
        for t in self.todoShifts:
            self.var["tagPt"+t] = array('d', [0])
            self.var["tagEta"+t] = array('d', [0])
            self.var["probePt"+t] = array('d', [0])
            self.var["probeEta"+t] = array('d', [0])
            self.var["ptAve"+t] = array('d', [0])
            self.var["balance"+t] = array('d', [0])
            #//self.var["veto1"+t] = array('d', [0])
            self.var["veto2"+t] = array('d', [0])

            histoPostFix = t+trg
            self.histos["ptProbe"+t] = ROOT.TH1F("ptProbe"+histoPostFix, "ptProbe"+histoPostFix, 100, 0, 100)
            self.histos["ptTag"+t] = ROOT.TH1F("ptTag"+histoPostFix, "ptTag"+histoPostFix, 100, 0, 100)
            self.histos["etaProbe"+t] = ROOT.TH1F("etaProbe"+histoPostFix, "etaProbe"+histoPostFix, 35, 1.3, 4.8)
            self.histos["etaTag"+t] = ROOT.TH1F("etaTag"+histoPostFix, "etaTag"+histoPostFix, 15, 0, 1.5)
            self.histos["nvtx"+t] = ROOT.TH1F("nvtx"+histoPostFix, "nvtx"+histoPostFix, 10, -0.5, 9.5)
 

        for t in self.histos:
            #self.histos[t][1] = ROOT.TH1F(name, name, nbins, self.histos[t][2], self.histos[t][3])
            self.histos[t].Sumw2()
            #self.GetOutputList().Add(self.histos[t])
            self.addToOutput(self.histos[t])

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
            #self.jetGetter = JetGetter("PFAK4CHS", jetColOverride="recoPFAK4ChsCorrectedMyRhop4")
            #self.jetGetter = JetGetter("PFAK4CHS", jetColOverride="recoPFAK4ChsCorrectedp4")
            self.jetGetter = JetGetter("PFAK4CHS", jetColOverride="hltAK4PFJetsCorrectedp4")
            #self.jetGetter = JetGetter("PFAK4CHS")
            #self.jetGetter = JetGetter("PFAK5CHS")
            #self.jetGetter = JetGetter("PF")
            self.jetGetter.disableGenJet()
            self.jetGetter.disableJetId()
            #self.jetGetter = GenJetProxy()
        else:
            self.jetGetter = JetGetter("PFAK5")
            #self.jetGetter = JetGetter("PFlegacy")
            self.jetGetter.disableGenJet()

        #self.jetGetter = BetterJetGetter("PFAK5") 
        #self.jetGetter = BetterJetGetter("Calo") 

        '''
        if self.isData:
            self.jetGetter = JetGetter("PFAK5") 
        else:
            self.jetGetter = JetGetter("PFlegacy") 
        '''

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
    
    def weight(self):
        if self.weightCache != None:
            return self.weightCache
        if not self.isData:
            weight = self.genWeight()
            if not self.HLT2015TempWorkaround:
                truePU = self.fChain.puTrueNumInteractions
                puWeight =  self.lumiWeighters["_jet15_central"].weight(truePU)
                weight *= puWeight
                w1 = self.HLTMCWeighterJ15L1Raw.getWeight()
                w2 = self.HLTMCWeighterJ15Raw.getWeight()
                triggerEff = w1*w2
                weight *= triggerEff
        else:
            weight = 1

        self.weightCache = weight
        return weight



    '''
    # stuff for code profiling
    def analyze(self):
        self.pr.enable()
        self.analyzeTT()
        self.pr.disable()
    def analyzeTT(self):
        '''
    def analyze(self):
        self.weightCache = None
        self.histos["evcnt"].Fill(0)
        # '''
        if not self.HLT2015TempWorkaround:
            if self.fChain.ngoodVTX == 0: return
            if self.fChain.HBHENoiseFilterResult == 0: return


        if self.isData:
            if self.fChain.jet15 < 0.5:
                return 1
            
        for v in self.var:
            self.var[v][0] = 0

        # reset is done after fill
        self.setExternals()

        self.jetGetter.newEvent(self.fChain)
        if not self.isData:
            self.HLTMCWeighterJ15L1Raw.newEvent(self.fChain)
            self.HLTMCWeighterJ15Raw.newEvent(self.fChain)


        # xxxwei

            

        fill = False
        for shift in self.todoShifts:
            tagJet = None
            probeJet = None
            probePT = None
            tagPT = None


            for jet in self.jetGetter.get(shift):
                pt = jet.pt()

                if pt < self.ptMin: continue
                eta = abs(jet.eta())
                if eta > self.etaMax: continue

                if not self.HLT2015TempWorkaround:
                    if not jet.jetid(): continue
                if eta < 1.4:
                    tagJet = jet
                    tagPT = pt
                else:
                    probeJet = jet
                    probePT = pt

            if tagJet != None and probeJet != None:
                dphi = abs(self.dphi(tagJet.p4(), probeJet.p4()))
                if dphi < 2.7: continue
                
                # check veto:
                ptAve = (probePT+tagPT)/2
                if ptAve < 25: continue


                veto2 = -1
                #for jet in self.jetGetter.get(shift):
                for jet in self.jetGetter.get(shift):
                    if jet == tagJet or probeJet == jet: continue
                    eta = abs(jet.eta())
                    if eta > self.etaMax: continue
                    vetoCand = jet.pt()/ptAve
                    if veto2 < vetoCand:
                        veto2 = vetoCand

                tagEta = abs(tagJet.eta())
                probeEta = abs(probeJet.eta())

                self.var["tagPt"+shift][0] = tagPT 
                self.var["tagEta"+shift][0] = tagEta
                self.var["probePt"+shift][0] = probePT
                self.var["probeEta"+shift][0] = probeEta
                self.var["ptAve"+shift][0] = ptAve
                self.var["balance"+shift][0] = (probePT-tagPT)/ptAve
                #self.var["veto1"+shift][0] = veto1
                self.var["veto2"+shift][0] = veto2
                fill = True


                #print "Hist fill", weight
                weight = self.weight()
                self.histos["ptProbe"+shift].Fill(probePT, weight)
                self.histos["ptTag"+shift].Fill(tagPT, weight)
                self.histos["etaProbe"+shift].Fill(probeEta, weight)
                self.histos["etaTag"+shift].Fill(tagEta, weight)
                #self.histos["nvtx"+shift].Fill(self.fChain.ngoodVTX, weight)

   
        # at least one variation ok.
        if fill:
            self.var["weight"][0] = self.weight()
            self.fill()

        self.resetExternals()

        return 1

    def finalize(self):
        print "Finalize:"
        if hasattr(self, "pr"):
            dname = "/nfs/dust/cms/user/fruboest/2014.11.MN2010/CMSSW_4_2_8_lowpupatch1/src/MNTriggerStudies/MNTriggerAna/test/MNxsectionAna/"
            profName = dname + "stats"
            self.pr.dump_stats(profName)

        # note: norm factor applied allready when filling
        #normFactor = self.getNormalizationFactor()
        #print "  applying norm", normFactor
        #for h in self.histos:
        #    self.histos[h].Scale(normFactor)

if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    ROOT.gSystem.Load("libFWCoreFWLite.so")
    ROOT.AutoLibraryLoader.enable()

    sampleList = None
    maxFilesMC = None
    maxFilesData = None
    nWorkers = 12
    treeName = "mnXS"

    sampleList = []
    #'''
    #sampleList.append("QCD_Pt-15to1000_TuneEE3C_Flat_7TeV_herwigpp")
    sampleList.append("QCD_Pt-15to3000_TuneZ2star_Flat_HFshowerLibrary_7TeV_pythia6")
    sampleList.append("JetMET-Run2010A-Apr21ReReco-v1")
    sampleList.append("JetMETTau-Run2010A-Apr21ReReco-v1")
    sampleList.append("Jet-Run2010B-Apr21ReReco-v1")
    #'''
    # '''

    # debug config:
    #'''
    #sampleList=["QCD_Pt-15to1000_TuneEE3C_Flat_7TeV_herwigpp"]
    #sampleList.append("QCD_Pt-15to3000_TuneZ2star_Flat_HFshowerLibrary_7TeV_pythia6")
    #sampleList.append("QCD_Pt-15to1000_TuneEE3C_Flat_7TeV_herwigpp")
    #sampleList.append("JetMETTau-Run2010A-Apr21ReReco-v1")
    #sampleList.append("Jet-Run2010B-Apr21ReReco-v1")
    #sampleList = ["JetMET-Run2010A-Apr21ReReco-v1"]
    #sampleList = ["JetMETTau-Run2010A-Apr21ReReco-v1", "Jet-Run2010B-Apr21ReReco-v1", "JetMET-Run2010A-Apr21ReReco-v1", "METFwd-Run2010B-Apr21ReReco-v1"]
    #maxFilesData = 2
    maxFilesMC = 60
    #nWorkers = 1
    #'''

    slaveParams = {}
    #slaveParams["doPtShiftsJEC"] = False
    slaveParams["doPtShiftsJEC"] = True

    #slaveParams["doPtShiftsJER"] = False
    slaveParams["doPtShiftsJER"] = True

    slaveParams["ptMin"] = 15
    slaveParams["etaMax"] = 4.7
    slaveParams["HLT2015TempWorkaround"] = False


    print sampleList

    BalanceTreeProducer.runAll(treeName=treeName,
                               slaveParameters=slaveParams,
                               sampleList=sampleList,
                               maxFilesMC = maxFilesMC,
                               maxFilesData = maxFilesData,
                               nWorkers=nWorkers, 
                               usePickle = True,
                               useProofOFile = True,
                               outFile = "treeDiJetBalance.root" )

