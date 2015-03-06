anaVersion="DiJet_20150225_QCD25ns"
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

rootPath="/scratch/scratch0/tfruboes/DATA_dijet/DiJet_20150225_QCD25ns/"
sam = {}

sam["QCD_Pt-1000to1400_Tune4C_13TeV_pythia8"]={}
sam["QCD_Pt-1000to1400_Tune4C_13TeV_pythia8"]["sgeJobs"]=80
sam["QCD_Pt-1000to1400_Tune4C_13TeV_pythia8"]["crabJobs"]=330
sam["QCD_Pt-1000to1400_Tune4C_13TeV_pythia8"]["GT"]='START42_V16::All'
sam["QCD_Pt-1000to1400_Tune4C_13TeV_pythia8"]["weightJet15"]='RooFormulaVar("weight","weight", "xsOverEvents*puWeightJet15V4*trgWeightJet15RawTF2*trgWeightJet15L1RawTF2", RooArgList(v["puWeightJet15V4"]["RooVar"],v["trgWeightJet15RawTF2"]["RooVar"],v["trgWeightJet15L1RawTF2"]["RooVar"]))'
sam["QCD_Pt-1000to1400_Tune4C_13TeV_pythia8"]["name"]='QCD_Pt-1000to1400_Tune4C_13TeV_pythia8'
sam["QCD_Pt-1000to1400_Tune4C_13TeV_pythia8"]["isData"]=False
sam["QCD_Pt-1000to1400_Tune4C_13TeV_pythia8"]["weightPuOnly"]='RooFormulaVar("weight","weight", "xsOverEvents*puWeightJet15V4", RooArgList(v["puWeightJet15V4"]["RooVar"]))'
sam["QCD_Pt-1000to1400_Tune4C_13TeV_pythia8"]["weightJet15Inverse"]='RooFormulaVar("weight","weight", "xsOverEvents*puWeightJet15V4", RooArgList(v["puWeightJet15V4"]["RooVar"]))'
sam["QCD_Pt-1000to1400_Tune4C_13TeV_pythia8"]["numEvents"]=-1
sam["QCD_Pt-1000to1400_Tune4C_13TeV_pythia8"]["lumiJet15"]='crashMeMC'
sam["QCD_Pt-1000to1400_Tune4C_13TeV_pythia8"]["weightNoPu"]='RooFormulaVar("weight","weight", "xsOverEvents", RooArgList())'
sam["QCD_Pt-1000to1400_Tune4C_13TeV_pythia8"]["json"]=''
sam["QCD_Pt-1000to1400_Tune4C_13TeV_pythia8"]["lumiDiJet15FB"]='crashMeMC'
sam["QCD_Pt-1000to1400_Tune4C_13TeV_pythia8"]["pathTrees"]='/XXXTMFTTree/store/user/fruboes/QCD_Pt-1000to1400_Tune4C_13TeV_pythia8/DiJet_20150225_QCD25ns_QCD_Pt-1000to1400_Tune4C_13TeV_pythia8/786157bb2073a4bd116a5e2a083577ea//'
sam["QCD_Pt-1000to1400_Tune4C_13TeV_pythia8"]["XS"]=8.195
sam["QCD_Pt-1000to1400_Tune4C_13TeV_pythia8"]["pathPAT"]='/XXXTMFPAT/store/user/fruboes/QCD_Pt-1000to1400_Tune4C_13TeV_pythia8/DiJet_20150225_QCD25ns_QCD_Pt-1000to1400_Tune4C_13TeV_pythia8/786157bb2073a4bd116a5e2a083577ea//'
sam["QCD_Pt-1000to1400_Tune4C_13TeV_pythia8"]["pathSE"]='srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=/pnfs/desy.de/cms/tier2/store/user/fruboes/QCD_Pt-1000to1400_Tune4C_13TeV_pythia8/DiJet_20150225_QCD25ns_QCD_Pt-1000to1400_Tune4C_13TeV_pythia8/786157bb2073a4bd116a5e2a083577ea/'
sam["QCD_Pt-1000to1400_Tune4C_13TeV_pythia8"]["DS"]='/QCD_Pt-1000to1400_Tune4C_13TeV_pythia8/Phys14DR-AVE20BX25_tsg_castor_PHYS14_25_V3-v1/AODSIM'

