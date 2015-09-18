#!/usr/bin/env python

from ROOT import *
from array import array

import os,re,sys,math
import ROOT

sys.path.append('/Users/hans/Physics/CSA14/CommonFSQFramework')

import CommonFSQFramework.Core.Util
import CommonFSQFramework.Core.Style
import CommonFSQFramework.Core.DrawUtil

def setInput(inputfile):
    global GlobalIn
    GlobalIn = inputfile
    print " input file set to: ", GlobalIn

def setOutput(outputfile):
    global GlobalOut
    GlobalOut = outputfile
    print " output file set to: ", GlobalOut

def resetCanvas():
    global GlobalCanvasList
    while len(GlobalCanvasList) > 0 :
        c = GlobalCanvasList.pop()
        if type(c) is TCanvas: c.Close()

def setBatchMode():
    ROOT.gROOT.SetBatch(True)
    global wait
    wait = False

def saveCanvas(outdir="./",tosave=[],formats=["pdf"]):
    global GlobalCanvasList
    for c in GlobalCanvasList:
        if type(c) is TCanvas:
            printit = False
            if len(tosave) > 0:
                for n in tosave:
                    if n in c.GetName(): printit = True
            else:
                printit = True

            if not printit: continue
        
        if type(c) is TCanvas:
            if "pdf" in formats: c.Print(outdir+c.GetName()+".pdf")
            if "eps" in formats: c.Print(outdir+c.GetName()+".eps")
            if "png" in formats: c.Print(outdir+c.GetName()+".png")
            if "C" in formats: c.Print(outdir+c.GetName()+".C")

def resetHisto():
    global GlobalHistoList
    while len(GlobalHistoList) > 0 : GlobalHistoList.pop()

def getAllHistos():
    
    # needs access to following global variables
    global GlobalIn
    global GlobalHistoList
    global GlobalNormFactorList
    
    # reset lists
    GlobalHistoList = []
    GlobalNormFactorList = {}
    
    # open the input ROOT file
    theTFile = ROOT.TFile(GlobalIn, "r")
    theList = theTFile.GetListOfKeys()

    for l in theList:
        print "Going through", l.GetName()
        currentDir = l.ReadObj()
        
        if not currentDir:
            print "Problem reading", l.GetName(), " - skipping"
            continue
                
        if type(currentDir) != ROOT.TDirectoryFile:
            print "Expected TDirectoryFile,", type(currentDir), "found"
            continue
                
        sampleName = l.GetName()
        if sampleName not in GlobalSampleList:
            raise Exception("Thats confusing... could not find directory name in the GlobalSampleList...")
        
        dirContents = currentDir.GetListOfKeys()
        for c in dirContents:
            if "PROOF_" in c.GetName(): continue
            
            # save the normfactor if it is found
            if "norm" == c.GetName():
                GlobalNormFactorList[sampleName] = c.ReadObj().GetBinContent(1)
                print " Read normfactor from root file: ", GlobalNormFactorList[sampleName]
                continue

            curObj = c.ReadObj()
            if not curObj.InheritsFrom("TH1"):
                print "Dont know how to load", curObj.GetName(), curObj.ClassName()
                continue
        
            curObjClone = curObj.Clone()
            curObjClone.SetDirectory(0)
            curObjClone.SetTitle(sampleName + "/" + curObjClone.GetName())
            curObjClone.UseCurrentStyle()
            GlobalHistoList.append(curObjClone)

    print "All histograms from ", GlobalIn, " loaded. In total: ", len(GlobalHistoList), " in the memory"
    # end getAllHistos function

