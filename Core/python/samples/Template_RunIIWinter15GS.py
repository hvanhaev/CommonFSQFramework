anaType="RunIIWinter15GS"

# root path needs proper XXX
# could be useful in the future, ignore this for the moment
preamble='''

'''

# point towards your list of samples you want
dsFile="./ds_RunIIWinter15GS.txt"

# define the util decorator. Functions marked with this wont turn into ds attribute
def util(func):
    setattr(func, "ignore", 1)
    return func
setattr(util, "ignore", 1) # for this function only


def DS(ds):
    return ds

def name(ds):
    split=ds.split("/") 
    if len(split) == 0: return None

    if isData(ds):
        ret = "data_"+split[1]
    else:
        ret = split[1]
    return ret

def isData(ds):
    realData = False
    if "Run201" in ds: realData = True
    return realData

def json(ds):
    realData = isData(ds)
    # they are just MC GEN-SIM samples, no json needed here
    return ""

def crabJobs(ds):
    dsName = name(ds)
    # define to run 100 crab jobs
    # make something more clever, based on number of events in the dataset
    return 100

def numEvents(ds):
    evts = -1
    # list all datasets in ds_RunIIWinterGS.txt file
    if "MinBias_TuneMonash13_13TeV-pythia8" in ds: evts = 998368 # from DAS
    
    return evts

def GT(ds):
    # no data, just get GT from GEN-SIM samples
    return "MCRUN2_71_V0::All"

def XS(ds):
    '''
    Note: all cross sections given in pb
    # http://iopscience.iop.org/0295-5075/96/2/21002
    LHCtotal= 73.5 mili b

    conversion factors cheatsheet:
    nano = 10^-6 mili
    nano = 10^-3 micro
    nano = 10^3 pico
    '''
    # if real data return nothing, not needed here but keep for other Templates
    realData = isData(ds)
    if realData:
        return -1

    # list all datasets in ds_RunIIWinter15GS.txt
    # Give all XS in pb
    s = {}
    s["MinBias_TuneMonash13_13TeV-pythia8"] = 78418400000.0 # from DAS - McM


    dsName = name(ds)
    if dsName in s:
        return s[dsName]
    else:
        print "FIXME - XS missing for", dsName
        print '    s["'+dsName+'"] = '
    return -1

@util
def getLumi(ds, trg):
    '''
    all lumi values here should be given in picob
    '''

    s = {}
    s.setdefault("minbias", {})

    # add all MC and data samples - for data get from json file in future?
    s["minbias"]["MinBias_TuneMonash13_13TeV-pythia8"] = numEvents(ds)/XS(ds) # pb, Nevents/XS

    dsName = name(ds)
    if dsName in s[trg]:
        return float(s[trg][dsName])

    print "Problem with lumi!", ds
    return "crashMe"

def lumiMinBias(ds):
    return getLumi(ds,"minbias")


# could useful in the future
@util
def onTheFlyCustomization():
    ret = ""

    return ret
#setattr(onTheFlyCustomization, "ignore", 1)


fun = {}
import copy,types
glob = copy.copy(globals())
for f in glob:
    if type(glob[f])==types.FunctionType:
        if hasattr(glob[f],"ignore"): 
            print "Skip", f
            continue
        #print f
        fun[f]=glob[f]




