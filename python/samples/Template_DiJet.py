
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
#dsFile="MNTriggerStudies/MNTriggerAna/python/samples/dsBase.txt"
#dsFile="MNTriggerStudies/MNTriggerAna/python/samples/ds70TriggerStudies.txt"
#dsFile="MNTriggerStudies/MNTriggerAna/python/samples/ds72TriggerStudies.txt"
#dsFile="MNTriggerStudies/MNTriggerAna/python/samples/ds73dijethltstudies.txt"
#dsFile="MNTriggerStudies/MNTriggerAna/python/samples/dsFwdQCD70PU20.txt"
dsFile="MNTriggerStudies/MNTriggerAna/python/samples/dsHLT1Step.txt"

# define the util decorator. Functions marked with this wont turn into ds attribute
def util(func):
    setattr(func, "ignore", 1)
    return func
setattr(util, "ignore", 1) # for this function only


def DS(ds):
    return ds

def name(ds, noPostfix = False):
    split=ds.split("/") 
    if len(split) == 0: return None

    # /Neutrino_Pt-2to20_gun/fruboes-20141023_NuGun162_HLTJetsPu20_720-2f37f2cc398b18482efdc56e9384d725/USER
    postfix = ""
    if "5GeV" in ds:
        postfix += "_5GeV"
    elif "10GeV" in ds:
        postfix += "_10GeV"

    if "pu0to10" in ds.lower():
        postfix += "_Pu0to10"
    elif "pu20to50" in ds.lower():
        postfix += "_Pu20to50"
    elif "pu20" in ds.lower() or "AVE20BX25" in ds.lower():
        postfix += "_Pu20"
    elif "pu40" in ds.lower():
        postfix += "_Pu40"

    if "162" in ds:
        postfix+= "_162"

    if noPostfix:
        postfix=""

    if isData(ds):
        ret = split[1] + "-" + split[2]
    else:
        ret = split[1]+postfix
    return ret

def isData(ds):
    realData = False
    if "Run201" in ds:
        realData = True
    return realData

