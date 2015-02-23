#!/usr/bin/env python


import sys, os, time, math
sys.path.append(os.path.dirname(__file__))

import ROOT
ROOT.gROOT.SetBatch(True)
from ROOT import *

from array import *

# please note that python selector class name (here: RateSimple) 
# should be consistent with this file name (RateSimple.py)

# you have to run this file from directory where it is saved

import MNTriggerStudies.MNTriggerAna.ExampleProofReader 

import BaseTrigger

class RateSimple(MNTriggerStudies.MNTriggerAna.ExampleProofReader.ExampleProofReader):
    def init(self):
        self.cnt = 0

        self.dist = ROOT.TH1F("dist", "; jet seed threshold", 21, -0.5,20.5 )
        self.dist.Sumw2()
        self.GetOutputList().Add(self.dist)


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
        jets  = self.fChain.oldRedoneL1Jets
        #jets  = self.fChain.hltAK4PFJets
        #jets = self.fChain.hltAK4PFJetsCorrected

        try:
            #bestJet = max(jets, key=lambda j: j.pt())
            #maxThr = bestJet.pt()
            maxThr = 0.
            for i in xrange(jets.size()):
                for j in xrange(jets.size()):
                    if i==j: continue
                    contender = min(jets.at(i).pt(), jets.at(j).pt())
                    if contender > maxThr:
                        maxThr = contender
        except ValueError:
            maxThr = 0

        self.fillRate(self.dist, maxThr, 1.)


    def finalizeWhenMerged(self):
        olist =  self.GetOutputList()
        histos = {}
        for o in olist:
            if not "TH1" in o.ClassName(): continue
            histos[o.GetName()]=o

        lhcFreq = 4E7 # 40 MHz
        totalBunches = 3564.
        #  (usually 2662 for 25ns bunch spacing, 1331 for 50ns bunch spacing) 
        filledBunches = 40.

        PU=0.01

        rateScalingFactor = lhcFreq*float(filledBunches)/float(totalBunches)*PU

        eff = histos["dist"].Clone("eff")
        eff.Scale(1./(eff.GetBinContent(1)))

        rate = eff.Clone("rate")
        rate.Scale(rateScalingFactor)
        self.GetOutputList().Add(eff)
        self.GetOutputList().Add(rate)

if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    ROOT.gSystem.Load("libFWCoreFWLite.so")
    AutoLibraryLoader.enable()

    sampleList = ["MinBias_TuneZ2star_13TeV_pythia6_162"]
    maxFilesMC = 1
    nWorkers = 1
    slaveParams = {}


    # note - remove maxFiles parameter in order to run on all files
    RateSimple.runAll(treeName="MNTriggerAnaNew",
                               slaveParameters=slaveParams,
                               sampleList=sampleList,
                               maxFilesMC = maxFilesMC,
                               nWorkers=nWorkers,
                               outFile = "SimpleRatePlots.root" )
                                
