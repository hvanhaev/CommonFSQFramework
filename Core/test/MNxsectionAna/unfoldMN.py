#!/usr/bin/env python

import ROOT
ROOT.gROOT.SetBatch(True)
from ROOT import *

import os,re,sys,math

import CommonFSQFramework.Core.Util
import CommonFSQFramework.Core.Style

from array import array

from optparse import OptionParser

ROOT.gSystem.Load("libRooUnfold.so")
from HistosHelper import getHistos


from mnDraw import DrawMNPlots 

optionsReg = {}


# note: this function should modify the histogram and return a pointer to it
# its user responsibility to clone histograms before the modifications
def vary1d(h):
    for ix in xrange(0, h.GetNbinsX()+2): # vary also over/under flow bins
            val = h.GetBinContent(ix)
            if val == 0: continue
            err = h.GetBinError(ix)
            if err == 0: 
                print "Warning: err=0 in {} bin {} with val={}".format(histo.GetName(), ix, val)
            mod = ROOT.gRandom.Gaus(0, err)
            newVal = val+mod
            newErr = err # should we scale here?
            if newVal <= 0: newVal, newErr = 0,0
            h.SetBinContent(ix, newVal)
            h.SetBinError(ix, newErr)
    return h

# TODO: what with over flows here?
# note: this function should modify the histogram and return a pointer to it
# its user responsibility to clone histograms before the modifications
def vary2d(h):
    for ix in xrange(0, h.GetNbinsX()+2): # vary also over/under flow bins
        for iy in xrange(0, h.GetNbinsY()+2): # vary also over/under flow bins
            val = h.GetBinContent(ix, iy)
            if val == 0: continue
            err = h.GetBinError(ix, iy)
            if err == 0: 
                print "Warning: err=0 in {} bin {},{} with val={}".format(histo.GetName(), ix, iy, val)
            mod = ROOT.gRandom.Gaus(0, err)
            #print mod
            newVal = val+mod
            newErr = err # should we scale here?
            if newVal <= 0: newVal, newErr = 0,0
            h.SetBinContent(ix, iy, newVal)
            h.SetBinError(ix, iy, newErr)

    return h

# note: this function should modify the histogram and return a pointer to it
# its user responsibility to clone histograms before the modifications
def vary(histo):
    #print "RAN", ROOT.gRandom.Gaus(0, 1)
    if "TH1" in histo.ClassName():
        return vary1d(histo)
    elif "TH2" in histo.ClassName():
        return vary2d(histo)
    else:
        raise Exception("vary: unsupported object {} {}".format(histo.ClassName(), histo.GetName()))


def doUnfold(measured, rooresponse, nIter = None):
    global optionsReg
    if nIter == None:
        nIter = optionsReg["unfNIter"]

    if optionsReg["alaGri"]:
        # histos[baseMC][r] - response object
        # histo - detector level distribution
        #   RooUnfoldResponse(const TH1* measured, const TH1* truth, const TH2* response
        for i in xrange(0, measured.GetNbinsX()+1):
            denom = rooresponse.Hmeasured().GetBinContent(i)
            if denom == 0: continue
            nom = rooresponse.Hfakes().GetBinContent(i)
            if nom > denom:
                print "Warning! More fakes than meas", nom, denom
            factor = 1.-nom/denom
            val = measured.GetBinContent(i)*factor
            err = measured.GetBinError(i)*factor
            measured.SetBinContent(i, val)
            measured.SetBinError(i, err)

        rooresponse.Hmeasured().Add(rooresponse.Hfakes(), -1)
        rooresponse.Hfakes().Add(rooresponse.Hfakes(), -1)

    unfold = ROOT.RooUnfoldBayes(rooresponse, measured, nIter)

    errorTreatment = 1 
    hReco= unfold.Hreco(errorTreatment)

    chi2 = unfold.Chi2(rooresponse.Htruth(),errorTreatment)
    sys.stdout.flush()

    if hReco.GetNbinsX() != measured.GetNbinsX():
        raise Exception("Different histogram sizes after unfolding")

    return (hReco, chi2)

def scale(h, s):
    #h.Scale(s)
    #return
    for i in xrange(0, h.GetNbinsX()+2):
        val = h.GetBinContent(i)*s
        err = h.GetBinError(i)*s
        h.SetBinContent(i, val)
        h.SetBinError(i, err)

def scale2d(h, s):
    for i in xrange(0, h.GetNbinsX()+2):
        for j in xrange(0, h.GetNbinsY()+2):
            val = h.GetBinContent(i,j)*s
            err = h.GetBinError(i, j)*s
            h.SetBinContent(i, j, val)
            h.SetBinError(i, j, err)



