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

    infile = "treeDiJetBalance.root"

    f = ROOT.TFile(infile, "r")
    lst = f.GetListOfKeys()

    MCTrees = []
    dataTrees = []
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
                dataTrees.append(tree)
        else:
            MCTrees.append(tree)

        print sampleName, tree.GetEntries()

        #print d

    tlist = ROOT.TList()
    for t in dataTrees:
        tlist.Add(t)

    dummyFile = ROOT.TFile("/tmp/dummy.root", "recreate")
    mergedDataTree= ROOT.TTree.MergeTrees(tlist)
    
    print "data tree after merge: ", mergedDataTree.GetEntries()


                




if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    ROOT.gSystem.Load("libFWCoreFWLite.so")
    AutoLibraryLoader.enable()
    main()
