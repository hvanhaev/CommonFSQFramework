#!/usr/bin/env python

import ROOT
ROOT.gROOT.SetBatch(True)
from ROOT import *

import os,re,sys,math

import MNTriggerStudies.MNTriggerAna.Util

from array import array
import resource
import time

import multiprocessing
from optparse import OptionParser

def init():
    pass
    #sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    #ROOT.gSystem.Load("libFWCoreFWLite.so")
    #AutoLibraryLoader.enable()

# rooFVar - RooFormulaVar, e.g.
#  ROOT.RooFormulaVar("w", "ww", "1", ROOT.RooArgList()) (switches off weighing)
# FIXME (?) - input dataset gets modified (new variable is added)
def reweighDS(ds, newname, rooFVar):
    ds = ds.Clone()
    wvar = ds.addColumn(rooFVar)
    newDS = ROOT.RooDataSet(newname, ds.GetTitle(), ds, ds.get(), "", wvar.GetName() )
    # should we return the wvar aswell?
    #del ds
    ds.IsA().Destructor(ds)
    return newDS


def getSummedRooDS(rootName, infile, samplesToAdd, weight=None):
    init()
    f = ROOT.TFile(infile)
    trees = []

    lst = f.GetListOfKeys()
    for l in lst:
        currentDir = l.ReadObj()

        if not currentDir:
            print "Problem reading", l.GetName(), " - skipping"
            continue

        if type(currentDir) != ROOT.TDirectoryFile:
            print "Expected TDirectoryFile,", type(currentDir), "found"
            continue

        sampleName = l.GetName()
        if sampleName not in samplesToAdd: 
            continue

        tree = currentDir.Get("data") # TODO (?) - arbitrary tree name????
        trees.append(tree)

        print sampleName, tree.GetEntries()


    dummyFile = ROOT.TFile("/tmp/dummy.root", "recreate")
    if len(trees) != len(samplesToAdd):
        raise Exception("Wrong number of trees found !" + str(len(trees)) + " " + str(len(samplesToAdd)) + " ".join(samplesToAdd))

    tlist = ROOT.TList()
    for tree in trees:
        tlist.Add(tree)
    treeMerged =  ROOT.TTree.MergeTrees(tlist)
    print "data tree after merge: ", treeMerged.GetEntries()


    vars = {} # note: we whave to save the variables outside the loop, otherwise they get
              #       garbage collected by python leading to a crash

    ds = None

    #variations = set()

    vars = {}
    observables = ROOT.RooArgSet()
    print "  min/max determination"
    for b in treeMerged.GetListOfBranches():
        name =  b.GetName()
        #if name != "weight": # "Fixme??"
        #    spl = name.split("_")
        #    if len(spl) > 1:
        #        variation = name.split("_")[-1]
        #        variations.add(variation)
        #    else:
        #        print "Not a variation, skip:", name

        rmin = treeMerged.GetMinimum(name)
        rmax = treeMerged.GetMaximum(name)
        rmin = rmin-abs(rmin/100.)
        rmax = rmax+abs(rmin/100.)
        #print name, rmin, rmax
        roovar = ROOT.RooRealVar( name, name, rmin, rmax, "")
        vars[name] = roovar
        print "Creating variable", name, type(roovar)
        sys.stdout.flush()
        observables.add(roovar)
    #importCMD = RooFit.Import(tree)
    #cutCMD = RooFit.Cut(preselectionString)
    print "  create dataset...", weight
    if weight == None:
        ds = ROOT.RooDataSet(rootName, rootName, treeMerged, observables)
    #ds = ROOT.RooDataSet(rootName, rootName, treeMerged, observables,  "", weight)
    else:
        # note: if we create the RooDS directly with weight there will be problems when we want to 
        # change weights later using reweighDS function
        #ds = ROOT.RooDataSet(rootName, rootName, treeMerged, observables,  "", weight)
        dsInt = ROOT.RooDataSet(rootName+"_Internal", rootName+"_Internal", treeMerged, observables)
        workaround =  ROOT.RooFormulaVar("weightWorkaround", "weightWorkaround", weight, ROOT.RooArgList(vars[weight]))
        ds = reweighDS(dsInt, rootName, workaround)

    print "        ...done"

    print "Dataset:", rootName, ds.numEntries()
    print "Convert to vectorstore"
    ds.convertToVectorStore()
    print "        ...done"


    #if "central" not in variations:
    #    raise Exception("Central value not found!")

    return  (ds, vars)

if __name__ == "__main__":
    pass

