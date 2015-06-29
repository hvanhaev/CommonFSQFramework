#!/usr/bin/env python
import sys,os,re, time

import ROOT
ROOT.gROOT.SetBatch(True)

from ROOT import *
ROOT.gSystem.Load("libFWCoreFWLite.so")
AutoLibraryLoader.enable()

from optparse import OptionParser
import subprocess

import CommonFSQFramework.Core.Util


def getFileListLcgLs(path):
    ret = []
    command = ["lcg-ls", path]
    proc = subprocess.Popen(command, stdout=subprocess.PIPE)
    cnt = 0
    for line in iter(proc.stdout.readline,''):
        l = line.strip()
        fname = l.split("/")[-1]
        if ".root" not in fname: continue
        srcFile = path + "/" + fname
        #targetFile = targetDir + "/" + fname
        ret.append(srcFile)

    return ret

def getFileListSrmLS(path):
    maxResults = 500
    offset = 0

    ret = []
    lastTime = 0
    cnt = 0
    while True: # handle maxResults results at a time
        command = ["srmls", "-2", "--offset", str(offset), "--count", str(maxResults),  path]
        retryCnt = 1
        goodRootFiles = 0
        # for current offset value obtain list of files.
        #    Try couple of times to handle empty output of srmls for some calls
        while True:
            lineCnt = 0
            print "Obtaining file list for", path, "- try", retryCnt, "offset", offset

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


                srcFile = path + "/" + fname
                #targetFile = targetDir + "/" + fname

                #print srcFile, targetFile
                cnt += 1

                
                #ret[srcFile]=targetFile
                ret.append(srcFile)

            if lineCnt <= 1:
                if retryCnt == 10:
                    err = "Cannot get filelist for  "+path+"\n"
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

    return ret


def checkRootFile(fp):
    while "//" in fp:
       fp = fp.replace("//","/")
    cmd = ["root", "-l", "-b", "-q", fp]
    #ret = subprocess.call(cmd)
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    while proc.poll() == None:
        time.sleep(1)

    errInStdout = False
    outData =""
    for line in proc.stdout:
        outData += line
        if "Error " in line:
            errInStdout = True
            break

    outData += "stderr::\n"
    for line in proc.stderr:
        outData += line
        if "Error " in line:
            errInStdout = True
            break

    if errInStdout:
        raise Exception("\nProblem processing call: "+" ".join(cmd)+ "\n\noutdata:\n\n" + outData)

    ret = proc.poll()
    return ret
    

def checkDataIntegrity(remove = False, checkFilesWithRoot = False):

    sampleList=CommonFSQFramework.Core.Util.getAnaDefinition("sam")
    for s in sampleList:
        todo = []
        if "pathTrees" in sampleList[s]:
            todo.append(sampleList[s]["pathTrees"])
        if "pathPAT" in sampleList[s]:
            todo.append(sampleList[s]["pathPAT"])

        if len(todo)>0:
            print "Doing", s
        else:
            print "No files found for sample", s, ",skipping"
            continue
        
        for t in todo:
            fileMap = {}
            for root, dirs, files in os.walk(t):
                for f in files:
                    fp = root + "/" + f
                    if not f.endswith(".root"):
                        print "Non root file:", fp
                        continue
                    spl = f.split("_")
                    try:
                        fileNum = int(spl[1])
                    except:
                        print "Error processing", fp,"- skipping"
                        continue

                    while "//" in fp:
                        fp = fp.replace("//","/")

                    if checkFilesWithRoot:
                        ret = checkRootFile(fp)
                        if ret != 0:
                            print "Bad file:", fp
                            continue

                    # root -l -b -q
                    fsize = os.path.getsize(fp)
                    if fsize == 0:
                        print "Empty file:", fp
                        if remove:
                            os.system("rm "+fp)
                    else:
                        fileMap.setdefault(fileNum, []).append(fp)
                    #print f

            for num in fileMap:
                if len(fileMap[num]) > 1:
                    print "Multiple files:", s, num, "-", len(fileMap[num])
                    for f in fileMap[num][:]:
                        #ret = 0
                        ret = checkRootFile(f)
                        if ret != 0:
                            print "Bad file:", f
                            if remove:
                                os.system("rm "+f)
                                filemap[num].remove(f)

                    if len(fileMap[num]) > 1: # after root file check
                        biggestFile = ""
                        biggestFileSize = 0
                        for f in fileMap[num]:
                            fsize = os.path.getsize(f)
                            if fsize > biggestFileSize:
                                biggestFileSize = fsize
                                biggestFile = f

                        for f in fileMap[num]:
                            if f == biggestFile:
                                continue
                            else:
                                print "Will remove", f
                                if remove:
                                    os.system("rm "+f)
                        

                        
                        
                            


        


