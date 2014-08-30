#!/usr/bin/env python


import sys, os, time, math
sys.path.append(os.path.dirname(__file__))

import ROOT
ROOT.gROOT.SetBatch(True)
from ROOT import *

from array import *

# please note that python selector class name (here: L1Rate) 
# should be consistent with this file name (L1Rate.py)

# you have to run this file from directory where it is saved

import MNTriggerStudies.MNTriggerAna.ExampleProofReader 

class L1Rate(MNTriggerStudies.MNTriggerAna.ExampleProofReader.ExampleProofReader):
    def init(self):
        puFile = edm.FileInPath("MNTriggerStudies/MNTriggerAna/test/mnTrgAnalyzer/PUhists.root").fullPath()

        self.newlumiWeighters = {}
        self.newlumiWeighters["flat2050toPU20"] = edm.LumiReWeighting(puFile, puFile, "Flat20to50/pileup", "PU20/pileup")
        self.newlumiWeighters["flat2050toPU25"] = edm.LumiReWeighting(puFile, puFile, "Flat20to50/pileup", "PU25/pileup")
        self.newlumiWeighters["flat2050toPU30"] = edm.LumiReWeighting(puFile, puFile, "Flat20to50/pileup", "PU30/pileup")
        self.newlumiWeighters["flat2050toPU35"] = edm.LumiReWeighting(puFile, puFile, "Flat20to50/pileup", "PU35/pileup")
        self.newlumiWeighters["flat2050toPU40"] = edm.LumiReWeighting(puFile, puFile, "Flat20to50/pileup", "PU40/pileup")
        self.newlumiWeighters["flat2050toPU45"] = edm.LumiReWeighting(puFile, puFile, "Flat20to50/pileup", "PU45/pileup")
        self.newlumiWeighters["flat2050toPU50"] = edm.LumiReWeighting(puFile, puFile, "Flat20to50/pileup", "PU50/pileup")
 
        self.histos = {}
        self.histoDenoms = {}
        for w in self.newlumiWeighters:
            name = "L1SingleJet_"+w
            binL = 49.5
            binH = 101.5
            nbins = binH - binL
            self.histos[name] = ROOT.TH1D(name, name, int(nbins), binL, binH)
            self.histos[name].Sumw2()
            self.GetOutputList().Add(self.histos[name])
            nameDenom = name+"Denom"
            self.histoDenoms[nameDenom] = ROOT.TH1D(nameDenom, nameDenom, 1, -0.5, 0.5)
            self.GetOutputList().Add(self.histoDenoms[nameDenom])


    def fillRate(self, hist, maxThr, weight):
        nbins = hist.GetNbinsX()
        getBinCenter = hist.GetXaxis().GetBinCenter
        for i in xrange(1,nbins+1):
            binCenter = getBinCenter(i)
            if binCenter <= int(maxThr):
                hist.Fill(binCenter, weight)
            else:
                break

    def analyze(self):
        hardestL1 = -1
        for i in xrange(self.fChain.L1Jets.size()):
            jetI = self.fChain.L1Jets.at(i)
            ptI = jetI.pt()
            if hardestL1 < ptI:
                hardestL1 = ptI
        pu = self.fChain.PUNumInteractions
        #print hardestL1, int(hardestL1)
        for w in self.newlumiWeighters:
            weight = self.newlumiWeighters[w].weight(pu)
            self.fillRate(self.histos["L1SingleJet_"+w], hardestL1, weight)
            self.histoDenoms["L1SingleJet_"+w+"Denom"].Fill(0, weight)

    def finalize(self):
        #print "Finalize:"
        #normFactor = self.getNormalizationFactor()
        pass

    def finalizeWhenMerged(self):
        olist =  self.GetOutputList()
        histos = {}
        for o in olist:
            if not "TH1" in o.ClassName(): continue
            histos[o.GetName()]=o

        lhcFreq = 4E7 # 40 MHz
        totalBunches = 3564.
        #  (usually 2662 for 25ns bunch spacing, 1331 for 50ns bunch spacing) 
        filledBunches = 2662.

        factor = float(lhcFreq)*filledBunches/totalBunches
        for h in histos:
            if "Denom" in h: continue
            #raise "HERE"
            # ptint XXXXX
            denom = histos[h+"Denom"].GetBinContent(1)
            #print "DDD", denom
            histos[h].Scale(factor/denom)

if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    ROOT.gSystem.Load("libFWCoreFWLite.so")
    AutoLibraryLoader.enable()

    sampleList = None # run through all
    maxFilesMC = None
    nWorkers = None

    # '''
    maxFilesMC = 1
    nWorkers = 1
    # '''
    #maxFilesMC = 32

    slaveParams = {}

    # select hltCollection here (see plugins/MNTriggerAna.cc to learn whats avaliable):

    # note - remove maxFiles parameter in order to run on all files
    L1Rate.runAll(treeName="L1JetsRateAna",
                               #slaveParameters=slaveParams,
                               #sampleList=sampleList,
                               maxFilesMC = maxFilesMC,
                               nWorkers=nWorkers,
                               outFile = "L1RatePlots.root" )
                                
