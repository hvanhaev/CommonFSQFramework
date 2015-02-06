#!/usr/bin/env python

import ROOT
ROOT.gROOT.SetBatch(True)

import os,sys

import MNTriggerStudies.MNTriggerAna.Util

from  RooDSHelper import getSummedRooDS

def doMinuitFit(ofile, data, mc):
    pass

def doBaselineFit(ofile, dsData, dsMC, lumi):
    c = ROOT.TCanvas()
    hData = ROOT.TH1F("dataa", "dataa", 100, 0, 100)
    hMCbase = hData.Clone()
    dsData[0].fillHistogram(hData, ROOT.RooArgList(dsData[1]["leadPt"]))
    hData.Scale(1./lumi)

    hMC = hMCbase.Clone("MC")
    dsMC[0].fillHistogram(hMC, ROOT.RooArgList(dsMC[1]["leadPt"]))
    hMC.Draw()
    hMC.SetLineColor(2)
    hData.Draw("SAME")
    c.Print("~/tmp/ttt.png")
    
    hData2MC = hData.Clone("data2mc")

    hData2MC.Divide(hMC)

    fitF = ROOT.TF1("ptHatW","[0]/x + [1]", 0, 1000000);
    fitF.SetParameter(0, 0.)
    fitF.SetParameter(1, 1.)
    hData2MC.Fit("ptHatW")

    ofile.WriteTObject(hData2MC)
    ofile.WriteTObject(hData)
    ofile.WriteTObject(hMC)
    ofile.WriteTObject(fitF)




def main():
    dataDSNames = ["JetMETTau-Run2010A-Apr21ReReco-v1", "Jet-Run2010B-Apr21ReReco-v1", "JetMET-Run2010A-Apr21ReReco-v1"]
    data = getSummedRooDS("data", "treesForPTHatReweighing.root", dataDSNames)
    lumi = 0.
    sampleList=MNTriggerStudies.MNTriggerAna.Util.getAnaDefinition("sam")
    for s in dataDSNames:
        lumi += sampleList[s]["lumiJet15"]

    print "Lumi:", lumi

    todoQCDNames = ["QCD_Pt-15to3000_TuneZ2star_Flat_HFshowerLibrary_7TeV_pythia6", "QCD_Pt-15to1000_TuneEE3C_Flat_7TeV_herwigpp"]
    #todoQCDNames = ["QCD_Pt-15to1000_TuneEE3C_Flat_7TeV_herwigpp",]
    #todoQCDNames = ["QCD_Pt-15to3000_TuneZ2star_Flat_HFshowerLibrary_7TeV_pythia6"]

    outFile = ROOT.TFile("ptHatWeighters.root", "recreate")
    for t in todoQCDNames:
        xxx = outFile.mkdir(t)
        dMC = getSummedRooDS(t, "treesForPTHatReweighing.root", [t], "weight")
        doBaselineFit(xxx, data, dMC, lumi)

#       leadEta
#       leadPt
#       qScale








if __name__ == "__main__":
    main()
