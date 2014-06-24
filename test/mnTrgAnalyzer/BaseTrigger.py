class TriggerObjectsGetter:
    def __init__(self, chain, collection):
        self.run = -1
        self.ev = -1
        self.trgMomenta = None
        self.chain = chain
        self.collection = collection

    def get(self):
        newEvent = False
        ev = self.chain.event
        run = self.chain.run
        if self.ev != ev or self.run != run:
            self.ev = ev
            self.run = run
            newEvent = True

        if not newEvent:
            return self.trgMomenta

        jets = getattr(self.chain, self.collection)
        self.trgMomenta = []
        for j in jets:
            if j.pt() < 15: continue
            self.trgMomenta.append(j)
        
        self.trgMomenta = sorted(self.trgMomenta, reverse = True, key = lambda j: j.pt())
        return self.trgMomenta

class BaseTrigger:
    def __init__(self, objectsGetter):
        self.objectsGetter = objectsGetter
        self.init()

    def init(self):
        ''' initialization routine for derived classes '''
        pass

    #def getDecision(self, threshold):
        
    def getMaxThr(self):
        return 0

class ForwardBackwardTrigger(BaseTrigger):
    def getMaxThr(self):
        hltJets = self.objectsGetter.get()
        #print "XXX", len(hltJets)
        bestF = None
        bestB = None
        for j in hltJets:
            eta = j.eta()
            if abs(eta) < 3.: continue
            pt = j.pt()
            if eta > 0:
                if bestF == None or pt > bestF:
                    bestF= pt
            else:
                if bestB == None or pt > bestB:
                    bestB = pt

        if None in [bestF, bestB]:
            return 0.

        return min(bestF, bestB)

