#!/usr/bin/env python

import sys
import ROOT
ROOT.gROOT.SetBatch(True)

import os,re, subprocess
from optparse import OptionParser

from MNTriggerStudies.MNTriggerAna.GetDatasetInfo import getTreeFilesAndNormalizations, validateRootFiles
from MNTriggerStudies.MNTriggerAna.Util import getAnaDefinition

# note: this script is likely to fail on slc5

def runQuiet(command):
    return subprocess.call(command,  stdout=subprocess.PIPE, stderr=subprocess.PIPE)

def main():
    filesToMerge = 10
    parser = OptionParser()
    #parser.add_option("-s", "--sample",   action="store", type="string", dest="sample", help="sample name" )
    #parser.add_option("-l", "--listSamples",   action="store", type="string", dest="list", help="listAllSamples" )
    (options, args) = parser.parse_args()

    anaDef = getAnaDefinition("sam")
    if len(args) != 1 or args[0] not in anaDef:
        print "Usage: printTTree.py sampleName"
        print "Avaliable samples:"
        for t in anaDef:
            print " ", t
        sys.exit(1)

    sample= args[0]
    treeFilesAndNormalizations = getTreeFilesAndNormalizations(maxFilesMC=None, maxFilesData=None,
                quiet = True, samplesToProcess=[sample,], usePickle=False, donotvalidate=True)

    if not treeFilesAndNormalizations[sample]["files"]:
        print "No files found for sample", sample, "- exiting"
        sys.exit(1)

    indirName = os.path.dirname(anaDef[sample]["pathSE"])
    if not indirName.startswith("srm://"):
        print "Dont know how to process: ", indirName

    odirName = indirName+"_merged/"

    #'''
    odirExists = subprocess.call(["lcg-ls", odirName],  stdout=subprocess.PIPE, stderr=subprocess.PIPE)==0
    if odirExists:
        print "output directory seems to allready exist", odirName
        sys.exit(1)

    odirCreated = subprocess.call(["srmmkdir", odirName],  stdout=subprocess.PIPE, stderr=subprocess.PIPE)==0
    if not odirCreated:
        print "cannot create output directory", odirName
        sys.exit(1)
    #'''

    aTodo = []
    todos = []
    for f in treeFilesAndNormalizations[sample]["files"]:
        aTodo.append(f)
        if len(aTodo)==filesToMerge:
            todos.append(aTodo)
            aTodo = []

    if aTodo:
        todos.append(aTodo)

    cnt = 0
    for t in todos:
        cnt += 1
        print "Doing", cnt, len(todos),"...",
        goodFiles = validateRootFiles(t, quiet=True)["fileList"]
        # be extra careful here - oname will be removed!!
        onamebase = "trees_"+str(cnt)+"_1_TMF.root"
        onameForCopy = odirName+"/"+onamebase
        command = ["lcg-ls", onameForCopy]
        if runQuiet(command)==0:
            print "Looks like file is allready present, skipping"
            continue

        oname = "/tmp/"+onamebase
        command = ["hadd", oname]
        command.extend(goodFiles)
        print "Hadd...",
        ret=runQuiet(command)
        if ret!=0:
            print "Problem with hadd, ofile", cnt
            runQuiet(["rm", oname])
            continue


        command = ["lcg-cp", "file:"+oname, onameForCopy]
        print "lcg-cp...",
        ret=runQuiet(command)
        if ret!=0:
            print "Problem with lcg-cp, ofile", cnt
            runQuiet(["rm", oname])
            runQuiet(["srmrm", onameForCopy])
            continue

        print "rm local file...",
        runQuiet(["rm", oname])
        print "done"
        

from ROOT import *
import ROOT
if __name__ == "__main__":

    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    ROOT.gSystem.Load("libFWCoreFWLite.so")
    AutoLibraryLoader.enable()
    main()

