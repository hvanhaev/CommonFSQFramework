#!/usr/bin/env python
import sys, os, time
sys.path.append(os.path.dirname(__file__))

import ROOT
ROOT.gROOT.SetBatch(True)
ROOT.gSystem.Load("libFWCoreFWLite.so")

ROOT.gSystem.Load("libRooUnfold.so")

ROOT.AutoLibraryLoader.enable()
from ROOT import edm, JetCorrectionUncertainty

from array import *
import cProfile

# please note that python selector class name (here: MNxsAnalyzerClean) 
# should be consistent with this file name (MNxsAnalyzerClean.py)

# you have to run this file from directory where it is saved

import MNTriggerStudies.MNTriggerAna.ExampleProofReader
from  MNTriggerStudies.MNTriggerAna.BetterJetGetter import BetterJetGetter

from optparse import OptionParser

from HLTMCWeighter import HLTMCWeighter
#import DiJetBalancePlugin

import math
class MNxsAnalyzerClean(MNTriggerStudies.MNTriggerAna.ExampleProofReader.ExampleProofReader):
    def init( self):
        if not self.isData:
            #self.hltMCWeighter = HLTMCWeighter("HLT_Jet15U")
            self.HLTMCWeighterJ15Raw = HLTMCWeighter("HLT_Jet15U_raw")
            self.HLTMCWeighterJ15L1Raw = HLTMCWeighter("HLT_Jet15U_L1Seeding_raw")
            self.HLTMCWeighterJ15FBL1Raw = HLTMCWeighter("HLT_DoubleJet15U_ForwardBackward_L1Seeding_raw")
            self.HLTMCWeighterJ15FBRaw = HLTMCWeighter("HLT_DoubleJet15U_ForwardBackward_raw")

        self.normFactor = self.getNormalizationFactor()

        #sys.stdout = sys.stderr
        #self.pr = cProfile.Profile()
        print "XXX init - MNxsAnalyzerClean", self.datasetName, self.isData

        self.todoShifts = ["_central"]
        if not self.isData and self.doPtShiftsJEC:
            self.todoShifts.append("_jecUp")
            self.todoShifts.append("_jecDown")

        if not self.isData and self.doPtShiftsJER:
            self.todoShifts.append("_jerUp")
            self.todoShifts.append("_jerDown")

        self.hist = {}
        todoTrg = ["_jet15", "_dj15fb"]

        binsEta = [x/10. for x in xrange(0, 61, 5)]
        binsEta.extend([7.0, 8.0, 9.4])
        print "xs vs eta: gonna use binning: ", binsEta
        binsNew = array('d',binsEta)

        for shift in self.todoShifts:
            for trg in todoTrg:
                t = shift+trg
                self.hist["ptLead"+t] =  ROOT.TH1F("ptLead"+t,   "ptLead"+t,  100, 0, 100)
                self.hist["ptSublead"+t] =  ROOT.TH1F("ptSublead"+t,   "ptSublead"+t,  100, 0, 100)
                self.hist["etaLead"+t] =  ROOT.TH1F("etaLead"+t,   "etaLead"+t,  100, -5, 5)
                self.hist["etaSublead"+t] =  ROOT.TH1F("etaSublead"+t,   "etaSublead"+t,  100, -5, 5)
                self.hist["xsVsDeltaEta"+t] =  ROOT.TH1F("xs"+t,   "xs"+t, len(binsEta)-1, binsNew)

                self.hist["xsVsDeltaEtaGen"+t] =  ROOT.TH1F("xsGen"+t,   "xsGen"+t, len(binsEta)-1, binsNew)
                self.hist["xsVsDeltaEtaFake"+t] =  ROOT.TH1F("xsFake"+t,   "xsFake"+t, len(binsEta)-1, binsNew)
                self.hist["xsVsDeltaEtaMiss"+t] =  ROOT.TH1F("xsMiss"+t,   "xsMiss"+t, len(binsEta)-1, binsNew)

                self.hist["vtx"+t] =  ROOT.TH1F("vtx"+t,   "vtx"+t,  10, -0.5, 9.5)

                if self.unfoldEnabled:
                    dummy = ROOT.TH2F("dummy"+t, "dummy"+t, len(binsEta)-1, binsNew, len(binsEta)-1, binsNew)
                    self.hist["response"+t]= ROOT.RooUnfoldResponse(self.hist["xsVsDeltaEta"+t], 
                                                                    self.hist["xsVsDeltaEta"+t], 
                                                                    dummy,
                                                                    "response"+t,"response"+t)



        if self.onlyPtHatReweighing:
            self.var = {}
            self.var["leadPt"] = array('d', [0])
            self.var["leadEta"] = array('d', [0])
            self.var["weight"] = array('d', [0]) # only jet15 trigger??
            #self.var["alphaQCD"] = array('d', [0])
            self.var["qScale"]   = array('d', [0])
            self.tree = ROOT.TTree("data", "data")
            for v in self.var:
                self.tree.Branch(v, self.var[v], v+"/D")
            self.addToOutput(self.tree)

        else:
            for h in self.hist:
                if not h.startswith("response"):
                    self.hist[h].Sumw2()
                #self.GetOutputList().Add(self.hist[h])
                self.addToOutput(self.hist[h])

        if self.applyPtHatReweighing and not self.isData:
                fp = "MNTriggerStudies/MNTriggerAna/test/MNxsectionAna/"
                todo = ["ptHatWeighters.root"]
                self.ptHatW = []
                for t in todo:
                    ptHatFileName = edm.FileInPath("MNTriggerStudies/MNTriggerAna/test/MNxsectionAna/"+t).fullPath()
                    ptHatFile = ROOT.TFile(ptHatFileName)
                    self.ptHatW.append(ptHatFile.Get(self.datasetName+"/ptHatW"))




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

        self.jetGetter = BetterJetGetter("PFAK5") 

    # note: for the ptHat reweighing we will do only the central variation.
    #       otherwise the changes from the JEC/JER variations would be fixed
    #       by the ptHat reweighing procedure

    #
    # leadPt:qScale gives a nice linear response
    #
    # todo: trigger correction for data
    def doPtHatReweighing(self, weightBase):
        if self.isData:
            if self.fChain.jet15 < 0.5:
                return
            weight = weightBase
        else:
            if not self.triggerFired("_jet15"):
                return
            truePU = self.fChain.puTrueNumInteractions
            puWeight =  self.lumiWeighters["_jet15_central"].weight(truePU)
            weight = weightBase*puWeight

        sortKey = lambda j: j.pt()*(j.pt()>self.threshold)\
                          *(j.jetid()>0.5)*(abs(j.eta())<4.7)

        # if empty sequence...
        try:
            bestJet = max(self.jetGetter.get("_central"), key=sortKey)
        except ValueError:
            return

        if not sortKey(bestJet): return # do we really have a jet passing the criteria?
        pt, eta =  bestJet.pt(), bestJet.eta()
        self.var["leadPt"][0] = pt
        self.var["leadEta"][0] = eta
        self.var["weight"][0] = weight
        if not self.isData:
            #self.var["alphaQCD"][0] = self.fChain.alphaQCD
            self.var["qScale"][0] = self.fChain.qScale
        self.tree.Fill()

        
    def triggerFired(self, case):
        if case == "_jet15" and self.MC_jet15_triggerFired_cached != None:
            return self.MC_jet15_triggerFired_cached
        if case == "_dj15fb" and self.MC_dj15fb_triggerFired_cached != None:
            return self.MC_dj15fb_triggerFired_cached

        ev = self.fChain.event
        rnd4eff = ev%10000/9999.

        if case == "_jet15":
            self.HLTMCWeighterJ15L1Raw.newEvent(self.fChain)
            self.HLTMCWeighterJ15Raw.newEvent(self.fChain)
            w1 = self.HLTMCWeighterJ15L1Raw.getWeight()
            w2 = self.HLTMCWeighterJ15Raw.getWeight()
            self.MC_jet15_triggerFired_cached = w1*w2 > rnd4eff
            return self.MC_jet15_triggerFired_cached
        elif case == "_dj15fb":
            self.HLTMCWeighterJ15FBL1Raw.newEvent(self.fChain)
            self.HLTMCWeighterJ15FBRaw.newEvent(self.fChain)
            w1 = self.HLTMCWeighterJ15FBL1Raw.getWeight()
            w2 = self.HLTMCWeighterJ15FBRaw.getWeight()
            self.MC_dj15fb_triggerFired_cached = w1*w2 > rnd4eff
            return self.MC_dj15fb_triggerFired_cached
        else:
            raise Excecption("triggerFired: case not known: "+str(case))

    def topology(self, j1, j2):
        eta1=j1.eta()
        eta2=j2.eta()
        if min(abs(eta1), abs(eta2)) > 3. and eta1*eta2<0: return "_dj15fb"
        return "_jet15"

    def dr(self, a,b):
        de = a.eta()-b.eta()
        dp = a.phi()-b.phi()
        pi = 3.1415
        if dp > pi: dp -= 2*pi
        if dp < -pi: dp += 2*pi
        return math.sqrt(de*de+dp*dp)

    def analyze(self):
        self.MC_jet15_triggerFired_cached = None
        self.MC_dj15fb_triggerFired_cached = None

        if self.fChain.ngoodVTX == 0: return
        self.jetGetter.newEvent(self.fChain)
        weightBase = 1. 
        puWeightJ15 = 1
        puWeightDJ15FB = 1
        if not self.isData:
            weightBase *= self.fChain.genWeight*self.normFactor 
            truePU = self.fChain.puTrueNumInteractions
            puWeightJ15 =  self.lumiWeighters["_jet15_central"].weight(truePU)
            puWeightDJ15FB = self.lumiWeighters["_dj15fb_central"].weight(truePU)


        if not self.isData and  self.applyPtHatReweighing:
            ptHat = self.fChain.qScale
            w = 1.
            for weighter in self.ptHatW:
                w*=max(weighter.Eval(ptHat), 0.)
                #print "W:", ptHat, weighter.Eval(ptHat)
            weightBase *= w
 
        if self.onlyPtHatReweighing:
            self.doPtHatReweighing(weightBase)
            return

        if not self.isData:
            goodGenJets = [j for j in self.fChain.genJets if j.pt()>self.threshold and abs(j.eta()) < 4.7 ]

        for shift in self.todoShifts:
            matchedPairs = set()

            # todo: j.jetID() > 0.5
            goodRecoJets = [j for j in self.jetGetter.get(shift) if  j.pt()>self.threshold and abs(j.eta()) < 4.7 and  j.jetid() ]
            for i1 in xrange(len(goodRecoJets)):
                for i2 in xrange(i1+1, len(goodRecoJets)):
                    j1 = goodRecoJets[i1]
                    j2 = goodRecoJets[i2]
                    topology = self.topology(j1, j2)
                    histoName = shift + topology
                    if self.isData:
                        if topology == "_jet15":
                            hasTrigger = self.fChain.jet15 > 0.5
                            weight = puWeightJ15*weightBase    
                        else:
                            hasTrigger = self.fChain.doubleJ15FB > 0.5
                            weight = puWeightDJ15FB*weightBase    
                    else:
                        hasTrigger = self.triggerFired(topology)
                        weight = 1

                    if not hasTrigger: continue

                    detaDet = abs(j1.eta()-j2.eta())
                    # todo: fill detLevel Histograms
                    # for MC - check if there is a matching pair, save result inside matchedPairs set
                    if not self.isData and len(goodGenJets) > 1:
                        closestGenJetI1 = min(xrange(len(goodGenJets)), key = lambda i: self.dr(j1, goodGenJets[i]) )
                        closestGenJetI2 = min(xrange(len(goodGenJets)), key = lambda i: self.dr(j2, goodGenJets[i]) )
                        dr1 = self.dr(j1, goodGenJets[closestGenJetI1])
                        dr2 = self.dr(j2, goodGenJets[closestGenJetI2])
                        matched=() # empty tuple
                        if max(dr1, dr2) < 0.3:
                            if closestGenJetI1 != closestGenJetI2:
                                # check the topology is correct
                                genTopology = self.topology(goodGenJets[closestGenJetI1], goodGenJets[closestGenJetI2])
                                if genTopology == topology:
                                    matchCand=(min(closestGenJetI1,closestGenJetI2), max(closestGenJetI1,closestGenJetI2))    
                                    if not matchCand in matchedPairs:
                                        matched=matchCand
                                        matchedPairs.add(matchCand)
                            else:
                                pass
                                #print "XXX Warning, matched to same genJet"
                                #print  j1.pt(), j1.eta(), j1.phi()
                                #print  j2.pt(), j2.eta(), j2.phi()
                                #def pr(x): print x
                                #map(lambda x: pr("Gen: {0} {1} {2}".format(x.pt(), x.eta() , x.phi())),  goodGenJets  )
                        

                        # add this point we know, if this is
                        #   a fake: no matched genJetPair
                        #   a fill: matched genJetPai
                        #fill the response matrix
                        if len(matched)>0:
                            if self.unfoldEnabled:
                                detaGen = abs(goodGenJets[matched[0]].eta()-goodGenJets[matched[1]].eta())
                                self.hist["response"+histoName].Fill(detaDet, detaGen, weight)
                        else:
                            if self.unfoldEnabled:
                                self.hist["response"+histoName].Fake(detaDet, weight)

            # Now: fill miss cateogory
            if self.unfoldEnabled and not self.isData:
                for i1 in xrange(len(goodGenJets)):
                    for i2 in xrange(i1+1, len(goodGenJets)):
                        if (i1, i2) in matchedPairs: continue
                        genTopology = self.topology(goodGenJets[i1], goodGenJets[i2])
                        if genTopology == "_jet15":
                            weight = puWeightJ15*weightBase    
                        else:
                            weight = puWeightDJ15FB*weightBase    
                        histoName = shift + genTopology
                        detaGen = abs(goodGenJets[i1].eta()-goodGenJets[i2].eta())
                        self.hist["response"+histoName].Miss(detaGen, weight)



    def finalize(self):
        print "Finalize:"

