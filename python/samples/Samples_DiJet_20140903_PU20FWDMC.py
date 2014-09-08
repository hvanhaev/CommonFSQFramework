anaVersion="DiJet_20140903_PU20FWDMC"
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

rootPath="/scratch/scratch0/tfruboes/DATA_dijet/DiJet_20140903_PU20FWDMC/"
sam = {}

sam["QCD_Pt-10to15_fwdJet_Tune4C_13TeV_pythia8"]={}
sam["QCD_Pt-10to15_fwdJet_Tune4C_13TeV_pythia8"]["sgeJobs"]=80
sam["QCD_Pt-10to15_fwdJet_Tune4C_13TeV_pythia8"]["crabJobs"]=470
sam["QCD_Pt-10to15_fwdJet_Tune4C_13TeV_pythia8"]["GT"]='START42_V16::All'
sam["QCD_Pt-10to15_fwdJet_Tune4C_13TeV_pythia8"]["weightJet15"]='RooFormulaVar("weight","weight", "xsOverEvents*puWeightJet15V4*trgWeightJet15RawTF2*trgWeightJet15L1RawTF2", RooArgList(v["puWeightJet15V4"]["RooVar"],v["trgWeightJet15RawTF2"]["RooVar"],v["trgWeightJet15L1RawTF2"]["RooVar"]))'
sam["QCD_Pt-10to15_fwdJet_Tune4C_13TeV_pythia8"]["name"]='QCD_Pt-10to15_fwdJet_Tune4C_13TeV_pythia8'
sam["QCD_Pt-10to15_fwdJet_Tune4C_13TeV_pythia8"]["isData"]=False
sam["QCD_Pt-10to15_fwdJet_Tune4C_13TeV_pythia8"]["weightPuOnly"]='RooFormulaVar("weight","weight", "xsOverEvents*puWeightJet15V4", RooArgList(v["puWeightJet15V4"]["RooVar"]))'
sam["QCD_Pt-10to15_fwdJet_Tune4C_13TeV_pythia8"]["weightJet15Inverse"]='RooFormulaVar("weight","weight", "xsOverEvents*puWeightJet15V4", RooArgList(v["puWeightJet15V4"]["RooVar"]))'
sam["QCD_Pt-10to15_fwdJet_Tune4C_13TeV_pythia8"]["numEvents"]=-1
sam["QCD_Pt-10to15_fwdJet_Tune4C_13TeV_pythia8"]["lumiJet15"]='crashMeMC'
sam["QCD_Pt-10to15_fwdJet_Tune4C_13TeV_pythia8"]["weightNoPu"]='RooFormulaVar("weight","weight", "xsOverEvents", RooArgList())'
sam["QCD_Pt-10to15_fwdJet_Tune4C_13TeV_pythia8"]["json"]=''
sam["QCD_Pt-10to15_fwdJet_Tune4C_13TeV_pythia8"]["lumiDiJet15FB"]='crashMeMC'
sam["QCD_Pt-10to15_fwdJet_Tune4C_13TeV_pythia8"]["pathTrees"]='/XXXTMFTTree/store/user/fruboes/QCD_Pt-10to15_fwdJet_Tune4C_13TeV_pythia8/DiJet_20140903_PU20FWDMC_QCD_Pt-10to15_fwdJet_Tune4C_13TeV_pythia8/ad312982f9c229126c0b740d5fced447//'
sam["QCD_Pt-10to15_fwdJet_Tune4C_13TeV_pythia8"]["XS"]=564600000.0
sam["QCD_Pt-10to15_fwdJet_Tune4C_13TeV_pythia8"]["pathPAT"]='/XXXTMFPAT/store/user/fruboes/QCD_Pt-10to15_fwdJet_Tune4C_13TeV_pythia8/DiJet_20140903_PU20FWDMC_QCD_Pt-10to15_fwdJet_Tune4C_13TeV_pythia8/ad312982f9c229126c0b740d5fced447//'
sam["QCD_Pt-10to15_fwdJet_Tune4C_13TeV_pythia8"]["pathSE"]='srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=/pnfs/desy.de/cms/tier2/store/user/fruboes/QCD_Pt-10to15_fwdJet_Tune4C_13TeV_pythia8/DiJet_20140903_PU20FWDMC_QCD_Pt-10to15_fwdJet_Tune4C_13TeV_pythia8/ad312982f9c229126c0b740d5fced447/'
sam["QCD_Pt-10to15_fwdJet_Tune4C_13TeV_pythia8"]["DS"]='/QCD_Pt-10to15_fwdJet_Tune4C_13TeV_pythia8/Spring14dr-castor_PU20bx25_POSTLS170_V5-v1/AODSIM'

