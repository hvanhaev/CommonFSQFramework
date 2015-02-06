#!/usr/bin/env python

import sys, os, time
sys.path.append(os.path.dirname(__file__))

import ROOT
ROOT.gROOT.SetBatch(True)
ROOT.gSystem.Load("libFWCoreFWLite.so")
ROOT.AutoLibraryLoader.enable()
from ROOT import edm, JetCorrectionUncertainty

from array import *

# please note that python selector class name (here: MCResolutionTreeProducer) 
# should be consistent with this file name (MCResolutionTreeProducer.py)

# you have to run this file from directory where it is saved
import MNTriggerStudies.MNTriggerAna.ExampleProofReader 
from MNTriggerStudies.MNTriggerAna.JetGetter import JetGetter

class MCResolutionTreeProducer(MNTriggerStudies.MNTriggerAna.ExampleProofReader.ExampleProofReader):
    def init(self):

        print "Params:", self.etaMax, self.ptMin
        self.normFactor = self.getNormalizationFactor()
        self.dr = ROOT.Math.VectorUtil.DeltaR

        self.tree = ROOT.TTree("data", "data")
        self.GetOutputList().Add(self.tree)

        puFile = edm.FileInPath("MNTriggerStudies/MNTriggerAna/test/mnTrgAnalyzer/PUhists.root").fullPath()
        self.newlumiWeighters = {}
        self.newlumiWeighters["flat010toPU1"] = edm.LumiReWeighting(puFile, puFile, "Flat0to10/pileup", "PU1/pileup")
        #self.newlumiWeighters["flat2050toPU20"] = edm.LumiReWeighting(puFile, puFile, "Flat20to50/pileup", "PU20/pileup")

        self.var = {}
        self.todoShifts = ["_central"]

        for t in self.todoShifts:
            #self.var["ptGen"+t] = array('d', [0])
            self.var["ptRec"+t] = array('d', [0])
            self.var["etaRec"+t] = array('d', [0])
            self.var["ptHLT"+t] = array('d', [0])
            self.var["hlt2recRatio"+t] = array('d', [0])
            self.var["jetType"+t] = array('d', [0])

        self.var["weight"] = array('d', [0])
        self.var["weightPU"] = array('d', [0])
        self.var["PU"] = array('d', [0])
        
        for v in self.var:
            self.tree.Branch(v, self.var[v], v+"/D")

        self.getters = {}
        '''
        ak4 =  JetGetter("PFAK4CHS")
        ak4.disableGenJet()
        self.getters["AK4CHS"] = ak4

        ak5 =  JetGetter("PFAK5CHS")
        ak5.disableGenJet()
        self.getters["AK5CHS"] = ak5

        ak5nochs =  JetGetter("PFAK5")
        ak5nochs.disableGenJet()
        self.getters["nochsAK5"] = ak5nochs
        '''

        self.getters["gen4"] = None
        #self.getters["gen5"] = None


        self.varE = {}
        sys.stdout.flush()

    def addExternalVar(self, names):
        for name in names:
            self.varE[name] =  0.
            self.var[name] = array('d', [0])
            self.tree.Branch(name, self.var[name], name+"/D")

            

    def setExternalVar(self, name, val):
        self.varE[name] = val

    def genWeight(self):
        #print "ASDFASD", self.fChain.genWeight
        return self.fChain.genWeight*self.normFactor

    def analyze(self):
        for v in self.var:
            self.var[v][0] = 0

        weight = self.genWeight()

        pu = self.fChain.PUNumInteractions
        for l in self.newlumiWeighters:
            wPU = self.newlumiWeighters[l].weight(pu)

        self.var["weight"][0] = weight
        self.var["weightPU"][0] = weight*wPU
        self.var["PU"][0] = pu




        hlt = self.fChain.hlt_EcalMultifit_HCALMethod2
        #hlt = self.fChain.PFAK4CHSnewjets
        #hlt = self.fChain.hltAK4PFJetsCorrected
        #hlt = self.fChain.hltAK5PFJetsCorrected
        for shift in self.todoShifts:
           for jetGetter in self.getters: 
                jetType = 4
                isGen = False
                if jetGetter == "gen4": 
                    self.getters[jetGetter] = self.fChain.ak4GenJets
                    isGen = True
                    jetType = -4
                elif jetGetter == "gen5": 
                    self.getters[jetGetter] = self.fChain.ak5GenJets
                    isGen = True
                    jetType = -5
                elif jetGetter.startswith("AK5"): 
                    jetType = 5
                    self.getters[jetGetter].newEvent(self.fChain)
                elif jetGetter.startswith("no"): 
                    jetType = 6
                    self.getters[jetGetter].newEvent(self.fChain)

                #print "----"
                #for jet in self.getters[jetGetter].get(shift):
                '''
                for jet in self.getters[jetGetter]:
                    ptRec = jet.pt()
                    if ptRec < self.ptMin: 
                        break # gen jets are pt sorted
                        continue
                    if ptRec > self.ptMax: continue
                    etaRec = abs(jet.eta())
                    if etaRec > self.etaMax: continue
                    for hltJet in hlt:
                        if isGen:
                            dr = self.dr(jet, hltJet)
                        else:
                            dr = self.dr(jet.p4(), hltJet)
                        if dr > 0.3: continue
                        ptHLT = hltJet.pt()
                        r = ptHLT/ptRec
                        self.var["ptRec"+shift][0] = ptRec
                        self.var["etaRec"+shift][0]= etaRec
                        self.var["ptHLT"+shift][0] = ptHLT
                        self.var["hlt2recRatio"+shift][0] = r
                        self.var["jetType"+shift][0] = jetType
                        self.tree.Fill()
                        break
                '''
                for hltJet in hlt:
                    bestJet = None
                    bestJetDR = None
                    for jet in self.getters[jetGetter]:
                        ptRec = jet.pt()
                        if ptRec < self.ptMin: 
                            break # gen jets are pt sorted
                        etaRec = abs(jet.eta())
                        if etaRec > self.etaMax: continue

                        if isGen:
                            dr = self.dr(jet, hltJet)
                        else:
                            dr = self.dr(jet.p4(), hltJet)
                        if dr > 0.3: continue
                        if bestJet == None or dr < bestJetDR:
                            bestJet = jet
                            bestJetDR = dr
                    if bestJet != None:
                        ptHLT = hltJet.pt()
                        ptRec = bestJet.pt()
                        etaRec = abs(bestJet.eta())
                        r = ptHLT/ptRec
                        #print bestJetDR
                        self.var["ptRec"+shift][0] = ptRec
                        self.var["etaRec"+shift][0]= etaRec
                        self.var["ptHLT"+shift][0] = ptHLT
                        self.var["hlt2recRatio"+shift][0] = r
                        self.var["jetType"+shift][0] = jetType
                        self.tree.Fill()
    






        return 1

    def finalize(self):
        print "Finalize:"
        #normFactor = self.getNormalizationFactor()
        #print "  applying norm", normFactor
        #for h in self.hist:
        #    self.hist[h].Scale(normFactor)

