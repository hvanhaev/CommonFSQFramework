#! /usr/bin/env python

import os
import ROOT
ROOT.gROOT.SetBatch(True)

import MNTriggerStudies.MNTriggerAna.Style

outDir = "~/tmp/balanceHLT_TodoXXX_recoAVGYYY/"
infile = "treeDiJetBalance.root"


def fit(todo, recoAVG, PUweight, cutBase):

    for t in todo:
        fitResultsDir = outDir.replace("XXX",str(t)).replace("YYY", str(recoAVG))
        command  = "./balanceFitAndPlot.py"
        command += " -i " + infile
        command += " -e 3 " 
        command += " -a "  + str(recoAVG)
        command += " -o " + fitResultsDir
        command += " -w " + PUweight
        if t > 0:
            command += " -c '" + cutBase.replace("XXX", str(t)) + "'"
        #command += " -c '" + cutBase + "'"
        os.system(command)



def plot(todo, ptAveReco, plotName, plotType):
    knownTypes = ["balance", "eff"]
    if plotType not in knownTypes:
        raise Exception("Plot type "+plotType+" not known")


    histoMap = {}
    for t in todo:
        fitResultsDir = outDir.replace("XXX",str(t)).replace("YYY", str(ptAveReco))
        histoFile = fitResultsDir+"/balanceHistos.root"
        rootfile = ROOT.TFile(histoFile, "read")
        lst = rootfile.GetListOfKeys()
        cnt = 0
        for l in lst:
            name = l.GetName()
            if "MC_" not in name:
                continue
            dir = l.ReadObj()
            if plotType == "balance":
                histo = dir.Get("balance_central_jet15").Clone()
            elif plotType == "eff":
                histo = dir.Get("num_balance_central_jet15").Clone()
            histo.SetDirectory(0)
            cnt += 1

        if cnt != 1:
            print "Wrong histogram cnt -", t, cnt
            continue
        histoMap[t]=histo

    if len(histoMap) == 0:
        print "No histograms found ?!?!?"
        sys.exit()

    #print histoMap
    canvas = ROOT.TCanvas()

    if plotType == "balance":
        hFrame = canvas.DrawFrame(2.8, -0.3, 5.2, 0.1)
        hFrame.GetYaxis().SetTitle("balance")
    elif plotType == "eff":
        hFrame = canvas.DrawFrame(2.8, 0, 5.2, 1.05)
        hFrame.GetYaxis().SetTitle("efficiency")

    hFrame.GetXaxis().SetTitle("#eta_{probe}")

    markerCnt = 20

    xS = 0.35
    xS = -0.15
    yS = -0.5
    leg = ROOT.TLegend(0.4+xS, 0.7+yS, 0.6+xS, 0.9+yS)
    leg.SetFillColor(0)

    #colorBase = ROOT.EColor.kRed
    colorBase = ROOT.EColor.kOrange
    colors = [ x for x in xrange(colorBase, colorBase+10) ]

    #print colorBase
    #sys.exit()
    #leg.SetHeader("p_{T}^{ave min HLT}:")
    #leg.SetHeader("Min L1SingleJet p_{T}:")
    leg.SetHeader("Threshold:")
    leg.AddEntry(0, "", "")
    cnt = 0

    xshift = 0
    if plotType == "eff":
        if -1 not in histoMap:
            raise Exception("Cannot find denominator")
        denom = histoMap[-1]
        del histoMap[-1]

    for t in sorted(histoMap.keys()):
        if plotType == "eff":
            histoMap[t].Divide(denom)
        histoMap[t].SetMarkerStyle(markerCnt)
        markerCnt += 1
        for i in xrange(1, histoMap[t].GetNbinsX()+1):
            histoMap[t].SetBinError(i,0)

        axe = histoMap[t].GetXaxis()
        histoMap[t].GetXaxis().Set(axe.GetNbins(), axe.GetXmin()+xshift, axe.GetXmax()+xshift )
        xshift+=0.03
        histoMap[t].Draw("e1 p same")
        color = colors[cnt]
        cnt +=1
        histoMap[t].SetMarkerColor(color)
        histoMap[t].SetLineColor(color)
        leg.AddEntry(histoMap[t], str(t), "p")

    #leg.AddEntry(0, "", "")
    label = ROOT.TLatex(0.8,0.965,  "reco p_{T}^{ave}>"+str(ptAveReco))
    label.SetNDC()
    label.SetTextSize(0.025)
    label.Draw()
    leg.Draw("SAME")
    canvas.Print("~/tmp/"+plotType+"_"+plotName)
        



