#!/usr/bin/env python
import sys,os,re,time, imp

import ROOT
ROOT.gROOT.SetBatch(True)

from ROOT import *
ROOT.gSystem.Load("libFWCoreFWLite.so")
AutoLibraryLoader.enable()

from optparse import OptionParser
import subprocess

import CommonFSQFramework.Core.Util

def getFileListLs(path):
    ret = []
    command = ["ls", path]
    proc = subprocess.Popen(command, stdout=subprocess.PIPE)
    cnt = 0
    for line in iter(proc.stdout.readline,''):
        l = line.strip()
        fname = l.split("/")[-1]

        if "SmallXAnaDefFile" not in os.environ:
            print "Please set SmallXAnaDefFile environment variable:"
            print "export SmallXAnaDefFile=FullPathToFile"
            raise Exception("Whoops! SmallXAnaDefFile env var not defined")

        anaDefFile = os.environ["SmallXAnaDefFile"]
        mod_dir, filename = os.path.split(anaDefFile)
        mod, ext = os.path.splitext(filename)
        f, filename, desc = imp.find_module(mod, [mod_dir])
        mod = imp.load_module(mod, f, filename, desc)

        localBasePathTrees = mod.TTreeBasePATH

        if "pathTrees" in path:
            path = path.replace("XXXTMFTTree", localBasePathTrees)




        if ".root" not in fname: continue
        srcFile = path + "/" + fname
        ret.append(srcFile)

    return ret

        


def main():
    sampleList=CommonFSQFramework.Core.Util.getAnaDefinition("sam")

    parser = OptionParser(usage="usage: %prog [options] filename",
                            version="%prog 1.0")

    parser.add_option("-d", "--destination", action="store",  type="string", dest="destinationDirectory")
    parser.add_option("-f", "--forceOverwrite", action="store_true", dest="forceOverwrite")

    (options, args) = parser.parse_args()
    doTrees = True

    if not options.destinationDirectory:
        print "Nothing to do. Run me with '-d /full/path/to/destination/directory' option to merge trees from current skim"
        sys.exit()

    if options.destinationDirectory:
        os.system("mkdir -p "+ options.destinationDirectory)
        if not os.path.isdir(options.destinationDirectory):
            raise Exception("Cannot create destination directory "+options.destinationDirectory)

    iSample = 0
    myprocs = []
    for s in sampleList:
        if "pathTrees" not in sampleList[s]:
            print "No Trees path found for sample", s
        iSample += 1
        appendString = "_sam" + str(iSample)
        flist = getFileListLs(sampleList[s]["pathTrees"])
        cnt = 0
        for srcFile in flist:
            fname = srcFile.split("/")[-1]
            fname = fname.split(".")[-2]
            fname += appendString
            fname += ".root"

            treeFile = "trees_" in fname

            doCopy = False

            if treeFile and doTrees:
                doCopy = True
                targetDir = options.destinationDirectory
                typeString = "treeFile"

            if not doCopy: continue
            cnt += 1
            targetFile = targetDir + "/" + fname

            cpCommand = ['cp', srcFile, targetFile]
            if os.path.isfile(targetFile):
                print "Already present", typeString, fname, " #"+str(cnt), "from", s
                continue

            print "Making copy in merged directory", typeString, fname, " #"+str(cnt), "from", s

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



    #Define paths for current and new dictionary file
    thisScript_path = os.path.abspath(__file__)
    thisScript_path_list = thisScript_path.split('/')
    base_path = ''
    smallXAnaVersion = os.environ['SmallXAnaVersion']
    smallXAnaVersion_path = smallXAnaVersion.replace('.', '/')
    smallXAnaVersion_path = smallXAnaVersion_path.replace('/Skim/', '/Skim/python/')
    smallXAnaVersion_path += '.py'

    for index, folder in enumerate(thisScript_path_list):
	if index < (len(thisScript_path_list) - 3 ):
	    base_path += folder+'/'

    dictionary_path = base_path + "src/" + smallXAnaVersion_path
    smallXAnaVersion_path = smallXAnaVersion_path.replace('.py', '_merged.py')
    new_dictionary_path = base_path + "src/" + smallXAnaVersion_path

    inFile = open(dictionary_path, 'r')

    if options.forceOverwrite:
        outFile = open(new_dictionary_path, 'w')
    else:
	if os.path.isfile(new_dictionary_path):
	    print "There is already a dictionary file at", new_dictionary_path
	    print "Run me with -f option to force overwriting it."
	    sys.exit()
	else:
	    outFile = open(new_dictionary_path, 'w')

    nEvents = 0
    lumi = 0
    for s in sampleList:
        nEvents += sampleList[s]["numEvents"]
	lumi += sampleList[s]["lumiMinBias"]

    bracketCount = 0
    commentedLine = False
    atEpilogue = False

    #Rewrite dictionary file, only using information from the first sample.
    for line in inFile:
	if line.strip().startswith("#"):
	    commentedLine = True
	else:
	    commentedLine = False
	if "fixLocalPaths" in line:
	    atEpilogue = True
	if atEpilogue:
	    outFile.write(line)
	    continue

	if "{" in line and not commentedLine: bracketCount += 1

        if not "sam[" in line:
            outFile.write(line)

	if (bracketCount == 1 or bracketCount == 2) and "sam[" in line:
	    if "numEvents" in line:
		line = line.split("=")[0]
		outFile.write(line + "=" + str(nEvents) + '\n')
	    elif "lumiMinBias" in line:
		line = line.split("=")[0]
		outFile.write(line + "=" + str(lumi) + '\n')
	    elif "pathTrees" in line:
		line = line.split("=")[0]
		outFile.write(line + '=\'' + targetDir + '/\'\n')
	    else:
	        outFile.write(line)

    print "Finished copying files to", targetDir
    print "The Tree files are also at their original location and you may want to delete them once you are satisfied with the merged sample."
    print "Created new dictionary file at", new_dictionary_path
    print "Make sure to update your SmallXAnaVersion environment variable to point to it."
            
    ###


if __name__ == "__main__":
    main()
