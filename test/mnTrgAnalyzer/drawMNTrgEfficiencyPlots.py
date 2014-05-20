#!/usr/bin/env python

import ROOT
ROOT.gROOT.SetBatch(True)
from ROOT import *

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



    todoEff  = { "HLT": "signalEffVsHLTThreshold",
                  "L1": "signalEffVsL1Threshold",
                 "L1_bothForward":   "signalEffVsL1Threshold_bothForward",
                 "HLT_bothForward":   "signalEffVsHLTThreshold_bothForward",
                 "HLT_atLeastOneNonForward":"signalEffVsHLTThreshold_atLeastOneNonForward",
                 "L1_atLeastOneNonForward": "signalEffVsL1Threshold_atLeastOneNonForward",
                 "HLTrateSinglePF": "signalEffVsHLTThreshold_SinglePFJet"

                }


    totalBunches = 3564
    collidingBunches = 2*1380 # take the highest value from 2012, mul x2 (50ns - > 25 ns)
    avgPU = 25
    #minBiasXS = 78.42 * 1E9 # pb
    #minBiasXS = 69.3 * 1E9 # pb // 8 TeV
    minBiasXS = 68. * 1E9 # pb // 7 TeV

    perBunchXSLumi = avgPU/minBiasXS # in pb-1
    print "per bunch lumi", perBunchXSLumi, "(pb^-1)"
    LHCFrequency = 40. * 1E6 # 40 MHz

    rateScaleFactor = perBunchXSLumi*LHCFrequency*float(collidingBunches)/float(totalBunches)


    print "Inst lumi", rateScaleFactor, "(pb^-1 * s^-1)"


    c1 = ROOT.TCanvas()
    for t in todoEff:
        fname = "~/"+t+".png"
        #nom = f.Get(todo[t][0])
        #denom = f.Get(todo[t][1])
        nom = finalMap[todoEff[t] + "_NOM"]
        denom = finalMap[todoEff[t] + "_DENOM"]

        nom.Divide(denom)
        nom.GetXaxis().SetTitle("trigger threshold [GeV]")
        nom.GetYaxis().SetTitle("signal efficiency")
        nom.Draw()
        c1.Print(fname)

        rate = finalMap[todoEff[t] + "_rate"]
        fname = "~/"+t+"_rate.png"
        rate.Scale(rateScaleFactor)

        rate.Draw()
        #rate.GetXaxis().SetRange(15, 50)
        rate.GetXaxis().SetTitle("trigger threshold [GeV]")
        rate.GetYaxis().SetTitle("rate  [Hz]")
        

        c1.Print(fname)


if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    ROOT.gSystem.Load("libFWCoreFWLite.so")
    AutoLibraryLoader.enable()
    main()