sam["QCD_Pt-120to170_Tune4C_13TeV_pythia8"]={}
sam["QCD_Pt-120to170_Tune4C_13TeV_pythia8"]["sgeJobs"]=80
sam["QCD_Pt-120to170_Tune4C_13TeV_pythia8"]["crabJobs"]=330
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
sam["QCD_Pt-120to170_Tune4C_13TeV_pythia8"]["pathTrees"]='/XXXTMFTTree/store/user/fruboes/QCD_Pt-120to170_Tune4C_13TeV_pythia8/DiJet_20150225_QCD25ns_QCD_Pt-120to170_Tune4C_13TeV_pythia8/5593ed0d4aba8aa7587b61fdd3fb12b2//'
sam["QCD_Pt-120to170_Tune4C_13TeV_pythia8"]["XS"]=493200.0
sam["QCD_Pt-120to170_Tune4C_13TeV_pythia8"]["pathPAT"]='/XXXTMFPAT/store/user/fruboes/QCD_Pt-120to170_Tune4C_13TeV_pythia8/DiJet_20150225_QCD25ns_QCD_Pt-120to170_Tune4C_13TeV_pythia8/5593ed0d4aba8aa7587b61fdd3fb12b2//'
sam["QCD_Pt-120to170_Tune4C_13TeV_pythia8"]["pathSE"]='srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=/pnfs/desy.de/cms/tier2/store/user/fruboes/QCD_Pt-120to170_Tune4C_13TeV_pythia8/DiJet_20150225_QCD25ns_QCD_Pt-120to170_Tune4C_13TeV_pythia8/5593ed0d4aba8aa7587b61fdd3fb12b2/'
sam["QCD_Pt-120to170_Tune4C_13TeV_pythia8"]["DS"]='/QCD_Pt-120to170_Tune4C_13TeV_pythia8/Phys14DR-AVE20BX25_tsg_castor_PHYS14_25_V3-v1/AODSIM'

sam["QCD_Pt-1400to1800_Tune4C_13TeV_pythia8"]={}
sam["QCD_Pt-1400to1800_Tune4C_13TeV_pythia8"]["sgeJobs"]=80
sam["QCD_Pt-1400to1800_Tune4C_13TeV_pythia8"]["crabJobs"]=330
sam["QCD_Pt-1400to1800_Tune4C_13TeV_pythia8"]["GT"]='START42_V16::All'
sam["QCD_Pt-1400to1800_Tune4C_13TeV_pythia8"]["weightJet15"]='RooFormulaVar("weight","weight", "xsOverEvents*puWeightJet15V4*trgWeightJet15RawTF2*trgWeightJet15L1RawTF2", RooArgList(v["puWeightJet15V4"]["RooVar"],v["trgWeightJet15RawTF2"]["RooVar"],v["trgWeightJet15L1RawTF2"]["RooVar"]))'
sam["QCD_Pt-1400to1800_Tune4C_13TeV_pythia8"]["name"]='QCD_Pt-1400to1800_Tune4C_13TeV_pythia8'
sam["QCD_Pt-1400to1800_Tune4C_13TeV_pythia8"]["isData"]=False
sam["QCD_Pt-1400to1800_Tune4C_13TeV_pythia8"]["weightPuOnly"]='RooFormulaVar("weight","weight", "xsOverEvents*puWeightJet15V4", RooArgList(v["puWeightJet15V4"]["RooVar"]))'
sam["QCD_Pt-1400to1800_Tune4C_13TeV_pythia8"]["weightJet15Inverse"]='RooFormulaVar("weight","weight", "xsOverEvents*puWeightJet15V4", RooArgList(v["puWeightJet15V4"]["RooVar"]))'
sam["QCD_Pt-1400to1800_Tune4C_13TeV_pythia8"]["numEvents"]=-1
sam["QCD_Pt-1400to1800_Tune4C_13TeV_pythia8"]["lumiJet15"]='crashMeMC'
sam["QCD_Pt-1400to1800_Tune4C_13TeV_pythia8"]["weightNoPu"]='RooFormulaVar("weight","weight", "xsOverEvents", RooArgList())'
sam["QCD_Pt-1400to1800_Tune4C_13TeV_pythia8"]["json"]=''
sam["QCD_Pt-1400to1800_Tune4C_13TeV_pythia8"]["lumiDiJet15FB"]='crashMeMC'
sam["QCD_Pt-1400to1800_Tune4C_13TeV_pythia8"]["pathTrees"]='/XXXTMFTTree/store/user/fruboes/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/DiJet_20150225_QCD25ns_QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/6f064f1ef21988bcc31d0873e5711f4d//'
sam["QCD_Pt-1400to1800_Tune4C_13TeV_pythia8"]["XS"]=0.7346
sam["QCD_Pt-1400to1800_Tune4C_13TeV_pythia8"]["pathPAT"]='/XXXTMFPAT/store/user/fruboes/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/DiJet_20150225_QCD25ns_QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/6f064f1ef21988bcc31d0873e5711f4d//'
sam["QCD_Pt-1400to1800_Tune4C_13TeV_pythia8"]["pathSE"]='srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=/pnfs/desy.de/cms/tier2/store/user/fruboes/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/DiJet_20150225_QCD25ns_QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/6f064f1ef21988bcc31d0873e5711f4d/'
sam["QCD_Pt-1400to1800_Tune4C_13TeV_pythia8"]["DS"]='/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/Phys14DR-AVE20BX25_tsg_castor_PHYS14_25_V3-v1/AODSIM'