def draw(localHistoList=[],normMeth="",localSampleList=[]):
    
    global GlobalCanvasList
    global GlobalLegendList
    global GlobalHistoRatioList
    
    startCL = len(GlobalCanvasList)
    
    wehaveratiosample = False
    
    if len(GlobalHistoList) == 0:
        print "Please first read all the histograms from a root file into the memory by executing getAllHistos()"
        return
    
    for h in GlobalHistoList:
        # filter out histograms you don't want to plot
        plotit = False
        if len(localHistoList) > 0:
            for n in localHistoList:
                if n in h.GetName(): plotit = True
        else:
            plotit = True
        if not plotit: continue

        spltstr = h.GetTitle().split("/")
        hsample = spltstr[0]
        hname = spltstr[1]
        if hname != h.GetName(): print "Help! This doesn't make sense: hname != h.GetName()"
        isData = GlobalSampleList[hsample]["isData"]
        if hsample == GlobalPlotRatioToSample: wehaveratiosample = True

        exists = False
        for c in GlobalCanvasList:
            if type(c) is not TCanvas: continue
            if c.GetName() == hname: exists = True
        
        if not exists:
	    if GlobalPlotRatio:
	        c = CommonFSQFramework.Core.DrawUtil.makeCMSCanvas(hname,hname,800,760)
            else:
	        c = CommonFSQFramework.Core.DrawUtil.makeCMSCanvas(hname,hname,800,600)
	    GlobalCanvasList.append(c)
            # define legend with default style
            nentries = len(GlobalNormFactorList)
            if len(localSampleList) != 0: nentries = len(localSampleList)
            leg = CommonFSQFramework.Core.DrawUtil.makeLegend(nentries)
            leg.SetName(hname)
            GlobalLegendList.append(leg)

    if len(GlobalCanvasList)-startCL == 0:
        print " Your draw selection didn't result in any matched histograms..."
    else:
        print " We are going to plot ", len(GlobalCanvasList)-startCL, " canvases for you..."

    # if there's a local sample list, check if the ratio reference sample is there
    if GlobalPlotRatio:
        if len(localSampleList) > 0:
            if GlobalPlotRatioToSample not in localSampleList:
                wehaveratiosample = False
                print " the sample you want to plot the ratio too, is not found... you have to include it in the third argument of the draw function."

    # loop over canvases you want
    for icanvas, c in enumerate(GlobalCanvasList):
        if type(c) is not TCanvas: continue
        cname = c.GetName()
        
        # check if we still need to plot this canvas
        plotit = False
        if len(localHistoList) > 0:
            for n in localHistoList:
                if n in cname: plotit = True
        else:
            plotit = True
        if not plotit: continue

        upperpad = None
	lowerpad = None
	reallyPlotRatio = False
        if GlobalPlotRatio and len(localSampleList) != 1 and wehaveratiosample: reallyPlotRatio = True
	if reallyPlotRatio:
	    c.cd()
	    upperpad = TPad(cname+"_up",cname+"_up",0,0.305,1,1)
	    lowerpad = TPad(cname+"_down",cname+"_down",0,0,1,0.305)
	    upperpad.SetLeftMargin(0.12)
	    upperpad.SetRightMargin(0.04)
	    upperpad.SetTopMargin(0.08*600/528)
	    upperpad.SetBottomMargin(0)
	    lowerpad.SetLeftMargin(0.12)
	    lowerpad.SetRightMargin(0.04)
	    lowerpad.SetTopMargin(0)
	    lowerpad.SetBottomMargin(0.12*600/232)
	    lowerpad.SetTickx(1)
	    upperpad.Draw()
	    lowerpad.Draw()
	    upperpad.cd()
	    
        else:
            c.cd()
	    
        # start with a clean legend
        GlobalLegendList[icanvas].Clear()

        hdata = None
        # first plot all data samples
        ihisto = 0
        for h in GlobalHistoList:
            if h.GetName() == cname:
                # get sample name
                spltstr = h.GetTitle().split("/")
                hsample = spltstr[0]
                if len(localSampleList) > 0:
                    if hsample not in localSampleList: continue
                
                isData = GlobalSampleList[hsample]["isData"]
                if isData:
                    # set normalisation
                    if normMeth == "int":
                        if h.Integral() != 0: h.Scale(1./h.Integral())
                    if normMeth == "max":
                        if h.GetBinContent(h.GetMaximumBin()) != 0: h.Scale(1./h.GetBinContent(h.GetMaximumBin()))
                    
		    # draw the stuff
		    if reallyPlotRatio:
                        h.GetYaxis().SetTitleSize(0.06*600/528)
                        h.GetYaxis().SetTitleOffset(0.83)
                        #h.GetYaxis().SetTickLength(0.03*600/528)
                        h.GetYaxis().SetLabelSize(0.05*600/528)
                        h.GetYaxis().SetLabelOffset(0.007*528/600)
                        h.GetXaxis().SetTitleSize(0.06*600/528)
                        h.GetXaxis().SetTitleOffset(0.9*528/600)
                        h.GetXaxis().SetTickLength(0.03*600/528)
                        h.GetXaxis().SetLabelSize(0.05*600/528)
                        h.GetXaxis().SetLabelOffset(0.007*528/600)

                    # execute style options if there are
                    if os.path.isfile(GlobalScriptFile+".style"):
                        execfile(GlobalScriptFile+".style")
		    
                    if ihisto == 0: h.Draw()
                    if ihisto != 0: h.Draw("same")
                    if hsample == GlobalPlotRatioToSample: hdata = h.Clone()
                    # add legend entry
                    GlobalLegendList[icanvas].AddEntry(h,GlobalSampleDic[hsample],"lpf");
                    ihisto+=1

        # then plot all MC samples
        for h in GlobalHistoList:
            if h.GetName() == cname:
                # get sample name
                spltstr = h.GetTitle().split("/")
                hsample = spltstr[0]
                if len(localSampleList) > 0:
                    if hsample not in localSampleList: continue
                
                isData = GlobalSampleList[hsample]["isData"]
                if not isData:
                    # set normalisation
                    if normMeth == "int":
                        if h.Integral() != 0: h.Scale(1./h.Integral())
                    if normMeth == "max":
                        if h.GetBinContent(h.GetMaximumBin()) != 0: h.Scale(1./h.GetBinContent(h.GetMaximumBin()))
                
                    # draw the stuff
		    if reallyPlotRatio:
                        h.GetYaxis().SetTitleSize(0.06*600/528)
                        h.GetYaxis().SetTitleOffset(0.83)
                        #h.GetYaxis().SetTickLength(0.03*600/528)
                        h.GetYaxis().SetLabelSize(0.05*600/528)
                        h.GetYaxis().SetLabelOffset(0.007*528/600)
                        h.GetXaxis().SetTitleSize(0.06*600/528)
                        h.GetXaxis().SetTitleOffset(0.9*528/600)
                        h.GetXaxis().SetTickLength(0.03*600/528)
                        h.GetXaxis().SetLabelSize(0.05*600/528)
                        h.GetXaxis().SetLabelOffset(0.007*528/600)

                    # execute style options if there are
                    if os.path.isfile(GlobalScriptFile+".style"):
                        execfile(GlobalScriptFile+".style")
		    
                    if ihisto == 0: h.Draw()
                    if ihisto != 0: h.Draw("same")
                    if hsample == GlobalPlotRatioToSample: hdata = h.Clone()
                    # add legend entry
                    GlobalLegendList[icanvas].AddEntry(h,GlobalSampleDic[hsample],"lpf");
                    ihisto+=1

        # draw legend
	if reallyPlotRatio: GlobalLegendList[icanvas].SetTextSize(0.04*600/528)
        GlobalLegendList[icanvas].Draw()
	
        # add CMS lumi style to current active pad
	if GlobalLumiPos == "left" and GlobalIsPrel: CommonFSQFramework.Core.DrawUtil.printLumiPrelLeft(gPad,GlobalLumiValue)
	if GlobalLumiPos == "out" and GlobalIsPrel: CommonFSQFramework.Core.DrawUtil.printLumiPrelOut(gPad,GlobalLumiValue)
        if GlobalLumiPos == "left" and not GlobalIsPrel: CommonFSQFramework.Core.DrawUtil.printLumiLeft(gPad,GlobalLumiValue)
        if GlobalLumiPos == "out" and not GlobalIsPrel: CommonFSQFramework.Core.DrawUtil.printLumiOut(gPad,GlobalLumiValue)	

        # ratio pad
        if reallyPlotRatio:
            lowerpad.cd()
            gPad.SetTitle("")
            
            if hdata.InheritsFrom("TH1"):
                iratio = 0
                for h in GlobalHistoList:
                    if h.GetName() == cname:
                        # get sample name
                        spltstr = h.GetTitle().split("/")
                        hsample = spltstr[0]
                        if len(localSampleList) > 0:
                            if hsample not in localSampleList: continue
                        
                        if hsample != GlobalPlotRatioToSample:
                            #calculate ratio to data
                            hratio = None
                            # if it is a TProfile, we have to divide their projectionsX
                            if type(h) is TProfile:
                                hratio = h.ProjectionX()
                                hratio.SetName(hratio.GetName() + "_ratio")
                                hratio.Divide(hdata.ProjectionX())
                                # copy style
                                hratio.SetLineColor(h.GetLineColor())
                                hratio.SetLineStyle(h.GetLineStyle())
                                hratio.SetLineWidth(h.GetLineWidth())
                                hratio.SetMarkerStyle(h.GetMarkerStyle())
                                hratio.SetMarkerSize(h.GetMarkerSize())
                                hratio.SetMarkerColor(h.GetMarkerColor())
                            else:
                                hratio = h.Clone()
                                hratio.Divide(hdata)

                            hratio.GetYaxis().SetTitle("MC/Data")
                            hratio.GetYaxis().SetRangeUser(0.1,1.9)
			    hratio.GetYaxis().SetTitleSize(0.06*600/232)
			    hratio.GetYaxis().SetTitleOffset(0.4)
			    hratio.GetYaxis().SetTickLength(0.04)
			    hratio.GetYaxis().SetLabelSize(0.05*600/232)
			    #hratio.GetYaxis().SetLabelOffset(0.007*232/600)
			    hratio.GetYaxis().SetNdivisions(505)
                            hratio.GetXaxis().SetTitleSize(0.06*600/232)
                            hratio.GetXaxis().SetTitleOffset(0.85)
                            hratio.GetXaxis().SetTickLength(0.03*600/232)
                            hratio.GetXaxis().SetLabelSize(0.05*600/232)
                            hratio.GetXaxis().SetLabelOffset(0.007*600/232)
			    
                            GlobalHistoRatioList.append(hratio)
                            # draw the stuff
                            if iratio == 0: hratio.Draw()
                            if iratio != 0: hratio.Draw("same")

                            iratio+=1
    


    #for s in GlobalSampleList:
    #    print "normfactor for sample: ", s, " = ", GlobalNormFactorList[s]

    updateCanvas()

