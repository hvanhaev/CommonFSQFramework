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

    #weight = "flat2050toPU20"
    #weight = "weight"
    weight = ""


   
    (options, args) = parser.parse_args()

    label = None
    if options.label:
        label = options.label

    signalCut = ""


    if options.infile:
        infile = options.infile
    else:
        infile = "plotsJECExperiments.root"

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

    treeName = "dataFit"

    for l in lst:
        print "Going through", l.GetName(), l.ClassName()
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
        tree = currentDir.Get(treeName)
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
            #print "YYY", name
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
        if weight:
            print "     ...weight", weight
            ds[t] = ROOT.RooDataSet(t, t, tree, observables, "", weight)
        else:
            print "     ...no weight"
            ds[t] = ROOT.RooDataSet(t, t, tree, observables)
        print "        ...done"

        print "Dataset:", t, ds[t].numEntries()


    curPath = ROOT.gDirectory.GetPath()
    of = ROOT.TFile(odir+"histos.root","RECREATE")
    outputHistos = {}
    outputHistos["data_jet15"] = of.mkdir("data_jet15")
    outputHistos["MC_jet15"] = of.mkdir("MC_jet15")
    ROOT.gDirectory.cd(curPath)

    
    #print vars["MC_jet15"].keys()
    # ['ptRaw', 'weight', 'ptGen', 'area', 'eta', 'rho']
    
    of = open("bfj.txt","w")

    ROOT.gROOT.ProcessLine(".L fit.cxx+")
    # http://root.cern.ch/root/html/tutorials/roofit/rf609_xychi2fit.C.html

    etas = [-0.2, 0.2]

    for t in ds:
        if t == "data_jet15": continue
        for i in xrange(len(etas)-1):
            etaL = etas[i]
            etaH = etas[i+1]
            print "Limiting range..."
            dsReduced = ds[t].reduce("ptRaw > 15 && ptRaw < 1000 && eta >"+str(etaL)+" && eta <"+str(etaH))
            print "              ...done", ds[t].numEntries(), "->", dsReduced.numEntries()

            pt = vars[t]["ptRaw"]
            ptGen = vars[t]["ptGen"]
            a = RooRealVar("a","a",0.0,-100,100) 
            b = RooRealVar("b","b",0.0,-100,100) 
            #f= ROOT.getTF(pt, RooArgList(a,b))
            #rho = vars[t]["rho"]
            rho = vars[t]["rhoarea"]
            pu = RooRealVar("pu","pu",0.0,-100,100) 
            f= ROOT.getTF2d(pt, rho, RooArgList(a,b, pu))
            #frame = pt.frame(RooFit.Title("Chi^2 fit of function set of (X#pmdX,Y#pmdY) values")) 
            #dsReduced.plotOnXY(frame, RooFit.YVar(ptGen))
            f.chi2FitTo(dsReduced, RooFit.YVar(ptGen))
            #f.plotOn(frame)
            #c = ROOT.TCanvas() 
            #frame.Draw()
            #c.Print("~/tmp/test.png")

        of.write(" ".join(map(str, ["BFJ", etaL, etaH, a.getVal(), b.getVal(), pu.getVal(), "|", a.getError(), b.getError(), pu.getError()] )))



if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    ROOT.gSystem.Load("libFWCoreFWLite.so")
    ROOT.gSystem.Load( "libRooFit" )
    AutoLibraryLoader.enable()
    MNTriggerStudies.MNTriggerAna.Style.setStyle()
    main()