sam["QCD_Pt-15to30_Tune4C_13TeV_pythia8"]={}
sam["QCD_Pt-15to30_Tune4C_13TeV_pythia8"]["sgeJobs"]=80
sam["QCD_Pt-15to30_Tune4C_13TeV_pythia8"]["crabJobs"]=330
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
sam["QCD_Pt-15to30_Tune4C_13TeV_pythia8"]["pathTrees"]='/XXXTMFTTree/store/user/fruboes/QCD_Pt-15to30_Tune4C_13TeV_pythia8/DiJet_20150225_QCD25ns_QCD_Pt-15to30_Tune4C_13TeV_pythia8/212a2bfcf5599cd83fa5bb20de9c3e27//'
sam["QCD_Pt-15to30_Tune4C_13TeV_pythia8"]["XS"]=2237000000.0
sam["QCD_Pt-15to30_Tune4C_13TeV_pythia8"]["pathPAT"]='/XXXTMFPAT/store/user/fruboes/QCD_Pt-15to30_Tune4C_13TeV_pythia8/DiJet_20150225_QCD25ns_QCD_Pt-15to30_Tune4C_13TeV_pythia8/212a2bfcf5599cd83fa5bb20de9c3e27//'
sam["QCD_Pt-15to30_Tune4C_13TeV_pythia8"]["pathSE"]='srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=/pnfs/desy.de/cms/tier2/store/user/fruboes/QCD_Pt-15to30_Tune4C_13TeV_pythia8/DiJet_20150225_QCD25ns_QCD_Pt-15to30_Tune4C_13TeV_pythia8/212a2bfcf5599cd83fa5bb20de9c3e27/'
sam["QCD_Pt-15to30_Tune4C_13TeV_pythia8"]["DS"]='/QCD_Pt-15to30_Tune4C_13TeV_pythia8/Phys14DR-AVE20BX25_tsg_castor_PHYS14_25_V3-v2/AODSIM'

sam["QCD_Pt-170to300_Tune4C_13TeV_pythia8"]={}
sam["QCD_Pt-170to300_Tune4C_13TeV_pythia8"]["sgeJobs"]=80
sam["QCD_Pt-170to300_Tune4C_13TeV_pythia8"]["crabJobs"]=330
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
sam["QCD_Pt-170to300_Tune4C_13TeV_pythia8"]["pathTrees"]='/XXXTMFTTree/store/user/fruboes/QCD_Pt-170to300_Tune4C_13TeV_pythia8/DiJet_20150225_QCD25ns_QCD_Pt-170to300_Tune4C_13TeV_pythia8/e2e1c7206eaa978fcbb37306c7ccfd2a//'
sam["QCD_Pt-170to300_Tune4C_13TeV_pythia8"]["XS"]=120300.0
sam["QCD_Pt-170to300_Tune4C_13TeV_pythia8"]["pathPAT"]='/XXXTMFPAT/store/user/fruboes/QCD_Pt-170to300_Tune4C_13TeV_pythia8/DiJet_20150225_QCD25ns_QCD_Pt-170to300_Tune4C_13TeV_pythia8/e2e1c7206eaa978fcbb37306c7ccfd2a//'
sam["QCD_Pt-170to300_Tune4C_13TeV_pythia8"]["pathSE"]='srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=/pnfs/desy.de/cms/tier2/store/user/fruboes/QCD_Pt-170to300_Tune4C_13TeV_pythia8/DiJet_20150225_QCD25ns_QCD_Pt-170to300_Tune4C_13TeV_pythia8/e2e1c7206eaa978fcbb37306c7ccfd2a/'
sam["QCD_Pt-170to300_Tune4C_13TeV_pythia8"]["DS"]='/QCD_Pt-170to300_Tune4C_13TeV_pythia8/Phys14DR-AVE20BX25_tsg_castor_PHYS14_25_V3-v1/AODSIM'

