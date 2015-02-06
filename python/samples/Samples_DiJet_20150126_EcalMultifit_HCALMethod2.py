anaVersion="DiJet_20150126_EcalMultifit_HCALMethod2"
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

rootPath="/scratch/scratch0/tfruboes/DATA_dijet/DiJet_20150126_EcalMultifit_HCALMethod2/"
sam = {}

sam["QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8_Pu0to10"]={}
sam["QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8_Pu0to10"]["sgeJobs"]=80
sam["QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8_Pu0to10"]["crabJobs"]=115
sam["QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8_Pu0to10"]["GT"]='START42_V16::All'
sam["QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8_Pu0to10"]["weightJet15"]='RooFormulaVar("weight","weight", "generatorWeight*puWeightJet15V4*trgWeightJet15RawTF2*trgWeightJet15L1RawTF2", RooArgList(v["generatorWeight"]["RooVar"],v["puWeightJet15V4"]["RooVar"],v["trgWeightJet15RawTF2"]["RooVar"],v["trgWeightJet15L1RawTF2"]["RooVar"]))'
sam["QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8_Pu0to10"]["name"]='QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8_Pu0to10'
sam["QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8_Pu0to10"]["isData"]=False
sam["QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8_Pu0to10"]["weightPuOnly"]='RooFormulaVar("weight","weight", "generatorWeight*puWeightJet15V4", RooArgList(v["generatorWeight"]["RooVar"],v["puWeightJet15V4"]["RooVar"]))'
sam["QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8_Pu0to10"]["weightJet15Inverse"]='RooFormulaVar("weight","weight", "generatorWeight*puWeightJet15V4", RooArgList(v["generatorWeight"]["RooVar"],v["puWeightJet15V4"]["RooVar"]))'
sam["QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8_Pu0to10"]["numEvents"]=-1
sam["QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8_Pu0to10"]["lumiJet15"]='crashMeMC'
sam["QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8_Pu0to10"]["weightNoPu"]='RooFormulaVar("weight","weight", "generatorWeight", RooArgList(v["generatorWeight"]["RooVar"]))'
sam["QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8_Pu0to10"]["json"]=''
sam["QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8_Pu0to10"]["lumiDiJet15FB"]='crashMeMC'
sam["QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8_Pu0to10"]["pathTrees"]='/XXXTMFTTree/store/user/fruboes/QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8/DiJet_20150126_EcalMultifit_HCALMethod2_QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8_Pu0to10/94b4c1145c04bffab8664e819643ea38//'
sam["QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8_Pu0to10"]["XS"]=2429000000
sam["QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8_Pu0to10"]["pathPAT"]='/XXXTMFPAT/store/user/fruboes/QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8/DiJet_20150126_EcalMultifit_HCALMethod2_QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8_Pu0to10/94b4c1145c04bffab8664e819643ea38//'
sam["QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8_Pu0to10"]["pathSE"]='srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=/pnfs/desy.de/cms/tier2/store/user/fruboes/QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8/DiJet_20150126_EcalMultifit_HCALMethod2_QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8_Pu0to10/94b4c1145c04bffab8664e819643ea38/'
sam["QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8_Pu0to10"]["DS"]='/QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8/fruboes-20150126_QCD_EcalMultifit_HCALMethod2_PU0to10-3e9c823de397371c7bd3a3d91198303d/USER'

sam["QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8_Pu20to50"]={}
sam["QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8_Pu20to50"]["sgeJobs"]=80
sam["QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8_Pu20to50"]["crabJobs"]=115
sam["QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8_Pu20to50"]["GT"]='START42_V16::All'
sam["QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8_Pu20to50"]["weightJet15"]='RooFormulaVar("weight","weight", "generatorWeight*puWeightJet15V4*trgWeightJet15RawTF2*trgWeightJet15L1RawTF2", RooArgList(v["generatorWeight"]["RooVar"],v["puWeightJet15V4"]["RooVar"],v["trgWeightJet15RawTF2"]["RooVar"],v["trgWeightJet15L1RawTF2"]["RooVar"]))'
sam["QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8_Pu20to50"]["name"]='QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8_Pu20to50'
sam["QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8_Pu20to50"]["isData"]=False
sam["QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8_Pu20to50"]["weightPuOnly"]='RooFormulaVar("weight","weight", "generatorWeight*puWeightJet15V4", RooArgList(v["generatorWeight"]["RooVar"],v["puWeightJet15V4"]["RooVar"]))'
sam["QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8_Pu20to50"]["weightJet15Inverse"]='RooFormulaVar("weight","weight", "generatorWeight*puWeightJet15V4", RooArgList(v["generatorWeight"]["RooVar"],v["puWeightJet15V4"]["RooVar"]))'
sam["QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8_Pu20to50"]["numEvents"]=-1
sam["QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8_Pu20to50"]["lumiJet15"]='crashMeMC'
sam["QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8_Pu20to50"]["weightNoPu"]='RooFormulaVar("weight","weight", "generatorWeight", RooArgList(v["generatorWeight"]["RooVar"]))'
sam["QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8_Pu20to50"]["json"]=''
sam["QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8_Pu20to50"]["lumiDiJet15FB"]='crashMeMC'
sam["QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8_Pu20to50"]["pathTrees"]='/XXXTMFTTree/store/user/fruboes/QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8/DiJet_20150126_EcalMultifit_HCALMethod2_QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8_Pu20to50/94b4c1145c04bffab8664e819643ea38//'
sam["QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8_Pu20to50"]["XS"]=2429000000
sam["QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8_Pu20to50"]["pathPAT"]='/XXXTMFPAT/store/user/fruboes/QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8/DiJet_20150126_EcalMultifit_HCALMethod2_QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8_Pu20to50/94b4c1145c04bffab8664e819643ea38//'
sam["QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8_Pu20to50"]["pathSE"]='srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=/pnfs/desy.de/cms/tier2/store/user/fruboes/QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8/DiJet_20150126_EcalMultifit_HCALMethod2_QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8_Pu20to50/94b4c1145c04bffab8664e819643ea38/'
sam["QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8_Pu20to50"]["DS"]='/QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8/fruboes-20150126_QCD_EcalMultifit_HCALMethod2_PU20to50-3e9c823de397371c7bd3a3d91198303d/USER'

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
