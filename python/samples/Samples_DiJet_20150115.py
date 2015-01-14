anaVersion="DiJet_20150115"
anaType="DiJet"

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

rootPath="/scratch/scratch0/tfruboes/DATA_dijet/DiJet_20150115/"
sam = {}

sam["QCD_Pt-120to170_Tune4C_13TeV_pythia8"]={}
sam["QCD_Pt-120to170_Tune4C_13TeV_pythia8"]["sgeJobs"]=80
sam["QCD_Pt-120to170_Tune4C_13TeV_pythia8"]["crabJobs"]=115
sam["QCD_Pt-120to170_Tune4C_13TeV_pythia8"]["GT"]='START42_V16::All'
sam["QCD_Pt-120to170_Tune4C_13TeV_pythia8"]["weightJet15"]='RooFormulaVar("weight","weight", "xsOverEvents*puWeightJet15V4*trgWeightJet15RawTF2*trgWeightJet15L1RawTF2", RooArgList(v["puWeightJet15V4"]["RooVar"],v["trgWeightJet15RawTF2"]["RooVar"],v["trgWeightJet15L1RawTF2"]["RooVar"]))'
sam["QCD_Pt-120to170_Tune4C_13TeV_pythia8"]["name"]='QCD_Pt-120to170_Tune4C_13TeV_pythia8'
sam["QCD_Pt-120to170_Tune4C_13TeV_pythia8"]["isData"]=False
sam["QCD_Pt-120to170_Tune4C_13TeV_pythia8"]["weightPuOnly"]='RooFormulaVar("weight","weight", "xsOverEvents*puWeightJet15V4", RooArgList(v["puWeightJet15V4"]["RooVar"]))'
sam["QCD_Pt-120to170_Tune4C_13TeV_pythia8"]["weightJet15Inverse"]='RooFormulaVar("weight","weight", "xsOverEvents*puWeightJet15V4", RooArgList(v["puWeightJet15V4"]["RooVar"]))'
sam["QCD_Pt-120to170_Tune4C_13TeV_pythia8"]["numEvents"]=-1
sam["QCD_Pt-120to170_Tune4C_13TeV_pythia8"]["lumiJet15"]='crashMeMC'
sam["QCD_Pt-120to170_Tune4C_13TeV_pythia8"]["weightNoPu"]='RooFormulaVar("weight","weight", "xsOverEvents", RooArgList())'
sam["QCD_Pt-120to170_Tune4C_13TeV_pythia8"]["json"]=''
sam["QCD_Pt-120to170_Tune4C_13TeV_pythia8"]["lumiDiJet15FB"]='crashMeMC'
sam["QCD_Pt-120to170_Tune4C_13TeV_pythia8"]["XS"]=493200.0
sam["QCD_Pt-120to170_Tune4C_13TeV_pythia8"]["DS"]='/QCD_Pt-120to170_Tune4C_13TeV_pythia8/Phys14DR-AVE20BX25_tsg_castor_PHYS14_25_V3-v1/AODSIM'

sam["QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8_Pu20"]={}
sam["QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8_Pu20"]["sgeJobs"]=80
sam["QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8_Pu20"]["crabJobs"]=115
sam["QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8_Pu20"]["GT"]='START42_V16::All'
sam["QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8_Pu20"]["weightJet15"]='RooFormulaVar("weight","weight", "generatorWeight*puWeightJet15V4*trgWeightJet15RawTF2*trgWeightJet15L1RawTF2", RooArgList(v["generatorWeight"]["RooVar"],v["puWeightJet15V4"]["RooVar"],v["trgWeightJet15RawTF2"]["RooVar"],v["trgWeightJet15L1RawTF2"]["RooVar"]))'
sam["QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8_Pu20"]["name"]='QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8_Pu20'
sam["QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8_Pu20"]["isData"]=False
sam["QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8_Pu20"]["weightPuOnly"]='RooFormulaVar("weight","weight", "generatorWeight*puWeightJet15V4", RooArgList(v["generatorWeight"]["RooVar"],v["puWeightJet15V4"]["RooVar"]))'
sam["QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8_Pu20"]["weightJet15Inverse"]='RooFormulaVar("weight","weight", "generatorWeight*puWeightJet15V4", RooArgList(v["generatorWeight"]["RooVar"],v["puWeightJet15V4"]["RooVar"]))'
sam["QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8_Pu20"]["numEvents"]=-1
sam["QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8_Pu20"]["lumiJet15"]='crashMeMC'
sam["QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8_Pu20"]["weightNoPu"]='RooFormulaVar("weight","weight", "generatorWeight", RooArgList(v["generatorWeight"]["RooVar"]))'
sam["QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8_Pu20"]["json"]=''
sam["QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8_Pu20"]["lumiDiJet15FB"]='crashMeMC'
sam["QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8_Pu20"]["pathTrees"]='/XXXTMFTTree/store/user/fruboes/QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8/DiJet_20150115_QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8_Pu20/5c7941628ba67de41f5435176de9d0bf//'
sam["QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8_Pu20"]["XS"]=2429000000
sam["QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8_Pu20"]["pathPAT"]='/XXXTMFPAT/store/user/fruboes/QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8/DiJet_20150115_QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8_Pu20/5c7941628ba67de41f5435176de9d0bf//'
sam["QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8_Pu20"]["pathSE"]='srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=/pnfs/desy.de/cms/tier2/store/user/fruboes/QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8/DiJet_20150115_QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8_Pu20/5c7941628ba67de41f5435176de9d0bf/'
sam["QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8_Pu20"]["DS"]='/QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8/Phys14DR-PU20bx25_trkalmb_PHYS14_25_V1-v1/AODSIM'

