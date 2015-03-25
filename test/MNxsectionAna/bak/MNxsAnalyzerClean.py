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

class EtaBinning:
    def bins(self):
        binsEta = [x/10. for x in xrange(0, 61, 5)]
        binsEta.extend([7.0, 8.0, 9.4])
        print "xs vs eta: gonna use binning: ", binsEta
        binsNew = array('d',binsEta)
        return binsNew

class PtBinning:
    def bins(self):
        bins = [x*10. for x in xrange(0, 10)]
        print "xs vs eta: gonna use binning: ", bins
        binsNew = array('d',bins)
        return binsNew

class BaseDijetAna:
    def xsVariable(self, j1, j2):
        return abs(j1.eta()-j2.eta())
    def filterPair(self, j1, j2):
        return True
    def filterCol(self, l):
        return l

class BasicVariant(BaseDijetAna, EtaBinning):
    def __init__(self): pass

class MostFBVariant(BaseDijetAna, EtaBinning):
    def filterCol(self, l):
        if len(l) < 2: return []
        return [min(l, key=lambda j: j.eta()), max(l, key=lambda j: j.eta())]

class AtLeastOneAbove(BaseDijetAna, EtaBinning):
    def filterPair(self, j1, j2):
        return max(j1.pt(), j2.pt()) > 45

    def filterCol(self, l):
        if len(l) < 2: return []
        if max(l, key=lambda j: j.pt()).pt() < 45: return []
        return l

class BothBelow(BaseDijetAna, EtaBinning):
    def filterCol(self, l):
        return [j for j in l if j.pt()  < 55]

# TODO (?) - filter mid eta jets
class FWD11_01(BaseDijetAna, PtBinning):
    def xsVariable(self, j1, j2):
        ret = j1.pt() if abs(j1.eta()) < abs(j2.eta()) else j2.pt()
        return ret
    def filterPair(self, j1, j2):
        eta1 = abs(j1.eta())
        eta2 = abs(j2.eta())
        if max(eta1, eta2) < 3: return False # no FWD jet
        if min(eta1, eta2) > 1.3: return False # no central Jet
        return True

