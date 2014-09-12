#!/usr/bin/env python
import sys,os,re,shutil
from optparse import OptionParser
import subprocess

# TODO: voms-proxy-init --voms cms --valid 168:00

try:
    ver=subprocess.check_output(["crab", "--version"])#,, "v3"
except OSError:
    print "Seems crab3 environment is not defined. Exiting."
    sys.exit()

if "v3" not in ver:
    print "This is a crab3 utility. You are trying to use it with crab2. Exiting."
    sys.exit()

parser = OptionParser(usage="usage: %prog [options] filename",
                        version="%prog 1.0")

(options, args) = parser.parse_args()

if len(args) != 2:
    print "Usage: manageCrab3.py taskName command"
    print "Example: manageCrab3.py L1JetRate_20140912TestCrab3 status"
    sys.exit()

taskName = args[0]
command = args[1]

if not os.path.isdir(taskName):
    print "Error:", taskName,"is not a directory"
    sys.exit()


for root, dirs, files in os.walk(taskName):
    #print root, dirs, files

    for d in dirs:
        fullDir = os.path.join(taskName, d)
        #toExec = "crab " + command + " " + fullDir
        toExec = "login"
        print "Try"
        os.system(toExec)
        print "Done"
        sys.exit()

    break # maxdepth=1 needed


