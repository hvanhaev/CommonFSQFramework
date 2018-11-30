#!/usr/bin/env python
#
#

import CommonFSQFramework.Core.ExampleProofReader

import sys, os, time
sys.path.append(os.path.dirname(__file__))
from os import listdir
from os.path import isfile, join
import ROOT
from math import sqrt, log10, log
from array import *

import numpy as np

# needs to be taken times 2.7
kLookUpTableADCtoCharge = [ 1,2,3,4,5,6,7,8,9,10,
                            11,12,13,14,15,16,18,20,22,24,
                            26,28,31,34,37,40,43,47,51,56,
                            61,66,61,66,71,76,81,86,91,96,
                            101,106,111,116,121,126,131,138,148,158,
                            168,178,188,198,211,226,241,256,273,293,
                            313,336,361,386,361,386,411,436,461,486,
                            511,536,561,586,611,636,661,686,711,748,
                            798,848,898,948,998,1048,1111,1186,1261,1336,
                            1423,1523,1623,1736,1861,1986,1861,1986,2047,2047,
                            2047,2047,2047,2047,2047,2047,2047,2047,2047,2047,
                            2047,2047,2047,2047,2047,2047,2047,2047,2047,2047,
                            2047,2047,2047,2047,2047,2047,2047,2047 ]


BadChannels = [#[2,1],
    [2,10], # extra bad channel !!! from L1 noise
    [16,6],
    [11,14],
    [3,8],
    [15,12],
    [3,11]]

