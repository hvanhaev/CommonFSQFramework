anaVersion="DiJet_20140516"
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

rootPath="/scratch/scratch0/tfruboes/DATA_dijet/DiJet_20140516/"
sam = {}

sam["QCD_Pt-10to15_Tune4C_13TeV_pythia8"]={}
sam["QCD_Pt-10to15_Tune4C_13TeV_pythia8"]["sgeJobs"]=80
sam["QCD_Pt-10to15_Tune4C_13TeV_pythia8"]["crabJobs"]=470
sam["QCD_Pt-10to15_Tune4C_13TeV_pythia8"]["GT"]='START42_V16::All'
sam["QCD_Pt-10to15_Tune4C_13TeV_pythia8"]["weightJet15"]='RooFormulaVar("weight","weight", "xsOverEvents*puWeightJet15V4*trgWeightJet15RawTF2*trgWeightJet15L1RawTF2", RooArgList(v["puWeightJet15V4"]["RooVar"],v["trgWeightJet15RawTF2"]["RooVar"],v["trgWeightJet15L1RawTF2"]["RooVar"]))'
sam["QCD_Pt-10to15_Tune4C_13TeV_pythia8"]["name"]='QCD_Pt-10to15_Tune4C_13TeV_pythia8'
sam["QCD_Pt-10to15_Tune4C_13TeV_pythia8"]["isData"]=False
sam["QCD_Pt-10to15_Tune4C_13TeV_pythia8"]["weightPuOnly"]='RooFormulaVar("weight","weight", "xsOverEvents*puWeightJet15V4", RooArgList(v["puWeightJet15V4"]["RooVar"]))'
sam["QCD_Pt-10to15_Tune4C_13TeV_pythia8"]["weightJet15Inverse"]='RooFormulaVar("weight","weight", "xsOverEvents*puWeightJet15V4", RooArgList(v["puWeightJet15V4"]["RooVar"]))'
sam["QCD_Pt-10to15_Tune4C_13TeV_pythia8"]["numEvents"]=-1
sam["QCD_Pt-10to15_Tune4C_13TeV_pythia8"]["lumiJet15"]='crashMeMC'
sam["QCD_Pt-10to15_Tune4C_13TeV_pythia8"]["weightNoPu"]='RooFormulaVar("weight","weight", "xsOverEvents", RooArgList())'
sam["QCD_Pt-10to15_Tune4C_13TeV_pythia8"]["json"]=''
sam["QCD_Pt-10to15_Tune4C_13TeV_pythia8"]["lumiDiJet15FB"]='crashMeMC'
sam["QCD_Pt-10to15_Tune4C_13TeV_pythia8"]["pathTrees"]='/XXXTMFTTree/store/user/fruboes/QCD_Pt-10to15_Tune4C_13TeV_pythia8/DiJet_20140516_QCD_Pt-10to15_Tune4C_13TeV_pythia8/e69320067b8f0ba24d244d9ad12dec6d//'
sam["QCD_Pt-10to15_Tune4C_13TeV_pythia8"]["XS"]=7528000000.0
sam["QCD_Pt-10to15_Tune4C_13TeV_pythia8"]["pathPAT"]='/XXXTMFPAT/store/user/fruboes/QCD_Pt-10to15_Tune4C_13TeV_pythia8/DiJet_20140516_QCD_Pt-10to15_Tune4C_13TeV_pythia8/e69320067b8f0ba24d244d9ad12dec6d//'
sam["QCD_Pt-10to15_Tune4C_13TeV_pythia8"]["pathSE"]='srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=/pnfs/desy.de/cms/tier2/store/user/fruboes/QCD_Pt-10to15_Tune4C_13TeV_pythia8/DiJet_20140516_QCD_Pt-10to15_Tune4C_13TeV_pythia8/e69320067b8f0ba24d244d9ad12dec6d/'
sam["QCD_Pt-10to15_Tune4C_13TeV_pythia8"]["DS"]='/QCD_Pt-10to15_Tune4C_13TeV_pythia8/Fall13dr-castor_tsg_PU1bx50_POSTLS162_V1-v3/AODSIM'

