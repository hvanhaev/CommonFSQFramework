#!/usr/bin/env python
import MNTriggerStudies.MNTriggerAna.ExampleProofReader
from  MNTriggerStudies.MNTriggerAna.GenericGetter import GenericGetter

import sys, os, time
sys.path.append(os.path.dirname(__file__))

import ROOT
ROOT.gROOT.SetBatch(True)
from ROOT import edm

from itertools import ifilter


from array import *

class JECExperiments(MNTriggerStudies.MNTriggerAna.ExampleProofReader.ExampleProofReader):
    def init( self):
        #self.jetBranch = "hltAK4PFJetsCorrected"
        self.jetBranch = "hltAK4PFJets"
        #self.jetBranch = "pfAK4CHS"
        self.jets = GenericGetter(self.jetBranch, "eta") 

        self.hist = {}
        self.hist["pt"] =  ROOT.TH1F("pt",   "pt",  100, -0.5, 99.5)
        self.hist["ptGen"] =  ROOT.TH1F("ptGen",   "ptGen",  100, -0.5, 99.5)
        self.hist["rho"] =  ROOT.TH1F("rho",   "rho",  100, -0.5, 99.5)
        self.hist["area"] =  ROOT.TH1F("area",   "area",  100, 0, 1)
        self.hist["eta"] =  ROOT.TH1F("eta",   "eta",  100, -5.5, 5.5)
        self.hist["bestdr"] =  ROOT.TH1F("bestdr",   "bestdr",  100, 0, 2)
        self.hist["ptGenVsPtRec"] = ROOT.TH2F("ptGenVsPtRec", "ptGenVsPtRec", 100, 0, 100, 100, 0, 100)
        self.hist["ptGenVsPtRecPR"] = ROOT.TProfile("ptGenVsPtRecPR", "ptGenVsPtRecPR", 100, 0, 1000, 0, 1000)
        self.hist["deltaPtGenRecVsRho"] = ROOT.TProfile("deltaPtGenRecVsRho", "deltaPtGenRecVsRho", 100, 0, 100)
        self.hist["deltaPtGenRecVsRhoArea"] = ROOT.TProfile("deltaPtGenRecVsRhoArea", "deltaPtGenRecVsRhoArea", 100, 0, 100)
    
        self.hist["response"] =  ROOT.TH1F("response",   "response",  100, 0, 2)
        self.hist["responseVsGenPT"] = ROOT.TProfile("responseVsGenPT", "responseVsGenPT", 100, 0, 100, 0, 10)
        self.hist["responseVsEta"] = ROOT.TProfile("responseVsEta", "responseVsEta", 20, -5.5, 5.5, 0, 10)
        self.hist["responseVsPU"] = ROOT.TProfile("responseVsPU", "responseVsPU", 20, 0, 100, 0, 10)
        '''
            area
            bestdr
            eta
            pt
            ptGen
            ptGenRatio
            rho
        '''

        self.trees = {}
        self.trees["fit"] = ROOT.TTree("dataFit", "dataFit")
        self.GetOutputList().Add(self.trees["fit"])
        self.trees["val"] = ROOT.TTree("dataVal", "dataVal")
        self.GetOutputList().Add(self.trees["val"])

        self.var = {}
        self.var["weight"] = array('d', [0])
        self.var["ptRaw"] = array('d', [0])
        self.var["ptGen"] = array('d', [0])
        self.var["eta"] = array('d', [0])
        self.var["rho"] = array('d', [0])
        self.var["area"] = array('d', [0])
        for v in self.var:
            self.trees["fit"].Branch(v, self.var[v], v+"/D")
            self.trees["val"].Branch(v, self.var[v], v+"/D")



        for h in self.hist:
            self.hist[h].Sumw2()
            self.GetOutputList().Add(self.hist[h])

    def analyze(self):
        weight =  self.fChain.genWeight
        rho =  getattr(self.fChain, self.jetBranch+"rho")
        ev = self.fChain.event
        self.hist["rho"].Fill(rho, weight)
        #if  rho < 38: return
        #if  rho > 32 or rho < 28: return

        self.jets.newEvent(self.fChain)
        PU = self.fChain.PUNumInteractions 

       # self.hist["deltaPtGenRecVsRho"] = ROOT.TProfile("deltaPtGenRecVsRho", "deltaPtGenRecVsRho", 100, 0, 100, 0, 1000)
       # self.hist["deltaPtGenRecVsRhoArea"] = ROOT.TProfile("deltaPtGenRecVsRhoArea", "deltaPtGenRecVsRhoArea", 100, 0, 100, 0, 1000)


        if self.jets:
            # rank jets by pt & apply selection criteria (one step)
            ''' # for studies at given rho point
            jselect = lambda j: 1 if abs(j.eta) < 0.2 \
                            and j.pt > 40  \
                            and j.bestdr < 0.25 \
                            else 0
            '''
            jselect = lambda j: 1 if abs(j.eta) < 0.2 \
                            and j.pt > 40 \
                            and j.bestdr < 0.25 \
                            else 0


            rankAndSelect = lambda j: j.ptGen*jselect(j)
            #hardestJet = max(self.jets.get(""), key = rankAndSelect)
            #if not rankAndSelect(jet): continue
            for jet in ifilter(jselect, self.jets.get("")):
                pt = jet.pt
                eta = jet.eta
                ptGen = jet.ptGen
                area = jet.area
                deltaPT  = pt - ptGen
                self.hist["deltaPtGenRecVsRho"].Fill(rho, deltaPT, weight)
                self.hist["deltaPtGenRecVsRhoArea"].Fill(rho, deltaPT*area, weight)


                self.hist["pt"].Fill(pt, weight)
                self.hist["ptGen"].Fill(ptGen, weight)
                self.hist["area"].Fill(area, weight)
                self.hist["bestdr"].Fill(jet.bestdr, weight)
                self.hist["eta"].Fill(eta, weight)

                self.hist["ptGenVsPtRec"].Fill(pt, ptGen, weight)
                self.hist["ptGenVsPtRecPR"].Fill(pt, ptGen, weight)

                r = jet.ptGenRatio
                self.hist["response"].Fill(r, weight)
                self.hist["responseVsGenPT"].Fill(ptGen, r, weight) 
                self.hist["responseVsEta"].Fill(eta, r, weight)
                self.hist["responseVsPU"].Fill(PU, r, weight)

                self.var["weight"][0]=weight
                self.var["ptRaw"][0]=pt
                self.var["ptGen"][0]=ptGen
                self.var["eta"][0]=eta
                self.var["rho"][0]=rho
                self.var["area"][0]=area

                if ev % 2 == 0:
                    self.trees["fit"].Fill()
                else:
                    self.trees["val"].Fill()

        return


    def finalize(self):
        pass
        #print "Finalize:"
        #normFactor = self.getNormalizationFactor()
        #print "  applying norm", normFactor
        #for h in self.hist:
        #    self.hist[h].Scale(normFactor)

if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    ROOT.gSystem.Load("libFWCoreFWLite.so")
    ROOT.AutoLibraryLoader.enable()

    sampleList = None # run through all
    maxFilesMC = None # run through all ffiles found
    maxFilesData = None # same
    nWorkers = None # Use all cpu cores

    # debug config:
    # Run printTTree.py alone to get the samples list
    #sampleList = []
    #sampleList.append("QCD_Pt-15to3000_TuneZ2star_Flat_HFshowerLibrary_7TeV_pythia6")
    #maxFilesData = 1
    maxFilesMC = 1
    nWorkers = 1


    slaveParams = {}
    slaveParams["maxEta"] = 2.


    # use printTTree.py <sampleName> to see what trees are avaliable inside the skim file
    #JECExperiments.runAll(treeName="BFJecTreeProducerHighPT",
    JECExperiments.runAll(treeName="BFJecTreeProducer",
           slaveParameters=slaveParams,
           sampleList=sampleList,
           maxFilesMC = maxFilesMC,
           maxFilesData = maxFilesData,
           nWorkers=nWorkers,
           outFile = "plotsJECExperiments.root" )
