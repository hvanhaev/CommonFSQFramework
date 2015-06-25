#!/usr/bin/env python
import sys, os
from optparse import OptionParser

template='''#!/usr/bin/env python
import CommonFSQFramework.Core.ExampleProofReader

# import all your getters here
from  CommonFSQFramework.Core.GenParticlesGetter import GenParticlesGetter

import sys, os, time
sys.path.append(os.path.dirname(__file__))

import ROOT
ROOT.gROOT.SetBatch(True)
from ROOT import edm

from array import *

class XXXXX(CommonFSQFramework.Core.ExampleProofReader.ExampleProofReader):

    def init( self):

        # define all your histograms
        self.hist = {}
        self.hist["numGenParticles"] =  ROOT.TH1F("numGenParticles",   "numGenParticles",  100, -0.5, 99.5)
	
	# define and initialize your getters
	self.genparts = GenParticlesGetter("genParticles")
        
	# add error treatment and add histograms to output
	for h in self.hist:
            self.hist[h].Sumw2()
            self.GetOutputList().Add(self.hist[h])

    def analyze(self):
        weight = 1
	
	# fetch all info with the getters for this event
	self.genparts.newEvent(self.fChain)
	
	# start making your histograms here...
	
	# fill gen histos
        numgen = 0
        for genpart in self.genparts.get():
            genpartp4 = genpart.p4 # get fourvector
            if genpartp4.pt() > 1.0:
                numgen+=1
                #self.hist["etaGenParticles"].Fill(genpartp4.eta(), weight)
                #self.hist["phiGenParticles"].Fill(genpartp4.phi(), weight)
                #self.hist["ptGenParticles"].Fill(genpartp4.pt(), weight)
                #self.hist["pdgIDGenParticles"].Fill(genpart.pdg, weight)

        self.hist["numGenParticles"].Fill(numgen, weight)
        
	
        #print self.maxEta # see slaveParams below
	
	
        return 1

    # this function will be executed after all events are processed, on each worker node separately
    def finalize(self):
        print "Finalize:"
        normFactor = self.getNormalizationFactor()
        print "  applying norm", normFactor
        for h in self.hist:
            self.hist[h].Scale(normFactor)
	   
    # this function will be executed after all events are processed, and after the results of all workers are merged/added
    # use it to e.g. correct mean values in histograms etc. for the number of workers that you used	   
    def finalizeWhenMerged(self):
        print "Final calculations after merging workers..."	   
	   

if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    ROOT.gSystem.Load("libFWCoreFWLite.so")
    ROOT.AutoLibraryLoader.enable()

    sampleList = None # run through all samples in the dictionary
    maxFilesMC = None # run through all files found
    maxFilesData = None # same but for data samples
    maxNevents = -1 # run on all events, change this to some positive value to restrict the number of events you want to process
    nWorkers = None # Use all cpu cores

    # debug/test config:
    # Run printTTree.py alone to get the samples list
    #sampleList = []
    #sampleList.append("MinBias_TuneMonash13_13TeV-pythia8")
    #maxFilesMC = 1
    #maxFilesData = 1
    #maxNevents = 5000
    #nWorkers = 1


    slaveParams = {}
    slaveParams["maxEta"] = 2.


    # use printTTree.py <sampleName> to see what trees are avaliable inside the skim file
    XXXXX.runAll(treeName="GenLevelTree",
           slaveParameters=slaveParams,
           sampleList=sampleList,
           maxFilesMC = maxFilesMC,
           maxFilesData = maxFilesData,
	   maxNevents = maxNevents,
           nWorkers=nWorkers,
           outFile = "plotsXXXXX.root" )
'''


if __name__ == "__main__":
    parser = OptionParser(usage="usage: %prog [options] filename",
                            version="%prog 1.0")

    parser.add_option("-s", "--sample", action="store", type="string", dest="sample" )
    #parser.add_option("-d", "--dataOnly", action="store", type="bool", dest="dataOnly" )
    (options, args) = parser.parse_args()
    if len(args)==0:
        print "Usage: NewProofAnalizer.py AnalizerName"
        sys.exit()

    name=args[0]
    fname = name+".py"
    if os.path.isfile(fname):
        print "Analizer with name " + name + " allready exists ("+fname+")"
        sys.exit()

    with open(fname, "w") as f:
        f.write(template.replace("XXXXX",name))

    os.system("chmod +x " + fname)

    print ""
    print "A skeleton python+proof analizer file was created (" + fname  + ")"
    print ""
    print "Now You need to decide on what tree it will run:"
    print "  - to list trees in current skim run: printTTrees aSampleName"
    print "  - to list avaliable sample names run: printTTrees.py"
    print ""
    print "Please also consider keeping your analyzer in your git repository. It's simple:"
    print ""
    print "git add "+fname
    print "git commit", fname, '-m "My commit message"'
    print ""