sam["QCD_Pt-15to30_Tune4C_13TeV_pythia8"]={}
sam["QCD_Pt-15to30_Tune4C_13TeV_pythia8"]["sgeJobs"]=80
sam["QCD_Pt-15to30_Tune4C_13TeV_pythia8"]["crabJobs"]=115
sam["QCD_Pt-15to30_Tune4C_13TeV_pythia8"]["GT"]='START42_V16::All'
sam["QCD_Pt-15to30_Tune4C_13TeV_pythia8"]["weightJet15"]='RooFormulaVar("weight","weight", "xsOverEvents*puWeightJet15V4*trgWeightJet15RawTF2*trgWeightJet15L1RawTF2", RooArgList(v["puWeightJet15V4"]["RooVar"],v["trgWeightJet15RawTF2"]["RooVar"],v["trgWeightJet15L1RawTF2"]["RooVar"]))'
sam["QCD_Pt-15to30_Tune4C_13TeV_pythia8"]["name"]='QCD_Pt-15to30_Tune4C_13TeV_pythia8'
sam["QCD_Pt-15to30_Tune4C_13TeV_pythia8"]["isData"]=False
sam["QCD_Pt-15to30_Tune4C_13TeV_pythia8"]["weightPuOnly"]='RooFormulaVar("weight","weight", "xsOverEvents*puWeightJet15V4", RooArgList(v["puWeightJet15V4"]["RooVar"]))'
sam["QCD_Pt-15to30_Tune4C_13TeV_pythia8"]["weightJet15Inverse"]='RooFormulaVar("weight","weight", "xsOverEvents*puWeightJet15V4", RooArgList(v["puWeightJet15V4"]["RooVar"]))'
sam["QCD_Pt-15to30_Tune4C_13TeV_pythia8"]["numEvents"]=-1
sam["QCD_Pt-15to30_Tune4C_13TeV_pythia8"]["lumiJet15"]='crashMeMC'
sam["QCD_Pt-15to30_Tune4C_13TeV_pythia8"]["weightNoPu"]='RooFormulaVar("weight","weight", "xsOverEvents", RooArgList())'
sam["QCD_Pt-15to30_Tune4C_13TeV_pythia8"]["json"]=''
sam["QCD_Pt-15to30_Tune4C_13TeV_pythia8"]["lumiDiJet15FB"]='crashMeMC'
sam["QCD_Pt-15to30_Tune4C_13TeV_pythia8"]["XS"]=2237000000.0
sam["QCD_Pt-15to30_Tune4C_13TeV_pythia8"]["DS"]='/QCD_Pt-15to30_Tune4C_13TeV_pythia8/Phys14DR-AVE20BX25_tsg_castor_PHYS14_25_V3-v2/AODSIM'

