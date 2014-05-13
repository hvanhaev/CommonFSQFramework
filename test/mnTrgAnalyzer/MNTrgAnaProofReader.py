#!/usr/bin/env python


import sys, os, time
sys.path.append(os.path.dirname(__file__))

import ROOT
ROOT.gROOT.SetBatch(True)
from ROOT import *

from array import *

# please note that python selector class name (here: MNTrgAnaProofReader) 
# should be consistent with this file name (MNTrgAnaProofReader.py)

# you have to run this file from directory where it is saved

from MNTriggerStudies.MNTriggerAna.ExampleProofReader import ExampleProofReader

class MNTrgAnaProofReader(ExampleProofReader):
    #def SlaveBegin( self, tree ):
    def configureAnalyzer(self):
        print 'configure: MNTrgAnaProofReader'
        self.hist = {}

        self.hist["signalEffVsHLTThreshold_NOM"] = ROOT.TH1F("signalEffVsHLTThreshold_NOM",   "signalEffVsHLTThreshold_NOM",  50, -0.5, 49.5)
        self.hist["signalEffVsHLTThreshold_DENOM"] = ROOT.TH1F("signalEffVsHLTThreshold_DENOM",   "signalEffVsHLTThreshold_DENOM",  50, -0.5, 49.5)
        self.hist["signalEffVsL1Threshold_NOM"] = ROOT.TH1F("signalEffVsL1Threshold_NOM",   "signalEffVsL1Threshold_NOM",  50, -0.5, 49.5)
        self.hist["signalEffVsL1Threshold_DENOM"] = ROOT.TH1F("signalEffVsL1Threshold_DENOM",   "signalEffVsL1Threshold_DENOM",  50, -0.5, 49.5)

        for h in self.hist:
            self.hist[h].Sumw2()
            self.GetOutputList().Add(self.hist[h])

        sys.stdout.flush()

    def analyze(self):
        #event = self.fChain.event
        #run = self.fChain.run
        #lumi = self.fChain.lumi
        #print event

        weight = 1. # calculate your event weight here

        pfJetsMomenta = self.fChain.pfJets

        #          (bkwd, fordward)
        bestPair = [None,None]

        for i in xrange(pfJetsMomenta.size()):
            if pfJetsMomenta.at(i).pt() < self.recoJetPtThreshold: continue

            eta = pfJetsMomenta.at(i).eta()
            if bestPair[0] == None or bestPair[0].eta() > eta:
                bestPair[0] = pfJetsMomenta.at(i)
            elif bestPair[1] == None or bestPair[1].eta() < eta:
                bestPair[1] = pfJetsMomenta.at(i)

        if bestPair[1] == None or bestPair[0] == None:
            return 1

        self.doThresholdAna(2,2) # HLT, threshold ana - requiering two jets
        self.doThresholdAna(1,1) # L1, threshold ana - one L1 jet required

        return 1

    def doThresholdAna(self, level, minObjects):
        ''' level=1 - L1, level=2 - HLT '''
        # at this point we got a signal event. Go through avaliable HLT jets
        # and find two with the highest PT
        # TODO  : recoJet2HLTjet matching
        # TODO2 : hltJet2l1Jet matching
        HLTpts = []

        if level == 2:
            hltJets = self.fChain.hltJets
        elif level == 1:
            hltJets = self.fChain.l1Jets
        else:
            raise Exception("level should be equal to 1 or 2")


        for i in xrange(hltJets.size()):
            pt = hltJets.at(i).pt()
            HLTpts.append(pt)

        lowestPTNeededForAcceptForThisEvent = 0 # if it stays 0 - less than two HLT jets present in the event
        if len(HLTpts)>= minObjects:
            lowestPTNeededForAcceptForThisEvent = sorted(HLTpts, reverse=True)[minObjects-1]


        # We found two HLT jets with pt at least equall to lowestPTNeededForAcceptForThisEvent
        # any double jet HLT path requireing pt higher than lowestPTNeededForAcceptForThisEvent
        # would not fire

        if level == 2:
            nom = self.hist["signalEffVsHLTThreshold_NOM"]
            denom = self.hist["signalEffVsHLTThreshold_DENOM"]
        elif level == 1:
            nom = self.hist["signalEffVsL1Threshold_NOM"]
            denom = self.hist["signalEffVsL1Threshold_DENOM"]


        nbins = denom.GetNbinsX()
        getBinCenter = denom.GetXaxis().GetBinCenter
        for i in xrange(1,nbins+1):
            denom.Fill(i)
            if getBinCenter(i) < lowestPTNeededForAcceptForThisEvent:
                nom.Fill(i)
        del getBinCenter


if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    ROOT.gSystem.Load("libFWCoreFWLite.so")
    AutoLibraryLoader.enable()

    sampleList = None # run through all
    #sampleList = ["QCD_Pt-30to50_Tune4C_13TeV_pythia8",]
    #MNTrgAnaProofReader.runAll(treeName="mnTriggerAna", sampleList=sampleList)


    slaveParams = {}
    slaveParams["recoJetPtThreshold"] = 35
        

    MNTrgAnaProofReader.runAll(treeName="mnTriggerAna", outFile = "~/plotsHLT.root", 
                                slaveParameters=slaveParams,
                                maxFiles = 10)
