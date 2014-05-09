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

parser.add_option("-p", "--doPat", action="store_true", dest="pat")
parser.add_option("-t", "--doTrees", action="store_true",  dest="trees")
(options, args) = parser.parse_args()

doPAT = False
doTrees = False

if options.pat :
    doPAT = True
elif options.trees:
    doTrees = True

if not doPAT and not doTrees:
    print "Nothing to do. Run me with '-t' option to copy trees from current skim"
    sys.exit()

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

        cpCommand = ['lcg-cp', srcFile, targetFile]
        #cpCommand = ['lcg-ls', srcFile]
        if os.path.isfile(targetFile):
            print "Allready present", typeString, " #"+str(cnt), "from", s
            continue

        print "Copying", typeString, " #"+str(cnt), "from", s


        result = subprocess.call(cpCommand)
        if result != 0:
            print "Problem within sample", s, "file", srcFile
