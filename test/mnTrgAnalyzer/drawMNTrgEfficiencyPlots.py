#!/usr/bin/env python

from ROOT import *
import ROOT
ROOT.gROOT.SetBatch(True)

import os,re,sys,math

def main():

    infile = "~/tmp/plotsMerged.root"
    f = ROOT.TFile(infile, "r")
    lst = f.GetListOfKeys()


    #for l in lst:
    #    print "Found", l.GetName()

    todo = {}
    todo["L1"] = ["signalEffVsL1Threshold_NOM","signalEffVsL1Threshold_DENOM"]
    todo["HLT"] = ["signalEffVsHLTThreshold_NOM","signalEffVsHLTThreshold_DENOM"]
    c1 = ROOT.TCanvas()
    for t in todo:
        fname = "~/tmp/"+t+".png"
        nom = f.Get(todo[t][0])
        denom = f.Get(todo[t][1])
        nom.Divide(denom)
        nom.Draw()
        c1.Print(fname)


if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    ROOT.gSystem.Load("libFWCoreFWLite.so")
    AutoLibraryLoader.enable()
    main()
