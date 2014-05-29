#!/usr/bin/env python

import ROOT
ROOT.gROOT.SetBatch(True)
from ROOT import *

import os,re,sys,math

import MNTriggerStudies.MNTriggerAna.Util

from array import array
import resource
import time


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

    infile = "treeDiJetBalance.root"

    f = ROOT.TFile(infile, "r")
    lst = f.GetListOfKeys()


    trees = {}
    trees["MC"] = []
    trees["data"] = []

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
                trees["data"].append(tree)
                
        else:
            #tree.SetDirectory(0)
            trees["MC"].append(tree)

        print sampleName, tree.GetEntries()

        #print d

    dummyFile = ROOT.TFile("/tmp/dummy.root", "recreate")
    for t in trees:
        tlist = ROOT.TList()
        if len(trees[t]) == 1 and False:
            trees[t] = trees[t][0]
        else:
            for tree in trees[t]:
                tlist.Add(tree)
            trees[t] =  ROOT.TTree.MergeTrees(tlist)
            print "data tree after merge: ", trees[t].GetEntries()


    vars = [] # note: we whave to save the variables outside the loop, otherwise they get
              #       garbage collected by python leading to a crash

    ds = {}

    variations = set()
    for t in trees:
        print "RooDataset:",t
        tree = trees[t]
        observables = ROOT.RooArgSet()
        print "  min/max"
        for b in tree.GetListOfBranches():
            name =  b.GetName()
            if name != "weight":
                variation = name.split("_")[-1]
                variations.add(variation)

            rmin = tree.GetMinimum(name)
            rmax = tree.GetMaximum(name)
            rmin = rmin-abs(rmin/100.)
            rmax = rmax+abs(rmin/100.)
            #print name, rmin, rmax
            roovar = ROOT.RooRealVar( name, name, rmin, rmax, "")
            vars.append(roovar)
            print "Creating variable", name, type(roovar)
            sys.stdout.flush()
            observables.add(roovar)
        #importCMD = RooFit.Import(tree)
        #cutCMD = RooFit.Cut(preselectionString)
        print "  create dataset..."
        ds[t] = ROOT.RooDataSet(t, t, tree, observables, "", "weight")
        print "        ...done"

        print "Dataset:", t, ds[t].numEntries()

    if "central" not in variations:
        raise Exception("Central value not found!")


    etaRanges = []
    etaRanges.extend([1.401, 1.701, 2.001, 2.322, 2.411, 2.601, 2.801, 3.001, 3.201, 3.501, 3.801, 4.101, 4.701])
    minPtAVG = 45
    for t in ds:
        for v in variations:
            if t=="data" and v != "central":
                continue
            for iEta in xrange(1, len(etaRanges)):
                etaMin = etaRanges[iEta-1]
                etaMax = etaRanges[iEta]
                print "Doing", t, v, etaMin, etaMax

                def vary(x, v=v):
                    return x + "_" + v

                cut = vary("tagPt") + " > 1"
                cut += " && " + vary("probePt") + " > 35 "
                cut += " && abs(" + vary("probeEta") + ") >  " + str(etaMin)
                cut += " && abs(" + vary("probeEta") + ") <  " + str(etaMax)
                cut += " && " + vary("ptAve") + " > " + str(minPtAVG)
                print cut

                dsReduced = ds[t].reduce(cut)
                #mean2 = RooRealVar("mean","mean of gaussian", 0, -1.5, 1.5)
                #sigma2 = RooRealVar("sigma","width of gaussian", .1, 0, 1)
                #gauss2 = RooGaussian("gauss","gaussian PDF",myVar, mean2, sigma2)
                #gauss2.fitTo(dsReduced, RooFit.Range(rangeLow, rangeHigh), RooFit.PrintLevel(-1)) # this exludes -1 point ("no jet matched point")







    #print "Sleep"
    #time.sleep(60)
    #print "Meminfo:", resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    #todo = {}
    #todo["MC"] = 
    #                 branches =  current.GetListOfBranches()


                




if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    ROOT.gSystem.Load("libFWCoreFWLite.so")
    AutoLibraryLoader.enable()
    main()