sam["QCD_Pt-120to170_fwdJet_Tune4C_13TeV_pythia8"]={}
sam["QCD_Pt-120to170_fwdJet_Tune4C_13TeV_pythia8"]["sgeJobs"]=80
sam["QCD_Pt-120to170_fwdJet_Tune4C_13TeV_pythia8"]["crabJobs"]=470
sam["QCD_Pt-120to170_fwdJet_Tune4C_13TeV_pythia8"]["GT"]='START42_V16::All'
sam["QCD_Pt-120to170_fwdJet_Tune4C_13TeV_pythia8"]["weightJet15"]='RooFormulaVar("weight","weight", "xsOverEvents*puWeightJet15V4*trgWeightJet15RawTF2*trgWeightJet15L1RawTF2", RooArgList(v["puWeightJet15V4"]["RooVar"],v["trgWeightJet15RawTF2"]["RooVar"],v["trgWeightJet15L1RawTF2"]["RooVar"]))'
sam["QCD_Pt-120to170_fwdJet_Tune4C_13TeV_pythia8"]["name"]='QCD_Pt-120to170_fwdJet_Tune4C_13TeV_pythia8'
sam["QCD_Pt-120to170_fwdJet_Tune4C_13TeV_pythia8"]["isData"]=False
sam["QCD_Pt-120to170_fwdJet_Tune4C_13TeV_pythia8"]["weightPuOnly"]='RooFormulaVar("weight","weight", "xsOverEvents*puWeightJet15V4", RooArgList(v["puWeightJet15V4"]["RooVar"]))'
sam["QCD_Pt-120to170_fwdJet_Tune4C_13TeV_pythia8"]["weightJet15Inverse"]='RooFormulaVar("weight","weight", "xsOverEvents*puWeightJet15V4", RooArgList(v["puWeightJet15V4"]["RooVar"]))'
sam["QCD_Pt-120to170_fwdJet_Tune4C_13TeV_pythia8"]["numEvents"]=-1
sam["QCD_Pt-120to170_fwdJet_Tune4C_13TeV_pythia8"]["lumiJet15"]='crashMeMC'
sam["QCD_Pt-120to170_fwdJet_Tune4C_13TeV_pythia8"]["weightNoPu"]='RooFormulaVar("weight","weight", "xsOverEvents", RooArgList())'
sam["QCD_Pt-120to170_fwdJet_Tune4C_13TeV_pythia8"]["json"]=''
sam["QCD_Pt-120to170_fwdJet_Tune4C_13TeV_pythia8"]["lumiDiJet15FB"]='crashMeMC'
sam["QCD_Pt-120to170_fwdJet_Tune4C_13TeV_pythia8"]["pathTrees"]='/XXXTMFTTree/store/user/fruboes/QCD_Pt-120to170_fwdJet_Tune4C_13TeV_pythia8/DiJet_20140903_PU20FWDMC_QCD_Pt-120to170_fwdJet_Tune4C_13TeV_pythia8/ad312982f9c229126c0b740d5fced447//'
sam["QCD_Pt-120to170_fwdJet_Tune4C_13TeV_pythia8"]["XS"]=166766.6
sam["QCD_Pt-120to170_fwdJet_Tune4C_13TeV_pythia8"]["pathPAT"]='/XXXTMFPAT/store/user/fruboes/QCD_Pt-120to170_fwdJet_Tune4C_13TeV_pythia8/DiJet_20140903_PU20FWDMC_QCD_Pt-120to170_fwdJet_Tune4C_13TeV_pythia8/ad312982f9c229126c0b740d5fced447//'
sam["QCD_Pt-120to170_fwdJet_Tune4C_13TeV_pythia8"]["pathSE"]='srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=/pnfs/desy.de/cms/tier2/store/user/fruboes/QCD_Pt-120to170_fwdJet_Tune4C_13TeV_pythia8/DiJet_20140903_PU20FWDMC_QCD_Pt-120to170_fwdJet_Tune4C_13TeV_pythia8/ad312982f9c229126c0b740d5fced447/'
sam["QCD_Pt-120to170_fwdJet_Tune4C_13TeV_pythia8"]["DS"]='/QCD_Pt-120to170_fwdJet_Tune4C_13TeV_pythia8/Spring14dr-castor_PU20bx25_POSTLS170_V5-v1/AODSIM'

