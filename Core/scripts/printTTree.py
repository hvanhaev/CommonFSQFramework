#!/usr/bin/env python

import sys
import ROOT
ROOT.gROOT.SetBatch(True)

import os,re
from optparse import OptionParser

from MNTriggerStudies.MNTriggerAna.GetDatasetInfo import getTreeFilesAndNormalizations
from MNTriggerStudies.MNTriggerAna.Util import getAnaDefinition


def main():



    parser = OptionParser()
    #parser.add_option("-s", "--sample",   action="store", type="string", dest="sample", help="sample name" )
    #parser.add_option("-l", "--listSamples",   action="store", type="string", dest="list", help="listAllSamples" )
    (options, args) = parser.parse_args()

    anaDef = getAnaDefinition("sam")
    directlyFromRootfile = False
    if len(args) != 1 or (not args[0].endswith(".root") and args[0] not in anaDef):
            print "Usage: printTTree.py sampleName"
            print " - or -"
            print "Usage: printTTree.py rootfile"
            print "Avaliable samples:"
            for t in anaDef:
                print " ", t
            sys.exit(0)

    if args[0].endswith(".root"):
        print "Will print structure of given file"
        directlyFromRootfile = True

    if not directlyFromRootfile:
        sample= args[0]
        treeFilesAndNormalizations = getTreeFilesAndNormalizations(maxFilesMC=1, maxFilesData=1,
                    quiet = True, samplesToProcess=[sample,])

        if not treeFilesAndNormalizations[sample]["files"]:
            print "No files found for sample", sample, "- exiting"
            sys.exit(0)

        filename = treeFilesAndNormalizations[sample]["files"][0]
    else:
        filename = args[0]

    
    rootfile = ROOT.TFile.Open(filename, "read")

    todo = [(rootfile, 0), ]
    for t in todo:
        indent = t[1]
        print " "*indent, t[0].GetName()
        lst = t[0].GetListOfKeys()
        for l in lst:
            #print l.GetName()
            #continue

            #print "Going through", l.GetName(), l.ClassName()
            current = l.ReadObj()
            #current = rootfile.Get(l.GetName())
            if not current: continue
            if "TDirectory" in current.ClassName():
                todo.append( (current, indent+2) )
            else:
                print " "*(indent+2), current.GetName(), current.GetTitle(), "/"+current.ClassName()+"/"
                #print " "*(indent+2), current.GetTitle(), "/"+current.ClassName()+"/"

            if current.ClassName() == "TTree":
                branches =  current.GetListOfBranches()
                branchesNames = []
                for b in branches:
                    branchesNames.append(b.GetName())

                for b in sorted(branchesNames):
                    print " "*(indent+4), b
            #print l.GetName()

    






from ROOT import *
import ROOT
if __name__ == "__main__":

    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    ROOT.gSystem.Load("libFWCoreFWLite.so")
    AutoLibraryLoader.enable()
    main()

