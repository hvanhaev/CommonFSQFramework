#!/usr/bin/env python

import sys, os, time
sys.path.append(os.path.dirname(__file__))

import ROOT
ROOT.gROOT.SetBatch(True)
ROOT.gSystem.Load("libFWCoreFWLite.so")
ROOT.AutoLibraryLoader.enable()
from ROOT import edm, JetCorrectionUncertainty

from array import *


# Following import breaks things. Why???
#import math

# please note that python selector class name (here: BalanceTreeProducer) 
# should be consistent with this file name (BalanceTreeProducer.py)

# you have to run this file from directory where it is saved


from MNTriggerStudies.MNTriggerAna.ExampleProofReader import ExampleProofReader

class JetGetter:
    def __init__(self, jType, JER, JECunc):
        self.JER = JER
        self.JECunc = JECunc

        if jType == "PF":
            self.jetcol = "pfJetsSmear"
            self.jetcolGen ="pfJets2Gen"
            self.jetcolReco = "pfJets"
        elif jType == "Calo":
            raise Exception("Jet collection not known "+jType)
        else:
            raise Exception("Jet collection not known "+jType)

        self.cnt = 0
        self.knownShifts = set(["_central", "_ptUp", "_ptDown", "_jerUp", "_jerDown"])
        self.shiftsTODO = set()

    def shiftsAvaliable(self):
        return self.knownShifts

    def doShifts(self, shifts):
        for s in shifts:
            if s not in self.knownShifts:
                print "#"*30
                print "Shift not known:", s
                continue
            self.shiftsTODO.add(s)

        if len(self.shiftsTODO) == 0:
            raise Exception("No shifts given!")

    def newEvent(self, chain):
        '''
        self.jets =  getattr(chain, self.jetcol) # smeared / broken again
        sTODO = len(self.shiftsTODO)
        hasCentral = "_central" in self.shiftsTODO
        if sTODO > 1 or not hasCentral: # TODO: actually used only by JER
            self.recoGenJets =  getattr(chain, self.jetcolGen)
            self.recoBaseJets =  getattr(chain, self.jetcolReco)
        '''
        self.recoGenJets =  getattr(chain, self.jetcolGen)
        self.recoBaseJets =  getattr(chain, self.jetcolReco)

    # TODO: cacheing
    def getSmeared(self, recoJetNoSmear, genJet, shift):
        if genJet.pt() < 0.01: 
            return recoJetNoSmear
        eta = abs(recoJetNoSmear.eta())
        if eta > 5.:
            return recoJetNoSmear

        isOK = False
        for jerEntry in self.JER:
            if eta < jerEntry[0]:
                isOK = True
                break
        if not isOK:
            raise Exception("Cannot determine eta range "+ str(eta))
        if shift == "_central":
            factor = jerEntry[1]
        elif shift.endswith("Down"):
            factor = jerEntry[3]
        elif shift.endswith("Up"):
            factor = jerEntry[2]
        else:
            raise Exception("Smear shift not known " + shift)

        ptRec = recoJetNoSmear.pt()
        ptGen = genJet.pt()
        diff = ptRec-ptGen
        ptRet = max(0, ptGen+factor*diff)
        #print "    ", shift, eta, "d="+str(diff), "f="+str(factor), "|", ptGen, ptRec, ptRet
        if ptRet == 0:
            return ROOT.reco.Candidate.LorentzVector(0, 0, 0, 0)
        else:
            scaleFactor = ptRet/ptRec
            return recoJetNoSmear* scaleFactor

    # TODO: cacheing
    def get(self, shift):
        self.cnt = 0
        if shift not in self.knownShifts:   # variation of a different kind, e.g. from PU
            shift = "_central"

        isJEC = shift.startswith("_pt")
        isJER = shift.startswith("_jer")
        isCentral = shift == ("_central")
        
        #while self.cnt < self.jets.size():
        while self.cnt < self.recoBaseJets.size():
            #jetSmeared = self.jets.at(self.cnt)
            genJet = self.recoGenJets.at(self.cnt)
            recoJetNoSmear = self.recoBaseJets.at(self.cnt)
            if isCentral or isJEC:
                jetSmeared =  self.getSmeared(recoJetNoSmear, genJet, "_central")

            if isCentral:
                yield jetSmeared
                self.cnt += 1 # we could use a single cnt+=1 at the end, but this would be error prone
                continue 
            else:
                if isJEC:
                    self.JECunc.setJetEta(jetSmeared.eta())
                    self.JECunc.setJetPt(jetSmeared.pt()) # should I use here smeared or normal pt??
                    unc = self.JECunc.getUncertainty(True)
                    if "_ptUp" == shift:
                        ptFactor = 1.
                    elif "_ptDown" == shift:
                        ptFactor = -1.
                    factor = (1. + ptFactor*unc)
                    if factor <= 0: 
                        yield ROOT.reco.Candidate.LorentzVector(0, 0, 0, 0)
                        self.cnt+=1
                        continue 
                    else:
                        yield jetSmeared*factor
                        self.cnt+=1
                        continue 
                elif isJER:
                    #genJet = self.recoGenJets.at(self.cnt)
                    #recoJetNoSmear = self.recoBaseJets.at(self.cnt)
                    yield self.getSmeared(recoJetNoSmear, genJet, shift)
                    self.cnt+=1
                    continue 
                else:
                    raise Exception("getJets - never should get here")


