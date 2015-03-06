#!/usr/bin/env python

import ROOT
ROOT.gROOT.SetBatch(True)
from ROOT import *

import os,re,sys,math

import MNTriggerStudies.MNTriggerAna.Util

from array import array
import resource
import time

import multiprocessing
from optparse import OptionParser

class FitThread(multiprocessing.Process):
    def __init__(self, inputMap):
        super(FitThread, self).__init__()
        self.inputMap = inputMap

    def run(self):
        inputMap = self.inputMap
        canvas = ROOT.TCanvas()
        #dsReduced = inputMap["dsReduced"]

        dsReduced =  inputMap["ds"].reduce(inputMap["cut"])
        myVar = inputMap["myVar"]

        #myVar = vars[t][vary("balance")]
        meanVal = dsReduced.mean(myVar)
        sigma   = dsReduced.sigma(myVar)

        print "XXXXX", meanVal, sigma

        #rangeLow = meanVal - sigma*0.75
        #rangeHigh = meanVal + sigma*0.75
        rangeLow = meanVal - sigma*1.5
        rangeHigh = meanVal + sigma*1.5
        #rangeLow = meanVal - sigma*1.5
        #rangeHigh = meanVal + sigma*1.5

        #rangeLow = -1.7
        #rangeHigh = 1.7

        mean2 = RooRealVar("mean","mean of gaussian", 1, 0, 2)
        sigma2 = RooRealVar("sigma","width of gaussian", .1, 0, 2)
        gauss2 = RooGaussian("gauss","gaussian PDF",myVar, mean2, sigma2)

        ''' RooFit info:      
            If you want the errors to reflect the information contained in the provided dataset, choose kTRUE.
            If you want the errors to reflect the precision you would be able to obtain with an unweighted dataset
               with 'sum-of-weights' events, choose kFALSE.'''
        gauss2.fitTo(dsReduced, ROOT.RooFit.Range(rangeLow, rangeHigh), \
                     #ROOT.RooFit.PrintLevel(-1), ROOT.RooFit.SumW2Error(False)) # this exludes -1 point ("no jet matched point")
                     ROOT.RooFit.PrintLevel(-1), ROOT.RooFit.SumW2Error(True)) # this exludes -1 point ("no jet matched point")

        #balanceVariable = "hlt/reco pt"
        balanceVariable = "hlt/gen pt"
        frame = myVar.frame(ROOT.RooFit.Range(-0.5,2))
        frame.GetXaxis().SetTitle(balanceVariable)
        #sampleList[s]["RooDS"].plotOn(frame)
        dsReduced.plotOn(frame)
        gauss2.plotOn(frame)

        gauss2.paramOn(frame, ROOT.RooFit.Layout(0.1, 0.3, 0.53)) # , RooFit.Label("Gauss Fit"))
        frame.getAttText().SetTextSize(0.02) 
        # myVar = treeReader.variables[balanceVariable]["RooVar"]
        ptProbeJetVar = inputMap["ptProbeJetVar"]
        meanPT = dsReduced.mean(ptProbeJetVar)
        sigmaPT = dsReduced.sigma(ptProbeJetVar)
        #meanPU = dsReduced.mean(inputMap["PU"])

        etaMin = inputMap["etaMin"]
        etaMax = inputMap["etaMax"]

        box = ROOT.TPaveText(0.1, 0.55, 0.30, 0.9, "BRNDC")
        box.SetFillColor(0)
        #box.AddText(tag)
        box.AddText("avg(p^{reco}_{T})=%10.2f" % meanPT)
        box.AddText("mean (fit variable) =%10.2f" % meanVal)
        box.AddText("\sigma (fit variable) =%10.2f" % sigma )
        box.AddText(str(etaMin) + " < |#eta_{reco}| < "+str(etaMax))
        #box.AddText("PU mean=%10.2f"% meanPU)

        frame.addObject(box)
        frame.Draw()
        odir = inputMap["odir"]
        preName = odir + myVar.GetName() + "_" + inputMap["name"]  \
        + "_etaMin_" + str(etaMin).replace(".", "_") \
        + "_etaMax_" + str(etaMax).replace(".", "_") 
        #+ "_" + tag
        fname = preName + "__2.png"
        canvas.Print(fname)
        #fname = preName + "__2.root"
        #canvas.Print(fname)

        fitResult = {}
        fitResult["iEta"] = inputMap["iEta"]
        fitResult["mean"]      = mean2.getVal()
        fitResult["meanErr"] = mean2.getError()
        fitResult["gaussWidth"] = sigma2.getVal()
        fitResult["gaussWidthErr"] = sigma2.getError()
        fitResult["sumEntries"] = dsReduced.sumEntries() # return sum of weights

        fitResult["meanFromDS"] = meanVal
        fitResult["stderrFromDS"] = sigma

        self.queue.put(fitResult)


