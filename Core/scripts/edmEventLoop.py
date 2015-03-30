#!/usr/bin/env python

from ROOT import *
import ROOT
ROOT.gROOT.SetBatch(True)

import os,re,sys,math
from DataFormats.FWLite import Events, Handle, Lumis

def main():
    infile = "mnTrgAna_PAT.root"
    events = Events([infile,])


    jetHandle = Handle("vector<pat::Jet>") # please note that handle creation is a very expensive call. 
                                           # It should be done outside the event loop
    jetLabel = ("selectedPatJets",)

    for event in events:
        lumi = event.eventAuxiliary().luminosityBlock()
        evN = event.eventAuxiliary().event()
        run = event.eventAuxiliary().run()
        print "----", run, lumi, evN

        event.getByLabel(jetLabel, jetHandle)
        for j in jetHandle.product():
            print j.pt(), j.eta()

if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    ROOT.gSystem.Load("libFWCoreFWLite.so")
    AutoLibraryLoader.enable()
    main()
