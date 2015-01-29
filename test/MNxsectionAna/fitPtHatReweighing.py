#!/usr/bin/env python

import ROOT
ROOT.gROOT.SetBatch(True)

import os,sys

import MNTriggerStudies.MNTriggerAna.Util

from  RooDSHelper import getSummedRooDS


def main():
    dataDSNames = ["JetMETTau-Run2010A-Apr21ReReco-v1", "Jet-Run2010B-Apr21ReReco-v1", "JetMET-Run2010A-Apr21ReReco-v1"]
    data = getSummedRooDS("data", "treesForPTHatReweighing.root", dataDSNames)
    lumi = 0.
    sampleList=MNTriggerStudies.MNTriggerAna.Util.getAnaDefinition("sam")
    for s in dataDSNames:
        lumi += sampleList[s]["lumiJet15"]

    todoQCDNames = ["QCD_Pt-15to3000_TuneZ2star_Flat_HFshowerLibrary_7TeV_pythia6", "QCD_Pt-15to1000_TuneEE3C_Flat_7TeV_herwigpp"]
    #todoQCDNames = ["QCD_Pt-15to1000_TuneEE3C_Flat_7TeV_herwigpp",]
    
    hData = ROOT.TH1F("dataa", "dataa", 100, 0, 100)
    hMC = hData.Clone()

    data[0].fillHistogram(hData, ROOT.RooArgList(data[1]["leadPt"]))
    hData.Scale(1./lumi)

    c = ROOT.TCanvas()
    outFile = ROOT.TFile("ptHatWeighters.root", "recreate")
    for t in todoQCDNames:

        xxx = outFile.mkdir(t)
        dMC = getSummedRooDS("t", "treesForPTHatReweighing.root", [t], "weight")
        dMC[0].fillHistogram(hMC, ROOT.RooArgList(dMC[1]["leadPt"]))
        hMC.Draw()
        hMC.SetLineColor(2)
        hData.Draw("SAME")
        c.Print("~/tmp/ttt.png")

        hData.Divide(hMC)

        fitF = ROOT.TF1("ptHatW","[0]*x + [1]", 0, 1000000);
        fitF.SetParameter(0, 0.)
        fitF.SetParameter(1, 1.)
        hData.Fit("ptHatW")

        xxx.WriteTObject(hData)
        xxx.WriteTObject(fitF)

#       leadEta
#       leadPt
#       qScale








if __name__ == "__main__":
    main()
