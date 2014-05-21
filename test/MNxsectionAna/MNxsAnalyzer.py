#!/usr/bin/env python


import sys, os, time
sys.path.append(os.path.dirname(__file__))

import ROOT
ROOT.gROOT.SetBatch(True)
from ROOT import *

from array import *

# please note that python selector class name (here: MNxsAnalyzer) 
# should be consistent with this file name (MNxsAnalyzer.py)

# you have to run this file from directory where it is saved


from MNTriggerStudies.MNTriggerAna.ExampleProofReader import ExampleProofReader

class MNxsAnalyzer(ExampleProofReader):
    def configureAnalyzer( self):
        print "configureAnalyzer - MNxsAnalyzer"
        self.hist = {}

        todo = ["_jet15", "_dj15fb"]
        for t in todo:
            self.hist["ptLead"+t] =  ROOT.TH1F("ptLead"+t,   "ptLead"+t,  100, 0, 100)
            self.hist["ptSublead"+t] =  ROOT.TH1F("ptSublead"+t,   "ptSublead"+t,  100, 0, 100)
            self.hist["etaLead"+t] =  ROOT.TH1F("etaLead"+t,   "etaLead"+t,  100, -5, 5)
            self.hist["etaSublead"+t] =  ROOT.TH1F("etaSublead"+t,   "etaSublead"+t,  100, -5, 5)
            self.hist["xsVsDeltaEta"+t] =  ROOT.TH1F("xs"+t,   "xs"+t,  100, 0, 9.4)

    

        for h in self.hist:
            self.hist[h].Sumw2()
            self.GetOutputList().Add(self.hist[h])

        sys.stdout.flush()

    def analyze(self):
        #event = self.fChain.event
        #run = self.fChain.run
        #lumi = self.fChain.lumi
        #print event

        #print "XXDS", self.datasetName, self.isData
        weight = 1. 
        if not self.isData:
            weight *= self.fChain.genWeight

        recoJets = getattr(self.fChain, self.recoJetCollection)

        mostFwdJet = None
        mostBkgJet = None
        for i in xrange(0, recoJets.size()):
            jet = recoJets.at(i)
            if jet.pt() < self.threshold: continue
            #print jet.pt()
            eta = jet.eta()
            if  mostFwdJet == None or recoJets.at(mostFwdJet).eta() < eta:
                mostFwdJet = i
            if  mostBkgJet == None or recoJets.at(mostBkgJet).eta() > eta:
                mostBkgJet = i

        #if mostFwdJet != None:
        #    print "Pair: F/B",  recoJets.at(mostFwdJet).eta(), recoJets.at(mostBkgJet).eta()
        pairFound = False
        if mostFwdJet != None and mostBkgJet != mostFwdJet:
            pairFound = True

        if pairFound:
            deta = abs(recoJets.at(mostFwdJet).eta() - recoJets.at(mostBkgJet).eta())
            triggerToUse = "_jet15"
            eta1 =  recoJets.at(mostFwdJet).eta()
            eta2 =  recoJets.at(mostBkgJet).eta()
            if abs(eta1) > 3 and abs(eta2) > 3 and eta1*eta2<0:
                triggerToUse = "_dj15fb"

            gotTrigger = True
            if self.isData: # check trigger
                if triggerToUse == "_jet15":
                    gotTrigger = self.fChain.jet15 > 0.5
                elif triggerToUse == "_dj15fb":
                    gotTrigger = self.fChain.doubleJ15FB > 0.5
                else:
                    raise Exception("Trigger not known??? "+triggerToUse)

            #print triggerToUse, eta1, eta2, gotTrigger
            # TODO: vertex reweighting depending on trigger
            if gotTrigger:
                leadJet = mostBkgJet
                subleadJet = mostFwdJet
                if recoJets.at(subleadJet).pt() > recoJets.at(leadJet).pt():
                    subleadJet = mostBkgJet
                    leadJet = mostFwdJet

                self.hist["ptLead"+triggerToUse].Fill(recoJets.at(leadJet).pt(), weight)
                self.hist["ptSublead"+triggerToUse].Fill(recoJets.at(subleadJet).pt(), weight)
                self.hist["etaLead"+triggerToUse].Fill(recoJets.at(leadJet).eta(), weight)
                self.hist["etaSublead"+triggerToUse].Fill(recoJets.at(subleadJet).eta(), weight)
                #print "DETA", deta, weight, triggerToUse
                self.hist["xsVsDeltaEta"+triggerToUse].Fill(deta, weight)


        return 1



    @classmethod
    def testAll(cls):
        # same as the label of EDProducer that was used to produce the trees
        #todo = [400, 100, 25, 8, 2]
        todo =[1,6,25,100,400]
        #todo = [8]
        for t in todo:
            oname = "~/tmp/plots_"+str(t)+".root"
            onameMerged = "~/tmp/plotsMerged_"+str(t)+".root"
            #pr = MNxsAnalyzer()
            #pr.runAll(treeName="exampleTree", outFile = oname, maxFiles = t)
            #MNxsAnalyzer.MNxsAnalyzer().runAll(treeName="exampleTree", outFile = oname, maxFiles = t)
            cls.runAll(treeName="exampleTree", outFile = oname, maxFiles = t)
            os.system("../../scripts/normalizeAndAddHistograms.py -i "+oname + " -o " + onameMerged)



if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    ROOT.gSystem.Load("libFWCoreFWLite.so")
    AutoLibraryLoader.enable()

    #sampleList = None
    sampleList= ["QCD_Pt-15to3000_TuneZ2star_Flat_HFshowerLibrary_7TeV_pythia6"]
    #sampleList= ["JetMETTau-Run2010A-Apr21ReReco-v1"]
    #slaveParams = {}
    #slaveParams["recoJetPtThreshold"] = 35
    #slaveParams["hltCollection"] = "hltAK5PFJetL1FastL2L3Corrected"

    # note - remove maxFiles parameter in order to run on all files
    slaveParams = {}
    slaveParams["threshold"] = 35.
    #slaveParams["recoJetCollection"] = "pfJets"
    slaveParams["recoJetCollection"] = "pfJetsSmear"
    #slaveParams["recoJetCollection"] = "caloJets"
    #slaveParams["recoJetCollection"] = "caloJetsSmear"

    MNxsAnalyzer.runAll(treeName="mnXS",
                               slaveParameters=slaveParams,
                               sampleList=sampleList,
                               maxFiles = 1,
                               #nWorkers=1,
                               outFile = "~/plotsMNxs.root" )



    #MNxsAnalyzer.testAll()

