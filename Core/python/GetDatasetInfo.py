#!/usr/bin/env python
import sys,os,re,imp

import ROOT
ROOT.gROOT.SetBatch(True)

from ROOT import *
ROOT.gSystem.Load("libFWCoreFWLite.so")
AutoLibraryLoader.enable()
import CommonFSQFramework.Core.Util
import time
from multiprocessing import Process, Queue

import pickle
import distutils.spawn
import subprocess

def validateRootFile(fname, q):
    rootFile = ROOT.TFile.Open(fname,"r")
    infoHisto = rootFile.Get("infoHisto/cntHisto")
    ret = {}
    ret["evCnt"]=-1
    ret["evCntSeenByTreeProducers"]=-1
    
    if type(infoHisto) != ROOT.TH1D:
        print "\nProblem reading info histo from", fname
    elif infoHisto.GetXaxis().GetBinLabel(3)!="evCnt":
        if not quiet: print "\nProblem - evCnt bin expected at position 3. Got",  infoHisto.getBinLabel(3)
    else:
        ret["evCnt"]  =  int(infoHisto.GetBinContent(3))
    if  infoHisto.GetXaxis().GetBinLabel(4)=="evCntSeenByTreeProducers":
        ret["evCntSeenByTreeProducers"] =  int(infoHisto.GetBinContent(4))

    del infoHisto
    rootFile.Close()
    del rootFile
    return q.put(ret)

def validateRootFiles(fileListUnvalidated, maxFiles=None, quiet = False):
    if not quiet: print "Validating",
    # verify we are able to read event counts from very file
    fileCnt = 0
    threads = {}
    goodFiles = 0
    maxThreads= 12
    fileList = []
    evCnt = 0
    evCntSeenByTreeProducers = 0
    if maxFiles != None:
        maxThreads  = min(maxThreads, maxFiles/2+1, len(fileListUnvalidated))

    for fname in fileListUnvalidated:
        if maxFiles != None and goodFiles >= maxFiles:
            break
        fileCnt += 1
        if (fileCnt%50 == 0):
            if not quiet: sys.stdout.write(str(int(100.*fileCnt/len(fileListUnvalidated)))+"%")
        else:
            if not quiet: sys.stdout.write('.')


        q = Queue()               
        thr = Process(target=validateRootFile, args=(fname, q))
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
                    if threads[t][2]["evCnt"] > 0:
                        goodFiles+=1

            if waitingOrRunning > maxThreads:
                time.sleep(1)
            else:
                break

    if not quiet: print "" # EOL
    fileCnt = 0
    for t in threads:
        if threads[t][2]==None:
            threads[t][0].join()
            threads[t][2] = threads[t][1].get()
        result = threads[t][2]["evCnt"] 
        resEvCntSeenByTreeProducers = threads[t][2]["evCntSeenByTreeProducers"]
        if result < 0:
            print "Problematic file", t
            continue
        elif result == 0:
            print "Warning: 0 ev file", t

        fileList.append(t)
        if result > 0:
            evCnt += result

        if resEvCntSeenByTreeProducers > 0:
            evCntSeenByTreeProducers+=resEvCntSeenByTreeProducers
        fileCnt += 1
        if maxFiles != None and fileCnt >= maxFiles:
            break

    validationResult = {}
    validationResult["fileList"]=fileList
    validationResult["evCnt"]=evCnt
    validationResult["evCntSeenByTreeProducers"]=evCntSeenByTreeProducers
    return validationResult


