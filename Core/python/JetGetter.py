import ROOT
ROOT.gROOT.SetBatch(True)
ROOT.gSystem.Load("libFWCoreFWLite.so")
ROOT.AutoLibraryLoader.enable()
from ROOT import edm, JetCorrectionUncertainty

class Jet():
    def __init__(self, p4, genJet, jetID, i):
        self.p4vec = p4
        self.p4vecGen = genJet
        self.jetID = jetID
        self.i = i
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
        return self.jetID

    def jetid(self):
        return self.jetID


    def genP4(self):
        return self.p4vecGen


    # todo: use index as a first check??
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
    def __init__(self, jType, jetColOverride = None):

        # idea store gen-rec as float
        if jType == "PFAK4CHS":
            self.jetcol = "PFAK4CHSnewjets"
            self.jetcolID = "PFAK4CHSnewjetid"
            self.jetcolGen ="PFAK4CHSnewgenjets"
        elif jType == "PFAK5CHS":
            self.jetcol = "PFAK5CHSnewjets"
            self.jetcolID = "PFAK5CHSnewjetid"
            self.jetcolGen ="PFAK5CHSnewgenjets"
        elif jType == "PFAK5":
            self.jetcol = "PFAK5newjets"
            self.jetcolID = "PFAK5newjetid"
            self.jetcolGen ="PFAK5newgenjets"
        elif jType == "PFlegacy":
            self.jetcol = "PFnewjets"
            self.jetcolID = "PFnewjetid"
            self.jetcolGen ="PFnewgenjets"
            '''
            pref = "PFAK5new"
            self.jetcol = pref+"jets"
            self.jetcolID = pref+"jetid"
            self.jetcolGen = pref+"genjets"
            #'''


        elif jType == "Calo":
            raise Exception("Jet collection not known "+jType)
            self.setJERScenario("Calo10")
        else:
            raise Exception("Jet collection not known "+jType)

        if jetColOverride != None:
            print "XXX, setting jet branch to", jetColOverride
            self.jetcol = jetColOverride
        

        self.cnt = 0
        # TODO: common nameing
        self.knownShifts = {"_central":"", 
                            "_ptUp": "_jecUp"  , 
                            "_ptDown": "_jecDown", 
                            "_jerUp": "_jerUp", 
                            "_jerDown": "_jerDown"}

        self.disableGen = False
        self.disableId = False

    def disableGenJet(self, do=True):
        self.disableGen = do

    def disableJetId(self, do=True):
        self.disableId = do

    def shiftsAvaliable(self):
        return self.knownShifts.keys()

    def newEvent(self, chain):
        self.data = {} # Note: this way we enforce user to call this method (note, that self.data is not present in init)
        self.chain = chain

    # TODO: cacheing
    def get(self, shift):
        cnt = 0
        if shift not in self.knownShifts:   # variation of a different kind, e.g. from PU
            shift = "_central"

        if shift not in self.data:
            # todo: choose what is actually read
            self.data.setdefault(shift, {}).setdefault("recojets", getattr(self.chain, self.jetcol+self.knownShifts[shift]))
            if not self.disableGen:
                self.data[shift].setdefault("genjets", getattr(self.chain, self.jetcolGen+self.knownShifts[shift]))
            if not self.disableId:
                self.data[shift].setdefault("jetid", getattr(self.chain, self.jetcolID+self.knownShifts[shift]))

        while cnt < self.data[shift]["recojets"].size():
            jet = self.data[shift]["recojets"].at(cnt)
            if not self.disableGen:
                genjet = self.data[shift]["genjets"].at(cnt)
            else:
                genjet = None
            if not self.disableId:
                id =   self.data[shift]["jetid"].at(cnt)
            else:
                id = None
            yield Jet(jet, genjet, id, cnt)
            cnt += 1 # we could use a single cnt+=1 at the end, but this would be error prone
