#!/usr/bin/env python

import ROOT
ROOT.gROOT.SetBatch(True)
from ROOT import *

import os,re,sys,math

import MNTriggerStudies.MNTriggerAna.Util
import MNTriggerStudies.MNTriggerAna.Style

from array import array


from optparse import OptionParser


class DrawPlots():
    def __init__(self):
        self.keep = [] # avoid garbage collection
        pass

    def getUncertaintyBand(self, histos, hCentral):
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

    def getLumi(self, target, samples): # override
        if "data_" not in target:
            raise Exception("getLumi called for "+ target )

        spl = target.split("_")
        if len(spl) < 1:
            raise Exception("Cannot extract trigger name from " + target)

        trg = spl[-1]
        triggersToSamples = {} # TODO make accessible from self
        triggersToSamples["jet15"] = ["Jet-Run2010B-Apr21ReReco-v1", "JetMETTau-Run2010A-Apr21ReReco-v1", "JetMET-Run2010A-Apr21ReReco-v1"]
        triggersToSamples["dj15fb"] = ["METFwd-Run2010B-Apr21ReReco-v1", "JetMETTau-Run2010A-Apr21ReReco-v1", "JetMET-Run2010A-Apr21ReReco-v1"]

        if trg not in triggersToSamples.keys():
            raise Exception("Dont know how to get lumi for "+ trg + ". Known triggers are " + " ".join(triggersToSamples.keys()))

        triggerToKey = {}
        triggerToKey["jet15"] = "lumiJet15"
        triggerToKey["dj15fb"] = "lumiDiJet15FB"

        sampleList=MNTriggerStudies.MNTriggerAna.Util.getAnaDefinition("sam")
        #print "-----"
        lumi = 0.
        for s in samples:
            #print s
            if s in triggersToSamples[trg]:
                lumiKeyName = triggerToKey[trg]
                lumi += sampleList[s][lumiKeyName]
                #print " lumi->",lumi

        return lumi



    def getTarget(self, histoName, sampleName): # override
        ''' target naming convention:
                - name should consist of two parts separated by underscore

                - part after underscore should contain your trigger label
                -- e.g. dj15fb (which for 2010 MN XS analysis coresponds to
                   HLT_DoubleJet15_ForwardBackward and HLT_DoubleJet15_ForwardBackward_v3)

                - part before underscore should start with string "data" or "MC"
                -- to distinguish different MC use descriptive names eg MCqcd or MCdymumu
        '''
        sampleList=MNTriggerStudies.MNTriggerAna.Util.getAnaDefinition("sam")

        trgSplt = histoName.split("_")
        if len(trgSplt) < 1:
            raise "Cannot extract trigger name from" , histoName
        triggerName =  trgSplt[-1]

        isData = sampleList[sampleName]["isData"]
        retName = None
        if not isData:
            retName = "MC_" + triggerName
        else:
            triggersToSamples = {} # TODO make accessible from self
            triggersToSamples["jet15"] = ["Jet-Run2010B-Apr21ReReco-v1", "JetMETTau-Run2010A-Apr21ReReco-v1", "JetMET-Run2010A-Apr21ReReco-v1"]
            triggersToSamples["dj15fb"] = ["METFwd-Run2010B-Apr21ReReco-v1", "JetMETTau-Run2010A-Apr21ReReco-v1", "JetMET-Run2010A-Apr21ReReco-v1"]
            if sampleName in triggersToSamples[triggerName]:
                retName = "data_" + triggerName

        return retName

    def applyScale(self, histoName, sampleName): # override
        if histoName.startswith("balance"): return False
        return True

    def setGlobalStyle(self):  # override
        MNTriggerStudies.MNTriggerAna.Style.setStyle()


    def decorate(self, canvas, dataHisto, MCStack, errBand): # override
        canvas.SetLogy()

        name = dataHisto.GetName()
        nspl = name.split("_")
        if len(nspl) > 0:
            dataHisto.GetXaxis().SetTitle(nspl[0])

        #MChistos = MCStack.GetHists()
        legend = ROOT.TLegend(0.3,0.95,1,1)
        legend.SetFillColor(0)
        legend.SetNColumns(3)
        legend.AddEntry(dataHisto, "data", "pel")



        MChistos = MCStack.GetStack()
        for h in MChistos:
            h.SetMarkerColor(4)
            h.SetMarkerSize(1)
            h.SetLineColor(4)
            h.SetMarkerStyle(22)
            h.Draw("SAME*P")
            legend.AddEntry(h, "MC", "pel")
            #print type(h.GetDrawOption())
            #h.SetOption("PE hist")
            #print h.GetDrawOption()
        
        legend.AddEntry(errBand, "MC unc", "f")

        dataHisto.SetMarkerSize(0.3)
        dataHisto.SetMarkerStyle(8)

        canvas.SetTopMargin(0.1)
        canvas.SetRightMargin(0.07)

        legend.Draw("SAME")
        self.keep.append(legend)

    def draw(self): # core function
        self.setGlobalStyle()
        sampleList=MNTriggerStudies.MNTriggerAna.Util.getAnaDefinition("sam")
        parser = OptionParser(usage="usage: %prog [options] filename",
                                version="%prog 1.0")

        parser.add_option("-i", "--infilee", action="store", type="string",  dest="infile" )
        parser.add_option("-o", "--outfile", action="store", type="string", dest="outfile")
        parser.add_option("-s", "--skipFinalMap", action="store_true", dest="skipFinalMap")
        (options, args) = parser.parse_args()


        if options.infile:
            infile = options.infile
        else:
            infile = "plotsMNxs.root"

        if options.outfile:
            outfile = options.outfile
        else:
            outfile = "~/plotsMNxs_norm.root"

        f = ROOT.TFile(infile, "r")
        lst = f.GetListOfKeys()

        finalMap = {}
        targetsToSamples = {}

        # options.skipFinalMap - input root file has following structure:
        #    TFile
        #      MC_XXX  ;TDirectory
        #       ptLead_central_XXX ; TH1
        #       ptLead_var1up_XXX ; TH1
        #       (...)
        #      data_XXX  ;TDirectory
        #       ptLead_central_XXX ; TH1
        #
        #  othwerwise:
        #    TFile
        #      QCD_15to3000....  ;TDirectory 
        #       ptLead_central_XXX ; TH1
            

        if options.skipFinalMap:
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
                    curObjClone = curObj.Clone()
                    curObjClone.SetDirectory(0)
                    finalMap.setdefault(target, {})
                    targetsToSamples.setdefault(target, set()) # keep empty
                    if curObjClone.GetName() in finalMap[target]:
                        finalMap[target][curObjClone.GetName()].Add(curObjClone)
                    else:
                        finalMap[target][curObjClone.GetName()] = curObjClone
        else:
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

                dirContents = currentDir.GetListOfKeys()
                for c in dirContents:
                    if "PROOF_" in c.GetName(): continue
                    if "norm" == c.GetName(): continue # not needed since we expect to get normalized histos
                    curObj = c.ReadObj()
                    if not curObj.InheritsFrom("TH1"):
                        print "Dont know how to merge", curObj.GetName(), curObj.ClassName()
                        continue

                    curObjClone = curObj.Clone()
                    curObjClone.SetDirectory(0)
                    curObjClone.SetTitle(curObjClone.GetName() + "_" + sampleName)


                    target = self.getTarget(curObjClone.GetName(), sampleName)
                    if target == None:
                        print "Skipping histo ", curObjClone.GetName(), "from sample", sampleName
                        continue


                    # save histogram in a map for future
                    finalMap.setdefault(target, {})
                    targetsToSamples.setdefault(target, set()).add(sampleName)
                    if curObjClone.GetName() in finalMap[target]:
                        finalMap[target][curObjClone.GetName()].Add(curObjClone)
                    else:
                        finalMap[target][curObjClone.GetName()] = curObjClone

        # final map done

        fOut = ROOT.TFile(outfile, "RECREATE")

        # write all histograms to root file.
        # for data histograms - divide by lumi
        for target in finalMap: # data/MC
            for histoName in finalMap[target]:
                if not self.applyScale(histoName, targetsToSamples[target]): continue
                if "data_" in target: # divide by lumi
                    lumi = self.getLumi(target, targetsToSamples[target]) # TODO
                    scale = 1./lumi
                    finalMap[target][histoName].Scale(scale)
                finalMap[target][histoName].Write(target+"_"+histoName)


        # extract variations from MC
        variations = set()
        triggers = set()
        histos = set()

        targetCategories = set() # part after the underscore

        for target in finalMap: # data_XXX / MC_XXX
            targetCategories.add(target.split("_")[-1])
            if not target.startswith("MC"): continue
            for d in finalMap[target]: # histo names 
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
        for targetCat in targetCategories:

            targetData = None
            targetsMC = []
            for target in finalMap:
                if not target.endswith(targetCat):
                    continue

                if target.startswith("data_"):
                    if targetData == None:
                        targetData = target
                        continue
                    else:
                        raise Exception("targetData allready set to "+targetData+ " (other="+target+")" )
                else:
                    targetsMC.append(target)



            for h in histos:
                #for t in triggers:
                    t = targetCat.split("_")[-1]
                    centralName = h+"_central_" +t

                    maxima = []
                    print "Doing", centralName

                    #print targetData, centralName, finalMap.keys(), finalMap[targetData].keys()
                    if centralName not in finalMap[targetData]:
                        print "#"*30
                        print " Cannot find (expected) histo:", centralName
                        print "#"*30
                        continue
        

                    hData =  finalMap[targetData][centralName]

                    maxima.append(hData.GetMaximum())


                    MCStack = ROOT.THStack("stack_"+centralName, "stack_"+centralName)
                    ROOT.SetOwnership(MCStack, False)
                    summedVariations = {}
                    summedCentral = None
                    for targetMC in targetsMC:
                        finalMap[targetMC][centralName].SetMarkerColor(2)
                        MCStack.Add(finalMap[targetMC][centralName])

                        # value needed for unc band calculation
                        if summedCentral == None:
                            summedCentral = finalMap[targetMC][centralName].Clone()
                        else:
                            summedCentral.Add(finalMap[targetMC][centralName])

                        for v in variations:
                            vname = h+"_"+v+"_"+t
                            if vname not in finalMap[targetMC]:
                                print "#"*30
                                print "Warning: variation not found: ", vname
                                print "#"*30
                                continue
                            thisVariationThisTarget = finalMap[targetMC][vname]
                            if v in summedVariations:
                                summedVariations[v].Add(thisVariationThisTarget)
                            else:
                                summedVariations[v] = thisVariationThisTarget

                            #uncHistos.append(finalMap["MC"][h+"_"+v+"_"+t])
                            #maxima.append(finalMap["MC"][h+"_"+v+"_"+t].GetMaximum())


                    uncHistos = []
                    for v in summedVariations:
                        uncHistos.append(summedVariations[v])

                    unc = self.getUncertaintyBand(uncHistos, summedCentral)

                    maxima.append(unc.GetMaximum())
                    maxima.append(MCStack.GetMaximum())

                    maximum = max(maxima)*1.05
                    unc.SetMaximum(maximum)
                    hData.SetMaximum(maximum)
                    MCStack.SetMaximum(maximum)
                    #hMCCentral.SetMarkerColor(4)
                    #hMCCentral.SetMarkerSize(2)
                    #hMCCentral.SetLineColor(4)


                    unc.SetFillColor(8);
                    hData.Draw()
                    unc.Draw("3SAME")
                    MCStack.Draw("SAME")
                    self.decorate(c1, hData, MCStack, unc)

                    c1.Print("~/tmp/"+ targetCat + "_" + centralName+".png")
                    c1.Print("~/tmp/"+ targetCat + "_" + centralName+".C")

if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    ROOT.gSystem.Load("libFWCoreFWLite.so")
    AutoLibraryLoader.enable()
    d = DrawPlots()
    d.draw()