def main():
    MNTriggerStudies.MNTriggerAna.Style.setStyle()
    PUWeight = "weight"
    #PUWeight = "flat010toPU10"
    #PUWeight = "flat010toPU1"
    #PUWeight = "flat010toPU5"

    todo = {}

    #todo[30] = ([-1, 1, 20, 25, 30, 35], "hltPtAve  > XXX && hltPtCen > XXX/2 && hltPtFwd > XXX/2")
    #todo[40] = ([-1, 1, 30, 35, 40, 45], "hltPtAve  > XXX && hltPtCen > XXX/2 && hltPtFwd > XXX/2")
    baseHLT = "hltPtAve  > XXX && hltPtCen > XXX/2 && hltPtFwd > XXX/2"
    baseHLTWithMatch = "hltPtAve  > XXX  && hltL1MatchPtCen > XXX/2 && hltL1MatchPtFwd > XXX/2"

    baseL1 = "l1SingleJetCentral > XXX"
    l1CenFwd = "l1SingleJetCentral > XXX && l1SingleJetForward > XXX"
    l1Fwd = "l1SingleJetForward > XXX"


    '''  l1 jet scale:  12 16 20 24 28 32.0 36.0 40.0 44.0 48.0 52.0 56.0 60.0 64.0 68.0 72.0 76.0 80.0 84.0 88.0 92.0    '''
    #  L1_SingleJet52 30000
    #  L1_SingleJet68 5000
    #  L1_SingleJet92 700
    #  L1_SingleJet128 150
    #'''
    ###########################################################################
    #
    # Note: -1 value has a special meaning - no extra cut at all!
    #
    ###########################################################################

    todo["A_HLT_60_baseHLT"] = ([-1, 45, 50, 55, 60], baseHLT, 60)
    todo["A_HLT_60_baseHLTwithL1Matching"] = ([-1, 45, 50, 55, 60], baseHLT + " && "+ baseHLTWithMatch, 60)
    todo["A_HLT_60_baseHLTwithL1MatchingWithL1Seed"] = ([-1,  45, 50, 55, 60], baseHLT + " && "+ baseHLTWithMatch + "&&" + l1CenFwd.replace("XXX", "35") , 60)

    todo["A_HLT_80_baseHLT"] = ([-1, 45, 50, 55, 60], baseHLT, 60)
    todo["A_HLT_80_baseHLTwithL1Matching"] = ([-1, 45, 50, 55, 60], baseHLT + " && "+ baseHLTWithMatch, 60)
    todo["A_HLT_80_baseHLTwithL1MatchingWithL1Seed"] = ([-1,  45, 50, 55, 60], baseHLT + " && "+ baseHLTWithMatch + "&&" + l1CenFwd.replace("XXX", "35") , 60)



    #todo["A_HLT_80"] = ([-1, 1, 50, 55, 60, 70], baseHLT, 80)
    #todo["A_HLT_120"] = ([-1, 1, 80, 90, 100, 110], baseHLT, 120)
    #'''

    # single jet L1 seeds
    '''
    todo["A_L1SingleCurrentMenu_60"] = ([-1, 1, 51, 67], baseL1, 60)
    todo["A_L1SingleCurrentMenu_80"] = ([-1, 1, 51, 67], baseL1, 80)
    todo["A_L1SingleCurrentMenu_120"] = ([-1, 1, 51, 67, 91], baseL1, 120)
    # '''
    #todo["A_L1_doubleJSeed_50"] = ([-1, 1, 23, 27, 31], l1CenFwd, 50) #
    #todo["B_L1_doubleJSeed_50"] = ([-1, 1, 35, 39, 43], l1CenFwd, 50) # 

    #todo["A_L1_doubleJSeed_60"] = ([-1, 1, 35, 39, 43], l1CenFwd, 60) # 
    #todo["B_L1_doubleJSeed_60"] = ([-1, 1, 47, 51, 55], l1CenFwd, 60) # 


    #todo["A_total_60"] = ([-1, 1, 47, 51, 55], l1CenFwd.replace(XXX, "35") + " && ", 60)

    #    cutBase = "hltPtAve  > 30 && hltPtCen > 15 && hltPtFwd > 15"  
    for t in todo:
        label = t
        ptAvesHLT = todo[t][0]
        cutBase = todo[t][1]
        ptAveReco = todo[t][2]
        fit(ptAvesHLT, ptAveReco, PUWeight, cutBase)
        plotName = "ptThreshods_"+label+"_"+ PUWeight +".png"
        plot(ptAvesHLT, ptAveReco, plotName, "balance")
        plot(ptAvesHLT, ptAveReco, plotName, "eff")


if __name__ == "__main__":
    main()







    



