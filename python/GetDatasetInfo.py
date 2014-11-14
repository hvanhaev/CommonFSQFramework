#!/usr/bin/env python
import sys,os,re,imp

import ROOT
ROOT.gROOT.SetBatch(True)

from ROOT import *
ROOT.gSystem.Load("libFWCoreFWLite.so")
AutoLibraryLoader.enable()
import MNTriggerStudies.MNTriggerAna.Util
import time
from multiprocessing import Process, Queue


def getTreeFilesAndNormalizations(maxFilesMC = None, maxFilesData = None, quiet = False, samplesToProcess = None):

    # TODO: SmallXAnaDefFile access function in Util
    if "SmallXAnaDefFile" not in os.environ:
        print "Please set SmallXAnaDefFile environment variable:"
        print "export SmallXAnaDefFile=FullPathToFile"
        raise Exception("Whooops! SmallXAnaDefFile env var not defined")

    anaDefFile = os.environ["SmallXAnaDefFile"]
    mod_dir, filename = os.path.split(anaDefFile)
    mod, ext = os.path.splitext(filename)
    f, filename, desc = imp.find_module(mod, [mod_dir])
    mod = imp.load_module(mod, f, filename, desc)

    localBasePathPAT = mod.PATbasePATH
    localBasePathTrees = mod.TTreeBasePATH
    if not hasattr(mod, "ROOTPrefix"):
        raise Exception("Please note you need to provide a (new) ROOTPrefix  parameter inside SmallXAnaDefFile. " \
                         +"See MNTriggerStudies/MNTriggerAna/doc/SmallXAnaDefFile.txt for details")

    localROOTPrefix = mod.ROOTPrefix
    isXrootdAccess = "xrootd" in localROOTPrefix
    localAccess = not isXrootdAccess

    sampleList=MNTriggerStudies.MNTriggerAna.Util.getAnaDefinition("sam")
    if samplesToProcess != None:
        newList = {}
        for s in samplesToProcess:
            if s not in sampleList:
                raise Exception("Requested sample "+s+ " not known")
            newList[s]=sampleList[s]
        sampleList = newList

    anaVersion=MNTriggerStudies.MNTriggerAna.Util.getAnaDefinition("anaVersion")

    if not quiet: print "if not quiet: printing info for: ",  anaVersion

    ret = {}
    tab = "     "
    for s in sampleList:
        ret[s] = {}
        if not quiet: print "#"*120
        if not quiet: print "Found sample:", s
        if not quiet: print tab,"dataset:",sampleList[s]["DS"]
        if not quiet: print tab, "xsection:",sampleList[s]["XS"] # note you can also fetch this from tree files (bin 2 in info histo)
        evCnt = 0
        fileList = []
        if "pathTrees" not in sampleList[s]:
            # TODO: should this be in localAccess part?
            if not quiet: print tab, "path to trees not found! Blame the skim-responsible-guy."
        else:

            # local access start

            fileListUnvalidated = []
            if localAccess:
                if not quiet: print tab, "path to trees:",sampleList[s]["pathTrees"]
                if not quiet: print tab, "path to trees taken from 'sampleList[s][\"pathTrees\"]' variable"
                for dirpath, dirnames, filenames in os.walk(sampleList[s]["pathTrees"]):
                    for f in filenames:

                        if not f.startswith("trees_"): continue
                        if not f.endswith(".root"): continue
                        fname = dirpath.replace("//","/") + f   # somehow root doesnt like // at the begining
                        fileListUnvalidated.append(localROOTPrefix+fname)
            elif isXrootdAccess:
                if not quiet: print tab, "will access trees from:",sampleList[s]["pathSE"]
                # Warning: duplicated from copyAnaData. Fixme
                import subprocess
                pathSE = sampleList[s]["pathSE"]
                command = ["lcg-ls", pathSE]
                proc = subprocess.Popen(command, stdout=subprocess.PIPE)
                cnt = 0
                for line in iter(proc.stdout.readline,''):
                    l = line.strip()
                    fname = l.split("/")[-1]
                    if ".root" not in fname: continue
                    if "trees_" not in fname: continue
                    srcFile = pathSE + "/" + fname
                    if "/store/" not in srcFile:
                        raise "Cannot convert to lfn:", srcFile
                    lfn = "/store/"+srcFile.split("/store/")[-1]

                    #targetFile = targetDir + "/" + fname
                    fileListUnvalidated.append(localROOTPrefix+lfn)
            else:
                raise Exception("Thats confusing! File access method undetermined!")

            # verify we are able to read event counts from very file
            maxFiles = maxFilesData
            if not sampleList[s]["isData"]:
                maxFiles = maxFilesMC
            fileCnt = 0
            threads = {}
            goodFiles = 0
            print "Total number of files in sample:", len(fileListUnvalidated)
            print "Validating",
            maxThreads= 12
            if maxFiles != None:
                maxThreads  = min(maxThreads, maxFiles/2+1)

            for fname in fileListUnvalidated:
                if maxFiles != None and goodFiles >= maxFiles:
                    break
                fileCnt += 1
                if (fileCnt%50 == 0):
                    sys.stdout.write(str(int(100.*fileCnt/len(fileListUnvalidated)))+"%")
                else:
                    sys.stdout.write('.')

                def validate(fname, q):
                    rootFile = ROOT.TFile.Open(fname,"r")
                    infoHisto = rootFile.Get("infoHisto/cntHisto")
                    ret = -1
                    if type(infoHisto) != ROOT.TH1D:
                        print "\nProblem reading info histo from", fname
                    elif infoHisto.GetXaxis().GetBinLabel(3)!="evCnt":
                        if not quiet: print "\nProblem - evCnt bin expected at position 3. Got",  infoHisto.getBinLabel(3)
                    else:
                        ret =  int(infoHisto.GetBinContent(3))
                    del infoHisto
                    rootFile.Close()
                    del rootFile
                    return q.put(ret)

                q = Queue()               
                thr = Process(target=validate, args=(fname, q))
                thr.start()
                threads[fname] = [thr, q, None]

                while True:
                    waitingOrRunning = 0 
                    goodFiles = 0
                    for t in threads:
                        #if not threads[t][0].ident or  threads[t][0].is_alive():
                        if threads[t][0].exitcode == None:
                            waitingOrRunning+=1
                        else:
                            if threads[t][2] == None:
                                threads[t][0].join()
                                threads[t][2] = threads[t][1].get()
                            if threads[t][2] > 0:
                                goodFiles+=1

                    if waitingOrRunning > maxThreads:
                        time.sleep(1)
                    else:
                        break

            print "" # EOL
            fileCnt = 0
            for t in threads:
                if threads[t][2]==None:
                    threads[t][0].join()
                    threads[t][2] = threads[t][1].get()
                result = threads[t][2] 
                if result <= 0:
                    print "Problematic file", t
                    continue
                fileList.append(t)
                evCnt += result
                fileCnt += 1
                if maxFiles != None and fileCnt >= maxFiles:
                    print tab, "will process", fileCnt, "files"
                    break


        if not quiet: print tab, "number of tree files:", len(fileList)
        if not quiet: print tab, "events processed in skim:", evCnt # in agreement with crab xml output
        if not quiet: print tab, "list of files for this ds saved in 'fileList' variable "
        if evCnt == 0:
            normFactor = -1
            if not quiet: print "Event count equals zero. Cowardly refusing to calculate normalization factor"
        else:
            normFactor = sampleList[s]["XS"]/evCnt
            if not quiet: print tab, "Normalization factor is ", normFactor
        ret[s]["files"] = fileList
        ret[s]["normFactor"] = normFactor

    return ret

if __name__ == "__main__":
    getTreeFilesAndNormalizations(maxFilesMC = None, maxFilesData = None)
    #getTreeFilesAndNormalizations(maxFilesMC = 10, maxFilesData = -10)


