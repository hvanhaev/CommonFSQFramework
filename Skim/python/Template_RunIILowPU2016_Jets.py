anaType="RunIILowPU2016_Jets"

# root path needs proper XXX
# some stuff needed for crab configuration, e.g. blacklisting
preamble='''
cbSmartCommand="smartCopy"
cbSmartBlackList=""
cbWMS="https://wmscms.cern.ch:7443/glite_wms_wmproxy_server"
skimEfficiencyMethod="getSkimEff"
'''

# point towards your list of samples you want
dsFile="CommonFSQFramework/Skim/python/ds_RunIILowPU2016_Jets_v1.txt"

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

    if "noPU" in ds: return split[1]+"_noPU"    
    if not isData(ds): return split[1]

    if isData(ds): return "data_"+split[1]

def isData(ds):
    realData = False
    if "Run2016" in ds: realData = True
    return realData

def json(ds):
    realData = isData(ds)
    if realData:
        return "CommonFSQFramework/Skim/lumi/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON_LowLowPU.txt"
    else:
        return ""

def crabJobs(ds):
    dsName = name(ds)
    # define to run 100 crab jobs
    # make something more clever, based on number of events in the dataset:
    # require around 50000 events to be processed per job
    return int(round(numEvents(ds)/100000.0))


def numEvents(ds):
    
    # 76X MC samples
    if "/QCD_Pt-10to35_TuneCUETHS1_13TeV-herwigpp/RunIIFall15MiniAODv2-PU25nsData2015v1_castor_76X_mcRun2_asymptotic_v12-v1" in ds: return 963800
    if "/QCD_Pt-10to35_TuneCUETHS1_13TeV-herwigpp/RunIIFall15MiniAODv2-noPU_castor_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM" in ds: return 997904
    if "/QCD_Pt-35toInf_TuneCUETHS1_13TeV-herwigpp/RunIIFall15MiniAODv2-noPU_castor_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM" in ds: return 997364
    
    # data
    
    # if nothing found...
    return -1

def GT(ds):
    if isData(ds) and "03Feb2017" in ds: return "80X_dataRun2_2016SeptRepro_v7"
    if isData(ds) and "PromptReco" in ds: return "80X_dataRun2_Prompt_v16"
	
    # if not data, return MC tag
    # 76X MC samples - use 80X GTs for now
    return "80X_mcRun2_asymptotic_2016_TrancheIV_v8"
    
def XS(ds):
    '''
    Note: all cross sections given in pb
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
    s["QCD_Pt-10to35_TuneCUETHS1_13TeV-herwigpp"] = 7272000000.0 # from McM
    s["QCD_Pt-10to35_TuneCUETHS1_13TeV-herwigpp_noPU"] = 7272000000.0
    s["QCD_Pt-35toInf_TuneCUETHS1_13TeV-herwigpp_noPU"] = 78170000.0

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




