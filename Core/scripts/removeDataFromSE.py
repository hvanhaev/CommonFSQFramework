#! /usr/bin/env python
import sys, os, imp, subprocess
from optparse import OptionParser
import random, time

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
print "Going to remove:"
print ""
for s in samples:
    print "   ", s
print ""
print "defined in", sampleFile
a=random.randint(1, 10)
b=random.randint(1, 10)
print "Type result of", a, "+", b, " <enter> to continue. ",
try:
    choice = int(raw_input().lower())
except:
    print "Wrong answer, exiting"
    sys.exit()

if abs(choice) != a+b:
    print "Wrong answer, exiting"
    sys.exit()

if choice > 0:
    print "10s sleep..."
    time.sleep(10)


for s in samples:
    if "pathSE" not in mod.sam[s]:
        print "Warning: sample",s,"has no SE path set"
        continue
    path = mod.sam[s]["pathSE"]
    #print s, path
    p = subprocess.Popen(["lcg-ls", path], stdout=subprocess.PIPE)
    data = p.communicate()[0].split("\n")

    total=float(len(data))
    cnt = 0
    print ""
    print "Doing", s
    for d in data:
        fname = d.split("/")[-1]
        if not fname:
            if len(fname)!=0:
                print "\nCannot extract file name from line: |"+d+"|"
                continue

        fullname = path + "/" +fname
        if choice > 0:
            subprocess.call(["srmrm", fullname])
            cnt += 1
            if cnt % 20 == 0:
                sys.stdout.write(str(int(100*cnt/total))+"%")
            else:
                sys.stdout.write(".")
            sys.stdout.flush()
        else:
            print fullname

    print ""