def json(ds):
    realData = isData(ds)
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

    return 330
    return 115

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
    s["Neutrino_Pt-2to20_gun"] = -1
    s["Neutrino_Pt-2to20_gun_162"] = -1
    s["QCD_Pt_15to30_TuneZ2star_HFshowerLibrary_7TeV_pythia6"]   = 8.1591283E8


    s["QCD_Pt-15to30_Tune4C_13TeV_pythia8"] = 2237000000.0 # https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get/BTV-Fall13-00041
    s["QCD_Pt-30to50_Tune4C_13TeV_pythia8"] = 161500000.0 # https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get/BTV-Fall13-00042
    s["QCD_Pt-50to80_Tune4C_13TeV_pythia8"] = 22110000.0 # https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get/BTV-Fall13-00043
    # Note: multiple entries  avaliable. Will use last entry:
    # Date: 2013-10-30-17-35 3116000.0 1.0 1.0
    # Date: 2014-05-07-15-30 3000114.3 1.0 1.0
    s["QCD_Pt-80to120_Tune4C_13TeV_pythia8"] = 3000114.3 # https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get/BTV-Fall13-00044
    # Note: multiple entries  avaliable. Will use last entry:
    # Date: 2013-10-30-17-35 486200.0 1.0 1.0
    # Date: 2014-05-07-15-28 493200.0 1.0 1.0
    s["QCD_Pt-120to170_Tune4C_13TeV_pythia8"] = 493200.0 # https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get/BTV-Fall13-00045
    # Note: multiple entries  avaliable. Will use last entry:
    # Date: 2013-10-30-17-35 12030.0 1.0 1.0
    # Date: 2014-05-07-14-47 120300.0 1.0 1.0
    s["QCD_Pt-170to300_Tune4C_13TeV_pythia8"] = 120300.0 # https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get/BTV-Fall13-00046
    s["QCD_Pt-300to470_Tune4C_13TeV_pythia8"] = 7475.0 # https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get/BTV-Fall13-00047
    s["QCD_Pt-470to600_Tune4C_13TeV_pythia8"] = 587.1 # https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get/BTV-Fall13-00048
    s["QCD_Pt-600to800_Tune4C_13TeV_pythia8"] = 167.0 # https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get/BTV-Fall13-00049
    s["QCD_Pt-800to1000_Tune4C_13TeV_pythia8"] = 28.25 # https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get/BTV-Fall13-00050
    s["QCD_Pt-1000to1400_Tune4C_13TeV_pythia8"] = 8.195 # https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get/BTV-Fall13-00051
    s["QCD_Pt-1400to1800_Tune4C_13TeV_pythia8"] = 0.7346 # https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get/BTV-Fall13-00052
    s["QCD_Pt-1800_Tune4C_13TeV_pythia8"] = 0.1091
    s["QCD_Pt-5to10_Tune4C_13TeV_pythia8"] = 80710000000.0 # https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get/FSQ-Fall13-00001
    s["QCD_Pt-10to15_Tune4C_13TeV_pythia8"] = 7528000000.0 # https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get/FSQ-Fall13-00002

    s["MinBias_TuneA2MB_13TeV_pythia8"] = 78420000000.0 # https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get/FSQ-Fall13-00015
    s["EWKWplus_mqq120_mnl50_13TeV_madgraph-pythia8"] = 14.246 # https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get/FSQ-Fall13-00016
    s["EWKWmin_mqq120_mnl50_13TeV_madgraph-pythia8"] = 9.4569 # https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get/FSQ-Fall13-00017
    s["GammaGammaToMuMu_Elastic_Pt3_13TeV_lpair"] = 1.0 # https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get/FSQ-Fall13-00018
    s["GammaGammaToTauTau_Elastic_Pt3_13TeV_lpair"] = 1.0 # https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get/FSQ-Fall13-00019
    s["EWKZjj_mqq120_mll50_13TeV_madgraph-pythia8"] = 1.949 # https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get/FSQ-Fall13-00020
    s["CEPGammaGamma_Pt2p5_13TeV_SuperCHIC"] = 1.0 # https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get/FSQ-Fall13-00021
    s["Upsilon1SToMuMu_13TeV_starlight"] = 1.0 # https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get/FSQ-Fall13-00022
    s["MinBias_TuneZ2star_13TeV_pythia6"] = 78260000000.0 # https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get/FSQ-Fall13-00023
    # Note: multiple entries  avaliable. Will use last entry:
    # Date: 2014-03-06-17-47 1785.0 1.0 1.0
    # Date: 2014-05-07-13-50 1592.0 1.0 1.0
    s["DYToMuMu_M-50_Tune4C_13TeV-pythia8"] = 1592.0 # https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get/FSQ-Fall13-00024
    # Note: multiple entries  avaliable. Will use last entry:
    # Date: 2014-03-06-17-55 1728.0 1.0 1.0
    # Date: 2014-05-07-13-53 1604.0 1.0 1.0
    s["DYToEE_M-50_Tune4C_13TeV-pythia8"] = 1604.0 # https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get/FSQ-Fall13-00025

    s["QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8"] = 2429000000 # https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get/JME-Fall13-00001
    s["QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8_Pu20"] = 2429000000

    s["QCD_Pt-10to15_fwdJet_Tune4C_13TeV_pythia8"] = 564600000.0 # filt=0.075 https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get/FSQ-Fall13-00003
    s["QCD_Pt-15to30_fwdJet_Tune4C_13TeV_pythia8"] = 550302000.0 # filt=0.246 https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get/FSQ-Fall13-00004
    s["QCD_Pt-30to50_fwdJet_Tune4C_13TeV_pythia8"] = 65892000.0 # filt=0.408 https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get/FSQ-Fall13-00005
    s["QCD_Pt-50to80_fwdJet_Tune4C_13TeV_pythia8"] = 8932440.0 # filt=0.404 https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get/FSQ-Fall13-00006
    s["QCD_Pt-80to120_fwdJet_Tune4C_13TeV_pythia8"] = 1146688.0 # filt=0.368 https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get/FSQ-Fall13-00007
    s["QCD_Pt-120to170_fwdJet_Tune4C_13TeV_pythia8"] = 166766.6 # filt=0.343 https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get/FSQ-Fall13-00008
    s["QCD_Pt-170toInf_fwdJet_Tune4C_13TeV_pythia8"] = 43444.8 # filt=0.336 https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get/FSQ-Fall13-00009


    dsName = name(ds)
    dsNameNoPF = name(ds, True)
    print "XXX", dsNameNoPF
    if dsNameNoPF in s:
        return s[dsNameNoPF]
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




