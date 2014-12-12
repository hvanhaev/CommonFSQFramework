anaVersion="DiJet_20141118_MN2010"
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

rootPath="/scratch/scratch0/tfruboes/DATA_dijet/DiJet_20141118_MN2010/"
sam = {}

sam["Jet-Run2010B-Apr21ReReco-v1"]={}
sam["Jet-Run2010B-Apr21ReReco-v1"]["sgeJobs"]=50
sam["Jet-Run2010B-Apr21ReReco-v1"]["crabJobs"]=470
sam["Jet-Run2010B-Apr21ReReco-v1"]["GT"]='GR_R_42_V19::All'
sam["Jet-Run2010B-Apr21ReReco-v1"]["name"]='Jet-Run2010B-Apr21ReReco-v1'
sam["Jet-Run2010B-Apr21ReReco-v1"]["isData"]=True
sam["Jet-Run2010B-Apr21ReReco-v1"]["weightJet15Inverse"]='RooFormulaVar("weight","weight", "invtrgWeightJet15RawTF2", RooArgList(v["invtrgWeightJet15RawTF2"]["RooVar"]))'
sam["Jet-Run2010B-Apr21ReReco-v1"]["numEvents"]=-1
sam["Jet-Run2010B-Apr21ReReco-v1"]["lumiJet15"]=0.0033470000000000001
sam["Jet-Run2010B-Apr21ReReco-v1"]["pathTrees"]='/XXXTMFTTree/store/user/fruboes/Jet/DiJet_20141118_MN2010_Jet-Run2010B-Apr21ReReco-v1/ea84a565e6d543ec1406ecd18c3abd3e//'
sam["Jet-Run2010B-Apr21ReReco-v1"]["json"]='MNTriggerStudies/MNTriggerAna/lumi/Cert_136033-149442_7TeV_Apr21ReReco_Collisions10_JSON_v2.txt'
sam["Jet-Run2010B-Apr21ReReco-v1"]["lumiDiJet15FB"]='crashMe'
sam["Jet-Run2010B-Apr21ReReco-v1"]["XS"]=-1
sam["Jet-Run2010B-Apr21ReReco-v1"]["pathPAT"]='/XXXTMFPAT/store/user/fruboes/Jet/DiJet_20141118_MN2010_Jet-Run2010B-Apr21ReReco-v1/ea84a565e6d543ec1406ecd18c3abd3e//'
sam["Jet-Run2010B-Apr21ReReco-v1"]["pathSE"]='srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=/pnfs/desy.de/cms/tier2/store/user/fruboes/Jet/DiJet_20141118_MN2010_Jet-Run2010B-Apr21ReReco-v1/ea84a565e6d543ec1406ecd18c3abd3e/'
sam["Jet-Run2010B-Apr21ReReco-v1"]["DS"]='/Jet/Run2010B-Apr21ReReco-v1/AOD'