sam["QCD_Pt-120to170_Tune4C_13TeV_pythia8"]={}
sam["QCD_Pt-120to170_Tune4C_13TeV_pythia8"]["sgeJobs"]=80
sam["QCD_Pt-120to170_Tune4C_13TeV_pythia8"]["crabJobs"]=470
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
sam["QCD_Pt-120to170_Tune4C_13TeV_pythia8"]["pathTrees"]='/XXXTMFTTree/store/user/fruboes/QCD_Pt-120to170_Tune4C_13TeV_pythia8/DiJet_20140516_QCD_Pt-120to170_Tune4C_13TeV_pythia8/f7355bc900d15e86df80b2b0a76f95b0//'
sam["QCD_Pt-120to170_Tune4C_13TeV_pythia8"]["XS"]=493200.0
sam["QCD_Pt-120to170_Tune4C_13TeV_pythia8"]["pathPAT"]='/XXXTMFPAT/store/user/fruboes/QCD_Pt-120to170_Tune4C_13TeV_pythia8/DiJet_20140516_QCD_Pt-120to170_Tune4C_13TeV_pythia8/f7355bc900d15e86df80b2b0a76f95b0//'
sam["QCD_Pt-120to170_Tune4C_13TeV_pythia8"]["pathSE"]='srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=/pnfs/desy.de/cms/tier2/store/user/fruboes/QCD_Pt-120to170_Tune4C_13TeV_pythia8/DiJet_20140516_QCD_Pt-120to170_Tune4C_13TeV_pythia8/f7355bc900d15e86df80b2b0a76f95b0/'
sam["QCD_Pt-120to170_Tune4C_13TeV_pythia8"]["DS"]='/QCD_Pt-120to170_Tune4C_13TeV_pythia8/Fall13dr-castor_tsg_PU1bx50_POSTLS162_V1-v1/AODSIM'

sam["QCD_Pt-15to30_Tune4C_13TeV_pythia8"]={}
sam["QCD_Pt-15to30_Tune4C_13TeV_pythia8"]["sgeJobs"]=80
sam["QCD_Pt-15to30_Tune4C_13TeV_pythia8"]["crabJobs"]=470
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
sam["QCD_Pt-15to30_Tune4C_13TeV_pythia8"]["pathTrees"]='/XXXTMFTTree/store/user/fruboes/QCD_Pt-15to30_Tune4C_13TeV_pythia8/DiJet_20140516_QCD_Pt-15to30_Tune4C_13TeV_pythia8/99e092f084ca597ce9e4db2331fd8768//'
sam["QCD_Pt-15to30_Tune4C_13TeV_pythia8"]["XS"]=2237000000.0
sam["QCD_Pt-15to30_Tune4C_13TeV_pythia8"]["pathPAT"]='/XXXTMFPAT/store/user/fruboes/QCD_Pt-15to30_Tune4C_13TeV_pythia8/DiJet_20140516_QCD_Pt-15to30_Tune4C_13TeV_pythia8/99e092f084ca597ce9e4db2331fd8768//'
sam["QCD_Pt-15to30_Tune4C_13TeV_pythia8"]["pathSE"]='srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=/pnfs/desy.de/cms/tier2/store/user/fruboes/QCD_Pt-15to30_Tune4C_13TeV_pythia8/DiJet_20140516_QCD_Pt-15to30_Tune4C_13TeV_pythia8/99e092f084ca597ce9e4db2331fd8768/'
sam["QCD_Pt-15to30_Tune4C_13TeV_pythia8"]["DS"]='/QCD_Pt-15to30_Tune4C_13TeV_pythia8/Fall13dr-castor_tsg_PU1bx50_POSTLS162_V1-v1/AODSIM'

