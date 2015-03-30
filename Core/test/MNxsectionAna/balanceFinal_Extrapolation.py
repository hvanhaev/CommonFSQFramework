#! /usr/bin/env python
#  export PYTHONPATH=/usr/lib/x86_64-linux-gnu/root5.34 


# Before execute
#  ./drawBalance.py  -i ~/tmp/balance/balanceHistos.root
#
#  for alpha=0.3 and alpha=0.2 values
#
#  execute this script for extrapolated values
#
#  at the end
# ./drawBalance.py -i balanceExtraPolation.root
import ROOT
ROOT.gROOT.SetBatch(True)

def getHistos(filename, dirname):
    infile = ROOT.TFile(filename, "read")
    keys =     infile.Get(dirname).GetListOfKeys()
    ret = {}
    for k in keys:
        current = k.ReadObj()
        if not current.GetName().startswith("balance_"): continue
        ret[current.GetName()]=current.Clone()
        ret[current.GetName()].SetDirectory(0)

    return ret

def getExtrapolation(v02, v03, histDir):
    # balance_ptDown_jet15
    h02 = getHistos(v02, histDir)
    h03 = getHistos(v03, histDir)

    if set(h02.keys()) != set(h03.keys()):
        print "Different histos:"
        print h02.keys()
        print h03.keys()
        sys.exit()

    store = []
    for k in h02.keys():
        newHisto = h02[k].Clone("extrapolated"+k)
        newHisto.SetDirectory(0)
        newHisto.Reset()

        for iBin in xrange(1, h02[k].GetNbinsX()+1):
            y1 = h03[k].GetBinContent(iBin)
            y2 = h02[k].GetBinContent(iBin)
            yExtrapol = y1+3*(y2-y1)
            newHisto.SetBinContent(iBin, yExtrapol)
            newHisto.SetBinError(iBin, h02[k].GetBinError(iBin))
            #store[k].append( (h02[k].GetBinCenter(iBin), yExtrapol))

        store.append(newHisto)
    return store        

def main():
    #v02 = "~/tmp/balance_v02_pt30/balanceHistos.root"
    #v03 = "~/tmp/balance_v03_pt30/balanceHistos.root"
    v02 = "~/tmp/balance_pt15_ave30_v02/balanceHistos.root"
    v03 = "~/tmp/balance_pt15_ave30_v03/balanceHistos.root"

    dataExtr = getExtrapolation(v02,v03, "data_jet15")
    MCExtr = getExtrapolation(v02,v03, "MC_jet15")

    ofile = ROOT.TFile("balanceExtraPolation.root", "recreate")
    odata = ofile.mkdir("data_jet15")
    oMC = ofile.mkdir("MC_jet15")

    odata.cd()
    for h in dataExtr:
        h.Write()

    oMC.cd()
    for h in MCExtr:
        h.Write()

if __name__ == "__main__":
    main()

