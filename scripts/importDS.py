#!/usr/bin/env python

import os, sys

import ROOT
ROOT.gROOT.SetBatch(True)

import pprint

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

    print dsFile

    sys.exit()


    anaType = getVariant()

    spl = anaType.split("_")

    dateTT = None
    for s in spl:
        if s.isdigit():
            dateTT  = s

    if not dateTT:
        print "Cannot find date in variant string"
        sys.exit(1)


    '''
    if "ZMuMu" in anaType:
        Template="Template_ZMuMu"
    elif "DiJet" in anaType:
        Template="Template_DiJet" # TODO: from env
    else:
        raise "Whhops!"

    exec "from DiJetAnalysis.DiJetAna.samples."+Template+" import preamble, dsFile, anaType, " \
         " rootPath, onTheFlyCustomization, fun"

    '''
    sam = {}
    sam=main(sam)
    printSam(sam)


