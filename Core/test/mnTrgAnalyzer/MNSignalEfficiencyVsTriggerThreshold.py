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
from MNTriggerStudies.MNTriggerAna.JetGetter import JetGetter

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
        ret = {}
        for topologyName in self.topologies:
            #print "Checking:", topologyName
            for topo in self.topologies[topologyName]:
                #print "Checking", topo  
                if len(jets) < len(topo): 
                    #print "len skip"
                    continue 
                rangeMask = [0]*len(topo)
                objectMask = [None]*len(topo)
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
                            objectMask[rangeCnt] = j

                            #print "Bingo!"
                            break # this range is ok, go to next jet
                #print "rangeMask", rangeMask
                if not 0 in rangeMask:
                    #ret.append(topologyName)
                    #retJets.append(objectMask)
                    ret[topologyName] = objectMask
                    continue # this topology is ok, no need to check other sets of this topology
        return ret

    def init(self):
        puFile = edm.FileInPath("MNTriggerStudies/MNTriggerAna/test/mnTrgAnalyzer/PUhists.root").fullPath()

        self.newlumiWeighters = {}
        self.newlumiWeighters["flat010toPU0p5"] = edm.LumiReWeighting(puFile, puFile, "Flat0to10/pileup", "PU0p5/pileup")
        #self.newlumiWeighters["flat010toPU1"] = edm.LumiReWeighting(puFile, puFile, "Flat0to10/pileup", "PU1/pileup")
        #self.newlumiWeighters["flat010toPU5"] = edm.LumiReWeighting(puFile, puFile, "Flat0to10/pileup", "PU5/pileup")
        #self.newlumiWeighters["flat010toPU10"] = edm.LumiReWeighting(puFile, puFile, "Flat0to10/pileup", "PU10/pileup")
        #self.newlumiWeighters["flat2050toPU20"] = edm.LumiReWeighting(puFile, puFile, "Flat20to50/pileup", "PU20/pileup")
        #self.newlumiWeighters["flat40toPU40"] = edm.LumiReWeighting(puFile, puFile, "Flat40/pileup", "PU40/pileup")



        topologies = {}
        f = "3    to 5.2"
        b = "-5.2 to -3"
        c = " -3 to 3"
        topologies["FB"] =  f + "&" + b 
        #topologies["FB"] +=  "|" + f + "&" + f # allow ff or bb combinations
        #topologies["FB"] +=  "|" + b + "&" + b
        topologies["atLeastOneCentral"] = c + "&" + c 
        topologies["atLeastOneCentral"] += "|"+ c + "&" + f 
        topologies["atLeastOneCentral"] += "|" + c + "&" + b 

        #topologies["atLeastOneForward"] = c + "&" + f
        #topologies["atLeastOneForward"] += "|" + c + "&" + b
        #topologies["atLeastOneForward"] += "|" + f + "&" + b

        topologies["central"] = c 
        topologies["fwdOrBkw"] = f + "|" + b

        cAve = "-1.4 to 1.4"
        fAve = "-5.2 to -2.7"
        bAve = "2.7 to 5.2"
        #topologies["centralAve"] = cAve
        #topologies["forwardAve"] = fAve + "|" + bAve
        #topologies["forwardAve"] = fAve + "|" + bAve
        #topologies["allHLTjetsForBalanceTrg"] = fAve + "|" + bAve + "|" + cAve
        #topologies["allHLTjets"] = "-5.2 to 5.2"
        etaCen = "-1.4 to 1.4"
        etaIntM = "-3. to -1.4"
        etaIntP = "1.4 to 3"
        etaFwdM = "-5. to -3."
        etaFwdP = "3. to 5."

        topologies = {}
        topologies["etaC"] = etaCen
        topologies["etaI"] = etaIntM + "|" + etaIntP
        topologies["etaF"] = etaFwdM + "|" + etaFwdP
        topologies["etaA"] = "-4.7 to 4.7"


        self.topologies = {} # convert strings to actual representation. Store it
        for t in topologies:
            self.topologies[t] = self.topologyParser(topologies[t])

        getter = BaseTrigger.TriggerObjectsGetter(self.fChain, self.hltCollection)
        getterUncor = BaseTrigger.TriggerObjectsGetter(self.fChain, self.hltCollectionUncor)
        getterL1 = BaseTrigger.TriggerObjectsGetter(self.fChain, self.l1Collection)
        getterL1NoMatch = BaseTrigger.TriggerObjectsGetter(self.fChain, self.l1Collection,  maxDR=-1)
        self.fbTrigger = BaseTrigger.ForwardBackwardTrigger(getter)
        #self.fbTrigger = BaseTrigger.DoubldForwardTrigger(getter)
        self.atLeastOneCentral = BaseTrigger.DoubleJetWithAtLeastOneCentralJetTrigger(getter)
        self.L1SingleJetSeed = BaseTrigger.SingleJetTrigger(getterL1)
        #self.L1SingleJetForwardSeed = BaseTrigger.SingleForwardJetTrigger(getterL1)
        #0.173999994993 0.521499991417 0.869499981403 1.21800005436 1.56599998474 1.95599997044 2.58599996567 3.25 3.75 4.25 4.75

        self.effHistos = {} # histoName:       [topologyName,trigger, effNom, effDenom]
        #self.effHistos["FB_HLT"] = ["FB", self.fbTrigger,       None, None, -0.5, 30.5]
        #self.effHistos["FB_L1"] = ["FB",  self.L1SingleJetSeed, None, None, -0.5, 30.5]
        #self.effHistos["atLeastOneCentral_HLT"] = ["atLeastOneCentral",  self.atLeastOneCentral, None, None, -0.5, 30.5]
        #self.effHistos["atLeastOneCentral_L1"] = ["atLeastOneCentral",  self.L1SingleJetSeed, None, None, -0.5, 30.5]

        ####################
        # single jet curves
        ####################
        #'''
        self.l1Central= BaseTrigger.SingleCentralJetTrigger(getterL1)
        self.l1CentralNoMatch= BaseTrigger.SingleCentralJetTrigger(getterL1NoMatch)
        self.l1Forward = BaseTrigger.SingleForwardJetTrigger(getterL1)
        self.l1ForwardNoMatch = BaseTrigger.SingleForwardJetTrigger(getterL1NoMatch)
        self.hltCentral= BaseTrigger.SingleCentralJetTrigger(getter)
        self.hltForward = BaseTrigger.SingleForwardJetTrigger(getter)
        '''
        self.effHistos["singleFwdOrBkw_HLT"] = ["fwdOrBkw", self.hltForward,       None, None, -0.5, 30.5]
        self.effHistos["singleFwdOrBkw_L1"] = ["fwdOrBkw", self.l1Forward,       None, None, -0.5, 30.5]
        self.effHistos["singleFwdOrBkw_L1noMatching"] = ["fwdOrBkw", self.l1ForwardNoMatch,       None, None, -0.5, 30.5]
        self.effHistos["singleCentral_HLT"] = ["central", self.hltCentral,       None, None, -0.5, 30.5]
        self.effHistos["singleCentral_L1"] =  ["central", self.l1Central,       None, None, -0.5, 30.5]
        self.effHistos["singleCentral_L1noMatching"] =  ["central", self.l1CentralNoMatch,       None, None, -0.5, 30.5]
        #'''
        th = self.recoJetPtThreshold

        #self.singleJetTrg = BaseTrigger.SingleJetTrigger(getter)
        #self.singleJetTrg = BaseTrigger.SingleJetTrigger(getterUncor)
        self.singleJetTrg = BaseTrigger.SingleJetTrigger(getterL1)
        #self.singleJetTrg = BaseTrigger.SingleJetTrigger(getterL1NoMatch)
        #postfix = "hltpfVsL1Stage1"
        postfix = "genVshltpf"
        if th < 31:
            #minBin = int(th/3)-1.5
            minBin = -0.5
            maxBin = int(th)+1.5
            #self.effHistos["allHLTjetsForBalanceTrg_"+postfix] = ["allHLTjetsForBalanceTrg", self.singleJetTrg,  None, None, minBin, maxBin]
            #self.effHistos["allHLTjetsForBalanceTrg_"+postfix] = ["allHLTjets", self.singleJetTrg,  None, None, minBin, maxBin]
            self.effHistos["singleJetEfficiencyC_"+postfix] = ["etaC", self.singleJetTrg,  None, None, minBin, maxBin]
            self.effHistos["singleJetEfficiencyI_"+postfix] = ["etaI", self.singleJetTrg,  None, None, minBin, maxBin]
            self.effHistos["singleJetEfficiencyF_"+postfix] = ["etaF", self.singleJetTrg,  None, None, minBin, maxBin]
            self.effHistos["singleJetEfficiencyA_"+postfix] = ["etaA", self.singleJetTrg,  None, None, minBin, maxBin]

        else:
            minBin = int(th/2)-1.5
            maxBin = int(th)+1.5
            #self.effHistos["allHLTjetsForBalanceTrg_"+postfix] = ["allHLTjetsForBalanceTrg", self.singleJetTrg,  None, None, minBin, maxBin]
            #self.effHistos["allHLTjetsForBalanceTrg_"+postfix] = ["allHLTjets", self.singleJetTrg,  None, None, minBin, maxBin]
            self.effHistos["singleJetEfficiencyC_"+postfix] = ["etaC", self.singleJetTrg,  None, None, minBin, maxBin]
            self.effHistos["singleJetEfficiencyI_"+postfix] = ["etaI", self.singleJetTrg,  None, None, minBin, maxBin]
            self.effHistos["singleJetEfficiencyF_"+postfix] = ["etaF", self.singleJetTrg,  None, None, minBin, maxBin]
            self.effHistos["singleJetEfficiencyA_"+postfix] = ["etaA", self.singleJetTrg,  None, None, minBin, maxBin]

        '''
        elif th == 60:
           self.effHistos["60_allHLTjetsForBalanceTrg_"+postfix] = ["allHLTjetsForBalanceTrg", self.singleJetTrg,       None, None, 29.5, 60.5]
        elif th == 80:
           self.effHistos["80_allHLTjetsForBalanceTrg_"+postfix] = ["allHLTjetsForBalanceTrg", self.singleJetTrg,       None, None, 39.5, 80.5]
        elif th == 100:
           self.effHistos["100_allHLTjetsForBalanceTrg_"+postfix] = ["allHLTjetsForBalanceTrg", self.singleJetTrg,       None, None, 49.5, 100.5]
        elif th == 160:
           self.effHistos["160_allHLTjetsForBalanceTrg_"+postfix] = ["allHLTjetsForBalanceTrg", self.singleJetTrg,       None, None, 79.5, 160.5]
        elif th == 220:
           self.effHistos["220_allHLTjetsForBalanceTrg_"+postfix] = ["allHLTjetsForBalanceTrg", self.singleJetTrg,       None, None, 109.5, 220.5]
        elif th == 300:
           self.effHistos["300_allHLTjetsForBalanceTrg_"+postfix] = ["allHLTjetsForBalanceTrg", self.singleJetTrg,       None, None, 109.5, 300.5]
        '''     



        '''
        self.l1Central4ave= BaseTrigger.SingleCentralJetTrigger(getterL1, 1.9)
        self.l1Forward4ave = BaseTrigger.SingleForwardJetTrigger(getterL1, 2.5)
        self.effHistos = {} 
        # HLT ave cuts 60, 100, 160, 220, 280
        th = self.recoJetPtThreshold
        if th == 20:
            self.effHistos["singleFwd20_L1"] = ["forwardAve", self.l1Forward4ave,       None, None, -0.5, 20.5]
            self.effHistos["singleCen20_L1"] =  ["centralAve", self.l1Central4ave,       None, None, -0.5, 20.5]
        elif th == 30:
            self.effHistos["singleFwd30_L1"] = ["forwardAve", self.l1Forward4ave,       None, None, -0.5, 30.5]
            self.effHistos["singleCen30_L1"] =  ["centralAve", self.l1Central4ave,       None, None, -0.5, 30.5]
        elif th == 40:
            self.effHistos["singleFwd40_L1"] = ["forwardAve", self.l1Forward4ave,       None, None, -0.5, 40.5]
            self.effHistos["singleCen40_L1"] =  ["centralAve", self.l1Central4ave,       None, None, -0.5, 40.5]
        elif th == 60:
            self.effHistos["singleFwd60_L1"] = ["forwardAve", self.l1Forward4ave,       None, None, 10.5, 61.5]
            self.effHistos["singleCen60_L1"] =  ["centralAve", self.l1Central4ave,       None, None, 10.5, 61.5]
        elif th == 100:
            self.effHistos["singleFwd100_L1"] = ["forwardAve", self.l1Forward4ave,       None, None, 20.5, 101.5]
            self.effHistos["singleCen100_L1"] =  ["centralAve", self.l1Central4ave,       None, None, 20.5, 101.5]
        elif th == 160 :
            self.effHistos["singleFwd160_L1"] = ["forwardAve", self.l1Forward4ave,       None, None, 67.5, 161.5]
            self.effHistos["singleCen160_L1"] =  ["centralAve", self.l1Central4ave,       None, None, 67.5, 161.5]
        elif th == 220 :
            self.effHistos["singleFwd220_L1"] = ["forwardAve", self.l1Forward4ave,       None, None, 90.5, 200.5]
            self.effHistos["singleCen220_L1"] =  ["centralAve", self.l1Central4ave,       None, None, 90.5, 200.5]
        elif th == 280:
            self.effHistos["singleFwd280_L1"] = ["forwardAve", self.l1Forward4ave,       None, None, 99.5, 200.5]
            self.effHistos["singleCen280_L1"] =  ["centralAve", self.l1Central4ave,       None, None, 99.5, 200.5]
        '''

        for h in self.effHistos:
                binL = self.effHistos[h][4]
                binH = self.effHistos[h][5]
                #binL = -0.5
                #binH = 49.5
                #binL = 39.5
                #binH = 69.5
                nbins = int(binH-binL)
                name = h+"_nom"
                self.effHistos[h][2] = ROOT.TH1F(name, name, nbins, binL, binH)
                self.effHistos[h][2].Sumw2()
                self.GetOutputList().Add(self.effHistos[h][2])
                name = h+"_denom"
                self.effHistos[h][3] = ROOT.TH1F(name, name, nbins, binL, binH)
                self.effHistos[h][3].Sumw2()
                self.GetOutputList().Add(self.effHistos[h][3])

        
        #self.jetGetter = JetGetter("Calo")
        #self.jetGetter = JetGetter("PFAK5")
        #self.jetGetter = JetGetter("PFAK5CHS")
        #self.jetGetter.disableGenJet()

                            
    def analyze(self):
        pu = self.fChain.PUNumInteractions
        #weight = self.newlumiWeighters["flat2050toPU20"].weight(pu)*self.fChain.genWeight
        #weight = self.newlumiWeighters["flat010toPU10"].weight(pu)*self.fChain.genWeight
        #weight = self.newlumiWeighters["flat010toPU1"].weight(pu)*self.fChain.genWeight
        #weight = self.newlumiWeighters["flat010toPU0p5"].weight(pu)*self.fChain.genWeight
        weight = self.fChain.genWeight

        #'''
        pfJetsMomenta = self.fChain.ak4GenJets # TODO: configrable
        #pfJetsMomenta = self.fChain.ak5GenJets # TODO: configrable
        #pfJetsMomenta = self.fChain.hltAK4PFJetsCorrected # TODO: configrable
        jetsAbovePtThr = []
        for i in xrange(pfJetsMomenta.size()):
            jet = pfJetsMomenta.at(i)
            if jet.pt() < self.recoJetPtThreshold: continue
            jetsAbovePtThr.append(jet)
            #print jet.pt(), jet.eta()
        '''
        jetsAbovePtThr = []
        self.jetGetter.newEvent(self.fChain)
        #for shift in self.todoShifts:
        for jet in self.jetGetter.get("_central"):
            if jet.pt() < self.recoJetPtThreshold: continue
            jetsAbovePtThr.append(jet)
        #'''

        topologies =  self.getTopologies(jetsAbovePtThr)
        #print topologies
        for h in self.effHistos:
            topologyName = self.effHistos[h][0]
            if not topologyName in topologies.keys(): continue
            # TODO add option to enable matching
            maxThr = self.effHistos[h][1].getMaxThreshold(topologies[topologyName])
            #print "AAA", topologyName, maxThr
            #maxThr = self.effHistos[h][1].getMaxThreshold()

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

