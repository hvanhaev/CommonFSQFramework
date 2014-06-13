#!/usr/bin/env python

import ROOT
ROOT.gROOT.SetBatch(True)

import os,re,sys,math

import MNTriggerStudies.MNTriggerAna.Util
import MNTriggerStudies.MNTriggerAna.Style

from MNTriggerStudies.MNTriggerAna.DrawPlots import DrawPlots

from array import array


from optparse import OptionParser

class DrawMNPlots(DrawPlots):
    #def init(self):
    #    pass
    def test(self):
        pass



if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    ROOT.gSystem.Load("libFWCoreFWLite.so")
    ROOT.AutoLibraryLoader.enable()
    d = DrawMNPlots()
    d.draw()

