import ROOT
ROOT.gROOT.SetBatch(True)

class Entry:
    def __init__(self, chain, branchPrefix, variation, branchStore, index):
        self.chain = chain
        self.branchPrefix = branchPrefix
        self.variation = variation
        self.index = index
        self.branchStore = branchStore
        self.cache = {}

    # TODO: add "_" as a separator
    def __getattr__(self, name):
        if name in self.cache:
            return self.cache[name]

        branchName = self.branchPrefix + name + self.variation
        # we could do following, instead of using self.variationToNames:
        #if not hasattr(self.chain, branchName): # what is cost of this call??
        #    branchName = self.branchPrefix + name 
        # this seems to be more expensive
        if branchName  not in self.branchStore:
            self.branchStore[branchName] = getattr(self.chain, branchName)

        #return self.branchStore[branchName].at(self.index)
        ret = self.branchStore[branchName].at(self.index)
        self.cache[name] = ret
        return ret
        #return getattr(self.chain, branchName).at(self.index)

    # FIXME: entries from two different events can be equal
    def __eq__(self, other):
        if other == None: return False
        # TODO check if types are eqeal
        if self.index != other.index: return False
        if self.branchPrefix != other.branchPrefix: return False
        if self.variation != other.variation: return False
        return True

    def __neq__(self, other):
        return not self.__eq__(other)

# Branch naming convention:
#   branchPrefix_attrName for central value
#   branchPrefix_attrName_variationName for variations
class BaseGetter:
    def __init__(self, branchPrefix):
        self.branchPrefix = branchPrefix
        self.knownVariations = set()

    def newEvent(self, chain):
        self.branchStore = {}
        self.chain = chain

    def getSize(self):
        raise Exception("Please implement getSize method in your derived getter")

    def __len__(self):
        return int(self.getSize())

    # TODO: cacheing
    def get(self, variation=""):
        if variation not in self.knownVariations:   # variation of a different kind, e.g. from PU
            variation = ""

        if variation == "_central":
            variation = ""

        index = 0
        size = self.getSize() # XXX
        while index < size:
            yield Entry(self.chain, self.branchPrefix, variation, self.branchStore, index)
            index += 1
