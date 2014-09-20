import ROOT

class TriggerObjectsGetter:
    def __init__(self, chain, collection, minPT=None, maxDR=0.8):
        self.run = -1
        self.ev = -1
        self.trgMomenta = {}
        self.chain = chain
        self.collection = collection
        self.minPT = minPT
        self.dr = ROOT.Math.VectorUtil.DeltaR
        self.maxDR = maxDR

    def get(self, matchingObjects = None):
        newEvent = False
        ev = self.chain.event
        run = self.chain.run
        if self.ev != ev or self.run != run:
            self.ev = ev
            self.run = run
            newEvent = True
        if newEvent:
            self.trgMomenta = {}

        idnum = id(matchingObjects) 
        if  idnum in self.trgMomenta:
            return self.trgMomenta[idnum]

        self.trgMomenta[idnum] = []
        jets = getattr(self.chain, self.collection)
        for j in jets:
            if self.minPT != None and j.pt() < self.minPT: continue
            isOK = True
            if matchingObjects != None:
                for m in matchingObjects:
                    dr = self.dr(m, j)
                    if dr > self.maxDR: continue
                    #print "XXX match", dr, m.eta(), m.phi(), j.eta(), j.phi()
                    break 
                else: # executed only if we dont hit break line above
                    isOK = False

            if isOK:
                self.trgMomenta[idnum].append(j)
            #else:
            #    print "XXX no match"
        
        self.trgMomenta[idnum] = sorted(self.trgMomenta[idnum], reverse = True, key = lambda j: j.pt())
        return self.trgMomenta[idnum]

class BaseTrigger:
    def __init__(self, objectsGetter):
        self.objectsGetter = objectsGetter
        self.init()

    def init(self):
        ''' initialization routine for derived classes '''
        pass

    #def getDecision(self, threshold):
        
    def getMaxThreshold(self, topologyFullfillyingObjects = None):
        return 0

class ForwardBackwardTrigger(BaseTrigger):
    def getMaxThreshold(self, topologyFullfillyingObjects = None):
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
    def getMaxThreshold(self, topologyFullfillyingObjects = None):
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
    def getMaxThreshold(self, topologyFullfillyingObjects = None):
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
    def getMaxThreshold(self, topologyFullfillyingObjects = None):
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
    def getMaxThreshold(self, topologyFullfillyingObjects = None):
        hltJets = self.objectsGetter.get()
        if len(hltJets) > 0:
            return hltJets[0].pt()
        return 0



class SingleForwardJetTrigger(BaseTrigger):
    def __init__(self, getter, etaLim = 2.5):
        BaseTrigger.__init__(self, getter)
        self.etaLim  = etaLim

    def getMaxThreshold(self, topologyFullfillyingObjects = None):
        if topologyFullfillyingObjects != None and len(topologyFullfillyingObjects) != 1:
            raise Exception("Expected 1 good object, got " + str(len(topologyFullfillyingObjects)))

        hltJets = self.objectsGetter.get(topologyFullfillyingObjects)
        for j in hltJets:
            if abs(j.eta() ) < self.etaLim: continue
            return j.pt()
        return 0



class SingleCentralJetTrigger(BaseTrigger):
    def __init__(self, getter, etaLim = 3.5):
        BaseTrigger.__init__(self, getter)
        self.etaLim  = etaLim
    def getMaxThreshold(self, topologyFullfillyingObjects = None):
        if topologyFullfillyingObjects != None and len(topologyFullfillyingObjects) != 1:
            raise Exception("Expected 1 good object, got " + str(len(topologyFullfillyingObjects)))
        hltJets = self.objectsGetter.get(topologyFullfillyingObjects)
        #print "----"
        for j in hltJets:
            #print j.eta(), j.pt(), self.etaLim
            #print "XXX", j.eta()
            if abs(j.eta() ) > self.etaLim: 
                #print "   skip"
                continue
            return j.pt()
        return 0


class PTAveProperTrigger(BaseTrigger):
    def getMaxThreshold(self, topologyFullfillyingObjects = None):
        hltJets = self.objectsGetter.get()
        tag = None
        probe = None
        for j in hltJets:
            if j.pt() < 10: continue
            eta = abs(j.eta())
            if eta < 1.4: 
                if tag == None or tag.pt() < j.pt():
                    tag = j
            elif eta > 2.7:
                if probe == None or probe.pt() < j.pt():
                    probe = j

        if tag == None or probe == None:
            return 0

        pt1 = tag.pt()
        pt2 = probe.pt()
        ave = (pt1+pt2)/2.
        if pt1 < ave/2:
            ave = 2*pt1
        if pt2 < ave/2:
            ave = 2*pt2

        return ave


class PTAveMessedTrigger(BaseTrigger):
    def getMaxThreshold(self, topologyFullfillyingObjects = None):
        hltJets = self.objectsGetter.get()
        tag = None
        probe = None

        bestPTS = []
        for j in hltJets:
            if j.pt() < 10: continue
            eta = abs(j.eta())
            good = False
            if eta < 1.4: 
                good = True
                if tag == None or tag.pt() < j.pt():
                    tag = j
            elif eta > 2.7:
                good = True
                if probe == None or probe.pt() < j.pt():
                    probe = j

            if good: bestPTS.append(j.pt())

        if tag == None or probe == None:
            return 0

        bestPTS = sorted(bestPTS, reverse=True)
        ave = (bestPTS[0]+bestPTS[1])/2

        pt1 = tag.pt()
        pt2 = probe.pt()
        if pt1 < ave/2:
            ave = 2*pt1
        if pt2 < ave/2:
            ave = 2*pt2

        return ave




