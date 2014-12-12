import pickle

import ROOT
ROOT.gROOT.SetBatch(True)
from ROOT import *
from ProductGetter import ProductGetter


from array import array 

class HLTMCWeighter:

    # https://wiki.physik.uzh.ch/lhcb/root:colorscheme    
    def set_palette(name="palette", ncontours=999):

        if name == "gray" or name == "grayscale":
            stops = [0.00, 0.34, 0.61, 0.84, 1.001]
            #stops = [0.00, 340, 611, 840, 1000]
            red   = [1.00, 0.84, 0.61, 0.34, 0.00]
            green = [1.00, 0.84, 0.61, 0.34, 0.00]
            blue  = [1.00, 0.84, 0.61, 0.34, 0.00]
        # elif name == "whatever":
            # (define more palettes)
        else:
            # default palette, looks cool
            stops = [0.00, 0.34, 0.61, 0.84, 1.00]
            red   = [0.00, 0.00, 0.87, 1.00, 0.51]
            green = [0.00, 0.81, 1.00, 0.20, 0.00]
            blue  = [0.51, 1.00, 0.12, 0.00, 0.00]

        s = array('d', stops)
        r = array('d', red)
        g = array('d', green)
        b = array('d', blue)

        npoints = len(s)
        TColor.CreateGradientColorTable(npoints, s, r, g, b, ncontours)
        gStyle.SetNumberContours(ncontours)


    def __init__(self, triggerName, period = None, weight = False):

        if period == None:
            runMin = 0
            runMax = 9999999
        elif period == "A":
            runMin = 0
            runMax = 146219
        elif period == "B":
            runMin = 146240
            runMax = 9999999
        elif isinstance( period, ( int, long ) ):
            runMin = period
            runMax = period
        else:
            print "HLTMCWeighter: Period not known:", period
            sys.exit()

        self.label = triggerName

        shortName = triggerName.replace("HLT_","")
        self.useRawPt = False
        shortName1 = shortName
        shortName2 = shortName
        if "_raw" in shortName:
            self.useRawPt = True
            shortName2 = shortName2.replace("_raw","")

        self.l1seeding = False
        if "_L1Seeding" in shortName:
            self.l1seeding = True
            shortName2 = shortName2.replace("_L1Seeding","")
            

        self.getter = ProductGetter()

        self.etaRangeLowForMax = 3.0 # dj fb
        self.etaRangeHighForMax = 5.1
        self.fb = True

        if shortName2 == "Jet15U":
            self.fb = False
            self.etaRangeLowForMax = -1.0
            self.etaRangeHighForMax = 5.1

        # hltEffHistos.root  prescales_Jet15U.p  
        # MNTriggerStudies/MNTriggerAna/test/MNxsectionAna/trgEfficiency
        fPrescales = edm.FileInPath( "MNTriggerStudies/MNTriggerAna/test/MNxsectionAna/trgEfficiency/prescales_" + shortName2+".p").fullPath()
        prescales = pickle.load( open( fPrescales, "rb" ) )

        fLumi      = edm.FileInPath( "MNTriggerStudies/MNTriggerAna/test/MNxsectionAna/trgEfficiency/runLumi_" + shortName2+".p").fullPath()
        runLumi = pickle.load( open( fLumi, "rb" ) )

        # hltEffHistos_DoubleJet15U_ForwardBackward.root  hltEffHistos_Jet15U.root

        fName =  "MNTriggerStudies/MNTriggerAna/test/MNxsectionAna/trgEfficiency/hltEffHistos_"+ shortName1 + ".root"
        print self.label, "- using", fName
        filePath = edm.FileInPath( fName ).fullPath()
        curPath = ROOT.gDirectory.GetPath()
        rootFileTF = ROOT.TFile(filePath, "READ")
        lst = rootFileTF.GetListOfKeys()
        # nom_142304
        h = {}
        h["nom"] = None
        h["denom"] = None
        denom = None
        self.runs = set()
        binx = 38
        biny =4
        sumNom = 0
        

        for l in lst:
            current = l.ReadObj()
            name = current.GetName()
            if not "nom_" in name: continue
            spl = name.split("_")
            hType = spl[0]
            run = int(spl[1])
            if run < runMin or run > runMax: continue
            self.runs.add(run)

            if weight:
                if run not in prescales:
                    print "HLTMCWeighter: run not found", run
                    continue
                if len(prescales[run])==0:
                    print "HLTMCWeighter: run found but empty", run
                    continue
                prescale = iter(prescales[run]).next()
                if run not in runLumi:
                    print "Lumi missing:", run
                    lumi = 0 
                else:
                    lumi = runLumi[run][0]

                factor = lumi/prescale
            else:
                factor = 1
            if hType == "nom":
                a = 1
                sumNom += current.GetBinContent(binx,biny)
                

            if h[hType] == None:
                #print "Clone"
                h[hType] = current.Clone( "clone_"+str(hType)+ str(run) )
                h[hType].Scale(factor)
            else:
                h[hType].Add(current, factor)

            #print "TTT", hType, h[hType].GetName(), h[hType].Integral()


        binx = h["nom"].GetXaxis().FindBin(50)
        biny = h["nom"].GetYaxis().FindBin(1)
        #print binx, biny
        nnom = h["nom"].GetBinContent(binx,biny)
        ndenom = h["denom"].GetBinContent(binx,biny)
        r = -1
        if ndenom != 0:
            r= float(nnom)/ndenom
        if ndenom < nnom: print "asdfa", period
        #print r, period,"|", nnom, ndenom

        #print sumNom
        
        nom = h["nom"].Clone()
        #nom.Scale(1000)
        denom = h["denom"].Clone()
        

        h["nom"].Divide(h["denom"]) 

        
        #  the histogram is associated with a currently open rootfile (which soon will be closed). A clone is needed in root main dir
        ROOT.gDirectory.cd(curPath)
        self.efficiencyHisto = h["nom"].Clone() 
        self.nom = nom.Clone("nomAA")
        self.denom = denom.Clone("denomAA")

    # TODO: check limits
    def getEfficiency(self,eta,pt):
        #if self.fb: # temporary, till workaround for HLT_FB logic is implemented
        #    eta = abs(eta)

        binx = self.efficiencyHisto.GetXaxis().FindBin(pt)
        biny = self.efficiencyHisto.GetYaxis().FindBin(eta)
        return self.efficiencyHisto.GetBinContent(binx,biny)

    # etaHalf = 0 - both
    # etaHalf = + - positive
    # etaHalf = - - negative
    def getWeight(self, ev, etaHalf=0):
        jetColType = "vector<pat::Jet>"
        jetColTag  = ("selectedPatJetsAK5Calo",)
        jets = self.getter.get(ev, jetColType, jetColTag)
        plus = 0
        minus = 0
        '''
        for j in jets:
            if j.pt() < 35: continue
            if abs(j.eta()) < 3.: continue
            if j.eta() < 0.: minus += 1
            else: plus += 1

        if plus > 0 and minus > 0:
            printD = True
        else:
            printD = False
        '''
        printD = False
        #printD = True


        if printD: print "################################", ev.eventAuxiliary().event()
        if etaHalf==0 and self.fb:
            w = self.getWeight(ev, -1)*self.getWeight(ev, 1)
            if printD: print "FB weight", w
            return w

        jetColType = "vector<pat::Jet>"
        jetColTag  = ("selectedPatJetsAK5Calo",)
        jets = self.getter.get(ev, jetColType, jetColTag)
        trgFactor = 1.
        #print "#"*10
        for j in jets:
            #eta = abs(j[0].eta())
            eta = j.eta()
            if printD: print j.eta(), j.pt(), j.correctedJet("Uncorrected").pt(),  j.isCaloJet(), etaHalf
            if etaHalf!=0 and self.fb:
                if eta*etaHalf < 0: 
                    if printD: print " ---> etaHalf skip"
                    continue

            if abs(eta) > 5.1: continue
            aeta = abs(eta)
            if aeta < self.etaRangeLowForMax or aeta > self.etaRangeHighForMax: 
                if printD: print "  ---> print etaRange skip" 
                continue
            pt = j.pt()
            if self.useRawPt:
                pt = j.correctedJet("Uncorrected").pt()

            w1 = self.getEfficiency(eta,pt)
            if printD: print " --->",w1
            if w1 < 0.01 and pt > 50 and aeta > self.etaRangeLowForMax and aeta < self.etaRangeHighForMax:
                w1 = 1
                if printD: print " Changing w to 1"

            trgFactor *= 1-w1
            if printD: print " --> factor:", trgFactor

        #print 1.- trgFactor
        return 1. - trgFactor


    def dumpEfficiencyHisto(self, name=""):
        '''
        binx = self.efficiencyHisto.GetXaxis().FindBin(55)
        for i in xrange(15):
            eta = 4.5 + float(i)/10.
            biny = self.efficiencyHisto.GetYaxis().FindBin(eta)
            w = self.efficiencyHisto.GetBinContent(binx,biny)
            print "a", eta, binx, biny, w
        '''

        #ROOT.gStyle.SetPadTopMargin(0.05)
        ROOT.gStyle.SetPadBottomMargin(0.10)
        ROOT.gStyle.SetPadLeftMargin(0.10)
        ROOT.gStyle.SetPadRightMargin(0.125)

        #ROOT.gStyle.SetPalette(1)
        self.set_palette()
        ROOT.gStyle.SetOptStat(0)
        c = ROOT.TCanvas("cc")
        self.efficiencyHisto.SetXTitle("p_{T}^{raw}")
        self.efficiencyHisto.SetYTitle("#eta_{jet}")
        self.efficiencyHisto.Draw("COLZ")
        c.Print("~/tmp/HLTMCWeighter_"+name+".png")
        rf = ROOT.TFile("~/tmp/HLTMCWeighter_"+name+".root", "RECREATE")

        todo = [ self.efficiencyHisto,  self.nom,  self.denom]
        for t in todo:
            t.Write()