sam["QCD_Pt-30to50_Tune4C_13TeV_pythia8"]={}
sam["QCD_Pt-30to50_Tune4C_13TeV_pythia8"]["sgeJobs"]=80
sam["QCD_Pt-30to50_Tune4C_13TeV_pythia8"]["crabJobs"]=115
sam["QCD_Pt-30to50_Tune4C_13TeV_pythia8"]["GT"]='START42_V16::All'
sam["QCD_Pt-30to50_Tune4C_13TeV_pythia8"]["weightJet15"]='RooFormulaVar("weight","weight", "xsOverEvents*puWeightJet15V4*trgWeightJet15RawTF2*trgWeightJet15L1RawTF2", RooArgList(v["puWeightJet15V4"]["RooVar"],v["trgWeightJet15RawTF2"]["RooVar"],v["trgWeightJet15L1RawTF2"]["RooVar"]))'
sam["QCD_Pt-30to50_Tune4C_13TeV_pythia8"]["name"]='QCD_Pt-30to50_Tune4C_13TeV_pythia8'
sam["QCD_Pt-30to50_Tune4C_13TeV_pythia8"]["isData"]=False
sam["QCD_Pt-30to50_Tune4C_13TeV_pythia8"]["weightPuOnly"]='RooFormulaVar("weight","weight", "xsOverEvents*puWeightJet15V4", RooArgList(v["puWeightJet15V4"]["RooVar"]))'
sam["QCD_Pt-30to50_Tune4C_13TeV_pythia8"]["weightJet15Inverse"]='RooFormulaVar("weight","weight", "xsOverEvents*puWeightJet15V4", RooArgList(v["puWeightJet15V4"]["RooVar"]))'
sam["QCD_Pt-30to50_Tune4C_13TeV_pythia8"]["numEvents"]=-1
sam["QCD_Pt-30to50_Tune4C_13TeV_pythia8"]["lumiJet15"]='crashMeMC'
sam["QCD_Pt-30to50_Tune4C_13TeV_pythia8"]["weightNoPu"]='RooFormulaVar("weight","weight", "xsOverEvents", RooArgList())'
sam["QCD_Pt-30to50_Tune4C_13TeV_pythia8"]["json"]=''
sam["QCD_Pt-30to50_Tune4C_13TeV_pythia8"]["lumiDiJet15FB"]='crashMeMC'
sam["QCD_Pt-30to50_Tune4C_13TeV_pythia8"]["XS"]=161500000.0
sam["QCD_Pt-30to50_Tune4C_13TeV_pythia8"]["DS"]='/QCD_Pt-30to50_Tune4C_13TeV_pythia8/Phys14DR-AVE20BX25_tsg_castor_PHYS14_25_V3-v2/AODSIM'

sam["QCD_Pt-50to80_Tune4C_13TeV_pythia8"]={}
sam["QCD_Pt-50to80_Tune4C_13TeV_pythia8"]["sgeJobs"]=80
sam["QCD_Pt-50to80_Tune4C_13TeV_pythia8"]["crabJobs"]=115
sam["QCD_Pt-50to80_Tune4C_13TeV_pythia8"]["GT"]='START42_V16::All'
sam["QCD_Pt-50to80_Tune4C_13TeV_pythia8"]["weightJet15"]='RooFormulaVar("weight","weight", "xsOverEvents*puWeightJet15V4*trgWeightJet15RawTF2*trgWeightJet15L1RawTF2", RooArgList(v["puWeightJet15V4"]["RooVar"],v["trgWeightJet15RawTF2"]["RooVar"],v["trgWeightJet15L1RawTF2"]["RooVar"]))'
sam["QCD_Pt-50to80_Tune4C_13TeV_pythia8"]["name"]='QCD_Pt-50to80_Tune4C_13TeV_pythia8'
sam["QCD_Pt-50to80_Tune4C_13TeV_pythia8"]["isData"]=False
sam["QCD_Pt-50to80_Tune4C_13TeV_pythia8"]["weightPuOnly"]='RooFormulaVar("weight","weight", "xsOverEvents*puWeightJet15V4", RooArgList(v["puWeightJet15V4"]["RooVar"]))'
sam["QCD_Pt-50to80_Tune4C_13TeV_pythia8"]["weightJet15Inverse"]='RooFormulaVar("weight","weight", "xsOverEvents*puWeightJet15V4", RooArgList(v["puWeightJet15V4"]["RooVar"]))'
sam["QCD_Pt-50to80_Tune4C_13TeV_pythia8"]["numEvents"]=-1
sam["QCD_Pt-50to80_Tune4C_13TeV_pythia8"]["lumiJet15"]='crashMeMC'
sam["QCD_Pt-50to80_Tune4C_13TeV_pythia8"]["weightNoPu"]='RooFormulaVar("weight","weight", "xsOverEvents", RooArgList())'
sam["QCD_Pt-50to80_Tune4C_13TeV_pythia8"]["json"]=''
sam["QCD_Pt-50to80_Tune4C_13TeV_pythia8"]["lumiDiJet15FB"]='crashMeMC'
sam["QCD_Pt-50to80_Tune4C_13TeV_pythia8"]["XS"]=22110000.0
sam["QCD_Pt-50to80_Tune4C_13TeV_pythia8"]["DS"]='/QCD_Pt-50to80_Tune4C_13TeV_pythia8/Phys14DR-AVE20BX25_tsg_castor_PHYS14_25_V3-v1/AODSIM'