def getPossibleActions():
    return set(["pythiaOnData", "herwigOnData", "pythiaOnHerwig", "herwigOnPythia", "herwigOnHerwig", "pythiaOnPythia"])

def unfold(action, infileName):
    possibleActions = getPossibleActions()
    if action not in possibleActions:
        print "Action", action, "not known. Possible actions "+ " ".join(possibleActions)
        return

    categories = {}
    if action == "herwigOnData":
        baseMC = "QCD_Pt-15to1000_TuneEE3C_Flat_7TeV_herwigpp"
        categories["_jet15"] = ["Jet-Run2010B-Apr21ReReco-v1", "JetMETTau-Run2010A-Apr21ReReco-v1", "JetMET-Run2010A-Apr21ReReco-v1"]
        categories["_dj15fb"] = ["METFwd-Run2010B-Apr21ReReco-v1", "JetMETTau-Run2010A-Apr21ReReco-v1", "JetMET-Run2010A-Apr21ReReco-v1"]
    elif action == "pythiaOnData":
        baseMC = "QCD_Pt-15to3000_TuneZ2star_Flat_HFshowerLibrary_7TeV_pythia6"
        categories["_jet15"] = ["Jet-Run2010B-Apr21ReReco-v1", "JetMETTau-Run2010A-Apr21ReReco-v1", "JetMET-Run2010A-Apr21ReReco-v1"]
        categories["_dj15fb"] = ["METFwd-Run2010B-Apr21ReReco-v1", "JetMETTau-Run2010A-Apr21ReReco-v1", "JetMET-Run2010A-Apr21ReReco-v1"]
    elif action ==  "pythiaOnHerwig":
        baseMC = "QCD_Pt-15to3000_TuneZ2star_Flat_HFshowerLibrary_7TeV_pythia6"
        otherMC =  "QCD_Pt-15to1000_TuneEE3C_Flat_7TeV_herwigpp"
        categories["_jet15"] = ["QCD_Pt-15to1000_TuneEE3C_Flat_7TeV_herwigpp"]
        categories["_dj15fb"] = ["QCD_Pt-15to1000_TuneEE3C_Flat_7TeV_herwigpp"]
    elif action ==  "herwigOnPythia":
        baseMC = "QCD_Pt-15to1000_TuneEE3C_Flat_7TeV_herwigpp"
        otherMC = "QCD_Pt-15to3000_TuneZ2star_Flat_HFshowerLibrary_7TeV_pythia6"
        categories["_jet15"] = ["QCD_Pt-15to3000_TuneZ2star_Flat_HFshowerLibrary_7TeV_pythia6"]
        categories["_dj15fb"] = ["QCD_Pt-15to3000_TuneZ2star_Flat_HFshowerLibrary_7TeV_pythia6"]
    elif action ==  "herwigOnHerwig":
        baseMC = "QCD_Pt-15to1000_TuneEE3C_Flat_7TeV_herwigpp"
        otherMC =  "QCD_Pt-15to1000_TuneEE3C_Flat_7TeV_herwigpp"
        categories["_jet15"] = ["QCD_Pt-15to1000_TuneEE3C_Flat_7TeV_herwigpp"]
        categories["_dj15fb"] = ["QCD_Pt-15to1000_TuneEE3C_Flat_7TeV_herwigpp"]
    elif action ==  "pythiaOnPythia":
        baseMC = "QCD_Pt-15to3000_TuneZ2star_Flat_HFshowerLibrary_7TeV_pythia6"
        otherMC = "QCD_Pt-15to3000_TuneZ2star_Flat_HFshowerLibrary_7TeV_pythia6"
        categories["_jet15"] = ["QCD_Pt-15to3000_TuneZ2star_Flat_HFshowerLibrary_7TeV_pythia6"]
        categories["_dj15fb"] = ["QCD_Pt-15to3000_TuneZ2star_Flat_HFshowerLibrary_7TeV_pythia6"]

    


    histos = getHistos(infileName)
    #print histos.keys()
    #print histos["JetMET-Run2010A-Apr21ReReco-v1"].keys()

    knownResponses = set(filter(lambda x: x.startswith("response_"), histos[baseMC].keys()))
    #print histos[baseMC].keys()

    #responsesCentral = set(filter(lambda x: "_central_" in x, knownResponses))
    #responsesVariations = knownResponses-responsesCentral

    # _dj15fb', 
    #'response_jecDown_jet15

    of =  ROOT.TFile(optionsReg["odir"]+"/mnxsHistos_unfolded_"+action+".root","RECREATE")

    # Warning: duplicated code for lumi calculation! See mnDraw.py
    triggerToKey = {}
    triggerToKey["_jet15"] = "lumiJet15"
    triggerToKey["_dj15fb"] = "lumiDiJet15FB"

    for c in categories:
        odirROOTfile = of.mkdir(c)

        centralHistoName = "xs_central"+c # in fact we should not find any other histogram in data than "central"
        histo = None

        sampleList=CommonFSQFramework.Core.Util.getAnaDefinition("sam")
        lumi = 0.
        for ds in categories[c]:
            h = histos[ds][centralHistoName]
            if not histo:
                histo = h.Clone()
                histo.SetDirectory(0)
            else:
                histo.Add(h)

            if "Data" in action: # 
                lumiKeyName = triggerToKey[c]
                lumi += sampleList[ds][lumiKeyName]


        if "Data" in action:
            histo.Scale(1./lumi)

        print "Lumi", c, action, lumi
        rawName = "xs_central"+c

        odirROOTfile.WriteTObject(histo,rawName)
        for r in knownResponses:
            if c not in r: continue # do not apply dj15fb to jet15 and viceversa
            variation = r.split("_")[1]
            # Doing:  _dj15fb response_central_dj15fb central

            print "Doing: ", c, r, variation
            rawName = "xsunfolded_" + variation+ c
            sys.stdout.flush()

            hReco = doUnfold(histo.Clone(), histos[baseMC][r].Clone())[0] # chi2 is on second part of ntuple
            hReco.SetName(rawName)
            odirROOTfile.WriteTObject(hReco, rawName)

            if "central" in variation:
                scanName = "chi2scan_"+rawName
                hScan = ROOT.TH1F(scanName, scanName+";iterations;chi^{2}", 8, 0.5, 8.5)
                hScan.GetYaxis().SetTitleOffset(1.8)
                for i in xrange(1,9):
                    chi2 = doUnfold(histo.Clone(), histos[baseMC][r].Clone(), i)[1]
                    iBin = hScan.FindBin(i)
                    hScan.SetBinContent(iBin, chi2)
                canv = ROOT.TCanvas()
                canv.SetLeftMargin(0.2)
                hScan.Draw()
                canv.Print(optionsReg["odir"]+"/{}_{}.png".format(action,scanName))
                canv.Print(optionsReg["odir"]+"/{}_{}.pdf".format(action,scanName))

            # now - toyMC approac to limited MC statistics
            todo = ["response", "fakes", "truth"]
            #todo = ["truth"]
            if optionsReg["disableToys"]:
                todo = []
            if variation == "central":
                badToys = 0
                for t in todo:
                    #   TProfile(const char* name, const char* title, Int_t nbinsx, const Double_t* xbins, Option_t* option = "")
                    bins = hReco.GetXaxis().GetXbins()
                    profile =  TProfile("prof_{}_{}".format(rawName, t), "", bins.GetSize()-1, bins.GetArray())
                    for i in xrange(0, optionsReg["ntoys"]):
                        clonedResponse = histos[baseMC][r].Clone()
                        htruth = clonedResponse.Htruth()
                        hfakes = clonedResponse.Hfakes()
                        hresponse = clonedResponse.Hresponse()
                        hmeas = clonedResponse.Hmeasured()
                        if t == "truth":
                            vary(htruth)
                        elif t == "fakes":
                            fakesOrg = hfakes.Clone()
                            vary(hfakes)
                            fakesDiff = hfakes.Clone()
                            fakesDiff.Add(fakesOrg, -1)
                            hmeas.Add(fakesDiff)
                        elif t == "response":
                            vary(hresponse)
                        else:
                            raise Exception("dont know what to do")

                        newResponse = ROOT.RooUnfoldResponse(hmeas, htruth, hresponse, \
                                                             "resp_{}_{}_{}".format(rawName, t,i)) 
                        hRecoVaried = doUnfold(histo.Clone(), newResponse)[0]
                        #print "TTT", hReco.Integral(), hRecoVaried.Integral()
                        binv1 =  hRecoVaried.GetBinContent(1)
                        if math.isnan(binv1) or math.isinf(binv1): 
                            badToys += 1
                            continue

                        for ix in xrange(0, hRecoVaried.GetNbinsX()+2):
                            binCenter = hRecoVaried.GetBinCenter(ix)
                            val = hRecoVaried.GetBinContent(ix)
                            if math.isnan(val) or math.isinf(val): 
                                print "TOYmc Error: nan/inf value found"
                                continue
                            # what to do??
                            profile.Fill(binCenter, val)

                    #print "Var: ", variation
                    #rawName = "xsunfolded_" + variation+ c
                    rawNameUp = rawName.replace("central", "toyMC{}Up".format(t) )
                    rawNameDown = rawName.replace("central", "toyMC{}Down".format(t) )
                    hUp = hReco.Clone(rawNameUp)
                    hDown = hReco.Clone(rawNameDown)
                    for i in xrange(1, hReco.GetNbinsX()+1):
                        binc1 =  hReco.GetBinCenter(i)
                        binc2 =  profile.GetBinCenter(i)
                        val1 =  hReco.GetBinContent(i)
                        val2 =  profile.GetBinContent(i)
                        if val1 <= 0: continue
                        errProf =  profile.GetBinError(i)
                        print "binc: {} {}, vals ratio {}, error: {}".format(binc1, binc2, val1/val2, errProf/val1)
                        hUp.SetBinContent(i, val1+errProf)
                        hDown.SetBinContent(i, val1-errProf)
                    odirROOTfile.WriteTObject(hUp, rawNameUp)
                    odirROOTfile.WriteTObject(hDown, rawNameDown)
                    print "TOYmc done for", r, " bad toys:", badToys

                    #ccc = hReco.Clone()
                    #varied = vary(ccc)
                    #print "TEST: ", hReco.Integral(), varied.Integral()
                    #print "TEST: ", ccc.Integral(), varied.Integral()
                #sys.stdout.flush()




