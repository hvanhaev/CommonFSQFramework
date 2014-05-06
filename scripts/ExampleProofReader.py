#!/usr/bin/env python

###############################################################################
#
# Example proof reader of trees produced with framework. This script reads
#  trees produced by ExampleTreeProducer. During execution pt of the leading
#  jet is read in two ways - from float tree branch (leadJetPt) and by using
#  collection of all jets momenta saved in pfJets branch.
#
#  Two histograms are produced - distribution of pt of leading jet and ratio
#   of pt obtained from both methods
#
#   TODO: automagic normalization
#
#
#   Additional notes:
#
#     1. change "workers" parameter to run on more cores
#     2. This script needs to be called from a directory where it is placed, 
#        (that is by typing ExampleProofReader.py). You can use symbolic 
#        link to overcome this
#     3.  Histos will be saved in ~/tmp/plots.root (this is currently 
#         hardcoded, change if needed)
#     4. You can see proof execution logs under  
#
#           ~/.proof/<long string coresponding to your directory name>/last-lite-session/worker-0.0.log
#
#         Your print statements will go there. 
#
#     5. Debugging proof analyzer (ie this analyzer) is often difficult, since
#        you dont see err messages (not even in file above). Often the only 
#        way is to comment/uncomment suspected parts of code and see if crash
#        persists
#       
#     6. Often problems are caused by having a bare return statement (without a 
#        value) in Process function. You should always return 1 (0 value is 
#        is used once, see below and dont touch :) )
#
#
###############################################################################

import sys, os, time
sys.path.append(os.path.dirname(__file__))

import ROOT
ROOT.gROOT.SetBatch(True)
from ROOT import *

from array import *

# please note that python selector class name (here: ExampleProofReader) 
# should be consistent with this file name (ExampleProofReader.py)
from ROOT import TPySelector
class ExampleProofReader( TPySelector ):
    def Begin( self ):
        print 'py: beginning'

    def SlaveBegin( self, tree ):
        print 'py: slave beginning'

        self.coarseBinning = False
        self.fbTrigger = False

        self.histograms = {}
        self.ptLeadHisto = ROOT.TH1F("ptLead",   "ptLead",  100, 0, 100)      
        self.ptRatioHisto = ROOT.TH1F("ptRatio", "ptRatio", 100, -0.0001, 10)      
        self.GetOutputList().Add(self.ptLeadHisto)
        self.GetOutputList().Add(self.ptRatioHisto)
        sys.stdout.flush()
    
    def Process( self, entry ):
        if self.fChain.GetEntry( entry ) <= 0:
           return 0
        #event = self.fChain.event
        #run = self.fChain.run
        #lumi = self.fChain.lumi
        #print event

        weight = 1. # calculate your event weight here

        leadJetPtFromFloatBranch = self.fChain.leadJetPt

        pfJetsMomenta = self.fChain.pfJets
        leadJetPtFromVectorBranch = 0
        # once again we will exploit the fact, that jets should be pt ordered
        if pfJetsMomenta.size() > 0: # note: here we are accessing size method from c++ std::vector. You can use any method..
            leadJetPtFromVectorBranch = pfJetsMomenta.at(0).pt()

        if leadJetPtFromVectorBranch != 0 and leadJetPtFromFloatBranch !=0:
            ratio = leadJetPtFromVectorBranch/leadJetPtFromFloatBranch
            self.ptRatioHisto.Fill(ratio, weight)
        elif leadJetPtFromVectorBranch != leadJetPtFromFloatBranch:
            self.ptRatioHisto.Fill(0, weight)

        #for j in pfJetsMomenta: # iterate over all jets:
        #    print j.pt()
        #print "XX",leadJetPtFromFloatBranch, leadJetPtFromVectorBranch

        self.ptLeadHisto.Fill( leadJetPtFromVectorBranch, weight)
        return 1

    def SlaveTerminate( self ):
       print 'py: slave terminating'

    def Terminate( self ): # executed once on client

        print 'py: terminating'
        c1 = ROOT.TCanvas("ccc")
        h1 = self.GetOutputList().FindObject("test")
        #h1.Draw()
        #c1.Print("~/tmp/ddd.png")
        olist =  self.GetOutputList()
        ending = ""
        outFile = ROOT.TFile("~/tmp/plots.root", "RECREATE") # TODO - take dir name from Central file

        # TODO save in a directory mathcing the hlt collection name
        for o in olist:
            o.Write()




if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    ROOT.gSystem.Load("libFWCoreFWLite.so")
    AutoLibraryLoader.enable()

    cwd = os.getcwd()+"/"


    dataset = TDSet( 'TTree', 'data', 'treeProd1') # the last name is the directory name inside the root file
    # TODO automatic file picking from ds
    dataset.Add( 'root://'+os.getcwd()+'/trees.root')
        

    TProof.AddEnvVar("PATH2",ROOT.gSystem.Getenv("PYTHONPATH")+":"+os.getcwd())

    proof = TProof.Open('workers=1')
    proof.Exec( 'gSystem->Setenv("PYTHONPATH",gSystem->Getenv("PATH2"));') # for some reason cannot use method below for python path
    proof.Exec( 'gSystem->Setenv("PATH", "'+ROOT.gSystem.Getenv("PATH") + '");')
    print dataset.Process( 'TPySelector', 'ExampleProofReader')

