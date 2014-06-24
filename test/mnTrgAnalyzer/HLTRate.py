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
        getter = BaseTrigger.TriggerObjectsGetter(self.fChain, self.hltCollection)
        self.fbTrigger = BaseTrigger.ForwardBackwardTrigger(getter)
        self.ptAveForJecTrigger = BaseTrigger.PTAveForHFJecTrigger(getter)
        self.singleJetTrigger = BaseTrigger.SingleJetTrigger(getter)
                    
        self.hist = {}

        n = "fb_rate"
        self.hist[n] = ROOT.TH1F(n, n, 30, -0.5, 29.5)

        n = "singleJet_rate"
        self.hist[n] = ROOT.TH1F(n, n, 100, 299.5, 399.5)

        n = "ptAveHFJEC_rate"
        self.hist[n] = ROOT.TH1F(n, n, 25, 14.5, 39.5)

        for t in self.hist:
            self.hist[t].Sumw2()
            self.GetOutputList().Add(self.hist[t])

    def fillRate(self, hist, maxThr):
        nbins = hist.GetNbinsX()
        getBinCenter = hist.GetXaxis().GetBinCenter
        fill = hist.Fill
        for i in xrange(1,nbins+1):
            binCenter = getBinCenter(i)
            if binCenter <= maxThr:
                fill(binCenter)
            else:
                break

        del fill
        del getBinCenter

    def analyze(self):
        weight = 1. # calculate your event weight here

        thr = self.singleJetTrigger.getMaxThreshold()
        if thr > 0.5:
            self.fillRate(self.hist["singleJet_rate"], thr )

        thr = self.ptAveForJecTrigger.getMaxThreshold()
        if thr > 0.5:
            self.fillRate(self.hist["ptAveHFJEC_rate"], thr )

        thr = self.fbTrigger.getMaxThreshold()
        if thr > 0.5:
            self.fillRate(self.hist["fb_rate"], thr)            

    def finalize(self):
        print "Finalize:"
        normFactor = self.getNormalizationFactor()
        print "  applying norm", normFactor
        for h in self.hist:
            self.hist[h].Scale(normFactor)

if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    ROOT.gSystem.Load("libFWCoreFWLite.so")
    AutoLibraryLoader.enable()

    sampleList = None # run through all
    maxFilesMC = 32
    #maxFilesMC = None
    nWorkers = None

    '''
    sampleList = ["QCD_Pt-30to50_Tune4C_13TeV_pythia8",]
    #sampleList = ["QCD_Pt-10to15_Tune4C_13TeV_pythia8",]
    maxFilesMC = 1
    nWorkers = 1
    # '''

    slaveParams = {}

    # select hltCollection here (see plugins/MNTriggerAna.cc to learn whats avaliable):
    slaveParams["hltCollection"] = "hltAK5PFJetL1FastL2L3Corrected"

    # note - remove maxFiles parameter in order to run on all files
    HLTRate.runAll(treeName="mnTriggerAna", 
                               slaveParameters=slaveParams,
                               sampleList=sampleList,
                               maxFilesMC = maxFilesMC,
                               nWorkers=nWorkers,
                               outFile = "TestHLTPlots.root" )
                                
