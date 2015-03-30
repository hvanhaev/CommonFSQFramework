#!/usr/bin/env python

import ROOT
ROOT.gROOT.SetBatch(True)
from ROOT import *

import os,re,sys,math

import MNTriggerStudies.MNTriggerAna.Util

from array import array


from optparse import OptionParser


class DrawPlots():
    def __init__(self, infile, outdir=None, outfile=None, skipFinalMap=False):
        self.keep = [] # avoid garbage collection
        self.infile = infile
        self.outfile=outfile
        if outdir == None:
            self.outdir = "./"
        else:
            self.outdir = outdir

        self.outdirOtherFormats = self.outdir+"/other/"
        os.system("mkdir -p " + self.outdirOtherFormats)
        self.skipFinalMap = skipFinalMap

        pass

    @staticmethod
    def splitCanvas(c):
        c.Divide(1,2)
        c.cd(1)
        split = 0.2
        margin = 0.005
        ROOT.gPad.SetPad(.005, split+margin, .995, .995)
        c.cd(2)
        ROOT.gPad.SetPad(.005, .005, .995, split)
        c.cd(1)

    @staticmethod
    def getUncertaintyBand(histos, hCentral):
        if len(histos) == 0:
            raise Exception("Empty histogram list")
        nbins = hCentral.GetNbinsX()
        for h in histos:
            if h.GetNbinsX() != nbins:
                raise Exception("Different number of bins - "+ h.GetName())

        x = array('d')

        y =  array('d')
        yUp = array('d')
        yDown = array('d')
        xUp = array('d')
        xDown = array('d')

        for i in xrange(1, nbins+1):

            centralValue = hCentral.GetBinContent(i)
            yUpLocal  = 0.
            yDownLocal  = 0.
            for h in histos:
                valLocal = h.GetBinContent(i)
                delta = centralValue - valLocal
                if delta < 0:
                    yUpLocal += delta*delta
                else:
                    yDownLocal += delta*delta

            #print histos[0].GetBinCenter(i), histos[0].GetBinLowEdge(i), histos[0].GetBinLowEdge(i+1)

            xCentral=histos[0].GetBinCenter(i)
            x.append(xCentral)
            xDown.append(xCentral-histos[0].GetBinLowEdge(i))
            xUp.append(histos[0].GetBinLowEdge(i+1)-xCentral)


            y.append(centralValue)
            yUp.append(sqrt(yUpLocal))
            yDown.append(sqrt(yDownLocal))

        minY = min(min(y), min( [a-b for a,b in zip(y, yDown)]),  min( [a+b for a,b in zip(y, yUp)]))
        maxY = max(max(y), max( [a-b for a,b in zip(y, yDown)]),  max( [a+b for a,b in zip(y, yUp)]))

        ret = ROOT.TGraphAsymmErrors(len(x), x, y, xDown, xUp, yDown, yUp)
        ret.SetFillStyle(3001);

        retD = {}
        retD["band"] = ret
        retD["min"] = minY
        retD["max"] = maxY

        return retD

    def getLumi(self, target, samples):
        print "getLumi called for", target, "- please implement me in derived class"
        return 1

    def getTarget(self, histoName, sampleName): # override
        raise Exception("")
     
    # should I scale data histogram by the lumi value?
    def applyScale(self, histoName, sampleName): # override
        return True

    def setGlobalStyle(self):  # override
        pass
    def decorate(self, canvas, dataHisto, MCStack, errBand, extra = None): # override
        pass

    def draw(self, ignoreSamples = None, doRatio = False): # core function
        self.setGlobalStyle()
        sampleList=MNTriggerStudies.MNTriggerAna.Util.getAnaDefinition("sam")
        parser = OptionParser(usage="usage: %prog [options] filename",
                                version="%prog 1.0")

        '''
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
        '''

        f = ROOT.TFile(self.infile, "r")
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
            

        if self.skipFinalMap:
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
                if ignoreSamples and sampleName in ignoreSamples:
                    print "Skipping", sampleName
                    continue

                if sampleName not in sampleList:
                    raise Exception("Thats confusing... sample not known (?) " + sampleName)

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

        if self.outfile:
            fOut = ROOT.TFile(self.outfile, "RECREATE")

        # write all histograms to root file.
        # for data histograms - divide by lumi
        for target in finalMap: # data/MC
            for histoName in finalMap[target]:
                if not self.applyScale(histoName, targetsToSamples[target]): continue
                if "data_" in target: # divide by lumi
                    lumi = self.getLumi(target, targetsToSamples[target]) # TODO
                    scale = 1./lumi
                    finalMap[target][histoName].Scale(scale)
                if self.outfile:
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
        if doRatio: self.splitCanvas(c1)

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
                    if targetData != None:
                        if centralName not in finalMap[targetData]:
                            print "#"*30
                            print " Cannot find (expected) histo:", centralName, ". Availabel: ", finalMap[targetData].keys()
                            print "#"*30
                            continue
                        hData =  finalMap[targetData][centralName]

                        maxima.append(hData.GetMaximum())
                    else:
                        hData = None


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

                    uncResult = self.getUncertaintyBand(uncHistos, summedCentral)
                    unc = uncResult["band"]


                    maxima.append(uncResult["max"])
                    maxima.append(unc.GetMaximum())
                    maxima.append(MCStack.GetMaximum())

                    #hMCCentral.SetMarkerColor(4)
                    #hMCCentral.SetMarkerSize(2)
                    #hMCCentral.SetLineColor(4)


                    maximum = max(maxima)*1.05
                    unc.SetFillColor(17);
                    if hData != None:
                        hData.SetMaximum(maximum)
                        hData.Draw()
                        #unc.Draw("3SAME")
                        unc.Draw("2SAME")
                        MCStack.Draw("SAME")
                    else:
                        MCStack.Draw()
                        #unc.Draw("3SAME")
                        unc.Draw("2SAME")
                        MCStack.Draw("SAME")

                    unc.SetMaximum(maximum)
                    MCStack.SetMaximum(maximum)
                    extra = {}
                    if doRatio: 
                        c1.cd(2)
                        MChistos = MCStack.GetStack()
                        hSum = None
                        for h in MChistos:
                            if hSum == None: hSum = h.Clone()
                            else: hSum.Add(h)


                        central = hData
                        centralRatio = hData.Clone()
                        centralRatio.Divide(central)
                        hSumRatio = hSum.Clone()
                        hSumRatio.Divide(central)

                        frame = ROOT.gPad.DrawFrame(central.GetXaxis().GetXmin(), 0, central.GetXaxis().GetXmax(), 3)
                        extra["frame"] = frame
                        ##
                        yUp = array('d')
                        yDown = array('d')
                        x = array('d')
                        y = array('d')
                        xDown = array('d')
                        xUp = array('d')
                        for iBin in xrange(1, central.GetNbinsX()+1):
                            val =  central.GetBinContent(iBin)
                            if val != 0:
                                valDown = unc.GetErrorYlow(iBin-1)/central.GetBinContent(iBin)
                                valUp =   unc.GetErrorYhigh(iBin-1)/central.GetBinContent(iBin)
                                yDown.append(valDown)
                                yUp.append(valUp)
                                #print valDown, valUp
                                x.append(unc.GetX()[iBin-1])
                                y.append(hSum.GetBinContent(iBin)/central.GetBinContent(iBin))
                                xDown.append(unc.GetErrorXlow(iBin-1))
                                xUp.append(unc.GetErrorXhigh(iBin-1))

                            #else:
                            #   yUp.append(0)
                            #   yDown.append(0)

                        if len(x) > 0:
                            uncRatio = ROOT.TGraphAsymmErrors(len(x), x, y, xDown, xUp, yDown, yUp)
                            uncRatio.SetFillStyle(3001)
                            uncRatio.SetFillColor(17)
                            uncRatio.Draw("2SAME")
                            centralRatio.Draw("SAME")
                            hSumRatio.Draw("SAME")

                        
                        c1.cd(1)


                    self.decorate(c1, hData, MCStack, unc, extra)

                    c1.Print(self.outdir + "/" + targetCat + "_" + centralName+".png")
                    c1.Print(self.outdirOtherFormats + "/"+ targetCat + "_" + centralName+".pdf")
                    c1.Print(self.outdirOtherFormats + "/"+ targetCat + "_" + centralName+".root")

if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    ROOT.gSystem.Load("libFWCoreFWLite.so")
    AutoLibraryLoader.enable()
    d = DrawPlots()
    d.draw()