if __name__ == "__main__":

    setStyle()
    '''
    weighter = HLTMCWeighter("HLT_Jet15U_raw", period="A")
    weighter.dumpEfficiencyHisto("Jet15U_raw_A")
    weighter = HLTMCWeighter("HLT_Jet15U_raw", period="B")
    weighter.dumpEfficiencyHisto("Jet15U_raw_B")
    #weighter = HLTMCWeighter("HLT_DoubleJet15U_ForwardBackward")
    weighter = HLTMCWeighter("HLT_DoubleJet15U_ForwardBackward_raw", period="A")
    weighter.dumpEfficiencyHisto("DoubleJet15U_ForwardBackward_raw_A")
    weighter = HLTMCWeighter("HLT_DoubleJet15U_ForwardBackward_raw", period="B")
    weighter.dumpEfficiencyHisto("DoubleJet15U_ForwardBackward_raw_B")
    '''

    '''
    weighter = HLTMCWeighter("HLT_DoubleJet15U_ForwardBackward_raw")
    weighter.dumpEfficiencyHisto("DoubleJet15U_ForwardBackward_raw")
    '''

    #'''
    weighter = HLTMCWeighter("HLT_DoubleJet15U_ForwardBackward_L1Seeding_raw")
    weighter.dumpEfficiencyHisto("DoubleJet15U_ForwardBackward_L1Seeding_raw")
    weighter = HLTMCWeighter("HLT_DoubleJet15U_ForwardBackward_raw")
    weighter.dumpEfficiencyHisto("DoubleJet15U_ForwardBackward_raw")
    #weighter = HLTMCWeighter("HLT_Jet15U_L1Seeding_raw")
    #weighter.dumpEfficiencyHisto("Jet15U_L1Seeding_raw")
    #weighter = HLTMCWeighter("HLT_Jet15U_raw")
    #weighter.dumpEfficiencyHisto("Jet15U_raw")

    '''
    periods = ["A","B"]
    for p in periods:
        weighter = HLTMCWeighter("HLT_Jet15U_L1Seeding_raw", period=p)
        weighter.dumpEfficiencyHisto("Jet15U_L1Seeding_raw_"+p)
        weighter = HLTMCWeighter("HLT_Jet15U_raw", period=p)
        weighter.dumpEfficiencyHisto("Jet15U_raw_"+p)
    '''




    '''
    i = 0
    for r in sorted(weighter.runs):
        #if i > 50: break
        i+=1
        print i
        w = HLTMCWeighter("HLT_Jet15U_L1Seeding_raw", period=r)
        #w.dumpEfficiencyHisto("Jet15U_L1Seeding_raw_"+str(r))
    #'''


    #'''

    #print weighter.getEfficiency(-4.55, 65)
    #print weighter.getEfficiency(-4.9, 65)


