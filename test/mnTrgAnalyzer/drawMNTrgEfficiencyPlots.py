#!/usr/bin/env python

from ROOT import *
import ROOT
ROOT.gROOT.SetBatch(True)

import os,re,sys,math

def main():

    infile = "~/plotsHLT.root"
    f = ROOT.TFile(infile, "r")
    lst = f.GetListOfKeys()

    # merge histograms across directories
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

        dirContents = currentDir.GetListOfKeys()
        for c in dirContents:
            if "PROOF_" in c.GetName(): continue
            if "norm" == c.GetName(): continue # not needed since we expect to get normalized histos


            curObj = c.ReadObj()
            if not curObj.InheritsFrom("TH1"):
                print "Dont know how to merge", curObj.GetName(), curObj.ClassName()
                continue


            if "isNormalized"  == c.GetName(): 
                val = curObj.GetBinContent(1)
                if val < 0.5:
                    errMsg = "Expected to find normalized histograms in dir " + l.GetName()
                    raise Exception(errMsg)
                continue



            curObjClone = curObj.Clone()
            curObjClone.SetDirectory(0)

            if curObjClone.GetName() in finalMap:
                finalMap[curObjClone.GetName()].Add(curObjClone)
            else:
                finalMap[curObjClone.GetName()] = curObjClone





    todo = {}
    todo["L1"] = ["signalEffVsL1Threshold_NOM","signalEffVsL1Threshold_DENOM"]
    todo["HLT"] = ["signalEffVsHLTThreshold_NOM","signalEffVsHLTThreshold_DENOM"]
    c1 = ROOT.TCanvas()
    for t in todo:
        fname = "~/"+t+".png"
        #nom = f.Get(todo[t][0])
        #denom = f.Get(todo[t][1])
        nom = finalMap[todo[t][0]]
        denom = finalMap[todo[t][1]]

        nom.Divide(denom)
        nom.Draw()
        c1.Print(fname)


if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    ROOT.gSystem.Load("libFWCoreFWLite.so")
    AutoLibraryLoader.enable()
    main()
