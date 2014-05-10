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
    def SlaveBegin( self, tree ):
        print 'py: slave beginning: DerivedProofReader'
        self.getVariables()
        self.ptLeadHisto = ROOT.TH1F("ptLead",   "ptLead",  100, 0, 100)
        self.GetOutputList().Add(self.ptLeadHisto)
        sys.stdout.flush()

    def Process( self, entry ):
        if self.fChain.GetEntry( entry ) <= 0:
           return 0
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
           self.ptLeadHisto.Fill( leadJetPtFromVectorBranch, weight)

        return 1


if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    ROOT.gSystem.Load("libFWCoreFWLite.so")
    AutoLibraryLoader.enable()

    DerivedProofReader.runAll(treeName="exampleTree")
