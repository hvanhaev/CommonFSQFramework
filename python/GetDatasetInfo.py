#!/usr/bin/env python
import sys,os,re

import ROOT
ROOT.gROOT.SetBatch(True)

from ROOT import *
ROOT.gSystem.Load("libFWCoreFWLite.so")
AutoLibraryLoader.enable()


import MNTriggerStudies.MNTriggerAna.Util

sampleList=MNTriggerStudies.MNTriggerAna.Util.getAnaDefinition("sam")
anaVersion=MNTriggerStudies.MNTriggerAna.Util.getAnaDefinition("anaVersion")

# TODO: control verbosity
def getTreeFilesAndNormalizations(maxFiles = None):
    print "Printing info for: ",  anaVersion

    ret = {}
    tab = "     "
    for s in sampleList:
        ret[s] = {}
        print "#"*120
        print "Found sample:", s
        print tab,"dataset:",sampleList[s]["DS"]
        print tab, "xsection:",sampleList[s]["XS"] # note you can also fetch this from tree files (bin 2 in info histo)
        evCnt = 0
        fileList = []
        if "pathTrees" not in sampleList[s]:
            print tab, "path to trees not found! Blame the skim-responsible-guy."
        else:
            #print tab, "path to trees:",sampleList[s]["pathTrees"]
            print tab, "path to trees taken from 'sampleList[s][\"pathTrees\"]' variable"

            fileCnt = 0
            for dirpath, dirnames, filenames in os.walk(sampleList[s]["pathTrees"]):
                for f in filenames:
                    if maxFiles != None and fileCnt >= maxFiles:
                        break # we dont need more

                    if not f.startswith("trees_"): continue
                    if not f.endswith(".root"): continue
                    fname = dirpath.replace("//","/") + f   # somehow root doesnt like // at the begining
                    rootFile = ROOT.TFile(fname,"r")
                    infoHisto = rootFile.Get("infoHisto/cntHisto")
                    if type(infoHisto) != ROOT.TH1D:
                        print "Problem reading info histo from", fname
                        continue


                    if infoHisto.GetXaxis().GetBinLabel(3)!="evCnt":
                        print "Problem - evCnt bin expected at position 3. Got",  infoHisto.getBinLabel(3)
                        continue

                    fileCnt += 1
                    fileList.append(fname)
                    evCnt += int(infoHisto.GetBinContent(3))
        print tab, "number of tree files:", len(fileList)
        print tab, "events processed in skim:", evCnt # in agreement with crab xml output
        print tab, "list of files for this ds saved in 'fileList' variable "
        if evCnt == 0:
            normFactor = -1
            print "Event count equals zero. Cowardly refusing to calculate normalization factor"
        else:
            normFactor = sampleList[s]["XS"]/evCnt
            print tab, "Normalization factor is ", normFactor
        ret[s]["files"] = fileList
        ret[s]["normFactor"] = normFactor

    return ret

if __name__ == "__main__":
    getTreeFilesAndNormalizations()