sam["JetMET-Run2010A-Apr21ReReco-v1"]={}
sam["JetMET-Run2010A-Apr21ReReco-v1"]["sgeJobs"]=50
sam["JetMET-Run2010A-Apr21ReReco-v1"]["crabJobs"]=470
sam["JetMET-Run2010A-Apr21ReReco-v1"]["GT"]='GR_R_42_V19::All'
sam["JetMET-Run2010A-Apr21ReReco-v1"]["name"]='JetMET-Run2010A-Apr21ReReco-v1'
sam["JetMET-Run2010A-Apr21ReReco-v1"]["isData"]=True
sam["JetMET-Run2010A-Apr21ReReco-v1"]["weightJet15Inverse"]='RooFormulaVar("weight","weight", "invtrgWeightJet15RawTF2", RooArgList(v["invtrgWeightJet15RawTF2"]["RooVar"]))'
sam["JetMET-Run2010A-Apr21ReReco-v1"]["numEvents"]=-1
sam["JetMET-Run2010A-Apr21ReReco-v1"]["lumiJet15"]=0.0095250000000000005
sam["JetMET-Run2010A-Apr21ReReco-v1"]["pathTrees"]='/XXXTMFTTree/store/user/fruboes/JetMET/DiJet_20141118_MN2010_JetMET-Run2010A-Apr21ReReco-v1/ea84a565e6d543ec1406ecd18c3abd3e//'
sam["JetMET-Run2010A-Apr21ReReco-v1"]["json"]='MNTriggerStudies/MNTriggerAna/lumi/Cert_136033-149442_7TeV_Apr21ReReco_Collisions10_JSON_v2.txt'
sam["JetMET-Run2010A-Apr21ReReco-v1"]["lumiDiJet15FB"]=2.8380000000000001
sam["JetMET-Run2010A-Apr21ReReco-v1"]["XS"]=-1
sam["JetMET-Run2010A-Apr21ReReco-v1"]["pathPAT"]='/XXXTMFPAT/store/user/fruboes/JetMET/DiJet_20141118_MN2010_JetMET-Run2010A-Apr21ReReco-v1/ea84a565e6d543ec1406ecd18c3abd3e//'
sam["JetMET-Run2010A-Apr21ReReco-v1"]["pathSE"]='srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=/pnfs/desy.de/cms/tier2/store/user/fruboes/JetMET/DiJet_20141118_MN2010_JetMET-Run2010A-Apr21ReReco-v1/ea84a565e6d543ec1406ecd18c3abd3e/'
sam["JetMET-Run2010A-Apr21ReReco-v1"]["DS"]='/JetMET/Run2010A-Apr21ReReco-v1/AOD'

sam["JetMETTau-Run2010A-Apr21ReReco-v1"]={}
sam["JetMETTau-Run2010A-Apr21ReReco-v1"]["sgeJobs"]=50
sam["JetMETTau-Run2010A-Apr21ReReco-v1"]["crabJobs"]=470
sam["JetMETTau-Run2010A-Apr21ReReco-v1"]["GT"]='GR_R_42_V19::All'
sam["JetMETTau-Run2010A-Apr21ReReco-v1"]["name"]='JetMETTau-Run2010A-Apr21ReReco-v1'
sam["JetMETTau-Run2010A-Apr21ReReco-v1"]["isData"]=True
sam["JetMETTau-Run2010A-Apr21ReReco-v1"]["weightJet15Inverse"]='RooFormulaVar("weight","weight", "invtrgWeightJet15RawTF2", RooArgList(v["invtrgWeightJet15RawTF2"]["RooVar"]))'
sam["JetMETTau-Run2010A-Apr21ReReco-v1"]["numEvents"]=-1
sam["JetMETTau-Run2010A-Apr21ReReco-v1"]["lumiJet15"]=0.013781
sam["JetMETTau-Run2010A-Apr21ReReco-v1"]["pathTrees"]='/XXXTMFTTree/store/user/fruboes/JetMETTau/DiJet_20141118_MN2010_JetMETTau-Run2010A-Apr21ReReco-v1/ea84a565e6d543ec1406ecd18c3abd3e//'
sam["JetMETTau-Run2010A-Apr21ReReco-v1"]["json"]='MNTriggerStudies/MNTriggerAna/lumi/Cert_136033-149442_7TeV_Apr21ReReco_Collisions10_JSON_v2.txt'
sam["JetMETTau-Run2010A-Apr21ReReco-v1"]["lumiDiJet15FB"]=0.28277400000000003
sam["JetMETTau-Run2010A-Apr21ReReco-v1"]["XS"]=-1
sam["JetMETTau-Run2010A-Apr21ReReco-v1"]["pathPAT"]='/XXXTMFPAT/store/user/fruboes/JetMETTau/DiJet_20141118_MN2010_JetMETTau-Run2010A-Apr21ReReco-v1/ea84a565e6d543ec1406ecd18c3abd3e//'
sam["JetMETTau-Run2010A-Apr21ReReco-v1"]["pathSE"]='srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=/pnfs/desy.de/cms/tier2/store/user/fruboes/JetMETTau/DiJet_20141118_MN2010_JetMETTau-Run2010A-Apr21ReReco-v1/ea84a565e6d543ec1406ecd18c3abd3e/'
sam["JetMETTau-Run2010A-Apr21ReReco-v1"]["DS"]='/JetMETTau/Run2010A-Apr21ReReco-v1/AOD'

