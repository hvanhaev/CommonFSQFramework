#!/usr/bin/env python

import ROOT
ROOT.gROOT.SetBatch(True)
from ROOT import *

import os,re,sys,math

import MNTriggerStudies.MNTriggerAna.Util

def main():

    sampleList=MNTriggerStudies.MNTriggerAna.Util.getAnaDefinition("sam")

    infile = "~/plotsMNxs.root"

    f = ROOT.TFile(infile, "r")
    lst = f.GetListOfKeys()

    finalMap = {}
    finalMap["MC"] = {}
    finalMap["data"] = {}

    lumiMap = {}
    lumiMap["jet15"]   = 0.
    lumiMap["dj15fb"]  = 0.

    triggersToSamples = {}
    triggersToSamples["jet15"] = ["Jet-Run2010B-Apr21ReReco-v1", "JetMETTau-Run2010A-Apr21ReReco-v1", "JetMET-Run2010A-Apr21ReReco-v1"]
    triggersToSamples["dj15fb"] = ["METFwd-Run2010B-Apr21ReReco-v1", "JetMETTau-Run2010A-Apr21ReReco-v1", "JetMET-Run2010A-Apr21ReReco-v1"]
    #  QCD_Pt-15to3000_TuneZ2star_Flat_HFshowerLibrary_7TeV_pythia6

    triggerToKey = {}
    triggerToKey["jet15"] = "lumiJet15"
    triggerToKey["dj15fb"] = "lumiDiJet15FB"

    for l in lst:
        #print "Going through", l.GetName(), l.ClassName()
        currentDir = l.ReadObj()

        if not currentDir:
            print "Problem reading", l.GetName(), " - skipping"
            continue

        if type(currentDir) != ROOT.TDirectoryFile:
            print "Expected TDirectoryFile,", type(currentDir), "found"
            continue

        sampleName = l.GetName()
        if sampleName not in sampleList:
            raise Exception("Thats confusing...")

        isData = sampleList[sampleName]["isData"]

        print sampleName, isData
        if isData:
            for trg in triggersToSamples:
                if sampleName in triggersToSamples[trg]:
                    lumiKeyName = triggerToKey[trg]
                    lumiMap[trg] += sampleList[sampleName][lumiKeyName]


        dirContents = currentDir.GetListOfKeys()
        for c in dirContents:
            if "PROOF_" in c.GetName(): continue
            if "norm" == c.GetName(): continue # not needed since we expect to get normalized histos
            if "isNormalized" == c.GetName(): continue # not needed since we expect to get normalized histos


            curObj = c.ReadObj()
            if not curObj.InheritsFrom("TH1"):
                print "Dont know how to merge", curObj.GetName(), curObj.ClassName()
                continue

            if not isData:
                if "isNormalized"  == c.GetName(): 
                    val = curObj.GetBinContent(1)
                    if val < 0.5:
                        errMsg = "Expected to find normalized histograms in dir " + l.GetName()
                        raise Exception(errMsg)
                    continue

            curObjClone = curObj.Clone()
            curObjClone.SetDirectory(0)

            addThisHistogram = True
            if isData:
                target = "data"

                nameSplit = curObjClone.GetName().split("_")
                if len(nameSplit)<2:
                    raise Exception("Not able to extract trigger name :(")
                triggerNameFromThisHisto = nameSplit[-1]

                addThisHistogram = sampleName in triggersToSamples[triggerNameFromThisHisto]

                if not addThisHistogram:
                    print "Skipping sample", sampleName, "for histogram", curObjClone.GetName()

            else:
                target = "MC"

            if addThisHistogram:
                if curObjClone.GetName() in finalMap[target]:
                    finalMap[target][curObjClone.GetName()].Add(curObjClone)
                else:
                    finalMap[target][curObjClone.GetName()] = curObjClone

    #for histName in finalMap["data"]
    oName = "~/plotsMNxs_norm.root"
    fOut = ROOT.TFile(oName, "RECREATE")

    print lumiMap

    for histoType in finalMap: # data/MC
        for histoName in finalMap[histoType]:
            if histoType == "data": # divide by lumi
                nameSplit = finalMap[histoType][histoName].GetName().split("_")
                if len(nameSplit)<2:
                    raise Exception("Not able to extract trigger name :(")
                triggerNameFromThisHisto = nameSplit[-1]
                lumi = lumiMap[triggerNameFromThisHisto]
                scale = 1./lumi
                finalMap[histoType][histoName].Scale(scale)
            finalMap[histoType][histoName].Write(histoType+"_"+histoName)


                




if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    ROOT.gSystem.Load("libFWCoreFWLite.so")
    AutoLibraryLoader.enable()
    main()