sam["QCD_Pt-170to300_Tune4C_13TeV_pythia8"]={}
sam["QCD_Pt-170to300_Tune4C_13TeV_pythia8"]["sgeJobs"]=80
sam["QCD_Pt-170to300_Tune4C_13TeV_pythia8"]["crabJobs"]=470
sam["QCD_Pt-170to300_Tune4C_13TeV_pythia8"]["GT"]='START42_V16::All'
sam["QCD_Pt-170to300_Tune4C_13TeV_pythia8"]["weightJet15"]='RooFormulaVar("weight","weight", "xsOverEvents*puWeightJet15V4*trgWeightJet15RawTF2*trgWeightJet15L1RawTF2", RooArgList(v["puWeightJet15V4"]["RooVar"],v["trgWeightJet15RawTF2"]["RooVar"],v["trgWeightJet15L1RawTF2"]["RooVar"]))'
sam["QCD_Pt-170to300_Tune4C_13TeV_pythia8"]["name"]='QCD_Pt-170to300_Tune4C_13TeV_pythia8'
sam["QCD_Pt-170to300_Tune4C_13TeV_pythia8"]["isData"]=False
sam["QCD_Pt-170to300_Tune4C_13TeV_pythia8"]["weightPuOnly"]='RooFormulaVar("weight","weight", "xsOverEvents*puWeightJet15V4", RooArgList(v["puWeightJet15V4"]["RooVar"]))'
sam["QCD_Pt-170to300_Tune4C_13TeV_pythia8"]["weightJet15Inverse"]='RooFormulaVar("weight","weight", "xsOverEvents*puWeightJet15V4", RooArgList(v["puWeightJet15V4"]["RooVar"]))'
sam["QCD_Pt-170to300_Tune4C_13TeV_pythia8"]["numEvents"]=-1
sam["QCD_Pt-170to300_Tune4C_13TeV_pythia8"]["lumiJet15"]='crashMeMC'
sam["QCD_Pt-170to300_Tune4C_13TeV_pythia8"]["weightNoPu"]='RooFormulaVar("weight","weight", "xsOverEvents", RooArgList())'
sam["QCD_Pt-170to300_Tune4C_13TeV_pythia8"]["json"]=''
sam["QCD_Pt-170to300_Tune4C_13TeV_pythia8"]["lumiDiJet15FB"]='crashMeMC'
sam["QCD_Pt-170to300_Tune4C_13TeV_pythia8"]["pathTrees"]='/XXXTMFTTree/store/user/fruboes/QCD_Pt-170to300_Tune4C_13TeV_pythia8/DiJet_20140516_QCD_Pt-170to300_Tune4C_13TeV_pythia8/45c40c0164dc217ea95f49523d90b883//'
sam["QCD_Pt-170to300_Tune4C_13TeV_pythia8"]["XS"]=120300.0
sam["QCD_Pt-170to300_Tune4C_13TeV_pythia8"]["pathPAT"]='/XXXTMFPAT/store/user/fruboes/QCD_Pt-170to300_Tune4C_13TeV_pythia8/DiJet_20140516_QCD_Pt-170to300_Tune4C_13TeV_pythia8/45c40c0164dc217ea95f49523d90b883//'
sam["QCD_Pt-170to300_Tune4C_13TeV_pythia8"]["pathSE"]='srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=/pnfs/desy.de/cms/tier2/store/user/fruboes/QCD_Pt-170to300_Tune4C_13TeV_pythia8/DiJet_20140516_QCD_Pt-170to300_Tune4C_13TeV_pythia8/45c40c0164dc217ea95f49523d90b883/'
sam["QCD_Pt-170to300_Tune4C_13TeV_pythia8"]["DS"]='/QCD_Pt-170to300_Tune4C_13TeV_pythia8/Fall13dr-castor_tsg_PU1bx50_POSTLS162_V2-v1/AODSIM'