sam["QCD_Pt-15to30_fwdJet_Tune4C_13TeV_pythia8"]={}
sam["QCD_Pt-15to30_fwdJet_Tune4C_13TeV_pythia8"]["sgeJobs"]=80
sam["QCD_Pt-15to30_fwdJet_Tune4C_13TeV_pythia8"]["crabJobs"]=470
sam["QCD_Pt-15to30_fwdJet_Tune4C_13TeV_pythia8"]["GT"]='START42_V16::All'
sam["QCD_Pt-15to30_fwdJet_Tune4C_13TeV_pythia8"]["weightJet15"]='RooFormulaVar("weight","weight", "xsOverEvents*puWeightJet15V4*trgWeightJet15RawTF2*trgWeightJet15L1RawTF2", RooArgList(v["puWeightJet15V4"]["RooVar"],v["trgWeightJet15RawTF2"]["RooVar"],v["trgWeightJet15L1RawTF2"]["RooVar"]))'
sam["QCD_Pt-15to30_fwdJet_Tune4C_13TeV_pythia8"]["name"]='QCD_Pt-15to30_fwdJet_Tune4C_13TeV_pythia8'
sam["QCD_Pt-15to30_fwdJet_Tune4C_13TeV_pythia8"]["isData"]=False
sam["QCD_Pt-15to30_fwdJet_Tune4C_13TeV_pythia8"]["weightPuOnly"]='RooFormulaVar("weight","weight", "xsOverEvents*puWeightJet15V4", RooArgList(v["puWeightJet15V4"]["RooVar"]))'
sam["QCD_Pt-15to30_fwdJet_Tune4C_13TeV_pythia8"]["weightJet15Inverse"]='RooFormulaVar("weight","weight", "xsOverEvents*puWeightJet15V4", RooArgList(v["puWeightJet15V4"]["RooVar"]))'
sam["QCD_Pt-15to30_fwdJet_Tune4C_13TeV_pythia8"]["numEvents"]=-1
sam["QCD_Pt-15to30_fwdJet_Tune4C_13TeV_pythia8"]["lumiJet15"]='crashMeMC'
sam["QCD_Pt-15to30_fwdJet_Tune4C_13TeV_pythia8"]["weightNoPu"]='RooFormulaVar("weight","weight", "xsOverEvents", RooArgList())'
sam["QCD_Pt-15to30_fwdJet_Tune4C_13TeV_pythia8"]["json"]=''
sam["QCD_Pt-15to30_fwdJet_Tune4C_13TeV_pythia8"]["lumiDiJet15FB"]='crashMeMC'
sam["QCD_Pt-15to30_fwdJet_Tune4C_13TeV_pythia8"]["pathTrees"]='/XXXTMFTTree/store/user/fruboes/QCD_Pt-15to30_fwdJet_Tune4C_13TeV_pythia8/DiJet_20140903_PU20FWDMC_QCD_Pt-15to30_fwdJet_Tune4C_13TeV_pythia8/ad312982f9c229126c0b740d5fced447//'
sam["QCD_Pt-15to30_fwdJet_Tune4C_13TeV_pythia8"]["XS"]=550302000.0
sam["QCD_Pt-15to30_fwdJet_Tune4C_13TeV_pythia8"]["pathPAT"]='/XXXTMFPAT/store/user/fruboes/QCD_Pt-15to30_fwdJet_Tune4C_13TeV_pythia8/DiJet_20140903_PU20FWDMC_QCD_Pt-15to30_fwdJet_Tune4C_13TeV_pythia8/ad312982f9c229126c0b740d5fced447//'
sam["QCD_Pt-15to30_fwdJet_Tune4C_13TeV_pythia8"]["pathSE"]='srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=/pnfs/desy.de/cms/tier2/store/user/fruboes/QCD_Pt-15to30_fwdJet_Tune4C_13TeV_pythia8/DiJet_20140903_PU20FWDMC_QCD_Pt-15to30_fwdJet_Tune4C_13TeV_pythia8/ad312982f9c229126c0b740d5fced447/'
sam["QCD_Pt-15to30_fwdJet_Tune4C_13TeV_pythia8"]["DS"]='/QCD_Pt-15to30_fwdJet_Tune4C_13TeV_pythia8/Spring14dr-castor_PU20bx25_POSTLS170_V5-v1/AODSIM'

