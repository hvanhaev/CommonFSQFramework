anaVersion="DiJet_20141023_TestsWith720"
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

rootPath="/scratch/scratch0/tfruboes/DATA_dijet/DiJet_20141023_TestsWith720/"
sam = {}

sam["Neutrino_Pt-2to20_gun"]={}
sam["Neutrino_Pt-2to20_gun"]["sgeJobs"]=50
sam["Neutrino_Pt-2to20_gun"]["crabJobs"]=470
sam["Neutrino_Pt-2to20_gun"]["GT"]='START42_V16::All'
sam["Neutrino_Pt-2to20_gun"]["weightJet15"]='RooFormulaVar("weight","weight", "xsOverEvents*puWeightJet15V4*trgWeightJet15RawTF2*trgWeightJet15L1RawTF2", RooArgList(v["puWeightJet15V4"]["RooVar"],v["trgWeightJet15RawTF2"]["RooVar"],v["trgWeightJet15L1RawTF2"]["RooVar"]))'
sam["Neutrino_Pt-2to20_gun"]["name"]='Neutrino_Pt-2to20_gun'
sam["Neutrino_Pt-2to20_gun"]["isData"]=False
sam["Neutrino_Pt-2to20_gun"]["weightPuOnly"]='RooFormulaVar("weight","weight", "xsOverEvents*puWeightJet15V4", RooArgList(v["puWeightJet15V4"]["RooVar"]))'
sam["Neutrino_Pt-2to20_gun"]["weightJet15Inverse"]='RooFormulaVar("weight","weight", "xsOverEvents*puWeightJet15V4", RooArgList(v["puWeightJet15V4"]["RooVar"]))'
sam["Neutrino_Pt-2to20_gun"]["numEvents"]=-1
sam["Neutrino_Pt-2to20_gun"]["lumiJet15"]='crashMeMC'
sam["Neutrino_Pt-2to20_gun"]["weightNoPu"]='RooFormulaVar("weight","weight", "xsOverEvents", RooArgList())'
sam["Neutrino_Pt-2to20_gun"]["json"]=''
sam["Neutrino_Pt-2to20_gun"]["lumiDiJet15FB"]='crashMeMC'
sam["Neutrino_Pt-2to20_gun"]["pathTrees"]='/XXXTMFTTree/store/user/fruboes/Neutrino_Pt-2to20_gun/DiJet_20141023_TestsWith720_Neutrino_Pt-2to20_gun/24c70f05f87aea9b65006d5382f94b91//'
sam["Neutrino_Pt-2to20_gun"]["XS"]=-1
sam["Neutrino_Pt-2to20_gun"]["pathPAT"]='/XXXTMFPAT/store/user/fruboes/Neutrino_Pt-2to20_gun/DiJet_20141023_TestsWith720_Neutrino_Pt-2to20_gun/24c70f05f87aea9b65006d5382f94b91//'
sam["Neutrino_Pt-2to20_gun"]["pathSE"]='srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=/pnfs/desy.de/cms/tier2/store/user/fruboes/Neutrino_Pt-2to20_gun/DiJet_20141023_TestsWith720_Neutrino_Pt-2to20_gun/24c70f05f87aea9b65006d5382f94b91/'
sam["Neutrino_Pt-2to20_gun"]["DS"]='/Neutrino_Pt-2to20_gun/fruboes-20141023_NuGun_HLTJetsPu20to50_720-5bf11c64ebfcb1bed227f4f3ad2897d4/USER'

