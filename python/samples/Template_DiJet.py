
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

from DiJetAnalysis.DiJetAna.ana.DiJetBalanceSelector import DiJetBalanceSelector
MySelector  = DiJetBalanceSelector()
from DiJetAnalysis.DiJetAna.ana.DiJetBalanceVariables import DiJetBalanceVariables
MyVariables = DiJetBalanceVariables()
MyVariables.doBalanceAnalisys()
MySelector.doBalanceAnalysis()

#MyVariables.doDiJetAnalysis()
#MySelector.doDiJetAnalysis()

#MyVariables.doMCResAnalysis()
#MySelector.doMCResAnalysis()



MyVariablesAllEvents="DiJetAnalysis.DiJetAna.ana.BaseVariables"
'''
# /scratch/scratch0/tfruboes/2013.05.DiJetNewGit/CMSSW_4_2_8_patch7/src/DiJetAnalysis/DiJetAna/python/samples
dsFile="MNTriggerStudies/MNTriggerAna/python/samples/dsBase.txt"

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
        ret = split[1] + "-" + split[2]
    else:
        ret = split[1]
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

    return 100

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
    #                                                              654130000
    s["QCD_Pt_15to30_TuneZ2star_HFshowerLibrary_7TeV_pythia6"]   = 8.1591283E8
    #                                                              42464000
    s["QCD_Pt_30to50_TuneZ2star_HFshowerLibrary_7TeV_pythia6"]   = 53122368.0
    #                                                               5113600
    s["QCD_Pt_50to80_TuneZ2star_HFshowerLibrary_7TeV_pythia6"]   =  6359119.0
    #                                                                636160
    s["QCD_Pt_80to120_TuneZ2star_HFshowerLibrary_7TeV_pythia6"]  =   784265.2
    #                                                                 93495
    s["QCD_Pt_120to170_TuneZ2star_HFshowerLibrary_7TeV_pythia6"] =   115133.5
    s["QCD_Pt_170to300_TuneZ2star_HFshowerLibrary_7TeV_pythia6"] =    24262.83
    s["QCD_Pt_300to470_TuneZ2star_HFshowerLibrary_7TeV_pythia6"] =     1168.494


    # it looks, like the fwd xs from prep page allready include filter efficiency
    factor = 1e9    
    s["QCD_Pt_10to25_fwdJet_TuneZ2star_HFshowerLibrary_7TeV_pythia6"] =  3.651* factor *  0.06727
    s["QCD_Pt_25to40_fwdJet_TuneZ2star_HFshowerLibrary_7TeV_pythia6"] =  0.1059* factor *   0.27707
    s["QCD_Pt_40to80_fwdJet_TuneZ2star_HFshowerLibrary_7TeV_pythia6"] =  0.01771* factor *   0.25234
    s["QCD_Pt_80to150_fwdJet_TuneZ2star_HFshowerLibrary_7TeV_pythia6"] =  8.756E-4*factor *   0.19052
    s["QCD_Pt_150toInf_fwdJet_TuneZ2star_HFshowerLibrary_7TeV_pythia6"] =  4.76E-5*factor *   0.14464


    #'''
    #                                                           654 130 000
    s["QCD_Pt-15to30_Tune23_HFshowerLibrary_7TeV_herwigpp"] = 1.25100006E9

    #                                                        42 464 000
    s["QCD_Pt-30to50_Tune23_HFshowerLibrary_7TeV_herwigpp"] = 8.31E7
    
    #                                                         5113600
    s["QCD_Pt-50to80_Tune23_HFshowerLibrary_7TeV_herwigpp"] = 1.001E7
    #                                                           636160  
    s["QCD_Pt-80to120_Tune23_HFshowerLibrary_7TeV_herwigpp"] = 1221000.0

    #
    # 179200.0/36040.0=4.972253052164262 # best cand pair
    #                                                            93495   
    s["QCD_Pt-120to170_Tune23_HFshowerLibrary_7TeV_herwigpp"] = 179200.0

    s["QCD_Pt-170to300_Tune23_HFshowerLibrary_7TeV_herwigpp"] =  36040.0

    s["QCD_Pt-300to470_Tune23_HFshowerLibrary_7TeV_herwigpp"] =  1702.0


    # https://twiki.cern.ch/twiki/bin/view/CMS/ProductionSummer2011#HERWIG
    # weighted samples, so the pt spectrum is flat

    # 0.0430588744076 * herwigXS = 9.5E8
    s["QCD_Pt-15to3000_Tune23_Flat_HFshowerLibrary_7TeV_herwigpp"] =    2.21268193E10
    # '''
    s["QCD_Pt-15to3000_TuneZ2star_Flat_HFshowerLibrary_7TeV_pythia6"] = 2.213E10 



    # xs from Tom - https://twiki.cern.ch/twiki/bin/viewauth/CMS/FSQxsec
    '''
    s["QCD_Pt-15to3000_Tune23_Flat_HFshowerLibrary_7TeV_herwigpp"] = 2.3841e+10 # err 1.15937e+8
    s["QCD_Pt-15to30_Tune23_HFshowerLibrary_7TeV_herwigpp"] = 8.41666e+8 # err 4.03076e+6
    s["QCD_Pt-30to50_Tune23_HFshowerLibrary_7TeV_herwigpp"] = 5.57944e+7 # err 3.0054e+5
    s["QCD_Pt-50to80_Tune23_HFshowerLibrary_7TeV_herwigpp"] = 6.83871e+6 # err 2.7796e+4
    s["QCD_Pt-80to120_Tune23_HFshowerLibrary_7TeV_herwigpp"] = 8.67734e+5 # err 3.60005e+3
    s["QCD_Pt-120to170_Tune23_HFshowerLibrary_7TeV_herwigpp"] = 1.29717e+5 # err 5.41466e+2
    s["QCD_Pt-170to300_Tune23_HFshowerLibrary_7TeV_herwigpp"] = 2.84432e+4 # err 1.58357e+2
    s["QCD_Pt-300to470_Tune23_HFshowerLibrary_7TeV_herwigpp"] = 1.40208e+3 # err 7.93158
    s["QCD_Pt-470to600_Tune23_HFshowerLibrary_7TeV_herwigpp"] = 87.1996 # err 0.523422
    s["QCD_Pt-600to800_Tune23_HFshowerLibrary_7TeV_herwigpp"] = 19.9533 # err 0.115348 
    '''






    '''
    todo = { "pythia6" : s["DiJet_20131008_QCD_Pt-15to3000_TuneZ2star_Flat_HFshowerLibrary_7TeV_pythia6"],
             "herwigpp": s["DiJet_20131008_QCD_Pt-15to3000_Tune23_Flat_HFshowerLibrary_7TeV_herwigpp"]
           }
    for t in todo:
        sum = 0.
        for sam in s:
            if not t in sam: continue
            if "15to3000" in sam: continue
            sum += s[sam]
        print t, sum/todo[t]
    '''

    dsName = name(ds)
    if dsName in s:
        return s[dsName]
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