import math
class MNxsAnalyzerClean(MNTriggerStudies.MNTriggerAna.ExampleProofReader.ExampleProofReader):
    def init( self):

        if self.variant == "basic":
            self.variantFilter = BasicVariant()
        elif self.variant == "mostFB":
            self.variantFilter = MostFBVariant()
        elif self.variant == "atLeastOneAbove":
            self.variantFilter = AtLeastOneAbove()

        elif self.variant == "bothBelow":
            self.variantFilter = BothBelow()

        else:
            raise Exception("Variant not known: "+self.variant)

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

        # since shifts for PU are in fact changes in weight
        # there is no sense to repeat whole analaysis
        # we will use the central value
        self.shiftsPU = ["_central"]
        if not self.isData and self.doShiftsPU:
            self.shiftsPU.append("_puUp")
            self.shiftsPU.append("_puDown")

        self.hist = {}
        todoTrg = ["_jet15", "_dj15fb"]

        binsNew = self.variantFilter.bins()

        # note: set gives as unique items, since _central is repeated
        for shift in set(self.todoShifts+self.shiftsPU):
            for trg in todoTrg:
                t = shift+trg
                self.hist["ptLead"+t] =  ROOT.TH1F("ptLead"+t,   "ptLead"+t,  100, 0, 100)
                self.hist["ptSublead"+t] =  ROOT.TH1F("ptSublead"+t,   "ptSublead"+t,  100, 0, 100)
                self.hist["etaLead"+t] =  ROOT.TH1F("etaLead"+t,   "etaLead"+t,  100, -5, 5)
                self.hist["etaSublead"+t] =  ROOT.TH1F("etaSublead"+t,   "etaSublead"+t,  100, -5, 5)
                self.hist["xsVsDeltaEta"+t] =  ROOT.TH1F("xs"+t,   "xs"+t, len(binsNew)-1, binsNew)
                self.hist["vtx"+t] =  ROOT.TH1F("vtx"+t,   "vtx"+t,  10, -0.5, 9.5)

                if self.unfoldEnabled:
                    dummy = ROOT.TH2F("dummy"+t, "dummy"+t, len(binsNew)-1, binsNew, len(binsNew)-1, binsNew)
                    self.hist["response"+t]= ROOT.RooUnfoldResponse(self.hist["xsVsDeltaEta"+t], 
                                                                    self.hist["xsVsDeltaEta"+t], 
                                                                    dummy,
                                                                    "response"+t,"response"+t)

        # in principle trigger does not applies to gen plots. We keep consistent naming though, so the unfolded result to gen level plots is possible
        # in each category
        self.hist["detaGen_jet15"] =  ROOT.TH1F("detaGen_central_jet15", "detaGen_central_jet15",
                                                len(binsNew)-1, binsNew)
        self.hist["detaGen_dj15fb"] =  ROOT.TH1F("detaGen_central_dj15fb", "detaGen_central_dj15fb",  
                                                len(binsNew)-1, binsNew)


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
        self.getterForTriggerModelling = BetterJetGetter("CaloRaw")

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
            if self.MC_dj15fb_triggerFired_cached == None and self.MC_jet15_triggerFired_cached == None:
                self.getterForTriggerModelling.newEvent(self.fChain)
                self.jetsForTRG = list(self.getterForTriggerModelling.get("_central"))

            # calls needed to reset cached values
            self.HLTMCWeighterJ15L1Raw.setJets(self.jetsForTRG)
            self.HLTMCWeighterJ15Raw.setJets(self.jetsForTRG)
            #self.HLTMCWeighterJ15L1Raw.setGetter(self.getterForTriggerModelling)
            #self.HLTMCWeighterJ15Raw.setGetter(self.getterForTriggerModelling)
            #self.HLTMCWeighterJ15L1Raw.newEvent(self.fChain)
            #self.HLTMCWeighterJ15Raw.newEvent(self.fChain)
            w1 = self.HLTMCWeighterJ15L1Raw.getWeight()
            w2 = self.HLTMCWeighterJ15Raw.getWeight()
            self.MC_jet15_triggerFired_cached = w1*w2 > rnd4eff
            return self.MC_jet15_triggerFired_cached
        elif case == "_dj15fb":
            if self.MC_dj15fb_triggerFired_cached == None and self.MC_jet15_triggerFired_cached == None:
                self.getterForTriggerModelling.newEvent(self.fChain)
                self.jetsForTRG = list(self.getterForTriggerModelling.get("_central"))
            # calls needed to reset cached values
            self.HLTMCWeighterJ15FBL1Raw.setJets(self.jetsForTRG)
            self.HLTMCWeighterJ15FBRaw.setJets(self.jetsForTRG)
            #self.HLTMCWeighterJ15FBL1Raw.setGetter(self.getterForTriggerModelling)
            #self.HLTMCWeighterJ15FBRaw.setGetter(self.getterForTriggerModelling)
            #self.HLTMCWeighterJ15FBL1Raw.newEvent(self.fChain)
            #self.HLTMCWeighterJ15FBRaw.newEvent(self.fChain)
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

    '''
    def analyze(self):
        self.pr.enable()
        self.analyzeTT()
        self.pr.disable()
    #'''
    #def analyzeTT(self):
    def analyze(self):
        self.MC_jet15_triggerFired_cached = None
        self.MC_dj15fb_triggerFired_cached = None

        if self.fChain.ngoodVTX == 0: return
        self.jetGetter.newEvent(self.fChain)
        weightBase = 1. 
        weightBaseNoMCNorm = 1. 
        puWeights = {}
        puWeights["_jet15"] = {}
        puWeights["_dj15fb"] = {}


        if not self.isData:
            weightBase *= self.fChain.genWeight*self.normFactor 
            weightBaseNoMCNorm *= self.fChain.genWeight
            truePU = self.fChain.puTrueNumInteractions
            for lw in self.lumiWeighters:
                spl = lw.split("_")
                trgName = "_"+spl[1]
                variationName = "_"+spl[2]
                puWeights[trgName][variationName] = self.lumiWeighters[lw].weight(truePU)

        if not self.isData and  self.applyPtHatReweighing:
            ptHat = self.fChain.qScale
            w = 1.
            for weighter in self.ptHatW:
                w*=max(weighter.Eval(ptHat), 0.)
                #print "W:", ptHat, weighter.Eval(ptHat)
            weightBase *= w
            weightBaseNoMCNorm*= w 

        if self.onlyPtHatReweighing:
            self.doPtHatReweighing(weightBase)
            return


        if not self.isData:
            goodGenJets = self.variantFilter.filterCol([j for j in self.fChain.genJets \
                                                        if j.pt()>self.threshold and abs(j.eta()) < 4.7 ])

        for shift in self.todoShifts:
            matchedPairs = set()
            # todo: j.jetID() > 0.5
            goodRecoJets = self.variantFilter.filterCol([j for j in self.jetGetter.get(shift) \
                                                        if j.pt()>self.threshold and abs(j.eta()) < 4.7 and  j.jetid()])

            for i1 in xrange(len(goodRecoJets)):
                for i2 in xrange(i1+1, len(goodRecoJets)):
                    j1 = goodRecoJets[i1]
                    j2 = goodRecoJets[i2]
                    if not self.variantFilter.filterPair(j1, j2): continue
                    topology = self.topology(j1, j2)
                    weight = {}
                    if self.isData:
                        if topology == "_jet15":
                            hasTrigger = self.fChain.jet15 > 0.5
                            weight["_central"] = 1
                        else:
                            hasTrigger = self.fChain.doubleJ15FB > 0.5
                            weight["_central"] = 1
                    else:
                        hasTrigger = self.triggerFired(topology)
                        weightNoNorm = {}
                        if shift == "_central":
                            for s in self.shiftsPU: # note: shifts pu contains central, puUp and puDown
                                weightPU = puWeights[topology][s]
                                weight[s] = weightPU*weightBase    
                                weightNoNorm[s] = weightPU*weightBaseNoMCNorm    
                        else:
                            weightPU = puWeights[topology]["_central"]
                            weight[shift] = weightPU*weightBase    
                            weightNoNorm[shift] = weightPU*weightBaseNoMCNorm    

                    if not hasTrigger: continue

                    detaDeta = self.variantFilter.xsVariable(j1, j2) # note: we should rename this...
                    ptSorted = sorted( [j1, j2], key = lambda j: -j.pt())

                    for w in weight:
                        histoName = w + topology
                        self.hist["ptLead"+histoName].Fill(ptSorted[0].pt(), weight[w])
                        self.hist["etaLead"+histoName].Fill(ptSorted[0].eta(), weight[w])
                        self.hist["ptSublead"+histoName].Fill(ptSorted[1].pt(), weight[w])
                        self.hist["etaSublead"+histoName].Fill(ptSorted[1].eta(), weight[w])
                        self.hist["xsVsDeltaEta"+histoName].Fill(detaDet, weight[w])
                        self.hist["vtx"+histoName].Fill(self.fChain.ngoodVTX, weight[w])

                    # todo: fill detLevel Histograms
                    # for MC - check if there is a matching pair, save result inside matchedPairs set
                    if not self.isData: # and len(goodGenJets) > 1:
                        matched=() # empty tuple
                        if len(goodGenJets) > 1:
                            closestGenJetI1 = min(xrange(len(goodGenJets)), key = lambda i: self.dr(j1, goodGenJets[i]) )
                            closestGenJetI2 = min(xrange(len(goodGenJets)), key = lambda i: self.dr(j2, goodGenJets[i]) )
                            if self.variantFilter.filterPair(goodGenJets[closestGenJetI1], goodGenJets[closestGenJetI2]):
                                dr1 = self.dr(j1, goodGenJets[closestGenJetI1])
                                dr2 = self.dr(j2, goodGenJets[closestGenJetI2])
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
                        #   a fake: no matched genJetPair (or genJet pair from different category)
                        #   a fill: matched genJetPai
                        #fill the response matrix
                        if len(matched)>0:
                            if self.unfoldEnabled:
                                detaGen = self.variantFilter.xsVariable(goodGenJets[matched[0]],goodGenJets[matched[1]])
                                for w in weightNoNorm:
                                    histoName = w + topology
                                    self.hist["response"+histoName].Fill(detaDet, detaGen, weightNoNorm[w])
                        else:
                            if self.unfoldEnabled:
                                for w in weightNoNorm:
                                    histoName = w + topology
                                    self.hist["response"+histoName].Fake(detaDet, weightNoNorm[w])

            # Now: fill miss cateogory
            # note: this is still happening in "shift" loop
            if self.unfoldEnabled and not self.isData:
                for i1 in xrange(len(goodGenJets)):
                    for i2 in xrange(i1+1, len(goodGenJets)):
                        if not self.variantFilter.filterPair(goodGenJets[i1], goodGenJets[i2]): continue
                        genTopology = None
                        detaGen = None
                        if shift == "_central":
                            genTopology = self.topology(goodGenJets[i1], goodGenJets[i2])
                            detaGen = self.variantFilter.xsVariable(goodGenJets[i1], goodGenJets[i2])
                            self.hist["detaGen"+genTopology].Fill(detaGen, weightBase)

                        if (i1, i2) in matchedPairs: continue
                        if genTopology == None:
                            genTopology = self.topology(goodGenJets[i1], goodGenJets[i2])
   
                        # note: code repeated here, see above defintion of weightNoNorm
                        weightNoNorm = {}
                        if shift == "_central":
                            for s in self.shiftsPU: # note: shifts pu contains central, puUp and puDown
                                weightPU = puWeights[genTopology][s]
                                weightNoNorm[s] = weightPU*weightBaseNoMCNorm    
                        else:
                            weightPU = puWeights[genTopology]["_central"]
                            weightNoNorm[shift] = weightPU*weightBaseNoMCNorm    

                        if detaGen == None:
                            detaGen = self.variantFilter.xsVariable(goodGenJets[i1], goodGenJets[i2])

                        for w in weightNoNorm:
                            histoName = w + genTopology
                            self.hist["response"+histoName].Miss(detaGen, weightNoNorm[w])

    def finalize(self):
        print "Finalize:"
        if hasattr(self, "pr"):
            dname = "/nfs/dust/cms/user/fruboest/2015.01.MN/slc6/CMSSW_7_0_5/src/MNTriggerStudies/MNTriggerAna/test/MNxsectionAna/bak/"
            profName = dname + "stats"
            self.pr.dump_stats(profName)