sam["Neutrino_Pt-2to20_gun_162"]={}
sam["Neutrino_Pt-2to20_gun_162"]["sgeJobs"]=50
sam["Neutrino_Pt-2to20_gun_162"]["crabJobs"]=470
sam["Neutrino_Pt-2to20_gun_162"]["GT"]='START42_V16::All'
sam["Neutrino_Pt-2to20_gun_162"]["weightJet15"]='RooFormulaVar("weight","weight", "xsOverEvents*puWeightJet15V4*trgWeightJet15RawTF2*trgWeightJet15L1RawTF2", RooArgList(v["puWeightJet15V4"]["RooVar"],v["trgWeightJet15RawTF2"]["RooVar"],v["trgWeightJet15L1RawTF2"]["RooVar"]))'
sam["Neutrino_Pt-2to20_gun_162"]["name"]='Neutrino_Pt-2to20_gun_162'
sam["Neutrino_Pt-2to20_gun_162"]["isData"]=False
sam["Neutrino_Pt-2to20_gun_162"]["weightPuOnly"]='RooFormulaVar("weight","weight", "xsOverEvents*puWeightJet15V4", RooArgList(v["puWeightJet15V4"]["RooVar"]))'
sam["Neutrino_Pt-2to20_gun_162"]["weightJet15Inverse"]='RooFormulaVar("weight","weight", "xsOverEvents*puWeightJet15V4", RooArgList(v["puWeightJet15V4"]["RooVar"]))'
sam["Neutrino_Pt-2to20_gun_162"]["numEvents"]=-1
sam["Neutrino_Pt-2to20_gun_162"]["lumiJet15"]='crashMeMC'
sam["Neutrino_Pt-2to20_gun_162"]["weightNoPu"]='RooFormulaVar("weight","weight", "xsOverEvents", RooArgList())'
sam["Neutrino_Pt-2to20_gun_162"]["json"]=''
sam["Neutrino_Pt-2to20_gun_162"]["lumiDiJet15FB"]='crashMeMC'
sam["Neutrino_Pt-2to20_gun_162"]["pathTrees"]='/XXXTMFTTree/store/user/fruboes/Neutrino_Pt-2to20_gun/DiJet_20141023_TestsWith720_Neutrino_Pt-2to20_gun_162/11c9466dca5563ccdc2a957343bf780e//'
sam["Neutrino_Pt-2to20_gun_162"]["XS"]=-1
sam["Neutrino_Pt-2to20_gun_162"]["pathPAT"]='/XXXTMFPAT/store/user/fruboes/Neutrino_Pt-2to20_gun/DiJet_20141023_TestsWith720_Neutrino_Pt-2to20_gun_162/11c9466dca5563ccdc2a957343bf780e//'
sam["Neutrino_Pt-2to20_gun_162"]["pathSE"]='srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=/pnfs/desy.de/cms/tier2/store/user/fruboes/Neutrino_Pt-2to20_gun/DiJet_20141023_TestsWith720_Neutrino_Pt-2to20_gun_162/11c9466dca5563ccdc2a957343bf780e/'
sam["Neutrino_Pt-2to20_gun_162"]["DS"]='/Neutrino_Pt-2to20_gun/fruboes-20141023_NuGun162_HLTJetsPu20_720-2f37f2cc398b18482efdc56e9384d725/USER'

sam["QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8"]={}
sam["QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8"]["sgeJobs"]=80
sam["QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8"]["crabJobs"]=470
sam["QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8"]["GT"]='START42_V16::All'
sam["QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8"]["weightJet15"]='RooFormulaVar("weight","weight", "generatorWeight*puWeightJet15V4*trgWeightJet15RawTF2*trgWeightJet15L1RawTF2", RooArgList(v["generatorWeight"]["RooVar"],v["puWeightJet15V4"]["RooVar"],v["trgWeightJet15RawTF2"]["RooVar"],v["trgWeightJet15L1RawTF2"]["RooVar"]))'
sam["QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8"]["name"]='QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8'
sam["QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8"]["isData"]=False
sam["QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8"]["weightPuOnly"]='RooFormulaVar("weight","weight", "generatorWeight*puWeightJet15V4", RooArgList(v["generatorWeight"]["RooVar"],v["puWeightJet15V4"]["RooVar"]))'
sam["QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8"]["weightJet15Inverse"]='RooFormulaVar("weight","weight", "generatorWeight*puWeightJet15V4", RooArgList(v["generatorWeight"]["RooVar"],v["puWeightJet15V4"]["RooVar"]))'
sam["QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8"]["numEvents"]=-1
sam["QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8"]["lumiJet15"]='crashMeMC'
sam["QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8"]["weightNoPu"]='RooFormulaVar("weight","weight", "generatorWeight", RooArgList(v["generatorWeight"]["RooVar"]))'
sam["QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8"]["json"]=''
sam["QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8"]["lumiDiJet15FB"]='crashMeMC'
sam["QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8"]["pathTrees"]='/XXXTMFTTree/store/user/fruboes/QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8/DiJet_20141023_TestsWith720_QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8/2be424a467ac5b96839a52cf83a9993f//'
sam["QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8"]["XS"]=2429000000
sam["QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8"]["pathPAT"]='/XXXTMFPAT/store/user/fruboes/QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8/DiJet_20141023_TestsWith720_QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8/2be424a467ac5b96839a52cf83a9993f//'
sam["QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8"]["pathSE"]='srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=/pnfs/desy.de/cms/tier2/store/user/fruboes/QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8/DiJet_20141023_TestsWith720_QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8/2be424a467ac5b96839a52cf83a9993f/'
sam["QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8"]["DS"]='/QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8/fruboes-20141023_QCDnewHFJecTRG_HLTJetsPu20to50_720-3a89b834271012cd860a1a9609fca634/USER'

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
