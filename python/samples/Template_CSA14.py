anaType="Tracks"

# root path needs proper XXX
preamble='''
cbSmartCommand="smartCopy"
cbSmartBlackList=""
cbWMS="https://wmscms.cern.ch:7443/glite_wms_wmproxy_server"
skimEfficiencyMethod="getSkimEff"
MyVariablesAllEvents="DiJetAnalysis.DiJetAna.ana.BaseVariables"
'''

dsFile="MNTriggerStudies/MNTriggerAna/python/samples/ds_csa14.txt"

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
    if "MinBias_TuneA2MB_13TeV_pythia8" in ds:         # XXX CSA14 TODO - when we have our datasets
        realData = True
    return realData

def json(ds):
    realData = isData(ds)
    return ""
    if realData and "-May10ReReco-" in ds:
        return "DiJetAnalysis/DiJetAna/lumi/Cert_160404-163869_7TeV_May10ReReco_Collisions11_JSON_v3.txt"
    if realData and "2011" in ds:
        return "DiJetAnalysis/DiJetAna/lumi//Cert_160404-180252_7TeV_PromptReco_Collisions11_JSON.txt"
    if realData:
        return "DiJetAnalysis/DiJetAna/lumi/Cert_136033-149442_7TeV_Apr21ReReco_Collisions10_JSON_v2.txt"
    else:
        return ""

def crabJobs(ds):
    dsName = name(ds)
    if "QCD_Pt-15to3000" in dsName and "_V17B-v2" in ds:
        return 1950 

    return 470

def numEvents(ds):
    return -1

def sgeJobs(ds):
    if "QCD" in ds:
        return 80
    else:
        return 50
    return 120

def GT(ds):
    realData = isData(ds)
    if realData:
        return "POSTLS170_V6::All"
    else:
        return "POSTLS170_V6::All"

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

    realData = isData(ds)
    if realData:
        return -1


    # Give all XS in pb
    s = {}
    s["MinBias_TuneZ2star_13TeV_pythia6"] = 78E9


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
    if not realData:
        return "crashMeMC" # booby trap the attribute in order to protect any feet from beeing shoot 

    s = {}
    s.setdefault("minbias", {})


    dsName = name(ds)
    if dsName in s[trg]:
        return s[trg][dsName]

    print "Problem with lumi!", ds
    return "crashMe"

def lumiMinBias(ds):
    return getLumi(ds,"minbias")


@util
def getWeight(variablesList):
    ''' 
    Accepts list of variables. Each variable may come with a power different of 1 (e.g. trgWeightJet15TF2^-1)
    Special variable names:
        xsOverEvents   
    ''' 
    formula = ""
    formulaSeparator = ""
    variables = ""
    variablesSeparator = ""
    for var in variablesList:
        spl = var.split("^")
        v = spl[0]
        if "xsOverEvents" != v:
            variables = variables + variablesSeparator+'v["'+v+'"]["RooVar"]'
            variablesSeparator = ","
        formula = formula + formulaSeparator + var
        formulaSeparator = "*"


    ret = 'RooFormulaVar("weight","weight", "'+formula+'", RooArgList('+variables+'))'
    return ret        

@util 
def weightBase(ds, variables):
    realData = isData(ds)
    if realData:
        return None
    dsName = name(ds)
    if "15to3000" in dsName:
        dsSpecyficVars = ["generatorWeight",]
    else:
        dsSpecyficVars = ["xsOverEvents",]


    return getWeight(dsSpecyficVars+variables)

def weightNoPu(ds):
    return weightBase(ds, [])

def weightPuOnly(ds):
    return weightBase(ds, ["puWeightJet15V4"])


def weightJet15(ds):
    return weightBase(ds, ["puWeightJet15V4","trgWeightJet15RawTF2", "trgWeightJet15L1RawTF2"])

def weightJet15Inverse(ds):
    realData = isData(ds)
    if realData:
        return getWeight(["invtrgWeightJet15RawTF2"])
    else:
        return weightBase(ds, ["puWeightJet15V4"])

#def weightDJet15FB(ds):
#    return weightBase(ds, ["puWeightJet15V4","trgWeightDJet15FBTF2"])


'''
def weightPUJet15V4(ds):
    return weightBase(ds, ["puWeightJet15V4"])

def weightPUJet15NT3(ds):
    return weightBase(ds, ["puWeightJet15NT3"])

def weightPUJet15NT4(ds):
    return weightBase(ds, ["puWeightJet15NT4"])
'''

@util
def onTheFlyCustomization():
    ret = '''
def icm(sam):
    import socket
    import os
    host = socket.gethostname()
    if ".icm." not in host:
       return sam
    root = "/mnt/lustre/permanent/plgtfruboes/data/"
    thisAna = root + anaVersion + "/"
    for s in sam:
        pathList = set()
        for r,d,f in os.walk(thisAna):
            for files in f:
                if files.endswith(".root"):
                     if s in r:
                        pathList.add( r )
        if len(pathList) != 1:
            print "Problem with paths:", s, pathList
        else:
            sam[s]["path"] = pathList.pop() + "/"
            sam[s]["sgeJobs"] = 80

    return sam
sam = icm(sam)
'''
    return ret
#setattr(onTheFlyCustomization, "ignore", 1)

@util
def rootPath(dateTT):
    import socket
    host = socket.gethostname()
    isICM = False
    if ".icm." in host:
        isICM = True

    if isICM == True:
        ret = "/mnt/lustre/permanent/plgtfruboes/data/" + anaType + "_" + dateTT + "/"
    else:
        ret = "/scratch/scratch0/tfruboes/DATA_dijet/" + anaType + "_" + dateTT + "/"

    return ret


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




