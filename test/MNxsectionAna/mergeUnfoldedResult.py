#!/usr/bin/env python

import ROOT
ROOT.gROOT.SetBatch(True)

from HistosHelper import getHistos

def main():
    herwigIn="~/tmp/mnxsHistos_unfolded_herwigOnData.root"
    pythiaIn="~/tmp/mnxsHistos_unfolded_pythiaOnData.root"
    histos = {}
    histos["herwig"]=getHistos(herwigIn)
    histos["pythia"]=getHistos(pythiaIn)
    print histos["herwig"]["_jet15"].keys()
    # TODO: test that dirs have the same contents






if __name__ == "__main__":
    main()

