#!/usr/bin/env python

import ROOT
ROOT.gROOT.SetBatch(True)
from ROOT import *

import os,re,sys,math

import MNTriggerStudies.MNTriggerAna.Util
import MNTriggerStudies.MNTriggerAna.Style

from array import array

from optparse import OptionParser

ROOT.gSystem.Load("libRooUnfold.so")
from HistosHelper import getHistos


from mnDraw import DrawMNPlots 

alaGri = True

def getPossibleActions():
    return set(["pythiaOnData", "herwigOnData", "pythiaOnHerwig", "herwigOnPythia", "herwigOnHerwig", "pythiaOnPythia"])

def unfold(action):
    possibleActions = getPossibleActions()
    if action not in possibleActions:
        print "Action", action, "not known. Possible actions "+ " ".join(possibleActions)
        return

    categories = {}
    if action == "herwigOnData":
        baseMC = "QCD_Pt-15to1000_TuneEE3C_Flat_7TeV_herwigpp"
        categories["_jet15"] = ["Jet-Run2010B-Apr21ReReco-v1", "JetMETTau-Run2010A-Apr21ReReco-v1", "JetMET-Run2010A-Apr21ReReco-v1"]
        categories["_dj15fb"] = ["METFwd-Run2010B-Apr21ReReco-v1", "JetMETTau-Run2010A-Apr21ReReco-v1", "JetMET-Run2010A-Apr21ReReco-v1"]
    elif action == "pythiaOnData":
        baseMC = "QCD_Pt-15to3000_TuneZ2star_Flat_HFshowerLibrary_7TeV_pythia6"
        categories["_jet15"] = ["Jet-Run2010B-Apr21ReReco-v1", "JetMETTau-Run2010A-Apr21ReReco-v1", "JetMET-Run2010A-Apr21ReReco-v1"]
        categories["_dj15fb"] = ["METFwd-Run2010B-Apr21ReReco-v1", "JetMETTau-Run2010A-Apr21ReReco-v1", "JetMET-Run2010A-Apr21ReReco-v1"]
    elif action ==  "pythiaOnHerwig":
        baseMC = "QCD_Pt-15to3000_TuneZ2star_Flat_HFshowerLibrary_7TeV_pythia6"
        otherMC =  "QCD_Pt-15to1000_TuneEE3C_Flat_7TeV_herwigpp"
        categories["_jet15"] = ["QCD_Pt-15to1000_TuneEE3C_Flat_7TeV_herwigpp"]
        categories["_dj15fb"] = ["QCD_Pt-15to1000_TuneEE3C_Flat_7TeV_herwigpp"]
    elif action ==  "herwigOnPythia":
        baseMC = "QCD_Pt-15to1000_TuneEE3C_Flat_7TeV_herwigpp"
        otherMC = "QCD_Pt-15to3000_TuneZ2star_Flat_HFshowerLibrary_7TeV_pythia6"
        categories["_jet15"] = ["QCD_Pt-15to3000_TuneZ2star_Flat_HFshowerLibrary_7TeV_pythia6"]
        categories["_dj15fb"] = ["QCD_Pt-15to3000_TuneZ2star_Flat_HFshowerLibrary_7TeV_pythia6"]
    elif action ==  "herwigOnHerwig":
        baseMC = "QCD_Pt-15to1000_TuneEE3C_Flat_7TeV_herwigpp"
        otherMC =  "QCD_Pt-15to1000_TuneEE3C_Flat_7TeV_herwigpp"
        categories["_jet15"] = ["QCD_Pt-15to1000_TuneEE3C_Flat_7TeV_herwigpp"]
        categories["_dj15fb"] = ["QCD_Pt-15to1000_TuneEE3C_Flat_7TeV_herwigpp"]
    elif action ==  "pythiaOnPythia":
        baseMC = "QCD_Pt-15to3000_TuneZ2star_Flat_HFshowerLibrary_7TeV_pythia6"
        otherMC = "QCD_Pt-15to3000_TuneZ2star_Flat_HFshowerLibrary_7TeV_pythia6"
        categories["_jet15"] = ["QCD_Pt-15to3000_TuneZ2star_Flat_HFshowerLibrary_7TeV_pythia6"]
        categories["_dj15fb"] = ["QCD_Pt-15to3000_TuneZ2star_Flat_HFshowerLibrary_7TeV_pythia6"]

    


    histos = getHistos("plotsMNxs.root")
    #print histos.keys()
    #print histos["JetMET-Run2010A-Apr21ReReco-v1"].keys()

    knownResponses = set(filter(lambda x: x.startswith("response_"), histos[baseMC].keys()))
    #print histos[baseMC].keys()

    #responsesCentral = set(filter(lambda x: "_central_" in x, knownResponses))
    #responsesVariations = knownResponses-responsesCentral

    # _dj15fb', 
    #'response_jecDown_jet15

    of =  ROOT.TFile("~/tmp/mnxsHistos_unfolded_"+action+".root","RECREATE")

    # Warning: duplicated code for lumi calculation! See mnDraw.py
    triggerToKey = {}
    triggerToKey["_jet15"] = "lumiJet15"
    triggerToKey["_dj15fb"] = "lumiDiJet15FB"

    for c in categories:
        odir = of.mkdir(c)

        centralHistoName = "xs_central"+c # in fact we should not find any other histogram in data than "central"
        histo = None

        sampleList=MNTriggerStudies.MNTriggerAna.Util.getAnaDefinition("sam")
        lumi = 0.
        for ds in categories[c]:
            h = histos[ds][centralHistoName]
            if not histo:
                histo = h.Clone()
                histo.SetDirectory(0)
            else:
                histo.Add(h)

            if "Data" in action: # 
                lumiKeyName = triggerToKey[c]
                lumi += sampleList[ds][lumiKeyName]


        if "Data" in action:
            histo.Scale(1./lumi)

        print "Lumi", c, action, lumi
        rawName = "xs_central"+c

        odir.WriteTObject(histo,rawName)
        for r in knownResponses:
            if c not in r: continue # do not apply dj15fb to jet15 and viceversa
            variation = r.split("_")[1]
            # Doing:  _dj15fb response_central_dj15fb central

            print "Doing: ", c, r, variation
            rawName = "xsunfolded_" + variation+ c
            sys.stdout.flush()

            if alaGri:
                acc = []
                print "Note: subs.bkg", r
                genXSHistName =  "xsGen"+r.replace("response","")
                genH = histos[baseMC][genXSHistName]
                missXSHistName =  "xsMiss"+r.replace("response","")
                missH = histos[baseMC][missXSHistName]
                fakeXSHistName =  "xsFake"+r.replace("response","")
                fakeXSHistMC = histos[baseMC][fakeXSHistName]  

                detHistName =  "xs"+r.replace("response","")
                detHistMC =     histos[baseMC][detHistName]  

                sizes = set( [histo.GetNbinsX(), fakeXSHistMC.GetNbinsX(), detHistMC.GetNbinsX(), genH.GetNbinsX(), missH.GetNbinsX() ])
                if len(sizes)!=1:
                    raise Exception("Different histogram sizes: " + " ".join(sizes) )

                for iBin in xrange(1, histo.GetNbinsX()+1):

                    valMC = detHistMC.GetBinContent(iBin)
                    valMCFake = fakeXSHistMC.GetBinContent(iBin)
                    valMCMiss = missH.GetBinContent(iBin)
                    valMCGen = genH.GetBinContent(iBin)
                    #'''
                    A = 1.
                    if valMCGen > 0:
                        A = 1. - valMCMiss/valMCGen
                    acc.append(A)
                    B = 0.
                    if valMC >0:
                        B =  valMCFake/valMC
                    

                    scaleingFactor = (1.-B)# /A
                    #print "XXX", A, B, scaleingFactor

                    valMeas = histo.GetBinContent(iBin)
                    histo.SetBinContent(iBin, scaleingFactor*valMeas)
                    #'''
                    #histo.SetBinContent(iBin, max(0, valMeas-valMCFake))


                


            if False: # second approach to alaGri
                # histos[baseMC][r] - response object
                # histo - detector level distribution
                #histo.Scale(0.5)
                responseWithBrokenFakesNorm = histos[baseMC][r]
                #   RooUnfoldResponse(const TH1* measured, const TH1* truth, const TH2* response
                meas  =  responseWithBrokenFakesNorm.Hmeasured().Clone()
                truth =  responseWithBrokenFakesNorm.Htruth().Clone()
                fake =  responseWithBrokenFakesNorm.Hfakes().Clone()
                fakeScaled =  responseWithBrokenFakesNorm.Hfakes().Clone()
                resp= responseWithBrokenFakesNorm.Hresponse().Clone()
                #scalingFactor = histo.Integral()/histos[baseMC][centralHistoName].Integral()
                scalingFactor = histo.Integral()/meas.Integral()

                # Note: simple call to h.Scale() is not enough
                def scale(h, s):
                    #h.Scale(s)
                    #return
                    for i in xrange(0, h.GetNbinsX()+1):
                        val = h.GetBinContent(i)*s
                        err = h.GetBinError(i)*s
                        h.SetBinContent(i, val)
                        h.SetBinError(i, err)

                def scale2d(h, s):
                    for i in xrange(0, h.GetNbinsX()+1):
                        for j in xrange(0, h.GetNbinsY()+1):
                            val = h.GetBinContent(i,j)*s
                            err = h.GetBinError(i, j)*s
                            h.SetBinContent(i, j, val)
                            h.SetBinError(i, j, err)

                for i in xrange(0, h.GetNbinsX()+1):
                    denom = meas.GetBinContent(i)
                    if denom == 0: continue
                    nom = fake.GetBinContent(i)
                    if nom > denom:
                        print "AAAA", nom, denom
                    factor = 1.-nom/denom
                    val = histo.GetBinContent(i)*factor
                    err = histo.GetBinError(i)*factor
                    histo.SetBinContent(i, val)
                    histo.SetBinError(i, err)


                #meas.Add(fake,-1)
                #print "AAAAA", r, fake.Integral()
                #scale(fakeScaled, scalingFactor)
                #histo.Add(fakeScaled, -1)
                #meas.Add(fakeScaled)
                #scale(meas, scalingFactor)
                #scale(truth, scalingFactor)
                #scale2d(resp, scalingFactor)
                meas.Reset()
                newResponseTmp = ROOT.RooUnfoldResponse(meas, truth, resp)

                measNew = newResponseTmp.Hfakes()
                scale(measNew, scalingFactor)
                scale(truth, scalingFactor)
                scale2d(resp, scalingFactor)
                newResponse = ROOT.RooUnfoldResponse(measNew, truth, resp)

                #newResponse = ROOT.RooUnfoldResponse(meas, truth, resp)
                #newResponse.Hfakes().Scale(0)
                #print "AAA",r, newResponse.Hfakes().Integral()

                '''
                # 
                newFakes = newResponse.Hfakes() 
                scalingFactor = histo.Integral()/meas.Integral()
                #scalingFactor = meas.Integral()/histo.Integral()
                newFakes.Scale(scalingFactor)
                deltaFakes = newFakes.Clone()
                deltaFakes.Add(responseWithBrokenFakesNorm.Hfakes(), -1)
                newMeas = newResponse.Hmeasured()
                newMeas.Add(deltaFakes, -1)
                '''

                #unfold = ROOT.RooUnfoldBayes(histos[baseMC][r], histo, 10)
                unfold = ROOT.RooUnfoldBayes(newResponse, histo, 10)

            unfold = ROOT.RooUnfoldBayes(histos[baseMC][r], histo, 10)
            hReco= unfold.Hreco()
            if hReco.GetNbinsX() != histo.GetNbinsX():
                raise Exception("Different histogram sizes after unfolding")

            '''
            if alaGri:
                for iBin in xrange(1, histo.GetNbinsX()+1):
                    if acc[iBin-1] == 0: continue
                    cont = hReco.GetBinContent(iBin)
                    hReco.SetBinContent(iBin, cont/acc[iBin-1])
            '''

                

            hReco.SetName(rawName)
            odir.WriteTObject(hReco, rawName)
            # unfold= RooUnfoldSvd (histos[r], histo, 20)
            # unfold= RooUnfoldTUnfold (histos[r], histo)

        # 1 create central histogram

    # centralResponsesFromPythia =  filter(lambda x: x.startswith("response_"), histos["QCD_Pt-15to1000_XXX_pythiap"].keys())
    # rename central to pythia, add to responsesVariations