def setLineColor(hn="",color=1):
    for h in GlobalHistoList:
        if hn in h.GetTitle(): h.SetLineColor(color)

def updateCanvas():
    for c in GlobalCanvasList:
        if type(c) is TCanvas:
            c.Update()

def setLegend(sample="",legend=""):
    GlobalSampleDic[sample] = legend

def plotRatio(value=True,data=""):
    global GlobalPlotRatio
    global GlobalPlotRatioToSample
    GlobalPlotRatio = value
    if data != "":
        GlobalPlotRatioToSample = data
    else:
        for s in GlobalSampleList:
            isData = GlobalSampleList[s]["isData"]
            if isData:
                GlobalPlotRatioToSample = s
                break
        if GlobalPlotRatioToSample == "":
            print " no valid data sample found, please select it manually"
            GlobalPlotRatio = False

    if GlobalPlotRatio: print "The following sample will be used to plot the ratio to: ", GlobalPlotRatioToSample
    
def setLumiPos(pos="left"):
    global GlobalLumiPos
    GlobalLumiPos = pos
    
def setLumiValue(value="13 TeV"):
    global GlobalLumiValue
    GlobalLumiValue = value
    
def isPreliminary(value=True):
    global GlobalIsPrel
    GlobalIsPrel = value

	

if __name__ == "__main__":
    
    # declare global variables
    wait = True
    GlobalIn = ""
    GlobalOut = ""
    GlobalScriptFile = ""
    GlobalHistoList = []
    GlobalHistoRatioList = []
    GlobalCanvasList = []
    GlobalLegendList = []
    GlobalNormFactorList = {}
    GlobalSampleDic = {}
    
    GlobalPlotRatio = False
    GlobalPlotRatioToSample = ""
    
    GlobalLumiPos = "left"
    GlobalLumiValue = "13 TeV"
    GlobalIsPrel = True
    
    GlobalSampleList=CommonFSQFramework.Core.Util.getAnaDefinition("sam")
    GlobalStyle = CommonFSQFramework.Core.Style.setStyle()
    # local changes to tdr style
    GlobalStyle.SetTitleYOffset(1)
    GlobalStyle.SetPadTickX(0)
    GlobalStyle.SetPadTickY(0)

    for s in GlobalSampleList:
        GlobalSampleDic[s] = s
    
    # treat input arguments, if any. TODO: upgrade this to options...
    if len(sys.argv) > 1:
        # execute what is in the users custom draw script
        GlobalScriptFile = str(sys.argv[1])
        GlobalScriptFile = GlobalScriptFile.replace(".py","")
        print "Executing script: ", GlobalScriptFile
        execfile(str(sys.argv[1]))
    else:
        print "No script given as input, you will have to type all functions yourself now..."

    if wait:
        print " "
        print " "
        py3 = sys.version_info[0] > 2 #creates boolean value for test that Python major version > 2
        if py3:
            response = input("Press enter to exit ")
        else:
            response = raw_input("Press enter to exit ")