sam["QCD_Pt-15to1000_TuneEE3C_Flat_7TeV_herwigpp"]={}
sam["QCD_Pt-15to1000_TuneEE3C_Flat_7TeV_herwigpp"]["sgeJobs"]=80
sam["QCD_Pt-15to1000_TuneEE3C_Flat_7TeV_herwigpp"]["crabJobs"]=115
sam["QCD_Pt-15to1000_TuneEE3C_Flat_7TeV_herwigpp"]["GT"]='START42_V16::All'
sam["QCD_Pt-15to1000_TuneEE3C_Flat_7TeV_herwigpp"]["weightJet15"]='RooFormulaVar("weight","weight", "xsOverEvents*puWeightJet15V4*trgWeightJet15RawTF2*trgWeightJet15L1RawTF2", RooArgList(v["puWeightJet15V4"]["RooVar"],v["trgWeightJet15RawTF2"]["RooVar"],v["trgWeightJet15L1RawTF2"]["RooVar"]))'
sam["QCD_Pt-15to1000_TuneEE3C_Flat_7TeV_herwigpp"]["name"]='QCD_Pt-15to1000_TuneEE3C_Flat_7TeV_herwigpp'
sam["QCD_Pt-15to1000_TuneEE3C_Flat_7TeV_herwigpp"]["isData"]=False
sam["QCD_Pt-15to1000_TuneEE3C_Flat_7TeV_herwigpp"]["weightPuOnly"]='RooFormulaVar("weight","weight", "xsOverEvents*puWeightJet15V4", RooArgList(v["puWeightJet15V4"]["RooVar"]))'
sam["QCD_Pt-15to1000_TuneEE3C_Flat_7TeV_herwigpp"]["weightJet15Inverse"]='RooFormulaVar("weight","weight", "xsOverEvents*puWeightJet15V4", RooArgList(v["puWeightJet15V4"]["RooVar"]))'
sam["QCD_Pt-15to1000_TuneEE3C_Flat_7TeV_herwigpp"]["numEvents"]=-1
sam["QCD_Pt-15to1000_TuneEE3C_Flat_7TeV_herwigpp"]["lumiJet15"]='crashMeMC'
sam["QCD_Pt-15to1000_TuneEE3C_Flat_7TeV_herwigpp"]["weightNoPu"]='RooFormulaVar("weight","weight", "xsOverEvents", RooArgList())'
sam["QCD_Pt-15to1000_TuneEE3C_Flat_7TeV_herwigpp"]["json"]=''
sam["QCD_Pt-15to1000_TuneEE3C_Flat_7TeV_herwigpp"]["lumiDiJet15FB"]='crashMeMC'
sam["QCD_Pt-15to1000_TuneEE3C_Flat_7TeV_herwigpp"]["pathTrees"]='/XXXTMFTTree/store/user/fruboes/QCD_Pt-15to1000_TuneEE3C_Flat_7TeV_herwigpp/DiJet_20141118_MN2010_QCD_Pt-15to1000_TuneEE3C_Flat_7TeV_herwigpp/572122135bb11777c94e0f696205d6fb//'
sam["QCD_Pt-15to1000_TuneEE3C_Flat_7TeV_herwigpp"]["XS"]=16953200000.0
sam["QCD_Pt-15to1000_TuneEE3C_Flat_7TeV_herwigpp"]["pathPAT"]='/XXXTMFPAT/store/user/fruboes/QCD_Pt-15to1000_TuneEE3C_Flat_7TeV_herwigpp/DiJet_20141118_MN2010_QCD_Pt-15to1000_TuneEE3C_Flat_7TeV_herwigpp/572122135bb11777c94e0f696205d6fb//'
sam["QCD_Pt-15to1000_TuneEE3C_Flat_7TeV_herwigpp"]["pathSE"]='srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=/pnfs/desy.de/cms/tier2/store/user/fruboes/QCD_Pt-15to1000_TuneEE3C_Flat_7TeV_herwigpp/DiJet_20141118_MN2010_QCD_Pt-15to1000_TuneEE3C_Flat_7TeV_herwigpp/572122135bb11777c94e0f696205d6fb/'
sam["QCD_Pt-15to1000_TuneEE3C_Flat_7TeV_herwigpp"]["DS"]='/QCD_Pt-15to1000_TuneEE3C_Flat_7TeV_herwigpp/Summer12-LowPU2010_DR42_BS2011_PU_S0_START42_V17B-v1/AODSIM'