sam["QCD_Pt-300to470_Tune4C_13TeV_pythia8"]={}
sam["QCD_Pt-300to470_Tune4C_13TeV_pythia8"]["sgeJobs"]=80
sam["QCD_Pt-300to470_Tune4C_13TeV_pythia8"]["crabJobs"]=470
sam["QCD_Pt-300to470_Tune4C_13TeV_pythia8"]["GT"]='START42_V16::All'
sam["QCD_Pt-300to470_Tune4C_13TeV_pythia8"]["weightJet15"]='RooFormulaVar("weight","weight", "xsOverEvents*puWeightJet15V4*trgWeightJet15RawTF2*trgWeightJet15L1RawTF2", RooArgList(v["puWeightJet15V4"]["RooVar"],v["trgWeightJet15RawTF2"]["RooVar"],v["trgWeightJet15L1RawTF2"]["RooVar"]))'
sam["QCD_Pt-300to470_Tune4C_13TeV_pythia8"]["name"]='QCD_Pt-300to470_Tune4C_13TeV_pythia8'
sam["QCD_Pt-300to470_Tune4C_13TeV_pythia8"]["isData"]=False
sam["QCD_Pt-300to470_Tune4C_13TeV_pythia8"]["weightPuOnly"]='RooFormulaVar("weight","weight", "xsOverEvents*puWeightJet15V4", RooArgList(v["puWeightJet15V4"]["RooVar"]))'
sam["QCD_Pt-300to470_Tune4C_13TeV_pythia8"]["weightJet15Inverse"]='RooFormulaVar("weight","weight", "xsOverEvents*puWeightJet15V4", RooArgList(v["puWeightJet15V4"]["RooVar"]))'
sam["QCD_Pt-300to470_Tune4C_13TeV_pythia8"]["numEvents"]=-1
sam["QCD_Pt-300to470_Tune4C_13TeV_pythia8"]["lumiJet15"]='crashMeMC'
sam["QCD_Pt-300to470_Tune4C_13TeV_pythia8"]["weightNoPu"]='RooFormulaVar("weight","weight", "xsOverEvents", RooArgList())'
sam["QCD_Pt-300to470_Tune4C_13TeV_pythia8"]["json"]=''
sam["QCD_Pt-300to470_Tune4C_13TeV_pythia8"]["lumiDiJet15FB"]='crashMeMC'
sam["QCD_Pt-300to470_Tune4C_13TeV_pythia8"]["pathTrees"]='/XXXTMFTTree/store/user/fruboes/QCD_Pt-300to470_Tune4C_13TeV_pythia8/DiJet_20140516_QCD_Pt-300to470_Tune4C_13TeV_pythia8/ca240519628083f3306afaf28fb39c0d//'
sam["QCD_Pt-300to470_Tune4C_13TeV_pythia8"]["XS"]=7475.0
sam["QCD_Pt-300to470_Tune4C_13TeV_pythia8"]["pathPAT"]='/XXXTMFPAT/store/user/fruboes/QCD_Pt-300to470_Tune4C_13TeV_pythia8/DiJet_20140516_QCD_Pt-300to470_Tune4C_13TeV_pythia8/ca240519628083f3306afaf28fb39c0d//'
sam["QCD_Pt-300to470_Tune4C_13TeV_pythia8"]["pathSE"]='srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=/pnfs/desy.de/cms/tier2/store/user/fruboes/QCD_Pt-300to470_Tune4C_13TeV_pythia8/DiJet_20140516_QCD_Pt-300to470_Tune4C_13TeV_pythia8/ca240519628083f3306afaf28fb39c0d/'
sam["QCD_Pt-300to470_Tune4C_13TeV_pythia8"]["DS"]='/QCD_Pt-300to470_Tune4C_13TeV_pythia8/Fall13dr-castor_tsg_PU1bx50_POSTLS162_V1-v2/AODSIM'

