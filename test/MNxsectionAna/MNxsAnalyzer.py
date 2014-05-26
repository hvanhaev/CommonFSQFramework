#!/usr/bin/env python


import sys, os, time
sys.path.append(os.path.dirname(__file__))

import ROOT
ROOT.gROOT.SetBatch(True)
from ROOT import *

from array import *
#import cProfile

# please note that python selector class name (here: MNxsAnalyzer) 
# should be consistent with this file name (MNxsAnalyzer.py)

# you have to run this file from directory where it is saved


from MNTriggerStudies.MNTriggerAna.ExampleProofReader import ExampleProofReader

#import DiJetBalancePlugin

class MNxsAnalyzer(ExampleProofReader):
    def configureAnalyzer( self):

        #sys.stdout = sys.stderr
        #self.pr = cProfile.Profile()
        print "XXX configureAnalyzer - MNxsAnalyzer", self.datasetName, self.isData

        self.todoShifts = ["_central"]
        if hasattr(self, "jetUncFile") and not self.isData and self.doPtShifts:
            self.todoShifts.append("_ptUp")
            self.todoShifts.append("_ptDown")
            self.jetUnc = JetCorrectionUncertainty(self.jetUncFile)


        #self.djBalance = DiJetBalancePlugin.DiJetBalancePlugin(self.recoJetCollection)

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


    def ptShifted(self, jet, shift):
        if not shift.startswith("_pt"): return jet.pt()
        if self.isData:
            raise Exception("pt shift for data called")


        pt = jet.pt()
        self.jetUnc.setJetEta(jet.eta())
        self.jetUnc.setJetPt(pt) # corrected pt
        unc = self.jetUnc.getUncertainty(true)
        if "_ptUp" == shift:
            ptFactor = 1.
        elif "_ptDown" == shift:
            ptFactor = -1.
        pt *= (1. + ptFactor*unc)

        if pt < 0: return 0
        return pt 


    '''
    # stuff for code profiling
    def analyze(self):
        self.pr.enable()
        self.analyzeTT()
        self.pr.disable()


    def SlaveTerminate( self ):
        print 'py: slave terminating AAZAZ'
        dname = "/scratch/scratch0/tfruboes/2014.05.NewFWAnd4_2/CMSSW_4_2_8_patch7/src/MNTriggerStudies/MNTriggerAna/test/MNxsectionAna/stats/"
        profName = dname + "stats"
        self.pr.dump_stats(profName)
    '''
        


    #def analyzeTT(self):
    def analyze(self):
            
        #if self.fChain.jet15 > 0.5:
        #    print "XXX", self.fChain.run, self.fChain.lumi
        #    sys.stdout.flush()
        #print "testXX", self.datasetName, self.isData
        #sys.stdout.flush()
        #event = self.fChain.event
        #run = self.fChain.run
        #lumi = self.fChain.lumi
        #print event

        #print "XXDS", self.datasetName, self.isData
        if self.fChain.ngoodVTX == 0: return

        recoJets = getattr(self.fChain, self.recoJetCollection)

        for shift in self.todoShifts:
            weightBase = 1. 
            if not self.isData:
                weightBase *= self.fChain.genWeight # keep inside shift iter

            # find best jet
            mostFwdJet = None
            mostBkgJet = None
            mostFwdJetEta = None
            mostBkgJetEta = None
            for i in xrange(0, recoJets.size()):
                jet = recoJets.at(i)



                if self.ptShifted(jet, shift) < self.threshold: continue
                eta = jet.eta()
                if abs(eta) > 4.7: continue
                #if abs(eta) > 3: continue
                if  mostFwdJet == None or mostFwdJetEta < eta:
                    mostFwdJet = i
                    mostFwdJetEta = eta
                if  mostBkgJet == None or mostBkgJetEta > eta:
                    mostBkgJet = i
                    mostBkgJetEta = eta

            #if mostFwdJet != None:
            #    print "Pair: F/B",  recoJets.at(mostFwdJet).eta(), recoJets.at(mostBkgJet).eta()
            pairFound = False
            if mostFwdJet != None and mostBkgJet != mostFwdJet:
                pairFound = True

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

                # TODO: vertex reweighting depending on trigger
                if gotTrigger:
                    leadJet = mostBkgJet
                    subleadJet = mostFwdJet
                    # self.ptShifted(jet.pt(), shift)
                    ptLead =  self.ptShifted( recoJets.at(leadJet), shift)
                    ptSublead =  self.ptShifted( recoJets.at(subleadJet), shift)

                    if ptSublead > ptLead:
                        ptLead, ptSublead = ptSublead, ptLead
                        leadJet, subleadJet = subleadJet, leadJet

                    #print recoJets.at(leadJet).pt(), weight
                    histoName = shift +triggerToUse


                    #
                    weight = weightBase
                    # puTrueNumInteractions
                    # _jet15_central
                    if not self.isData:
                        truePU = self.fChain.puTrueNumInteractions
                        puWeight =  self.lumiWeighters[triggerToUse+"_central"].weight(truePU)
                        weight *= puWeight


                    # why calling a fill method is so costly ?!?
                    #  -- cost is not comming from python
                    self.hist["ptLead"+histoName].Fill(ptLead, weight)
                    self.hist["ptSublead"+histoName].Fill(ptSublead, weight)
                    self.hist["etaLead"+histoName].Fill(recoJets.at(leadJet).eta(), weight)
                    self.hist["etaSublead"+histoName].Fill(recoJets.at(subleadJet).eta(), weight)
                    #print "DETA", deta, weight, 
                    self.hist["xsVsDeltaEta"+histoName].Fill(deta, weight)
                    self.hist["vtx"+histoName].Fill(self.fChain.ngoodVTX, weight)

        #self.djBalance.analyze(self.fChain)
        return 1



    @classmethod
    def testAll(cls):
        # same as the label of EDProducer that was used to produce the trees
        #todo = [400, 100, 25, 8, 2]
        todo =[1,6,25,100,400]
        #todo = [8]
        for t in todo:
            oname = "~/tmp/plots_"+str(t)+".root"
            onameMerged = "~/tmp/plotsMerged_"+str(t)+".root"
            #pr = MNxsAnalyzer()
            #pr.runAll(treeName="exampleTree", outFile = oname, maxFiles = t)
            #MNxsAnalyzer.MNxsAnalyzer().runAll(treeName="exampleTree", outFile = oname, maxFiles = t)
            cls.runAll(treeName="exampleTree", outFile = oname, maxFiles = t)
            os.system("../../scripts/normalizeAndAddHistograms.py -i "+oname + " -o " + onameMerged)



