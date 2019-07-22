anaType="PARun2016C_Pbp"

# root path needs proper XXX
# some stuff needed for crab configuration, e.g. blacklisting
preamble='''
cbSmartCommand="smartCopy"
cbSmartBlackList=""
cbWMS="https://wmscms.cern.ch:7443/glite_wms_wmproxy_server"
skimEfficiencyMethod="getSkimEff"
'''

# point towards your list of samples you want
dsFile="CommonFSQFramework/Skim/python/ds_PARun2016C_Pbp_v1.txt"

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

    
    if not isData(ds): return split[1]

    if isData(ds): return "data_"+split[1]

def isData(ds):
    realData = False
    if "PARun2016" in ds: realData = True
    return realData

def json(ds):
    realData = isData(ds)
    if realData:
        if "PARun2016C" in ds: return "CommonFSQFramework/Skim/lumi/HI8TeV_PromptReco_Pbp_Run_286010.txt"
    else:
        return ""

def crabJobs(ds):
    dsName = name(ds)
    # define to run 100 crab jobs
    # make something more clever, based on number of events in the dataset:
    # require around 50000 events to be processed per job
    return int(round(numEvents(ds)/100000.0))


def numEvents(ds):
    
    # Pbp MC
    if "ReggeGribovPartonMC_EposLHC_PbP_4080_4080_DataBS" in name(ds): return 29785600
    if "hvanhaev-ReggeGribovPartonMC_EposLHC_4080_4080GeV_Pbp_RECO_CastorNoiseFix" in ds: 444000
    
    # data
    
    # if nothing found...
    return -1

def GT(ds):
    if isData(ds) and "PARun2016C-PromptReco" in ds: return "80X_dataRun2_Prompt_v15"
	
    # Pbp MC GT
    if "pPb816Summer16DR" in ds: return "80X_mcRun2_pA_v4" 
    if "hvanhaev-ReggeGribovPartonMC_EposLHC_4080_4080GeV_Pbp_RECO_CastorNoiseFix" in ds: return "80X_mcRun2_pA_v4"
    
    return "80X_dataRun2_Prompt_v14"
    
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

    # list all datasets
    # Give all XS in pb
    s = {}
    s["ReggeGribovPartonMC_EposLHC_PbP_4080_4080_DataBS"] = 2069160000000.0 # 5 TeV cross section
    s["MinBias"] = 2069160000000.0 # 5 TeV cross section
    

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
    
    realData = isData(ds)
    if realData:
        return -1
    
    # for MC just do something very simple for now
    lumi = float(numEvents(ds)/XS(ds)) # pb, Nevents/XS
    return lumi

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