class BalanceTreeProducer(ExampleProofReader):
    def configureAnalyzer( self):

        self.tree = ROOT.TTree("data", "data")
        self.GetOutputList().Add(self.tree)

        self.var = {}
        self.todoShifts = ["_central"]
        if hasattr(self, "jetUncFile") and not self.isData and self.doPtShiftsJEC:
            self.todoShifts.append("_ptUp")
            self.todoShifts.append("_ptDown")
            self.jetUnc = JetCorrectionUncertainty(self.jetUncFile)
        else:
            self.jetUnc = None

        if not self.isData and self.doPtShiftsJER:
            self.todoShifts.append("_jerUp")
            self.todoShifts.append("_jerDown")

        for t in self.todoShifts:
            self.var["tagPt"+t] = array('d', [0])
            self.var["tagEta"+t] = array('d', [0])
            self.var["probePt"+t] = array('d', [0])
            self.var["probeEta"+t] = array('d', [0])
            self.var["ptAve"+t] = array('d', [0])
            self.var["balance"+t] = array('d', [0])

        self.var["weight"] = array('d', [0])
        
        for v in self.var:
            self.tree.Branch(v, self.var[v], v+"/D")
        
        jet15FileV2 = edm.FileInPath("MNTriggerStudies/MNTriggerAna/test/MNxsectionAna/data/PUJet15V2.root").fullPath()   # MC gen distribution
        puFiles = {}
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

        #     def __init__(self, jType, JER, JECunc):

        self.jetGetter = JetGetter("PF", self.jer, self.jetUnc)
        sys.stdout.flush()


    def ptShifted(self, jet, jetIndex, shift):
        isJEC = shift.startswith("_pt")
        isJER = shift.startswith("_jer")
        #isCentral = shift.startswith("_central")
        isCentral = not isJER and not isJEC

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
            unc = self.jetUnc.getUncertainty(true)
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


    def analyze(self):
        #print "----"
        if self.fChain.ngoodVTX == 0: return
        if self.isData:
            if self.fChain.jet15 < 0.5:
                return 1
            
        for v in self.var:
            self.var[v][0] = 0
    


        self.jetGetter.newEvent(self.fChain)
        recoJets = getattr(self.fChain, self.recoJetCollection)



        fill = False
        for shift in self.todoShifts:
            weight = 1. 
            if not self.isData:
                weight *= self.fChain.genWeight # keep inside shift iter
                truePU = self.fChain.puTrueNumInteractions
                puWeight =  self.lumiWeighters["_jet15_central"].weight(truePU)
                weight *= puWeight

            self.var["weight"][0] = weight


            tagJet = None
            probeJet = None
            probePT = None
            tagPT = None


            dbgCnt = 0
            for jet in self.jetGetter.get(shift):
            #for i in xrange(0, recoJets.size()):
            #    jet = recoJets.at(i)
                dbgJet = recoJets.at(dbgCnt)
                dbgCnt+=1
                #print shift, dbgCnt,"|", jet.pt(), jet.eta(), "|", dbgJet.pt(), dbgJet.eta()

                pt = jet.pt()
                if pt < 35: continue
                eta = abs(jet.eta())
                if eta > 4.7: continue
                if eta < 1.4:
                    tagJet = jet
                    tagPT = pt
                else:
                    probeJet = jet
                    probePT = pt

            if tagJet != None and probeJet != None:
                # check veto:
                badEvent = False
                ptAve = (probePT+tagPT)/2
                for jet in self.jetGetter.get(shift):
                #for i in xrange(0, recoJets.size()):
                    if jet == tagJet or probeJet == jet: continue
                    eta = abs(jet.eta())
                    if eta > 4.7: continue
                    veto =  jet.pt()/ptAve
                    if veto > 0.2:
                        badEvent = True
                        break
                if not badEvent:
                    self.var["tagPt"+shift][0] = tagPT 
                    self.var["tagEta"+shift][0] =  abs(tagJet.eta())
                    self.var["probePt"+shift][0] = probePT
                    self.var["probeEta"+shift][0] = abs(probeJet.eta())
                    self.var["ptAve"+shift][0] = ptAve
                    self.var["balance"+shift][0] = (probePT-tagPT)/ptAve
                    fill = True

   
        # at least one variation ok.
        if fill:
            #print "Filll!"
            self.tree.Fill()

        return 1


