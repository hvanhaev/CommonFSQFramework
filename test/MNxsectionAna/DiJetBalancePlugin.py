import ROOT
ROOT.gROOT.SetBatch(True)
from ROOT import *


class DiJetBalancePlugin():
    def __init__(self, jetCollection):
        self.jetCollection = jetCollection
        self.etaRanges =  []
        self.etaRanges.extend([1.401, 1.701, 2.001, 2.322, 2.411, 2.601, 2.801, 3.001, 3.201, 3.501, 3.801, 4.101, 4.701])
        self.histos = []
        for i in xrange(1, len(self.etaRanges)):
            x1=self.etaRanges[i-1]
            x2=self.etaRanges[i]
            name = "balance_"+str(x1)+"_"+str(x2)
            self.histos.append(ROOT.TH1F(name, name, 1000, 0,30))


    def getHistos(self):
        return self.histos

    def eta2histo(self, eta):
        eta = abs(eta)
        ret = -1
        for i in xrange(1, len(self.etaRanges)):
            if eta > self.etaRanges[i-1] and eta < self.etaRanges[i]:
                return i-1



    def analyze(self, fChain):
        jets = getattr(fChain, self.jetCollection)
        for jet in jets:
            print jet.pt()


if __name__ == "__main__":
    cl = DiJetBalancePlugin("teest")


    
