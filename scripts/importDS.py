#! /usr/bin/env python

import os, sys, subprocess

import ROOT
ROOT.gROOT.SetBatch(True)
from ROOT import *

import pprint
import MNTriggerStudies.MNTriggerAna.Util

try:
    from elementtree import ElementTree
except:
    from xml.etree.ElementTree import ElementTree 

def getSEDirsCrab3(anaVersion, name):
    # from runCrab3Jobs.py:
    # pycfgextra.append("config.General.workArea='"+anaVersion+"'")
    # pycfgextra.append("config.General.requestName='"+name+"'")
    for taskDir in os.listdir(anaVersion):
        if name in taskDir: break
    else:
        raise Exception("Cannot find crab3 dir for "+anaVersion+" "+ name)

    taskDir = os.path.join(anaVersion, taskDir)
    output = subprocess.check_output(["crab", "getoutput", "--dump", taskDir])
    SEDirs = set()
    for l in output.splitlines():
        filename = l.split("/")[-1]
        if not filename.startswith("trees_"): continue
        if not filename.endswith(".root"): continue
        SEDirs.add(l.replace(filename,""))

    return SEDirs

def getSEDirsCrab2(anaVersion, name):
    crabDirName = anaVersion+"_"+name # crab dir naming from runCrabJobs.py
    crabResDir = crabDirName + "/res/"
    SEDirs = set()
    for  r,d,f in os.walk(crabResDir):
        for file in f:
            if not file.endswith(".xml"): continue
            if not file.startswith("crab_fjr_"): continue
            if "Submission_" in r: continue
            crabFjr = r+"/"+file
            fp = open(crabFjr,"r")
            try:
                et = ElementTree()
            except:
                et = ElementTree
            mydoc = et.parse(fp)
            pfnDir=None
            for e in mydoc.findall('./File/PFN'):
                if pfnDir != None:
                    print "Allready have a pfn in", crabFjr
                else:
                    pfnDir = e.text.strip()
                
                #print pfnDir
            for e in mydoc.findall('./AnalysisFile/PFN'):
                #print type(e)
                #print dir(e)
                #print e.tag, e.attrib
                #print  "XXXX", e.text.strip()
                if pfnDir != None:
                    print "Allready have a pfn in", crabFjr
                else:
                    pfnDir = e.attrib["Value"]
            if pfnDir:
                fileName = pfnDir.split("/")[-1]
                pfnDir = pfnDir.replace(fileName,"")
                SEDirs.add(pfnDir)

            if len(SEDirs) > 0: # makes consistency checks above useless, but it;s to long to parse all xml files
                break

    return SEDirs


def main(sam):
    if os.path.isfile(dsFile):
        file=open(dsFile)
    else:
        file=open( edm.FileInPath(dsFile).fullPath())



    for line in file:

        if line.find("#") != -1:
            continue

        ds=line.rstrip()
        if len(ds) == 0:
            print "Warning - empty line in ds file. Skipping"
            continue

        isData = fun["isData"](ds)

        name = fun["name"](ds)
        if not name:
            print "#Warning - empty line (?) ", line
            continue


        # set attributes
        sam[name]={}
        for f in fun:
            value = fun[f](ds)
            if value != None:
                sam[name][f] = value

        crabVersion = MNTriggerStudies.MNTriggerAna.Util.getCrabVersion()
        if crabVersion == 2:
            SEDirs = getSEDirsCrab2(anaVersion, name)
        elif crabVersion == 3:
            SEDirs = getSEDirsCrab3(anaVersion, name)
        else:
            raise Exception("Unexpected crab version: "+str(crabVersion))

        SEDir = None
        if len(SEDirs)!=1: 
            print "Problem determining SE dir for", name, "- candidates are: ", SEDirs
            print "   Note: this is perfectly normal if you are before running crab or none of your jobs produced usable output "
            print ""
        else:
            SEDir = SEDirs.pop()
            # put also local paths together

            sam[name]["pathSE"] = SEDir
            tagBasePathPAT = "XXXTMFPAT"  # note this tag in customization function below
            tagBasePathTrees = "XXXTMFTTree" # note this tag in customization function below
            basePathName = ""
            startRecording = False
            for x in SEDir.split("/"):
                if x == "store":
                    startRecording = True

                if startRecording:
                    basePathName += "/" + x
                    
            basePathName += "/"

            sam[name]["pathPAT"] = "/" + tagBasePathPAT + basePathName
            sam[name]["pathTrees"] = "/" + tagBasePathTrees + basePathName

            '''
            # TODO or place elsewhere
            todo = [sam[name]["pathPAT"], sam[name]["pathTrees"]]
            for t in todo:
                cnt = 0
                for r,d,f in os.walk(t):
                    for files in f:
                        if not files.endswith(".root"): continue
                        cnt += 1

                if cnt == 0:
                    print "Warning - empty path", t
            '''







    return sam