class CastorPlots(CommonFSQFramework.Core.ExampleProofReader.ExampleProofReader):
    def init( self, maxEvents = None):

        self.maxEvents = maxEvents
                
        self.hist = {}
        self.hist["EventCounter"] = ROOT.TH1D("EventCounter","EventCounter",10,0,20)
        
        # the castor data
        self.hist["castor_channel_2d"] =  ROOT.TH2D("castor_channel_2d", "castor_channel_2d", 14, 0.5, 14.5, 16, 0.5, 16.5)
        self.hist["castor_tower"] =  ROOT.TH1D("castor_tower", "castor_tower", 300, -10, 20)
        self.hist["castor_total"] =  ROOT.TH1D("castor_total", "castor_total", 300, -10, 20)

        self.hist["hottest_tower"] =  ROOT.TH1D("hottest_tower", "hottest_tower", 500, -50, 2000)
        self.hist["hottest_tower_em"] =  ROOT.TH1D("hottest_tower_em", "hottest_tower_em", 500, -50, 2000)
        self.hist["hottest_tower_had"] =  ROOT.TH1D("hottest_tower_had", "hottest_tower_had", 500, -50, 2000)

        self.hist["hottest_tower_494"] =  ROOT.TH1D("hottest_tower_494", "hottest_tower_494", 500, -50, 2000)
        self.hist["hottest_tower_em_505"] =  ROOT.TH1D("hottest_tower_em_505", "hottest_tower_em_505", 500, -50, 2000)
        self.hist["hottest_tower_had_505"] =  ROOT.TH1D("hottest_tower_had_505", "hottest_tower_had_505", 500, -50, 2000)

        self.hist["hottest_tower_BptxPlus"] =  ROOT.TH1D("hottest_tower_BptxPlus", "hottest_tower_BptxPlus", 500, -50, 2000)
        self.hist["hottest_tower_em_BptxPlus"] =  ROOT.TH1D("hottest_tower_em_BptxPlus", "hottest_tower_em_BptxPlus", 500, -50, 2000)
        self.hist["hottest_tower_had_BptxPlus"] =  ROOT.TH1D("hottest_tower_had_BptxPlus", "hottest_tower_had_BptxPlus", 500, -50, 2000)

        self.hist["hottest_tower_BptxMinus"] =  ROOT.TH1D("hottest_tower_BptxMinus", "hottest_tower_BptxMinus", 500, -50, 2000)
        self.hist["hottest_tower_em_BptxMinus"] =  ROOT.TH1D("hottest_tower_em_BptxMinus", "hottest_tower_em_BptxMinus", 500, -50, 2000)
        self.hist["hottest_tower_had_BptxMinus"] =  ROOT.TH1D("hottest_tower_had_BptxMinus", "hottest_tower_had_BptxMinus", 500, -50, 2000)

        self.hist["hottest_tower_NotBptxOR"] =  ROOT.TH1D("hottest_tower_NotBptxOR", "hottest_tower_NotBptxOR", 500, -50, 2000)
        self.hist["hottest_tower_em_NotBptxOR"] =  ROOT.TH1D("hottest_tower_em_NotBptxOR", "hottest_tower_em_NotBptxOR", 500, -50, 2000)
        self.hist["hottest_tower_had_NotBptxOR"] =  ROOT.TH1D("hottest_tower_had_NotBptxOR", "hottest_tower_had_NotBptxOR", 500, -50, 2000)

        self.hist["hottest_tower_digi_BptxPlus"] =  ROOT.TH1D("hottest_tower_digi_BptxPlus", "hottest_tower_digi_BptxPlus", 500, -50, 2000)
        self.hist["hottest_tower_digi_em_BptxPlus"] =  ROOT.TH1D("hottest_tower_digi_em_BptxPlus", "hottest_tower_digi_em_BptxPlus", 500, -50, 2000)
        self.hist["hottest_tower_digi_had_BptxPlus"] =  ROOT.TH1D("hottest_tower_digi_had_BptxPlus", "hottest_tower_digi_had_BptxPlus", 500, -50, 2000)

        self.hist["hottest_tower_digi_BptxMinus"] =  ROOT.TH1D("hottest_tower_digi_BptxMinus", "hottest_tower_digi_BptxMinus", 500, -50, 2000)
        self.hist["hottest_tower_digi_em_BptxMinus"] =  ROOT.TH1D("hottest_tower_digi_em_BptxMinus", "hottest_tower_digi_em_BptxMinus", 500, -50, 2000)
        self.hist["hottest_tower_digi_had_BptxMinus"] =  ROOT.TH1D("hottest_tower_digi_had_BptxMinus", "hottest_tower_digi_had_BptxMinus", 500, -50, 2000)

        self.hist["hottest_tower_digi_NotBptxOR"] =  ROOT.TH1D("hottest_tower_digi_NotBptxOR", "hottest_tower_digi_NotBptxOR", 500, -50, 2000)
        self.hist["hottest_tower_digi_em_NotBptxOR"] =  ROOT.TH1D("hottest_tower_digi_em_NotBptxOR", "hottest_tower_digi_em_NotBptxOR", 500, -50, 2000)
        self.hist["hottest_tower_digi_had_NotBptxOR"] =  ROOT.TH1D("hottest_tower_digi_had_NotBptxOR", "hottest_tower_digi_had_NotBptxOR", 500, -50, 2000)

        self.hist["castor_trace"] =  ROOT.TProfile("castor_trace", "castor_trace", 4000, 0, 4000)
        self.hist["castor_trace_n"] =  ROOT.TH1D("castor_trace_n", "castor_trace_n", 4000, 0, 4000)
        self.hist["castor_trace_high"] =  ROOT.TProfile("castor_trace_high", "castor_trace_high", 4000, 0, 4000)

        self.minL1 = 0 # includes L1_MinimumBiasHF1_AND
        self.maxL1 = 510 # includes CASTOR bits
        nL1 = self.maxL1-self.minL1
        
        self.hist["castor_bits"] =  ROOT.TH1D("castor_bits", "castor_bits", nL1, self.minL1, self.maxL1)
        
        self.hist["castor_bits2D"] =  ROOT.TH2D("castor_bits2D", "castor_bits2D", 4000, 0, 4000, nL1, self.minL1, self.maxL1)

        self.hist["corr_L1Muon_beam1_502"] =  ROOT.TH1D("corr_L1Muon_beam1_502", "corr_L1Muon_beam1", 101, -50, 50)
        self.hist["corr_L1Muon_beam2_502"] =  ROOT.TH1D("corr_L1Muon_beam2_502", "corr_L1Muon_beam2", 101, -50, 50)
        self.hist["corr_L1Muon_collision_502"] =  ROOT.TH1D("corr_L1Muon_collision", "corr_L1Muon_collision", 101, -50, 50)

        self.hist["corr_L1Muon_beam1_503"] =  ROOT.TH1D("corr_L1Muon_beam1_503", "corr_L1Muon_beam1", 101, -50, 50)
        self.hist["corr_L1Muon_beam2_503"] =  ROOT.TH1D("corr_L1Muon_beam2_503", "corr_L1Muon_beam2", 101, -50, 50)
        self.hist["corr_L1Muon_collision_503"] =  ROOT.TH1D("corr_L1Muon_collision_503", "corr_L1Muon_collision", 101, -50, 50)
        