sam["QCD_Pt-1800_Tune4C_13TeV_pythia8"]={}
sam["QCD_Pt-1800_Tune4C_13TeV_pythia8"]["sgeJobs"]=80
sam["QCD_Pt-1800_Tune4C_13TeV_pythia8"]["crabJobs"]=330
sam["QCD_Pt-1800_Tune4C_13TeV_pythia8"]["GT"]='START42_V16::All'
sam["QCD_Pt-1800_Tune4C_13TeV_pythia8"]["weightJet15"]='RooFormulaVar("weight","weight", "xsOverEvents*puWeightJet15V4*trgWeightJet15RawTF2*trgWeightJet15L1RawTF2", RooArgList(v["puWeightJet15V4"]["RooVar"],v["trgWeightJet15RawTF2"]["RooVar"],v["trgWeightJet15L1RawTF2"]["RooVar"]))'
sam["QCD_Pt-1800_Tune4C_13TeV_pythia8"]["name"]='QCD_Pt-1800_Tune4C_13TeV_pythia8'
sam["QCD_Pt-1800_Tune4C_13TeV_pythia8"]["isData"]=False
sam["QCD_Pt-1800_Tune4C_13TeV_pythia8"]["weightPuOnly"]='RooFormulaVar("weight","weight", "xsOverEvents*puWeightJet15V4", RooArgList(v["puWeightJet15V4"]["RooVar"]))'
sam["QCD_Pt-1800_Tune4C_13TeV_pythia8"]["weightJet15Inverse"]='RooFormulaVar("weight","weight", "xsOverEvents*puWeightJet15V4", RooArgList(v["puWeightJet15V4"]["RooVar"]))'
sam["QCD_Pt-1800_Tune4C_13TeV_pythia8"]["numEvents"]=-1
sam["QCD_Pt-1800_Tune4C_13TeV_pythia8"]["lumiJet15"]='crashMeMC'
sam["QCD_Pt-1800_Tune4C_13TeV_pythia8"]["weightNoPu"]='RooFormulaVar("weight","weight", "xsOverEvents", RooArgList())'
sam["QCD_Pt-1800_Tune4C_13TeV_pythia8"]["json"]=''
sam["QCD_Pt-1800_Tune4C_13TeV_pythia8"]["lumiDiJet15FB"]='crashMeMC'
sam["QCD_Pt-1800_Tune4C_13TeV_pythia8"]["pathTrees"]='/XXXTMFTTree/store/user/fruboes/QCD_Pt-1800_Tune4C_13TeV_pythia8/DiJet_20150225_QCD25ns_QCD_Pt-1800_Tune4C_13TeV_pythia8/48d407b16e7e83da3d0291b08ac20996//'
sam["QCD_Pt-1800_Tune4C_13TeV_pythia8"]["XS"]=0.1091
sam["QCD_Pt-1800_Tune4C_13TeV_pythia8"]["pathPAT"]='/XXXTMFPAT/store/user/fruboes/QCD_Pt-1800_Tune4C_13TeV_pythia8/DiJet_20150225_QCD25ns_QCD_Pt-1800_Tune4C_13TeV_pythia8/48d407b16e7e83da3d0291b08ac20996//'
sam["QCD_Pt-1800_Tune4C_13TeV_pythia8"]["pathSE"]='srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=/pnfs/desy.de/cms/tier2/store/user/fruboes/QCD_Pt-1800_Tune4C_13TeV_pythia8/DiJet_20150225_QCD25ns_QCD_Pt-1800_Tune4C_13TeV_pythia8/48d407b16e7e83da3d0291b08ac20996/'
sam["QCD_Pt-1800_Tune4C_13TeV_pythia8"]["DS"]='/QCD_Pt-1800_Tune4C_13TeV_pythia8/Phys14DR-AVE20BX25_tsg_castor_PHYS14_25_V3-v1/AODSIM'