sam["Jet-Run2010B-Apr21ReReco-v1-JEC16Full"]={}
sam["Jet-Run2010B-Apr21ReReco-v1-JEC16Full"]["sgeJobs"]=50
sam["Jet-Run2010B-Apr21ReReco-v1-JEC16Full"]["crabJobs"]=115
sam["Jet-Run2010B-Apr21ReReco-v1-JEC16Full"]["GT"]='GR_R_42_V19::All'
sam["Jet-Run2010B-Apr21ReReco-v1-JEC16Full"]["name"]='Jet-Run2010B-Apr21ReReco-v1'
sam["Jet-Run2010B-Apr21ReReco-v1-JEC16Full"]["isData"]=True
sam["Jet-Run2010B-Apr21ReReco-v1-JEC16Full"]["weightJet15Inverse"]='RooFormulaVar("weight","weight", "invtrgWeightJet15RawTF2", RooArgList(v["invtrgWeightJet15RawTF2"]["RooVar"]))'
sam["Jet-Run2010B-Apr21ReReco-v1-JEC16Full"]["numEvents"]=-1
sam["Jet-Run2010B-Apr21ReReco-v1-JEC16Full"]["lumiJet15"]=0.0033470000000000001
sam["Jet-Run2010B-Apr21ReReco-v1-JEC16Full"]["json"]='MNTriggerStudies/MNTriggerAna/lumi/Cert_136033-149442_7TeV_Apr21ReReco_Collisions10_JSON_v2.txt'
sam["Jet-Run2010B-Apr21ReReco-v1-JEC16Full"]["lumiDiJet15FB"]='crashMe'
sam["Jet-Run2010B-Apr21ReReco-v1-JEC16Full"]["XS"]=-1
sam["Jet-Run2010B-Apr21ReReco-v1-JEC16Full"]["DS"]='/Jet/Run2010B-Apr21ReReco-v1/AOD'

sam["JetMET-Run2010A-Apr21ReReco-v1-JEC16Full"]={}
sam["JetMET-Run2010A-Apr21ReReco-v1-JEC16Full"]["sgeJobs"]=50
sam["JetMET-Run2010A-Apr21ReReco-v1-JEC16Full"]["crabJobs"]=115
sam["JetMET-Run2010A-Apr21ReReco-v1-JEC16Full"]["GT"]='GR_R_42_V19::All'
sam["JetMET-Run2010A-Apr21ReReco-v1-JEC16Full"]["name"]='JetMET-Run2010A-Apr21ReReco-v1'
sam["JetMET-Run2010A-Apr21ReReco-v1-JEC16Full"]["isData"]=True
sam["JetMET-Run2010A-Apr21ReReco-v1-JEC16Full"]["weightJet15Inverse"]='RooFormulaVar("weight","weight", "invtrgWeightJet15RawTF2", RooArgList(v["invtrgWeightJet15RawTF2"]["RooVar"]))'
sam["JetMET-Run2010A-Apr21ReReco-v1-JEC16Full"]["numEvents"]=-1
sam["JetMET-Run2010A-Apr21ReReco-v1-JEC16Full"]["lumiJet15"]=0.0095250000000000005
sam["JetMET-Run2010A-Apr21ReReco-v1-JEC16Full"]["json"]='MNTriggerStudies/MNTriggerAna/lumi/Cert_136033-149442_7TeV_Apr21ReReco_Collisions10_JSON_v2.txt'
sam["JetMET-Run2010A-Apr21ReReco-v1-JEC16Full"]["lumiDiJet15FB"]=2.8380000000000001
sam["JetMET-Run2010A-Apr21ReReco-v1-JEC16Full"]["XS"]=-1
sam["JetMET-Run2010A-Apr21ReReco-v1-JEC16Full"]["DS"]='/JetMET/Run2010A-Apr21ReReco-v1/AOD'

