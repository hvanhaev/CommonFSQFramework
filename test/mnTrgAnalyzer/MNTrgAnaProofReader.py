#!/usr/bin/env python


import sys, os, time, math
sys.path.append(os.path.dirname(__file__))

import ROOT
ROOT.gROOT.SetBatch(True)
from ROOT import *

from array import *

# please note that python selector class name (here: MNTrgAnaProofReader) 
# should be consistent with this file name (MNTrgAnaProofReader.py)

# you have to run this file from directory where it is saved

from MNTriggerStudies.MNTriggerAna.ExampleProofReader import ExampleProofReader

class MNTrgAnaProofReader(ExampleProofReader):
    #def SlaveBegin( self, tree ):
    def init(self):
        print 'configure: MNTrgAnaProofReader'
        self.lastEv  = 0
        self.lastRun = 0

        self.hist = {}

        todo = ["signalEffVsHLTThreshold",
                "signalEffVsL1Threshold",
                "signalEffVsL1Threshold_bothForward",
                "signalEffVsHLTThreshold_bothForward",
                "signalEffVsHLTThreshold_atLeastOneNonForward",
                "signalEffVsL1Threshold_atLeastOneNonForward"
                ]

        todo2= ["_NOM", "_DENOM", "_rate"]

        for t1 in todo:
            for t2 in todo2:
                t = t1+t2
                self.hist[t] = ROOT.TH1F(t, t, 50, -0.5, 49.5)
                self.hist[t].Sumw2()
                self.GetOutputList().Add(self.hist[t])


        todoXCheck = [  "signalEffVsHLTThreshold_SinglePFJet",]
        for t1 in todoXCheck:
            for t2 in todo2:
                t = t1+t2
                self.hist[t] = ROOT.TH1F(t, t, 100, 309.5, 409.5)
                #self.hist[t] = ROOT.TH1F(t, t, 100, 9.5, 109.5)
                self.hist[t].Sumw2()
                self.GetOutputList().Add(self.hist[t])





        sys.stdout.flush()

    def getTriggers(self):
        newEvent = False
        event = self.fChain.event
        run = self.fChain.run
        if event != self.lastEv:
            newEvent = True
        elif run != self.lastRun:
            newEvent = True

        if newEvent: # cache best trigger objects
            self.lastRun =  run
            self.lastEv = event

            self.allL1 = [] # Currently all L1 jets not depending on eta
            self.allHLT = [] # Currently all HLT jets not depending on eta
            self.bestCAny = [] # CC or CF (or CB :)
            self.bestFF = [] # can be FF or FB (or BB :)

            todo = {}
            todo["l1"] = self.fChain.l1Jets
            todo["hlt"] =  getattr(self.fChain, self.hltCollection)
            for t in todo:
                curFwd = []
                curCen = []
                for jet in todo[t]:
                    isCentral = abs(jet.eta()) < 3.0
                    if isCentral:
                        curCen.append(jet.pt())
                    else:
                        curFwd.append(jet.pt())

                if t == "l1":
                    self.allL1 = sorted(curFwd + curCen, reverse = True)
                else:
                    curCen = sorted(curCen, reverse = True)
                    curFwd = sorted(curFwd, reverse = True)
                    self.allHLT  = sorted(curCen + curFwd, reverse = True)
                    if len(curCen) > 0 and len(curCen) + len(curFwd) > 1:
                        pt1 = curCen[0]
                        pt2Cand = []
                        if len(curFwd) > 0:
                            pt2Cand.append(curFwd[0])
                        if len(curCen) > 1:
                            pt2Cand.append(curCen[1])

                        if len(pt2Cand) == 0:   # not possible...
                            raise Exception("Totally lost.")

                        pt2 = max(pt2Cand)
                        self.bestCAny = sorted([pt1, pt2], reverse = True)

                    if len(curFwd) > 1:
                        self.bestFF = sorted([curFwd[0], curFwd[1]], reverse = True)

                    #print "Best: CFff", self.bestCAny
                    #if len(self.bestCAny) > 1:
                    ##    for j in todo["hlt"]:
                    #        print j.pt(), j.eta()
                            
    def analyze(self):
        #event = self.fChain.event
        #run = self.fChain.run
        #lumi = self.fChain.lumi
        #print event

        weight = 1. # calculate your event weight here

        # for xcheck purposes 
        self.getTriggers()
        if len(self.allHLT) > 0:
            hardest = self.allHLT[0]
            rateVsPtThreshold = self.hist["signalEffVsHLTThreshold_SinglePFJet_rate"]
            nbins = rateVsPtThreshold.GetNbinsX()
            getBinCenter = rateVsPtThreshold.GetXaxis().GetBinCenter
            fill = rateVsPtThreshold.Fill
            for i in xrange(1,nbins+1):
                binCenter = getBinCenter(i)
                if binCenter <= hardest:
                    print "  fl!", i, rateVsPtThreshold.GetXaxis().GetBinCenter(i)
                    fill(binCenter)
                else:
                    break


        pfJetsMomenta = self.fChain.pfJets

        #          (bkwd, fordward)
        bestPair = [None,None]

        for i in xrange(pfJetsMomenta.size()):
            if pfJetsMomenta.at(i).pt() < self.recoJetPtThreshold: continue

            eta = pfJetsMomenta.at(i).eta()
            if bestPair[0] == None or bestPair[0].eta() > eta:
                bestPair[0] = pfJetsMomenta.at(i)
            elif bestPair[1] == None or bestPair[1].eta() < eta:
                bestPair[1] = pfJetsMomenta.at(i)



        self.doThresholdAna(level=2, minObjects=2, isRatePlot = True) # HLT, threshold ana - requiering two jets
        self.doThresholdAna(level=1, minObjects=1, isRatePlot = True) # L1, threshold ana - one L1 jet required
                    
        self.doThresholdAna(level=1, minObjects = 1, bothForwardTrigger=True, isRatePlot = True)
        self.doThresholdAna(level=1, minObjects = 1, bothForwardTrigger=False, isRatePlot = True)
        self.doThresholdAna(level=2, minObjects = 2, bothForwardTrigger=True, isRatePlot = True)
        self.doThresholdAna(level=2, minObjects = 2, bothForwardTrigger=False, isRatePlot = True)

        if bestPair[1] == None or bestPair[0] == None:
            return 1
        eta1 = abs(bestPair[0].eta())
        eta2 = abs(bestPair[1].eta())
        bothForward = False
        if eta1 > 3 and eta2 > 3:
            bothForward = True

        self.doThresholdAna(level=2, minObjects=2) # HLT, threshold ana - requiering two jets
        self.doThresholdAna(level=1, minObjects=1) # L1, threshold ana - one L1 jet required

        self.doThresholdAna(level=1, minObjects = 1, bothForwardTrigger=bothForward)
        self.doThresholdAna(level=2, minObjects = 2, bothForwardTrigger=bothForward)


        return 1

    def doThresholdAna(self, level, minObjects, bothForwardTrigger=None, isRatePlot = False):
        ''' level=1 - L1, level=2 - HLT
        bothForwardTrigger=None - do not use split trigger
        bothForwardTrigger=True - use split trigger for bothForward category
        bothForwardTrigger=False - use split trigger for atLeastOneNonForward category
        '''
        # at this point we got a signal event. Go through avaliable HLT jets
        # and find two with the highest PT
        # TODO  : recoJet2HLTjet matching
        # TODO2 : hltJet2l1Jet matching

        if level != 2 and level != 1:
            raise Exception("level should be equal to 1 or 2")

        self.getTriggers() # cache best L1 and HLT objects
        highestHLTThresholdPossibleForThisEvent = 0 # if it stays 0 - less than two HLT jets present in the event

        if bothForwardTrigger == None:
            if level == 1:
                base = "signalEffVsL1Threshold"
                if len(self.allL1)>= minObjects:
                    highestHLTThresholdPossibleForThisEvent = sorted(self.allL1, reverse=True)[minObjects-1]
            elif level == 2:
                base = "signalEffVsHLTThreshold"
                if len(self.allHLT)>= minObjects:
                    highestHLTThresholdPossibleForThisEvent = sorted(self.allHLT, reverse=True)[minObjects-1]
        elif bothForwardTrigger == True:
            if level == 1:
                base = "signalEffVsL1Threshold_bothForward"
                if len(self.allL1)>= minObjects:
                    highestHLTThresholdPossibleForThisEvent = sorted(self.allL1, reverse=True)[minObjects-1]
            elif level == 2:
                base = "signalEffVsHLTThreshold_bothForward"
                if len(self.bestFF) > 1:
                    highestHLTThresholdPossibleForThisEvent = min(self.bestFF[0], self.bestFF[1])

        elif bothForwardTrigger == False: 
            if level == 1:
                base = "signalEffVsL1Threshold_atLeastOneNonForward"
                if len(self.allL1)>= minObjects:
                    highestHLTThresholdPossibleForThisEvent = sorted(self.allL1, reverse=True)[minObjects-1]
            elif level == 2:
                base = "signalEffVsHLTThreshold_atLeastOneNonForward"
                if len(self.bestCAny) > 1:
                    highestHLTThresholdPossibleForThisEvent = min(self.bestCAny[0], self.bestCAny[1])
                    #print "  -->", highestHLTThresholdPossibleForThisEvent
        else:
            raise Exception("Got confused by bothForwardTrigger variable")
    

        #print base, highestHLTThresholdPossibleForThisEvent, math.ceil(highestHLTThresholdPossibleForThisEvent)
        nom = self.hist[base + "_NOM"]
        denom = self.hist[base + "_DENOM"]


        if not isRatePlot:
            fillNom = nom.Fill
            fillDenom = denom.Fill
            nbins = denom.GetNbinsX()
            getBinCenter = denom.GetXaxis().GetBinCenter
            for i in xrange(1,nbins+1):
                binCenter = getBinCenter(i)
                fillDenom(binCenter)
                if binCenter <= highestHLTThresholdPossibleForThisEvent:
                    #print "->Fill"
                    fillNom(binCenter)
            del getBinCenter

    
        if isRatePlot:
            rateVsPtThreshold = self.hist[base+"_rate"]
            nbins = rateVsPtThreshold.GetNbinsX()
            getBinCenter = rateVsPtThreshold.GetXaxis().GetBinCenter
            #binMax = rateVsPtThreshold.GetXaxis().FindBin(highestHLTThresholdPossibleForThisEvent)
            #addBinContent = rateVsPtThreshold.AddBinContent
            fill = rateVsPtThreshold.Fill
            for i in xrange(1,nbins+1):

                binCenter = getBinCenter(i)
                if binCenter <= highestHLTThresholdPossibleForThisEvent:
                    #print "  fl", i, rateVsPtThreshold.GetXaxis().GetBinCenter(i)
                    fill(binCenter)
                else:
                    break
                #addBinContent(i)

            del getBinCenter

    def finalize(self):
        print "Finalize:"
        normFactor = self.getNormalizationFactor()
        print "  applying norm", normFactor
        for h in self.hist:
            self.hist[h].Scale(normFactor)

if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    ROOT.gSystem.Load("libFWCoreFWLite.so")
    AutoLibraryLoader.enable()

    sampleList = None # run through all
    maxFilesMC = None

    '''
    sampleList = ["QCD_Pt-30to50_Tune4C_13TeV_pythia8",]
    #sampleList = ["QCD_Pt-10to15_Tune4C_13TeV_pythia8",]
    maxFilesMC = 1
    # '''



    slaveParams = {}
    slaveParams["recoJetPtThreshold"] = 35

    # select hltCollection here (see plugins/MNTriggerAna.cc to learn whats avaliable):
    slaveParams["hltCollection"] = "hltAK5PFJetL1FastL2L3Corrected"

    # note - remove maxFiles parameter in order to run on all files
    MNTrgAnaProofReader.runAll(treeName="mnTriggerAna", 
                               slaveParameters=slaveParams,
                               sampleList=sampleList,
                               maxFilesMC = maxFilesMC,
                               outFile = "~/plotsHLT.root" )
                                