sam["QCD_Pt-170toInf_fwdJet_Tune4C_13TeV_pythia8"]={}
sam["QCD_Pt-170toInf_fwdJet_Tune4C_13TeV_pythia8"]["sgeJobs"]=80
sam["QCD_Pt-170toInf_fwdJet_Tune4C_13TeV_pythia8"]["crabJobs"]=470
sam["QCD_Pt-170toInf_fwdJet_Tune4C_13TeV_pythia8"]["GT"]='START42_V16::All'
sam["QCD_Pt-170toInf_fwdJet_Tune4C_13TeV_pythia8"]["weightJet15"]='RooFormulaVar("weight","weight", "xsOverEvents*puWeightJet15V4*trgWeightJet15RawTF2*trgWeightJet15L1RawTF2", RooArgList(v["puWeightJet15V4"]["RooVar"],v["trgWeightJet15RawTF2"]["RooVar"],v["trgWeightJet15L1RawTF2"]["RooVar"]))'
sam["QCD_Pt-170toInf_fwdJet_Tune4C_13TeV_pythia8"]["name"]='QCD_Pt-170toInf_fwdJet_Tune4C_13TeV_pythia8'
sam["QCD_Pt-170toInf_fwdJet_Tune4C_13TeV_pythia8"]["isData"]=False
sam["QCD_Pt-170toInf_fwdJet_Tune4C_13TeV_pythia8"]["weightPuOnly"]='RooFormulaVar("weight","weight", "xsOverEvents*puWeightJet15V4", RooArgList(v["puWeightJet15V4"]["RooVar"]))'
sam["QCD_Pt-170toInf_fwdJet_Tune4C_13TeV_pythia8"]["weightJet15Inverse"]='RooFormulaVar("weight","weight", "xsOverEvents*puWeightJet15V4", RooArgList(v["puWeightJet15V4"]["RooVar"]))'
sam["QCD_Pt-170toInf_fwdJet_Tune4C_13TeV_pythia8"]["numEvents"]=-1
sam["QCD_Pt-170toInf_fwdJet_Tune4C_13TeV_pythia8"]["lumiJet15"]='crashMeMC'
sam["QCD_Pt-170toInf_fwdJet_Tune4C_13TeV_pythia8"]["weightNoPu"]='RooFormulaVar("weight","weight", "xsOverEvents", RooArgList())'
sam["QCD_Pt-170toInf_fwdJet_Tune4C_13TeV_pythia8"]["json"]=''
sam["QCD_Pt-170toInf_fwdJet_Tune4C_13TeV_pythia8"]["lumiDiJet15FB"]='crashMeMC'
sam["QCD_Pt-170toInf_fwdJet_Tune4C_13TeV_pythia8"]["pathTrees"]='/XXXTMFTTree/store/user/fruboes/QCD_Pt-170toInf_fwdJet_Tune4C_13TeV_pythia8/DiJet_20140903_PU20FWDMC_QCD_Pt-170toInf_fwdJet_Tune4C_13TeV_pythia8/ad312982f9c229126c0b740d5fced447//'
sam["QCD_Pt-170toInf_fwdJet_Tune4C_13TeV_pythia8"]["XS"]=43444.8
sam["QCD_Pt-170toInf_fwdJet_Tune4C_13TeV_pythia8"]["pathPAT"]='/XXXTMFPAT/store/user/fruboes/QCD_Pt-170toInf_fwdJet_Tune4C_13TeV_pythia8/DiJet_20140903_PU20FWDMC_QCD_Pt-170toInf_fwdJet_Tune4C_13TeV_pythia8/ad312982f9c229126c0b740d5fced447//'
sam["QCD_Pt-170toInf_fwdJet_Tune4C_13TeV_pythia8"]["pathSE"]='srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=/pnfs/desy.de/cms/tier2/store/user/fruboes/QCD_Pt-170toInf_fwdJet_Tune4C_13TeV_pythia8/DiJet_20140903_PU20FWDMC_QCD_Pt-170toInf_fwdJet_Tune4C_13TeV_pythia8/ad312982f9c229126c0b740d5fced447/'
sam["QCD_Pt-170toInf_fwdJet_Tune4C_13TeV_pythia8"]["DS"]='/QCD_Pt-170toInf_fwdJet_Tune4C_13TeV_pythia8/Spring14dr-castor_PU20bx25_POSTLS170_V5-v1/AODSIM'