sam["JetMETTau-Run2010A-Apr21ReReco-v1-JEC16Full"]={}
sam["JetMETTau-Run2010A-Apr21ReReco-v1-JEC16Full"]["sgeJobs"]=50
sam["JetMETTau-Run2010A-Apr21ReReco-v1-JEC16Full"]["crabJobs"]=115
sam["JetMETTau-Run2010A-Apr21ReReco-v1-JEC16Full"]["GT"]='GR_R_42_V19::All'
sam["JetMETTau-Run2010A-Apr21ReReco-v1-JEC16Full"]["name"]='JetMETTau-Run2010A-Apr21ReReco-v1'
sam["JetMETTau-Run2010A-Apr21ReReco-v1-JEC16Full"]["isData"]=True
sam["JetMETTau-Run2010A-Apr21ReReco-v1-JEC16Full"]["weightJet15Inverse"]='RooFormulaVar("weight","weight", "invtrgWeightJet15RawTF2", RooArgList(v["invtrgWeightJet15RawTF2"]["RooVar"]))'
sam["JetMETTau-Run2010A-Apr21ReReco-v1-JEC16Full"]["numEvents"]=-1
sam["JetMETTau-Run2010A-Apr21ReReco-v1-JEC16Full"]["lumiJet15"]=0.013781
sam["JetMETTau-Run2010A-Apr21ReReco-v1-JEC16Full"]["json"]='MNTriggerStudies/MNTriggerAna/lumi/Cert_136033-149442_7TeV_Apr21ReReco_Collisions10_JSON_v2.txt'
sam["JetMETTau-Run2010A-Apr21ReReco-v1-JEC16Full"]["lumiDiJet15FB"]=0.28277400000000003
sam["JetMETTau-Run2010A-Apr21ReReco-v1-JEC16Full"]["XS"]=-1
sam["JetMETTau-Run2010A-Apr21ReReco-v1-JEC16Full"]["DS"]='/JetMETTau/Run2010A-Apr21ReReco-v1/AOD'