sam["QCD_Pt-300to470_Tune4C_13TeV_pythia8"]={}
sam["QCD_Pt-300to470_Tune4C_13TeV_pythia8"]["sgeJobs"]=80
sam["QCD_Pt-300to470_Tune4C_13TeV_pythia8"]["crabJobs"]=330
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
sam["QCD_Pt-300to470_Tune4C_13TeV_pythia8"]["pathTrees"]='/XXXTMFTTree/store/user/fruboes/QCD_Pt-300to470_Tune4C_13TeV_pythia8/DiJet_20150225_QCD25ns_QCD_Pt-300to470_Tune4C_13TeV_pythia8/b2c68c0b830eee4575c8f565e4de1d07//'
sam["QCD_Pt-300to470_Tune4C_13TeV_pythia8"]["XS"]=7475.0
sam["QCD_Pt-300to470_Tune4C_13TeV_pythia8"]["pathPAT"]='/XXXTMFPAT/store/user/fruboes/QCD_Pt-300to470_Tune4C_13TeV_pythia8/DiJet_20150225_QCD25ns_QCD_Pt-300to470_Tune4C_13TeV_pythia8/b2c68c0b830eee4575c8f565e4de1d07//'
sam["QCD_Pt-300to470_Tune4C_13TeV_pythia8"]["pathSE"]='srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=/pnfs/desy.de/cms/tier2/store/user/fruboes/QCD_Pt-300to470_Tune4C_13TeV_pythia8/DiJet_20150225_QCD25ns_QCD_Pt-300to470_Tune4C_13TeV_pythia8/b2c68c0b830eee4575c8f565e4de1d07/'
sam["QCD_Pt-300to470_Tune4C_13TeV_pythia8"]["DS"]='/QCD_Pt-300to470_Tune4C_13TeV_pythia8/Phys14DR-AVE20BX25_tsg_castor_PHYS14_25_V3-v1/AODSIM'

sam["QCD_Pt-30to50_Tune4C_13TeV_pythia8"]={}
sam["QCD_Pt-30to50_Tune4C_13TeV_pythia8"]["sgeJobs"]=80
sam["QCD_Pt-30to50_Tune4C_13TeV_pythia8"]["crabJobs"]=330
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
sam["QCD_Pt-30to50_Tune4C_13TeV_pythia8"]["pathTrees"]='/XXXTMFTTree/store/user/fruboes/QCD_Pt-30to50_Tune4C_13TeV_pythia8/DiJet_20150225_QCD25ns_QCD_Pt-30to50_Tune4C_13TeV_pythia8/88df97595cac2a6fa47f471748d8070e//'
sam["QCD_Pt-30to50_Tune4C_13TeV_pythia8"]["XS"]=161500000.0
sam["QCD_Pt-30to50_Tune4C_13TeV_pythia8"]["pathPAT"]='/XXXTMFPAT/store/user/fruboes/QCD_Pt-30to50_Tune4C_13TeV_pythia8/DiJet_20150225_QCD25ns_QCD_Pt-30to50_Tune4C_13TeV_pythia8/88df97595cac2a6fa47f471748d8070e//'
sam["QCD_Pt-30to50_Tune4C_13TeV_pythia8"]["pathSE"]='srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=/pnfs/desy.de/cms/tier2/store/user/fruboes/QCD_Pt-30to50_Tune4C_13TeV_pythia8/DiJet_20150225_QCD25ns_QCD_Pt-30to50_Tune4C_13TeV_pythia8/88df97595cac2a6fa47f471748d8070e/'
sam["QCD_Pt-30to50_Tune4C_13TeV_pythia8"]["DS"]='/QCD_Pt-30to50_Tune4C_13TeV_pythia8/Phys14DR-AVE20BX25_tsg_castor_PHYS14_25_V3-v2/AODSIM'

