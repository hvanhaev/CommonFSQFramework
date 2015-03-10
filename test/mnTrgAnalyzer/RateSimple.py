#!/usr/bin/env python


import sys, os, time, math
sys.path.append(os.path.dirname(__file__))

import ROOT
ROOT.gROOT.SetBatch(True)
from ROOT import *

from array import *

# please note that python selector class name (here: RateSimple) 
# should be consistent with this file name (RateSimple.py)

# you have to run this file from directory where it is saved

import MNTriggerStudies.MNTriggerAna.ExampleProofReader 

import BaseTrigger

class RateSimple(MNTriggerStudies.MNTriggerAna.ExampleProofReader.ExampleProofReader):
    def init(self):
        self.cnt = 0

        binL = -0.5
        binH = 61.5
        nbins = int(binH-binL)

        self.dist = ROOT.TH1F("dist", "; jet seed threshold", nbins, binL, binH )
        self.dist.Sumw2()
        self.GetOutputList().Add(self.dist)

        puFile = edm.FileInPath("MNTriggerStudies/MNTriggerAna/test/mnTrgAnalyzer/PUhists.root").fullPath()
        self.newlumiWeighters = {}
        '''
        self.newlumiWeighters["flat2050toPU40"] = edm.LumiReWeighting(puFile, puFile, "Flat20to50/pileup", "PU40/pileup")
        self.newlumiWeighters["flat2050toPU30"] = edm.LumiReWeighting(puFile, puFile, "Flat20to50/pileup", "PU30/pileup")
        #self.newlumiWeighters["flat2050toPU25"] = edm.LumiReWeighting(puFile, puFile, "Flat20to50/pileup", "PU25/pileup")
        self.newlumiWeighters["flat2050toPU20"] = edm.LumiReWeighting(puFile, puFile, "Flat20to50/pileup", "PU20/pileup")
        self.newlumiWeighters["flat2050toPU15"] = edm.LumiReWeighting(puFile, puFile, "Flat20to50/pileup", "PU15/pileup")
        self.newlumiWeighters["flat2050toPU10"] = edm.LumiReWeighting(puFile, puFile, "Flat20to50/pileup", "PU10/pileup")
        #'''
        #self.newlumiWeighters["flat010toPU10"] = edm.LumiReWeighting(puFile, puFile, "Flat0to10/pileup", "PU10/pileup")
        #self.newlumiWeighters["flat010toPU1"] = edm.LumiReWeighting(puFile, puFile, "Flat0to10/pileup", "PU1/pileup")
        #self.newlumiWeighters["PU20toPU20"] = edm.LumiReWeighting(puFile, puFile, "PU20/pileup", "PU20/pileup")


        self.dists = {}
        for pu in self.newlumiWeighters:
            dist = ROOT.TH1F(pu, "; jet seed threshold",  nbins, binL, binH )
            dist.Sumw2()
            self.dists[pu] = dist
            self.GetOutputList().Add(dist)


    def fillRate(self, hist, maxThr, weight):
        nbins = hist.GetNbinsX()



    def fillRate(self, hist, maxThr, weight):
        nbins = hist.GetNbinsX()
        getBinCenter = hist.GetXaxis().GetBinCenter
        for i in xrange(1,nbins+1):
            #binCenter = int(getBinCenter(i))
            binCenter = getBinCenter(i)

            # As always "<=" is a tricky thing...
            if binCenter < maxThr or abs(binCenter-maxThr) < 0.1:
                hist.Fill(binCenter, weight)
            else:
                break
        del getBinCenter

    def single(self, jets, etaMin = None, etaMax = None):
        #bestJet = max(jets, key=lambda j: j.pt())
        #maxThr = bestJet.pt()
        maxThr = 0.
        for i in xrange(jets.size()):
            eta = abs(jets.at(i).eta())
            if etaMin != None and eta < etaMin: continue
            if etaMax != None and eta > etaMax: continue
            pt = jets.at(i).pt()
            if pt > maxThr:
                maxThr = pt


        return maxThr

    def doubleJet(self, jets, fb=False):
        maxThr = 0.
        for i in xrange(jets.size()):
            for j in xrange(i+1, jets.size()):
                if fb:
                    eta1 =  jets.at(i).eta()
                    if abs(eta1) < 3.: continue
                    eta2 =  jets.at(j).eta()
                    if abs(eta2) < 3.: continue
                    if eta1*eta2 > 0 : continue

                contender = min(jets.at(i).pt(), jets.at(j).pt())
                if contender > maxThr:
                    maxThr = contender
        return maxThr

    def doubleJetAve(self, jets, probeCentral = False, etaProbeLimit = 2.7):
        maxThr = 0.
        ptmin = 10.
        for i in xrange(jets.size()):
            ptI = jets.at(i).pt()
            if ptI < ptmin: continue

            etaI = abs(jets.at(i).eta())
            if etaI >  1.4: continue
            for j in xrange(0, jets.size()):
                if i == j: continue

                ptJ = jets.at(j).pt()
                if ptJ < ptmin: continue

                etaJ = abs(jets.at(j).eta())
                if not probeCentral:
                    if etaJ <  etaProbeLimit: continue
                else:
                    if etaJ >  etaProbeLimit: continue
                dphi = abs(ROOT.Math.VectorUtil.DeltaPhi(jets.at(j), jets.at(i)))
                if dphi < 2.5: continue

                ptAve = (ptI + ptJ)/2.
                if ptAve > maxThr: maxThr = ptAve

        return maxThr

    def analyze(self):
        #jets  = self.fChain.oldRedoneL1Jets
        #jets  = self.fChain.oldL1Jets
        #jets  = self.fChain.hltAK4PFJets
        #jets = self.fChain.hltAK4PFJetsCorrected
        jets = self.fChain.hltAK4PFJetsCorrectedp4
        #jets = self.fChain.ak4GenJets

        maxThr = 0
        try:

            '''
            #   trgDiPFJet15FBEta2
            #   trgDiPFJet15FBEta3
            maxThr = self.doubleJet(jets, True)
            if  maxThr > 15. and self.fChain.trgDiPFJet15FBEta2 == 0:
                print "AAA", maxThr, self.fChain.trgDiPFJet15FBEta3

            if  maxThr < 15. and self.fChain.trgDiPFJet15FBEta2 == 1:
                print "BBB", maxThr, self.fChain.trgDiPFJet15FBEta3
            '''

            '''
            maxThr = self.doubleJet(jets, False)
            if  maxThr > 15. and self.fChain.trgDiPFJet15 == 0:
                print "AAA", maxThr, self.fChain.trgDiPFJet15
            if  maxThr < 15. and self.fChain.trgDiPFJet15 == 1:
                print "BBB", maxThr, self.fChain.trgDiPFJet15
            '''


            '''
            maxThrC = self.doubleJetAve(jets, probeCentral=True)
            maxThrCF = self.doubleJetAve(jets, probeCentral=False)
            todoThr = [15,25,35]
            for t in todoThr:
                cen = getattr(self.fChain, "trgDiPFJetAve"+str(t)+"Central")
                hf  = getattr(self.fChain, "trgDiPFJetAve"+str(t)+"HFJEC")
                #print "AA", cen, hf, maxThrC, maxThrCF
                if maxThrC > t and cen == 0:
                    print "AAA"+str(t), maxThrC, cen
                if maxThrC < t and cen == 1:
                    print "BBB"+str(t), maxThrC, cen
                if maxThrCF > t and hf == 0:
                    print "CCC"+str(t), maxThrCF, hf
                if maxThrCF < t and hf == 1:
                    print "DDD"+str(t), maxThrCF, hf
            '''
            '''
            maxThr = self.single(jets)
            maxThrE2 = self.single(jets, etaMin=2.)
            maxThrE3 = self.single(jets, etaMin=3.)
            todoThr = [15,25,40]
            for t in todoThr:
                base = getattr(self.fChain, "trgPFJet"+str(t)) == 1
                eta2 = getattr(self.fChain, "trgPFJet"+str(t)+"FwdEta2") == 1
                eta3 = getattr(self.fChain, "trgPFJet"+str(t)+"FwdEta3") == 1
                if base != (maxThr > t):
                    print "AAA"+str(t), base, maxThr
                if eta2 != (maxThrE2 > t):
                    print "BBB"+str(t), eta2, maxThrE2
                if eta3 != (maxThrE3 > t):
                    print "CCC"+str(t), eta3, maxThrE3
            '''


                
            maxThr = self.doubleJet(jets)
            #maxThr = self.doubleJetAve(jets)
            #maxThr = self.doubleJetAve(jets, probeCentral=True)
            #maxThr = self.doubleJetAve(jets, etaProbeLimit=3.139)
            #maxThr = self.single(jets)
            #maxThr = self.single(jets, etaMin=2.)
            #maxThr = self.single(jets, etaMin=3.)
            #maxThr = self.single(jets, etaMax=1.4)
        except ValueError:
            maxThr = 0

        self.fillRate(self.dist, maxThr, 1.)
        pu = self.fChain.PUNumInteractions
        for l in self.newlumiWeighters:
            wPU = self.newlumiWeighters[l].weight(pu)
            self.fillRate(self.dists[l], maxThr, wPU)



    def finalizeWhenMerged(self):
        olist =  self.GetOutputList()
        histos = {}
        for o in olist:
            if not "TH1" in o.ClassName(): continue
            histos[o.GetName()]=o

        lhcFreq = 4E7 # 40 MHz
        totalBunches = 3564.
        #  (usually 2662 for 25ns bunch spacing, 1331 for 50ns bunch spacing) 
        #filledBunches = 40.
        filledBunches = 1331

        #PU=0.01
        #PU=0.4
        #PU=0.4
        PU=1

        rateScalingFactor = lhcFreq*float(filledBunches)/float(totalBunches)*PU

        todo = filter(lambda x: "dist" in x or "PU" in x, histos.keys())
        avoidGC = []

        res = {}
        for t in todo:
            name =  histos[t].GetName()
            eff = histos[t].Clone(name+"_eff")
            eff.Scale(1./(eff.GetBinContent(1)))

            rate = eff.Clone(name+"_rate")
            rate.Scale(rateScalingFactor)
            self.GetOutputList().Add(eff)
            self.GetOutputList().Add(rate)
            avoidGC.append(eff)
            avoidGC.append(rate)

            if "PU" in name:
                puVal = int(name.split("PU")[-1])
                print puVal, eff.GetBinCenter(15), eff.GetBinContent(15),  eff.GetBinError(15)
                res[puVal] = eff.GetBinContent(15)

                todoPT = [16, 36, 52, 68, 128, 176]
                for pt in todoPT:
                    bin = rate.FindBin(pt-1)
                    val = rate.GetBinContent(bin)
                    err = rate.GetBinError(bin)
                    rel = "-"
                    if val > 0:
                        rel = err/val
                    print "PU", puVal, "L1singleJet"+str(pt), val, err, rel



        for p in sorted(res.keys()):
            print "Prob at PU =",p, res[p]
'''
Info/Notes:

    - In case of NeutrinoGun sample this file allows to estimate what is the probability
        to find given trigger for given PU in ZeroBias

    - MinBias - rate estimation


'''


if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    ROOT.gSystem.Load("libFWCoreFWLite.so")
    AutoLibraryLoader.enable()

    sampleList = ["MinBias_TuneZ2star_13TeV_pythia6"]
    #sampleList = ["MinBias_TuneZ2star_13TeV_pythia6_162"]
    #sampleList = ["QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8"]
    #sampleList = ["Neutrino_Pt-2to20_gun"]
    #sampleList = ["Neutrino_Pt-2to20_gun_162"]
    maxFilesMC = 20
    nWorkers = 1
    slaveParams = {}


    # note - remove maxFiles parameter in order to run on all files
    RateSimple.runAll(treeName="MNTriggerAnaNew",
                               slaveParameters=slaveParams,
                               sampleList=sampleList,
                               maxFilesMC = maxFilesMC,
                               nWorkers=nWorkers,
                               outFile = "SimpleRatePlots.root" )
                                
