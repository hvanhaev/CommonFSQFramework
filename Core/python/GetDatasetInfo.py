#!/usr/bin/env python
import sys,os,re,imp

import ROOT
ROOT.gROOT.SetBatch(True)

from ROOT import *
import CommonFSQFramework.Core.Util
import time
from multiprocessing import Process, Queue

import pickle
import subprocess



def validateRootFile(fname, q, CFFTreeName=""):
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
    if CFFTreeName != "":
        cff = rootFile.Get(CFFTreeName + "/data")
        if (ret["evCnt"] != cff.GetEntries()):
            print ("validation error for" + fname + str(ret["evCnt"]) + " " + str(cff.GetEntries()))
        del cff
    rootFile.Close()
    del rootFile
    return q.put(ret)



def validateRootFiles(fileListUnvalidated, maxFiles=None, quiet = False, CFFTreeName=""):
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
        thr = Process(target=validateRootFile, args=(fname, q, CFFTreeName))
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



def getTreeFilesAndNormalizations(maxFilesMC = None, maxFilesData = None, quiet = False, samplesToProcess = None, usePickle=False, donotvalidate=True):
    # in principle we should check if lcg-ls supports -c/ -o argumets
    legacyMode = False
    if "SCRAM_ARCH" in  os.environ:
        legacyMode = "slc5" in os.environ["SCRAM_ARCH"] 
        if legacyMode:
            print "Warning - running in legacy mode. Access to remote directories with more than 1000 files wont be possible"
            print "CHECK, if this is really true for gfal-ls !! "

    if usePickle and donotvalidate:
        print ("Cannot go this way (usePickle and donotvalidate)")
        sys.exit(1)

    localBasePathTrees, localBasePathPAT, ROOTPrefix = CommonFSQFramework.Core.Util.readAnaConfig()
    if "..none.." in ROOTPrefix:
        print ("Please note you need to provide a (new) ROOTPrefix  parameter inside SmallXAnaDefFile. " \
                   + "See CommonFSQFramework.Core/doc/SmallXAnaDefFile.txt for details")
        sys.exit(1)

    isXrootdAccess = False
    if "xrootd" in ROOTPrefix: isXrootdAccess = True
    if "xrd" in ROOTPrefix: isXrootdAccess = True
    localAccess = not isXrootdAccess

    samplesFileDir = os.path.dirname(CommonFSQFramework.Core.Util.getFullPathToAnaDefinitionFile())+"/"

    sampleList=CommonFSQFramework.Core.Util.getAnaDefinition("sam")
    if samplesToProcess != None:
        newList = {}
        for s in samplesToProcess:
            if s not in sampleList:
                print ("Requested sample "+s+ " not known")
                sys.exit(1)
            newList[s]=sampleList[s]
        sampleList = newList

    anaVersion = CommonFSQFramework.Core.Util.getAnaDefinition("anaVersion")
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

        fileListUnvalidated = set()
        if localAccess:

            if "pathTrees" not in sampleList[s]:
                if not quiet: print tab, "path to trees not found! Blame the skim-responsible-guy."
                writePickle = False

            if not quiet: print tab, "path to local trees:",sampleList[s]["pathTrees"]
            if not quiet: print tab, "path to trees taken from 'sampleList[s][\"pathTrees\"]' variable"
            if not "eos/cms" in sampleList[s]["pathTrees"]:
                for dirpath, dirnames, filenames in os.walk(sampleList[s]["pathTrees"]):
                    if "fail" in dirpath: continue
                    if "/log" in dirpath == 0: continue
                    for f in filenames:
                        if "fail" in f: continue
                        if not f.startswith("trees"): continue
                        if not f.endswith(".root"): continue
                        fname = dirpath.replace("//","/").rstrip('/') + '/' + f   # somehow root doesnt like // at the begining
                        fileListUnvalidated.add(ROOTPrefix+fname)
            else: # if "eos/cms" in sampleList[s]["pathTrees"]:
                if not  distutils.spawn.find_executable("xrd"):   # only works on lxplus...
                    print ("Cannot find xrd executable. You may need to run this on lxplus!")
                    sys.exit(1)
                lscomm = ["xrd", "eoscms", "ls", sampleList[s]["pathTrees"]]
                proc = subprocess.Popen(lscomm, stdout=subprocess.PIPE)
                for line in iter(proc.stdout.readline,''):
                    ifile = line.strip()
                    if "fail" in ifile: continue
                    if "trees" not in ifile: continue
                    if ".root" not in ifile: continue
                    filename = ifile.split("//")[-1]
                    fileListUnvalidated.add("root://eoscms/"+sampleList[s]["pathTrees"]+filename)

        elif isXrootdAccess:
            if not quiet: print tab, "will access trees from:",sampleList[s]["pathSE"]
            pathSE = sampleList[s]["pathSE"]
            fileListUnvalidatedSE = CommonFSQFramework.Core.Util.getFileListGFAL(pathSE)
            for fname in fileListUnvalidatedSE:
                if ".root" not in fname: continue
                if "trees" not in fname: continue
                srcFile = pathSE + "/" + fname
                if "/store/" not in srcFile:
                    print ("Cannot convert to lfn:", srcFile)
                    sys.exit(1)
                lfn = "/store/" + srcFile.split("/store/")[-1]
                fileListUnvalidated.add(ROOTPrefix+lfn)
        else:
            print ("Thats confusing! File access method undetermined!")
            sys.exit(1)

        print "Total number of (unvalidated) files in sample:", len(fileListUnvalidated)
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
        if len(fileListUnvalidated) > 0:
            treeName = ""
            #if localAccess and "treeName" in sampleList[s]:
            #    treeName = sampleList[s]["treeName"]
            validationResult = validateRootFiles(fileListUnvalidated, maxFiles, CFFTreeName=treeName)
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
    getTreeFilesAndNormalizations(maxFilesMC = None, maxFilesData = None, usePickle=True, donotvalidate=True)
    #sam = getTreeFilesAndNormalizations(maxFilesMC = None, maxFilesData = None, donotvalidate = True)
    #for s in sam:
    #    print s
    #getTreeFilesAndNormalizations(maxFilesMC = 10, maxFilesData = 10)