sam["Jet-Run2010B-Apr21ReReco-v1-JEC16Full"]["pathTrees"]='/XXXTMFTTree/store/user/fruboes/Jet/DiJet_20141118_MN2010_Jet-Run2010B-Apr21ReReco-v1-JEC16Full/39dbed0eff6f23c261ef61260ad17bc8//'
sam["Jet-Run2010B-Apr21ReReco-v1-JEC16Full"]["pathPAT"]='/XXXTMFPAT/store/user/fruboes/Jet/DiJet_20141118_MN2010_Jet-Run2010B-Apr21ReReco-v1-JEC16Full/39dbed0eff6f23c261ef61260ad17bc8//'
sam["Jet-Run2010B-Apr21ReReco-v1-JEC16Full"]["pathSE"]='srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=/pnfs/desy.de/cms/tier2/store/user/fruboes/Jet/DiJet_20141118_MN2010_Jet-Run2010B-Apr21ReReco-v1-JEC16Full/39dbed0eff6f23c261ef61260ad17bc8/'
sam["JetMET-Run2010A-Apr21ReReco-v1-JEC16Full"]["pathTrees"]='/XXXTMFTTree/store/user/fruboes/JetMET/DiJet_20141118_MN2010_JetMET-Run2010A-Apr21ReReco-v1-JEC16Full/39dbed0eff6f23c261ef61260ad17bc8//'
sam["JetMET-Run2010A-Apr21ReReco-v1-JEC16Full"]["pathPAT"]='/XXXTMFPAT/store/user/fruboes/JetMET/DiJet_20141118_MN2010_JetMET-Run2010A-Apr21ReReco-v1-JEC16Full/39dbed0eff6f23c261ef61260ad17bc8//'
sam["JetMET-Run2010A-Apr21ReReco-v1-JEC16Full"]["pathSE"]='srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=/pnfs/desy.de/cms/tier2/store/user/fruboes/JetMET/DiJet_20141118_MN2010_JetMET-Run2010A-Apr21ReReco-v1-JEC16Full/39dbed0eff6f23c261ef61260ad17bc8/'
sam["JetMETTau-Run2010A-Apr21ReReco-v1-JEC16Full"]["pathTrees"]='/XXXTMFTTree/store/user/fruboes/JetMETTau/DiJet_20141118_MN2010_JetMETTau-Run2010A-Apr21ReReco-v1-JEC16Full/39dbed0eff6f23c261ef61260ad17bc8//'
sam["JetMETTau-Run2010A-Apr21ReReco-v1-JEC16Full"]["pathPAT"]='/XXXTMFPAT/store/user/fruboes/JetMETTau/DiJet_20141118_MN2010_JetMETTau-Run2010A-Apr21ReReco-v1-JEC16Full/39dbed0eff6f23c261ef61260ad17bc8//'
sam["JetMETTau-Run2010A-Apr21ReReco-v1-JEC16Full"]["pathSE"]='srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=/pnfs/desy.de/cms/tier2/store/user/fruboes/JetMETTau/DiJet_20141118_MN2010_JetMETTau-Run2010A-Apr21ReReco-v1-JEC16Full/39dbed0eff6f23c261ef61260ad17bc8/'



sam["Jet-Run2010B-Apr21ReReco-v1-V16TFPartV2"]={}
sam["Jet-Run2010B-Apr21ReReco-v1-V16TFPartV2"]["sgeJobs"]=50
sam["Jet-Run2010B-Apr21ReReco-v1-V16TFPartV2"]["crabJobs"]=115
sam["Jet-Run2010B-Apr21ReReco-v1-V16TFPartV2"]["GT"]='GR_R_42_V19::All'
sam["Jet-Run2010B-Apr21ReReco-v1-V16TFPartV2"]["name"]='Jet-Run2010B-Apr21ReReco-v1'
sam["Jet-Run2010B-Apr21ReReco-v1-V16TFPartV2"]["isData"]=True
sam["Jet-Run2010B-Apr21ReReco-v1-V16TFPartV2"]["weightJet15Inverse"]='RooFormulaVar("weight","weight", "invtrgWeightJet15RawTF2", RooArgList(v["invtrgWeightJet15RawTF2"]["RooVar"]))'
sam["Jet-Run2010B-Apr21ReReco-v1-V16TFPartV2"]["numEvents"]=-1
sam["Jet-Run2010B-Apr21ReReco-v1-V16TFPartV2"]["lumiJet15"]=0.0033470000000000001
sam["Jet-Run2010B-Apr21ReReco-v1-V16TFPartV2"]["json"]='MNTriggerStudies/MNTriggerAna/lumi/Cert_136033-149442_7TeV_Apr21ReReco_Collisions10_JSON_v2.txt'
sam["Jet-Run2010B-Apr21ReReco-v1-V16TFPartV2"]["lumiDiJet15FB"]='crashMe'
sam["Jet-Run2010B-Apr21ReReco-v1-V16TFPartV2"]["XS"]=-1
sam["Jet-Run2010B-Apr21ReReco-v1-V16TFPartV2"]["DS"]='/Jet/Run2010B-Apr21ReReco-v1/AOD'