if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    parser = OptionParser(usage="usage: %prog [options] filename",
                            version="%prog 1.0")

    parser.add_option("-p", "--ptHatReweighing",   action="store_true", dest="ptHatReweighing", \
                                help="produce tree for ptHat reweighing")

    (options, args) = parser.parse_args()

    sampleList = None
    maxFilesMC = None
    maxFilesData = None
    nWorkers = 12

    # debug config:
    #'''
    sampleList = []
    sampleList= ["QCD_Pt-15to3000_TuneZ2star_Flat_HFshowerLibrary_7TeV_pythia6"]
    #sampleList.append("QCD_Pt-15to1000_TuneEE3C_Flat_7TeV_herwigpp")
    #'''
    #sampleList.append("JetMETTau-Run2010A-Apr21ReReco-v1")
    #sampleList.append("Jet-Run2010B-Apr21ReReco-v1")
    #sampleList.append("JetMET-Run2010A-Apr21ReReco-v1")
    #sampleList.append("METFwd-Run2010B-Apr21ReReco-v1")
    # '''
    # '''
    #maxFilesMC = 48
    maxFilesMC = 1
    #maxFilesData = 1
    nWorkers = 10
    #maxFilesMC = 16
    #nWorkers = 12
    #nWorkers = 10

    slaveParams = {}
    slaveParams["threshold"] = 35.
    #slaveParams["doPtShiftsJEC"] = False
    slaveParams["doPtShiftsJEC"] = True

    #slaveParams["doPtShiftsJER"] = False
    slaveParams["doPtShiftsJER"] = True

    #slaveParams["jetID"] = "pfJets_jetID" # TODO

    slaveParams["unfoldEnabled"] = True

    if options.ptHatReweighing:
        slaveParams["onlyPtHatReweighing"] = True
        slaveParams["applyPtHatReweighing"] = False
        slaveParams["threshold"] = 30.
        ofile = "treesForPTHatReweighing.root"
        sampleList.remove("METFwd-Run2010B-Apr21ReReco-v1")
    else:
        slaveParams["onlyPtHatReweighing"] = False
        #slaveParams["applyPtHatReweighing"] = True
        slaveParams["applyPtHatReweighing"] = False
        ofile = "plotsMNxs.root"


    MNxsAnalyzerClean.runAll(treeName="mnXS",
                               slaveParameters=slaveParams,
                               sampleList=sampleList,
                               maxFilesMC = maxFilesMC,
                               maxFilesData = maxFilesData,
                               nWorkers=nWorkers,
                               usePickle = True,
                               useProofOFile = True,
                               outFile = ofile )

    print "TODO: fakes prob vs eta"
    print "TODO: larger statistics for herwig"
    print "TODO: better binning for det level plots"