sam["QCD_Pt-30to50_Tune4C_13TeV_pythia8"]={}
sam["QCD_Pt-30to50_Tune4C_13TeV_pythia8"]["sgeJobs"]=80
sam["QCD_Pt-30to50_Tune4C_13TeV_pythia8"]["crabJobs"]=470
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
sam["QCD_Pt-30to50_Tune4C_13TeV_pythia8"]["pathTrees"]='/XXXTMFTTree/store/user/fruboes/QCD_Pt-30to50_Tune4C_13TeV_pythia8/DiJet_20140516_QCD_Pt-30to50_Tune4C_13TeV_pythia8/c558ad3a18d04628a4b38f7254e4a057//'
sam["QCD_Pt-30to50_Tune4C_13TeV_pythia8"]["XS"]=161500000.0
sam["QCD_Pt-30to50_Tune4C_13TeV_pythia8"]["pathPAT"]='/XXXTMFPAT/store/user/fruboes/QCD_Pt-30to50_Tune4C_13TeV_pythia8/DiJet_20140516_QCD_Pt-30to50_Tune4C_13TeV_pythia8/c558ad3a18d04628a4b38f7254e4a057//'
sam["QCD_Pt-30to50_Tune4C_13TeV_pythia8"]["pathSE"]='srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=/pnfs/desy.de/cms/tier2/store/user/fruboes/QCD_Pt-30to50_Tune4C_13TeV_pythia8/DiJet_20140516_QCD_Pt-30to50_Tune4C_13TeV_pythia8/c558ad3a18d04628a4b38f7254e4a057/'
sam["QCD_Pt-30to50_Tune4C_13TeV_pythia8"]["DS"]='/QCD_Pt-30to50_Tune4C_13TeV_pythia8/Fall13dr-castor_tsg_PU1bx50_POSTLS162_V1-v1/AODSIM'

sam["QCD_Pt-470to600_Tune4C_13TeV_pythia8"]={}
sam["QCD_Pt-470to600_Tune4C_13TeV_pythia8"]["sgeJobs"]=80
sam["QCD_Pt-470to600_Tune4C_13TeV_pythia8"]["crabJobs"]=470
sam["QCD_Pt-470to600_Tune4C_13TeV_pythia8"]["GT"]='START42_V16::All'
sam["QCD_Pt-470to600_Tune4C_13TeV_pythia8"]["weightJet15"]='RooFormulaVar("weight","weight", "xsOverEvents*puWeightJet15V4*trgWeightJet15RawTF2*trgWeightJet15L1RawTF2", RooArgList(v["puWeightJet15V4"]["RooVar"],v["trgWeightJet15RawTF2"]["RooVar"],v["trgWeightJet15L1RawTF2"]["RooVar"]))'
sam["QCD_Pt-470to600_Tune4C_13TeV_pythia8"]["name"]='QCD_Pt-470to600_Tune4C_13TeV_pythia8'
sam["QCD_Pt-470to600_Tune4C_13TeV_pythia8"]["isData"]=False
sam["QCD_Pt-470to600_Tune4C_13TeV_pythia8"]["weightPuOnly"]='RooFormulaVar("weight","weight", "xsOverEvents*puWeightJet15V4", RooArgList(v["puWeightJet15V4"]["RooVar"]))'
sam["QCD_Pt-470to600_Tune4C_13TeV_pythia8"]["weightJet15Inverse"]='RooFormulaVar("weight","weight", "xsOverEvents*puWeightJet15V4", RooArgList(v["puWeightJet15V4"]["RooVar"]))'
sam["QCD_Pt-470to600_Tune4C_13TeV_pythia8"]["numEvents"]=-1
sam["QCD_Pt-470to600_Tune4C_13TeV_pythia8"]["lumiJet15"]='crashMeMC'
sam["QCD_Pt-470to600_Tune4C_13TeV_pythia8"]["weightNoPu"]='RooFormulaVar("weight","weight", "xsOverEvents", RooArgList())'
sam["QCD_Pt-470to600_Tune4C_13TeV_pythia8"]["json"]=''
sam["QCD_Pt-470to600_Tune4C_13TeV_pythia8"]["lumiDiJet15FB"]='crashMeMC'
sam["QCD_Pt-470to600_Tune4C_13TeV_pythia8"]["pathTrees"]='/XXXTMFTTree/store/user/fruboes/QCD_Pt-470to600_Tune4C_13TeV_pythia8/DiJet_20140516_QCD_Pt-470to600_Tune4C_13TeV_pythia8/00951ef0f7eaaba4bde52a152a0aed8f//'
sam["QCD_Pt-470to600_Tune4C_13TeV_pythia8"]["XS"]=587.1
sam["QCD_Pt-470to600_Tune4C_13TeV_pythia8"]["pathPAT"]='/XXXTMFPAT/store/user/fruboes/QCD_Pt-470to600_Tune4C_13TeV_pythia8/DiJet_20140516_QCD_Pt-470to600_Tune4C_13TeV_pythia8/00951ef0f7eaaba4bde52a152a0aed8f//'
sam["QCD_Pt-470to600_Tune4C_13TeV_pythia8"]["pathSE"]='srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=/pnfs/desy.de/cms/tier2/store/user/fruboes/QCD_Pt-470to600_Tune4C_13TeV_pythia8/DiJet_20140516_QCD_Pt-470to600_Tune4C_13TeV_pythia8/00951ef0f7eaaba4bde52a152a0aed8f/'
sam["QCD_Pt-470to600_Tune4C_13TeV_pythia8"]["DS"]='/QCD_Pt-470to600_Tune4C_13TeV_pythia8/Fall13dr-castor_tsg_PU1bx50_POSTLS162_V1-v1/AODSIM'