sam["JetMET-Run2010A-Apr21ReReco-v1-V16TFPartV2"]={}
sam["JetMET-Run2010A-Apr21ReReco-v1-V16TFPartV2"]["sgeJobs"]=50
sam["JetMET-Run2010A-Apr21ReReco-v1-V16TFPartV2"]["crabJobs"]=115
sam["JetMET-Run2010A-Apr21ReReco-v1-V16TFPartV2"]["GT"]='GR_R_42_V19::All'
sam["JetMET-Run2010A-Apr21ReReco-v1-V16TFPartV2"]["name"]='JetMET-Run2010A-Apr21ReReco-v1'
sam["JetMET-Run2010A-Apr21ReReco-v1-V16TFPartV2"]["isData"]=True
sam["JetMET-Run2010A-Apr21ReReco-v1-V16TFPartV2"]["weightJet15Inverse"]='RooFormulaVar("weight","weight", "invtrgWeightJet15RawTF2", RooArgList(v["invtrgWeightJet15RawTF2"]["RooVar"]))'
sam["JetMET-Run2010A-Apr21ReReco-v1-V16TFPartV2"]["numEvents"]=-1
sam["JetMET-Run2010A-Apr21ReReco-v1-V16TFPartV2"]["lumiJet15"]=0.0095250000000000005
sam["JetMET-Run2010A-Apr21ReReco-v1-V16TFPartV2"]["json"]='MNTriggerStudies/MNTriggerAna/lumi/Cert_136033-149442_7TeV_Apr21ReReco_Collisions10_JSON_v2.txt'
sam["JetMET-Run2010A-Apr21ReReco-v1-V16TFPartV2"]["lumiDiJet15FB"]=2.8380000000000001
sam["JetMET-Run2010A-Apr21ReReco-v1-V16TFPartV2"]["XS"]=-1
sam["JetMET-Run2010A-Apr21ReReco-v1-V16TFPartV2"]["DS"]='/JetMET/Run2010A-Apr21ReReco-v1/AOD'

sam["JetMETTau-Run2010A-Apr21ReReco-v1-V16TFPartV2"]={}
sam["JetMETTau-Run2010A-Apr21ReReco-v1-V16TFPartV2"]["sgeJobs"]=50
sam["JetMETTau-Run2010A-Apr21ReReco-v1-V16TFPartV2"]["crabJobs"]=115
sam["JetMETTau-Run2010A-Apr21ReReco-v1-V16TFPartV2"]["GT"]='GR_R_42_V19::All'
sam["JetMETTau-Run2010A-Apr21ReReco-v1-V16TFPartV2"]["name"]='JetMETTau-Run2010A-Apr21ReReco-v1'
sam["JetMETTau-Run2010A-Apr21ReReco-v1-V16TFPartV2"]["isData"]=True
sam["JetMETTau-Run2010A-Apr21ReReco-v1-V16TFPartV2"]["weightJet15Inverse"]='RooFormulaVar("weight","weight", "invtrgWeightJet15RawTF2", RooArgList(v["invtrgWeightJet15RawTF2"]["RooVar"]))'
sam["JetMETTau-Run2010A-Apr21ReReco-v1-V16TFPartV2"]["numEvents"]=-1
sam["JetMETTau-Run2010A-Apr21ReReco-v1-V16TFPartV2"]["lumiJet15"]=0.013781
sam["JetMETTau-Run2010A-Apr21ReReco-v1-V16TFPartV2"]["json"]='MNTriggerStudies/MNTriggerAna/lumi/Cert_136033-149442_7TeV_Apr21ReReco_Collisions10_JSON_v2.txt'
sam["JetMETTau-Run2010A-Apr21ReReco-v1-V16TFPartV2"]["lumiDiJet15FB"]=0.28277400000000003
sam["JetMETTau-Run2010A-Apr21ReReco-v1-V16TFPartV2"]["XS"]=-1
sam["JetMETTau-Run2010A-Apr21ReReco-v1-V16TFPartV2"]["DS"]='/JetMETTau/Run2010A-Apr21ReReco-v1/AOD'