from optparse import OptionParser
if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    ROOT.gSystem.Load("libFWCoreFWLite.so")
    AutoLibraryLoader.enable()

    sampleList = None # run through all
    maxFilesMC = None
    nWorkers = 12

    sampleList = ["MinBias_TuneZ2star_13TeV_pythia6_162"]
    #sampleList = ["QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8"]
    #sampleList = ["QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8_5GeV_Pu20to50"]
    #sampleList = ["QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8_10GeV_Pu20to50"]


    #'''
    #sampleList = ["QCD_Pt-30to50_Tune4C_13TeV_pythia8",]
    #sampleList = ["QCD_Pt-10to15_Tune4C_13TeV_pythia8",]
    maxFilesMC = 6*16
    #maxFilesMC = 12
    nWorkers = 12
    #maxFilesMC = 1
    #nWorkers = 1
    # '''
    #maxFilesMC = 24
    parser = OptionParser()
    (options, args) = parser.parse_args()


    slaveParams = {}

    if len(args) == 0:
        slaveParams["recoJetPtThreshold"] = 15
    else:
        slaveParams["recoJetPtThreshold"] = int(args[0])

    # select hltCollection here (see plugins/MNTriggerAna.cc to learn whats avaliable):
    slaveParams["hltCollection"] = "hltAK4PFJetsCorrected"
    slaveParams["hltCollectionUncor"] = "hltAK4PFJets"

    #slaveParams["hltCollection"] = "hltPFJetsCorrectedMatchedToL1"
    #slaveParams["hltCollection"] = "hltPFJetsCorrectedMatchedToL1"

    #slaveParams["l1Collection"] = "l1Jets" # alias for old
    #slaveParams["l1Collection"] = "stage1L1Jets"
    #slaveParams["l1Collection"] = "stage1allL1Jets"
    #slaveParams["l1Collection"] = "hltAK4CaloJetsCorrected"
    #slaveParams["l1Collection"] = "hltAK4PFJetsCorrected"
    slaveParams["l1Collection"] = "oldRedoneL1Jets"


    # note - remove maxFiles parameter in order to run on all files
    MNSignalEfficiencyVsTriggerThreshold.runAll(treeName="MNTriggerAnaNew", 
                               slaveParameters=slaveParams,
                               sampleList=sampleList,
                               maxFilesMC = maxFilesMC,
                               nWorkers=nWorkers,
                               outFile = "RecoSignalVsHLTEfficiency_"+str(slaveParams["recoJetPtThreshold"])+".root" )
                                
    print "Next step: ./drawMNTrgEfficiencyPlots.py"