def main():

    parser = OptionParser(usage="usage: %prog [options] filename",
                            version="%prog 1.0")

    parser.add_option("-i", "--infile", action="store", type="string",  dest="infile" )
    parser.add_option("-o", "--outdir", action="store", type="string",  dest="outdir" )
    parser.add_option("-c", "--cutExtra", action="store", type="string",  dest="cutExtra" )
    parser.add_option("-w", "--weight", action="store", type="string",  dest="weight" )
    (options, args) = parser.parse_args()

    #weight = "weightPU"
    weight = "weight"
    if options.weight:
        weight = options.weight


    if options.infile:
        infile = options.infile
    else:
        infile = "treeMCRes.root"


    if options.outdir:
        odir = options.outdir
    else:
        odir = "~/tmp/mcres/"

    os.system("mkdir -p "+odir)

    etaRanges = [x/10. for x in xrange(0,51,5) ]

    sampleList=MNTriggerStudies.MNTriggerAna.Util.getAnaDefinition("sam")

    f = ROOT.TFile(infile, "r")
    lst = f.GetListOfKeys()
    trees = {}
    trees["MC_jet15"] = []
    trees["data_jet15"] = []

    samplesData = ["Jet-Run2010B-Apr21ReReco-v1", "JetMETTau-Run2010A-Apr21ReReco-v1", "JetMET-Run2010A-Apr21ReReco-v1"]

    for l in lst:
        #print "Going through", l.GetName(), l.ClassName()
        currentDir = l.ReadObj()

        if not currentDir:
            print "Problem reading", l.GetName(), " - skipping"
            continue

        if type(currentDir) != ROOT.TDirectoryFile:
            print "Expected TDirectoryFile,", type(currentDir), "found"
            continue

        sampleName = l.GetName()
        if sampleName not in sampleList:
            raise Exception("Thats confusing...")
        tree = currentDir.Get("data")
        isData = sampleList[sampleName]["isData"]
        if isData:
            if sampleName in samplesData:
                #tree.SetDirectory(0)
                trees["data_jet15"].append(tree)
                
        else:
            #tree.SetDirectory(0)
            trees["MC_jet15"].append(tree)

        print sampleName, tree.GetEntries()

        #print d

    dummyFile = ROOT.TFile("/tmp/dummy.root", "recreate")
    if len(trees["data_jet15"]) == 0:
            print "Cleaning data (no sample found)"
            del trees["data_jet15"]

    for t in trees:
        tlist = ROOT.TList()
        if len(trees[t]) == 1 and False:
            trees[t] = trees[t][0]
        else:
            for tree in trees[t]:
                tlist.Add(tree)
            trees[t] =  ROOT.TTree.MergeTrees(tlist)
            print "data tree after merge: ", trees[t].GetEntries()


    vars = {} # note: we whave to save the variables outside the loop, otherwise they get
              #       garbage collected by python leading to a crash

    ds = {}

    variations = set()


    for t in trees:
        print "RooDataset:",t
        vars[t] = {}
        tree = trees[t]
        observables = ROOT.RooArgSet()
        print "  min/max"
        for b in tree.GetListOfBranches():
            name =  b.GetName()
            if name != "weight":
                spl = name.split("_")
                if len(spl) > 1:
                    variation = name.split("_")[-1]
                    variations.add(variation)
                else:
                    print "Not a variation, skip:", name

            rmin = tree.GetMinimum(name)
            rmax = tree.GetMaximum(name)
            rmin = rmin-abs(rmin/100.)
            rmax = rmax+abs(rmin/100.)
            #print name, rmin, rmax
            roovar = ROOT.RooRealVar( name, name, rmin, rmax, "")
            vars[t][name] = roovar
            print "Creating variable", name, type(roovar)
            sys.stdout.flush()
            observables.add(roovar)
        #importCMD = RooFit.Import(tree)
        #cutCMD = RooFit.Cut(preselectionString)
        print "  create dataset...", weight
        #ds[t] = ROOT.RooDataSet(t, t, tree, observables, "weight < 100", weight)
        ds[t] = ROOT.RooDataSet(t, t, tree, observables,  "", weight)
        print "        ...done"

        print "Dataset:", t, ds[t].numEntries()

    if "central" not in variations:
        raise Exception("Central value not found!")


    #etaRanges = []
    #etaRanges.extend([0.001, 0.201, 0.401, 0.601, 0.801, 1.001, 1.201])
    #etaRanges.extend([1.401, 1.701, 2.001, 2.322, 2.411, 2.601, 2.801, 3.001, 3.201, 3.501, 3.801, 4.101, 4.701])
    #etaRanges.extend([2.801, 3.001, 3.201, 3.501, 3.801, 4.101, 4.401, 4.701, 5.001])
    #etaRanges.extend([4.101, 4.701])
    #minPt = 60
    #maxPt = 70
    #maxPt = 100
    #minPt = 10
    #maxPt = 15
    #minPt = 20
    #maxPt = 25
    minPt = 30
    maxPt = 40
    #minPt = 30
    #maxPt = 40
    #minPt = 30
    #maxPt = 40

    curPath = ROOT.gDirectory.GetPath()
    of = ROOT.TFile(odir+"mcresHistos.root","RECREATE")
    outputHistos = {}
    outputHistos["data_jet15"] = of.mkdir("data_jet15")
    outputHistos["MC_jet15"] = of.mkdir("MC_jet15")
    ROOT.gDirectory.cd(curPath)
    
    for t in ds:
        for v in variations:
            def vary(x, v=v):
                return x + "_" + v

            queue = multiprocessing.Queue()
            if t=="data_jet15" and v != "central":
                continue


            myThreads = []
            results = []
            cutBase =  vary("ptRec") + " > " + str(minPt)
            cutBase =  vary("ptRec") + " < " + str(maxPt)
            #cutBase += " && " + vary("jetType") +  " < 4.5 "
            cutBase += " && " + vary("jetType") +  " < -3.5 "
            cutBase += " && " + vary("jetType") +  " > -4.5 "
            #cutBase += " && " + " PU < 10.5"
            #cutBase += " && " + " PU > 9.5"
            #cutBase += " && " + " PU < 0.5"
            #cut += " && " + vary("balance") + " > " + str(-1)
            #cut += " && " + vary("balance") + " < " + str(1)
            cutBase += "&&" + vary("hlt2recRatio") + " < 2."
            cutBase += "&&" + vary("hlt2recRatio") + " > 0.01"
            if options.cutExtra != None:
                cutBase += " && " +  options.cutExtra
            


            cutFor2d = cutBase + " && " + vary("hlt2recRatio") + " < 2."
            print "XXXA"
            hist2d = ds[t].createHistogram(  vars[t][vary("etaRec")],  vars[t][vary("hlt2recRatio")], 10, 50, cutFor2d)
            outputHistos[t].WriteTObject(hist2d, "rVsEta")

            for iEta in xrange(1, len(etaRanges)):
                etaMin = etaRanges[iEta-1]
                etaMax = etaRanges[iEta]
                print "Doing", t, v, etaMin, etaMax

                cut = cutBase
                cut += " && abs(" + vary("etaRec") + ") >  " + str(etaMin)
                cut += " && abs(" + vary("etaRec") + ") <  " + str(etaMax)
                print cut

                #print "Reduce"
                #dsReduced = ds[t].reduce(cut)
                #print "Reduce...done"
            

                inputMap = {}
                inputMap["name"] = t
                inputMap["odir"] = odir
                #inputMap["dsReduced"] = dsReduced
                #inputMap["ds"] =  ds[t].Clone()
                inputMap["ptProbeJetVar"] =  vars[t][vary("ptRec")] 
                inputMap["ds"] =  ds[t]
                inputMap["myVar"] = vars[t][vary("hlt2recRatio")]
                inputMap["etaMin"] = etaMin
                inputMap["etaMax"] = etaMax
                inputMap["iEta"] = iEta # xcheck only
                inputMap["cut"] = cut


                thr = FitThread(inputMap)
                thr.queue = queue
                thr.start()
                myThreads.append(thr)
                #ptProbeJetVar
                #fitResult = fit(inputMap)
                #results.append(fitResult)

                #t = threading.Thread(target=fit, args = (dsReduced, queue))
                #t.daemon = False
                #t.start()

            for thr in myThreads:
                print "Joining!"
                thr.join()
                ret = queue.get()
                print ret
                results.append(ret)
            #sys.exit()            


            # all etas done. Create summary (vs eta) histogram
            etaArray = array('d', etaRanges)
            #histName = "balance_"+v + "_jet15"
            print "Note: non standard name"
            histName = "avgHLT2GenVsEta;#eta;response"
        
            #print etaRanges
            #print etaArray
            hist = ROOT.TH1F(histName, histName, len(etaArray)-1, etaArray)
            hist.Sumw2()
            histEffName = "num_"+histName
            histEff = ROOT.TH1F(histEffName, histEffName, len(etaArray)-1, etaArray)
            for i in xrange(len(results)):
                res = results[i]
                iEta = res["iEta"]
                etaMin = etaRanges[iEta-1]
                etaMax = etaRanges[iEta]
                etaAvg = (etaMin+etaMax)/2.
                bin = hist.FindBin(etaAvg)
                if bin != iEta:
                    print bin, iEta, etaAvg
                    raise Exception("Problem with binning")

                #hist.SetBinContent(bin, res["meanFromDS"])
                #hist.SetBinError(bin, res["stderrFromDS"])
                #print "Note: fit values ommited. Avg from DS taken"
                hist.SetBinContent(bin, res["mean"])
                hist.SetBinError(bin, res["meanErr"])


                histEff.SetBinContent(bin, res["sumEntries"])
            outputHistos[t].WriteTObject(hist,histName)
            c1 = ROOT.TCanvas()
            hist.Draw()

            hist.SetMaximum(1.6)
            hist.SetMinimum(0.4)
            hist.SetStats(False)
            # Warning: Q&D definition!
            c1.Print(odir+"/asEtaF.png")
            outputHistos[t].WriteTObject(histEff, histEffName)


        # all variations done








    #print "Sleep"
    #time.sleep(60)
    #print "Meminfo:", resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    #todo = {}
    #todo["MC"] = 
    #                 branches =  current.GetListOfBranches()


                




if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    ROOT.gSystem.Load("libFWCoreFWLite.so")
    AutoLibraryLoader.enable()
    main()
    print "Note: events with generator weight > 100 are ommited"
    print "./drawBalance.py  -i ~/tmp/balance/balanceHistos.root"


