#!/usr/bin/env python

import ROOT
ROOT.gROOT.SetBatch(True)
from ROOT import *

import os,re,sys,math

import MNTriggerStudies.MNTriggerAna.Util

from array import array
import resource
import time

from optparse import OptionParser

import MNTriggerStudies.MNTriggerAna.Style


def main():
    MNTriggerStudies.MNTriggerAna.Style.setStyle()

    parser = OptionParser(usage="usage: %prog [options] filename",
                            version="%prog 1.0")

    parser.add_option("-i", "--infile", action="store", type="string",  dest="infile" )
    parser.add_option("-o", "--outdir", action="store", type="string",  dest="outdir" )
    parser.add_option("-l", "--label", action="store", type="string",  dest="label" )

    weight = "flat2050toPU20"
    #weight = "weight"

    cutSignalHLTPTAve = "hltPtAve > XXX && hltPtCen > XXX/2 && hltPtFwd > XXX/2"
    cutToOptimizeCalo = "hltCaloPtAve > YYY && hltCaloPtCen > YYY/2 && hltCaloPtFwd > YYY/2"
    cutToOptimizeCaloSingle = "hltCaloPtCen > YYY || hltCaloPtFwd > YYY"
    cutToOptimizeL1 = " s1l1SingleJetAny > YYY"
    todo = {}

    '''
    todo["calo30"] = (30, [x for x in xrange(0,31,2)], cutSignalHLTPTAve, cutToOptimizeCalo)
    todo["calo60"] = (60, [x for x in xrange(30,61,2)], cutSignalHLTPTAve, cutToOptimizeCalo)
    todo["calo80"] = (80, [x for x in xrange(40,81,2)], cutSignalHLTPTAve, cutToOptimizeCalo)
    todo["calo100"] = (100, [x for x in xrange(50,101,5)], cutSignalHLTPTAve, cutToOptimizeCalo)
    todo["calo160"] = (160, [x for x in xrange(80,161,5)], cutSignalHLTPTAve, cutToOptimizeCalo)
    todo["calo220"] = (220, [x for x in xrange(110,221,10)], cutSignalHLTPTAve, cutToOptimizeCalo)
    todo["calo300"] = (300, [x for x in xrange(150,301,10)], cutSignalHLTPTAve, cutToOptimizeCalo)
    #'''


    todo["calo30"] = (30, [x for x in xrange(0,31,2)], cutSignalHLTPTAve, cutToOptimizeCalo)
    todo["calo60"] = (60, [x for x in xrange(0,61,2)], cutSignalHLTPTAve, cutToOptimizeCalo)
    todo["calo80"] = (80, [x for x in xrange(0,81,2)], cutSignalHLTPTAve, cutToOptimizeCalo)
    todo["calo100"] = (100, [x for x in xrange(0,101,5)], cutSignalHLTPTAve, cutToOptimizeCalo)
    todo["calo160"] = (160, [x for x in xrange(0,161,5)], cutSignalHLTPTAve, cutToOptimizeCalo)
    todo["calo220"] = (220, [x for x in xrange(0,221,10)], cutSignalHLTPTAve, cutToOptimizeCalo)
    todo["calo300"] = (300, [x for x in xrange(0,301,10)], cutSignalHLTPTAve, cutToOptimizeCalo)


    todo["caloSingle30"] = (30, [x for x in xrange(0,31,2)], cutSignalHLTPTAve, cutToOptimizeCaloSingle)
    todo["caloSingle60"] = (60, [x for x in xrange(0,61,2)], cutSignalHLTPTAve, cutToOptimizeCaloSingle)
    todo["caloSingle80"] = (80, [x for x in xrange(0,81,2)], cutSignalHLTPTAve, cutToOptimizeCaloSingle)
    todo["caloSingle100"] = (100, [x for x in xrange(0,101,5)], cutSignalHLTPTAve, cutToOptimizeCaloSingle)
    todo["caloSingle160"] = (160, [x for x in xrange(0,161,5)], cutSignalHLTPTAve, cutToOptimizeCaloSingle)
    todo["caloSingle220"] = (220, [x for x in xrange(0,221,10)], cutSignalHLTPTAve, cutToOptimizeCaloSingle)
    todo["caloSingle300"] = (300, [x for x in xrange(0,301,10)], cutSignalHLTPTAve, cutToOptimizeCaloSingle)



    todo["30l1"] =   (30, [x for x in xrange(1,29,1)], cutSignalHLTPTAve, cutToOptimizeL1)
    todo["60l1"] = (60, [x for x in xrange(21,61,1)],   cutSignalHLTPTAve, cutToOptimizeL1)
    todo["80l1"] = (80, [x for x in xrange(41,81,1)],   cutSignalHLTPTAve, cutToOptimizeL1)
    todo["100l1"] = (100, [x for x in xrange(53,101,1)],   cutSignalHLTPTAve, cutToOptimizeL1)
    todo["160l1"] = (160, [x for x in xrange(81,161,1)],   cutSignalHLTPTAve, cutToOptimizeL1)
    todo["220l1"] = (220, [x for x in xrange(113,221,1)],   cutSignalHLTPTAve, cutToOptimizeL1)
    todo["300l1"] = (300, [x for x in xrange(153,301,1)],   cutSignalHLTPTAve, cutToOptimizeL1)
    #todo["80l1"] = (60, [x for x in xrange(31,81,4)],   cutSignalHLTPTAve, cutToOptimizeL1)
    todo["singleCen60l1"] = (60, [x for x in xrange(0, 60, 1)],   "hltPtCen > XXX" , "s1l1SingleJetCentral > YYY")
    todo["singleFwd60l1"] = (60, [x for x in xrange(0, 60, 1)],   "hltPtFwd > XXX" , "s1l1SingleJetForward > YYY")


    
    (options, args) = parser.parse_args()

    label = None
    if options.label:
        label = options.label

    signalCut = ""


    if options.infile:
        infile = options.infile
    else:
        infile = "treeDiJetBalance.root"

    if options.outdir:
        odir = options.outdir
    else:
        odir = "~/tmp/effOpt/"

    os.system("mkdir -p "+odir)

    sampleList=MNTriggerStudies.MNTriggerAna.Util.getAnaDefinition("sam")

    f = ROOT.TFile(infile, "r")
    lst = f.GetListOfKeys()
    trees = {}
    trees["MC_jet15"] = []
    trees["data_jet15"] = []

    samplesData = ["Jet-Run2010B-Apr21ReReco-v1", "JetMETTau-Run2010A-Apr21ReReco-v1", "JetMET-Run2010A-Apr21ReReco-v1"]

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
        tree = currentDir.Get("data")
        isData = sampleList[sampleName]["isData"]
        if isData:
            if sampleName in samplesData:
                #tree.SetDirectory(0)
                trees["data_jet15"].append(tree)
                
        else:
            #tree.SetDirectory(0)
            trees["MC_jet15"].append(tree)

        print sampleName, tree.GetEntries()

        #print d

    dummyFile = ROOT.TFile("/tmp/dummy.root", "recreate")
    if len(trees["data_jet15"]) == 0:
            print "Cleaning data (no sample found)"
            del trees["data_jet15"]

    for t in trees:
        tlist = ROOT.TList()
        if len(trees[t]) == 1 and False:
            trees[t] = trees[t][0]
        else:
            for tree in trees[t]:
                tlist.Add(tree)
            trees[t] =  ROOT.TTree.MergeTrees(tlist)
            print "data tree after merge: ", trees[t].GetEntries()


    vars = {} # note: we whave to save the variables outside the loop, otherwise they get
              #       garbage collected by python leading to a crash

    ds = {}

    variations = set()


    for t in trees:
        print "RooDataset:",t
        vars[t] = {}
        tree = trees[t]
        observables = ROOT.RooArgSet()
        print "  min/max"
        for b in tree.GetListOfBranches():
            name =  b.GetName()
            #print "XXX", name
            if name != "weight":
                spl = name.split("_")
                if len(spl) > 1:
                    variation = name.split("_")[-1]
                    variations.add(variation)
                else:
                    print "Not a variation, skip:", name

            rmin = tree.GetMinimum(name)
            rmax = tree.GetMaximum(name)
            rmin = rmin-abs(rmin/100.)
            rmax = rmax+abs(rmin/100.)
            #print name, rmin, rmax
            roovar = ROOT.RooRealVar( name, name, rmin, rmax, "")
            vars[t][name] = roovar
            #print "Creating variable", name, type(roovar)
            sys.stdout.flush()
            observables.add(roovar)
        #importCMD = RooFit.Import(tree)
        #cutCMD = RooFit.Cut(preselectionString)
        print "  create dataset..."
        ds[t] = ROOT.RooDataSet(t, t, tree, observables, "", weight)
        print "        ...done"

        print "Dataset:", t, ds[t].numEntries()

    if "central" not in variations:
        raise Exception("Central value not found!")

    curPath = ROOT.gDirectory.GetPath()
    of = ROOT.TFile(odir+"histos.root","RECREATE")
    outputHistos = {}
    outputHistos["data_jet15"] = of.mkdir("data_jet15")
    outputHistos["MC_jet15"] = of.mkdir("MC_jet15")
    ROOT.gDirectory.cd(curPath)

    
    for t in ds:
        for signalPointName in todo:
            signalPoint = todo[signalPointName][0]
            cutSignal = todo[signalPointName][2]

            pointsToTest = todo[signalPointName][1]
            cutToOptimize = todo[signalPointName][3]

            signalCut = cutSignal.replace("XXX", str(signalPoint))
            dsSignal = ds[t].reduce(signalCut)
            numSignal =  dsSignal.sumEntries()
            print "-"*10
            print "Signal point", signalPointName
            print " Entries", numSignal

            xVals = []
            yVals = []
            for candidatePoint in pointsToTest:
                candidateCut = cutToOptimize.replace("YYY",str(candidatePoint))
                dsAfterCandCut = dsSignal.reduce(candidateCut)
                numAfterCandCut = dsAfterCandCut.sumEntries()
                eff = float(numAfterCandCut)/numSignal
                print "  cp:",candidatePoint, eff
                xVals.append(candidatePoint)
                yVals.append(eff)


            xArray = array('d', xVals)
            yArray = array('d', yVals)
            gr = ROOT.TGraph(len(xArray), xArray, yArray)
            gr.GetHistogram().SetMaximum(1.02)          
            gr.GetHistogram().SetMinimum(0.75)          
            gr.GetXaxis().SetTitle("threshold")
            gr.GetYaxis().SetTitle("efficiency")
            oname = odir + "/" + signalPointName + ".png"
            c = ROOT.TCanvas() 
            gr.Draw()
            c.Print(oname)


        '''
        binL = 13.5
        binH = 26.5
        nbins = int(binH - binL)
        histN = ROOT.TH1F("nom", "nom;PUNumInteractions for bx=0;3rd jet veto efficiency", nbins, binL, binH)
        histD = ROOT.TH1F("denom", "denom",  nbins, binL, binH)

        puVar = "PUNumInteractions"
        #puVar = "puTrueNumInteractions"
        histN = dsReducedWithVeto.fillHistogram(histN, ROOT.RooArgList(vars[t][puVar]))
        histD = dsReduced.fillHistogram(histD, ROOT.RooArgList(vars[t][puVar]))
        
        print "Total before cut:", dsReduced.sumEntries()
        print "Total after  cut:", dsReducedWithVeto.sumEntries()


        histN.Divide(histD)
        '''
        '''
		#todo["stat"] = histD
        c = ROOT.TCanvas() 
        for t in todo:
			todo[t].Draw()
			todo[t].SetMinimum(0.)
			todo[t].SetMaximum(1.02)
			if label:
			    leg = ROOT.TLegend(0.2, 0.95, 1, 1)
			    leg.SetHeader(label)
			    leg.SetFillColor(0)
			    leg.Draw("SAME")

			odir = ("~/tmp/vetoEffVsPU_"+str(minPTAve)+"/").replace(".","_")
			os.system("mkdir -p " + odir)
			name = (odir+t+"_"+str(etaMin) + "_" + str(etaMax)).replace(".","_")+".png"
			c.Print(name)
        '''




if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    ROOT.gSystem.Load("libFWCoreFWLite.so")
    AutoLibraryLoader.enable()
    MNTriggerStudies.MNTriggerAna.Style.setStyle()
    main()