sam["QCD_Pt-470to600_Tune4C_13TeV_pythia8"]={}
sam["QCD_Pt-470to600_Tune4C_13TeV_pythia8"]["sgeJobs"]=80
sam["QCD_Pt-470to600_Tune4C_13TeV_pythia8"]["crabJobs"]=330
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
sam["QCD_Pt-470to600_Tune4C_13TeV_pythia8"]["pathTrees"]='/XXXTMFTTree/store/user/fruboes/QCD_Pt-470to600_Tune4C_13TeV_pythia8/DiJet_20150225_QCD25ns_QCD_Pt-470to600_Tune4C_13TeV_pythia8/bdb9b12f3cbb846b5e85adf8ca15e8b2//'
sam["QCD_Pt-470to600_Tune4C_13TeV_pythia8"]["XS"]=587.1
sam["QCD_Pt-470to600_Tune4C_13TeV_pythia8"]["pathPAT"]='/XXXTMFPAT/store/user/fruboes/QCD_Pt-470to600_Tune4C_13TeV_pythia8/DiJet_20150225_QCD25ns_QCD_Pt-470to600_Tune4C_13TeV_pythia8/bdb9b12f3cbb846b5e85adf8ca15e8b2//'
sam["QCD_Pt-470to600_Tune4C_13TeV_pythia8"]["pathSE"]='srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=/pnfs/desy.de/cms/tier2/store/user/fruboes/QCD_Pt-470to600_Tune4C_13TeV_pythia8/DiJet_20150225_QCD25ns_QCD_Pt-470to600_Tune4C_13TeV_pythia8/bdb9b12f3cbb846b5e85adf8ca15e8b2/'
sam["QCD_Pt-470to600_Tune4C_13TeV_pythia8"]["DS"]='/QCD_Pt-470to600_Tune4C_13TeV_pythia8/Phys14DR-AVE20BX25_tsg_castor_PHYS14_25_V3-v1/AODSIM'

sam["QCD_Pt-50to80_Tune4C_13TeV_pythia8"]={}
sam["QCD_Pt-50to80_Tune4C_13TeV_pythia8"]["sgeJobs"]=80
sam["QCD_Pt-50to80_Tune4C_13TeV_pythia8"]["crabJobs"]=330
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
sam["QCD_Pt-50to80_Tune4C_13TeV_pythia8"]["pathTrees"]='/XXXTMFTTree/store/user/fruboes/QCD_Pt-50to80_Tune4C_13TeV_pythia8/DiJet_20150225_QCD25ns_QCD_Pt-50to80_Tune4C_13TeV_pythia8/8a80c4a515433b828b5575865e5a1583//'
sam["QCD_Pt-50to80_Tune4C_13TeV_pythia8"]["XS"]=22110000.0
sam["QCD_Pt-50to80_Tune4C_13TeV_pythia8"]["pathPAT"]='/XXXTMFPAT/store/user/fruboes/QCD_Pt-50to80_Tune4C_13TeV_pythia8/DiJet_20150225_QCD25ns_QCD_Pt-50to80_Tune4C_13TeV_pythia8/8a80c4a515433b828b5575865e5a1583//'
sam["QCD_Pt-50to80_Tune4C_13TeV_pythia8"]["pathSE"]='srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=/pnfs/desy.de/cms/tier2/store/user/fruboes/QCD_Pt-50to80_Tune4C_13TeV_pythia8/DiJet_20150225_QCD25ns_QCD_Pt-50to80_Tune4C_13TeV_pythia8/8a80c4a515433b828b5575865e5a1583/'
sam["QCD_Pt-50to80_Tune4C_13TeV_pythia8"]["DS"]='/QCD_Pt-50to80_Tune4C_13TeV_pythia8/Phys14DR-AVE20BX25_tsg_castor_PHYS14_25_V3-v1/AODSIM'

sam["QCD_Pt-600to800_Tune4C_13TeV_pythia8"]={}
sam["QCD_Pt-600to800_Tune4C_13TeV_pythia8"]["sgeJobs"]=80
sam["QCD_Pt-600to800_Tune4C_13TeV_pythia8"]["crabJobs"]=330
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
sam["QCD_Pt-600to800_Tune4C_13TeV_pythia8"]["pathTrees"]='/XXXTMFTTree/store/user/fruboes/QCD_Pt-600to800_Tune4C_13TeV_pythia8/DiJet_20150225_QCD25ns_QCD_Pt-600to800_Tune4C_13TeV_pythia8/611b54704a81699184928d51cb3e24ac//'
sam["QCD_Pt-600to800_Tune4C_13TeV_pythia8"]["XS"]=167.0
sam["QCD_Pt-600to800_Tune4C_13TeV_pythia8"]["pathPAT"]='/XXXTMFPAT/store/user/fruboes/QCD_Pt-600to800_Tune4C_13TeV_pythia8/DiJet_20150225_QCD25ns_QCD_Pt-600to800_Tune4C_13TeV_pythia8/611b54704a81699184928d51cb3e24ac//'
sam["QCD_Pt-600to800_Tune4C_13TeV_pythia8"]["pathSE"]='srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=/pnfs/desy.de/cms/tier2/store/user/fruboes/QCD_Pt-600to800_Tune4C_13TeV_pythia8/DiJet_20150225_QCD25ns_QCD_Pt-600to800_Tune4C_13TeV_pythia8/611b54704a81699184928d51cb3e24ac/'
sam["QCD_Pt-600to800_Tune4C_13TeV_pythia8"]["DS"]='/QCD_Pt-600to800_Tune4C_13TeV_pythia8/Phys14DR-AVE20BX25_tsg_castor_PHYS14_25_V3-v1/AODSIM'

