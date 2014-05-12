#!/usr/bin/env python


import sys, os, time
sys.path.append(os.path.dirname(__file__))

import ROOT
ROOT.gROOT.SetBatch(True)
from ROOT import *

from array import *

# please note that python selector class name (here: DerivedProofReader) 
# should be consistent with this file name (DerivedProofReader.py)

# note2: current limitation is that the derived class (DerivedProofReader) must 
#        be run from the same dir as ExampleProofReader

from ExampleProofReader import ExampleProofReader

class DerivedProofReader(ExampleProofReader):
    def configureAnalyzer( self):
        print "configureAnalyzer - DerivedProofReader"
        self.hist = {}

        self.hist["ptLeadHisto"] =  ROOT.TH1F("ptLead",   "ptLead",  100, 0, 100)
        # 2d histograms also supported
        self.hist["dummy2d"] =  ROOT.TH2F("dummy2d",   "dummy2d",  100, 0, 100, 100, 0, 100)

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
        leadJetPtFromVectorBranch = 0
        # once again we will exploit the fact, that jets should be pt ordered
        if pfJetsMomenta.size() > 0: # note: here we are accessing size method from c++ std::vector. You can use any method..
            leadJetPtFromVectorBranch = pfJetsMomenta.at(0).pt()

        if leadJetPtFromVectorBranch > 30:
           self.hist["ptLeadHisto"].Fill( leadJetPtFromVectorBranch, weight)

        return 1


if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    ROOT.gSystem.Load("libFWCoreFWLite.so")
    AutoLibraryLoader.enable()

    # same as the label of EDProducer that was used to produce the trees
    DerivedProofReader.runAll(treeName="exampleTree", outFile = "~/tmp/plots2.root", maxFiles = 10)
