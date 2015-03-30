#! /usr/bin/env python

from ROOT import TFile
from ROOT import gDirectory

# open the file
myfile = TFile( 'trees.root' )

# retrieve the ntuple of interest
mychain = gDirectory.Get( 'mnXS/data' )
entries = mychain.GetEntriesFast()

for jentry in xrange( entries ):
 # get the next tree in the chain and verify
    ientry = mychain.LoadTree( jentry )
    if ientry < 0:
       break

    nb = mychain.GetEntry( jentry )
    if nb <= 0:
       continue
    event = mychain.event
    run =   mychain.run
    print run, event

    #jets = mychain.caloJets
    #jetsId = mychain.caloJets_jetID
    jets = mychain.pfJets
    jetsId = mychain.pfJets_jetID
    print jetsId.size(), jets.size()
    for i in xrange(len(jets)):
        print jetsId.at(i), jets.at(i).pt(), jets.at(i).eta()


