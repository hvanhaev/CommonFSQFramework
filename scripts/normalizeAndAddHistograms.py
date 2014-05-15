#!/usr/bin/env python

import ROOT
ROOT.gROOT.SetBatch(True)
from ROOT import *

import os,re,sys,math
from optparse import OptionParser

def main():
    parser = OptionParser(usage="usage: %prog [options] filename",
                            version="%prog 1.0")

    parser.add_option("-i", "--inputFile", action="store", type="string", dest="infile")
    parser.add_option("-o", "--outputFile", action="store", type="string", dest="ofile")
    (options, args) = parser.parse_args()

    f = ROOT.TFile(options.infile, "r")
    lst = f.GetListOfKeys()

    finalMap = {}
    for l in lst:
        #print "Going through", l.GetName(), l.ClassName()
        currentDir = l.ReadObj()

        if not currentDir: 
            print "Problem reading", l.GetName(), " - skipping"
            continue

        if type(currentDir) != ROOT.TDirectoryFile:
            print "Expected TDirectoryFile,", type(currentDir), "found"
            continue

        norm = currentDir.Get("norm")
        if not norm:
           raise Exception("Cannot read norm for "+l.GetName())

        normFactor = norm.GetBinContent(1)

        dirContents = currentDir.GetListOfKeys()
        for c in dirContents:
            if "PROOF_" in c.GetName(): continue
            if "norm" == c.GetName(): continue # already done

            curObj = c.ReadObj()
            if not curObj.InheritsFrom("TH1"):
                print "Dont know how to scale and merge", curObj.GetName(), curObj.ClassName()

            curObjClone = curObj.Clone()
            curObjClone.SetDirectory(0)
            #curObjClone.Scale(normFactor)

            if curObjClone.GetName() in finalMap:
                finalMap[curObjClone.GetName()].Add(curObjClone)
            else:        
                finalMap[curObjClone.GetName()] = curObjClone

    f.Close()

    f= ROOT.TFile(options.ofile, "RECREATE")
    for o in finalMap:
        finalMap[o].Write()

if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    ROOT.gSystem.Load("libFWCoreFWLite.so")
    AutoLibraryLoader.enable()
    main()
