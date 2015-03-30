import BaseGetter

class GenTracksGetter(BaseGetter.BaseGetter):
    def __init__(self, branchPrefix):
        BaseGetter.BaseGetter.__init__(self, branchPrefix)
        #self.knownVariations = set(["_central"])
        self.knownVariations = set()

    # Note: use the most used branch (so performance wont suffer from reading otherwise unused stuff)
    # fixme: -> p4
    def getSize(self):
        srcBranch = "genTracksgenTracks"
        return getattr(self.chain, srcBranch).size()

