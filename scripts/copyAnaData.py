#!/usr/bin/env python
import sys,os,re

import ROOT
ROOT.gROOT.SetBatch(True)

from ROOT import *
ROOT.gSystem.Load("libFWCoreFWLite.so")
AutoLibraryLoader.enable()

from optparse import OptionParser
import subprocess

import MNTriggerStudies.MNTriggerAna.Util

sampleList=MNTriggerStudies.MNTriggerAna.Util.getAnaDefinition("sam")


parser = OptionParser(usage="usage: %prog [options] filename",
                        version="%prog 1.0")

parser.add_option("-p", "--patOnly", action="store_true", dest="patOnly")
parser.add_option("-t", "--treesOnly", action="store_true",  dest="treesOnly")
(options, args) = parser.parse_args()


if options.patOnly :
    doPAT = True
    doTrees = False
elif options.treesOnly:
    doPAT = False
    doTrees = True
else:
    doTrees = True
    doPAT = True

for s in sampleList:
    if "pathSE" not in sampleList[s]:
        print "No SE path found for sample", s
        continue
    os.system("mkdir -p "+ sampleList[s]["pathPAT"] )
    os.system("mkdir -p "+ sampleList[s]["pathTrees"] )

    command = ["lcg-ls", sampleList[s]["pathSE"]]
    proc = subprocess.Popen(command, stdout=subprocess.PIPE)
    cnt = 0
    for line in iter(proc.stdout.readline,''):
        #print "XAQ", line.rstrip()
        l =  line.strip()
        fname = l.split("/")[-1]
        if ".root" not in fname: continue
        patFile = "mnTrgAna_PAT_" in fname
        treeFile = "trees_" in fname
        doCopy = False
        if patFile and doPAT:
            doCopy = True
            targetDir = sampleList[s]["pathPAT"]
            typeString = "patFile"
        if treeFile and doTrees:
            doCopy = True
            targetDir = sampleList[s]["pathTrees"]
            typeString = "treeFile"

        if not doCopy: continue

        srcFile = sampleList[s]["pathSE"] + "/" + fname
        targetFile = targetDir + "/" + fname

        #print srcFile, targetFile
        cnt += 1

        print "Copying", typeString, " #"+str(cnt), "from", s
        cpCommand = ['lcg-cp', srcFile, targetFile]
        #cpCommand = ['lcg-ls', srcFile]
        result = subprocess.call(cpCommand)
        if result != 0:
            print "Problem within sample", s, "file", srcFile
