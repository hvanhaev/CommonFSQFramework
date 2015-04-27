anaType="RunIIWinter15GS"

# root path needs proper XXX
# some stuff needed for crab configuration, e.g. blacklisting
preamble='''
cbSmartCommand="smartCopy"
cbSmartBlackList=""
cbWMS="https://wmscms.cern.ch:7443/glite_wms_wmproxy_server"
skimEfficiencyMethod="getSkimEff"
'''

# point towards your list of samples you want
dsFile="CommonFSQFramework/Skim/python/ds_RunIIWinter15GS.txt"

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
    # make something more clever, based on number of events in the dataset:
    # require around 50000 events to be processed per job
    return int(round(numEvents(ds)/50000.0)) 
    #return 100

def numEvents(ds):
    evts = -1
    
    # list all datasets in ds_RunIIWinterGS.txt file, get events from DAS
    if "MinBias_TuneMonash13_13TeV-pythia8" in ds: evts = 998368
    if "MinBias_TuneCUETP8S1-HERAPDF_13TeV-pythia8" in ds: evts = 9765120
    if "ReggeGribovPartonMC_13TeV-EPOS" in ds: evts = 998312
    if "ReggeGribovPartonMC_13TeV-QGSJetII" in ds: evts = 1000000
    if "MinBias_TuneZ2star_13TeV-pythia6" in ds: evts = 998098
    if "MinBias_TuneCUETP8M1_13TeV-pythia8" in ds: evts = 999330
    if "MinBias_TuneMBR_13TeV-pythia8" in ds: evts = 998920
    if "MinBias_TuneEE5C_13TeV-herwigpp" in ds: evts = 1000000
    if "MinBias_TuneMBR_epsilon080-pythia8" in ds: evts = 998380
    
    if "QCD_Pt-15to3000_castorJet_TuneCUETP8M1_Flat_13TeV-pythia8" in ds: evts = 4941690
    if "ReggeGribovPartonMC_castorJet_13TeV-EPOS" in ds: evts = 4974768
    if "ReggeGribovPartonMC_castorJet_13TeV-QGSJetII" in ds: evts = 5703036
    
    if "MinBias_chgMult110_TuneCUETP8M1_13TeV-pythia8" in ds: evts = 1152226
    if "MinBias_chgMult60_TuneCUETP8M1_13TeV-pythia8" in ds: evts = 772686
    
    return evts

def GT(ds):
    # no data, just get GT from GEN-SIM samples
    if "MinBias_chgMult" in ds: return "MCRUN2_71_V1::All"
    if "TuneCUETP8S1-HERAPDF" in ds: return "MCRUN2_71_V1::All"
    
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
    s["MinBias_TuneCUETP8S1-HERAPDF_13TeV-pythia8"] = 78418400000.0
    s["ReggeGribovPartonMC_13TeV-EPOS"] = 78418400000.0
    s["ReggeGribovPartonMC_13TeV-QGSJetII"] = 78418400000.0
    s["MinBias_TuneZ2star_13TeV-pythia6"] = 78260000000.0
    s["MinBias_TuneCUETP8M1_13TeV-pythia8"] = 78418400000.0
    s["MinBias_TuneMBR_13TeV-pythia8"] = 78418400000.0
    s["MinBias_TuneEE5C_13TeV-herwigpp"] = 36460000000.0
    s["MinBias_TuneMBR_epsilon080-pythia8"] = 75930000000.0
    
    s["QCD_Pt-15to3000_castorJet_TuneCUETP8M1_Flat_13TeV-pythia8"] = 986200000.0
    s["ReggeGribovPartonMC_castorJet_13TeV-EPOS"] = 1.0 # XS not known
    s["ReggeGribovPartonMC_castorJet_13TeV-QGSJetII"] = 1.0 # XS not known
    
    s["MinBias_chgMult110_TuneCUETP8M1_13TeV-pythia8"] = 28590000.0
    s["MinBias_chgMult60_TuneCUETP8M1_13TeV-pythia8"] = 28590000.0


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
    
    # just do something very simple for now
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




