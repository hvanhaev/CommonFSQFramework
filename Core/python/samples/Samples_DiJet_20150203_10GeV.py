anaVersion="DiJet_20150203_10GeV"
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

rootPath="/scratch/scratch0/tfruboes/DATA_dijet/DiJet_20150203_10GeV/"
sam = {}

sam["MinBias_TuneZ2star_13TeV_pythia6_162"]={}
sam["MinBias_TuneZ2star_13TeV_pythia6_162"]["sgeJobs"]=50
sam["MinBias_TuneZ2star_13TeV_pythia6_162"]["crabJobs"]=115
sam["MinBias_TuneZ2star_13TeV_pythia6_162"]["GT"]='START42_V16::All'
sam["MinBias_TuneZ2star_13TeV_pythia6_162"]["weightJet15"]='RooFormulaVar("weight","weight", "xsOverEvents*puWeightJet15V4*trgWeightJet15RawTF2*trgWeightJet15L1RawTF2", RooArgList(v["puWeightJet15V4"]["RooVar"],v["trgWeightJet15RawTF2"]["RooVar"],v["trgWeightJet15L1RawTF2"]["RooVar"]))'
sam["MinBias_TuneZ2star_13TeV_pythia6_162"]["name"]='MinBias_TuneZ2star_13TeV_pythia6_162'
sam["MinBias_TuneZ2star_13TeV_pythia6_162"]["isData"]=False
sam["MinBias_TuneZ2star_13TeV_pythia6_162"]["weightPuOnly"]='RooFormulaVar("weight","weight", "xsOverEvents*puWeightJet15V4", RooArgList(v["puWeightJet15V4"]["RooVar"]))'
sam["MinBias_TuneZ2star_13TeV_pythia6_162"]["weightJet15Inverse"]='RooFormulaVar("weight","weight", "xsOverEvents*puWeightJet15V4", RooArgList(v["puWeightJet15V4"]["RooVar"]))'
sam["MinBias_TuneZ2star_13TeV_pythia6_162"]["numEvents"]=-1
sam["MinBias_TuneZ2star_13TeV_pythia6_162"]["lumiJet15"]='crashMeMC'
sam["MinBias_TuneZ2star_13TeV_pythia6_162"]["weightNoPu"]='RooFormulaVar("weight","weight", "xsOverEvents", RooArgList())'
sam["MinBias_TuneZ2star_13TeV_pythia6_162"]["json"]=''
sam["MinBias_TuneZ2star_13TeV_pythia6_162"]["lumiDiJet15FB"]='crashMeMC'
sam["MinBias_TuneZ2star_13TeV_pythia6_162"]["pathTrees"]='/XXXTMFTTree/store/user/fruboes/MinBias_TuneZ2star_13TeV_pythia6/DiJet_20150203_10GeV_MinBias_TuneZ2star_13TeV_pythia6_162/45e0016f15b7348448bde8b05416c51b//'
sam["MinBias_TuneZ2star_13TeV_pythia6_162"]["XS"]=78260000000.0
sam["MinBias_TuneZ2star_13TeV_pythia6_162"]["pathPAT"]='/XXXTMFPAT/store/user/fruboes/MinBias_TuneZ2star_13TeV_pythia6/DiJet_20150203_10GeV_MinBias_TuneZ2star_13TeV_pythia6_162/45e0016f15b7348448bde8b05416c51b//'
sam["MinBias_TuneZ2star_13TeV_pythia6_162"]["pathSE"]='srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=/pnfs/desy.de/cms/tier2/store/user/fruboes/MinBias_TuneZ2star_13TeV_pythia6/DiJet_20150203_10GeV_MinBias_TuneZ2star_13TeV_pythia6_162/45e0016f15b7348448bde8b05416c51b/'
sam["MinBias_TuneZ2star_13TeV_pythia6_162"]["DS"]='/MinBias_TuneZ2star_13TeV_pythia6/Fall13dr-castor_tsg_NoPileUp_POSTLS162_V1-v1/AODSIM'

sam["Neutrino_Pt-2to20_gun_162"]={}
sam["Neutrino_Pt-2to20_gun_162"]["sgeJobs"]=50
sam["Neutrino_Pt-2to20_gun_162"]["crabJobs"]=115
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
sam["Neutrino_Pt-2to20_gun_162"]["pathTrees"]='/XXXTMFTTree/store/user/fruboes/Neutrino_Pt-2to20_gun/DiJet_20150203_10GeV_Neutrino_Pt-2to20_gun_162/feaf54fd36602aa86215a16579297695//'
sam["Neutrino_Pt-2to20_gun_162"]["XS"]=-1
sam["Neutrino_Pt-2to20_gun_162"]["pathPAT"]='/XXXTMFPAT/store/user/fruboes/Neutrino_Pt-2to20_gun/DiJet_20150203_10GeV_Neutrino_Pt-2to20_gun_162/feaf54fd36602aa86215a16579297695//'
sam["Neutrino_Pt-2to20_gun_162"]["pathSE"]='srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=/pnfs/desy.de/cms/tier2/store/user/fruboes/Neutrino_Pt-2to20_gun/DiJet_20150203_10GeV_Neutrino_Pt-2to20_gun_162/feaf54fd36602aa86215a16579297695/'
sam["Neutrino_Pt-2to20_gun_162"]["DS"]='/Neutrino_Pt-2to20_gun/Fall13dr-castor_tsg_PU1bx50_POSTLS162_V1-v1/AODSIM'

sam["QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8"]={}
sam["QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8"]["sgeJobs"]=80
sam["QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8"]["crabJobs"]=115
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
sam["QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8"]["pathTrees"]='/XXXTMFTTree/store/user/fruboes/QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8/DiJet_20150203_10GeV_QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8/5ee30148d4552bbfe93c4bc8536e79ea//'
sam["QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8"]["XS"]=2429000000
sam["QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8"]["pathPAT"]='/XXXTMFPAT/store/user/fruboes/QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8/DiJet_20150203_10GeV_QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8/5ee30148d4552bbfe93c4bc8536e79ea//'
sam["QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8"]["pathSE"]='srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=/pnfs/desy.de/cms/tier2/store/user/fruboes/QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8/DiJet_20150203_10GeV_QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8/5ee30148d4552bbfe93c4bc8536e79ea/'
sam["QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8"]["DS"]='/QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8/Spring14dr-Flat0to10_POSTLS170_V5-v1/AODSIM'

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