def getTreeFilesAndNormalizations(maxFilesMC = None, maxFilesData = None, quiet = False, samplesToProcess = None, usePickle=False, donotvalidate=False):
    # in principle we should check if lcg-ls supports -c/ -o argumets
    legacyMode = "slc5" in os.environ["SCRAM_ARCH"] 
    if legacyMode:
        print "Warning - running in legacy mode. Access to remote directories with more than 1000 files wont be possible"


    if usePickle and donotvalidate:
        raise Exception("Cannot go this way (usePickle and donotvalidate)")

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
                         +"See CommonFSQFramework.Core/doc/SmallXAnaDefFile.txt for details")

    localROOTPrefix = mod.ROOTPrefix
    isXrootdAccess = False
    if "xrootd" in localROOTPrefix: isXrootdAccess = True
    if "xrd" in localROOTPrefix: isXrootdAccess = True
    localAccess = not isXrootdAccess
    if isXrootdAccess:
        if not  distutils.spawn.find_executable("lcg-ls"):
            raise Exception("Cannot find lcg-ls executable. Check your grid environment!")


    samplesFileDir = os.path.dirname(CommonFSQFramework.Core.Util.getFullPathToAnaDefinitionFile())+"/"

    sampleList=CommonFSQFramework.Core.Util.getAnaDefinition("sam")
    if samplesToProcess != None:
        newList = {}
        for s in samplesToProcess:
            if s not in sampleList:
                raise Exception("Requested sample "+s+ " not known")
            newList[s]=sampleList[s]
        sampleList = newList

    anaVersion=CommonFSQFramework.Core.Util.getAnaDefinition("anaVersion")

    if not quiet: print "printing info for: ",  anaVersion

    ret = {}
    tab = "     "
    for s in sampleList:
        maxFiles = maxFilesData
        if not sampleList[s]["isData"]:
            maxFiles = maxFilesMC

        ret[s] = {}
        pickleName = samplesFileDir+"cache_"+anaVersion+"_"+s+".pkl"
        fromPickle = False
        writePickle = True
        if not quiet: print "#"*120
        if not quiet: print "Found sample:", s
        if not quiet: print tab,"dataset:",sampleList[s]["DS"]
        if not quiet: print tab, "xsection:",sampleList[s]["XS"] # note you can also fetch this from tree files (bin 2 in info histo)
        evCnt = 0
        evCntSeenByTreeProducers = 0
        fileList = []
        if "pathTrees" not in sampleList[s]:
            # TODO: should this be in localAccess part?
            if not quiet: print tab, "path to trees not found! Blame the skim-responsible-guy."
            writePickle = False
        else:
            fileListUnvalidated = set()
            if localAccess:
                if not quiet: print tab, "path to trees:",sampleList[s]["pathTrees"]
                if not quiet: print tab, "path to trees taken from 'sampleList[s][\"pathTrees\"]' variable"
		if not "eos/cms" in sampleList[s]["pathTrees"]:
                    for dirpath, dirnames, filenames in os.walk(sampleList[s]["pathTrees"]):
                        for f in filenames:
                            if not f.startswith("trees_"): continue
                            if not f.endswith(".root"): continue
                            fname = dirpath.replace("//","/") + f   # somehow root doesnt like // at the begining
                            fileListUnvalidated.add(localROOTPrefix+fname)
		if "eos/cms" in sampleList[s]["pathTrees"]:
		    # only works on lxplus...
		    lscomm = ["xrd", "eoscms", "ls", sampleList[s]["pathTrees"]]
		    proc = subprocess.Popen(lscomm, stdout=subprocess.PIPE)
		    for line in iter(proc.stdout.readline,''):
		        ifile = line.strip()
			if "trees_" not in ifile: continue
			if ".root" not in ifile: continue
			filename = ifile.split("//")[-1]
			fileListUnvalidated.add("root://eoscms/"+sampleList[s]["pathTrees"]+filename)
			
            elif isXrootdAccess:
                if not quiet: print tab, "will access trees from:",sampleList[s]["pathSE"]
                # Warning: duplicated from copyAnaData. Fixme
                pathSE = sampleList[s]["pathSE"]
                cnt = 999
                offset = 0
                lastSize = len(fileListUnvalidated)
                while True:
                    if legacyMode:
                        command = ["lcg-ls", pathSE]
                    else:
                        command = ["lcg-ls", "-c", str(cnt), "-o", str(offset), pathSE]
                    proc = subprocess.Popen(command, stdout=subprocess.PIPE)
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
                        fileListUnvalidated.add(localROOTPrefix+lfn)

                    if lastSize !=  len(fileListUnvalidated):
                        lastSize = len(fileListUnvalidated)
                        offset+=cnt
                    else:
                        break
                    if legacyMode:
                        break

            else:
                raise Exception("Thats confusing! File access method undetermined!")

            print "Total number of files in sample:", len(fileListUnvalidated)
            if donotvalidate:
                fileList = list(fileListUnvalidated) 
                evCnt = 0
                fileListUnvalidated = set()

            if maxFiles == None and usePickle: 
                if os.path.isfile(pickleName):
                    pkl_file = open(pickleName, 'rb')
                    pickledData = pickle.load(pkl_file)
                    if set(pickledData["files"])!=set(fileListUnvalidated):
                        print "File list from pickled file and unvalidated list of files different"
                        print "Broken (?) pickle file", pickleName
                    else:
                        print "Cached data from", pickleName
                        fileListUnvalidated = set()  # Q&D - disable validation. 
                        fileList = pickledData["files"]
                        evCnt =  pickledData["evCnt"]
                        evCntSeenByTreeProducers = pickledData["evCntSeenByTreeProducers"]
                        fromPickle = True

            # xxxx
            if fileListUnvalidated:
                validationResult = validateRootFiles(fileListUnvalidated, maxFiles)
                fileList =  validationResult["fileList"]
                evCnt = validationResult["evCnt"]
                evCntSeenByTreeProducers = validationResult["evCntSeenByTreeProducers"]

        if writePickle and not fromPickle and  maxFiles == None and usePickle: 
            toPickle = {}
            toPickle["files"] = fileList
            toPickle["evCnt"] = evCnt
            toPickle["evCntSeenByTreeProducers"] = evCntSeenByTreeProducers

            # pickleName
            outputPickle = open(pickleName, 'wb')
            pickle.dump(toPickle, outputPickle)
            outputPickle.close()


        if not quiet: print tab, "number of tree files:", len(fileList)
        if not quiet: print tab, "events processed in skim:", evCnt # in agreement with crab xml output
        if not quiet: print tab, "list of files for this ds saved in 'fileList' variable "
        if evCnt == 0:
            normFactor = -1
            if not quiet: print "Event count equals zero. Cowardly refusing to calculate normalization factor"
        else:
            normFactor = sampleList[s]["XS"]/evCnt
            if not quiet: print tab, "Normalization factor is ", normFactor
            if not quiet: print tab, "[xcheck] number of events passed to tree producers (ie when running on AOD):", evCntSeenByTreeProducers
        ret[s]["files"] = fileList
        ret[s]["normFactor"] = normFactor

    return ret

if __name__ == "__main__":
    getTreeFilesAndNormalizations(maxFilesMC = None, maxFilesData = None, usePickle=True)
    #sam = getTreeFilesAndNormalizations(maxFilesMC = None, maxFilesData = None, donotvalidate = True)
    #for s in sam:
    #    print s
    #getTreeFilesAndNormalizations(maxFilesMC = 10, maxFilesData = 10)