sam["QCD_Pt-50to80_Tune4C_13TeV_pythia8"]={}
sam["QCD_Pt-50to80_Tune4C_13TeV_pythia8"]["sgeJobs"]=80
sam["QCD_Pt-50to80_Tune4C_13TeV_pythia8"]["crabJobs"]=470
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
sam["QCD_Pt-50to80_Tune4C_13TeV_pythia8"]["pathTrees"]='/XXXTMFTTree/store/user/fruboes/QCD_Pt-50to80_Tune4C_13TeV_pythia8/DiJet_20140516_QCD_Pt-50to80_Tune4C_13TeV_pythia8/93709b35c6f80c65b1bc5e47664cf12b//'
sam["QCD_Pt-50to80_Tune4C_13TeV_pythia8"]["XS"]=22110000.0
sam["QCD_Pt-50to80_Tune4C_13TeV_pythia8"]["pathPAT"]='/XXXTMFPAT/store/user/fruboes/QCD_Pt-50to80_Tune4C_13TeV_pythia8/DiJet_20140516_QCD_Pt-50to80_Tune4C_13TeV_pythia8/93709b35c6f80c65b1bc5e47664cf12b//'
sam["QCD_Pt-50to80_Tune4C_13TeV_pythia8"]["pathSE"]='srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=/pnfs/desy.de/cms/tier2/store/user/fruboes/QCD_Pt-50to80_Tune4C_13TeV_pythia8/DiJet_20140516_QCD_Pt-50to80_Tune4C_13TeV_pythia8/93709b35c6f80c65b1bc5e47664cf12b/'
sam["QCD_Pt-50to80_Tune4C_13TeV_pythia8"]["DS"]='/QCD_Pt-50to80_Tune4C_13TeV_pythia8/Fall13dr-castor_tsg_PU1bx50_POSTLS162_V1-v1/AODSIM'

