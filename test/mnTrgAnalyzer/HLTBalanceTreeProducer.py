#!/usr/bin/env python

import sys, os, time
sys.path.append(os.path.dirname(__file__))

import ROOT
ROOT.gROOT.SetBatch(True)
ROOT.gSystem.Load("libFWCoreFWLite.so")
ROOT.AutoLibraryLoader.enable()
from ROOT import edm, JetCorrectionUncertainty

# please note that python selector class name (here: HLTBalanceTreeProducer) 
# should be consistent with this file name (HLTBalanceTreeProducer.py)

# you have to run this file from directory where it is saved


# Setup:
# ln -s ../MNxsectionAna/BalanceTreeProducer.py
# ln -s ../MNxsectionAna/balanceFitAndPlot.py
# ln -s ../MNxsectionAna/drawBalance.py
import BalanceTreeProducer 
from MNTriggerStudies.MNTriggerAna.JetGetter import JetGetter

class HLTBalanceTreeProducer(BalanceTreeProducer.BalanceTreeProducer):
    def init(self):
        BalanceTreeProducer.BalanceTreeProducer.init(self)
        self.addExternalVar(["hltPtAve"])
        self.addExternalVar(["hltPtCen"])
        self.addExternalVar(["hltPtFwd"])
        self.addExternalVar(["hltL1MatchPtCen"])
        self.addExternalVar(["hltL1MatchPtFwd"])
        self.addExternalVar(["l1DoubleJet"])
        self.addExternalVar(["l1SingleJetCentral"])
        self.addExternalVar(["l1SingleJetForward"])
        self.addExternalVar(["s1l1SingleJetCentral"])
        self.addExternalVar(["s1l1SingleJetForward"])


        self.addExternalVar(["s1DoubleJetCFDphi31"])
        self.addExternalVar(["s1DoubleJetCFDphi27"])
        self.addExternalVar(["s1DoubleJetCFDphi24"])
        self.addExternalVar(["s1DoubleJetCFDphi20"])
        self.addExternalVar(["s1DoubleJetCFDphi17"])


        self.addExternalVar(["PUNumInteractions"])
        self.addExternalVar(["puTrueNumInteractions"])


        # for the PU file run
        # utils/GetFlatPUDist.py
        puFile = edm.FileInPath("MNTriggerStudies/MNTriggerAna/test/mnTrgAnalyzer/PUhists.root").fullPath()

        self.newlumiWeighters = {}
        self.newlumiWeighters["flat010toPU1"] = edm.LumiReWeighting(puFile, puFile, "Flat0to10/pileup", "PU1/pileup")
        self.newlumiWeighters["flat010toPU2"] = edm.LumiReWeighting(puFile, puFile, "Flat0to10/pileup", "PU2/pileup")
        self.newlumiWeighters["flat010toPU3"] = edm.LumiReWeighting(puFile, puFile, "Flat0to10/pileup", "PU3/pileup")
        self.newlumiWeighters["flat010toPU4"] = edm.LumiReWeighting(puFile, puFile, "Flat0to10/pileup", "PU4/pileup")
        self.newlumiWeighters["flat010toPU5"] = edm.LumiReWeighting(puFile, puFile, "Flat0to10/pileup", "PU5/pileup")
        self.newlumiWeighters["flat010toPU10"] = edm.LumiReWeighting(puFile, puFile, "Flat0to10/pileup", "PU10/pileup")
        self.newlumiWeighters["flat2050toPU20"] = edm.LumiReWeighting(puFile, puFile, "Flat20to50/pileup", "PU20/pileup")
        self.newlumiWeighters["flat2050toPU25"] = edm.LumiReWeighting(puFile, puFile, "Flat20to50/pileup", "PU25/pileup")
        self.newlumiWeighters["flat2050toPU30"] = edm.LumiReWeighting(puFile, puFile, "Flat20to50/pileup", "PU30/pileup")
        self.addExternalVar(self.newlumiWeighters.keys())

    #deltaPHI: 0.0 0.349 0.698 1.047 1.396 1.745 2.094 2.443 2.792 3.141
    def getBestL1PairWithPhiSeparation(self, jets, dphiTHR):
        bestThr = 0
        for i in xrange(jets.size()):
            iJet = jets.at(i)
            if abs(iJet.eta()) > 1.7: continue
            for j in xrange(0, jets.size()):
                jJet = jets.at(j)
                if abs(jJet.eta()) < 2.5: continue
                dphi = abs(ROOT.Math.VectorUtil.DeltaPhi(iJet, jJet))
                if dphi < dphiTHR: continue
                minPT = min(iJet.pt(), jJet.pt())
                if minPT > bestThr: bestThr = minPT
        return bestThr

    def getHLTTagProbe(self, hltJets):
        probe = None
        tag = None

        for j in hltJets:
            pt = j.pt()
            if pt < 10.: continue
            eta = abs(j.eta())
            tagCand = eta < 1.4
            probeCand = eta > 2.7 and eta < 5.2

            if probeCand and (probe == None or probe.pt() < pt): probe = j
            if tagCand and (tag == None or tag.pt() < pt): tag = j

        return (tag, probe)

    def analyze(self):
        tag, probe = self.getHLTTagProbe(self.fChain.hltAK4PFJetsCorrected)
        tagL1match, probeL1match = self.getHLTTagProbe(self.fChain.hltPFJetsCorrectedMatchedToL1)


        avePT = 0 # this are all HLT level values!
        tagPT = 0 
        probePT = 0
        tagL1matchPT = 0 
        probeL1matchPT = 0
        
        if probe != None and tag!=None:  
            #print "XXX", tag.pt(), probe.pt()
            avePT = (tag.pt() + probe.pt())/2.
            tagPT = tag.pt()
            probePT = probe.pt()

        if probeL1match != None:
            probeL1matchPT = probeL1match.pt()

        if tagL1match != None:
            tagL1matchPT = tagL1match.pt()


        self.setExternalVar("hltL1MatchPtCen", tagL1matchPT)
        self.setExternalVar("hltL1MatchPtFwd", probeL1matchPT)


        self.setExternalVar("hltPtAve", avePT)
        self.setExternalVar("hltPtCen", tagPT)
        self.setExternalVar("hltPtFwd", probePT)
        self.setExternalVar("PUNumInteractions", self.fChain.PUNumInteractions)
        self.setExternalVar("puTrueNumInteractions", self.fChain.puTrueNumInteractions)


        l1Jets = self.fChain.l1Jets
        s1l1Jets = self.fChain.stage1L1Jets
        #print "XX"
        todo = {}
        todo["old"] = l1Jets
        todo["stage1"] = s1l1Jets

        #  0.0 0.34906578064 0.698131561279 1.04719740549 1.39626330534 1.74532920519 2.09439510107 2.44346088568 2.79252672195 3.14159256617
        self.setExternalVar("s1DoubleJetCFDphi31", self.getBestL1PairWithPhiSeparation(s1l1Jets, 3.1))
        self.setExternalVar("s1DoubleJetCFDphi27", self.getBestL1PairWithPhiSeparation(s1l1Jets, 2.7))
        self.setExternalVar("s1DoubleJetCFDphi24", self.getBestL1PairWithPhiSeparation(s1l1Jets, 2.4))
        self.setExternalVar("s1DoubleJetCFDphi20", self.getBestL1PairWithPhiSeparation(s1l1Jets, 2.0))
        self.setExternalVar("s1DoubleJetCFDphi17", self.getBestL1PairWithPhiSeparation(s1l1Jets, 1.7))


        for t in todo:
            pts = []
            hardestL1Central = 0
            hardestL1Forwad  = 0

            # eta l1 scale:  -0.174 -0.5215 -0.8695 -1.218 -1.566 -1.956 -2.586 -3.25 -3.75 -4.25 -4.75
            for j in todo[t]:
                #print "PPP", j.phi()
                pts.append(j.pt())
                if abs(j.eta()) < 1.7 and hardestL1Central < j.pt():
                    hardestL1Central = j.pt()
                if abs(j.eta()) > 2.5 and hardestL1Forwad < j.pt():
                    hardestL1Forwad = j.pt()

            top2 = sorted(pts)[-2:]
            doubleJetLowestThr = 1000
            if len(top2) == 2:
                doubleJetLowestThr = top2[0]

            #print "A", pts
            #print "B", top2
            #print "C", doubleJetLowestThr
            if t == "old":
                self.setExternalVar("l1DoubleJet", doubleJetLowestThr)
                self.setExternalVar("l1SingleJetCentral", hardestL1Central)
                self.setExternalVar("l1SingleJetForward", hardestL1Forwad)
            elif t == "stage1":
                self.setExternalVar("s1l1SingleJetCentral", hardestL1Central)
                self.setExternalVar("s1l1SingleJetForward", hardestL1Forwad)
            else:
                raise Exception("thats surprising!")

        pu = self.fChain.PUNumInteractions
        genW = BalanceTreeProducer.BalanceTreeProducer.genWeight(self)
        for l in self.newlumiWeighters:
            w = self.newlumiWeighters[l].weight(pu)
            self.setExternalVar(l, w*genW)


        BalanceTreeProducer.BalanceTreeProducer.analyze(self)

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

    #slaveParams["recoJetCollection"] = "pfJets"
    #slaveParams["recoJetCollection"] = "pfJetsSmear"
    #slaveParams["recoJetCollectionBaseReco"] = "pfJets"
    #slaveParams["recoJetCollectionGEN"] = "pfJets2Gen"
    #slaveParams["recoJetCollection"] = "caloJets"
    #slaveParams["recoJetCollection"] = "caloJetsSmear"

    slaveParams["HLT2015TempWorkaround"] =  True
    slaveParams["doPtShiftsJER"] = False
    slaveParams["doPtShiftsJEC"] = False


    '''
    sampleList=["QCD_Pt-300to470_Tune4C_13TeV_pythia8"]
    nWorkers = 1
    maxFilesMC = 12
    #'''
    #maxFilesMC = 1
    #nWorkers=1
    #treeName = "mnTriggerAna"
    slaveParams["ptMin"] = 20
    slaveParams["etaMax"] = 5

    out = "treeDiJetBalance.root"
    HLTBalanceTreeProducer().runAll(treeName="MNTriggerAnaNew",
                           slaveParameters=slaveParams,
                           sampleList=sampleList,
                           maxFilesMC = maxFilesMC,
                           maxFilesData = maxFilesData,
                           nWorkers=nWorkers,
                           outFile = out )