#        for isec in xrange(0,16):
#            henergy = 'MuonSignal_sec_{sec}'.format(sec=str(isec+1))
#            self.hist[henergy] = ROOT.TH1D(henergy, henergy, 200, -50, 6000)
#            
#            for imod in xrange(0,14):
#                hname1 = 'MuonSignal_sec_{sec}_mod_{mod}'.format(sec=str(isec+1), mod=str(imod+1))
#                hname2 = 'NoiseSignal_sec_{sec}_mod_{mod}'.format(sec=str(isec+1), mod=str(imod+1))
#                self.hist[hname1] = ROOT.TH1D(hname1, hname1, len(binsMuon)-1, array('d',binsMuon)) # muons
#                self.hist[hname2] = ROOT.TH1D(hname2, hname2, len(binsNoise)-1, array('d',binsNoise))   # noise


        # store all histograms
        for h in self.hist:
            if not "TTree" in self.hist[h].ClassName():
                self.hist[h].Sumw2()
            self.GetOutputList().Add(self.hist[h])




            
    def analyze(self):

        self.hist["EventCounter"].Fill("all", 1)

        #if (self.hist["EventCounter"].GetBinContent(1) % 100 != 0):
        #    return 0
        
        BX = self.fChain.bx
        LS = self.fChain.lumi
        #if (LS>170):
        #    return 0
        
        for iL1 in range(self.minL1, self.maxL1):
            if (iL1<self.fChain.trgl1L1GTAlgo.size() and self.fChain.trgl1L1GTAlgo[iL1]):
                self.hist["castor_bits"].Fill(iL1)
                self.hist["castor_bits2D"].Fill(BX, iL1)
                        
        # l1 bit correlations
        if self.fChain.trgl1L1GTAlgo[49]: # L1_CatorMuon
            for fill_bx in self.beam1BX:
                self.hist["corr_L1Muon_beam1_502"].Fill(BX - fill_bx - 1)
            for fill_bx in self.beam2BX:
                self.hist["corr_L1Muon_beam2_502"].Fill(BX - fill_bx - 1)
            for fill_bx in self.collBX:
                self.hist["corr_L1Muon_collision_502"].Fill(BX - fill_bx - 1)

        if self.fChain.trgl1L1GTAlgo[503]: # L1_CatorMuon
            for fill_bx in self.beam1BX:
                self.hist["corr_L1Muon_beam1_503"].Fill(BX - fill_bx - 1)
            for fill_bx in self.beam2BX:
                self.hist["corr_L1Muon_beam2_503"].Fill(BX - fill_bx - 1)
            for fill_bx in self.collBX:
                self.hist["corr_L1Muon_collision_503"].Fill(BX - fill_bx - 1)
                            
        if self.fChain.CastorRecHitEnergy.size() != 224:
            return 0

        self.hist["EventCounter"].Fill("Data Valid", 1)

        # read CASTOR RecHits
        energy_ch_max = 0
        energy_ch = [[0 for _ in xrange(14)] for _ in xrange(16)]
        for ich in range(self.fChain.CastorRecHitEnergy.size()):
            isec = ich//14
            imod = ich%14
            energy_ch[isec][imod] = self.fChain.CastorRecHitEnergy.at(ich)
            energy_ch_max = max(energy_ch_max, energy_ch[isec][imod])

        # read CASTOR digis TS4
        digi_ch = [[0 for _ in xrange(14)] for _ in xrange(16)]
        for ich in range(self.fChain.CastorDigisADC_TS4.size()):
            isec = ich//14
            imod = ich%14
            digi_ch[isec][imod] = self.fChain.CastorDigisADC_TS4.at(ich)
                
        # CASTOR data
        
        energy_tot = 0
        energy_secsum = [0.0] * 16
        energy_secsum_em = [0.0] * 16
        energy_secsum_had = [0.0] * 16
        energy_secsum_max = 0
        energy_secsum_max_em = 0
        energy_secsum_max_had = 0
        digi_secsum_max = 0
        digi_secsum_max_em = 0
        digi_secsum_max_had = 0
        for isec in xrange(16):
            digi_secsum = 0
            digi_secsum_em = 0
            digi_secsum_had = 0
            for imod in xrange(14):
                if [isec+1,imod+1] in self.BadChannels:
                    continue
                self.hist["castor_channel_2d"].Fill(imod+1, isec+1, energy_ch[isec][imod])
                # rechits
                energy_secsum[isec] += energy_ch[isec][imod]
                if (imod<2):
                    energy_secsum_em[isec] += energy_ch[isec][imod]
                else:
                    energy_secsum_had[isec] += energy_ch[isec][imod]
                # digis
                if (imod>=12):
                    continue
                digi = kLookUpTableADCtoCharge[ int(digi_ch[isec][imod]) ] * 2.6
                digi_secsum += digi
                if (imod<2):
                    digi_secsum_em += digi
                else:
                    digi_secsum_had += digi
            energy_secsum_max = max(energy_secsum_max, energy_secsum[isec])
            energy_secsum_max_em = max(energy_secsum_max_em, energy_secsum_em[isec])
            energy_secsum_max_had = max(energy_secsum_max_had, energy_secsum_had[isec])

            digi_secsum_max = max(digi_secsum_max, digi_secsum)
            digi_secsum_max_em = max(digi_secsum_max_em, digi_secsum_em)
            digi_secsum_max_had = max(digi_secsum_max_had, digi_secsum_had)
            
            self.hist["castor_tower"].Fill(energy_secsum[isec]) 
            energy_tot += energy_secsum[isec]
            
        self.hist["castor_total"].Fill(energy_tot)
        self.hist["castor_trace"].Fill(BX, energy_secsum_max)
        self.hist["castor_trace_n"].Fill(BX, 1)
        if (energy_secsum_max>3) :
            self.hist["castor_trace_high"].Fill(BX, energy_secsum_max)

        # check if ZeroBias:
        if (self.fChain.trgl1L1GTAlgo[100]):

            self.hist["hottest_tower"].Fill(energy_secsum_max)
            self.hist["hottest_tower_em"].Fill(energy_secsum_max_em)
            self.hist["hottest_tower_had"].Fill(energy_secsum_max_had)
            
            if (self.fChain.trgl1L1GTAlgo[494]):
                self.hist["hottest_tower_494"].Fill(energy_secsum_max)

            if (self.fChain.trgl1L1GTAlgo[505]):
                self.hist["hottest_tower_em_505"].Fill(energy_secsum_max_em)
                self.hist["hottest_tower_had_505"].Fill(energy_secsum_max_had)

        # check if L1_UnpairedBunchBptxPlus
        if (self.fChain.trgl1L1GTAlgo[112]): 

            self.hist["hottest_tower_BptxPlus"].Fill(energy_secsum_max)
            self.hist["hottest_tower_em_BptxPlus"].Fill(energy_secsum_max_em)
            self.hist["hottest_tower_had_BptxPlus"].Fill(energy_secsum_max_had)

            self.hist["hottest_tower_digi_BptxPlus"].Fill(digi_secsum_max)
            self.hist["hottest_tower_digi_em_BptxPlus"].Fill(digi_secsum_max_em)
            self.hist["hottest_tower_digi_had_BptxPlus"].Fill(digi_secsum_max_had)

        # check if L1_UnpairedBunchBptxMinus
        if (self.fChain.trgl1L1GTAlgo[113]): 

            self.hist["hottest_tower_BptxMinus"].Fill(energy_secsum_max)
            self.hist["hottest_tower_em_BptxMinus"].Fill(energy_secsum_max_em)
            self.hist["hottest_tower_had_BptxMinus"].Fill(energy_secsum_max_had)

            self.hist["hottest_tower_digi_BptxMinus"].Fill(digi_secsum_max)
            self.hist["hottest_tower_digi_em_BptxMinus"].Fill(digi_secsum_max_em)
            self.hist["hottest_tower_digi_had_BptxMinus"].Fill(digi_secsum_max_had)

        # check if L1_NotBptxOR
        if (self.fChain.trgl1L1GTAlgo[103]): 

            # check also that we are in empty region of BX scheme
            # fill 7450, run 326822
            if ((BX>20 and BX<50) or
                (BX>585 and BX<600) or
                (BX>1665 and BX<1680) or
                (BX>2880 and BX<2900)):

                self.hist["hottest_tower_NotBptxOR"].Fill(energy_secsum_max)
                self.hist["hottest_tower_em_NotBptxOR"].Fill(energy_secsum_max_em)
                self.hist["hottest_tower_had_NotBptxOR"].Fill(energy_secsum_max_had)

                self.hist["hottest_tower_digi_NotBptxOR"].Fill(digi_secsum_max)
                self.hist["hottest_tower_digi_em_NotBptxOR"].Fill(digi_secsum_max_em)
                self.hist["hottest_tower_digi_had_NotBptxOR"].Fill(digi_secsum_max_had)
                
        return 1
    

    
    
    
    def finalize(self):

        print "Finalize:"

        
        
    def finalizeWhenMerged(self):
        print "finalizeWhenMerged"

        olist = self.GetOutputList()
        histos = {}
        for o in olist:
            if not "TH1" in o.ClassName():
                if not "TH2" in o.ClassName():
                    if not "TProfile" in o.ClassName():
                        continue
            histos[o.GetName()] = o
        
        




