#! /usr/bin/env python
import sys, os, imp, subprocess
from optparse import OptionParser

parser = OptionParser()
(options, args) = parser.parse_args()
if len(args) != 1:
    print "You must provide samples dictionary file"
    sys.exit(0)

sampleFile = args[0]

#anaDefFile = os.environ["SmallXAnaDefFile"]
mod_dir, filename = os.path.split(sampleFile)
mod, ext = os.path.splitext(filename)
f, filename, desc = imp.find_module(mod, [mod_dir])
mod = imp.load_module(mod, f, filename, desc)

samples = mod.sam.keys()
for s in samples:
    if "pathSE" not in mod.sam[s]:
        print "Warning: sample",s,"has no SE path set"
        continue
    path = mod.sam[s]["pathSE"]
    #print s, path
    p = subprocess.Popen(["lcg-ls", path], stdout=subprocess.PIPE)
    data = p.communicate()[0].split("\n")
    for d in data:
        fname = d.split("/")[-1]
        if not fname:
            print "Cannot extract file name from line: |"+d+"|"
            continue

        fullname = path + "/" +fname

