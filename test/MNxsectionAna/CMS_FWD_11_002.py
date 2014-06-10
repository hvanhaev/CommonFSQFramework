#!/usr/bin/env python
# http://cdsweb.cern.ch/record/1347749
# http://cdsweb.cern.ch/record/1347515
# http://cdsweb.cern.ch/record/1421692?ln=en
# http://arxiv.org/abs/arXiv:1202.0704
# http://rivet.hepforge.org/code/2.1.0/a00543_source.html
from MNTriggerStudies.MNTriggerAna.ExampleProofReader import ExampleProofReader

import sys, os, time
#sys.path.append(os.path.dirname(__file__))

import ROOT
ROOT.gROOT.SetBatch(True)
from ROOT import edm, JetCorrectionUncertainty

from array import *
#import cProfile

# please note that python selector class name (here: CMS_FWD_11_002) 
# should be consistent with this file name (CMS_FWD_11_002.py)

# you have to run this file from directory where it is saved

#import DiJetBalancePlugin

class CMS_FWD_11_002(ExampleProofReader):
    def configureAnalyzer( self):

        #sys.stdout = sys.stderr
        #self.pr = cProfile.Profile()
        print "XXX configureAnalyzer - CMS_FWD_11_002", self.datasetName, self.isData

        self.todoShifts = ["_central"]
        if hasattr(self, "jetUncFile") and not self.isData and self.doPtShiftsJEC:
            self.todoShifts.append("_ptUp")
            self.todoShifts.append("_ptDown")
            self.jetUnc = JetCorrectionUncertainty(self.jetUncFile)

        if not self.isData and self.doPtShiftsJER:
            self.todoShifts.append("_jerUp")
            self.todoShifts.append("_jerDown")


        #self.djBalance = DiJetBalancePlugin.DiJetBalancePlugin(self.recoJetCollection)

        self.hist = {}
        todoTrg = ["_jet15"]


        pedroPtBins = array('d', [35, 45, 57, 72, 90, 120, 150, 200])
        for shift in self.todoShifts:
            for trg in todoTrg:
                t = shift+trg
                self.hist["ptFwd"+t] =  ROOT.TH1F("ptFwd"+t,   "ptFwd"+t,  100, 0, 100)
                self.hist["ptCen"+t] =  ROOT.TH1F("ptCen"+t,   "ptCen"+t,  100, 0, 100)
                self.hist["etaFwd"+t] =  ROOT.TH1F("etaFwd"+t,   "etaFwd"+t,  100, -5, 5)
                self.hist["etaCen"+t] =  ROOT.TH1F("etaCen"+t,   "etaCen"+t,  100, -5, 5)
                self.hist["vtx"+t] =  ROOT.TH1F("vtx"+t,   "vtx"+t,  10, -0.5, 9.5)
                self.hist["pedro"+t] = ROOT.TH1F("ptFwdNormBinw"+t, "ptFwdNormBinw"+t, len(pedroPtBins)-1, pedroPtBins)
                

        # follow the histogram naming convention even if it makes no sense for gen - needed for drawPlots.py
        self.hist["pedroGen"] = ROOT.TH1F("pedroGen_central_jet15", "pedroGen_central_jet15", len(pedroPtBins)-1, pedroPtBins)
        self.hist["pedroBase"] = ROOT.TH1F("pedroBase_central_jet15", "pedroBase_central_jet15", len(pedroPtBins)-1, pedroPtBins)



        for h in self.hist:
            self.hist[h].Sumw2()
            self.GetOutputList().Add(self.hist[h])


        puFiles = {}
        # MNTriggerStudies/MNTriggerAna/test/MNxsectionAna/
        jet15FileV2 = edm.FileInPath("MNTriggerStudies/MNTriggerAna/test/MNxsectionAna/data/PUJet15V2.root").fullPath()   # MC gen distribution

        puFiles["dj15_1"] = edm.FileInPath("MNTriggerStudies/MNTriggerAna/test/MNxsectionAna/data/pu_dj15_1_0.root").fullPath()
        puFiles["dj15_1_05"] = edm.FileInPath("MNTriggerStudies/MNTriggerAna/test/MNxsectionAna/data/pu_dj15_1_05.root").fullPath()
        puFiles["dj15_0_95"] = edm.FileInPath("MNTriggerStudies/MNTriggerAna/test/MNxsectionAna/data/pu_dj15_0_95.root").fullPath()
        puFiles["j15_1"] = edm.FileInPath("MNTriggerStudies/MNTriggerAna/test/MNxsectionAna/data/pu_j15_1_0.root").fullPath()
        puFiles["j15_1_05"] = edm.FileInPath("MNTriggerStudies/MNTriggerAna/test/MNxsectionAna/data/pu_j15_1_05.root").fullPath()
        puFiles["j15_0_95"] = edm.FileInPath("MNTriggerStudies/MNTriggerAna/test/MNxsectionAna/data/pu_j15_0_95.root").fullPath()

        self.lumiWeighters = {}
        self.lumiWeighters["_jet15_central"] = edm.LumiReWeighting(jet15FileV2, puFiles["j15_1"], "MC", "pileup")
        self.lumiWeighters["_jet15_puUp"] = edm.LumiReWeighting(jet15FileV2, puFiles["j15_1_05"], "MC", "pileup")
        self.lumiWeighters["_jet15_puDown"] = edm.LumiReWeighting(jet15FileV2, puFiles["j15_0_95"], "MC", "pileup")

        self.lumiWeighters["_dj15fb_central"] = edm.LumiReWeighting(jet15FileV2, puFiles["dj15_1"], "MC", "pileup")
        self.lumiWeighters["_dj15fb_puUp"] = edm.LumiReWeighting(jet15FileV2, puFiles["dj15_1_05"], "MC", "pileup")
        self.lumiWeighters["_dj15fb_puDown"] = edm.LumiReWeighting(jet15FileV2, puFiles["dj15_0_95"], "MC", "pileup")

        calo = []
        calo.append("1.1 1.088 0.007 0.07 0.075") 
        calo.append("1.7 1.139 0.019 0.08 0.084") 
        calo.append("2.3 1.082 0.030 0.14 0.139")
        calo.append("5.0 1.065 0.042 0.23 0.235")

        pf = []
        pf.append("1.1 1.066 0.007 0.07 0.072") 
        pf.append("1.7 1.191 0.019 0.06 0.062")
        pf.append("2.3 1.096 0.030 0.08 0.085")
        pf.append("5.0 1.166 0.050 0.19 0.199") 

        ''' 2011 factors for xcheck
        # for this factors obtained up/down values are
        # consistent with those from JetResolution twiki
        # https://twiki.cern.ch/twiki/bin/viewauth/CMS/JetResolution
        pf.append("0.5 1.052 0.012 0.062 0.061")
        pf.append("1.1 1.057 0.012 0.056 0.055")
        pf.append("1.7 1.096 0.017 0.063 0.062")
        pf.append("2.3 1.134 0.035 0.087 0.085")
        pf.append("5.0 1.288 0.127 0.155 0.153")
        '''

        todo = None
        if self.recoJetCollection.startswith("pf"):
            todo = pf
        elif self.recoJetCollection.startswith("calo"):
            todo = calo
        else:
            raise Exception("Dont know how to apply JER smearing to " + self.recoJetCollection)

        self.jer = []
        for line in todo:
            spl = line.split()
            etaMax = float(spl[0])
            jer = float(spl[1])
            err = float(spl[2])
            errUp = float(spl[3])
            errDown = float(spl[4])
            jerUp   = jer + ROOT.TMath.Sqrt(err*err+errUp*errUp)
            jerDown = jer - ROOT.TMath.Sqrt(err*err+errDown*errDown)
            #jerUp = 1
            #jerDown = 1 # XXAA
            print "JER factors:", etaMax, jer, jerUp, jerDown, "|", err, errUp, errDown
            self.jer.append( [etaMax, jer, jerUp, jerDown] )

    def ptShifted(self, jet, jetIndex, shift):
        isJEC = shift.startswith("_pt")
        isJER = shift.startswith("_jer")
        isCentral = shift.startswith("_central")

        if self.isData:
            return jet.pt()
            #raise Exception("pt shift for data called")

        #ptBase = 
        if isJEC or isCentral: 
            recoGenJets =  getattr(self.fChain, self.recoJetCollectionGEN)
            genJet = recoGenJets.at(jetIndex)
            recoJets    = getattr(self.fChain, self.recoJetCollectionBaseReco)
            recoJet = recoJets.at(jetIndex)
            if genJet.pt() < 1:
                ptBase = recoJet.pt()
            else:
                eta = abs(recoJet.eta())
                isOK = False
                for jerEntry in self.jer:
                    if eta < jerEntry[0]:
                        isOK = True
                        break
                if not isOK:
                    raise Exception("Cannot determine eta range "+ str(eta))
                factorCentral = jerEntry[1]
                ptGen =  genJet.pt()
                diff = recoJet.pt() - ptGen
                ptBase = max(0, ptGen+factorCentral*diff)

            pt = ptBase
            if  "_central" == shift:
                return pt

            self.jetUnc.setJetEta(recoJet.eta())
            self.jetUnc.setJetPt(pt) # corrected pt
            unc = self.jetUnc.getUncertainty(True)
            if "_ptUp" == shift:
                ptFactor = 1.
            elif "_ptDown" == shift:
                ptFactor = -1.
            pt *= (1. + ptFactor*unc)

            if pt < 0: return 0
            return pt 

        if isJER:
            recoGenJets =  getattr(self.fChain, self.recoJetCollectionGEN)
            genJet = recoGenJets.at(jetIndex)
            recoJets = getattr(self.fChain, self.recoJetCollectionBaseReco)
            recoJet = recoJets.at(jetIndex)
            if genJet.pt() < 1:
                return recoJet.pt()
            eta = abs(recoJet.eta())
            isOK = False
            for jerEntry in self.jer:
                if eta < jerEntry[0]:
                    isOK = True
                    break
            if not isOK:
                raise Exception("Cannot determine eta range "+ str(eta))
            factorCentral = jerEntry[1]

            if shift.endswith("Down"):
                factor = jerEntry[3]
            elif shift.endswith("Up"):
                factor = jerEntry[2]

            factorCentral = jerEntry[1]

            ptRec = recoJet.pt()
            ptGen = genJet.pt()
            diff = ptRec-ptGen
            ptRet = max(0, ptGen+factor*diff)

            #ptSmearedCentral = max(0, ptGen+factorCentral*diff)
            #print ptRec, recoJet.pt(), ptSmearedCentral, ptRet, shift
            return ptRet


    '''
    # stuff for code profiling
    def analyze(self):
        self.pr.enable()
        self.analyzeTT()
        self.pr.disable()


    def SlaveTerminate( self ):
        print 'py: slave terminating AAZAZ'
        dname = "/scratch/scratch0/tfruboes/2014.05.NewFWAnd4_2/CMSSW_4_2_8_patch7/src/MNTriggerStudies/MNTriggerAna/test/MNxsectionAna/stats/"
        profName = dname + "stats"
        self.pr.dump_stats(profName)
   # '''
        


    #def analyzeTT(self):
    def analyze(self):

        if not self.isData:
            fwdPt = None
            cenPt = None
            genJets = self.fChain.genJets
            for i in xrange(genJets.size()):
                j = genJets.at(i)
                pt = j.pt()
                if pt < 35. : continue
                eta = abs(j.eta())
                if eta > 4.7: continue
                if fwdPt == None and eta > 3.2 and eta < 4.7:
                    fwdPt = pt
                if cenPt == None and eta < 2.8:
                    cenPt = pt
            if cenPt != None and fwdPt != None:
                weight = self.fChain.genWeight
                etaFactor = 3.
                binN =  self.hist["pedroGen"].FindBin(pt)
                binWidthFactor = self.hist["pedroGen"].GetBinWidth(binN)
                self.hist["pedroGen"].Fill(fwdPt, weight/(etaFactor*binWidthFactor))

        trg = self.fChain.jet15 > 0.5
        if not self.isData or trg:
            fwdPt = None
            cenPt = None
            pJets = self.fChain.pfJetsSmear
            for i in xrange(pJets.size()):
                j = pJets.at(i)
                pt = j.pt()
                if pt < 35. : continue
                eta = abs(j.eta())
                if eta > 4.7: continue
                #print "XA", pt, eta
                if fwdPt == None and eta > 3.2 and eta < 4.7:
                    fwdPt = pt
                if cenPt == None and eta < 2.8:
                    cenPt = pt
            if cenPt != None and fwdPt != None:
                weight = 1.
                if not self.isData:
                    weight = self.fChain.genWeight
                etaFactor = 3.
                binN =  self.hist["pedroBase"].FindBin(pt)
                binWidthFactor = self.hist["pedroBase"].GetBinWidth(binN)
                #print "Base fill:", fwdPt, etaFactor, binWidthFactor
                self.hist["pedroBase"].Fill(fwdPt, weight/(etaFactor*binWidthFactor))


        if self.fChain.ngoodVTX == 0: return
        recoJets = getattr(self.fChain, self.recoJetCollection)
        jetID = getattr(self.fChain, self.jetID)

        for shift in self.todoShifts:
            triggerToUse = "_jet15"
            histoName = shift +triggerToUse

            if self.isData:
                if self.fChain.jet15 < 0.5:
                    continue

            # find best fwd-central pair
            fwdPt = None
            cenPt = None
            fwdEta = None
            cenEta = None
            for i in xrange(recoJets.size()):
                jet = recoJets.at(i)
                eta = abs(jet.eta())
                if eta > 4.7: continue
                pt = self.ptShifted(jet, i, shift)
                if pt < 35. : continue
                if jetID.at(i) < 0.5: continue
                #print "XA", pt, eta
                if fwdPt == None and eta > 3.2 and eta < 4.7:
                    fwdPt = pt
                    fwdEta = jet.eta()
                if cenPt == None and eta < 2.8:
                    cenPt = pt
                    cenEta = jet.eta()

            if cenPt != None and fwdPt != None:
                if not self.isData:
                    weightBase = 1. 
                    if not self.isData:
                        weightBase *= self.fChain.genWeight # keep inside shift iter
                    weight = weightBase
                    truePU = self.fChain.puTrueNumInteractions
                    puWeight =  self.lumiWeighters[triggerToUse+"_central"].weight(truePU)
                    weight *= puWeight

                etaFactor = 3.
                binN =  self.hist["pedro"+histoName].FindBin(pt)
                binWidthFactor = self.hist["pedro"+histoName].GetBinWidth(binN)
                self.hist["pedro"+histoName].Fill(fwdPt, weight/(etaFactor*binWidthFactor))

                self.hist["ptFwd"+histoName].Fill(fwdPt, weight)
                self.hist["ptCen"+histoName].Fill(cenPt, weight)
                self.hist["etaFwd"+histoName].Fill(fwdEta , weight)
                self.hist["etaCen"+histoName].Fill(cenEta, weight)
                self.hist["vtx"+histoName].Fill(self.fChain.ngoodVTX, weight)

        return 1



    @classmethod
    def testAll(cls):
        # same as the label of EDProducer that was used to produce the trees
        #todo = [400, 100, 25, 8, 2]
        todo =[1,6,25,100,400]
        #todo = [8]
        for t in todo:
            oname = "~/tmp/plots_"+str(t)+".root"
            onameMerged = "~/tmp/plotsMerged_"+str(t)+".root"
            #pr = CMS_FWD_11_002()
            #pr.runAll(treeName="exampleTree", outFile = oname, maxFiles = t)
            #CMS_FWD_11_002.CMS_FWD_11_002().runAll(treeName="exampleTree", outFile = oname, maxFiles = t)
            cls.runAll(treeName="exampleTree", outFile = oname, maxFiles = t)
            os.system("../../scripts/normalizeAndAddHistograms.py -i "+oname + " -o " + onameMerged)



