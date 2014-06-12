#!/usr/bin/env python


import sys, os, time
sys.path.append(os.path.dirname(__file__))

import ROOT
ROOT.gROOT.SetBatch(True)
from ROOT import *

from array import *

# please note that python selector class name (here: DerivedProofReader) 
# should be consistent with this file name (DerivedProofReader.py)

# you have to run this file from directory where it is saved


from MNTriggerStudies.MNTriggerAna.ExampleProofReader import ExampleProofReader

class DerivedProofReader(ExampleProofReader):
    def init( self):
        print "init - DerivedProofReader"
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



    @classmethod
    def testAll(cls):
        # same as the label of EDProducer that was used to produce the trees
        #todo = [400, 100, 25, 8, 2]
        todo =[1,6,25,100,400]
        #todo = [8]
        for t in todo:
            oname = "~/tmp/plots_"+str(t)+".root"
            onameMerged = "~/tmp/plotsMerged_"+str(t)+".root"
            #pr = DerivedProofReader()
            #pr.runAll(treeName="exampleTree", outFile = oname, maxFiles = t)
            #DerivedProofReader.DerivedProofReader().runAll(treeName="exampleTree", outFile = oname, maxFiles = t)
            cls.runAll(treeName="exampleTree", outFile = oname, maxFiles = t)
            os.system("../../scripts/normalizeAndAddHistograms.py -i "+oname + " -o " + onameMerged)

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
    DerivedProofReader.testAll()