if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    ROOT.gSystem.Load("libFWCoreFWLite.so")
    AutoLibraryLoader.enable()

    sampleList = None
    maxFiles = None
    nWorkers = None # Use all

    # debug config:
    #sampleList= ["QCD_Pt-15to3000_TuneZ2star_Flat_HFshowerLibrary_7TeV_pythia6"]
    #sampleList=  ["JetMETTau-Run2010A-Apr21ReReco-v1"]
    #sampleList=  ["Jet-Run2010B-Apr21ReReco-v1"] 
    #sampleList = ["JetMET-Run2010A-Apr21ReReco-v1"]
    #sampleList = ["JetMETTau-Run2010A-Apr21ReReco-v1", "Jet-Run2010B-Apr21ReReco-v1", "JetMET-Run2010A-Apr21ReReco-v1", "METFwd-Run2010B-Apr21ReReco-v1"]
    #maxFiles = 2
    #maxFiles = 1
    #nWorkers = 1


    slaveParams = {}
    slaveParams["threshold"] = 35.
    #slaveParams["doPtShifts"] = False
    slaveParams["doPtShifts"] = True
    #slaveParams["recoJetCollection"] = "pfJets"
    slaveParams["recoJetCollection"] = "pfJetsSmear"
    #slaveParams["recoJetCollection"] = "caloJets"
    #slaveParams["recoJetCollection"] = "caloJetsSmear"

    #jetUncFile = "START42_V11_AK5PF_Uncertainty.txt"
    jetUncFile = "START41_V0_AK5PF_Uncertainty.txt"


    slaveParams["jetUncFile"] =  edm.FileInPath("MNTriggerStudies/MNTriggerAna/test/MNxsectionAna/"+jetUncFile).fullPath()


    MNxsAnalyzer.runAll(treeName="mnXS",
                               slaveParameters=slaveParams,
                               sampleList=sampleList,
                               maxFiles = maxFiles,
                               nWorkers=nWorkers,
                               outFile = "~/plotsMNxs.root" )



