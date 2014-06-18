#! /usr/bin/env python

import os
import ROOT
ROOT.gROOT.SetBatch(True)


cutBase = " && hltPtAve  > XXX"
outDir = "~/tmp/balanceHLT_XXX/"

#infile = "treeDiJetBalance_15.root"
infile = "treeDiJetBalance.root"
#todo = [10, 15, 20, 25, 30, 35, 40]
todo = [10,  20, 40]


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
    hFrame = canvas.DrawFrame(2.8, -0.3, 5.2, 0.3)
    hFrame.GetXaxis().SetTitle("#eta")
    hFrame.GetYaxis().SetTitle("balance")

    #fHist = histoMap.itervalues().next()
    #fHist.Draw()
    #fHist.GetXaxis().SetLimits(2.8, 5.2)
    #fHist.GetYaxis().SetLimits(-0.3, 0.3)
    #canvas.Range(2.8, -0.3, 5.2, 0.3)
    for h in histoMap:
        histoMap[h].Draw("SAME")

    canvas.Print("~/tmp/ttt.png")
        






def main():
    #fit()
    plot()



if __name__ == "__main__":
    main()







    



