#! /usr/bin/env python

import os


cutBase = " && hltPtAve  > XXX"
#infile = "treeDiJetBalance_15.root"
infile = "treeDiJetBalance.root"
#todo = [10, 15, 20, 25, 30, 35, 40]
todo = [10,  20, 40]

for t in todo:
    fitResultsDir = "~/tmp/balanceHLT_" + str(t) + "/"
    command  = "./balanceFitAndPlot.py"
    command += " -i " + infile
    command += " -o " + fitResultsDir
    command += " -c '" + cutBase.replace("XXX", str(t)) + "'"
    os.system(command)



    



