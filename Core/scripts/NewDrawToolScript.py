#!/usr/bin/env python
import sys, os
from optparse import OptionParser

template='''
# here you can write down the draw functions/sequence/stuff you want to be executed with the main DrawTool.py program.
# For a complete list of all available functions and options
# please visit: https://twiki.cern.ch/twiki/bin/viewauth/CMS/CFFDrawTool

# specify if you want to run the script and ROOT in batch mode (this will not show any canvases):
#setBatchMode()

# Set the wanted input file and load all available histograms in this file in the memory:
setInput("XXXXX")
getAllHistos()

# define nice legend names for the samples that you are plotting:
setLegend("MinBias_TuneMonash13_13TeV-pythia8","Pythia8 Monash13")
setLegend("data_ZeroBias1","Data")

# this will plot ALL histograms found the in the file:
draw()

# update all open canvases to display the changes
updateCanvas()

# after drawing one can save the plots as files
# by default the PDF format is chosen to save a plot
# by default they are saved in the current directory
# save all open canvases to pdf files:
#saveCanvas()
'''

styletemplate='''
#
# use the "hsample" variable to set draw properties per sample that is plotted
# this will be propagated to all canvases
# access the histograms with "h"
# all default ROOT functions can be used here
#

if hsample == "MinBias_TuneMonash13_13TeV-pythia8":
    h.SetLineColor(4)

if hsample == "data_ZeroBias1":
    h.SetLineColor(2)
    h.SetMarkerStyle(20)
    h.SetMarkerColor(2)
    h.SetMarkerSize(0.5)

#
# use the "cname" variable to set draw properties of the histograms per canvas e.g. plot ranges
# access the histograms with "h"
# access the canvas with "c"
# if a particular canvas plots a ratio panel, you'll have to use the upper pad to set e.g. log scales. Access it with "upperpad"
# all default ROOT functions can be used here
#

if cname == "phiRecoTracks_central_minbias":
    h.GetYaxis().SetRangeUser(0.031,0.05)
    h.GetYaxis().SetNdivisions(505)
    h.GetYaxis().SetTitle("(1/N)dN/d#phi")
    h.GetXaxis().SetTitle("#phi_{track}")

if cname == "ptRecoTracks_central_minbias":
    #c.cd().SetLogy() # use this without ratio panel
    upperpad.SetLogy() # use with ratio panel
    h.GetYaxis().SetRangeUser(0.000002,10)
    h.GetYaxis().SetTitle("(1/N)dN/dp_{T}")
    h.GetXaxis().SetTitle("track p_{T}")
'''

if __name__ == "__main__":
    parser = OptionParser(usage="usage: %prog [options] filename",
                            version="%prog 1.0")

    parser.add_option("-s", "--sample", action="store", type="string", dest="sample" )
    #parser.add_option("-d", "--dataOnly", action="store", type="bool", dest="dataOnly" )
    (options, args) = parser.parse_args()
    if len(args) < 2:
        print "Usage: NewDrawToolScript.py MyDrawScriptName inputfile.root"
        sys.exit()

    name=args[0]
    fname = name+".py"
    inputfile = args[1]
    stylename = name+".style"
    
    if os.path.isfile(fname):
        print "Draw script with name " + name + " already exists ("+fname+")"
        sys.exit()

    with open(fname, "w") as f:
        f.write(template.replace("XXXXX",inputfile))
	
    with open(stylename, "w") as f:
        f.write(styletemplate)

    print ""
    print "A skeleton DrawTool script + style file was created (" + fname  + " and " + stylename + ")"
    print ""













