#! /usr/bin/env python

import os
import ROOT
ROOT.gROOT.SetBatch(True)


cutBase = " && hltPtAve  > XXX"
outDir = "~/tmp/balanceHLT_XXX/"

#infile = "treeDiJetBalance_15.root"
infile = "treeDiJetBalance.root"
#todo = [10, 20, 30,  40, 50]
#todo = [10,  20, 40]
todo = [40, 45, 50, 55]


def fit():
    for t in todo:
        fitResultsDir = outDir.replace("XXX",str(t))
        command  = "./balanceFitAndPlot.py"
        command += " -i " + infile
        command += " -o " + fitResultsDir
        command += " -c '" + cutBase.replace("XXX", str(t)) + "'"
        os.system(command)

        #plotCommand = "./drawBalance.py"
        #plotCommand += " -i "+fitResultsDir+"/balanceHistos.root" 
        #plotCommand += " -o "+fitResultsDir
        #os.system(plotCommand)


def plot():

    histoMap = {}

    #histMin, histMax = (0,0)
    for t in todo:
        fitResultsDir = outDir.replace("XXX",str(t))
        histoFile = fitResultsDir+"/balanceHistos.root"
        #print histoFile
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
    hFrame = canvas.DrawFrame(2.8, -0.15, 5.2, 0.05)
    hFrame.GetXaxis().SetTitle("#eta")
    hFrame.GetYaxis().SetTitle("balance")

    markerCnt = 20
    leg = ROOT.TLegend(0.6,0.6,1,1)
    leg.SetHeader("HLT ptAve:")
    for t in sorted(histoMap.keys()):
        histoMap[t].SetMarkerStyle(markerCnt)
        markerCnt += 1
        histoMap[t].Draw("e p same")
        leg.AddEntry(histoMap[t], str(t), "p")

    leg.Draw("SAME")
    canvas.Print("~/tmp/ttt.png")
        



def main():
    fit()
    plot()



if __name__ == "__main__":
    main()







    



