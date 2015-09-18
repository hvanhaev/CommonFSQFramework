#!/usr/bin/env python
import sys, os
from optparse import OptionParser

template='''#!/usr/bin/env python
##################################################################
# This is the default stuff, and should not be changed

# import general system and ROOT functions
import ROOT
from ROOT import *
from array import array
import os,re,sys,math

# import CFF specific functions
from CommonFSQFramework.Core.Util import *
from CommonFSQFramework.Core.DrawUtil import *
import CommonFSQFramework.Core.Style

# set the CFF style
style = CommonFSQFramework.Core.Style.setStyle()

##################################################################

# user specific code
# manually draw your stuff from different files/histograms

# make canvas with makeCMSCanvas(name, title, width, height), no arguments will produce a standard 800x600 canvas
c = makeCMSCanvas()
# set a unique name to avoid overwriting
c.SetName("hfRecHitenergy")
c.cd().SetLogy()

# get histogram with getHisto(input filename, histogram name, sample name)
h1 = getHisto("./plotsHFplotsVdMruns255019.root","hfRecHitenergy","data_ZeroBias1")
h1.SetLineColor(1)
h1.SetLineWidth(2)
h1.Scale(1./h1.Integral())
h1.GetYaxis().SetRangeUser(0.00000001,1000)
h1.GetYaxis().SetTitle("(1/N)dN/dE")
h1.GetXaxis().SetTitle("energy [GeV]")
h1.Draw()

h2 = getHisto("./plotsHFplotsVdMruns255031.root","hfRecHitenergy","data_ZeroBias1")
h2.SetLineColor(4)
h2.SetLineWidth(2)
h2.Scale(1./h2.Integral())
h2.Draw("same")

# add legend for 2 entries
l = makeLegend(2)
l.AddEntry(h1,"Run 255019")
l.AddEntry(h2,"Run 255031")
l.Draw()

# add CMS lumi to this canvas, put a custom text as second argument to change default lumi value
printLumiPrelLeft(c)

# update canvas to show it
c.Update()

# prevent python from exiting and closing the canvas
preventExit()

'''


if __name__ == "__main__":
    parser = OptionParser(usage="usage: %prog [options] filename",
                            version="%prog 1.0")

    parser.add_option("-s", "--sample", action="store", type="string", dest="sample" )
    #parser.add_option("-d", "--dataOnly", action="store", type="bool", dest="dataOnly" )
    (options, args) = parser.parse_args()
    if len(args) == 0:
        print "Usage: NewDrawScript.py MyScriptName"
        sys.exit()

    name=args[0]
    fname = name+".py"
    
    if os.path.isfile(fname):
        print "Draw script with name " + name + " already exists ("+fname+")"
        sys.exit()

    with open(fname, "w") as f:
        f.write(template)

    os.system("chmod +x " + fname)

    print ""
    print "A skeleton draw script file was created (" + fname  + ")"
    print "This you can extend to manually choose what plots to draw."
    print "Note that you do NOT use this with the automatic DrawTool.py, just execute the file."
    print ""