sam["QCD_Pt-30to50_fwdJet_Tune4C_13TeV_pythia8"]={}
sam["QCD_Pt-30to50_fwdJet_Tune4C_13TeV_pythia8"]["sgeJobs"]=80
sam["QCD_Pt-30to50_fwdJet_Tune4C_13TeV_pythia8"]["crabJobs"]=470
sam["QCD_Pt-30to50_fwdJet_Tune4C_13TeV_pythia8"]["GT"]='START42_V16::All'
sam["QCD_Pt-30to50_fwdJet_Tune4C_13TeV_pythia8"]["weightJet15"]='RooFormulaVar("weight","weight", "xsOverEvents*puWeightJet15V4*trgWeightJet15RawTF2*trgWeightJet15L1RawTF2", RooArgList(v["puWeightJet15V4"]["RooVar"],v["trgWeightJet15RawTF2"]["RooVar"],v["trgWeightJet15L1RawTF2"]["RooVar"]))'
sam["QCD_Pt-30to50_fwdJet_Tune4C_13TeV_pythia8"]["name"]='QCD_Pt-30to50_fwdJet_Tune4C_13TeV_pythia8'
sam["QCD_Pt-30to50_fwdJet_Tune4C_13TeV_pythia8"]["isData"]=False
sam["QCD_Pt-30to50_fwdJet_Tune4C_13TeV_pythia8"]["weightPuOnly"]='RooFormulaVar("weight","weight", "xsOverEvents*puWeightJet15V4", RooArgList(v["puWeightJet15V4"]["RooVar"]))'
sam["QCD_Pt-30to50_fwdJet_Tune4C_13TeV_pythia8"]["weightJet15Inverse"]='RooFormulaVar("weight","weight", "xsOverEvents*puWeightJet15V4", RooArgList(v["puWeightJet15V4"]["RooVar"]))'
sam["QCD_Pt-30to50_fwdJet_Tune4C_13TeV_pythia8"]["numEvents"]=-1
sam["QCD_Pt-30to50_fwdJet_Tune4C_13TeV_pythia8"]["lumiJet15"]='crashMeMC'
sam["QCD_Pt-30to50_fwdJet_Tune4C_13TeV_pythia8"]["weightNoPu"]='RooFormulaVar("weight","weight", "xsOverEvents", RooArgList())'
sam["QCD_Pt-30to50_fwdJet_Tune4C_13TeV_pythia8"]["json"]=''
sam["QCD_Pt-30to50_fwdJet_Tune4C_13TeV_pythia8"]["lumiDiJet15FB"]='crashMeMC'
sam["QCD_Pt-30to50_fwdJet_Tune4C_13TeV_pythia8"]["pathTrees"]='/XXXTMFTTree/store/user/fruboes/QCD_Pt-30to50_fwdJet_Tune4C_13TeV_pythia8/DiJet_20140903_PU20FWDMC_QCD_Pt-30to50_fwdJet_Tune4C_13TeV_pythia8/ad312982f9c229126c0b740d5fced447//'
sam["QCD_Pt-30to50_fwdJet_Tune4C_13TeV_pythia8"]["XS"]=65892000.0
sam["QCD_Pt-30to50_fwdJet_Tune4C_13TeV_pythia8"]["pathPAT"]='/XXXTMFPAT/store/user/fruboes/QCD_Pt-30to50_fwdJet_Tune4C_13TeV_pythia8/DiJet_20140903_PU20FWDMC_QCD_Pt-30to50_fwdJet_Tune4C_13TeV_pythia8/ad312982f9c229126c0b740d5fced447//'
sam["QCD_Pt-30to50_fwdJet_Tune4C_13TeV_pythia8"]["pathSE"]='srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=/pnfs/desy.de/cms/tier2/store/user/fruboes/QCD_Pt-30to50_fwdJet_Tune4C_13TeV_pythia8/DiJet_20140903_PU20FWDMC_QCD_Pt-30to50_fwdJet_Tune4C_13TeV_pythia8/ad312982f9c229126c0b740d5fced447/'
sam["QCD_Pt-30to50_fwdJet_Tune4C_13TeV_pythia8"]["DS"]='/QCD_Pt-30to50_fwdJet_Tune4C_13TeV_pythia8/Spring14dr-castor_PU20bx25_POSTLS170_V5-v1/AODSIM'

