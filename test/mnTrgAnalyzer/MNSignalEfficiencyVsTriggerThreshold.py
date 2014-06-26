#!/usr/bin/env python


import sys, os, time, math
sys.path.append(os.path.dirname(__file__))

import ROOT
ROOT.gROOT.SetBatch(True)
from ROOT import *

from array import *

# please note that python selector class name (here: MNSignalEfficiencyVsTriggerThreshold) 
# should be consistent with this file name (MNSignalEfficiencyVsTriggerThreshold.py)

# you have to run this file from directory where it is saved

import MNTriggerStudies.MNTriggerAna.ExampleProofReader 
import BaseTrigger

class MNSignalEfficiencyVsTriggerThreshold(MNTriggerStudies.MNTriggerAna.ExampleProofReader.ExampleProofReader):

    def topologyParser(self, topo):
        ''' see getTopologies for topology definition 

            note, that for performance more probable topologies should be first
        '''
        ret = []
        topo = topo.replace(" ", "")
        split = topo.split("|")
        for s in split:
            jetRanges = s.split("&")
            requiredJetsRanges = []
            for range in jetRanges:
                spl = range.split("to")
                r1 = float(spl[0])
                r2 = float(spl[1])
                r1, r2 = (min(r1,r2), max(r1,r2))
                jetRange = (r1, r2)
                requiredJetsRanges.append(jetRange)
            ret.append(requiredJetsRanges)

        return ret

    def getTopologies(self, jets):
        ''' Returns a list of topologies, that are fullfilled by the input jet list.

            Currently a topology consists of a list of sets of etaStart...etaEnd ranges. 
            Event fullfills the topology requirement if there is a set for which a jet
            is present for every eta range of that set'''
        ret = []
        for topologyName in self.topologies:
            #print "Checking:", topologyName
            for topo in self.topologies[topologyName]:
                #print "Checking", topo  
                if len(jets) < len(topo): 
                    #print "len skip"
                    continue 
                rangeMask = [0]*len(topo)
                for j in jets:
                    eta = j.eta()
                    rangeCnt = -1
                    for range in topo:
                        #print eta, range[0], range[1]
                        rangeCnt += 1
                        if rangeMask[rangeCnt] == 1:
                            #print "Range allready ok"
                            continue
                        if eta > range[0] and eta < range[1]:
                            rangeMask[rangeCnt] = 1
                            #print "Bingo!"
                            break # this range is ok, go to next jet
                #print "rangeMask", rangeMask
                if not 0 in rangeMask:
                    ret.append(topologyName)
                    continue # this topology is ok, no need to check other sets of this topology
        return ret

    def init(self):
        topologies = {}
        f = "3    to 4.7"
        b = "-4.7 to -3"
        c = " -3 to 3"
        topologies["FB"] =  f + "&" + b 
        #topologies["FB"] +=  "|" + f + "&" + f # allow ff or bb combinations
        #topologies["FB"] +=  "|" + b + "&" + b
        topologies["atLeastOneCentral"] = c + "&" + c 
        topologies["atLeastOneCentral"] += "|"+ c + "&" + f 
        topologies["atLeastOneCentral"] += "|" + c + "&" + b 

        self.topologies = {} # convert strings to actual representation. Store it
        for t in topologies:
            self.topologies[t] = self.topologyParser(topologies[t])

        getter = BaseTrigger.TriggerObjectsGetter(self.fChain, self.hltCollection)
        getterL1 = BaseTrigger.TriggerObjectsGetter(self.fChain, self.l1Collection)
        self.fbTrigger = BaseTrigger.ForwardBackwardTrigger(getter)
        #self.fbTrigger = BaseTrigger.DoubldForwardTrigger(getter)
        self.atLeastOneCentral = BaseTrigger.DoubleJetWithAtLeastOneCentralJetTrigger(getter)
        self.L1SingleJetSeed = BaseTrigger.SingleJetTrigger(getterL1)

        self.effHistos = {} # histoName:       [topologyName,trigger, effNom, effDenom]
        self.effHistos["FB_HLT"] = ["FB", self.fbTrigger,       None, None]
        self.effHistos["FB_L1"] = ["FB",  self.L1SingleJetSeed, None, None]
        self.effHistos["atLeastOneCentral_HLT"] = ["atLeastOneCentral",  self.atLeastOneCentral, None, None]
        self.effHistos["atLeastOneCentral_L1"] = ["atLeastOneCentral",  self.L1SingleJetSeed, None, None]
        for h in self.effHistos:
                name = h+"_nom"
                self.effHistos[h][2] = ROOT.TH1F(name, name, 50, -0.5, 49.5)
                self.effHistos[h][2].Sumw2()
                self.GetOutputList().Add(self.effHistos[h][2])
                name = h+"_denom"
                self.effHistos[h][3] = ROOT.TH1F(name, name, 50, -0.5, 49.5)
                self.effHistos[h][3].Sumw2()
                self.GetOutputList().Add(self.effHistos[h][3])
                            
    def analyze(self):
        weight = 1. # calculate your event weight here

        pfJetsMomenta = self.fChain.pfJets # TODO: configrable
        jetsAbovePtThr = []
        for i in xrange(pfJetsMomenta.size()):
            jet = pfJetsMomenta.at(i)
            if jet.pt() < self.recoJetPtThreshold: continue
            jetsAbovePtThr.append(jet)
            #print jet.pt(), jet.eta()

        topologies =  self.getTopologies(jetsAbovePtThr)
        for h in self.effHistos:
            topologyName = self.effHistos[h][0]
            if not topologyName in topologies: continue
            maxThr = self.effHistos[h][1].getMaxThreshold()

            fillNom = self.effHistos[h][2].Fill
            fillDenom = self.effHistos[h][3].Fill
            getBinCenter = self.effHistos[h][2].GetXaxis().GetBinCenter
            nbins = self.effHistos[h][2].GetNbinsX()
            for i in xrange(1,nbins+1):
                binCenter = getBinCenter(i)
                fillDenom(binCenter, weight)
                if binCenter <= maxThr:
                    fillNom(binCenter, weight)
            del getBinCenter
            del fillNom
            del fillDenom

        ''' XCheck
        if len(jetsAbovePtThr) > 1 and len(topologies) == 0:
            print "Warning! More then two jets and no topologies!!!"
            for j in jetsAbovePtThr:
                print j.eta(), j.pt()
        #'''
 
    def finalize(self):
        print "Finalize:"
        normFactor = self.getNormalizationFactor()
        print "  applying norm", normFactor
        for h in self.effHistos:
            self.effHistos[h][2].Scale(normFactor)
            self.effHistos[h][3].Scale(normFactor)

if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    ROOT.gSystem.Load("libFWCoreFWLite.so")
    AutoLibraryLoader.enable()

    sampleList = None # run through all
    maxFilesMC = None
    nWorkers = None

    #'''
    #sampleList = ["QCD_Pt-30to50_Tune4C_13TeV_pythia8",]
    #sampleList = ["QCD_Pt-10to15_Tune4C_13TeV_pythia8",]
    #maxFilesMC = 1
    #nWorkers = 1
    # '''
    #maxFilesMC = 32



    slaveParams = {}
    slaveParams["recoJetPtThreshold"] = 35

    # select hltCollection here (see plugins/MNTriggerAna.cc to learn whats avaliable):
    slaveParams["hltCollection"] = "hltAK5PFJetL1FastL2L3Corrected"
    slaveParams["l1Collection"] = "l1Jets"

    # note - remove maxFiles parameter in order to run on all files
    MNSignalEfficiencyVsTriggerThreshold.runAll(treeName="mnTriggerAna", 
                               slaveParameters=slaveParams,
                               sampleList=sampleList,
                               maxFilesMC = maxFilesMC,
                               nWorkers=nWorkers,
                               outFile = "RecoSignalVsHLTEfficiency.root" )
                                
