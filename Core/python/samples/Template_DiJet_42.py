
anaType="DiJet"

# root path needs proper XXX
preamble='''
cbSmartCommand="smartCopy"
cbSmartBlackList=""
#cbWMS="https://wms-cms-analysis.grid.cnaf.infn.it:7443/glite_wms_wmproxy_server"
cbWMS="https://wmscms.cern.ch:7443/glite_wms_wmproxy_server"
#diObjectType="vector<CompositePtrCandidateT1T2MEt<pat::Muon,pat::Tau> >"
#skimEfficiencyMethod="getSkimEffFromME"
skimEfficiencyMethod="getSkimEff"

#from DiJetAnalysis.DiJetAna.ana.DiJetBalanceSelector import DiJetBalanceSelector
#MySelector  = DiJetBalanceSelector()
#from DiJetAnalysis.DiJetAna.ana.DiJetBalanceVariables import DiJetBalanceVariables
#MyVariables = DiJetBalanceVariables()
#MyVariables.doBalanceAnalisys()
#MySelector.doBalanceAnalysis()

#MyVariables.doDiJetAnalysis()
#MySelector.doDiJetAnalysis()

#MyVariables.doMCResAnalysis()
#MySelector.doMCResAnalysis()



MyVariablesAllEvents="DiJetAnalysis.DiJetAna.ana.BaseVariables"
'''
# /scratch/scratch0/tfruboes/2013.05.DiJetNewGit/CMSSW_4_2_8_patch7/src/DiJetAnalysis/DiJetAna/python/samples
dsFile="MNTriggerStudies/MNTriggerAna/python/samples/ds2010_42.txt"

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
        #ret = split[1] + "-" + split[2]+"-V16TFPartV2"
        ret = split[1] + "-" + split[2]
    else:
        #ret = split[1]+"-V16TFPartV2"
        ret = split[1]
    return ret

def isData(ds):
    realData = False
    if "Run201" in ds:
        realData = True
    return realData

def json(ds):
    realData = isData(ds)
    '''
    if realData and "-May10ReReco-" in ds:
        return "DiJetAnalysis/DiJetAna/lumi/Cert_160404-163869_7TeV_May10ReReco_Collisions11_JSON_v3.txt"
    if realData and "2011" in ds:
        return "DiJetAnalysis/DiJetAna/lumi//Cert_160404-180252_7TeV_PromptReco_Collisions11_JSON.txt"
    '''
    if realData:
        return "MNTriggerStudies/MNTriggerAna/lumi/Cert_136033-149442_7TeV_Apr21ReReco_Collisions10_JSON_v2.txt"
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
        return "GR_R_42_V19::All"
    else:
        return "START42_V16::All"

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

    s = {}

    s["QCD_Pt-15to3000_TuneZ2star_Flat_HFshowerLibrary_7TeV_pythia6"] = 2.213E10
    s["QCD_Pt-15to1000_TuneEE3C_Flat_7TeV_herwigpp"] = 16953200000.  # 30% difference wrt pythia. Note different pt Range!




    dsName = name(ds)
    if dsName in s:
        return s[dsName]
    else:
        print "FIXME - XS missing for", dsName
        print '    s["'+dsName+'"] = '
    return -1

# not needed?
'''
def num(ds):
    realData = isData(ds)
    if realData:
        return -1

    s = {}
    s["QCD_Pt_15to30_TuneZ2star_HFshowerLibrary_7TeV_pythia6"] = 3000000
    s["QCD_Pt_30to50_TuneZ2star_HFshowerLibrary_7TeV_pythia6"] = 5000000
    s["QCD_Pt_50to80_TuneZ2star_HFshowerLibrary_7TeV_pythia6"] = 5000000
    s["QCD_Pt_80to120_TuneZ2star_HFshowerLibrary_7TeV_pythia6"] = 5000000
    s["QCD_Pt_120to170_TuneZ2star_HFshowerLibrary_7TeV_pythia6"] = 4000000
    dsName = name(ds)
    if dsName in s:
        return s[dsName]
    return -1
'''
@util
def getLumi(ds, trg):
    '''
    all lumi values here should be given in picob
    '''
    realData = isData(ds)
    if not realData:
        return "crashMeMC" # booby trap the attribute in order to protect any feet from beeing shoot 

    s = {}
    s.setdefault("j15", {})
    s.setdefault("dj15fb", {})
    s["j15"]["Jet-Run2010B-Apr21ReReco-v1"] =  3.347/1000.
    s["j15"]["JetMET-Run2010A-Apr21ReReco-v1"] = 9.525/1000.
    s["j15"]["JetMETTau-Run2010A-Apr21ReReco-v1"] = 13.781/1000. 
    s["j15"]["METFwd-Run2010B-Apr21ReReco-v1"] = "crashMe" # shouldnt be used with that trigger

    s["dj15fb"]["Jet-Run2010B-Apr21ReReco-v1"] =  "crashMe" # shouldnt be used with that trigger
    s["dj15fb"]["JetMET-Run2010A-Apr21ReReco-v1"] =  2.838
    s["dj15fb"]["JetMETTau-Run2010A-Apr21ReReco-v1"] = 282.774/1000.
    s["dj15fb"]["METFwd-Run2010B-Apr21ReReco-v1"] = 1.763 + 477.319/1000.


    dsName = name(ds)
    if dsName in s[trg]:
        return s[trg][dsName]

    print "Problem with lumi!", ds
    return "crashMe"

def lumiJet15(ds):
    return getLumi(ds,"j15")
def lumiDiJet15FB(ds):
    return getLumi(ds,"dj15fb")


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




