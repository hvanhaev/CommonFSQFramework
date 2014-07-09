#!/usr/bin/env python
import sys, os
from optparse import OptionParser

template='''#!/usr/bin/env python
import MNTriggerStudies.MNTriggerAna.ExampleProofReader

import sys, os, time
sys.path.append(os.path.dirname(__file__))

import ROOT
ROOT.gROOT.SetBatch(True)
from ROOT import edm

from array import *

class XXXXX(MNTriggerStudies.MNTriggerAna.ExampleProofReader.ExampleProofReader):
    def init( self):

        self.hist = {}
        self.hist["numGenTracks"] =  ROOT.TH1F("numGenTracks",   "numGenTracks",  100, -0.5, 99.5)
        for h in self.hist:
            self.hist[h].Sumw2()
            self.GetOutputList().Add(self.hist[h])

    def analyze(self):
        weight = 1
        num = 0
        # genTracks
        #num = self.fChain.genTracks.size()
        #print num
        #print self.maxEta # see slaveParams below
        self.hist["numGenTracks"].Fill(num, weight)
        return 1

    def finalize(self):
        print "Finalize:"
        normFactor = self.getNormalizationFactor()
        print "  applying norm", normFactor
        for h in self.hist:
            self.hist[h].Scale(normFactor)

if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    ROOT.gSystem.Load("libFWCoreFWLite.so")
    ROOT.AutoLibraryLoader.enable()

    sampleList = None # run through all
    maxFilesMC = None # run through all ffiles found
    maxFilesData = None # same
    nWorkers = None # Use all cpu cores

    # debug config:
    # Run printTTree.py alone to get the samples list
    #sampleList = []
    #sampleList.append("QCD_Pt-15to3000_TuneZ2star_Flat_HFshowerLibrary_7TeV_pythia6")
    #maxFilesMC = 1
    #maxFilesData = 1
    #maxFilesData = 1
    #nWorkers = 1


    slaveParams = {}
    slaveParams["maxEta"] = 2.


    # use printTTree.py <sampleName> to see what trees are avaliable inside the skim file
    XXXXX.runAll(treeName="tracksTree",
           slaveParameters=slaveParams,
           sampleList=sampleList,
           maxFilesMC = maxFilesMC,
           maxFilesData = maxFilesData,
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













