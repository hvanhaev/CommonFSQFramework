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
class LinearCorrector:
    def __init__(self, l):
        #BFJ -0.2 0.2 -47.9425538604 0.0 4.89909102873 | ERR
        spl = l.strip().split()
        self.etas = sorted(map(float, spl[1:3]))
        self.parms = map(float, spl[3:6])

    #ret = (par[0]+x[0]*par[1]); // x[0] - pt
    #ret += par[2]*x[1]; // x[1] - rho*area
    def corr(self, pt, rho):
        return self.parms[0]+self.parms[1]*pt + self.parms[2]*rho


#    double ptSignalAndPU  = (a+b*par[1]);
#    double PUcorrection = (pu1+pu2*ptSignalAndPU +   pu3/(pu4+pu5*ptSignalAndPU))*x[1]+pu6;
class FancyCorrector:
    def __init__(self, l):
        #BFJ -0.2 0.2 -47.9425538604 0.0 4.89909102873 | ERR
        spl = l.strip().split()
        self.etas = sorted(map(float, spl[1:3]))
        self.parms = map(float, spl[3:11])

    def corr(self, pt, rhoarea):
        ptSignalAndPU  = (self.parms[0]+self.parms[1]*pt)
        pu1 = self.parms[2]
        pu2 = self.parms[3]
        pu3 = self.parms[4]
        pu4 = self.parms[5]
        pu5 = self.parms[6]
        pu6 = self.parms[7]
        PUcorrection = (pu1+pu2*ptSignalAndPU +   pu3/(pu4+pu5*ptSignalAndPU))*rhoarea+pu6
        return ptSignalAndPU+PUcorrection


class JECExperiments(MNTriggerStudies.MNTriggerAna.ExampleProofReader.ExampleProofReader):
    def init( self):
        self.correctors = []
        with open(self.jecDefPath)  as inf:
            for l in inf:
                #c = LinearCorrector(l)
                c = FancyCorrector(l)
                self.correctors.append( (c, c.etas[0], c.etas[1]) )

        print self.correctors


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
        
        self.ptPoints = [15, 20, 25, 30, 35, 40, 45]
        for p in self.ptPoints:
            n1 = "deltaPtGenRecVsRho_"+str(p)
            n2 = "deltaPtGenRecVsRhoArea_"+str(p)
            n3 = "deltaR_"+str(p)
            self.hist[n1] = ROOT.TProfile(n1, n1, 100, 0, 100)
            self.hist[n2] = ROOT.TProfile(n2, n2, 100, 0, 100)
            self.hist[n3] =  ROOT.TH1F(n3, n3,  100, 0, 2)

        self.rhoPoints = [20, 25, 30, 35, 40]
        for p in self.rhoPoints:
            n1 = "ptGenVsPtRecPR_"+str(p)
            self.hist[n1] = ROOT.TProfile(n1, n1, 100, 0, 1000, 0, 1000)
            
            
            


        prefixes = ["", "my_"]
        for p in prefixes:
            self.hist[p+"response"] =  ROOT.TH1F(p+"response",   p+"response",  100, 0, 2)
            self.hist[p+"responseVsGenPT"] = ROOT.TProfile(p+"responseVsGenPT", p+"responseVsGenPT", 100, 0, 100, 0, 10)
            self.hist[p+"responseVsEta"] = ROOT.TProfile(p+"responseVsEta", p+"responseVsEta", 20, -5.5, 5.5, 0, 10)
            self.hist[p+"responseVsPU"] = ROOT.TProfile(p+"responseVsPU", p+"responseVsPU", 20, 0, 100, 0, 10)
            # PU, genPT -> response
            self.hist[p+"responseVsPUVsGenPT"] = ROOT.TProfile2D(p+"responseVsPUVsGenPT", p+"responseVsPUVsGenPT", 20, 0, 100,  \
                                                                                                                 100, 0, 100, \
                                                                                                                 0, 10) 



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
        self.var["rhoarea"] = array('d', [0])
        self.var["deltaPtRawGen"] = array('d', [0])
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
                            and j.pt > 15 \
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
                # calibrated stuff
                for c in self.correctors:
                    #if eta ...
                    corrected = c[0].corr(pt, rho*area)
                    myR = ptGen/corrected
                    self.hist["my_response"].Fill(myR, weight)
                    self.hist["my_responseVsGenPT"].Fill(ptGen, myR, weight) 
                    self.hist["my_responseVsEta"].Fill(eta, myR, weight)
                    self.hist["my_responseVsPU"].Fill(PU, myR, weight)
                    self.hist["my_responseVsPUVsGenPT"].Fill(PU, ptGen, myR, weight)

            
                for p in self.ptPoints:
                    if ptGen > p and ptGen < p+2:
                        n1 = "deltaPtGenRecVsRho_"+str(p)
                        n2 = "deltaPtGenRecVsRhoArea_"+str(p)
                        n3 = "deltaR_"+str(p)
                        self.hist[n1].Fill(rho,  deltaPT, weight) 
                        self.hist[n2].Fill(rho, deltaPT*area, weight)
                        self.hist[n3].Fill(jet.bestdr, weight)

                for p in self.rhoPoints:
                    if rho > p and rho < p+2:
                        n1 = "ptGenVsPtRecPR_"+str(p)
                        self.hist[n1].Fill(pt, ptGen, weight)
                    


                # 
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
                self.hist["responseVsPUVsGenPT"].Fill(PU, ptGen, r, weight)

                self.var["weight"][0]=weight
                self.var["ptRaw"][0]=pt
                self.var["ptGen"][0]=ptGen
                self.var["deltaPtRawGen"][0]=pt-ptGen
                self.var["eta"][0]=eta
                self.var["rho"][0]=rho
                self.var["area"][0]=area
                self.var["rhoarea"][0]=area*rho

                if True: # ev % 2 == 0:
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
    #maxFilesMC = 1
    #nWorkers = 1


    slaveParams = {}
    slaveParams["maxEta"] = 2.
    #slaveParams["jecDefPath"] = os.getcwd()+"/"+"bfj15to100.txt"
    #slaveParams["jecDefPath"] = os.getcwd()+"/"+"bfj15to1000.txt"
    #slaveParams["jecDefPath"] = os.getcwd()+"/"+"bfj15to1000_genWeight.txt"
    slaveParams["jecDefPath"] = os.getcwd()+"/"+"bfj30to1000_genWeight.txt"


    # use printTTree.py <sampleName> to see what trees are avaliable inside the skim file
    JECExperiments.runAll(treeName="BFJecTreeProducer",
    #JECExperiments.runAll(treeName="BFJecTreeProducerHighPT",
           slaveParameters=slaveParams,
           sampleList=sampleList,
           maxFilesMC = maxFilesMC,
           maxFilesData = maxFilesData,
           nWorkers=nWorkers,
           outFile = "plotsJECExperiments.root" )
