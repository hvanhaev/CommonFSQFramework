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
# ln -s ../MNxsectionAna/HLTMCWeighter.py
import BalanceTreeProducer 
from MNTriggerStudies.MNTriggerAna.JetGetter import JetGetter

import BaseTrigger


class HLTBalanceTreeProducer(BalanceTreeProducer.BalanceTreeProducer):
    def init(self):
        BalanceTreeProducer.BalanceTreeProducer.init(self)
        self.addExternalVar(["genW"])
        self.addExternalVar(["hltPtAve"])
        self.addExternalVar(["hltPtCen"])
        self.addExternalVar(["hltPtFwd"])
        self.addExternalVar(["hltCaloPtAve"])
        self.addExternalVar(["hltCaloPtCen"])
        self.addExternalVar(["hltCaloPtFwd"])

        #self.addExternalVar(["hltL1MatchPtCen"])
        #self.addExternalVar(["hltL1MatchPtFwd"])
        #self.addExternalVar(["l1DoubleJet"])
        #self.addExternalVar(["l1SingleJetCentral"])
        #self.addExternalVar(["l1SingleJetForward"])
        self.addExternalVar(["s1l1SingleJetCentral"])
        self.addExternalVar(["s1l1SingleJetForward"])
        self.addExternalVar(["s1l1SingleJetAny"])

        #hltgetter = BaseTrigger.TriggerObjectsGetter(self.fChain, "hltAK4PFJetsCorrected")
        #hltgetter = BaseTrigger.TriggerObjectsGetter(self.fChain, "PFAK4CHSnewjets")
        hltgetter = BaseTrigger.TriggerObjectsGetter(self.fChain, "recoPFAK4ChsCorrectedMyRhop4")
        #hltgetter = BaseTrigger.TriggerObjectsGetter(self.fChain, "recoPFAK4ChsCorrectedp4")
        print "Note: will go through reco jets and not hlt jets!"
        # note: this file is a mess. Source collection defined in couple of places, so look out

        self.hltAveFromPython = BaseTrigger.PTAveProperTrigger(hltgetter)
        self.addExternalVar(["hltAveFromPython"])
        self.addExternalVar(["hltCaloPreselection"])




        '''
        self.addExternalVar(["s1DoubleJetCFDphi31"])
        self.addExternalVar(["s1DoubleJetCFDphi27"])
        self.addExternalVar(["s1DoubleJetCFDphi24"])
        self.addExternalVar(["s1DoubleJetCFDphi20"])
        self.addExternalVar(["s1DoubleJetCFDphi17"])
        '''


        self.addExternalVar(["PUNumInteractions"])
        self.addExternalVar(["puTrueNumInteractions"])

        #self.addExternalVar(["trgptAve60CenFwd"])
        #self.addExternalVar(["trgptAve80CenFwd"])



        # for the PU file run
        # utils/GetFlatPUDist.py
        puFile = edm.FileInPath("MNTriggerStudies/MNTriggerAna/test/mnTrgAnalyzer/PUhists.root").fullPath()

        self.newlumiWeighters = {}
        '''
        self.newlumiWeighters["flat010toflat010"] = edm.LumiReWeighting(puFile, puFile, "Flat0to10/pileup", "Flat0to10/pileup")
        self.newlumiWeighters["flat010toPU1"] = edm.LumiReWeighting(puFile, puFile, "Flat0to10/pileup", "PU1/pileup")
        #self.newlumiWeighters["flat010toPU2"] = edm.LumiReWeighting(puFile, puFile, "Flat0to10/pileup", "PU2/pileup")
        #self.newlumiWeighters["flat010toPU3"] = edm.LumiReWeighting(puFile, puFile, "Flat0to10/pileup", "PU3/pileup")
        #self.newlumiWeighters["flat010toPU4"] = edm.LumiReWeighting(puFile, puFile, "Flat0to10/pileup", "PU4/pileup")
        self.newlumiWeighters["flat010toPU5"] = edm.LumiReWeighting(puFile, puFile, "Flat0to10/pileup", "PU5/pileup")
        self.newlumiWeighters["flat010toPU10"] = edm.LumiReWeighting(puFile, puFile, "Flat0to10/pileup", "PU10/pileup")
        #'''
        #'''
        self.newlumiWeighters["flat2050toPU10"] = edm.LumiReWeighting(puFile, puFile, "Flat20to50/pileup", "PU10/pileup")
        self.newlumiWeighters["flat2050toPU15"] = edm.LumiReWeighting(puFile, puFile, "Flat20to50/pileup", "PU15/pileup")
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

        #if tag and probe:
        #    print "XXX", tag.pt(), probe.pt()
        return (tag, probe)

    def emulateHLTAveNew(self, l1jets, hltJets, minJetPT, l1thr, aveMin):
        for j in l1jets:
            if j.pt() > l1thr:
                break
        else:
            return 0

        probes = []
        tags = []

        for j in hltJets:
            pt = j.pt()
            if pt < minJetPT: continue
            eta = abs(j.eta())
            if eta < 1.4: tags.append(j)
            if eta > 2.7 and eta < 5.5: probes.append(j)

        if not probes or not tags: return 0
        bestAve = 0
        for t in tags:
            for p in probes:
                dphi = abs(ROOT.Math.VectorUtil.DeltaPhi(t, p))
                if dphi < 1.5: continue
                ave = (p.pt()+t.pt())/2
                if ave > bestAve: bestAve = ave


            
        if bestAve > aveMin: return 1
        return 0

    def analyzeDumb(self):
    #def analyze(self):
        self.setExternalVar("PUNumInteractions", self.fChain.PUNumInteractions)
        self.setExternalVar("puTrueNumInteractions", self.fChain.puTrueNumInteractions)

        pu = self.fChain.PUNumInteractions
        genW = BalanceTreeProducer.BalanceTreeProducer.genWeight(self)
        for l in self.newlumiWeighters:
            w = self.newlumiWeighters[l].weight(pu)
            #print pu, l, w, genW
            self.setExternalVar(l, w*genW)

        BalanceTreeProducer.BalanceTreeProducer.analyze(self)


    #def analyzeGood(self):
    def analyze(self):
        thr = self.hltAveFromPython.getMaxThreshold()
        self.setExternalVar("hltAveFromPython", thr)
        #     cut = cms.string( "pt>40 && (abs(eta)<1.4 || abs(eta) > 2.7)" )
        '''
        bestCalo = 0
        for j in self.fChain.hltAK4CaloJetsCorrected:
            eta = abs(j.eta())
            if eta > 1.4 and eta < 2.7:
                continue
            pt = j.pt()
            if pt > bestCalo: bestCalo = pt

        self.setExternalVar("hltCaloPreselection", bestCalo)
        '''



        '''
        #s1l1Jets = self.fChain.stage1L1Jets
        tmpl1 = self.fChain.oldL1Jets
        #tmpl1 = self.fChain.stage1L1Jets
        tmphlt =  self.fChain.hltAK4PFJetsCorrected
        #     def emulateHLTAveNew(self, l1jets, hltJets, minJetPT, l1thr, ave):
        res60 = self.emulateHLTAveNew(tmpl1, tmphlt, 30, 34, 60)
        res80 = self.emulateHLTAveNew(tmpl1, tmphlt, 20, 66, 40)

        dbg = False
        if abs(res60-self.fChain.trgnewAve60) > 0.1: 
            print "XXXProblem 60: ", res60, self.fChain.trgnewAve60
            dbg = True

        else: 
            print "YYYOK 60"
        if abs(res80-self.fChain.trgnewAve80) > 0.1: 
            print "XXXProblem 80: ", res60, self.fChain.trgnewAve80
            dbg = True
        else: 
            print "YYYOK 80"

        if dbg: 
            for l1 in tmpl1:
                print "l1", l1.pt()
            for hlt in tmphlt:
                if hlt.pt() < 29: continue
                print "hlt", hlt.pt(), hlt.eta(), hlt.phi()

        return
        #'''

        todo = {}
        #todo["hlt"] = self.getHLTTagProbe(self.fChain.hltAK4PFJetsCorrected)
        #todo["hlt"] = self.getHLTTagProbe(self.fChain.PFAK4CHSnewjets)
        #todo["hltL1match"] = self.getHLTTagProbe(self.fChain.hltAK4PFJetsCorrected)
        #todo["hltCalo"] = self.getHLTTagProbe(self.fChain.hltAK4CaloJetsCorrected)
        #tag, probe = self.getHLTTagProbe(self.fChain.hltAK4PFJetsCorrected)
        #tagCalo, probeCalo = self.getHLTTagProbe(self.fChain.hltAK4CaloJetsCorrected)
        #tagL1match, probeL1match = self.getHLTTagProbe(self.fChain.hltPFJetsCorrectedMatchedToL1)

        for t in todo:
            avePT = 0 # this are all HLT level values!
            tagPT = 0 
            probePT = 0
            tagL1matchPT = 0 
            probeL1matchPT = 0
            tag = todo[t][0]
            probe = todo[t][1]
            
            if probe != None and tag!=None:  
                #print "XXX", tag.pt(), probe.pt()
                avePT = (tag.pt() + probe.pt())/2.
                tagPT = tag.pt()
                probePT = probe.pt()

            #print t, tagPT, probePT
            self.setExternalVar(t+"PtAve", avePT)
            self.setExternalVar(t+"PtCen", tagPT)
            self.setExternalVar(t+"PtFwd", probePT)



        self.setExternalVar("PUNumInteractions", self.fChain.PUNumInteractions)
        self.setExternalVar("puTrueNumInteractions", self.fChain.puTrueNumInteractions)

        #self.setExternalVar("trgptAve60CenFwd", self.fChain.trgptAve60CenFwd)
        #self.setExternalVar("trgptAve80CenFwd", self.fChain.trgptAve80CenFwd)

        #l1Jets = self.fChain.l1Jets
        # xxx -  disabled L1!!!
        #s1l1Jets = self.fChain.stage1L1Jets
        #print "XX"
        todo = {}
        #todo["old"] = l1Jets
        #todo["stage1"] = s1l1Jets

        #  0.0 0.34906578064 0.698131561279 1.04719740549 1.39626330534 1.74532920519 2.09439510107 2.44346088568 2.79252672195 3.14159256617
        ##self.setExternalVar("s1DoubleJetCFDphi31", self.getBestL1PairWithPhiSeparation(s1l1Jets, 3.1))
        #self.setExternalVar("s1DoubleJetCFDphi27", self.getBestL1PairWithPhiSeparation(s1l1Jets, 2.7))
        ##self.setExternalVar("s1DoubleJetCFDphi24", self.getBestL1PairWithPhiSeparation(s1l1Jets, 2.4))
        #self.setExternalVar("s1DoubleJetCFDphi20", self.getBestL1PairWithPhiSeparation(s1l1Jets, 2.0))
        #self.setExternalVar("s1DoubleJetCFDphi17", self.getBestL1PairWithPhiSeparation(s1l1Jets, 1.7))


        for t in todo:
            pts = []
            hardestL1Central = 0
            hardestL1Forwad  = 0
            hardestL1  = 0

            # eta l1 scale:  -0.174 -0.5215 -0.8695 -1.218 -1.566 -1.956 -2.586 -3.25 -3.75 -4.25 -4.75
            for j in todo[t]:
                pt = j.pt()
                if pt > hardestL1: hardestL1 = pt
                eta = abs(j.eta())
                if abs(j.eta()) < 1.7 and hardestL1Central < j.pt():
                    hardestL1Central = j.pt()
                if abs(j.eta()) > 2.5 and hardestL1Forwad < j.pt():
                    hardestL1Forwad = j.pt()



            if t == "stage1":
                #print "L1", hardestL1
                self.setExternalVar("s1l1SingleJetAny", hardestL1)
                self.setExternalVar("s1l1SingleJetCentral", hardestL1Central)
                self.setExternalVar("s1l1SingleJetForward", hardestL1Forwad)

            '''
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
                self.setExternalVar("s1l1SingleJetAny", hardestL1)
            else:
                raise Exception("thats surprising!")
            '''

        pu = self.fChain.PUNumInteractions
        genW = BalanceTreeProducer.BalanceTreeProducer.genWeight(self)
        self.setExternalVar("genW", genW)
        for l in self.newlumiWeighters:
            w = self.newlumiWeighters[l].weight(pu)
            self.setExternalVar(l, w*genW)

        if self.standalone:
            BalanceTreeProducer.BalanceTreeProducer.setExternals(self)
            BalanceTreeProducer.BalanceTreeProducer.fillGenWeight(self)
            BalanceTreeProducer.BalanceTreeProducer.fill(self)
            BalanceTreeProducer.BalanceTreeProducer.resetExternals(self)
            #print "XXXX, filled"
        else:
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
    #slaveParams["standalone"] = True
    slaveParams["standalone"] = False

    # recoPFAK4ChsCorrectedMyRhop4
    #sampleList=["QCD_Pt-50to80_Tune4C_13TeV_pythia8"]
    #sampleList=["QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8"]
    #sampleList=["QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8_Pu20"]
    #'''
    nWorkers = 10
    #maxFilesMC = 12
    #'''
    #maxFilesMC = 1
    maxFilesMC = 10
    #nWorkers=1
    #treeName = "mnTriggerAna"
    slaveParams["ptMin"] = 10
    slaveParams["etaMax"] = 5.2

    out = "treeDiJetBalance.root"
    HLTBalanceTreeProducer().runAll(treeName="MNTriggerAnaNew",
                           slaveParameters=slaveParams,
                           sampleList=sampleList,
                           maxFilesMC = maxFilesMC,
                           maxFilesData = maxFilesData,
                           nWorkers=nWorkers,
                           usePickle = True,
                           useProofOFile = True,
                           outFile = out )