sam["QCD_Pt-80to120_Tune4C_13TeV_pythia8"]={}
sam["QCD_Pt-80to120_Tune4C_13TeV_pythia8"]["sgeJobs"]=80
sam["QCD_Pt-80to120_Tune4C_13TeV_pythia8"]["crabJobs"]=115
sam["QCD_Pt-80to120_Tune4C_13TeV_pythia8"]["GT"]='START42_V16::All'
sam["QCD_Pt-80to120_Tune4C_13TeV_pythia8"]["weightJet15"]='RooFormulaVar("weight","weight", "xsOverEvents*puWeightJet15V4*trgWeightJet15RawTF2*trgWeightJet15L1RawTF2", RooArgList(v["puWeightJet15V4"]["RooVar"],v["trgWeightJet15RawTF2"]["RooVar"],v["trgWeightJet15L1RawTF2"]["RooVar"]))'
sam["QCD_Pt-80to120_Tune4C_13TeV_pythia8"]["name"]='QCD_Pt-80to120_Tune4C_13TeV_pythia8'
sam["QCD_Pt-80to120_Tune4C_13TeV_pythia8"]["isData"]=False
sam["QCD_Pt-80to120_Tune4C_13TeV_pythia8"]["weightPuOnly"]='RooFormulaVar("weight","weight", "xsOverEvents*puWeightJet15V4", RooArgList(v["puWeightJet15V4"]["RooVar"]))'
sam["QCD_Pt-80to120_Tune4C_13TeV_pythia8"]["weightJet15Inverse"]='RooFormulaVar("weight","weight", "xsOverEvents*puWeightJet15V4", RooArgList(v["puWeightJet15V4"]["RooVar"]))'
sam["QCD_Pt-80to120_Tune4C_13TeV_pythia8"]["numEvents"]=-1
sam["QCD_Pt-80to120_Tune4C_13TeV_pythia8"]["lumiJet15"]='crashMeMC'
sam["QCD_Pt-80to120_Tune4C_13TeV_pythia8"]["weightNoPu"]='RooFormulaVar("weight","weight", "xsOverEvents", RooArgList())'
sam["QCD_Pt-80to120_Tune4C_13TeV_pythia8"]["json"]=''
sam["QCD_Pt-80to120_Tune4C_13TeV_pythia8"]["lumiDiJet15FB"]='crashMeMC'
sam["QCD_Pt-80to120_Tune4C_13TeV_pythia8"]["XS"]=3000114.3
sam["QCD_Pt-80to120_Tune4C_13TeV_pythia8"]["DS"]='/QCD_Pt-80to120_Tune4C_13TeV_pythia8/Phys14DR-AVE20BX25_tsg_castor_PHYS14_25_V3-v1/AODSIM'

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
def fixLocalPaths(sam):
        import os,imp
        if "SmallXAnaDefFile" not in os.environ:
            print "Please set SmallXAnaDefFile environment variable:"
            print "export SmallXAnaDefFile=FullPathToFile"
            raise Exception("Whooops! SmallXAnaDefFile env var not defined")

        anaDefFile = os.environ["SmallXAnaDefFile"]
        mod_dir, filename = os.path.split(anaDefFile)
        mod, ext = os.path.splitext(filename)
        f, filename, desc = imp.find_module(mod, [mod_dir])
        mod = imp.load_module(mod, f, filename, desc)

        localBasePathPAT = mod.PATbasePATH
        localBasePathTrees = mod.TTreeBasePATH

        for s in sam:
            if "pathPAT" in sam[s]:
                sam[s]["pathPAT"] = sam[s]["pathPAT"].replace("XXXTMFPAT", localBasePathPAT)
            if "pathTrees" in sam[s]:
                sam[s]["pathTrees"] = sam[s]["pathTrees"].replace("XXXTMFTTree", localBasePathTrees)
            #print sam[s]["pathPAT"]
            #print sam[s]["pathTrees"]
        return sam
sam = fixLocalPaths(sam)
