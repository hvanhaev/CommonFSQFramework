#!/usr/bin/env python

import sys, os
from optparse import OptionParser
import ROOT
ROOT.gROOT.SetBatch(True)
ROOT.gSystem.Load("libRooUnfold.so")

sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
parser = OptionParser(usage="usage: %prog [options] filename",
                        version="%prog 1.0")

(options, args) = parser.parse_args()
if len(args) < 2:
    print "Wrong usage"
    sys.exit()

outfile = args[0]
infiles = args[1:]
#print outfile, infiles

if os.path.isfile(outfile):
    print "output file exists. Exiting"
    sys.exit()

merger  = ROOT.TFileMerger( False, False);
merger.OutputFile(outfile, True, 1)
for t in infiles:
    merger.AddFile(t)

status = merger.Merge()
print "Merge status: ", status

