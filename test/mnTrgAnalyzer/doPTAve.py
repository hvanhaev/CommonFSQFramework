#! /usr/bin/env python

import os
import ROOT
ROOT.gROOT.SetBatch(True)

import MNTriggerStudies.MNTriggerAna.Style

cutBase = " && hltPtAve  > XXX"
outDir = "~/tmp/balanceHLT_XXX/"
infile = "treeDiJetBalance.root"


def fit(todo):
    for t in todo:
        fitResultsDir = outDir.replace("XXX",str(t))
        command  = "./balanceFitAndPlot.py"
        command += " -i " + infile
        command += " -o " + fitResultsDir
        command += " -c '" + cutBase.replace("XXX", str(t)) + "'"
        os.system(command)

def plot(todo, plotName):
    histoMap = {}
    for t in todo:
        fitResultsDir = outDir.replace("XXX",str(t))
        histoFile = fitResultsDir+"/balanceHistos.root"
        rootfile = ROOT.TFile(histoFile, "read")
        lst = rootfile.GetListOfKeys()
        cnt = 0
        for l in lst:
            name = l.GetName()
            if "MC_" not in name:
                continue
            dir = l.ReadObj()
            histo = dir.Get("balance_central_jet15").Clone()
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
    hFrame = canvas.DrawFrame(2.8, -0.3, 5.2, 0.1)
    hFrame.GetXaxis().SetTitle("#eta_{probe}")
    hFrame.GetYaxis().SetTitle("balance")

    markerCnt = 20

    leg = ROOT.TLegend(0.4, 0.7, 0.8, 0.9)
    leg.SetFillColor(0)

    #colorBase = ROOT.EColor.kRed
    colorBase = ROOT.EColor.kOrange
    colors = [colorBase+1, colorBase+2, colorBase+3,colorBase+4]

    #print colorBase
    #sys.exit()
    leg.SetHeader("HLT p_{T}^{ave}\n threshold:")
    cnt = 0
    for t in sorted(histoMap.keys()):
        histoMap[t].SetMarkerStyle(markerCnt)
        markerCnt += 1
        histoMap[t].Draw("e1 p same")
        color = colors[cnt]
        cnt +=1
        histoMap[t].SetMarkerColor(color)
        histoMap[t].SetLineColor(color)
        leg.AddEntry(histoMap[t], str(t), "p")

    leg.Draw("SAME")
    canvas.Print("~/tmp/"+plotName)
        



def main():
    MNTriggerStudies.MNTriggerAna.Style.setStyle()
    low = [10, 15, 20]
    high = [20, 25, 30]
    #fit(low+high)
    plot(low, "hltPtThreshods_low.png")
    plot(high, "hltPtThreshods_high.png")



if __name__ == "__main__":
    main()







    



