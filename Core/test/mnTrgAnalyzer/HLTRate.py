#!/usr/bin/env python


import sys, os, time, math
sys.path.append(os.path.dirname(__file__))

import ROOT
ROOT.gROOT.SetBatch(True)
from ROOT import *

from array import *

# please note that python selector class name (here: HLTRate) 
# should be consistent with this file name (HLTRate.py)

# you have to run this file from directory where it is saved

import MNTriggerStudies.MNTriggerAna.ExampleProofReader 

import BaseTrigger

class HLTRate(MNTriggerStudies.MNTriggerAna.ExampleProofReader.ExampleProofReader):
    def init(self):
        self.avgW = 0.
        self.cnt = 0

        self.normFactor = self.getNormalizationFactor()
        puFile = edm.FileInPath("MNTriggerStudies/MNTriggerAna/test/mnTrgAnalyzer/PUhists.root").fullPath()
        self.newlumiWeighters = {}
        self.newlumiWeighters["flat2050toPU10"] = edm.LumiReWeighting(puFile, puFile, "Flat20to50/pileup", "PU10/pileup")
        #self.newlumiWeighters["flat2050toPU15"] = edm.LumiReWeighting(puFile, puFile, "Flat20to50/pileup", "PU15/pileup")
        #self.newlumiWeighters["flat2050toPU20"] = edm.LumiReWeighting(puFile, puFile, "Flat20to50/pileup", "PU20/pileup")
        #self.newlumiWeighters["flat2050toPU30"] = edm.LumiReWeighting(puFile, puFile, "Flat20to50/pileup", "PU30/pileup")
        #self.newlumiWeighters["flat2050toPU40"] = edm.LumiReWeighting(puFile, puFile, "Flat20to50/pileup", "PU40/pileup")
        #self.newlumiWeighters["flat2050toPU40"] = edm.LumiReWeighting(puFile, puFile, "Flat20to50/pileup", "PU40/pileup")
        #self.newlumiWeighters["flat010toPU10"] = edm.LumiReWeighting(puFile, puFile, "Flat0to10/pileup", "PU10/pileup")
        #self.newlumiWeighters["flat010toPU1"] = edm.LumiReWeighting(puFile, puFile, "Flat0to10/pileup", "PU1/pileup")
        #self.newlumiWeighters["PU20toPU20"] = edm.LumiReWeighting(puFile, puFile, "PU20/pileup", "PU20/pileup")



        getter = BaseTrigger.TriggerObjectsGetter(self.fChain, self.hltCollection)
        getterReco = BaseTrigger.TriggerObjectsGetter(self.fChain, self.recoCollection)
        #self.fbTrigger = BaseTrigger.ForwardBackwardTrigger(getter)
        #self.doubleFwdTrigger = BaseTrigger.DoubldForwardTrigger(getter)
        #self.atLeastOneCentral = BaseTrigger.DoubleJetWithAtLeastOneCentralJetTrigger(getter)
        #self.ptAveForJecTrigger = BaseTrigger.PTAveForHFJecTrigger(getter)
        #self.singleJetTrigger = BaseTrigger.SingleJetTrigger(getter)
        self.messed = BaseTrigger.PTAveMessedTrigger(getter)         
        self.proper = BaseTrigger.PTAveProperTrigger(getter)
        self.properForLumiEst = BaseTrigger.PTAveProperTrigger(getter,  etaTag = 1.3, etaProbeMin = 3.139, etaProbeMax = 5.191, minDphi=2.7)

        self.properReco = BaseTrigger.PTAveProperTrigger(getterReco, etaTag=1.3, etaProbeMin=3.139)

           
        self.histos = {} # name -> trigger, histo, rLow, rHigh
        #self.histos["ptAveMessed"] = [self.messed, None, 59.5, 81.5]

        '''
        self.histos["ptAveProper30_60"] = [self.properForLumiEst, None, 29.5, 61.5]
        self.histos["ptAveProper60_200"] = [self.properForLumiEst, None, 59.5, 201.5]
        self.histos["ptAveProper60_80"] = [self.properForLumiEst, None, 59.5, 81.5]
        self.histos["ptAveProper80_120"] = [self.properForLumiEst, None, 79.5, 121.5]
        self.histos["ptAveProper120_200"] = [self.properForLumiEst, None, 119.5, 200.5]
        self.histos["ptAveProper200_300"] = [self.properForLumiEst, None, 199.5, 300.5]
        self.histos["ptAveProper300_400"] = [self.properForLumiEst, None, 299.5, 400.5]
        '''

        self.histos["ptAveProper30_60"] = [self.proper, None, 29.5, 61.5]
        self.histos["ptAveProper60_200"] = [self.proper, None, 59.5, 201.5]
        self.histos["ptAveProper60_80"] = [self.proper, None, 59.5, 81.5]
        self.histos["ptAveProper80_120"] = [self.proper, None, 79.5, 121.5]
        self.histos["ptAveProper120_200"] = [self.proper, None, 119.5, 200.5]
        self.histos["ptAveProper200_300"] = [self.proper, None, 199.5, 300.5]
        self.histos["ptAveProper300_400"] = [self.proper, None, 299.5, 400.5]




        #self.histos["recoptAveProper30_60"] = [self.properReco, None, 29.5, 61.5]
        #self.histos["recoptAveProper60_80"] = [self.properReco, None, 59.5, 81.5]
        #self.histos["recoptAveProper80_120"] = [self.properReco, None, 79.5, 121.5]
        #self.histos["recoptAveProper120_200"] = [self.properReco, None, 119.5, 200.5]
        #self.histos["recoptAveProper200_300"] = [self.properReco, None, 199.5, 300.5]



        #self.histos["doubleForward"] = [self.doubleFwdTrigger, None, 14.5, 29.5]
        #self.histos["atLeastOneCentral"] = [self.atLeastOneCentral, None, 14.5, 29.5]
        #self.histos["singleJet"] = [self.singleJetTrigger, None, 299.5, 399.5]
        #self.histos["ptAveHFJEC"] = [self.ptAveForJecTrigger, None, 14.5, 39.5]

        for t in self.histos:
            nbins = int(self.histos[t][3]-self.histos[t][2])
            name = t+"_rate"
            self.histos[t][1] = ROOT.TH1F(name, name, nbins, self.histos[t][2], self.histos[t][3])
            self.histos[t][1].Sumw2()
            self.GetOutputList().Add(self.histos[t][1])

    def genWeight(self):
        #print "ASDFASD", self.fChain.genWeight
        return self.fChain.genWeight*self.normFactor

    def fillRate(self, hist, maxThr, weight):
        nbins = hist.GetNbinsX()
        getBinCenter = hist.GetXaxis().GetBinCenter
        for i in xrange(1,nbins+1):
            #binCenter = int(getBinCenter(i))
            binCenter = getBinCenter(i)

            # As always "<=" is a tricky thing...
            if binCenter < maxThr or abs(binCenter-maxThr) < 0.1:
                hist.Fill(binCenter, weight)
            else:
                break
        del getBinCenter


    def analyze(self):
        weight = self.genWeight()  # calculate your event weight here
        self.avgW += self.fChain.genWeight
        self.cnt += 1
        pu = self.fChain.PUNumInteractions
        for l in self.newlumiWeighters:
            wPU = self.newlumiWeighters[l].weight(pu)
            break

        # TODO: implement weighting!!!!
        for t in self.histos:
            thr = self.histos[t][0].getMaxThreshold()
            if thr > 0.5:
                self.fillRate(self.histos[t][1], thr, weight*wPU )

    def finalize(self):
        #pass
        #print "Finalize:"
        #normFactor = self.getNormalizationFactor()
        #print "  applying norm", normFactor
        self.avgW /= self.cnt
        for h in self.histos:
            self.histos[h][1].Scale(1/self.avgW)