sam["QCD_Pt-50to80_fwdJet_Tune4C_13TeV_pythia8"]={}
sam["QCD_Pt-50to80_fwdJet_Tune4C_13TeV_pythia8"]["sgeJobs"]=80
sam["QCD_Pt-50to80_fwdJet_Tune4C_13TeV_pythia8"]["crabJobs"]=470
sam["QCD_Pt-50to80_fwdJet_Tune4C_13TeV_pythia8"]["GT"]='START42_V16::All'
sam["QCD_Pt-50to80_fwdJet_Tune4C_13TeV_pythia8"]["weightJet15"]='RooFormulaVar("weight","weight", "xsOverEvents*puWeightJet15V4*trgWeightJet15RawTF2*trgWeightJet15L1RawTF2", RooArgList(v["puWeightJet15V4"]["RooVar"],v["trgWeightJet15RawTF2"]["RooVar"],v["trgWeightJet15L1RawTF2"]["RooVar"]))'
sam["QCD_Pt-50to80_fwdJet_Tune4C_13TeV_pythia8"]["name"]='QCD_Pt-50to80_fwdJet_Tune4C_13TeV_pythia8'
sam["QCD_Pt-50to80_fwdJet_Tune4C_13TeV_pythia8"]["isData"]=False
sam["QCD_Pt-50to80_fwdJet_Tune4C_13TeV_pythia8"]["weightPuOnly"]='RooFormulaVar("weight","weight", "xsOverEvents*puWeightJet15V4", RooArgList(v["puWeightJet15V4"]["RooVar"]))'
sam["QCD_Pt-50to80_fwdJet_Tune4C_13TeV_pythia8"]["weightJet15Inverse"]='RooFormulaVar("weight","weight", "xsOverEvents*puWeightJet15V4", RooArgList(v["puWeightJet15V4"]["RooVar"]))'
sam["QCD_Pt-50to80_fwdJet_Tune4C_13TeV_pythia8"]["numEvents"]=-1
sam["QCD_Pt-50to80_fwdJet_Tune4C_13TeV_pythia8"]["lumiJet15"]='crashMeMC'
sam["QCD_Pt-50to80_fwdJet_Tune4C_13TeV_pythia8"]["weightNoPu"]='RooFormulaVar("weight","weight", "xsOverEvents", RooArgList())'
sam["QCD_Pt-50to80_fwdJet_Tune4C_13TeV_pythia8"]["json"]=''
sam["QCD_Pt-50to80_fwdJet_Tune4C_13TeV_pythia8"]["lumiDiJet15FB"]='crashMeMC'
sam["QCD_Pt-50to80_fwdJet_Tune4C_13TeV_pythia8"]["pathTrees"]='/XXXTMFTTree/store/user/fruboes/QCD_Pt-50to80_fwdJet_Tune4C_13TeV_pythia8/DiJet_20140903_PU20FWDMC_QCD_Pt-50to80_fwdJet_Tune4C_13TeV_pythia8/ad312982f9c229126c0b740d5fced447//'
sam["QCD_Pt-50to80_fwdJet_Tune4C_13TeV_pythia8"]["XS"]=8932440.0
sam["QCD_Pt-50to80_fwdJet_Tune4C_13TeV_pythia8"]["pathPAT"]='/XXXTMFPAT/store/user/fruboes/QCD_Pt-50to80_fwdJet_Tune4C_13TeV_pythia8/DiJet_20140903_PU20FWDMC_QCD_Pt-50to80_fwdJet_Tune4C_13TeV_pythia8/ad312982f9c229126c0b740d5fced447//'
sam["QCD_Pt-50to80_fwdJet_Tune4C_13TeV_pythia8"]["pathSE"]='srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=/pnfs/desy.de/cms/tier2/store/user/fruboes/QCD_Pt-50to80_fwdJet_Tune4C_13TeV_pythia8/DiJet_20140903_PU20FWDMC_QCD_Pt-50to80_fwdJet_Tune4C_13TeV_pythia8/ad312982f9c229126c0b740d5fced447/'
sam["QCD_Pt-50to80_fwdJet_Tune4C_13TeV_pythia8"]["DS"]='/QCD_Pt-50to80_fwdJet_Tune4C_13TeV_pythia8/Spring14dr-castor_PU20bx25_POSTLS170_V5-v1/AODSIM'