sam["QCD_Pt-800to1000_Tune4C_13TeV_pythia8"]={}
sam["QCD_Pt-800to1000_Tune4C_13TeV_pythia8"]["sgeJobs"]=80
sam["QCD_Pt-800to1000_Tune4C_13TeV_pythia8"]["crabJobs"]=330
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
sam["QCD_Pt-800to1000_Tune4C_13TeV_pythia8"]["pathTrees"]='/XXXTMFTTree/store/user/fruboes/QCD_Pt-800to1000_Tune4C_13TeV_pythia8/DiJet_20150225_QCD25ns_QCD_Pt-800to1000_Tune4C_13TeV_pythia8/2da60c898ba638c8a7afd25171bc658e//'
sam["QCD_Pt-800to1000_Tune4C_13TeV_pythia8"]["XS"]=28.25
sam["QCD_Pt-800to1000_Tune4C_13TeV_pythia8"]["pathPAT"]='/XXXTMFPAT/store/user/fruboes/QCD_Pt-800to1000_Tune4C_13TeV_pythia8/DiJet_20150225_QCD25ns_QCD_Pt-800to1000_Tune4C_13TeV_pythia8/2da60c898ba638c8a7afd25171bc658e//'
sam["QCD_Pt-800to1000_Tune4C_13TeV_pythia8"]["pathSE"]='srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=/pnfs/desy.de/cms/tier2/store/user/fruboes/QCD_Pt-800to1000_Tune4C_13TeV_pythia8/DiJet_20150225_QCD25ns_QCD_Pt-800to1000_Tune4C_13TeV_pythia8/2da60c898ba638c8a7afd25171bc658e/'
sam["QCD_Pt-800to1000_Tune4C_13TeV_pythia8"]["DS"]='/QCD_Pt-800to1000_Tune4C_13TeV_pythia8/Phys14DR-AVE20BX25_tsg_castor_PHYS14_25_V3-v1/AODSIM'

sam["QCD_Pt-80to120_Tune4C_13TeV_pythia8"]={}
sam["QCD_Pt-80to120_Tune4C_13TeV_pythia8"]["sgeJobs"]=80
sam["QCD_Pt-80to120_Tune4C_13TeV_pythia8"]["crabJobs"]=330
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
sam["QCD_Pt-80to120_Tune4C_13TeV_pythia8"]["pathTrees"]='/XXXTMFTTree/store/user/fruboes/QCD_Pt-80to120_Tune4C_13TeV_pythia8/DiJet_20150225_QCD25ns_QCD_Pt-80to120_Tune4C_13TeV_pythia8/29f04759a7da0ed7f07963c9f5606479//'
sam["QCD_Pt-80to120_Tune4C_13TeV_pythia8"]["XS"]=3000114.3
sam["QCD_Pt-80to120_Tune4C_13TeV_pythia8"]["pathPAT"]='/XXXTMFPAT/store/user/fruboes/QCD_Pt-80to120_Tune4C_13TeV_pythia8/DiJet_20150225_QCD25ns_QCD_Pt-80to120_Tune4C_13TeV_pythia8/29f04759a7da0ed7f07963c9f5606479//'
sam["QCD_Pt-80to120_Tune4C_13TeV_pythia8"]["pathSE"]='srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=/pnfs/desy.de/cms/tier2/store/user/fruboes/QCD_Pt-80to120_Tune4C_13TeV_pythia8/DiJet_20150225_QCD25ns_QCD_Pt-80to120_Tune4C_13TeV_pythia8/29f04759a7da0ed7f07963c9f5606479/'
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
