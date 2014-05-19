#!/usr/bin/env python
import sys,os,re, time

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


lastTime = 0
for s in sampleList:
    if "pathSE" not in sampleList[s]:
        print "No SE path found for sample", s
        continue
    os.system("mkdir -p "+ sampleList[s]["pathPAT"] )
    os.system("mkdir -p "+ sampleList[s]["pathTrees"] )

    cnt = 0


    # on my installation lcg-ls does not have offset/count params
    # needed for srm access to dirs with >1000 files.
    #command = ["lcg-ls", sampleList[s]["pathSE"]]
    
    maxResults = 500
    offset = 0
    while True: # handle 100 results at a time
        command = ["srmls", "-2", "--offset", str(offset), "--count", str(maxResults),  sampleList[s]["pathSE"]]
        retryCnt = 1
        goodRootFiles = 0
        # for current offset value obtain list of files.
        #    Try couple of times to handle empty output of srmls for some calls
        while True:
            lineCnt = 0
            print "Obtaining file list for", s, "- try", retryCnt, "offset", offset

            curTime = time.time()
            sinceLastSrmls= abs(curTime-lastTime)
            if sinceLastSrmls < 15: # dont be too agressive
                print "   Since last srmls", sinceLastSrmls,"- sleeping"
                time.sleep( int(15 - sinceLastSrmls) )
                print "   OK, back to work"
            proc = subprocess.Popen(command, stdout=subprocess.PIPE)
            lastTime = int(time.time())
            for line in iter(proc.stdout.readline,''):
                lineCnt += 1
                #print "XAQ", line.rstrip()
                l =  line.strip()
                fname = l.split("/")[-1]
                if not fname.endswith(".root"): continue
                goodRootFiles += 1 # this is a bit risky, since we may have other files in dir then rootfiles. TODO
                #print "Found", fname

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

            if lineCnt <= 1:
                if retryCnt == 8:
                    err = "Cannot get filelist for sample "+s+"\n"
                    err += " - if  some files were copied allready this probably means some server related problems."
                    err += " Please retry in couple of minutes. \n"  
                    err += " - if none of the files were copied please check your certificate proxy.\n"
                    raise Exception(err)

                retryCnt += 1
            else:
                break

        if goodRootFiles>0:
            offset += maxResults
        else:
            break