def printSam(sam):
    pp = pprint.PrettyPrinter()
    toFile = []


    toFile.append('anaVersion="' + anaVersion + '"\n')
    toFile.append('anaType="'    + anaType + '"\n')
    toFile.append(preamble + "\n")
    toFile.append('rootPath="' + rootPath(dateTT) + '"\n')
    
    toFile.append('sam = {}' + "\n")

    for s in sorted(sam.keys()):
        toFile.append("\n")
        toFile.append('sam["'+s+'"]={}' + "\n")
        for atr in sam[s]:
            toFile.append('sam["'+s+'"]["'+atr+'"]='+pp.pformat(sam[s][atr]) + "\n")

    epilogue = onTheFlyCustomization()
    toFile.append(epilogue)

    toFile.append('''def fixLocalPaths(sam):
        import os,imp
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

        for s in sam:
            if "pathPAT" in sam[s]:
                sam[s]["pathPAT"] = sam[s]["pathPAT"].replace("XXXTMFPAT", localBasePathPAT)
            if "pathTrees" in sam[s]:
                sam[s]["pathTrees"] = sam[s]["pathTrees"].replace("XXXTMFTTree", localBasePathTrees)
            #print sam[s]["pathPAT"]
            #print sam[s]["pathTrees"]
        return sam
sam = fixLocalPaths(sam)
''' )




    ofile = "Samples_"+anaVersion+".py"
    #'''
    if os.path.isfile(ofile):
        import random
        import string
        char_set = string.ascii_uppercase + string.digits
        name = ''.join(random.sample(char_set*6,6))
        ofileBak = ofile+"_"+name
        print "BAK:", ofileBak
        os.system("cp " + ofile + " " + ofileBak)
    #'''
    print "Please remember to do diff on new " + ofile + " and the one in python/samples dir"

    outputFile = open("Samples_"+anaVersion+".py", "w") 
    for line in toFile:
        outputFile.write(line)


from optparse import OptionParser
import imp

if __name__ == "__main__":
    ROOT.gSystem.Load("libFWCoreFWLite.so")
    ROOT.AutoLibraryLoader.enable()

    parser = OptionParser(usage="usage: %prog [options] filename",
                            version="%prog 1.0")
                            
    #parser.add_option("-p", "--plotDefFile",   action="store", type="string", dest="plotDefFile", help="plot using definitions from plot def file" )
    parser.add_option("-d", "--date",   action="store", type="string", dest="date", help="skim date" )
    parser.add_option("-i", "--inputDSFile",   action="store", type="string", dest="dsFile", help="override dsFile" )
    (options, args) = parser.parse_args()

    if not options.date:
        print "Date missing"
        sys.exit()

    if len(args) == 0:
        print "You should give the template file name"
        sys.exit()
    mod_dir, filename = os.path.split(args[0])
    mod, ext = os.path.splitext(filename)
    f, filename, desc = imp.find_module(mod, [mod_dir])
    mod = imp.load_module(mod, f, filename, desc)

    todo = ["preamble","dsFile","anaType","rootPath","onTheFlyCustomization","fun"]
    for t in todo:
        globals()[t] = getattr(mod,t)

    if options.dsFile:
        print "Overriding dsFile to ", options.dsFile
        globals()["dsFile"] = options.dsFile
    

    dateTT = options.date#"20140411" ## TODO fixme!
    anaVersion = anaType + "_" + dateTT
    #globals()["anaVersion"] = anaVersion


    sam = {}
    sam=main(sam)
    printSam(sam)