sam["QCD_Pt-600to800_Tune4C_13TeV_pythia8"]={}
sam["QCD_Pt-600to800_Tune4C_13TeV_pythia8"]["sgeJobs"]=80
sam["QCD_Pt-600to800_Tune4C_13TeV_pythia8"]["crabJobs"]=470
sam["QCD_Pt-600to800_Tune4C_13TeV_pythia8"]["GT"]='START42_V16::All'
sam["QCD_Pt-600to800_Tune4C_13TeV_pythia8"]["weightJet15"]='RooFormulaVar("weight","weight", "xsOverEvents*puWeightJet15V4*trgWeightJet15RawTF2*trgWeightJet15L1RawTF2", RooArgList(v["puWeightJet15V4"]["RooVar"],v["trgWeightJet15RawTF2"]["RooVar"],v["trgWeightJet15L1RawTF2"]["RooVar"]))'
sam["QCD_Pt-600to800_Tune4C_13TeV_pythia8"]["name"]='QCD_Pt-600to800_Tune4C_13TeV_pythia8'
sam["QCD_Pt-600to800_Tune4C_13TeV_pythia8"]["isData"]=False
sam["QCD_Pt-600to800_Tune4C_13TeV_pythia8"]["weightPuOnly"]='RooFormulaVar("weight","weight", "xsOverEvents*puWeightJet15V4", RooArgList(v["puWeightJet15V4"]["RooVar"]))'
sam["QCD_Pt-600to800_Tune4C_13TeV_pythia8"]["weightJet15Inverse"]='RooFormulaVar("weight","weight", "xsOverEvents*puWeightJet15V4", RooArgList(v["puWeightJet15V4"]["RooVar"]))'
sam["QCD_Pt-600to800_Tune4C_13TeV_pythia8"]["numEvents"]=-1
sam["QCD_Pt-600to800_Tune4C_13TeV_pythia8"]["lumiJet15"]='crashMeMC'
sam["QCD_Pt-600to800_Tune4C_13TeV_pythia8"]["weightNoPu"]='RooFormulaVar("weight","weight", "xsOverEvents", RooArgList())'
sam["QCD_Pt-600to800_Tune4C_13TeV_pythia8"]["json"]=''
sam["QCD_Pt-600to800_Tune4C_13TeV_pythia8"]["lumiDiJet15FB"]='crashMeMC'
sam["QCD_Pt-600to800_Tune4C_13TeV_pythia8"]["pathTrees"]='/XXXTMFTTree/store/user/fruboes/QCD_Pt-600to800_Tune4C_13TeV_pythia8/DiJet_20140516_QCD_Pt-600to800_Tune4C_13TeV_pythia8/480d69d0a2051b62040655d33c9013da//'
sam["QCD_Pt-600to800_Tune4C_13TeV_pythia8"]["XS"]=167.0
sam["QCD_Pt-600to800_Tune4C_13TeV_pythia8"]["pathPAT"]='/XXXTMFPAT/store/user/fruboes/QCD_Pt-600to800_Tune4C_13TeV_pythia8/DiJet_20140516_QCD_Pt-600to800_Tune4C_13TeV_pythia8/480d69d0a2051b62040655d33c9013da//'
sam["QCD_Pt-600to800_Tune4C_13TeV_pythia8"]["pathSE"]='srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=/pnfs/desy.de/cms/tier2/store/user/fruboes/QCD_Pt-600to800_Tune4C_13TeV_pythia8/DiJet_20140516_QCD_Pt-600to800_Tune4C_13TeV_pythia8/480d69d0a2051b62040655d33c9013da/'
sam["QCD_Pt-600to800_Tune4C_13TeV_pythia8"]["DS"]='/QCD_Pt-600to800_Tune4C_13TeV_pythia8/Fall13dr-castor_tsg_PU1bx50_POSTLS162_V1-v1/AODSIM'

