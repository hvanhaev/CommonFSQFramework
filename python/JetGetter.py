import ROOT
ROOT.gROOT.SetBatch(True)
ROOT.gSystem.Load("libFWCoreFWLite.so")
ROOT.AutoLibraryLoader.enable()
from ROOT import edm, JetCorrectionUncertainty

class Jet():
    def __init__(self, p4, i, genJetCollection, jetID):
        self.p4vec = p4
        self.i = i
        self.genCol = genJetCollection
        self.jetID = jetID
        self.dr = ROOT.Math.VectorUtil.DeltaR


    def p4(self):
        return self.p4vec

    def pt(self):
        return self.p4vec.pt()

    def phi(self):
        return self.p4vec.phi()

    def eta(self):
        return self.p4vec.eta()

    def looseId(self):
        if self.i == None:
            return False
        ret = self.jetID.at(self.i)
        #print "XXX", ret
        return ret

    def genP4(self):
        if self.i == None:
            return ROOT.reco.Candidate.LorentzVector(0, 0, 0, 0)

        return self.genCol.at(self.i)

    def __eq__(self, other):
        if other == None: return False
        #if self.p4 == other.p4: return True # could speed up a bit
        dr = self.dr(self.p4vec, other.p4vec)
        ret  = dr == 0.
        ret2 = dr < 0.001
        if ret != ret2:
            print "Warning:Jet:dr equality may be calculated wrong for", self.pt(), self.eta(), "|", other.pt(), other.eta()
        if not ret: return ret
        pt1 = self.pt()
        pt2 = other.pt()
        
        if pt1 != pt2:
            print "Warning:Jet:pt equality may be calculated wrong for", self.pt(), self.eta(), "|", other.pt(), other.eta()

        return ret
        

    def __neq__(self, other):
        return not self.__eq__(other)




class JetGetter:
    def __init__(self, jType):

        if jType == "PF":
            self.jetcol = "pfJetsSmear"
            self.jetcolID = "pfJets_jetID"
            self.jetcolGen ="pfJets2Gen"
            self.jetcolReco = "pfJets"
            self.setJERScenario("PF10")
        elif jType == "Calo":
            raise Exception("Jet collection not known "+jType)
            self.setJERScenario("Calo10")
        else:
            raise Exception("Jet collection not known "+jType)
        jetUncFile = "START41_V0_AK5PF_Uncertainty.txt"
        jecFileFP =  edm.FileInPath("MNTriggerStudies/MNTriggerAna/test/MNxsectionAna/"+jetUncFile).fullPath()
        self.JECunc = JetCorrectionUncertainty(jecFileFP)

        self.cnt = 0
        self.knownShifts = set(["_central", "_ptUp", "_ptDown", "_jerUp", "_jerDown"])
        self.shiftsTODO = set()

    def setJERScenario(self, scenario):
        known = set(["PF10", "PF11", "Calo10"])
        if scenario not in known:
            raise Exception("JER scenario not known: "+scenario)
        calo = []
        calo.append("1.1 1.088 0.007 0.07 0.075") 
        calo.append("1.7 1.139 0.019 0.08 0.084") 
        calo.append("2.3 1.082 0.030 0.14 0.139")
        calo.append("5.0 1.065 0.042 0.23 0.235")

        pf = []
        pf.append("1.1 1.066 0.007 0.07 0.072") 
        pf.append("1.7 1.191 0.019 0.06 0.062")
        pf.append("2.3 1.096 0.030 0.08 0.085")
        pf.append("5.0 1.166 0.050 0.19 0.199")  #ORG!

        #print "XXXX wrong JER"*50
        #pf.append("2.8 1.166 0.050 0.19 0.199") # keep org till 2.8
        #pf.append("5.0 1.288 0.127 0.155 0.153") # use factors from 2011

        pf11 = []
        pf11.append("0.5 1.052 0.012 0.062 0.061")
        pf11.append("1.1 1.057 0.012 0.056 0.055")
        pf11.append("1.7 1.096 0.017 0.063 0.062")
        pf11.append("2.3 1.134 0.035 0.087 0.085")
        pf11.append("5.0 1.288 0.127 0.155 0.153")

        if scenario == "PF10":
            self.setJER(pf)
        elif scenario == "Calo10":
            self.setJER(calo)
        elif scenario == "PF11":
            self.setJER(pf11)
        else:
            raise Exception("Thats confusing "+scenario)

    def setJER(self, todo):
        self.JER = []
        for line in todo:
            spl = line.split()
            etaMax = float(spl[0])
            jer = float(spl[1])
            err = float(spl[2])
            errUp = float(spl[3])
            errDown = float(spl[4])
            jerUp   = jer + ROOT.TMath.Sqrt(err*err+errUp*errUp)
            jerDown = jer - ROOT.TMath.Sqrt(err*err+errDown*errDown)
            print "JER factors:", etaMax, jer, jerUp, jerDown, "|", err, errUp, errDown
            self.JER.append( [etaMax, jer, jerUp, jerDown] )

    def hackJER(self):
        return
        for j in self.JER:
            j[2] = 1.5
            j[3] = 1

        print "JER overriden:"
        print self.JER


    def setJecUncertainty(self, jecUncPath):
        self.JECunc = JetCorrectionUncertainty(jecUncPath)

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
        self.recoSmearedJets =  getattr(chain, self.jetcol)
        self.recoJetID =  getattr(chain, self.jetcolID)

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
                #r1 = self.recoSmearedJets.at(self.cnt).pt()/jetSmeared.pt()
                #i1 = self.recoSmearedJets.at(self.cnt).eta()*jetSmeared.eta()
                #i1 /= abs(i1)
                #print "XXX", r1, i1

            # genJetCollection
            #    def __init__(self, p4, i, genJetCollection):
            if isCentral:
                #yield jetSmeared
                yield Jet(jetSmeared, self.cnt, self.recoGenJets, self.recoJetID)
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
                        ret = ROOT.reco.Candidate.LorentzVector(0, 0, 0, 0)
                        yield Jet(ret, None, None, None)
                        self.cnt+=1
                        continue 
                    else:
                        ret = jetSmeared*factor
                        yield Jet(ret, self.cnt, self.recoGenJets, self.recoJetID)
                        self.cnt+=1
                        continue 
                elif isJER:
                    #genJet = self.recoGenJets.at(self.cnt)
                    #recoJetNoSmear = self.recoBaseJets.at(self.cnt)
                    ret = self.getSmeared(recoJetNoSmear, genJet, shift)
                    yield Jet(ret, self.cnt, self.recoGenJets, self.recoJetID)
                    self.cnt+=1
                    continue 
                else:
                    raise Exception("getJets - never should get here")


