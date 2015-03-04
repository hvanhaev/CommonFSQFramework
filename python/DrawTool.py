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
                print "Dont know how to merge", curObj.GetName(), curObj.ClassName()
                continue
        
            curObjClone = curObj.Clone()
            curObjClone.SetDirectory(0)
            curObjClone.SetTitle(sampleName + "/" + curObjClone.GetName())
            GlobalHistoList.append(curObjClone)

    print "All histograms from ", GlobalIn, " loaded. In total: ", len(GlobalHistoList), " in the memory"
    # end getAllHistos function

def draw(localHistoList=[],normMeth=""):
    
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
        for i in GlobalCanvasList:
            if i.GetName() == hname: exists = True
        
        if not exists:
            c = TCanvas(hname,hname)
            GlobalCanvasList.append(c)
            # define legend with default style
            leg = TLegend(0.52,0.73,0.82,0.91)
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
    icanvas = 0
    for c in GlobalCanvasList:
        cname = c.GetName()
        c.cd()
    
        # loop over histograms in the list for all samples
        ihisto = 0
        for h in GlobalHistoList:
            if h.GetName() == cname:
                # get sample name
                spltstr = h.GetTitle().split("/")
                hsample = spltstr[0]
                # set normalisation
                if normMeth == "int":
                    if h.Integral() != 0: h.Scale(1./h.Integral())
                if normMeth == "max":
                    if h.GetBinContent(h.GetMaximumBin()) != 0: h.Scale(1./h.GetBinContent(h.GetMaximumBin()))
                # execute style options
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
        icanvas+=1

    
    #for s in GlobalSampleList:
    #    print "normfactor for sample: ", s, " = ", GlobalNormFactorList[s]
    
    #raw_input("\n\nPress the enter key to exit.")

    updateCanvas()

def setLineColor(hn="",color=1):
    for h in GlobalHistoList:
        if hn in h.GetTitle(): h.SetLineColor(color)

def updateCanvas():
    for c in GlobalCanvasList:
        c.Update()

def setLegend(sample="",legend=""):
    GlobalSampleDic[sample] = legend


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