sam["QCD_Pt-80to120_fwdJet_Tune4C_13TeV_pythia8"]={}
sam["QCD_Pt-80to120_fwdJet_Tune4C_13TeV_pythia8"]["sgeJobs"]=80
sam["QCD_Pt-80to120_fwdJet_Tune4C_13TeV_pythia8"]["crabJobs"]=470
sam["QCD_Pt-80to120_fwdJet_Tune4C_13TeV_pythia8"]["GT"]='START42_V16::All'
sam["QCD_Pt-80to120_fwdJet_Tune4C_13TeV_pythia8"]["weightJet15"]='RooFormulaVar("weight","weight", "xsOverEvents*puWeightJet15V4*trgWeightJet15RawTF2*trgWeightJet15L1RawTF2", RooArgList(v["puWeightJet15V4"]["RooVar"],v["trgWeightJet15RawTF2"]["RooVar"],v["trgWeightJet15L1RawTF2"]["RooVar"]))'
sam["QCD_Pt-80to120_fwdJet_Tune4C_13TeV_pythia8"]["name"]='QCD_Pt-80to120_fwdJet_Tune4C_13TeV_pythia8'
sam["QCD_Pt-80to120_fwdJet_Tune4C_13TeV_pythia8"]["isData"]=False
sam["QCD_Pt-80to120_fwdJet_Tune4C_13TeV_pythia8"]["weightPuOnly"]='RooFormulaVar("weight","weight", "xsOverEvents*puWeightJet15V4", RooArgList(v["puWeightJet15V4"]["RooVar"]))'
sam["QCD_Pt-80to120_fwdJet_Tune4C_13TeV_pythia8"]["weightJet15Inverse"]='RooFormulaVar("weight","weight", "xsOverEvents*puWeightJet15V4", RooArgList(v["puWeightJet15V4"]["RooVar"]))'
sam["QCD_Pt-80to120_fwdJet_Tune4C_13TeV_pythia8"]["numEvents"]=-1
sam["QCD_Pt-80to120_fwdJet_Tune4C_13TeV_pythia8"]["lumiJet15"]='crashMeMC'
sam["QCD_Pt-80to120_fwdJet_Tune4C_13TeV_pythia8"]["weightNoPu"]='RooFormulaVar("weight","weight", "xsOverEvents", RooArgList())'
sam["QCD_Pt-80to120_fwdJet_Tune4C_13TeV_pythia8"]["json"]=''
sam["QCD_Pt-80to120_fwdJet_Tune4C_13TeV_pythia8"]["lumiDiJet15FB"]='crashMeMC'
sam["QCD_Pt-80to120_fwdJet_Tune4C_13TeV_pythia8"]["pathTrees"]='/XXXTMFTTree/store/user/fruboes/QCD_Pt-80to120_fwdJet_Tune4C_13TeV_pythia8/DiJet_20140903_PU20FWDMC_QCD_Pt-80to120_fwdJet_Tune4C_13TeV_pythia8/ad312982f9c229126c0b740d5fced447//'
sam["QCD_Pt-80to120_fwdJet_Tune4C_13TeV_pythia8"]["XS"]=1146688.0
sam["QCD_Pt-80to120_fwdJet_Tune4C_13TeV_pythia8"]["pathPAT"]='/XXXTMFPAT/store/user/fruboes/QCD_Pt-80to120_fwdJet_Tune4C_13TeV_pythia8/DiJet_20140903_PU20FWDMC_QCD_Pt-80to120_fwdJet_Tune4C_13TeV_pythia8/ad312982f9c229126c0b740d5fced447//'
sam["QCD_Pt-80to120_fwdJet_Tune4C_13TeV_pythia8"]["pathSE"]='srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=/pnfs/desy.de/cms/tier2/store/user/fruboes/QCD_Pt-80to120_fwdJet_Tune4C_13TeV_pythia8/DiJet_20140903_PU20FWDMC_QCD_Pt-80to120_fwdJet_Tune4C_13TeV_pythia8/ad312982f9c229126c0b740d5fced447/'
sam["QCD_Pt-80to120_fwdJet_Tune4C_13TeV_pythia8"]["DS"]='/QCD_Pt-80to120_fwdJet_Tune4C_13TeV_pythia8/Spring14dr-castor_PU20bx25_POSTLS170_V5-v1/AODSIM'

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
