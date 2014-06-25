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
        
    def getMaxThreshold(self):
        return 0

class ForwardBackwardTrigger(BaseTrigger):
    def getMaxThreshold(self):
        hltJets = self.objectsGetter.get()
        bestF, bestB = (None, None)
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


class DoubldForwardTrigger(BaseTrigger):
    def getMaxThreshold(self):
        hltJets = self.objectsGetter.get()
        pts = []
        for j in hltJets:
            eta = j.eta()
            if abs(eta) < 3.: continue
            pts.append(j.pt())

        if len(pts) < 2:
            return 0

        return min(pts[:2])


class DoubleJetWithAtLeastOneCentralJetTrigger(BaseTrigger):
    def getMaxThreshold(self):
        hltJets = self.objectsGetter.get()
        jetsF = []
        jetsC = []
        for j in hltJets:
            eta = j.eta()
            cen = abs(eta) < 3.
            fwd = abs(eta) > 3.
            pt = j.pt()
            if cen: jetsC.append(pt)
            if fwd: jetsF.append(pt)
        
        if len(jetsC) == 0 : return 0
        if len(jetsC) + len(jetsF) < 2 : return 0
        pt1 = jetsC[0]
        jetsC.append(0) # Q&D way of making sure, we dont get out of range 
        jetsF.append(0) #    when calculating pt2 below
        pt2 = max(jetsC[1], jetsF[0])
        return min(pt1, pt2)

class PTAveForHFJecTrigger(BaseTrigger):
    def getMaxThreshold(self):
        hltJets = self.objectsGetter.get()
        tag, probe = (None, None) 
        for j in hltJets:
            eta = abs(j.eta())
            tagCand = eta < 1.4
            probeCand = eta > 2.8 and eta < 5.2
            if probeCand or tagCand:
                pt = j.pt() 
                if probeCand and (probe == None or probe < pt): probe = pt
                if tagCand and (tag == None or tag < pt): tag = pt
            
        if None in [tag, probe]:
            return 0.
        return  (tag+probe)/2


class SingleJetTrigger(BaseTrigger):
    def getMaxThreshold(self):
        hltJets = self.objectsGetter.get()
        if len(hltJets) > 0:
            return hltJets[0].pt()
        return 0
