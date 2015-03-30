#!/usr/bin/env python

import ROOT
ROOT.gROOT.SetBatch(True)
from ROOT import *

import os,re,sys,math
import MNTriggerStudies.MNTriggerAna.Style

from optparse import OptionParser
def main():
    MNTriggerStudies.MNTriggerAna.Style.setStyle()
    parser = OptionParser()
    (options, args) = parser.parse_args()
    if len(args) == 0:
        print "Provide threshold"
        sys.exit(0)


    thr = int(args[0])
    infile = "RecoSignalVsHLTEfficiency_"+str(thr)+".root"

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


    todo = []
    for f in finalMap:
        name = f.replace("_nom","").replace("_denom","")
        if name not in todo:
            todo.append(name)

    c1 = ROOT.TCanvas()
    for t in todo:
        fname = "~/tmp/"+str(thr)+"_"+t+".png"
        nom = finalMap[t + "_nom"]
        denom = finalMap[t + "_denom"]

        nom.Divide(denom)
        nom.GetXaxis().SetTitle("trigger threshold [GeV]")
        nom.GetYaxis().SetTitle("signal efficiency")
        nom.Draw()
        nom.SetMaximum(1.03)
        nom.SetMinimum(0)
        nom.GetYaxis().SetTitleOffset(2)
        c1.Print(fname)


if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    ROOT.gSystem.Load("libFWCoreFWLite.so")
    AutoLibraryLoader.enable()
    main()
