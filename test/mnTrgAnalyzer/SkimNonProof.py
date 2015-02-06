#! /usr/bin/env python

import ROOT
ROOT.gROOT.SetBatch(True)
from ROOT import TFile
from ROOT import gDirectory

from MNTriggerStudies.MNTriggerAna.GetDatasetInfo import getTreeFilesAndNormalizations

maxFiles = None

'''
  Neutrino_Pt-2to20_gun_10GeV_Pu20to50
  QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8_5GeV_Pu0to10
  QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8_5GeV_Pu20to50
  Neutrino_Pt-2to20_gun_5GeV_Pu20to50
  QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8_10GeV_Pu20to50
  QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8_10GeV_Pu0to10
'''
#samplesToProcess = ["QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8_5GeV_Pu0to10"]
#samplesToProcess = ["QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8_10GeV_Pu0to10"]


samples2files = getTreeFilesAndNormalizations(maxFilesMC=maxFiles, samplesToProcess=samplesToProcess)
if len(samples2files) != 1:
    raise Exception("TODO")

mychain = ROOT.TChain("MNTriggerAnaNew/data")
for s in samples2files:
    flist = samples2files[s]["files"]
    for f in flist:
        mychain.Add(f)

entries = mychain.GetEntriesFast()

skimfile = ROOT.TFile(samplesToProcess[0]+".root","recreate") 
initialized = False

cnt = 0
for jentry in xrange( entries ):
    ientry = mychain.LoadTree( jentry )
    if ientry < 0:
       break

    nb = mychain.GetEntry( jentry )
    if nb <= 0:
       continue

    if not initialized:
        initialized = True
        newtree = mychain.GetTree().CloneTree(0)

    cnt += 1
    if cnt % 100000 == 0:
        print "done:", cnt
    if mychain.PUNumInteractions != 0: continue
    newtree.Fill()