sam["Jet-Run2010B-Apr21ReReco-v1-V16TFPartV2"]["pathTrees"]='/XXXTMFTTree/store/user/fruboes/Jet/DiJet_20141118_MN2010_Jet-Run2010B-Apr21ReReco-v1-V16TFPartV2/9e683e6bb14029aff8e86a85149cf327//'
sam["Jet-Run2010B-Apr21ReReco-v1-V16TFPartV2"]["pathPAT"]='/XXXTMFPAT/store/user/fruboes/Jet/DiJet_20141118_MN2010_Jet-Run2010B-Apr21ReReco-v1-V16TFPartV2/9e683e6bb14029aff8e86a85149cf327//'
sam["Jet-Run2010B-Apr21ReReco-v1-V16TFPartV2"]["pathSE"]='srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=/pnfs/desy.de/cms/tier2/store/user/fruboes/Jet/DiJet_20141118_MN2010_Jet-Run2010B-Apr21ReReco-v1-V16TFPartV2/9e683e6bb14029aff8e86a85149cf327/'
sam["JetMET-Run2010A-Apr21ReReco-v1-V16TFPartV2"]["pathTrees"]='/XXXTMFTTree/store/user/fruboes/JetMET/DiJet_20141118_MN2010_JetMET-Run2010A-Apr21ReReco-v1-V16TFPartV2/9e683e6bb14029aff8e86a85149cf327//'
sam["JetMET-Run2010A-Apr21ReReco-v1-V16TFPartV2"]["pathPAT"]='/XXXTMFPAT/store/user/fruboes/JetMET/DiJet_20141118_MN2010_JetMET-Run2010A-Apr21ReReco-v1-V16TFPartV2/9e683e6bb14029aff8e86a85149cf327//'
sam["JetMET-Run2010A-Apr21ReReco-v1-V16TFPartV2"]["pathSE"]='srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=/pnfs/desy.de/cms/tier2/store/user/fruboes/JetMET/DiJet_20141118_MN2010_JetMET-Run2010A-Apr21ReReco-v1-V16TFPartV2/9e683e6bb14029aff8e86a85149cf327/'
sam["JetMETTau-Run2010A-Apr21ReReco-v1-V16TFPartV2"]["pathTrees"]='/XXXTMFTTree/store/user/fruboes/JetMETTau/DiJet_20141118_MN2010_JetMETTau-Run2010A-Apr21ReReco-v1-V16TFPartV2/9e683e6bb14029aff8e86a85149cf327//'
sam["JetMETTau-Run2010A-Apr21ReReco-v1-V16TFPartV2"]["pathPAT"]='/XXXTMFPAT/store/user/fruboes/JetMETTau/DiJet_20141118_MN2010_JetMETTau-Run2010A-Apr21ReReco-v1-V16TFPartV2/9e683e6bb14029aff8e86a85149cf327//'
sam["JetMETTau-Run2010A-Apr21ReReco-v1-V16TFPartV2"]["pathSE"]='srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=/pnfs/desy.de/cms/tier2/store/user/fruboes/JetMETTau/DiJet_20141118_MN2010_JetMETTau-Run2010A-Apr21ReReco-v1-V16TFPartV2/9e683e6bb14029aff8e86a85149cf327/'


#'''
knownExtraTags = ["-JEC16Full", "-V16TFPartV2"]
extraTag = "-JEC16Full"
#extraTag = "-V16TFPartV2"
#extraTag = ""

samOrg = sam
sam = {}
for s in samOrg:
    cp = True
    if "QCD" not in s:
        if extraTag:
            if extraTag not in s:
                cp = False
        else:
            for k in knownExtraTags:
                if k in s:
                    cp = False

    print cp, s
    if cp:
        newName = s
        if extraTag:
            newName = newName.replace(extraTag, "")
        sam[newName] = samOrg[s]
print sam.keys()
#'''



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
