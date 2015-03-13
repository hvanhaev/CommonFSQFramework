#!/usr/bin/env python

import ROOT
ROOT.gROOT.SetBatch(True)

from HistosHelper import getHistos

def main():
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

    # add jet15 and dj15 histos
    # note: histo binning should be the same from beginning!
    finalSet["merged"] = {}
    for t in finalSet["_jet15"]:
        newName = t.replace("_jet15", "_jet15andDJ15FB")
        finalHisto = finalSet["_jet15"][t].Clone()
        finalHisto.Add(finalSet["_dj15fb"][t.replace("_jet15", "_dj15fb")].Clone())
        finalSet["merged"][t] = finalHisto

    # save all to file
    ofile = ROOT.TFile(ofileName, "RECREATE")
    for dirName in finalSet:
        odir = ofile.mkdir(dirName)
        for h in finalSet[dirName]:
            odir.WriteTObject(finalSet[dirName][h])

if __name__ == "__main__":
    main()