def compareMCGentoMCUnfolded(action):
    if action == "herwigOnPythia" or action == "pythiaOnPythia":
        unfoldingWasDoneOn = "QCD_Pt-15to3000_TuneZ2star_Flat_HFshowerLibrary_7TeV_pythia6"
    elif action == "pythiaOnHerwig" or action == "herwigOnHerwig":
        unfoldingWasDoneOn = "QCD_Pt-15to1000_TuneEE3C_Flat_7TeV_herwigpp"
    else:
        print "compareMCGentoMCUnfolded: wrong action", action, "skipping (usually you can ignore this message)"
        return

    # detaGen_central_jet15
    fileWithUnfoldedPlotsName = "~/tmp/mnxsHistos_unfolded_"+action +".root"
    fileWithUnfoldedPlots = ROOT.TFile(fileWithUnfoldedPlotsName)


    #mnxsHistos_unfolded_pythiaOnHerwig.root
    histos = getHistos("plotsMNxs.root")
    #print histos[unfoldingWasDoneOn].keys()
    todo = ["_jet15", "_dj15fb"]
    #todo = ["_jet15"]

    c = ROOT.TCanvas()
    for t in todo:
        genHisto = histos[unfoldingWasDoneOn]["detaGen_central"+t]
        unfoldedHistoName = t+"/xsunfolded_central"+t
        unfoldedHisto = fileWithUnfoldedPlots.Get(unfoldedHistoName)
        #print unfoldedHistoName, type(unfoldedHisto), unfoldedHisto.ClassName()
        #genHisto.Scale(0.5)
        genHisto.Draw()
        genHisto.GetXaxis().SetTitle(DrawMNPlots.xLabels()["xs"])
        genHisto.GetYaxis().SetTitleOffset(1.8)
        genHisto.GetYaxis().SetTitle(DrawMNPlots.yLabels()["xsAsPB"])

        genHisto.SetMarkerColor(2)
        genHisto.SetLineColor(2)
        unfoldedHisto.Draw("SAME")
        trueMax = max(genHisto.GetMaximum(), unfoldedHisto.GetMaximum())
        genHisto.SetMaximum(trueMax*1.07)

        c.Print("~/tmp/MConMCunfoldingTest_"+action+t+".png")

def main():
    MNTriggerStudies.MNTriggerAna.Style.setTDRStyle()
    possibleActions = getPossibleActions()
    global alaGri
    alaGri = False

    possibleActions = ["pythiaOnPythia",  "herwigOnPythia", "pythiaOnHerwig", "herwigOnHerwig"]
    for action in possibleActions:
        unfold(action)
        compareMCGentoMCUnfolded(action)


if __name__ == "__main__":
    main()

