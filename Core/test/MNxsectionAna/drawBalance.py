#!/usr/bin/env python

import ROOT
ROOT.gROOT.SetBatch(True)

import os,re,sys,math

import MNTriggerStudies.MNTriggerAna.Util
import MNTriggerStudies.MNTriggerAna.Style

from MNTriggerStudies.MNTriggerAna.DrawPlots import DrawPlots

from array import array


from optparse import OptionParser

class DrawBalancePlots(DrawPlots):
    def getLumi(self, target, samples): # override
        if "data_" not in target:
            raise Exception("getLumi called for "+ target )

        spl = target.split("_")
        if len(spl) < 1:
            raise Exception("Cannot extract trigger name from " + target)

        trg = spl[-1]
        triggersToSamples = {} # TODO make accessible from self
        triggersToSamples["jet15"] = ["Jet-Run2010B-Apr21ReReco-v1", "JetMETTau-Run2010A-Apr21ReReco-v1", "JetMET-Run2010A-Apr21ReReco-v1"]
        triggersToSamples["dj15fb"] = ["METFwd-Run2010B-Apr21ReReco-v1", "JetMETTau-Run2010A-Apr21ReReco-v1", "JetMET-Run2010A-Apr21ReReco-v1"]

        if trg not in triggersToSamples.keys():
            raise Exception("Dont know how to get lumi for "+ trg + ". Known triggers are " + " ".join(triggersToSamples.keys()))

        triggerToKey = {}
        triggerToKey["jet15"] = "lumiJet15"
        triggerToKey["dj15fb"] = "lumiDiJet15FB"

        sampleList=MNTriggerStudies.MNTriggerAna.Util.getAnaDefinition("sam")
        #print "-----"
        lumi = 0.
        for s in samples:
            #print s
            if s in triggersToSamples[trg]:
                lumiKeyName = triggerToKey[trg]
                lumi += sampleList[s][lumiKeyName]
                #print " lumi->",lumi

        return lumi

    def getTarget(self, histoName, sampleName): # override
        ''' target naming convention:
                - name should consist of two parts separated by underscore

                - part after underscore should contain your trigger label
                -- e.g. dj15fb (which for 2010 MN XS analysis coresponds to
                   HLT_DoubleJet15_ForwardBackward and HLT_DoubleJet15_ForwardBackward_v3)

                - part before underscore should start with string "data" or "MC"
                -- to distinguish different MC use descriptive names eg MCqcd or MCdymumu
        '''
        sampleList=MNTriggerStudies.MNTriggerAna.Util.getAnaDefinition("sam")

        trgSplt = histoName.split("_")
        if len(trgSplt) < 1:
            raise "Cannot extract trigger name from" , histoName
        triggerName =  trgSplt[-1]

        isData = sampleList[sampleName]["isData"]
        retName = None
        if not isData:
            retName = "MC_" + triggerName
        else:
            triggersToSamples = {} # TODO make accessible from self
            triggersToSamples["jet15"] = ["Jet-Run2010B-Apr21ReReco-v1", "JetMETTau-Run2010A-Apr21ReReco-v1", "JetMET-Run2010A-Apr21ReReco-v1"]
            triggersToSamples["dj15fb"] = ["METFwd-Run2010B-Apr21ReReco-v1", "JetMETTau-Run2010A-Apr21ReReco-v1", "JetMET-Run2010A-Apr21ReReco-v1"]
            if sampleName in triggersToSamples[triggerName]:
                retName = "data_" + triggerName

        return retName

    def applyScale(self, histoName, sampleName): # override
        if histoName.startswith("balance"): return False
        print "Fixme: scaling"
        return False
        #return True

    def setGlobalStyle(self):  # override
        MNTriggerStudies.MNTriggerAna.Style.setStyle()


    def decorate(self, canvas, dataHisto, MCStack, errBand): # override
        if dataHisto != None:
            name = dataHisto.GetName()
            if "balance" in name:
                dataHisto.GetXaxis().SetTitle("|#eta|")
                dataHisto.GetYaxis().SetTitle("avg balance")


            dataHisto.SetMinimum(-0.5)
            dataHisto.SetMaximum(0.2)
            dataHisto.SetMarkerSize(0.3)
            dataHisto.SetMarkerStyle(8)
        else:
            MCStack.SetMinimum(-0.5)
            MCStack.SetMaximum(0.2)

        #MChistos = MCStack.GetHists()
        legend = ROOT.TLegend(0.3,0.95,1,1)
        legend.SetFillColor(0)
        legend.SetNColumns(3)
        if dataHisto != None:
            legend.AddEntry(dataHisto, "data", "pel")

        MChistos = MCStack.GetStack()
        for h in MChistos:
            h.SetMarkerColor(4)
            h.SetMarkerSize(1)
            h.SetLineColor(4)
            h.SetMarkerStyle(22)
            h.Draw("SAME*P")
            legend.AddEntry(h, "MC", "pel")
            #print type(h.GetDrawOption())
            #h.SetOption("PE hist")
            #print h.GetDrawOption()
        
        legend.AddEntry(errBand, "MC unc", "f")


        canvas.SetTopMargin(0.1)
        canvas.SetRightMargin(0.07)

        legend.Draw("SAME")
        self.keep.append(legend)



if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    ROOT.gSystem.Load("libFWCoreFWLite.so")
    ROOT.AutoLibraryLoader.enable()


    parser = OptionParser(usage="usage: %prog [options] filename",
                            version="%prog 1.0")

    parser.add_option("-i", "--infile", action="store", type="string",  dest="infile" )
    parser.add_option("-o", "--outdir", action="store", type="string",  dest="outdir" )
    (options, args) = parser.parse_args()

    if options.outdir:
        os.system("mkdir -p " + options.outdir)
        d = DrawBalancePlots(options.infile, outdir = options.outdir, skipFinalMap = True)
    else:
        d = DrawBalancePlots(options.infile,skipFinalMap = True)
    d.draw()