if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    ROOT.gSystem.Load("libFWCoreFWLite.so")
    ROOT.AutoLibraryLoader.enable()

    #sampleList = ["QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8",]
    #sampleList = ["QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8_Pu20",]
    #sampleList = ["QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8_Pu20to50"]
    sampleList = ["QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8_Pu0to10"]
    maxFilesMC = None
    maxFilesData = None
    nWorkers = None # Use all

    # debug config:
    '''
    sampleList=[]
    sampleList.append("QCD_Pt-15to3000_TuneZ2star_Flat_HFshowerLibrary_7TeV_pythia6")
    maxFilesData = 1
    '''
    maxFilesMC = 120
    #nWorkers = 1
    #'''

    slaveParams = {}
    slaveParams["ptMin"] = 30
    slaveParams["ptMax"] = 70
    slaveParams["etaMax"] = 5.2



    #MCResolutionTreeProducer.runAll(treeName="MNTriggerAnaNew",
    MCResolutionTreeProducer.runAll(treeName="MNTriggerAnaHLTJECOnFly",
                               slaveParameters=slaveParams,
                               sampleList=sampleList,
                               maxFilesMC = maxFilesMC,
                               maxFilesData = maxFilesData,
                               nWorkers=nWorkers,
                               outFile = "treeMCRes.root" )

