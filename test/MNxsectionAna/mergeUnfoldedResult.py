#!/usr/bin/env python

import ROOT
ROOT.gROOT.SetBatch(True)

from HistosHelper import getHistos

from MNTriggerStudies.MNTriggerAna.DrawPlots import DrawPlots

import  MNTriggerStudies.MNTriggerAna.Style

from mnDraw import DrawMNPlots 
from array import array

def main():
    MNTriggerStudies.MNTriggerAna.Style.setTDRStyle()

    lumiUncertainty = 0.04
    herwigIn="~/tmp/mnxsHistos_unfolded_herwigOnData.root"
    pythiaIn="~/tmp/mnxsHistos_unfolded_pythiaOnData.root"
    ofileName = "~/tmp/mnxsHistos_unfolded_onData_merged.root"


    histos = {}
    histos["herwig"]=getHistos(herwigIn)
    histos["pythia"]=getHistos(pythiaIn)
    #print histos["herwig"]["_jet15"].keys()
    #sys.exit()
    # TODO: test that dirs have the same contents

    # ['xsunfolded_central_jet15', 'xsunfolded_jecDown_jet15', 'xs_central_jet15', 'xsunfolded_jerDown_jet15', 'xsunfolded_jecUp_jet15', 'xsunfolded_jerUp_jet15']
    finalSet = {}

    # TODO: lumi unc
    todo = ["_jet15", "_dj15fb"]
    for t in todo:
        finalSet[t] = {}
        for hName in histos["herwig"][t]:
            if hName.startswith("xs_"): continue # skip detector level histogram

            hAvg = histos["herwig"][t][hName].Clone()

            hAvg.Add(histos["pythia"][t][hName])
            hAvg.Scale(0.5)
            finalSet[t][hName]=hAvg

            # add herwig/pythia central histo as variations
            #  in case we would have more than two MC - for every MC
            #   add a central value as "up" variation, as a "down"
            #   variation use the averaged histogram
            #    this way we have consistent list of up/down variations,
            #    where the down variation doesnt enlarge uncertainty band
            if "_central_" in hName:
                newNameHerwig = hName.replace("_central_", "_modelUp_")
                newNamePythia = hName.replace("_central_", "_modelDown_")
                finalSet[t][newNameHerwig] = histos["herwig"][t][hName].Clone(newNameHerwig)
                finalSet[t][newNamePythia] = histos["pythia"][t][hName].Clone(newNamePythia)

                # at the same point - use the averaged histogram to add lumi uncertainy
                #  BTW: should we do it here??
                newNameAvgUp = hName.replace("_central_", "_lumiUp_")
                newNameAvgDown = hName.replace("_central_", "_lumiDown_")
                finalSet[t][newNameAvgUp] = hAvg.Clone(newNameAvgUp)
                finalSet[t][newNameAvgDown] = hAvg.Clone(newNameAvgDown)
                finalSet[t][newNameAvgUp].Scale(1.+lumiUncertainty)
                finalSet[t][newNameAvgDown].Scale(1.-lumiUncertainty)



    # add jet15 and dj15 histos
    # note: histo binning should be the same from beginning!
    finalSet["merged"] = {}
    for t in finalSet["_jet15"]:
        newName = t.replace("_jet15", "_jet15andDJ15FB")
        finalHisto = finalSet["_jet15"][t].Clone(newName)
        finalHisto.Add(finalSet["_dj15fb"][t.replace("_jet15", "_dj15fb")].Clone())
        finalSet["merged"][newName] = finalHisto

    # save all to file
    ofile = ROOT.TFile(ofileName, "RECREATE")
    for dirName in finalSet:
        odir = ofile.mkdir(dirName)
        for h in finalSet[dirName]:
            odir.WriteTObject(finalSet[dirName][h])


    # make final plot, including uncertainty band
    central = [ finalSet["merged"][hName] for hName in finalSet["merged"].keys() if "_central_" in hName ]
    if len(central) != 1:
        raise Exception("Error: more than one central histo found")
    central = central[0]

    uncert  = [finalSet["merged"][hName] for hName in finalSet["merged"].keys() if "_central_" not in hName ]

    uncResult= DrawPlots.getUncertaintyBand(uncert, central)
    unc = uncResult["band"]


    # get GEN level distributions
    histosFromPyAnalyzer = getHistos("plotsMNxs.root")
    herwigDir = "QCD_Pt-15to1000_TuneEE3C_Flat_7TeV_herwigpp"
    pythiaDir =  "QCD_Pt-15to3000_TuneZ2star_Flat_HFshowerLibrary_7TeV_pythia6"
    genHistoHerwig = histosFromPyAnalyzer[herwigDir]["detaGen_central_jet15"].Clone()
    genHistoHerwig.Add(histosFromPyAnalyzer[herwigDir]["detaGen_central_dj15fb"])
    genHistoPythia = histosFromPyAnalyzer[pythiaDir]["detaGen_central_jet15"].Clone()
    genHistoPythia.Add(histosFromPyAnalyzer[pythiaDir]["detaGen_central_dj15fb"])

    maxima = []
    maxima.append(uncResult["max"])
    for t in [unc, central, genHistoHerwig, genHistoPythia]:
        maxima.append(t.GetMaximum())

    c = ROOT.TCanvas()
    c.Divide(1,2)
    c.cd(1)
    split = 0.2
    margin = 0.005
    ROOT.gPad.SetPad(.005, split+margin, .995, .995)
    c.cd(2)
    ROOT.gPad.SetPad(.005, .005, .995, split)
    c.cd(1)

    ROOT.gPad.SetTopMargin(0.1)
    #c.SetRightMargin(0.07)
    central.SetMaximum(max(maxima)*1.05)
    unc.SetFillColor(17);
    central.Draw()
    central.GetXaxis().SetTitle("#Delta#eta")
    central.GetYaxis().SetTitle("#sigma [pb]")
    central.GetYaxis().SetTitleOffset(1.8)
    unc.Draw("2SAME")
    central.Draw("SAME")

    genHistoHerwig.Draw("SAME HIST")
    genHistoHerwig.SetLineColor(2)

    genHistoPythia.Draw("SAME HIST")
    genHistoPythia.SetLineColor(4)

    DrawMNPlots.banner()


    legend = ROOT.TLegend(0.6, 0.7, 0.9, 0.85)
    legend.SetFillColor(0)
    legend.AddEntry(central, "data", "pel")
    legend.AddEntry(unc, "syst. unc.", "f")
    legend.AddEntry(genHistoHerwig, "herwig", "l")
    legend.AddEntry(genHistoPythia, "pythia", "l")
    legend.Draw("SAME")    

    c.cd(2)
    ROOT.gPad.DrawFrame(central.GetXaxis().GetXmin(), 0, central.GetXaxis().GetXmax(), 3)

    yUp = array('d')
    yDown = array('d')
    x = array('d')
    y = array('d')
    xDown = array('d')
    xUp = array('d')
    for iBin in xrange(1, central.GetNbinsX()+1):
        val =  central.GetBinContent(iBin)
        if val != 0:
            valDown = unc.GetErrorYlow(iBin-1)/central.GetBinContent(iBin)
            valUp =   unc.GetErrorYhigh(iBin-1)/central.GetBinContent(iBin)
            yDown.append(valDown)
            yUp.append(valUp)
            print valDown, valUp
        else:
           yUp.append(0)
           yDown.append(0)
        #print 
        x.append(unc.GetX()[iBin-1])
        y.append(1)
        xDown.append(unc.GetErrorXlow(iBin-1))
        xUp.append(unc.GetErrorXhigh(iBin-1))

    #print type(x)
    uncRatio = ROOT.TGraphAsymmErrors(len(x), x, y, xDown, xUp, yDown, yUp)
    uncRatio.SetFillStyle(3001)
    uncRatio.SetFillColor(17)
    uncRatio.Draw("2SAME")


    centralRatio = central.Clone()
    centralRatio.Divide(central)
    centralRatio.Draw("SAME")

    herwigRatio = genHistoHerwig.Clone()
    herwigRatio.Divide(central)

    pythiaRatio = genHistoPythia.Clone()
    pythiaRatio.Divide(central)

    herwigRatio.Draw("SAME L")
    pythiaRatio.Draw("SAME L")


    c.Print("~/tmp/mergedUnfolded.png")
    c.cd(1)
    ROOT.gPad.SetLogy()
    c.Print("~/tmp/mergedUnfolded_log.png")







    #central = filter(lambda  finalSet["merged"])

if __name__ == "__main__":
    main()

