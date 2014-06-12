#!/usr/bin/env python

import os, sys, imp
import ROOT
ROOT.gROOT.SetBatch(True)
from ROOT import *

from MNTriggerStudies.MNTriggerAna.GetDatasetInfo import getTreeFilesAndNormalizations
import MNTriggerStudies.MNTriggerAna.Util

from optparse import OptionParser

if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    ROOT.gSystem.Load("libFWCoreFWLite.so")
    AutoLibraryLoader.enable()


    parser = OptionParser()
    (options, args) = parser.parse_args()
    if len(args) != 1:
        print "Usage: copyAnaDataLocal.py localDir"
        print "    usefull for making local copy of data (e.g. nfs to /tmp/)"
        sys.exit(0)

    target = args[0]


    treeFilesAndNormalizations = getTreeFilesAndNormalizations()

    anaDefFile = os.environ["SmallXAnaDefFile"]
    mod_dir, filename = os.path.split(anaDefFile)
    mod, ext = os.path.splitext(filename)
    f, filename, desc = imp.find_module(mod, [mod_dir])
    mod = imp.load_module(mod, f, filename, desc)



    localBasePathPAT = mod.PATbasePATH
    localBasePathTrees = mod.TTreeBasePATH

    targetPAT = target + "/PAT/"
    targetTrees = target + "/trees/"

    print "Copy to:"
    print targetPAT
    print targetTrees

    for s in treeFilesAndNormalizations:
        for f in treeFilesAndNormalizations[s]["files"]:
            src = f

            if localBasePathPAT in f:
                trg = f.replace(localBasePathPAT, targetPAT)
            elif localBasePathTrees in f:
                trg = f.replace(localBasePathTrees, targetTrees)
            else:
                print "File not known: ", f # shouldnt happen
                continue


            if os.path.isfile(trg): 
                s1 = os.path.getsize(src)
                s2 = os.path.getsize(trg)
                if s1 != s2:
                    print "File size dont match. Will overwrite", trg
                else:
                    continue
            dirname = os.path.dirname(trg)
            os.system("mkdir -p "+  dirname)
            #print src, trg
            os.system("cp " + src + " " + trg)


    print 'PATbasePATH="'+targetPAT+'"'
    print 'TTreeBasePATH="' + targetTrees + '"'


