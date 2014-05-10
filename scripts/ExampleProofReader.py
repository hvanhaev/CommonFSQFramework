#!/usr/bin/env python

from MNTriggerStudies.MNTriggerAna.GetDatasetInfo import getTreeFilesAndNormalizations
###############################################################################
#
#  TODO: 
#   1. Select output root file when calling runAll
#   2. Same for datasets
#   4. Fetch generator weight, create histos with sumw
#
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
    def getVariables(self):
        self.dsName = ROOT.gSystem.Getenv("TMFDatasetName")

    def Begin( self ):
        print 'py: beginning'
        self.getVariables()

    def SlaveBegin( self, tree ):
        print 'py: slave beginning'
        self.getVariables()

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

        if leadJetPtFromVectorBranch > 0:
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

        outFile = ROOT.TFile("~/tmp/plots.root", "UPDATE") # TODO - take dir name from Central file

        outDir = outFile.mkdir(self.dsName)
        outDir.cd()

        # TODO save in a directory mathcing the hlt collection name
        for o in olist:
            o.Write()


    #@staticmethod
    @classmethod
    def runAll(cls, treeName):
        cwd = os.getcwd()+"/"
        treeFilesAndNormalizations = getTreeFilesAndNormalizations()

        #todo = ["QCD_Pt-30to50_Tune4C_13TeV_pythia8"] # devel on one ds
        #todo.append("QCD_Pt-10to15_Tune4C_13TeV_pythia8")
        todo = treeFilesAndNormalizations.keys() # run them all

        # ret[s]["files"] = fileList
        # ret[s]["normFactor"] = normFactor

        outFile = "~/tmp/plots.root" # note: duplicated defintion above...
        of = ROOT.TFile(outFile,"RECREATE")
        if not of:
            print "Cannot create outfile:", outFile
            sys.exit()
        of.Close() # so we dont mess with file opens during proof ana
        

        skipped = []
        for t in todo:
            if len(treeFilesAndNormalizations[t]["files"])==0:
                print "Skipping, empty filelist for",t
                skipped.append(t)
                continue

            dataset = TDSet( 'TTree', 'data', treeName) # the last name is the directory name inside the root file
            for file in treeFilesAndNormalizations[t]["files"]:
                dataset.Add( 'root://'+file)
            

            TProof.AddEnvVar("PATH2",ROOT.gSystem.Getenv("PYTHONPATH")+":"+os.getcwd())

            ROOT.gSystem.Setenv("TMFDatasetName", t)

            proof = TProof.Open('')
            #proof = TProof.Open('workers=1')
            proof.Exec( 'gSystem->Setenv("PYTHONPATH",gSystem->Getenv("PATH2"));') # for some reason cannot use method below for python path
            proof.Exec( 'gSystem->Setenv("PATH", "'+ROOT.gSystem.Getenv("PATH") + '");')
            #print dataset.Process( 'TPySelector', 'ExampleProofReader')
            print "Running:", cls.__name__
            print dataset.Process( 'TPySelector', cls.__name__)


        if len(skipped)>0:
            print "Note: following samples were skipped:"
            for sk in skipped:
                print "  ",sk

        print "Writing normalization constants: "
        of = ROOT.TFile(outFile,"UPDATE")
        for t in set(todo)-set(skipped):
            saveDir = of.Get(t)
            if not saveDir:
                print "Cannot get directory from plot file"
                continue
            saveDir.cd()
            norm = treeFilesAndNormalizations[t]["normFactor"]
            print "  ",t, norm
            hist = ROOT.TH1D("norm", "norm", 1,0,1)
            hist.SetBinContent(1, norm)
            hist.Write()

if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    ROOT.gSystem.Load("libFWCoreFWLite.so")
    AutoLibraryLoader.enable()
    ExampleProofReader.runAll(treeName="exampleTree")
