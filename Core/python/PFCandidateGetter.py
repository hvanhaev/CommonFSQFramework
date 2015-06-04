import BaseGetter

class PFCandidateGetter(BaseGetter.BaseGetter):
    def __init__(self, branchPrefix):
        BaseGetter.BaseGetter.__init__(self, branchPrefix)
        #self.knownVariations = set(["_central"])
        self.knownVariations = set()

    # Note: use the most used branch (so performance wont suffer from reading otherwise unused stuff)
    def getSize(self):
        srcBranch = "PFCandidatesp4"
        return getattr(self.chain, srcBranch).size()

