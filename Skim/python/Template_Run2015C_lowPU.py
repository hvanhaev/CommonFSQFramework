anaType="Run2015C_lowPU"

# root path needs proper XXX
# some stuff needed for crab configuration, e.g. blacklisting
preamble='''
cbSmartCommand="smartCopy"
cbSmartBlackList=""
cbWMS="https://wmscms.cern.ch:7443/glite_wms_wmproxy_server"
skimEfficiencyMethod="getSkimEff"
'''

# point towards your list of samples you want
dsFile="CommonFSQFramework/Skim/python/ds_Run2015C_lowPU_v1.txt"

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
    if "Run2015" in ds: realData = True
    return realData

def json(ds):
    realData = isData(ds)
    if realData:
        if "Run2015C" in ds: return "CommonFSQFramework/Skim/lumi/Run2015C_lowPU.json"
    else:
        return ""

def crabJobs(ds):
    dsName = name(ds)
    # define to run 100 crab jobs
    # make something more clever, based on number of events in the dataset:
    # require around 50000 events to be processed per job
    return int(round(numEvents(ds)/100000.0))


def numEvents(ds):
    
    # 3.8T MC
    if "MinBias_TuneMonash13_13TeV-pythia8" in name(ds): return 997552
    if "ReggeGribovPartonMC_13TeV-EPOS" in name(ds): return 998312
    if "ReggeGribovPartonMC_13TeV-QGSJetII" in name(ds): return 1000000
    if "MinBias_TuneZ2star_13TeV-pythia6" in name(ds): return 998098
    if "MinBias_TuneCUETP8M1_13TeV-pythia8" in name(ds): return 999330
    if "MinBias_TuneMBR_13TeV-pythia8" in name(ds): return 998920
    if "MinBias_TuneEE5C_13TeV-herwigpp" in name(ds): return 1000000 
    
    # data
    
    # if nothing found...
    return -1

def GT(ds):
    if isData(ds) and "Run2015C-v1_LowPU_RERECO_74X_dataRun2_Prompt_v2_withCustomCond-v1" in ds: return "74X_dataRun2_Prompt_v2" 
    if isData(ds) and "Run2015C-PromptReco-v1" in ds: return "74X_dataRun2_Prompt_v1"
	
    # 3.8T MC GT
    if "NoPU_castor_MCRUN2_74_V8" in ds: return "MCRUN2_74_V8" 
    if "NoPURawReco_castor_MCRUN2_74_V8B" in ds: return "MCRUN2_74_V8B"
    
    return "MCRUN2_74_V8B"
    
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
    s["MinBias_TuneMonash13_13TeV-pythia8"] = 78418400000.0 # from DAS - McM
    s["ReggeGribovPartonMC_13TeV-EPOS"] = 78418400000.0
    s["ReggeGribovPartonMC_13TeV-QGSJetII"] = 78418400000.0
    s["MinBias_TuneZ2star_13TeV-pythia6"] = 78260000000.0
    s["MinBias_TuneCUETP8M1_13TeV-pythia8"] = 78418400000.0
    s["MinBias_TuneMBR_13TeV-pythia8"] = 78418400000.0
    s["MinBias_TuneEE5C_13TeV-herwigpp"] = 36460000000.0


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




