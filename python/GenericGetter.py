import BaseGetter

class GenericGetter(BaseGetter.BaseGetter):
    def __init__(self, branchPrefix, srcBranch):
        BaseGetter.BaseGetter.__init__(self, branchPrefix)
        #self.knownVariations = set(["_central"])
        self.knownVariations = set()
        self.srcBranch = branchPrefix+srcBranch

    # Note: use the most used branch (so performance wont suffer from reading otherwise unused stuff)
    # fixme: -> p4
    def getSize(self):
        return getattr(self.chain, self.srcBranch).size()

