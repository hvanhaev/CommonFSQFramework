#!/usr/bin/env python

import ROOT
ROOT.gROOT.SetBatch(True)
from ROOT import *

import os,re,sys,math

import MNTriggerStudies.MNTriggerAna.Util

from array import array



def getUncertaintyBand(histos, hCentral):
    if len(histos) == 0:
        raise Exception("Empty histogram list")
    nbins = hCentral.GetNbinsX()
    for h in histos:
        if h.GetNbinsX() != nbins:
            raise Exception("Different number of bins - "+ h.GetName())

    x = array('d')
    xZeros = array('d')

    y =  array('d')
    yUp = array('d')
    yDown = array('d')
    for i in xrange(1, nbins+1):
        x.append(histos[0].GetBinCenter(i))

        centralValue = hCentral.GetBinContent(i)
        yUpLocal  = 0.
        yDownLocal  = 0.
        for h in histos:
            valLocal = h.GetBinContent(i)
            delta = centralValue - valLocal
            if delta > 0:
                yUpLocal += delta*delta
            else:
                yDownLocal += delta*delta


        xZeros.append(0)

        y.append(centralValue)
        yUp.append(sqrt(yUpLocal))
        yDown.append(sqrt(yDownLocal))


    ret = ROOT.TGraphAsymmErrors(len(x), x, y, xZeros, xZeros, yDown, yUp)
    ret.SetFillStyle(3001);
    #    graphBand.Draw("3") 

    return ret




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
    #triggersToSamples["jet15"] = ["JetMETTau-Run2010A-Apr21ReReco-v1"]
    #triggersToSamples["jet15"]=     [ "JetMET-Run2010A-Apr21ReReco-v1"]
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

    #for d in finalMap["data"]: 
    variations = set()
    triggers = set()
    histos = set()
    for d in finalMap["MC"]: 
        spl = d.split("_")
        if len(spl)!=3:
            print "Skipping: ", d

        trg = spl[2]
        variation = spl[1]
        histname = spl[0]
        variations.add(variation)
        triggers.add(trg)
        histos.add(histname)

    c1 = ROOT.TCanvas()
    for h in histos:
        for t in triggers:
            centralName = h+"_central_" +t

            maxima = []
            hData =  finalMap["data"][centralName]
            hMCCentral = finalMap["MC"][centralName]
            maxima.append(hData.GetMaximum())
            maxima.append(hMCCentral.GetMaximum())

            uncHistos = []
            for v in variations:
                uncHistos.append(finalMap["MC"][h+"_"+v+"_"+t])
                maxima.append(finalMap["MC"][h+"_"+v+"_"+t].GetMaximum())

            unc = getUncertaintyBand(uncHistos, hMCCentral)
            maxima.append(unc.GetMaximum())


            maximum = max(maxima)*1.05
            unc.SetMaximum(maximum)
            hData.SetMaximum(maximum)
            hMCCentral.SetMaximum(maximum)
            hMCCentral.SetMarkerColor(4)
            hMCCentral.SetMarkerSize(2)
            hMCCentral.SetLineColor(4)


            unc.SetFillColor(8);
            hData.Draw()
            unc.Draw("3SAME")
            hMCCentral.Draw("SAME")

            c1.Print("~/tmp/"+centralName+".png")



            
        
        

        #print d



                




if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    ROOT.gSystem.Load("libFWCoreFWLite.so")
    AutoLibraryLoader.enable()
    main()