if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    ROOT.gSystem.Load("libFWCoreFWLite.so")
    ROOT.AutoLibraryLoader.enable()

    sampleList = None
    maxFilesMC = None
    maxFilesData = None
    nWorkers = None # Use all

    # debug config:
    #sampleList=[]
    #sampleList.append("QCD_Pt-15to3000_TuneZ2star_Flat_HFshowerLibrary_7TeV_pythia6")
    #sampleList.append("JetMETTau-Run2010A-Apr21ReReco-v1")
    #sampleList.append("Jet-Run2010B-Apr21ReReco-v1")
    #sampleList = ["JetMET-Run2010A-Apr21ReReco-v1"]
    #sampleList = ["JetMETTau-Run2010A-Apr21ReReco-v1", "Jet-Run2010B-Apr21ReReco-v1", "JetMET-Run2010A-Apr21ReReco-v1", "METFwd-Run2010B-Apr21ReReco-v1"]
    #maxFilesData = 1
    #maxFilesMC = 1
    #nWorkers = 1


    slaveParams = {}
    slaveParams["threshold"] = 35.
    #slaveParams["doPtShiftsJEC"] = False
    slaveParams["doPtShiftsJEC"] = True

    #slaveParams["doPtShiftsJER"] = False
    slaveParams["doPtShiftsJER"] = True


    #slaveParams["recoJetCollection"] = "pfJets"
    slaveParams["recoJetCollection"] = "pfJetsSmear"
    slaveParams["recoJetCollectionBaseReco"] = "pfJets"
    slaveParams["recoJetCollectionGEN"] = "pfJets2Gen"
    #slaveParams["recoJetCollection"] = "caloJets"
    #slaveParams["recoJetCollection"] = "caloJetsSmear"

    #jetUncFile = "START42_V11_AK5PF_Uncertainty.txt"
    jetUncFile = "START41_V0_AK5PF_Uncertainty.txt"


    slaveParams["jetUncFile"] =  edm.FileInPath("MNTriggerStudies/MNTriggerAna/test/MNxsectionAna/"+jetUncFile).fullPath()


    BalanceTreeProducer.runAll(treeName="mnXS",
                               slaveParameters=slaveParams,
                               sampleList=sampleList,
                               maxFilesMC = maxFilesMC,
                               nWorkers=nWorkers,
                               outFile = "treeDiJetBalance.root" )


