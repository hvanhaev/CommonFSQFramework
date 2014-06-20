#!/usr/bin/env python

import sys, os, time
sys.path.append(os.path.dirname(__file__))

import ROOT
ROOT.gROOT.SetBatch(True)
ROOT.gSystem.Load("libFWCoreFWLite.so")
ROOT.AutoLibraryLoader.enable()
from ROOT import edm, JetCorrectionUncertainty

# please note that python selector class name (here: HLTBalanceTreeProducer) 
# should be consistent with this file name (HLTBalanceTreeProducer.py)

# you have to run this file from directory where it is saved


# Setup:
# ln -s ../MNxsectionAna/BalanceTreeProducer.py
# ln -s ../MNxsectionAna/balanceFitAndPlot.py
# ln -s ../MNxsectionAna/drawBalance.py
import BalanceTreeProducer 
from MNTriggerStudies.MNTriggerAna.JetGetter import JetGetter

class HLTBalanceTreeProducer(BalanceTreeProducer.BalanceTreeProducer):
    def init(self):
        BalanceTreeProducer.BalanceTreeProducer.init(self)
        self.addExternalVar(["hltPtAve"])

    #    print "XX2!"
        #self.balanceProd =  BalanceTreeProducer()
        #self.GetOutputList().Add(self.tree)

    def analyze(self):
        #print "XAXA" ,  self.HLTptAve
        # hltAK5PFJetL1FastL2L3Corrected
        #setattr(self.fChain, "ngoodVTX", 2) # TODO: fChain proxy ?!?

        hltJets = self.fChain.hltAK5PFJetL1FastL2L3Corrected
        probe = None
        tag = None

        for j in hltJets:
            pt = j.pt()
            eta = abs(j.eta())
            tagCand = eta < 1.4
            probeCand = eta > 2.8 and eta < 5.2

            if probeCand and (probe == None or probe.pt() < pt): probe = j
            if tagCand and (tag == None or tag.pt() < pt): tag = j

        if probe != None and tag!=None  and probe != tag:
            ptAve = (tag.pt() + probe.pt())/2.
            if ptAve > 10.:
                self.setExternalVar("hltPtAve", ptAve)
                BalanceTreeProducer.BalanceTreeProducer.analyze(self)

    def finalize(self):
        print "Finalize HLTBala:"




if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    #ROOT.gSystem.Load("libFWCoreFWLite.so")
    #ROOT.AutoLibraryLoader.enable()

    sampleList = None
    maxFilesMC = None
    maxFilesData = None
    nWorkers = None # Use all

    slaveParams = {}
    slaveParams["threshold"] = 35.

    #slaveParams["recoJetCollection"] = "pfJets"
    #slaveParams["recoJetCollection"] = "pfJetsSmear"
    #slaveParams["recoJetCollectionBaseReco"] = "pfJets"
    #slaveParams["recoJetCollectionGEN"] = "pfJets2Gen"
    #slaveParams["recoJetCollection"] = "caloJets"
    #slaveParams["recoJetCollection"] = "caloJetsSmear"

    # TODO: correct JEC uncertainty
    #jetUncFile = "START42_V11_AK5PF_Uncertainty.txt"
    jetUncFile = "START41_V0_AK5PF_Uncertainty.txt"


    slaveParams["jetUncFile"] =  edm.FileInPath("MNTriggerStudies/MNTriggerAna/test/MNxsectionAna/"+jetUncFile).fullPath()
    slaveParams["HLT2015TempWorkaround"] =  True
    slaveParams["doPtShiftsJER"] = False
    slaveParams["doPtShiftsJEC"] = False


    '''
    sampleList=["QCD_Pt-300to470_Tune4C_13TeV_pythia8"]
    nWorkers = 1
    maxFilesMC = 12
    #'''
    #maxFilesMC = 12
    #treeName = "mnTriggerAna"
    slaveParams["ptMin"] = 20
    slaveParams["etaMax"] = 5

    out = "treeDiJetBalance.root"
    HLTBalanceTreeProducer().runAll(treeName="mnTriggerAna",
                           slaveParameters=slaveParams,
                           sampleList=sampleList,
                           maxFilesMC = maxFilesMC,
                           maxFilesData = maxFilesData,
                           nWorkers=nWorkers,
                           outFile = out )


