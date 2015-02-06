#!/usr/bin/env python

import ROOT
ROOT.gROOT.SetBatch(True)
#ROOT.gSystem.Load("libRooFit.so" ) # for bindFunction
#https://root.cern.ch/root/htmldoc/tutorials/roofit/rf105_funcbinding.C.html

import os,sys, math
from array import array

import MNTriggerStudies.MNTriggerAna.Util

from  RooDSHelper import getSummedRooDS, reweighDS

# I hate myself...
hData = ROOT.TH1F("dataa", "dataa", 100, 0, 100)
hMCbase = hData.Clone()
globalMC = None

def doMinuitFit(ofile, dsData, dsMC, lumi):
    c = ROOT.TCanvas()
    hData.Reset()
    dsData[0].fillHistogram(hData, ROOT.RooArgList(dsData[1]["leadPt"]))
    hData.Scale(1./lumi)
    global globalMC
    globalMC = dsMC

    # setup minuit
    gMinuit = ROOT.TMinuit(5)
    gMinuit.SetFCN( fcn )

    arglist = array( 'd', 10*[0.] )
    ierflg = ROOT.Long(1982)

    arglist[0] = 1
    gMinuit.mnexcm( "SET ERR", arglist, 1, ierflg )

    # Set starting values and step sizes for parameters
    vstart = array( 'd', ( 1,  0) )
    step   = array( 'd', ( 0.01, 0.01 ) )
    gMinuit.mnparm( 0, "a1", vstart[0], step[0], 0, 0, ierflg )
    gMinuit.mnparm( 1, "a2", vstart[1], step[1], 0, 0, ierflg )

    # Now ready for minimization step
    arglist[0] = 500 # max calls 
    arglist[1] = 1.  # tolerance - how far from minimum
    gMinuit.mnexcm( "MIGRAD", arglist, 2, ierflg )

    # Print results
    amin, edm, errdef = ROOT.Double(0.18), ROOT.Double(0.19), ROOT.Double(0.20)
    nvpar, nparx, icstat = ROOT.Long(1983), ROOT.Long(1984), ROOT.Long(1985)
    gMinuit.mnstat( amin, edm, errdef, nvpar, nparx, icstat )

cnt = 0

def fcn( npar, gin, f, par, iflag ):
    global cnt
    cnt +=1
    # get weighted MC ds
    global globalMC
    vars = globalMC[1]
    #localMCds = globalMC[0].Clone()
    baseWeight = "weight" # yuck, Q&D
    a1 = ROOT.RooRealVar("a1","a1", par[0])
    a2 = ROOT.RooRealVar("a2","a2", par[1])
    args = ROOT.RooArgList(vars["qScale"], a1, a2)
    linear = ROOT.RooFormulaVar("lin", "lin", "a1+a2*qScale", args)

    newweight = ROOT.RooFormulaVar("w"+str(cnt), "ww", baseWeight+"*lin"  , ROOT.RooArgList(vars[baseWeight], linear))
    wds = reweighDS(globalMC[0], "neww", newweight)


    # fill MC histograms
    hMC = hMCbase.Clone("MC")
    wds.fillHistogram(hMC, ROOT.RooArgList(vars["leadPt"]))

    # get chi2
    chisq, delta = 0., 0.
    for i in xrange(1, hMC.GetNbinsX()+1):
        errData = hData.GetBinError(i)
        errMC =   hMC.GetBinError(i)
        err = math.sqrt(errData*errData+errMC*errMC)
        if err > 0:
            delta = (hData.GetBinContent(i)-hMC.GetBinError(i))/err
            chisq += delta*delta
        
    f[0] = chisq
    print "Call:", cnt, par[0], par[1], "chisq", chisq





def doBaselineFit(ofile, dsData, dsMC, lumi):
    c = ROOT.TCanvas()
    hData.Reset()
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

    #todoQCDNames = ["QCD_Pt-15to3000_TuneZ2star_Flat_HFshowerLibrary_7TeV_pythia6", "QCD_Pt-15to1000_TuneEE3C_Flat_7TeV_herwigpp"]
    todoQCDNames = ["QCD_Pt-15to1000_TuneEE3C_Flat_7TeV_herwigpp",]
    #todoQCDNames = ["QCD_Pt-15to3000_TuneZ2star_Flat_HFshowerLibrary_7TeV_pythia6"]

    outFile = ROOT.TFile("ptHatWeighters.root", "recreate")
    for t in todoQCDNames:
        xxx = outFile.mkdir(t)
        dMC = getSummedRooDS(t, "treesForPTHatReweighing.root", [t], "weight")

        #doBaselineFit(xxx, data, dMC, lumi)
        doMinuitFit(xxx, data, dMC, lumi)

#       leadEta
#       leadPt
#       qScale








if __name__ == "__main__":
    main()