if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    ROOT.gSystem.Load("libFWCoreFWLite.so")
    AutoLibraryLoader.enable()

    sampleList = None # run through all
    maxFilesMC = None
    nWorkers = None

    #'''
    #sampleList = ["QCD_Pt-30to50_Tune4C_13TeV_pythia8",]
    #sampleList = ["QCD_Pt-10to15_Tune4C_13TeV_pythia8",]
    #maxFilesMC = 12
    #nWorkers = 12
    # '''
    maxFilesMC = 400
    #maxFilesMC = 999
    nWorkers = 12

    slaveParams = {}

    # select hltCollection here (see plugins/MNTriggerAna.cc to learn whats avaliable):
    #slaveParams["hltCollection"] = "hltAK5PFJetL1FastL2L3Corrected"
    #slaveParams["hltCollection"] = "hltPFJetsCorrectedMatchedToL1"
    #slaveParams["hltCollection"] = "hltAK4PFJetsCorrected"
    slaveParams["hltCollection"] = "hltAK4PFJetsCorrectedp4"

    #slaveParams["recoCollection"] = "PFAK4CHSnewjets"
    slaveParams["recoCollection"] = "recoPFAK4ChsCorrectedMyRhop4"
    


    # note - remove maxFiles parameter in order to run on all files
    HLTRate.runAll(treeName="MNTriggerAnaNew",
                               slaveParameters=slaveParams,
                               sampleList=sampleList,
                               maxFilesMC = maxFilesMC,
                               nWorkers=nWorkers,
                               usePickle = True,
                               #useProofOFile = True,
                               outFile = "HLTRatePlots.root" )
                                
