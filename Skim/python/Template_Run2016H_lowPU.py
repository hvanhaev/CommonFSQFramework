anaType="Run2016H_jets_lowPU"

# root path needs proper XXX
# some stuff needed for crab configuration, e.g. blacklisting
preamble='''
cbSmartCommand="smartCopy"
cbSmartBlackList=""
cbWMS="https://wmscms.cern.ch:7443/glite_wms_wmproxy_server"
skimEfficiencyMethod="getSkimEff"
'''

# point towards your list of samples you want
dsFile="CommonFSQFramework/Skim/python/ds_Run2016H.txt"

# define the util decorator. Functions marked with this wont turn into ds attribute
def util(func):
    setattr(func, "ignore", 1)
    return func
setattr(util, "ignore", 1) # for this function only


def DS(ds):
    return ds

def name(ds):
    split=ds.split("/")
    #if isData(ds):
	#	split=ds.split("-") 
    #elif not isData:
	#	split=ds.split("/")
    if len(split) == 0: return None

    
    if not isData(ds): return split[1]

    if isData(ds): return "data_"+split[1]

def isData(ds):
    realData = False
    if "Run2016" in ds: realData = True
    return realData

def json(ds):
    realData = isData(ds)
    if realData:
        if "Run2016" in ds: return "CommonFSQFramework/Skim/lumi/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON_LowLowPU.json"
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
    if "FSQJets" in name(ds): return 6002822
    if "data_L1MinimumBias0" in name(ds) : return 20301400
    if "data_L1MinimumBias1" in name(ds) : return 20301026
    if "data_L1MinimumBias2" in name(ds) : return 20301419
    if "data_L1MinimumBias3" in name(ds) : return 20301121
    if "data_L1MinimumBias4" in name(ds) : return 20301412
    if "data_L1MinimumBias5" in name(ds) : return 20301253
    if "data_L1MinimumBias6" in name(ds) : return 20301163
    if "data_L1MinimumBias7" in name(ds) : return 20301586
    if "data_L1MinimumBias8" in name(ds) : return 20300955
    if "data_L1MinimumBias9" in name(ds) : return 20300939
    if "QCD_Pt-15to7000_TuneCUETHS1_FlatP6_13TeV_herwigpp" in name(ds): return 9790720
    if "QCD_Pt-15to7000_TuneCUETP8M1_FlatP6_13TeV_pythia8" in name(ds): return 9647872
    if "MinBias_TuneCUETP8M1_13TeV-pythia8" in name(ds): return 9999488
    if "QCD_Pt-15to3000_TuneCUETP8M1_Flat_13TeV_pythia8" in name(ds) : return 994573
    if "QCD_Pt-15to7000_TuneCUETP8M1_Flat_13TeV_pythia8" in name(ds) : return 9960448

    
    # data
    
    # if nothing found...
    return -1

def GT(ds):
    if isData(ds) and "FSQJets" and "Run2016H" in ds: return "80X_dataRun2_2016SeptRepro_v7"
    if isData(ds) and "L1MinimumBias" and "Run2016H" in ds: return "80X_dataRun2_2016SeptRepro_v7"
	
    if "QCD_Pt-15to7000_TuneCUETHS1_FlatP6_13TeV_herwigpp" in name(ds): return "80X_mcRun2_asymptotic_2016_TrancheIV_v8" 
    if "QCD_Pt-15to7000_TuneCUETP8M1_FlatP6_13TeV_pythia8" in ds: return "80X_mcRun2_asymptotic_2016_TrancheIV_v8" 
    if "MinBias_TuneCUETP8M1_13TeV-pythia8" in ds: return "80X_mcRun2_asymptotic_2016_TrancheIV_v8"
    if "QCD_Pt-15to3000_TuneCUETP8M1_Flat_13TeV_pythia8" in ds : return "76X_mcRun2_asymptotic_v12"
    if "QCD_Pt-15to7000_TuneCUETP8M1_Flat_13TeV_pythia8" in ds : return "76X_mcRun2_asymptotic_v12"
    
    return -1
    
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
    s["QCD_Pt-15to7000_TuneCUETHS1_FlatP6_13TeV_herwigpp"] = 1667000000.0
    s["QCD_Pt-15to7000_TuneCUETP8M1_FlatP6_13TeV_pythia8"] = 2022100000.0
    s["MinBias_TuneCUETP8M1_13TeV-pythia8"] = 78418400000.0
    s["QCD_Pt-15to3000_TuneCUETP8M1_Flat_13TeV_pythia8"] = 1900000000.0
    s["QCD_Pt-15to7000_TuneCUETP8M1_Flat_13TeV_pythia8"] = 1900000000.0

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





