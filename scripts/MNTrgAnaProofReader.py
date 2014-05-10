#!/usr/bin/env python


import sys, os, time
sys.path.append(os.path.dirname(__file__))

import ROOT
ROOT.gROOT.SetBatch(True)
from ROOT import *

from array import *

# please note that python selector class name (here: MNTrgAnaProofReader) 
# should be consistent with this file name (MNTrgAnaProofReader.py)

# note2: current limitation is that the derived class (MNTrgAnaProofReader) must 
#        be run from the same dir as ExampleProofReader

from ExampleProofReader import ExampleProofReader

class MNTrgAnaProofReader(ExampleProofReader):
    def SlaveBegin( self, tree ):
        print 'py: slave beginning: MNTrgAnaProofReader'
        self.getVariables()
        self.signalEffVsHLTThreshold_NOM = ROOT.TH1F("signalEffVsHLTThreshold_NOM",   "signalEffVsHLTThreshold_NOM",  50, -0.5, 49.5)
        self.signalEffVsHLTThreshold_DENOM = ROOT.TH1F("signalEffVsHLTThreshold_DENOM",   "signalEffVsHLTThreshold_DENOM",  50, -0.5, 49.5)
        self.GetOutputList().Add(self.signalEffVsHLTThreshold_NOM)
        self.GetOutputList().Add(self.signalEffVsHLTThreshold_DENOM)
        sys.stdout.flush()

    def Process( self, entry ):
        if self.fChain.GetEntry( entry ) <= 0:
           return 0

        recoJetPtThreshold = 35
        #event = self.fChain.event
        #run = self.fChain.run
        #lumi = self.fChain.lumi
        #print event

        weight = 1. # calculate your event weight here

        pfJetsMomenta = self.fChain.pfJets

        #          (bkwd, fordward)
        bestPair = [None,None]

        for i in xrange(pfJetsMomenta.size()):
            if pfJetsMomenta.at(i).pt() < recoJetPtThreshold: continue

            eta = pfJetsMomenta.at(i).eta()
            if bestPair[0] == None or bestPair[0].eta() > eta:
                bestPair[0] = pfJetsMomenta.at(i)
            elif bestPair[1] == None or bestPair[1].eta() < eta:
                bestPair[1] = pfJetsMomenta.at(i)

        if bestPair[1] == None or bestPair[0] == None:
            return 1

        # at this point we got a signal event. Go through avaliable HLT jets
        # and find two with the highest PT
        # TODO  : recoJet2HLTjet matching
        # TODO2 : hltJet2l1Jet matching
        HLTpts = []
        hltJets = self.fChain.hltJets
        for i in xrange(hltJets.size()):
            pt = hltJets.at(i).pt()
            HLTpts.append(pt)

        lowestPTNeededForAcceptForThisEvent = 0 # if it stays 0 - less than two HLT jets present in the event
        if len(HLTpts)>1:
            lowestPTNeededForAcceptForThisEvent = sorted(HLTpts, reverse=True)[1]


        #print "XXX", lowestPTNeededForAcceptForThisEvent
        # We found two HLT jets with pt at least equall to lowestPTNeededForAcceptForThisEvent
        # any double jet HLT path requireing pt higher than lowestPTNeededForAcceptForThisEvent
        # would not fire

        nbins = self.signalEffVsHLTThreshold_DENOM.GetNbinsX()
        getBinCenter = self.signalEffVsHLTThreshold_DENOM.GetXaxis().GetBinCenter
        for i in xrange(1,nbins+1):
            self.signalEffVsHLTThreshold_DENOM.Fill(i)
            #if histAxis.GetBinCenter(i) < lowestPTNeededForAcceptForThisEvent:
            if getBinCenter(i) < lowestPTNeededForAcceptForThisEvent:
                self.signalEffVsHLTThreshold_NOM.Fill(i)
        del getBinCenter

        #l1Jets = self.fChain.l1Jets
        return 1

if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    ROOT.gSystem.Load("libFWCoreFWLite.so")
    AutoLibraryLoader.enable()

    sampleList = None # run through all
    #sampleList = ["QCD_Pt-30to50_Tune4C_13TeV_pythia8",]
    MNTrgAnaProofReader.runAll(treeName="mnTriggerAna", sampleList=sampleList)