def compareMCGentoMCUnfolded(action, infileName):
    if action == "herwigOnPythia" or action == "pythiaOnPythia":
        unfoldingWasDoneOn = "QCD_Pt-15to3000_TuneZ2star_Flat_HFshowerLibrary_7TeV_pythia6"
    elif action == "pythiaOnHerwig" or action == "herwigOnHerwig":
        unfoldingWasDoneOn = "QCD_Pt-15to1000_TuneEE3C_Flat_7TeV_herwigpp"
    else:
        print "compareMCGentoMCUnfolded: wrong action", action, "skipping (usually you can ignore this message)"
        return

    # detaGen_central_jet15
    fileWithUnfoldedPlotsName = optionsReg["odir"]+"/mnxsHistos_unfolded_"+action +".root"
    fileWithUnfoldedPlots = ROOT.TFile(fileWithUnfoldedPlotsName)


    #mnxsHistos_unfolded_pythiaOnHerwig.root
    histos = getHistos(infileName)
    #print histos[unfoldingWasDoneOn].keys()
    todo = ["_jet15", "_dj15fb"]
    #todo = ["_jet15"]

    c = ROOT.TCanvas()
    for t in todo:
        genHisto = histos[unfoldingWasDoneOn]["detaGen_central"+t]
        unfoldedHistoName = t+"/xsunfolded_central"+t
        unfoldedHisto = fileWithUnfoldedPlots.Get(unfoldedHistoName)
        #print unfoldedHistoName, type(unfoldedHisto), unfoldedHisto.ClassName()
        #genHisto.Scale(0.5)
        genHisto.Draw()
        genHisto.GetXaxis().SetTitle(DrawMNPlots.xLabels()["xs"])
        genHisto.GetYaxis().SetTitleOffset(1.8)
        genHisto.GetYaxis().SetTitle(DrawMNPlots.yLabels()["xsAsPB"])

        genHisto.SetMarkerColor(2)
        genHisto.SetLineColor(2)
        unfoldedHisto.Draw("SAME")
        trueMax = max(genHisto.GetMaximum(), unfoldedHisto.GetMaximum())
        genHisto.SetMaximum(trueMax*1.07)

        c.Print(optionsReg["odir"]+"/MConMCunfoldingTest_"+action+t+".png")

def main():
    CommonFSQFramework.Core.Style.setTDRStyle()
    possibleActions = getPossibleActions()
    optionsReg["alaGri"] = True
    optionsReg["ntoys"]  = 1000
    optionsReg["unfNIter"]  = 3
    optionsReg["disableToys"]  = False
    
    parser = OptionParser(usage="usage: %prog [options] filename",
                            version="%prog 1.0")

    parser.add_option("-v", "--variant",   action="store", dest="variant", type="string", \
                                help="choose analysis variant")



    (options, args) = parser.parse_args()
    if not options.variant:
        print "Provide analysis variant"
        sys.exit()

    infileName = "plotsMNxs_{}.root".format(options.variant)
    odir = "~/tmp/unfolded_{}/".format(options.variant)
    os.system("mkdir -p "+odir)
    optionsReg["odir"] = odir

    #possibleActions = ["pythiaOnPythia",  "herwigOnPythia", "pythiaOnHerwig", "herwigOnHerwig"]
    for action in possibleActions:
        unfold(action, infileName)
        compareMCGentoMCUnfolded(action, infileName)

if __name__ == "__main__":
    main()

