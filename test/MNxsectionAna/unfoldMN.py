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


def getHistos(infile):
    f = ROOT.TFile(infile, "r")
    lst = f.GetListOfKeys()

    finalMap = {}
    targetsToSamples = {}


    for l in lst:
        currentDir = l.ReadObj()
        if not currentDir:
            print "Problem reading", l.GetName(), " - skipping"
            continue
        if type(currentDir) != ROOT.TDirectoryFile:
            print "Expected TDirectoryFile,", type(currentDir), "found"
            continue

        target =  l.GetName()#.replace("_j15", "_jet15")
        dirContents = currentDir.GetListOfKeys()
        for c in dirContents:
            curObj = c.ReadObj()
            curObjName = curObj.GetName()
            clsname = curObj.ClassName()
            if not clsname.startswith("TH") and not curObjName.startswith("response_"): 
                #print "Skip: ", curObj.GetName(), clsname, target
                continue

            #print "Found", curObj.GetName(), target
            curObjClone = curObj.Clone()
            if clsname.startswith("TH"):
                curObjClone.SetDirectory(0)
            finalMap.setdefault(target, {})
            targetsToSamples.setdefault(target, set()) # keep empty
            if curObjClone.GetName() in finalMap[target]:
                finalMap[target][curObjClone.GetName()].Add(curObjClone)
            else:
                finalMap[target][curObjClone.GetName()] = curObjClone
    return finalMap

def getPossibleActions():
    return set(["pythiaOnData", "herwigOnData", "pythiaOnHerwig", "herwigOnPythia"])

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
        categories["_jet15"] = ["QCD_Pt-15to1000_TuneEE3C_Flat_7TeV_herwigpp"]
        categories["_dj15fb"] = ["QCD_Pt-15to1000_TuneEE3C_Flat_7TeV_herwigpp"]
    elif action ==  "herwigOnPythia":
        baseMC = "QCD_Pt-15to1000_TuneEE3C_Flat_7TeV_herwigpp"
        "QCD_Pt-15to3000_TuneZ2star_Flat_HFshowerLibrary_7TeV_pythia6"
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

    for c in categories:
        odir = of.mkdir(c)

        centralHistoName = "xs_central"+c # in fact we should not find any other histogram in data than "central"
        histo = None
        for ds in categories[c]:
            h = histos[ds][centralHistoName]
            if not histo:
                histo = h.Clone()
                histo.SetDirectory(0)
            else:
                histo.Add(h)

        rawName = "xs_central"+c
        odir.WriteTObject(histo,rawName)
        for r in knownResponses:
            if c not in r: continue # do not apply dj15fb to jet15 and viceversa
            variation = r.split("_")[1]
            # Doing:  _dj15fb response_central_dj15fb central

            print "Doing: ", c, r, variation
            rawName = "xsunfolded_" + variation+ c
            sys.stdout.flush()

            print type(histos[baseMC][r])
            unfold = ROOT.RooUnfoldBayes(histos[baseMC][r], histo, 4)
            hReco= unfold.Hreco()
            odir.WriteTObject(hReco, rawName)
            # unfold= RooUnfoldSvd (histos[r], histo, 20)
            # unfold= RooUnfoldTUnfold (histos[r], histo)

        # 1 create central histogram

    # centralResponsesFromPythia =  filter(lambda x: x.startswith("response_"), histos["QCD_Pt-15to1000_XXX_pythiap"].keys())
    # rename central to pythia, add to responsesVariations


def main():
    possibleActions = getPossibleActions()
    for action in possibleActions:
        unfold(action)


if __name__ == "__main__":
    main()

