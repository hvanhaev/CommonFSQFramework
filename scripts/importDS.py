#! /usr/bin/env python

import os, sys

import ROOT
ROOT.gROOT.SetBatch(True)
from ROOT import *

import pprint
from elementtree import ElementTree
#from elementtree.ElementTree import ElementTree

#from DiJetAnalysis.Common.Util import *


def main(sam):
    file=open( edm.FileInPath(dsFile).fullPath())
    for line in file:

        if line.find("#") != -1:
            continue

        ds=line.rstrip()
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

        # todo: set path also via "fun"
        #path discrovery

        '''
        pathList = set()
        for r,d,f in os.walk(rootPath(dateTT)):
            for files in f:
                if files.endswith(".root"):
                     if name in r:
                        pathList.add( r )
                        #print  name, r
                     #fullname = os.path.join(r,files)

        if len(pathList) != 1:
            print "Problem with paths:", name, pathList
        else:
            sam[name]["path"] = pathList.pop() + "/"
        '''


        # SEDir for copying
        #DiJet_20140214_METFwd-Run2010B-Apr21ReReco-v1
        crabDirName = "DiJet_20140214_METFwd-Run2010B-Apr21ReReco-v1"
        print "Warning - devel name of crab dir"
        # crabDirName = name
        crabResDir = crabDirName + "/res/"

        SEDirs = set()
        for  r,d,f in os.walk(crabResDir):
            for file in f:
                if not file.endswith(".xml"): continue
                if not file.startswith("crab_fjr_"): continue
                if "Submission_" in r: continue
                crabFjr = r+"/"+file
                fp = open(crabFjr,"r")
                mydoc = ElementTree.parse(fp)
                pfnDir=None
                for e in mydoc.findall('./File/PFN'):
                    if pfnDir != None:
                        print "Allready have a pfn in", crabFjr
                    else:
                        pfnDir = e.text.strip()
                    
                    #print pfnDir
                    fileName = pfnDir.split("/")[-1]
                    pfnDir = pfnDir.replace(fileName,"")
                    SEDirs.add(pfnDir)

                if len(SEDirs) > 0: # makes consistency checks above useless, but it;s to long to parse all xml files
                    break

        SEDir = None
        if len(SEDirs)!=1: 
            print "Problem determining SE dir for", name, "- candidates are: ", SEDirs
        else:
            SEDir = SEDirs.pop()

        sam[name]["SEDir"] = SEDir








    return sam

def printSam(sam):
    pp = pprint.PrettyPrinter()
    toFile = []

    anaVersion = anaType + "_" + dateTT

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

    ofile = "Samples_"+anaVersion+".py"
    if os.path.isfile(ofile):
        import random
        import string
        char_set = string.ascii_uppercase + string.digits
        name = ''.join(random.sample(char_set*6,6))
        ofileBak = ofile+"_"+name
        os.system("cp " + ofile + " " + ofileBak)
        print "diff " + ofile + " " + ofileBak

    outputFile = open("Samples_"+anaVersion+".py", "w") 
    for line in toFile:
        outputFile.write(line)


from optparse import OptionParser
import imp

if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)    # disable buffering
    ROOT.gSystem.Load("libFWCoreFWLite.so")
    ROOT.AutoLibraryLoader.enable()

    parser = OptionParser(usage="usage: %prog [options] filename",
                            version="%prog 1.0")
                            
    #parser.add_option("-p", "--plotDefFile",   action="store", type="string", dest="plotDefFile", help="plot using definitions from plot def file" )
    (options, args) = parser.parse_args()

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
    


    dateTT = "20140411" ## TODO fixme!

    sam = {}
    sam=main(sam)
    printSam(sam)


