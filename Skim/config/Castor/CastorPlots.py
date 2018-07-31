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


class CastorPlots(CommonFSQFramework.Core.ExampleProofReader.ExampleProofReader):
    def init( self, maxEvents = None):

        self.maxEvents = maxEvents
                
        self.hist = {}
        self.hist["EventCounter"] = ROOT.TH1D("EventCounter","EventCounter",10,0,20)
        
        # the castor data
        self.hist["castor_channel_2d"] =  ROOT.TH2D("castor_channel_2d", "castor_channel_2d", 14, 0.5, 14.5, 16, 0.5, 16.5)
        self.hist["castor_tower"] =  ROOT.TH1D("castor_tower", "castor_tower", 300, -10, 20)
        self.hist["castor_total"] =  ROOT.TH1D("castor_total", "castor_total", 300, -10, 20)

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

        if self.fChain.CastorRecHitEnergy.size() != 224:
            return 0

        self.hist["EventCounter"].Fill("Data Valid",1)

        # read CASTOR RecHits
        energy_ch = [[0 for _ in xrange(14)] for _ in xrange(16)]
        for ich in range(self.fChain.CastorRecHitEnergy.size()):
            isec = ich//14
            imod = ich%14
            energy_ch[isec][imod] = self.fChain.CastorRecHitEnergy.at(ich)
            

        # CASTOR data
                    
        energy_tot = 0
        energy_secsum = [0.0] * 16
        for isec in xrange(16):
            for imod in xrange(14):
#                if [isec+1,imod+1] in self.bad_ch:
#                    continue
                energy_secsum[isec] += energy_ch[isec][imod]                

                self.hist["castor_channel_2d"].Fill(imod+1, isec+1, energy_ch[isec][imod])
                                
            self.hist["castor_tower"].Fill(energy_secsum[isec]) 
            energy_tot += energy_secsum[isec]
            
        self.hist["castor_total"].Fill(energy_tot)
                               
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
                    if not "TProfile2D" in o.ClassName():
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
        
    outfolder = './'
    outFileName = "CastorPlotsOutput_" + sampleList[0] + ".root"
    slaveParams = {"theSample": sampleList[0]}
    
    CastorPlots.runAll(treeName="CFFTree", 
                       slaveParameters = slaveParams,
                       sampleList = sampleList, 
                       maxNevents = -1, #100000000,
#                       maxNevents = 100000,
                       nWorkers = 12,
                       outFile = outFileName)
    
    print ("Output file name: " + outFileName )


    
