import BaseGetter
import ROOT
ROOT.gROOT.SetBatch(True)

class JetEntry:
    def __init__(self, jet):
        self.jet = jet
        self.cache = {}

    def pt(self):
        return self.jet.pt

    def eta(self):
        return self.jet.eta

    def phi(self):
        return self.jet.phi

    def p4(self):
        if "p4" in self.cache:
            return self.cache["p4"]
        ret = ROOT.reco.Candidate.PolarLorentzVector(self.jet.pt, self.jet.eta, self.jet.phi, 0)
        self.cache["p4"] = ret
        return ret

    def jetid(self):
        return self.jet.jetid

    def genP4(self):
        return self.jet.genpt

    '''
    # FIXME: entries from two different events can be equal
    def __eq__(self, other):
        if other == None: return False
        # TODO check if types are eqeal
        if self.jet.index != other.jet.index: return False
        if self.jet.branchPrefix != other.jet.branchPrefix: return False
        if self.jet.variation != other.jet.variation: return False
        return True

    def __neq__(self, other):
        return not self.__eq__(other)
    '''


class BetterJetGetter(BaseGetter.BaseGetter):
    def __init__(self, branchPrefix):
        BaseGetter.BaseGetter.__init__(self, branchPrefix)
        #self.knownVariations = set(["_central"])
        self.knownVariations = set(["_central", "_jecDown", "_jecUp", "_jerDown", "_jerUp"])
        self.srcBranch = branchPrefix+"pt"
        self.dphiHelper = ROOT.Math.VectorUtil.DeltaPhi
        self.drHelper = ROOT.Math.VectorUtil.DeltaR

    def getSize(self):
        return getattr(self.chain, self.srcBranch).size()
    
    def get(self, variation=""):
        for j in BaseGetter.BaseGetter.get(self, variation):
            je = JetEntry(j)
            yield je


    #def pt(self):
    #    return self.pt