sam["QCD_Pt-800to1000_Tune4C_13TeV_pythia8"]={}
sam["QCD_Pt-800to1000_Tune4C_13TeV_pythia8"]["sgeJobs"]=80
sam["QCD_Pt-800to1000_Tune4C_13TeV_pythia8"]["crabJobs"]=470
sam["QCD_Pt-800to1000_Tune4C_13TeV_pythia8"]["GT"]='START42_V16::All'
sam["QCD_Pt-800to1000_Tune4C_13TeV_pythia8"]["weightJet15"]='RooFormulaVar("weight","weight", "xsOverEvents*puWeightJet15V4*trgWeightJet15RawTF2*trgWeightJet15L1RawTF2", RooArgList(v["puWeightJet15V4"]["RooVar"],v["trgWeightJet15RawTF2"]["RooVar"],v["trgWeightJet15L1RawTF2"]["RooVar"]))'
sam["QCD_Pt-800to1000_Tune4C_13TeV_pythia8"]["name"]='QCD_Pt-800to1000_Tune4C_13TeV_pythia8'
sam["QCD_Pt-800to1000_Tune4C_13TeV_pythia8"]["isData"]=False
sam["QCD_Pt-800to1000_Tune4C_13TeV_pythia8"]["weightPuOnly"]='RooFormulaVar("weight","weight", "xsOverEvents*puWeightJet15V4", RooArgList(v["puWeightJet15V4"]["RooVar"]))'
sam["QCD_Pt-800to1000_Tune4C_13TeV_pythia8"]["weightJet15Inverse"]='RooFormulaVar("weight","weight", "xsOverEvents*puWeightJet15V4", RooArgList(v["puWeightJet15V4"]["RooVar"]))'
sam["QCD_Pt-800to1000_Tune4C_13TeV_pythia8"]["numEvents"]=-1
sam["QCD_Pt-800to1000_Tune4C_13TeV_pythia8"]["lumiJet15"]='crashMeMC'
sam["QCD_Pt-800to1000_Tune4C_13TeV_pythia8"]["weightNoPu"]='RooFormulaVar("weight","weight", "xsOverEvents", RooArgList())'
sam["QCD_Pt-800to1000_Tune4C_13TeV_pythia8"]["json"]=''
sam["QCD_Pt-800to1000_Tune4C_13TeV_pythia8"]["lumiDiJet15FB"]='crashMeMC'
sam["QCD_Pt-800to1000_Tune4C_13TeV_pythia8"]["pathTrees"]='/XXXTMFTTree/store/user/fruboes/QCD_Pt-800to1000_Tune4C_13TeV_pythia8/DiJet_20140516_QCD_Pt-800to1000_Tune4C_13TeV_pythia8/3785454fec0cb5af907bd4395d5415ea//'
sam["QCD_Pt-800to1000_Tune4C_13TeV_pythia8"]["XS"]=28.25
sam["QCD_Pt-800to1000_Tune4C_13TeV_pythia8"]["pathPAT"]='/XXXTMFPAT/store/user/fruboes/QCD_Pt-800to1000_Tune4C_13TeV_pythia8/DiJet_20140516_QCD_Pt-800to1000_Tune4C_13TeV_pythia8/3785454fec0cb5af907bd4395d5415ea//'
sam["QCD_Pt-800to1000_Tune4C_13TeV_pythia8"]["pathSE"]='srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=/pnfs/desy.de/cms/tier2/store/user/fruboes/QCD_Pt-800to1000_Tune4C_13TeV_pythia8/DiJet_20140516_QCD_Pt-800to1000_Tune4C_13TeV_pythia8/3785454fec0cb5af907bd4395d5415ea/'
sam["QCD_Pt-800to1000_Tune4C_13TeV_pythia8"]["DS"]='/QCD_Pt-800to1000_Tune4C_13TeV_pythia8/Fall13dr-castor_tsg_PU1bx50_POSTLS162_V1-v1/AODSIM'

sam["QCD_Pt-80to120_Tune4C_13TeV_pythia8"]={}
sam["QCD_Pt-80to120_Tune4C_13TeV_pythia8"]["sgeJobs"]=80
sam["QCD_Pt-80to120_Tune4C_13TeV_pythia8"]["crabJobs"]=470
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
sam["QCD_Pt-80to120_Tune4C_13TeV_pythia8"]["pathTrees"]='/XXXTMFTTree/store/user/fruboes/QCD_Pt-80to120_Tune4C_13TeV_pythia8/DiJet_20140516_QCD_Pt-80to120_Tune4C_13TeV_pythia8/ed4583f263f96aee4a382259882e5333//'
sam["QCD_Pt-80to120_Tune4C_13TeV_pythia8"]["XS"]=3000114.3
sam["QCD_Pt-80to120_Tune4C_13TeV_pythia8"]["pathPAT"]='/XXXTMFPAT/store/user/fruboes/QCD_Pt-80to120_Tune4C_13TeV_pythia8/DiJet_20140516_QCD_Pt-80to120_Tune4C_13TeV_pythia8/ed4583f263f96aee4a382259882e5333//'
sam["QCD_Pt-80to120_Tune4C_13TeV_pythia8"]["pathSE"]='srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=/pnfs/desy.de/cms/tier2/store/user/fruboes/QCD_Pt-80to120_Tune4C_13TeV_pythia8/DiJet_20140516_QCD_Pt-80to120_Tune4C_13TeV_pythia8/ed4583f263f96aee4a382259882e5333/'
sam["QCD_Pt-80to120_Tune4C_13TeV_pythia8"]["DS"]='/QCD_Pt-80to120_Tune4C_13TeV_pythia8/Fall13dr-castor_tsg_PU1bx50_POSTLS162_V1-v1/AODSIM'

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