if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    ROOT.gSystem.Load("libFWCoreFWLite.so")
    ROOT.AutoLibraryLoader.enable()

    sampleList = None
    maxFilesMC = None
    maxFilesData = None
    nWorkers = None # Use all

    # debug config:
    #sampleList = []
    #sampleList.append("QCD_Pt-15to3000_TuneZ2star_Flat_HFshowerLibrary_7TeV_pythia6")
    #sampleList.append("JetMETTau-Run2010A-Apr21ReReco-v1")
    #sampleList=  ["Jet-Run2010B-Apr21ReReco-v1"] 
    #sampleList = ["JetMET-Run2010A-Apr21ReReco-v1"]
    #sampleList = ["JetMETTau-Run2010A-Apr21ReReco-v1", "Jet-Run2010B-Apr21ReReco-v1", "JetMET-Run2010A-Apr21ReReco-v1", "METFwd-Run2010B-Apr21ReReco-v1"]
    maxFilesMC = 1
    maxFilesData = 1
    #nWorkers = 16
    #maxFilesData = 1
    nWorkers = 1


    slaveParams = {}
    slaveParams["threshold"] = 35.
    #slaveParams["doPtShiftsJEC"] = False
    slaveParams["doPtShiftsJEC"] = True

    #slaveParams["doPtShiftsJER"] = False
    slaveParams["doPtShiftsJER"] = True

    slaveParams["recoJetCollection"] = "pfJets"
    #slaveParams["recoJetCollection"] = "pfJetsSmear" 
    slaveParams["recoJetCollectionBaseReco"] = "pfJets"
    slaveParams["recoJetCollectionGEN"] = "pfJets2Gen"


    slaveParams["jetID"] = "pfJets_jetID"



    #slaveParams["recoJetCollection"] = "caloJets"
    #slaveParams["recoJetCollection"] = "caloJetsSmear"

    #jetUncFile = "START42_V11_AK5PF_Uncertainty.txt"
    jetUncFile = "START41_V0_AK5PF_Uncertainty.txt"


    slaveParams["jetUncFile"] =  edm.FileInPath("MNTriggerStudies/MNTriggerAna/test/MNxsectionAna/"+jetUncFile).fullPath()


    CMS_FWD_11_002.runAll(treeName="mnXS",
                               slaveParameters=slaveParams,
                               sampleList=sampleList,
                               maxFilesMC = maxFilesMC,
                               maxFilesData = maxFilesData,
                               nWorkers=nWorkers,
                               outFile = "plotsCMS_FWD_11_002.root" )



