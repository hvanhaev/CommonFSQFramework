#!/usr/bin/env python

import ROOT
ROOT.gROOT.SetBatch(True)

from HistosHelper import getHistos

from MNTriggerStudies.MNTriggerAna.DrawPlots import DrawPlots

import  MNTriggerStudies.MNTriggerAna.Style

from mnDraw import DrawMNPlots 

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
    maxima = []
    maxima.append(uncResult["max"])
    maxima.append(unc.GetMaximum())
    maxima.append(central.GetMaximum())

    c = ROOT.TCanvas()
    c.SetTopMargin(0.1)
    c.SetRightMargin(0.07)
    central.SetMaximum(max(maxima)*1.05)
    unc.SetFillColor(17);
    central.Draw()
    central.GetXaxis().SetTitle("#Delta#eta")
    central.GetYaxis().SetTitle("#sigma [pb]")
    central.GetYaxis().SetTitleOffset(1.8)
    unc.Draw("2SAME")
    DrawMNPlots.banner()
    c.Print("~/tmp/mergedUnfolded.png")
    c.SetLogy()
    c.Print("~/tmp/mergedUnfolded_log.png")







    #central = filter(lambda  finalSet["merged"])

if __name__ == "__main__":
    main()

