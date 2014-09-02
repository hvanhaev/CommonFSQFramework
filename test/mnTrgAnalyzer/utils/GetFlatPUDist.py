#! /usr/bin/env python

from ROOT import *
import ROOT
ROOT.gROOT.SetBatch(True)

import os,re,sys,math

numberOfTruePUPoints = 200
triesForSingleTruePUPoint = 100000
binLow = 0
binHigh = 80
nbins = int(binHigh-binLow)


#random=ROOT.gRandom
def getTruePU(puTrueLow, puTrueHigh):
    if puTrueHigh == None:
        return puTrueLow
    return  ROOT.gRandom.Uniform(puTrueLow, puTrueHigh)

def doPU(puTrueLow, puTrueHigh):
    outputHist = ROOT.TH1D("pileup","pileup", nbins, binLow, binHigh)
    outputHistTruePU = ROOT.TH1D("true","true", nbins*10, binLow, binHigh)
    outputHist.Sumw2()

    todo = numberOfTruePUPoints
    if puTrueHigh == None:
        todo = 1

    for _ in xrange(todo):
        truePU = getTruePU(puTrueLow, puTrueHigh)
        outputHistTruePU.Fill(truePU)
        
        for _ in xrange(triesForSingleTruePUPoint):
            outputHist.Fill(ROOT.gRandom.Poisson(truePU))

    return (outputHist, outputHistTruePU)


def doAndSave(rootfile, label, puTrueLow, puTrueHigh):
    #cwd = rootfile.GetDirectory()
    print "Doing", label, puTrueLow, puTrueHigh
    hists = doPU(puTrueLow, puTrueHigh)
    newdir = rootfile.mkdir(label)
    newdir.WriteTObject(hists[0])
    newdir.WriteTObject(hists[1])
    h = hists[0]
    del h
    h = hists[1]
    del h


if __name__ == "__main__":
    of = ROOT.TFile("PUhists.root", "RECREATE")
    doAndSave(of, "Flat0to10", 0, 11 ) # the actuall number in the high range is 1 greater then the expected one
    doAndSave(of, "Flat20to50", 20, 51 )
    doAndSave(of, "PU0p01", 0.01, None )
    doAndSave(of, "PU0p1", 0.1, None )
    doAndSave(of, "PU0p5", 0.5, None )
    for i in xrange(1,12):
        doAndSave(of, "PU"+str(i), i, None)
    for i in [20, 25, 30, 35, 40, 45, 50]:
        doAndSave(of, "PU"+str(i), i, None)
         
   

