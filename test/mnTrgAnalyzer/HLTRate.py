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
        self.doubleFwdTrigger = BaseTrigger.DoubldForwardTrigger(getter)
        self.atLeastOneCentral = BaseTrigger.DoubleJetWithAtLeastOneCentralJetTrigger(getter)
        self.ptAveForJecTrigger = BaseTrigger.PTAveForHFJecTrigger(getter)
        self.singleJetTrigger = BaseTrigger.SingleJetTrigger(getter)
                    
        self.histos = {} # name -> trigger, histo, rLow, rHigh
        self.histos["fb"] = [self.fbTrigger, None, -14.5, 29.5]
        self.histos["doubleForward"] = [self.doubleFwdTrigger, None, -14.5, 29.5]
        self.histos["atLeastOneCentral"] = [self.atLeastOneCentral, None, -14.5, 29.5]
        self.histos["singleJet"] = [self.singleJetTrigger, None, 299.5, 399.5]
        self.histos["ptAveHFJEC"] = [self.ptAveForJecTrigger, None, 14.5, 39.5]

        for t in self.histos:
            nbins = int(self.histos[t][3]-self.histos[t][2])
            name = t+"_rate"
            self.histos[t][1] = ROOT.TH1F(name, name, nbins, self.histos[t][2], self.histos[t][3])
            self.histos[t][1].Sumw2()
            self.GetOutputList().Add(self.histos[t][1])

    # TODO: implement weighting!!!!
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
        # TODO: implement weighting!!!!
        for t in self.histos:
            thr = self.histos[t][0].getMaxThreshold()
            if thr > 0.5:
                self.fillRate(self.histos[t][1], thr )

    def finalize(self):
        print "Finalize:"
        normFactor = self.getNormalizationFactor()
        print "  applying norm", normFactor
        for h in self.histos:
            self.histos[h][1].Scale(normFactor)

if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    ROOT.gSystem.Load("libFWCoreFWLite.so")
    AutoLibraryLoader.enable()

    sampleList = None # run through all
    #maxFilesMC = None
    nWorkers = None

    '''
    sampleList = ["QCD_Pt-30to50_Tune4C_13TeV_pythia8",]
    #sampleList = ["QCD_Pt-10to15_Tune4C_13TeV_pythia8",]
    maxFilesMC = 1
    nWorkers = 1
    # '''
    maxFilesMC = 32

    slaveParams = {}

    # select hltCollection here (see plugins/MNTriggerAna.cc to learn whats avaliable):
    slaveParams["hltCollection"] = "hltAK5PFJetL1FastL2L3Corrected"

    # note - remove maxFiles parameter in order to run on all files
    HLTRate.runAll(treeName="mnTriggerAna", 
                               slaveParameters=slaveParams,
                               sampleList=sampleList,
                               maxFilesMC = maxFilesMC,
                               nWorkers=nWorkers,
                               outFile = "HLTRatePlots.root" )
                                
