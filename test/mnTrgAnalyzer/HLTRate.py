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
    #def SlaveBegin( self, tree ):
    def init(self):
        print 'configure: HLTRate'
        self.lastEv  = 0
        self.lastRun = 0

        getter = BaseTrigger.TriggerObjectsGetter(self.fChain, self.hltCollection)
        self.fbTrigger = BaseTrigger.ForwardBackwardTrigger(getter)

        self.hist = {}

        n = "fb_rate"
        self.hist[n] = ROOT.TH1F(n, n, 30, -0.5, 29.5)

        n = "singleJet_rate"
        self.hist[n] = ROOT.TH1F(n, n, 100, 299.5, 399.5)

        n = "ptAveHFJEC_rate"
        self.hist[n] = ROOT.TH1F(n, n, 25, 14.5, 39.5)

        n = "test_rate"
        self.hist[n] = ROOT.TH1F(n, n, 100, 299.5, 399.5)

        '''
        todo = ["singleJet",
                "fb"
               ]


        for t1 in todo:
                t = t1+"_rate"
                self.hist[t] = ROOT.TH1F(t, t, 30, -0.5, 29.5)
                self.hist[t].Sumw2()
                self.GetOutputList().Add(self.hist[t])
        '''
        for t in self.hist:
            self.hist[t].Sumw2()
            self.GetOutputList().Add(self.hist[t])


        sys.stdout.flush()

    def cacheTriggerObjects(self):
        newEvent = False
        event = self.fChain.event
        run = self.fChain.run
        if event != self.lastEv:
            newEvent = True
        elif run != self.lastRun:
            newEvent = True

        if newEvent: # cache best trigger objects
            self.lastRun =  run
            self.lastEv = event

            self.allL1 = [] # Currently all L1 jets not depending on eta
            self.allHLT = [] # Currently all HLT jets not depending on eta

            todo = {}
            todo["l1"] = self.fChain.l1Jets
            todo["hlt"] =  getattr(self.fChain, self.hltCollection)
            for t in todo:
                cur = []
                for jet in todo[t]:
                    if jet.pt()>15:
                        cur.append(jet)

                if t == "l1":
                    self.allL1 = sorted(cur, reverse = True, key = lambda j: j.pt())
                else:
                    self.allHLT  = sorted(cur, reverse = True, key = lambda j: j.pt())

    def ptAveHFJEC(self):
        #ptAveHFJEC_rate
        tag = None
        probe = None
        for j in self.allHLT:
            eta = abs(j.eta())
            tagCand = eta < 1.4
            probeCand = eta > 2.8 and eta < 5.2
            if probeCand or tagCand:
                pt = j.pt()
                if probeCand and (probe == None or probe < pt): probe = pt
                if tagCand and (tag == None or tag < pt): tag = pt

        if None in [tag, probe]:
            return 0.
        return  (tag+probe)/2


    
    def fillRate(self, hist, maxThr):
        #rateVsPtThreshold = self.hist["singleJet_rate"]
        nbins = hist.GetNbinsX()
        getBinCenter = hist.GetXaxis().GetBinCenter
        fill = hist.Fill
        for i in xrange(1,nbins+1):
            binCenter = getBinCenter(i)
            if binCenter <= maxThr:
                fill(binCenter)
                #print hist.GetName(), maxThr, binCenter
            else:
                break

        del fill
        del getBinCenter


    def analyze(self):
        #event = self.fChain.event
        #run = self.fChain.run
        #lumi = self.fChain.lumi
        #print event

        weight = 1. # calculate your event weight here

        # for xcheck purposes 
        self.cacheTriggerObjects()

        if len(self.allHLT) > 0:
            #print "----"
            #for tt in self.allHLT:
            #    print tt.pt()
            
            hardest = self.allHLT[0].pt()
            rateVsPtThreshold = self.hist["test_rate"]
            nbins = rateVsPtThreshold.GetNbinsX()
            getBinCenter = rateVsPtThreshold.GetXaxis().GetBinCenter
            fill = rateVsPtThreshold.Fill
            for i in xrange(1,nbins+1):
                binCenter = getBinCenter(i)
                if binCenter <= hardest:
                    #print "  fl!", i, rateVsPtThreshold.GetXaxis().GetBinCenter(i)
                    fill(binCenter)
                else:
                    break
            del fill
            del getBinCenter




        hardest = 0
        if len(self.allHLT) > 0:
            hardest = self.allHLT[0].pt()
        if hardest > 0.5:
            self.fillRate(self.hist["singleJet_rate"], hardest )

        ptAveMaxThr = self.ptAveHFJEC()
        #print ptAveMaxThr
        if ptAveMaxThr > 0.5:
            self.fillRate(self.hist["ptAveHFJEC_rate"], ptAveMaxThr )

        ttt= self.fbTrigger.getMaxThr()
        if ttt > 0.5:
            self.fillRate(self.hist["fb_rate"], ttt )            
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

    #'''
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
                                
