import os, sys, imp
import ROOT
from array import array
import CommonFSQFramework.Core.CMS_lumi

def getHisto(file,histoname,sample):
    # open the input ROOT file
    theTFile = ROOT.TFile(file, "r")
    theList = theTFile.GetListOfKeys()

    h = None
    for l in theList:
        currentDir = l.ReadObj()
        
        if not currentDir:
            print "Problem reading", l.GetName(), " - skipping"
            continue
                
        if type(currentDir) != ROOT.TDirectoryFile:
            print "Expected TDirectoryFile,", type(currentDir), "found"
            continue
                
        sampleName = l.GetName()
        if sampleName != sample: continue
        
        dirContents = currentDir.GetListOfKeys()
        for c in dirContents:
            if "PROOF_" in c.GetName(): continue

            curObj = c.ReadObj()
            if not (curObj.InheritsFrom("TH1") or curObj.InheritsFrom("TH2")):
                #print "Dont know how to load", curObj.GetName(), curObj.ClassName()
                continue
	    	
            if curObj.GetName() != histoname: continue
	
	    print " returning", curObj.GetName(), "from", sampleName
            curObjClone = curObj.Clone()
            curObjClone.SetDirectory(0)
            curObjClone.SetTitle(sampleName + "/" + curObjClone.GetName())
	    h = curObjClone
    
    h.UseCurrentStyle()
    return h
    
def makeCMSCanvas(name="canvas",title="canvas",width=800,height=600):
    canvas = ROOT.TCanvas(name,name,50,50,width,height)
    canvas.SetFillColor(0)
    canvas.SetBorderMode(0)
    canvas.SetFrameFillStyle(0)
    canvas.SetFrameBorderMode(0)
    T = 0.08*600
    B = 0.12*600 
    L = 0.12*800
    R = 0.04*800
    canvas.SetLeftMargin( L/width )
    canvas.SetRightMargin( R/width )
    canvas.SetTopMargin( T/height )
    canvas.SetBottomMargin( B/height )
    canvas.SetTickx(0)
    canvas.SetTicky(0)
    if width == 800: ROOT.gStyle.SetTitleYOffset(1)
    return canvas
    
def makeLegend(nentries=1):
    height = nentries*0.06
    leg = ROOT.TLegend(0.56,(0.88 - height),0.92,0.88)
    leg.SetMargin(0.2)
    leg.SetFillColor(ROOT.kWhite)
    leg.SetBorderSize(0)
    leg.SetTextSize(0.04)
    leg.SetTextFont(42)
    return leg    

def printLumiPrelLeft(canvas, lumitext="13 TeV"):
    #change the CMS_lumi variables (see CMS_lumi.py)
    CommonFSQFramework.Core.CMS_lumi.writeExtraText = 1
    CommonFSQFramework.Core.CMS_lumi.extraText = "Preliminary"
    CommonFSQFramework.Core.CMS_lumi.lumi_sqrtS = lumitext # used with iPeriod = 0, e.g. for simulation-only plots (default is an empty string)
    
    iPos = 11 # inside frame left, default
    
    if ( iPos==0 ): CommonFSQFramework.Core.CMS_lumi.relPosX = 0.12
    iPeriod = 0
    
    CommonFSQFramework.Core.CMS_lumi.CMS_lumi(canvas, iPeriod, iPos)
    

def printLumiPrelOut(canvas, lumitext="13 TeV"):
    #change the CMS_lumi variables (see CMS_lumi.py)
    CommonFSQFramework.Core.CMS_lumi.writeExtraText = 1
    CommonFSQFramework.Core.CMS_lumi.extraText = "Preliminary"
    CommonFSQFramework.Core.CMS_lumi.lumi_sqrtS = lumitext # used with iPeriod = 0, e.g. for simulation-only plots (default is an empty string)
    
    iPos = 0 # outside frame left
    
    if ( iPos==0 ): CommonFSQFramework.Core.CMS_lumi.relPosX = 0.12
    iPeriod = 0
    
    CommonFSQFramework.Core.CMS_lumi.CMS_lumi(canvas, iPeriod, iPos)

def printLumiLeft(canvas, lumitext="13 TeV"):
    #change the CMS_lumi variables (see CMS_lumi.py)
    CommonFSQFramework.Core.CMS_lumi.writeExtraText = 0
    CommonFSQFramework.Core.CMS_lumi.extraText = ""
    CommonFSQFramework.Core.CMS_lumi.lumi_sqrtS = lumitext # used with iPeriod = 0, e.g. for simulation-only plots (default is an empty string)

    iPos = 11 # inside frame left, default

    if ( iPos==0 ): CommonFSQFramework.Core.CMS_lumi.relPosX = 0.12
    iPeriod = 0

    CommonFSQFramework.Core.CMS_lumi.CMS_lumi(canvas, iPeriod, iPos)


def printLumiOut(canvas, lumitext="13 TeV"):
    #change the CMS_lumi variables (see CMS_lumi.py)
    CommonFSQFramework.Core.CMS_lumi.writeExtraText = 0
    CommonFSQFramework.Core.CMS_lumi.extraText = ""
    CommonFSQFramework.Core.CMS_lumi.lumi_sqrtS = lumitext # used with iPeriod = 0, e.g. for simulation-only plots (default is an empty string)

    iPos = 0 # outside frame left        

    if ( iPos==0 ): CommonFSQFramework.Core.CMS_lumi.relPosX = 0.12
    iPeriod = 0

    CommonFSQFramework.Core.CMS_lumi.CMS_lumi(canvas, iPeriod, iPos)