##################################################################################
##################################################################################
##################################################################################
##################################################################################

if __name__ == "__main__":

    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)

    if (len(sys.argv) < 2 or len(sys.argv) > 3):
        print "Please specify exaclty one CFF sample to run over"
        print "use printTree.py to see list of available samples"
        print "add \"force\" to force run even if no improvement is expected"
        sys.exit(1)
            
    sampleList = []
    sampleList.append(sys.argv[1])

    if (len(sampleList)!=1):
        print "You must specify exactly one CFF sample to run over"
        print "Use printTree.py to see available samples"
        sys.exit(1)


    # opening filling scheme data
    beam1BX=[]
    beam2BX=[]
    collBX=[]
    with open("LHC_fillingscheme_fill7444.txt") as filling:
        print ("READING LHC BUNCH FILLING SCHEME FILL=" + filling.name)
        lines=filling.readlines()
        filling.close()
        beamNo=0
        for line in lines:
            if "#" in line or "RFbucket" in line:
                continue
            if "BEAM" in line:
                beamNo = int(line.split(' ')[1])
                print ("read beam " + str(beamNo))
                continue
            cols = line.split(',')
            if (len(cols)!=12):
                continue
            bx = int(line.split(',')[1])
            ip5 = int(line.split(',')[4])
            if beamNo == 1:
                beam1BX.append(bx)
            elif beamNo == 2:
                beam2BX.append(bx)
            else:
                print str(beamNo)
                print line
                print ("ERROR")
                sys.exit(1)
            if ip5==1:
                collBX.append(bx)
                
    filling.close()
    #print ("beam1" + str(beam1BX))
    #print ("beam2" + str(beam1BX))
    #print ("beam-coll" + str(collBX))
        
    outfolder = './'
    outFileName = "CastorPlotsOutput_" + sampleList[0] + ".root"
    slaveParams = {"theSample": sampleList[0],
                   "BadChannels": BadChannels,
                   "beam1BX": beam1BX,
                   "beam2BX": beam2BX,
                   "collBX" : collBX}
    
    CastorPlots.runAll(treeName="CFFTree", 
                       slaveParameters = slaveParams,
                       sampleList = sampleList, 
                       maxNevents = -1, #100000000,
#                       maxNevents = 100000,
                       nWorkers = 12,
                       outFile = outFileName)
    
    print ("Output file name: " + outFileName )


    