def main():
    sampleList=CommonFSQFramework.Core.Util.getAnaDefinition("sam")

    parser = OptionParser(usage="usage: %prog [options] filename",
                            version="%prog 1.0")

    parser.add_option("-p", "--doPat", action="store_true", dest="pat")
    parser.add_option("-t", "--doTrees", action="store_true",  dest="trees")
    parser.add_option("-c", "--checkDataIntegrity", action="store_true",  dest="check")
    parser.add_option("-d", "--deleteBadFiles", action="store_true",  dest="remove")
    parser.add_option("-r", "--rootCheck", action="store_true",  dest="checkFilesWithRoot")
    parser.add_option("-s", "--srmls", action="store_true",  dest="usesrmls")
    parser.add_option("-m", "--maxFilesMC", action="store",  type="int", dest="maxFilesMC")
    (options, args) = parser.parse_args()

    maxFilesMC = -1
    if options.maxFilesMC:
        maxFilesMC = options.maxFilesMC


    if options.check:
        remove = False
        checkFilesWithRoot = False
        if options.remove: remove = True
        if options.checkFilesWithRoot: checkFilesWithRoot = options.checkFilesWithRoot
        
        checkDataIntegrity(remove, checkFilesWithRoot)
        sys.exit(0)

    doPAT = False
    doTrees = False

    if options.pat :
        doPAT = True
    elif options.trees:
        doTrees = True

    if not doPAT and not doTrees:
        print "Nothing to do. Run me with '-t' option to copy trees from current skim"
        sys.exit()
	

    #333
    myprocs = []
    for s in sampleList:
        if "pathSE" not in sampleList[s]:
            print "No SE path found for sample", s

        try:
            todo = [sampleList[s]["pathPAT"], sampleList[s]["pathTrees"]]
            for d in todo:
	        if "eos/cms" in d:
		    os.system("xrd eoscms mkdir -p " + d)
		    #print " would create dir: xrd eoscms mkdir -p ", d
		else:
                    os.system("mkdir -p "+ d)
		    #print " would create dir:", d
                    if not os.path.isdir(d):
                        raise Exception("Cannot create output dir "+d)
                        continue
        except:
            continue

        # TODO: check dir existence



        # on my installation lcg-ls does not have offset/count params
        # needed for srm access to dirs with >1000 files.
        
#command = ["lcg-ls", sampleList[s]["pathSE"]]
        if options.usesrmls:
            flist = getFileListSrmLS(sampleList[s]["pathSE"])
        else:
            flist = getFileListLcgLs(sampleList[s]["pathSE"])
        cnt = 0
        for srcFile in flist:
            fname = srcFile.split("/")[-1]
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
            cnt += 1
            targetFile = targetDir + "/" + fname
            if not sampleList[s]["isData"] and maxFilesMC >= 0 and cnt >= maxFilesMC:
                continue

            if "eos/cms" in targetDir:
	        cpCommand = ['lcg-cp', srcFile, "srm://srm-eoscms.cern.ch/"+targetFile]
	    else:
                cpCommand = ['lcg-cp', srcFile, targetFile]
            
	    #cpCommand = ['lcg-ls', srcFile]
	    #print "would be cpCommand: ", cpCommand
            
	    if "eos/cms" not in targetDir and os.path.isfile(targetFile):
                print "Allready present", typeString, fname, " #"+str(cnt), "from", s
                continue

            print "Copying", typeString, fname, " #"+str(cnt), "from", s

            myproc = subprocess.Popen(cpCommand)
            myprocs.append( (myproc, cpCommand) ) 
            while len(myprocs) > 3:
                time.sleep(1)
                for p in myprocs[:]:
                    exitCode = p[0].poll()
                    #print exitCode, p[1]
                    if exitCode != None:
                        if exitCode != 0:
                            print "Problem with ", p[1]
                        myprocs.remove(p)

    while len(myprocs) > 0:
        time.sleep(1)
        for p in myprocs[:]:
            exitCode = p[0].poll()
            #print exitCode, p[1]
            if exitCode != None:
                if exitCode != 0:
                    print "Problem with ", p[1]
                myprocs.remove(p)

            
    ###


if __name__ == "__main__":
    main()
