from ROOT import *
from array import array

import os,re,sys,math
import ROOT

sys.path.append('/Users/hans/Physics/CSA14/CommonFSQFramework')

import MNTriggerStudies.MNTriggerAna.Util
import MNTriggerStudies.MNTriggerAna.Style

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
            GlobalHistoList.append(curObjClone)

    print "All histograms from ", GlobalIn, " loaded. In total: ", len(GlobalHistoList), " in the memory"
    # end getAllHistos function

def draw(localHistoList=[],normMeth="",localSampleList=[]):
    
    global GlobalCanvasList
    global GlobalLegendList
    startCL = len(GlobalCanvasList)
    
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

        exists = False
        for c in GlobalCanvasList:
            if type(c) is not TCanvas: continue
            if c.GetName() == hname: exists = True
        
        if not exists:
            c = TCanvas(hname,hname)
            GlobalCanvasList.append(c)
            # define legend with default style
            leg = TLegend(0.52,0.73,0.82,0.92)
            leg.SetMargin(0.2)
            leg.SetFillColor(kWhite)
            leg.SetBorderSize(0)
            leg.SetTextSize(0.035)
            leg.SetName(hname)
            GlobalLegendList.append(leg)

    if len(GlobalCanvasList)-startCL == 0:
        print " Your draw selection didn't result in any matched histograms..."
    else:
        print " We are going to plot ", len(GlobalCanvasList)-startCL, " canvases for you..."

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
        
        c.cd()
        
        # start with a clean legend
        GlobalLegendList[icanvas].Clear()
    
        # loop over histograms in the list for all samples
        ihisto = 0
        for h in GlobalHistoList:
            if h.GetName() == cname:
                # get sample name
                spltstr = h.GetTitle().split("/")
                hsample = spltstr[0]
                if len(localSampleList) > 0:
                    if hsample not in localSampleList: continue
                
                # set normalisation
                if normMeth == "int":
                    if h.Integral() != 0: h.Scale(1./h.Integral())
                if normMeth == "max":
                    if h.GetBinContent(h.GetMaximumBin()) != 0: h.Scale(1./h.GetBinContent(h.GetMaximumBin()))
            
                # execute style options if there are
                if os.path.isfile(sys.path[0]+"/"+GlobalScriptFile+".style"):
                    execfile(sys.path[0]+"/"+GlobalScriptFile+".style")
                
                # draw the stuff
                if ihisto == 0:
                    h.Draw()
                if ihisto != 0:
                    h.Draw("same")
                
                # add legend entry
                GlobalLegendList[icanvas].AddEntry(h,GlobalSampleDic[hsample],"lpf");
                        
                ihisto+=1

        # draw legend
        GlobalLegendList[icanvas].Draw()

    
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

def printCMS(localHistoList=[]):
    for c in GlobalCanvasList:
        if type(c) is not TCanvas: continue
        plotit = False
        if len(localHistoList) > 0:
            for n in localHistoList:
                if n in c.GetName(): plotit = True
        else:
            plotit = True

        if not plotit: continue
        c.cd()
        GlobalCMSLabel.Draw()

def printCMSPreliminary(localHistoList=[]):
    for c in GlobalCanvasList:
        if type(c) is not TCanvas: continue
        plotit = False
        if len(localHistoList) > 0:
            for n in localHistoList:
                if n in c.GetName(): plotit = True
        else:
            plotit = True
        
        if not plotit: continue
        c.cd()
        GlobalCMSPreLabel.Draw()

def printCMEnergy(localHistoList=[],cm="13"):
    GlobalCMEnergyLabel.AddText("#sqrt{s} = "+cm+" TeV")
    for c in GlobalCanvasList:
        if type(c) is not TCanvas: continue
        plotit = False
        if len(localHistoList) > 0:
            for n in localHistoList:
                if n in c.GetName(): plotit = True
        else:
            plotit = True
        
        if not plotit: continue
        c.cd()
        GlobalCMEnergyLabel.Draw()

def printLumi(lumi="",localHistoList=[]):
    GlobalLumiLabel.AddText("L = "+lumi)
    for c in GlobalCanvasList:
        if type(c) is not TCanvas: continue
        plotit = False
        if len(localHistoList) > 0:
            for n in localHistoList:
                if n in c.GetName(): plotit = True
        else:
            plotit = True
        
        if not plotit: continue
        c.cd()
        GlobalLumiLabel.Draw()


if __name__ == "__main__":
    
    # declare global variables
    GlobalIn = ""
    GlobalOut = ""
    GlobalScriptFile = ""
    GlobalHistoList = []
    GlobalCanvasList = []
    GlobalLegendList = []
    GlobalNormFactorList = {}
    GlobalSampleDic = {}
    
    GlobalLumiLabel = TPaveText(0.22,0.76,0.52,0.82,"NDC")
    GlobalLumiLabel.SetTextColor(kBlack)
    GlobalLumiLabel.SetFillColor(kWhite)
    GlobalLumiLabel.SetBorderSize(0)
    GlobalLumiLabel.SetTextAlign(12)
    GlobalLumiLabel.SetTextSize(0.035)
    #GlobalLumiLabel.SetTextFont(42)
    
    GlobalCMEnergyLabel = TPaveText(0.22,0.81,0.52,0.87,"NDC")
    GlobalCMEnergyLabel.SetTextColor(kBlack)
    GlobalCMEnergyLabel.SetFillColor(kWhite)
    GlobalCMEnergyLabel.SetBorderSize(0)
    GlobalCMEnergyLabel.SetTextAlign(12)
    GlobalCMEnergyLabel.SetTextSize(0.035)
    #GlobalCMEnergyLabel.SetTextFont(42)
    
    GlobalCMSLabel = TPaveText(0.22,0.86,0.52,0.92,"NDC")
    GlobalCMSLabel.SetTextColor(kBlack)
    GlobalCMSLabel.SetFillColor(kWhite)
    GlobalCMSLabel.SetBorderSize(0)
    GlobalCMSLabel.SetTextAlign(12)
    GlobalCMSLabel.SetTextSize(0.035)
    #GlobalCMSLabel.SetTextFont(42)
    GlobalCMSLabel.AddText("CMS")
    
    GlobalCMSPreLabel = TPaveText(0.22,0.86,0.52,0.92,"NDC")
    GlobalCMSPreLabel.SetTextColor(kBlack)
    GlobalCMSPreLabel.SetFillColor(kWhite)
    GlobalCMSPreLabel.SetBorderSize(0)
    GlobalCMSPreLabel.SetTextAlign(12)
    GlobalCMSPreLabel.SetTextSize(0.035)
    #GlobalCMSPreLabel.SetTextFont(42)
    GlobalCMSPreLabel.AddText("CMS Preliminary")
    
    GlobalSampleList=MNTriggerStudies.MNTriggerAna.Util.getAnaDefinition("sam")
    GlobalStyle = MNTriggerStudies.MNTriggerAna.Style.setStyle()
    for s in GlobalSampleList:
        GlobalSampleDic[s] = s
    
    # treat input arguments, if any. TODO: upgrade this to options...
    if len(sys.argv) > 1:
        # execute what is in the users custom draw script
        GlobalScriptFile = str(sys.argv[1])
        GlobalScriptFile = GlobalScriptFile.replace(".py","")
        print "Executing script: ", GlobalScriptFile
        execfile(sys.path[0]+"/"+str(sys.argv[1]))
    else:
        print "No script given as input, you will have to type all functions yourself now..."