if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    parser = OptionParser(usage="usage: %prog [options] filename",
                            version="%prog 1.0")

    parser.add_option("-p", "--ptHatReweighing",   action="store_true", dest="ptHatReweighing", \
                                help="produce tree for ptHat reweighing")
    parser.add_option("-v", "--variant",   action="store", dest="variant", type="string", \
                                help="choose analysis variant")

    (options, args) = parser.parse_args()

    sampleList = None
    maxFilesMC = None
    maxFilesData = None
    nWorkers = 12

    # debug config:
    #'''
    sampleList = []
    #sampleList= ["QCD_Pt-15to3000_TuneZ2star_Flat_HFshowerLibrary_7TeV_pythia6"]
    sampleList.append("QCD_Pt-15to1000_TuneEE3C_Flat_7TeV_herwigpp")
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
    slaveParams["doShiftsPU"] = True

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

    knownVariants = ["basic", "mostFB", "atLeastOneAbove", "bothBelow"]
    if options.variant:
        if options.variant not in knownVariants:
            print "Variant not known. Choose from: " + " ".join(knownVariants)
            sys.exit()
        slaveParams["variant"] = options.variant
    else:
        slaveParams["variant"] = "mostFB"  # highest delta eta separation

    #slaveParams["variant"] = "basic"  
    #slaveParams["variant"] = "atLeastOneAbove"
    #slaveParams["variant"] = "bothBelow"

    ofile = "test_plotsMNxs_{}.root".format(slaveParams["variant"])

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


