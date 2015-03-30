#!/usr/bin/env python

import ROOT
ROOT.gROOT.SetBatch(True)
from ROOT import *

import os,re,sys,math
import MNTriggerStudies.MNTriggerAna.Style

def main():
    MNTriggerStudies.MNTriggerAna.Style.setStyle()

    infile = "HLTRatePlots.root"
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



    # verification - single jet trigger for PU=25
    #   https://twiki.cern.ch/twiki/bin/view/CMS/TriggerMenuDevelopment#Rate_Studies
    #
    #  -> rate scale factor (equal to instantaneous luminosity) correctly calculated 
    #       (you need to set avgPU to 25)
    #       
    #  -> single jet rates (click JetHT) @ 13 TeV
    #
    #     HLT_PFJet320  97.77 pm 1.71 
    #     HLT_PFJet400  29.27 pm 0.07 
    #



    totalBunches = 3564
    collidingBunches = 1331 # the highest value from 2012
    #collidingBunches = 2*1380 # take the highest value from 2012, mul x2 (50ns - > 25 ns)
    avgPU = 10
    #avgPU = 1
    minBiasXS = 78.42 * 1E9 # pb
    #minBiasXS = 69.3 * 1E9 # pb // 8 TeV
    #minBiasXS = 68. * 1E9 # pb // 7 TeV

    perBunchXSLumi = avgPU/minBiasXS # in pb-1
    print "per bunch lumi", perBunchXSLumi, "(pb^-1)"
    LHCFrequency = 40. * 1E6 # 40 MHz

    rateScaleFactor = perBunchXSLumi*LHCFrequency*float(collidingBunches)/float(totalBunches)


    print "Inst lumi", rateScaleFactor, "(pb^-1 * s^-1)"

    doXSInsteadOfRate = True
    doXSInsteadOfRate = False



    c1 = ROOT.TCanvas()
    todo = [30, 60, 80, 100, 160, 220, 300]


    ofile = ROOT.TFile("~/tmp/rates/ptAveRate_PU"+str(avgPU)+".root", "recreate")
    res = {}
    for t in finalMap:
        rate = finalMap[t]
        fname = "~/tmp/rates/"+t+"_rate_PU"+str(avgPU) +".png"
        if not doXSInsteadOfRate:
            rate.Scale(rateScaleFactor)

        rate.Draw()
        rate.GetYaxis().SetTitleOffset(2)
        if "ptAveHFJEC" in t:
            rate.GetXaxis().SetTitle("p_{T}^{ave min HLT}")
        elif "test" in t or "singleJet" in t:
            rate.GetXaxis().SetTitle("threshold [GeV]")
            rate.GetXaxis().SetRangeUser(300, 400)
        else:
            rate.GetXaxis().SetTitle("threshold [GeV]")
            #rate.GetXaxis().SetRangeUser(15, 50)


        if doXSInsteadOfRate:
            rate.GetYaxis().SetTitle("xs  [pb-1]")  
        else:
            rate.GetYaxis().SetTitle("rate  [Hz]")
        
        xxx = t.split("Proper")[-1].split("_")
        low = int(xxx[0])
        high = int(xxx[1])
        for t in todo:
            if t >= low and t < high:
                bin = rate.FindBin(t)
                val = rate.GetBinContent(bin)
                #print "Rate:", t, val
                if t in res:
                    ratio = val/res[t]
                    if ratio < 0.98 or ratio > 1.02:
                       print "Warning: trg", t, ratio
                else:
                    res[t]=val
                
        ofile.WriteTObject(rate)

        c1.Print(fname)

    with open(os.environ["HOME"]+"/tmp/rates/rates_PU"+str(avgPU)+".txt", "w") as f:
        print >> f, "Rate table for PU", avgPU, "/ ptAve [GeV], rate [Hz]/"
        for t in sorted(res.keys()):
            print >> f, t, res[t]

    os.system("cp HLTRatePlots.root ~/tmp/rates/")

if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    ROOT.gSystem.Load("libFWCoreFWLite.so")
    AutoLibraryLoader.enable()
    main()
