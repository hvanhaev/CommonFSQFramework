#!/usr/bin/env python


import sys, os, time, math
sys.path.append(os.path.dirname(__file__))

import ROOT
ROOT.gROOT.SetBatch(True)
from ROOT import *

from array import *

# please note that python selector class name (here: L1Rate) 
# should be consistent with this file name (L1Rate.py)

# you have to run this file from directory where it is saved

import MNTriggerStudies.MNTriggerAna.ExampleProofReader 
import MNTriggerStudies.MNTriggerAna.Style

class L1Rate(MNTriggerStudies.MNTriggerAna.ExampleProofReader.ExampleProofReader):
    def init(self):
        # run MNTriggerAna/test/mnTrgAnalyzer/utils/GetFlatPUDist.py
        puFile = edm.FileInPath("MNTriggerStudies/MNTriggerAna/test/mnTrgAnalyzer/PUhists.root").fullPath()

        self.newlumiWeighters = {}
        self.newlumiWeighters["flat2050toPU15"] = edm.LumiReWeighting(puFile, puFile, "Flat20to50/pileup", "PU15/pileup")
        self.newlumiWeighters["flat2050toPU20"] = edm.LumiReWeighting(puFile, puFile, "Flat20to50/pileup", "PU20/pileup")
        self.newlumiWeighters["flat2050toPU25"] = edm.LumiReWeighting(puFile, puFile, "Flat20to50/pileup", "PU25/pileup")
        self.newlumiWeighters["flat2050toPU30"] = edm.LumiReWeighting(puFile, puFile, "Flat20to50/pileup", "PU30/pileup")

        #self.newlumiWeighters["flat2050toPU35"] = edm.LumiReWeighting(puFile, puFile, "Flat20to50/pileup", "PU35/pileup")
        #self.newlumiWeighters["flat2050toPU40"] = edm.LumiReWeighting(puFile, puFile, "Flat20to50/pileup", "PU40/pileup")
        #self.newlumiWeighters["flat2050toPU45"] = edm.LumiReWeighting(puFile, puFile, "Flat20to50/pileup", "PU45/pileup")
        #self.newlumiWeighters["flat2050toPU50"] = edm.LumiReWeighting(puFile, puFile, "Flat20to50/pileup", "PU50/pileup")

        #self.newlumiWeighters["PU20toPU20"] = edm.LumiReWeighting(puFile, puFile, "PU20/pileup", "PU20/pileup")
        #self.newlumiWeighters["PU20toPU15"] = edm.LumiReWeighting(puFile, puFile, "PU20/pileup", "PU15/pileup")
        #self.newlumiWeighters["PU20toPU25"] = edm.LumiReWeighting(puFile, puFile, "PU20/pileup", "PU25/pileup")
 
        self.histos = {}
        self.histoDenoms = {}

        todo = []
        todo.append( ("L1SingleJet", 32.5, 177.5) )
        #todo.append( ("L1SingleJet", 150.5, 250.5) )
        #todo.append( ("L1SingleJet", 49.5, 61.5) )
        #todo.append( ("L1DoubleJetCF", 29.5, 71.5) )
        #todo.append( ("L1DoubleJet35CFDphi", 1.99, 3.15) )
        #todo.append( ("L1DoubleJet35CFDphi", -0.01, 3.15) )
        for w in self.newlumiWeighters:
            for t in todo:
                name = t[0]+"_"+w
                binL = t[1]
                binH = t[2]
                nbins = binH - binL
                if t[0] == "L1DoubleJet35CFDphi": 
                    nbins = 30

                pu=w.split("PU")[1]
                yLabel = t[0]+ "@PU="+pu + " rate [Hz]"
                self.histos[name] = ROOT.TH1D(name, name+";Threshold [GeV];"+yLabel, int(nbins), binL, binH)
                self.histos[name].SetMarkerSize(0.5)
                self.histos[name].SetMarkerStyle(20)
                self.histos[name].Sumw2()
                self.GetOutputList().Add(self.histos[name])
                nameDenom = name+"Denom"
                self.histoDenoms[nameDenom] = ROOT.TH1D(nameDenom, nameDenom, 1, -0.5, 0.5)
                self.histoDenoms[nameDenom].Sumw2()
                self.GetOutputList().Add(self.histoDenoms[nameDenom])

                nameDist = name+"Dist"
                self.histos[nameDist] = ROOT.TH1D(nameDist, nameDist, 261, -0.5, 260.5)
                self.histos[nameDist].Sumw2()
                self.GetOutputList().Add(self.histos[nameDist])




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


    #  0.0 0.34906578064 0.698131561279 1.04719740549 1.39626330534 1.74532920519 2.09439510107 2.44346088568 2.79252672195 3.14159256617
    def getBestMaxSeparation(self, jets, ptThr):
        bestDphi = -1
        for i in xrange(jets.size()):
            iJet = jets.at(i)
            if iJet.pt() < ptThr: continue
            if abs(iJet.eta()) > 1.7: continue
            for j in xrange(i+1, jets.size()):
                jJet = jets.at(j)
                if jJet.pt() < ptThr: continue
                if abs(jJet.eta()) < 2.5: continue
                dphi = abs(ROOT.Math.VectorUtil.DeltaPhi(iJet, jJet))
                if bestDphi < dphi: bestDphi = dphi
        return bestDphi


    def analyze(self):
        #puAvg = self.fChain.puTrueNumInteractions
        #if puAvg < 20 or puAvg > 22: return 0


        hardestL1 = -1
        hardestL1Central = -1
        hardestL1Forwad  = -1

        #l1jets = getattr(self.fChain, "stage1L1Jets")
        #l1jets = getattr(self.fChain, "L1Jets")
        l1jets = getattr(self.fChain, self.l1col)

        for i in xrange(l1jets.size()):
            jetI = l1jets.at(i)
            ptI = jetI.pt()
            if hardestL1 < ptI:
                hardestL1 = ptI
            etaI = abs(jetI.eta())
            if etaI < 1.7 and hardestL1Central < ptI:
                hardestL1Central = ptI
            if etaI > 2.5 and hardestL1Forwad < ptI:
                hardestL1Forwad = ptI

        doubleJetCFSeedMaxThr = min(hardestL1Central, hardestL1Forwad)

        pu = self.fChain.PUNumInteractions

        dphiMax = self.getBestMaxSeparation(l1jets, 35)
        #print "TTTT", dphiMax

        #print hardestL1, int(hardestL1)
        for w in self.newlumiWeighters:
            weight = self.newlumiWeighters[w].weight(pu)
            self.fillRate(self.histos["L1SingleJet_"+w], hardestL1, weight)
            self.histoDenoms["L1SingleJet_"+w+"Denom"].Fill(0, weight)
            self.histos["L1SingleJet_"+w+"Dist"].Fill(hardestL1, weight)
            #self.fillRate(self.histos["L1DoubleJetCF_"+w], doubleJetCFSeedMaxThr, weight)
            #self.histoDenoms["L1DoubleJetCF_"+w+"Denom"].Fill(0, weight)

            #self.fillRate(self.histos["L1DoubleJet35CFDphi_"+w], dphiMax, weight)
            #self.histoDenoms["L1DoubleJet35CFDphi_"+w+"Denom"].Fill(0, weight)

    def finalize(self):
        #print "Finalize:"
        #normFactor = self.getNormalizationFactor()
        pass

    def finalizeWhenMerged(self):
        olist =  self.GetOutputList()
        histos = {}
        for o in olist:
            if not "TH1" in o.ClassName(): continue
            histos[o.GetName()]=o

        lhcFreq = 4E7 # 40 MHz
        totalBunches = 3564.
        #  (usually 2662 for 25ns bunch spacing, 1331 for 50ns bunch spacing) 
        filledBunches = 2662.

        factor = float(lhcFreq)*filledBunches/totalBunches
        avaliableHistos = []
        for h in histos:
            if "Denom" in h: continue
            if "Dist" in h: continue
            #raise "HERE"
            # ptint XXXXX
            denom = histos[h+"Denom"].GetBinContent(1)
            #print "DDD", denom
            '''
            for iBin in xrange(1, histos[h].GetNbinsX()+1):
                binCont =  histos[h].GetBinContent(iBin)
                pu = int(h.split("_")[1].split("PU")[1])
                prob = 1-math.exp(-pu*binCont/denom  )
                err = pu*((math.sqrt(binCont + ((binCont)**2)/denom))/denom)
                histos[h].SetBinContent(iBin, factor*prob)
                histos[h].SetBinError(iBin, err)

                # rateerr_mc = xs * ilumi * ((math.sqrt(counts + ((counts)**2)/nevt))/nevt)
            '''
                

            histos[h].Scale(factor/denom)
            avaliableHistos.append(h)

        # L1SingleJet_flat2050toPU50
        puPoints = {}
        for h in avaliableHistos:
            if "PU" not in h: continue
            pu = int(h.split("_")[1].split("PU")[-1])
            puPoints[pu] = h.split("_")[1]

        del avaliableHistos

        binL = min(puPoints.keys())-1.5
        binH = max(puPoints.keys())+1.5
        nbins = int(binH-binL)


        #'''  l1 jet scale:  12 16 20 24 28 32.0 36.0 40.0 44.0 48.0 52.0 56.0 60.0 64.0 68.0 72.0 76.0 80.0 84.0 88.0 92.0    '''
        todo = []
        todo.append( ("L1SingleJet", 36 ) ) # (seed name, threshold)
        todo.append( ("L1SingleJet", 52 ) ) # (seed name, threshold)
        todo.append( ("L1SingleJet", 68 ) ) # (seed name, threshold)
        todo.append( ("L1SingleJet", 92 ) ) # (seed name, threshold)
        todo.append( ("L1SingleJet", 128 ) ) # (seed name, threshold)
        todo.append( ("L1SingleJet", 176 ) ) # (seed name, threshold)
        #todo.append( ("L1SingleJet", 200 ) ) # (seed name, threshold)
        #todo.append( ("L1SingleJet", 240 ) ) # (seed name, threshold)

        '''
        todo.append( ("L1DoubleJetCF", 32 ) ) # (seed name, threshold)
        todo.append( ("L1DoubleJetCF", 36 ) ) # (seed name, threshold)
        todo.append( ("L1DoubleJetCF", 40 ) ) # (seed name, threshold)
        todo.append( ("L1DoubleJetCF", 44 ) ) # (seed name, threshold)
        todo.append( ("L1DoubleJetCF", 48 ) ) # (seed name, threshold)
        todo.append( ("L1DoubleJetCF", 52 ) ) # (seed name, threshold)
        todo.append( ("L1DoubleJetCF", 68 ) ) # (seed name, threshold)
        todo.append( ("L1DoubleJet35CFDphi", 2.7 ) ) # (seed name, threshold)
        
        #'''
        for t in todo:
            seed = t[0]
            thr =  t[1]
            histoname = "rateVsPU_"+seed+str(thr).replace(".","_")
            yLabel = seed+str(thr) + " rate [Hz]"
            hist = ROOT.TH1F(histoname, histoname+";PU;" + yLabel, nbins, binL, binH)
            hist.SetMarkerSize(0.5)
            hist.SetMarkerStyle(20)
            hist.Sumw2()
            for pu in puPoints:
                h = seed + "_"+  puPoints[pu]
                #binNumberForThisThrForThisPU = histos[h].GetBin(thr)
                binNumberForThisThrForThisPU = histos[h].FindBin(thr)
                #print "AAAA reading histo=", h, "bin=", binNumberForThisThrForThisPU, "thr=", thr
                rate = histos[h].GetBinContent(binNumberForThisThrForThisPU)
                rateErr = histos[h].GetBinError(binNumberForThisThrForThisPU)
                targetBin = hist.FindBin(pu)
                hist.SetBinContent(targetBin, rate)
                hist.SetBinError(targetBin,   rateErr)
                #print "XXXX", targetBin, pu, rate, rateErr
            self.GetOutputList().Add(hist)

        olist =  self.GetOutputList()
        MNTriggerStudies.MNTriggerAna.Style.setStyle()


        curPath = ROOT.gDirectory.GetPath()
        of = ROOT.TFile("~/tmp/l1hist.root","RECREATE")
        ROOT.gDirectory.cd(curPath)


        for o in olist:
            if not "TH1" in o.ClassName(): continue
            if "Denom" in o.GetName(): continue
            c1 = ROOT.TCanvas()
            c1.SetLeftMargin(0.2)
            fname = "~/tmp/" + o.GetName() + ".png"
            o.Draw("e1 p")
            o.GetYaxis().SetTitleOffset(2)
            c1.Print(fname)
            of.WriteTObject(o, o.GetName())



if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    ROOT.gSystem.Load("libFWCoreFWLite.so")
    AutoLibraryLoader.enable()

    sampleList = ["Neutrino_Pt-2to20_gun"] # run through all
    #sampleList =  ["Neutrino_Pt-2to20_gun_162"]
    maxFilesMC = None
    nWorkers = None

    # '''
    #maxFilesMC = 1
    #nWorkers = 1
    # '''
    #maxFilesMC = 32

    slaveParams = {"l1col": "stage1L1Jets" }
    #slaveParams = {"l1col": "oldL1Jets" }
    # select hltCollection here (see plugins/MNTriggerAna.cc to learn whats avaliable):

    # note - remove maxFiles parameter in order to run on all files
    #L1Rate.runAll(treeName="L1JetsRateAna",
    L1Rate.runAll(treeName="MNTriggerAnaNew",
                               slaveParameters=slaveParams,
                               sampleList=sampleList,
                               maxFilesMC = maxFilesMC,
                               nWorkers=nWorkers,
                               outFile = "L1RatePlots.root" )
                                
