anaVersion="Run2015A_B0T_lowPU_withNewcastorMC"
anaType="Run2015A_B0T_lowPU"

cbSmartCommand="smartCopy"
cbSmartBlackList=""
cbWMS="https://wmscms.cern.ch:7443/glite_wms_wmproxy_server"
skimEfficiencyMethod="getSkimEff"

sam = {}

######################################################
## Samples with new CASTOR simulation and alignment ##
######################################################

sam["MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORmeasured"]={}
sam["MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORmeasured"]["crabJobs"]=99
sam["MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORmeasured"]["GT"]='76X_mcRun2_asymptotic_v14'
sam["MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORmeasured"]["name"]='MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORmeasured'
sam["MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORmeasured"]["isData"]=False
sam["MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORmeasured"]["numEvents"]=4917500
sam["MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORmeasured"]["pathSE"]='srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=/pnfs/desy.de/cms/tier2/store/user/sbaur/MinBias_CUETP8M1_13TeV-pythia8/MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORmeasured_CFF/160210_103222/0000/'
sam["MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORmeasured"]["pathTrees"]='/XXXTMFTTree/store/user/sbaur/MinBias_CUETP8M1_13TeV-pythia8/MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORmeasured_CFF/160210_103222/0000/'
sam["MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORmeasured"]["json"]=''
sam["MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORmeasured"]["lumiMinBias"]=6.88821963860484642e-05
sam["MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORmeasured"]["XS"]=71.39e+09
sam["MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORmeasured"]["pathPAT"]='/XXXTMFPAT/store/user/sbaur/MinBias_CUETP8M1_13TeV-pythia8/MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORmeasured_CFF/160210_103222/0000/'
sam["MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORmeasured"]["DS"]='/MinBias_CUETP8M1_13TeV-pythia8/sbaur-MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORmeasured_RECO-ea75752f65bd25232845285a23f93f6b/USER'

sam["MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORsystPlus"]={}
sam["MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORsystPlus"]["crabJobs"]=13
sam["MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORsystPlus"]["GT"]='76X_mcRun2_asymptotic_v14'
sam["MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORsystPlus"]["name"]='MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORsystPlus'
sam["MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORsystPlus"]["isData"]=False
sam["MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORsystPlus"]["numEvents"]=960000
sam["MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORsystPlus"]["pathSE"]='srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=/pnfs/desy.de/cms/tier2/store/user/sbaur/MinBias_CUETP8M1_13TeV-pythia8/MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORsystPlus_CFF/160210_161831/0000/'
sam["MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORsystPlus"]["pathTrees"]='/XXXTMFTTree/store/user/sbaur/MinBias_CUETP8M1_13TeV-pythia8/MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORsystPlus_CFF/160210_161831/0000/'
sam["MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORsystPlus"]["json"]=''
sam["MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORsystPlus"]["lumiMinBias"]=1.34472615212214589e-05
sam["MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORsystPlus"]["XS"]=71.39e+09
sam["MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORsystPlus"]["pathPAT"]='/XXXTMFPAT/store/user/sbaur/MinBias_CUETP8M1_13TeV-pythia8/MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORsystPlus_CFF/160210_161831/0000/'
sam["MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORsystPlus"]["DS"]='/MinBias_CUETP8M1_13TeV-pythia8/katkov-MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORsystPlus_RECO-ea75752f65bd25232845285a23f93f6b/USER'

sam["MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORsystMinus"]={}
sam["MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORsystMinus"]["crabJobs"]=14
sam["MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORsystMinus"]["GT"]='76X_mcRun2_asymptotic_v14'
sam["MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORsystMinus"]["name"]='MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORsystMinus'
sam["MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORsystMinus"]["isData"]=False
sam["MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORsystMinus"]["numEvents"]=980000
sam["MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORsystMinus"]["pathSE"]='srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=/pnfs/desy.de/cms/tier2/store/user/sbaur/MinBias_CUETP8M1_13TeV-pythia8/MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORsystMinus_CFF/160210_161855/0000/'
sam["MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORsystMinus"]["pathTrees"]='/XXXTMFTTree/store/user/sbaur/MinBias_CUETP8M1_13TeV-pythia8/MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORsystMinus_CFF/160210_161855/0000/'
sam["MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORsystMinus"]["json"]=''
sam["MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORsystMinus"]["lumiMinBias"]=1.37274128029135739e-05
sam["MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORsystMinus"]["XS"]=71.39e+09
sam["MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORsystMinus"]["pathPAT"]='/XXXTMFPAT/store/user/sbaur/MinBias_CUETP8M1_13TeV-pythia8/MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORsystMinus_CFF/160210_161855/0000/'
sam["MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORsystMinus"]["DS"]='/MinBias_CUETP8M1_13TeV-pythia8/katkov-MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORsystMinus_RECO-ea75752f65bd25232845285a23f93f6b/USER'

sam["MinBias_TuneMBR_13TeV-pythia8_MagnetOff_CASTORmeasured"]={}
sam["MinBias_TuneMBR_13TeV-pythia8_MagnetOff_CASTORmeasured"]["crabJobs"]=65
sam["MinBias_TuneMBR_13TeV-pythia8_MagnetOff_CASTORmeasured"]["GT"]='76X_mcRun2_asymptotic_v14'
sam["MinBias_TuneMBR_13TeV-pythia8_MagnetOff_CASTORmeasured"]["name"]='MinBias_TuneMBR_13TeV-pythia8_MagnetOff_CASTORmeasured'
sam["MinBias_TuneMBR_13TeV-pythia8_MagnetOff_CASTORmeasured"]["isData"]=False
sam["MinBias_TuneMBR_13TeV-pythia8_MagnetOff_CASTORmeasured"]["numEvents"]=4862000
sam["MinBias_TuneMBR_13TeV-pythia8_MagnetOff_CASTORmeasured"]["pathSE"]='srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=/pnfs/desy.de/cms/tier2/store/user/sbaur/MinBias_TuneMBR_13TeV-pythia8/MinBias_TuneMBR_13TeV-pythia8_MagnetOff_CASTORmeasured_CFF/160210_182150/0000/'
sam["MinBias_TuneMBR_13TeV-pythia8_MagnetOff_CASTORmeasured"]["pathTrees"]='/XXXTMFTTree/store/user/sbaur/MinBias_TuneMBR_13TeV-pythia8/MinBias_TuneMBR_13TeV-pythia8_MagnetOff_CASTORmeasured_CFF/160210_182150/0000/'
sam["MinBias_TuneMBR_13TeV-pythia8_MagnetOff_CASTORmeasured"]["json"]=''
sam["MinBias_TuneMBR_13TeV-pythia8_MagnetOff_CASTORmeasured"]["lumiMinBias"]=6.20007549248645671e-05
sam["MinBias_TuneMBR_13TeV-pythia8_MagnetOff_CASTORmeasured"]["XS"]=78418400000.0
sam["MinBias_TuneMBR_13TeV-pythia8_MagnetOff_CASTORmeasured"]["pathPAT"]='/XXXTMFPAT/store/user/sbaur/MinBias_TuneMBR_13TeV-pythia8/MinBias_TuneMBR_13TeV-pythia8_MagnetOff_CASTORmeasured_CFF/160210_182150/0000/'
sam["MinBias_TuneMBR_13TeV-pythia8_MagnetOff_CASTORmeasured"]["DS"]='/MinBias_TuneMBR_13TeV-pythia8/sbaur-MinBias_TuneMBR_13TeV-pythia8_MagnetOff_CASTORmeasured_RECO-ea75752f65bd25232845285a23f93f6b/USER'

sam["MinBias_EPOS_13TeV_MagnetOff_CASTORmeasured"]={}
sam["MinBias_EPOS_13TeV_MagnetOff_CASTORmeasured"]["crabJobs"]=65
sam["MinBias_EPOS_13TeV_MagnetOff_CASTORmeasured"]["GT"]='76X_mcRun2_asymptotic_v14'
sam["MinBias_EPOS_13TeV_MagnetOff_CASTORmeasured"]["name"]='MinBias_EPOS_13TeV_MagnetOff_CASTORmeasured'
sam["MinBias_EPOS_13TeV_MagnetOff_CASTORmeasured"]["isData"]=False
sam["MinBias_EPOS_13TeV_MagnetOff_CASTORmeasured"]["numEvents"]=4978400
sam["MinBias_EPOS_13TeV_MagnetOff_CASTORmeasured"]["pathSE"]='srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=/pnfs/desy.de/cms/tier2/store/user/sbaur/MinBias_EPOS_13TeV/MinBias_EPOS_13TeV_MagnetOff_CASTORmeasured_CFF/160321_104938/0000/'
sam["MinBias_EPOS_13TeV_MagnetOff_CASTORmeasured"]["pathTrees"]='/XXXTMFTTree/store/user/sbaur/MinBias_EPOS_13TeV/MinBias_EPOS_13TeV_MagnetOff_CASTORmeasured_CFF/160321_104938/0000/'
sam["MinBias_EPOS_13TeV_MagnetOff_CASTORmeasured"]["json"]=''
sam["MinBias_EPOS_13TeV_MagnetOff_CASTORmeasured"]["lumiMinBias"]=-1
sam["MinBias_EPOS_13TeV_MagnetOff_CASTORmeasured"]["XS"]=-1
sam["MinBias_EPOS_13TeV_MagnetOff_CASTORmeasured"]["pathPAT"]='/XXXTMFPAT/store/user/sbaur/MinBias_EPOS_13TeV/MinBias_EPOS_13TeV_MagnetOff_CASTORmeasured_CFF/160321_104938/0000/'
sam["MinBias_EPOS_13TeV_MagnetOff_CASTORmeasured"]["DS"]=' /MinBias_EPOS_13TeV/sbaur-MinBias_EPOS_13TeV_MagnetOff_CASTORmeasured_RECO-ea75752f65bd25232845285a23f93f6b/USER'

sam["CastorJet_10GeV_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORmeasured"]={}
sam["CastorJet_10GeV_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORmeasured"]["crabJobs"]=17
sam["CastorJet_10GeV_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORmeasured"]["GT"]='76X_mcRun2_asymptotic_v14'
sam["CastorJet_10GeV_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORmeasured"]["name"]='CastorJet_10GeV_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORmeasured'
sam["CastorJet_10GeV_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORmeasured"]["isData"]=False
sam["CastorJet_10GeV_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORmeasured"]["numEvents"]=1128742
sam["CastorJet_10GeV_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORmeasured"]["pathSE"]='srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=/pnfs/desy.de/cms/tier2/store/user/sbaur/CASTORJet_CUETP8M1_13TeV-pythia8/CASTORJet_10GeV_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORmeasured_CFF/160211_104245/0000/'
sam["CastorJet_10GeV_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORmeasured"]["pathTrees"]='/XXXTMFTTree/store/user/sbaur/CASTORJet_CUETP8M1_13TeV-pythia8/CASTORJet_10GeV_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORmeasured_CFF/160211_104245/0000/'
sam["CastorJet_10GeV_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORmeasured"]["json"]=''
sam["CastorJet_10GeV_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORmeasured"]["lumiMinBias"]=1.581092589e-05
sam["CastorJet_10GeV_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORmeasured"]["XS"]=71.39e+09
sam["CastorJet_10GeV_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORmeasured"]["pathPAT"]='/XXXTMFPAT/store/user/sbaur/CASTORJet_CUETP8M1_13TeV-pythia8/CASTORJet_10GeV_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORmeasured_CFF/160211_104245/0000/'
sam["CastorJet_10GeV_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORmeasured"]["DS"]='/CASTORJet_CUETP8M1_13TeV-pythia8/cwohrman-CASTORJet_10GeV_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORmeasured_RECO-ea75752f65bd25232845285a23f93f6b/USER'


######################################################
## Samples with Hans Noise fix   ##
######################################################

sam["CUETP8M1_old"]={}
sam["CUETP8M1_old"]["crabJobs"]=0
sam["CUETP8M1_old"]["GT"]='74X_dataRun2_Prompt_v2'
sam["CUETP8M1_old"]["name"]='CUETP8M1_old'
sam["CUETP8M1_old"]["isData"]=False
sam["CUETP8M1_old"]["numEvents"]=-1
sam["CUETP8M1_old"]["pathSE"]='srm://maite.iihe.ac.be:8443/srm/managerv2?SFN=/pnfs/iihe/cms/store/user/hvanhaev/MinBias_CUETP8M1_13TeV-pythia8/MinBias_pythia8_old_v2/160422_114038/0000/'
sam["CUETP8M1_old"]["pathTrees"]='/XXXTMFTTree/store/user/hvanhaev/MinBias_CUETP8M1_13TeV-pythia8/MinBias_pythia8_old_v2/160422_114038/0000//'
sam["CUETP8M1_old"]["json"]=''
sam["CUETP8M1_old"]["lumiMinBias"]=-1
sam["CUETP8M1_old"]["XS"]=-1
sam["CUETP8M1_old"]["pathPAT"]='/XXXTMFPAT/store/user/hvanhaev/MinBias_CUETP8M1_13TeV-pythia8/MinBias_pythia8_old_v2/160422_114038/0000//'
sam["CUETP8M1_old"]["DS"]='/MinBias_CUETP8M1_13TeV-pythia8/hvanhaev-reco_old_v1-7c944757e3469f919dc18c0c33a42956/USER'

sam["CUETP8M1_new"]={}
sam["CUETP8M1_new"]["crabJobs"]=0
sam["CUETP8M1_new"]["GT"]='74X_dataRun2_Prompt_v2'
sam["CUETP8M1_new"]["name"]='CUETP8M1_new'
sam["CUETP8M1_new"]["isData"]=False
sam["CUETP8M1_new"]["numEvents"]=-1
sam["CUETP8M1_new"]["pathSE"]='srm://maite.iihe.ac.be:8443/srm/managerv2?SFN=/pnfs/iihe/cms/store/user/hvanhaev/MinBias_CUETP8M1_13TeV-pythia8/MinBias_pythia8_new_v1/160425_105329/0000/'
sam["CUETP8M1_new"]["pathTrees"]='/XXXTMFTTree/store/user/hvanhaev/MinBias_CUETP8M1_13TeV-pythia8/MinBias_pythia8_new_v1/160425_105329/0000//'
sam["CUETP8M1_new"]["json"]=''
sam["CUETP8M1_new"]["lumiMinBias"]=-1
sam["CUETP8M1_new"]["XS"]=-1
sam["CUETP8M1_new"]["pathPAT"]='/XXXTMFPAT/store/user/hvanhaev/MinBias_CUETP8M1_13TeV-pythia8/MinBias_pythia8_new_v1/160425_105329/0000//'
sam["CUETP8M1_new"]["DS"]='/MinBias_CUETP8M1_13TeV-pythia8/hvanhaev-reco_new_v1-cd17d7dbeddf22a96ea65c7de0f89034/USER'


sam["MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORmeasured_newNoise"]={}
sam["MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORmeasured_newNoise"]["crabJobs"]=99
sam["MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORmeasured_newNoise"]["GT"]='76X_mcRun2_asymptotic_v14'
sam["MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORmeasured_newNoise"]["name"]='MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORmeasured_newNoise'
sam["MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORmeasured_newNoise"]["isData"]=False
sam["MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORmeasured_newNoise"]["numEvents"]=4917500
sam["MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORmeasured_newNoise"]["pathSE"]='srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=/pnfs/desy.de/cms/tier2/store/user/sbaur/MinBias_CUETP8M1_13TeV-pythia8/MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORmeasured_newCASTORnoise_CFF/160513_124612/0000/'
sam["MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORmeasured_newNoise"]["pathTrees"]='/XXXTMFTTree/store/user/sbaur/MinBias_CUETP8M1_13TeV-pythia8/MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORmeasured_newCASTORnoise_CFF/160513_124612/0000/'
sam["MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORmeasured_newNoise"]["json"]=''
sam["MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORmeasured_newNoise"]["lumiMinBias"]=6.88821963860484642e-05
sam["MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORmeasured_newNoise"]["XS"]=71.39e+09
sam["MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORmeasured_newNoise"]["pathPAT"]='/XXXTMFPAT/store/user/sbaur/MinBias_CUETP8M1_13TeV-pythia8/MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORmeasured_newCASTORnoise_CFF/160513_124612/0000/'
sam["MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORmeasured_newNoise"]["DS"]='/MinBias_CUETP8M1_13TeV-pythia8/sbaur-MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORmeasured_newCASTORnoise_RECO-288ab5be9a42aa4a7ffd90fa253c6744/USER'

sam["MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORmeasured_newNoise_newTracking"]={}
sam["MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORmeasured_newNoise_newTracking"]["crabJobs"]=99
sam["MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORmeasured_newNoise_newTracking"]["GT"]='76X_mcRun2_asymptotic_v14'
sam["MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORmeasured_newNoise_newTracking"]["name"]='MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORmeasured_newNoise_newTracking'
sam["MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORmeasured_newNoise_newTracking"]["isData"]=False
sam["MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORmeasured_newNoise_newTracking"]["numEvents"]=4917500
sam["MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORmeasured_newNoise_newTracking"]["pathSE"]='srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=/pnfs/desy.de/cms/tier2/store/user/sbaur/MinBias_CUETP8M1_13TeV-pythia8/MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORmeasured_newCASTORnoise_newTracking_CFF/161021_132723/0000/'
sam["MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORmeasured_newNoise_newTracking"]["pathTrees"]='/XXXTMFTTree/store/user/sbaur/MinBias_CUETP8M1_13TeV-pythia8/MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORmeasured_newCASTORnoise_newTracking_CFF/161021_132723/0000/'
sam["MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORmeasured_newNoise_newTracking"]["json"]=''
sam["MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORmeasured_newNoise_newTracking"]["lumiMinBias"]=6.88821963860484642e-05
sam["MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORmeasured_newNoise_newTracking"]["XS"]=71.39e+09
sam["MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORmeasured_newNoise_newTracking"]["pathPAT"]='/XXXTMFPAT/store/user/sbaur/MinBias_CUETP8M1_13TeV-pythia8/MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORmeasured_newCASTORnoise_newTracking_CFF/161021_132723/0000/'
sam["MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORmeasured_newNoise_newTracking"]["DS"]='/MinBias_CUETP8M1_13TeV-pythia8/sbaur-MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORmeasured_newCASTORnoise_RECO-288ab5be9a42aa4a7ffd90fa253c6744/USER'


sam["MinBias_TuneMBR_13TeV-pythia8_MagnetOff_CASTORmeasured_newNoise"]={}
sam["MinBias_TuneMBR_13TeV-pythia8_MagnetOff_CASTORmeasured_newNoise"]["crabJobs"]=98
sam["MinBias_TuneMBR_13TeV-pythia8_MagnetOff_CASTORmeasured_newNoise"]["GT"]='76X_mcRun2_asymptotic_v14'
sam["MinBias_TuneMBR_13TeV-pythia8_MagnetOff_CASTORmeasured_newNoise"]["name"]='MinBias_TuneMBR_13TeV-pythia8_MagnetOff_CASTORmeasured_newNoise'
sam["MinBias_TuneMBR_13TeV-pythia8_MagnetOff_CASTORmeasured_newNoise"]["isData"]=False
sam["MinBias_TuneMBR_13TeV-pythia8_MagnetOff_CASTORmeasured_newNoise"]["numEvents"]=4862000
sam["MinBias_TuneMBR_13TeV-pythia8_MagnetOff_CASTORmeasured_newNoise"]["pathSE"]='srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=/pnfs/desy.de/cms/tier2/store/user/sbaur/MinBias_TuneMBR_13TeV-pythia8/MinBias_TuneMBR_13TeV-pythia8_MagnetOff_CASTORmeasured_newCASTORnoise_CFF_2/160610_100853/0000/'
sam["MinBias_TuneMBR_13TeV-pythia8_MagnetOff_CASTORmeasured_newNoise"]["pathTrees"]='/XXXTMFTTree/store/user/sbaur/MinBias_TuneMBR_13TeV-pythia8/MinBias_TuneMBR_13TeV-pythia8_MagnetOff_CASTORmeasured_newCASTORnoise_CFF_2/160610_100853/0000/'
sam["MinBias_TuneMBR_13TeV-pythia8_MagnetOff_CASTORmeasured_newNoise"]["json"]=''
sam["MinBias_TuneMBR_13TeV-pythia8_MagnetOff_CASTORmeasured_newNoise"]["lumiMinBias"]=6.20007549248645671e-05
sam["MinBias_TuneMBR_13TeV-pythia8_MagnetOff_CASTORmeasured_newNoise"]["XS"]=78418400000.0
sam["MinBias_TuneMBR_13TeV-pythia8_MagnetOff_CASTORmeasured_newNoise"]["pathPAT"]='/XXXTMFPAT/store/user/sbaur/MinBias_TuneMBR_13TeV-pythia8/MinBias_TuneMBR_13TeV-pythia8_MagnetOff_CASTORmeasured_newCASTORnoise_CFF_2/160610_100853/0000/'
sam["MinBias_TuneMBR_13TeV-pythia8_MagnetOff_CASTORmeasured_newNoise"]["DS"]='/MinBias_TuneMBR_13TeV-pythia8/sbaur-MinBias_TuneMBR_13TeV-pythia8_MagnetOff_CASTORmeasured_newCASTORnoise_fix_RECO-288ab5be9a42aa4a7ffd90fa253c6744/USER'

sam["MinBias_EPOS_13TeV_MagnetOff_CASTORmeasured_newNoise"]={}
sam["MinBias_EPOS_13TeV_MagnetOff_CASTORmeasured_newNoise"]["crabJobs"]=100
sam["MinBias_EPOS_13TeV_MagnetOff_CASTORmeasured_newNoise"]["GT"]='76X_mcRun2_asymptotic_v14'
sam["MinBias_EPOS_13TeV_MagnetOff_CASTORmeasured_newNoise"]["name"]='MinBias_EPOS_13TeV_MagnetOff_CASTORmeasured_newNoise'
sam["MinBias_EPOS_13TeV_MagnetOff_CASTORmeasured_newNoise"]["isData"]=False
sam["MinBias_EPOS_13TeV_MagnetOff_CASTORmeasured_newNoise"]["numEvents"]=4978400
sam["MinBias_EPOS_13TeV_MagnetOff_CASTORmeasured_newNoise"]["pathSE"]='srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=/pnfs/desy.de/cms/tier2/store/user/sbaur/MinBias_EPOS_13TeV/MinBias_EPOS_13TeV_MagnetOff_CASTORmeasured_newCASTORnoise_CFF/160518_072336/0000/'
sam["MinBias_EPOS_13TeV_MagnetOff_CASTORmeasured_newNoise"]["pathTrees"]='/XXXTMFTTree/store/user/sbaur/MinBias_EPOS_13TeV/MinBias_EPOS_13TeV_MagnetOff_CASTORmeasured_newCASTORnoise_CFF/160518_072336/0000/'
sam["MinBias_EPOS_13TeV_MagnetOff_CASTORmeasured_newNoise"]["json"]=''
sam["MinBias_EPOS_13TeV_MagnetOff_CASTORmeasured_newNoise"]["lumiMinBias"]=-1
sam["MinBias_EPOS_13TeV_MagnetOff_CASTORmeasured_newNoise"]["XS"]=-1
sam["MinBias_EPOS_13TeV_MagnetOff_CASTORmeasured_newNoise"]["pathPAT"]='/XXXTMFPAT/store/user/sbaur/MinBias_EPOS_13TeV/MinBias_EPOS_13TeV_MagnetOff_CASTORmeasured_newCASTORnoise_CFF/160518_072336'
sam["MinBias_EPOS_13TeV_MagnetOff_CASTORmeasured_newNoise"]["DS"]='/MinBias_EPOS_13TeV/sbaur-MinBias_EPOS_13TeV_MagnetOff_CASTORmeasured_newCASTORnoise_RECO-288ab5be9a42aa4a7ffd90fa253c6744/USER'

######################################################
## Samples with old CASTOR simulation and alignment ##
######################################################

sam["MinBias_TuneEE5C_13TeV-herwigpp_MagnetOff"]={}
sam["MinBias_TuneEE5C_13TeV-herwigpp_MagnetOff"]["crabJobs"]=10
sam["MinBias_TuneEE5C_13TeV-herwigpp_MagnetOff"]["GT"]='MCRUN2_740TV0'
sam["MinBias_TuneEE5C_13TeV-herwigpp_MagnetOff"]["name"]='MinBias_TuneEE5C_13TeV-herwigpp_MagnetOff'
sam["MinBias_TuneEE5C_13TeV-herwigpp_MagnetOff"]["isData"]=False
sam["MinBias_TuneEE5C_13TeV-herwigpp_MagnetOff"]["numEvents"]=997682
sam["MinBias_TuneEE5C_13TeV-herwigpp_MagnetOff"]["pathSE"]='srm://maite.iihe.ac.be:8443/srm/managerv2?SFN=/pnfs/iihe/cms/store/user/hvanhaev/MinBias_TuneEE5C_13TeV-herwigpp/Run2015A_B0T_lowPU_14102015_MinBias_TuneEE5C_13TeV-herwigpp_MagnetOff/151014_225628/0000/'
sam["MinBias_TuneEE5C_13TeV-herwigpp_MagnetOff"]["pathTrees"]='/XXXTMFTTree/store/user/hvanhaev/MinBias_TuneEE5C_13TeV-herwigpp/Run2015A_B0T_lowPU_14102015_MinBias_TuneEE5C_13TeV-herwigpp_MagnetOff/151014_225628/0000//'
sam["MinBias_TuneEE5C_13TeV-herwigpp_MagnetOff"]["json"]=''
sam["MinBias_TuneEE5C_13TeV-herwigpp_MagnetOff"]["lumiMinBias"]=2.7363741086121776e-05
sam["MinBias_TuneEE5C_13TeV-herwigpp_MagnetOff"]["XS"]=36460000000.0
sam["MinBias_TuneEE5C_13TeV-herwigpp_MagnetOff"]["pathPAT"]='/XXXTMFPAT/store/user/hvanhaev/MinBias_TuneEE5C_13TeV-herwigpp/Run2015A_B0T_lowPU_14102015_MinBias_TuneEE5C_13TeV-herwigpp_MagnetOff/151014_225628/0000//'
sam["MinBias_TuneEE5C_13TeV-herwigpp_MagnetOff"]["DS"]='/MinBias_TuneEE5C_13TeV-herwigpp/RunIISpring15DR74-NoPU0TRawReco_magnetOff_MCRUN2_740TV0-v1/GEN-SIM-RECO'

sam["MinBias_TuneMBR_13TeV-pythia8_MagnetOff"]={}
sam["MinBias_TuneMBR_13TeV-pythia8_MagnetOff"]["crabJobs"]=10
sam["MinBias_TuneMBR_13TeV-pythia8_MagnetOff"]["GT"]='MCRUN2_740TV0'
sam["MinBias_TuneMBR_13TeV-pythia8_MagnetOff"]["name"]='MinBias_TuneMBR_13TeV-pythia8_MagnetOff'
sam["MinBias_TuneMBR_13TeV-pythia8_MagnetOff"]["isData"]=False
sam["MinBias_TuneMBR_13TeV-pythia8_MagnetOff"]["numEvents"]=997146
sam["MinBias_TuneMBR_13TeV-pythia8_MagnetOff"]["pathSE"]='srm://maite.iihe.ac.be:8443/srm/managerv2?SFN=/pnfs/iihe/cms/store/user/hvanhaev/MinBias_TuneMBR_13TeV-pythia8/Run2015A_B0T_lowPU_14102015_MinBias_TuneMBR_13TeV-pythia8_MagnetOff/151014_225721/0000/'
sam["MinBias_TuneMBR_13TeV-pythia8_MagnetOff"]["pathTrees"]='/XXXTMFTTree/store/user/hvanhaev/MinBias_TuneMBR_13TeV-pythia8/Run2015A_B0T_lowPU_14102015_MinBias_TuneMBR_13TeV-pythia8_MagnetOff/151014_225721/0000//'
sam["MinBias_TuneMBR_13TeV-pythia8_MagnetOff"]["json"]=''
sam["MinBias_TuneMBR_13TeV-pythia8_MagnetOff"]["lumiMinBias"]=1.271571467920794e-05
sam["MinBias_TuneMBR_13TeV-pythia8_MagnetOff"]["XS"]=78418400000.0
sam["MinBias_TuneMBR_13TeV-pythia8_MagnetOff"]["pathPAT"]='/XXXTMFPAT/store/user/hvanhaev/MinBias_TuneMBR_13TeV-pythia8/Run2015A_B0T_lowPU_14102015_MinBias_TuneMBR_13TeV-pythia8_MagnetOff/151014_225721/0000//'
sam["MinBias_TuneMBR_13TeV-pythia8_MagnetOff"]["DS"]='/MinBias_TuneMBR_13TeV-pythia8/RunIISpring15DR74-NoPU0TRawReco_magnetOff_MCRUN2_740TV0-v1/GEN-SIM-RECO'

sam["MinBias_TuneMonash13_13TeV-pythia8_MagnetOff"]={}
sam["MinBias_TuneMonash13_13TeV-pythia8_MagnetOff"]["crabJobs"]=10
sam["MinBias_TuneMonash13_13TeV-pythia8_MagnetOff"]["GT"]='MCRUN2_740TV0'
sam["MinBias_TuneMonash13_13TeV-pythia8_MagnetOff"]["name"]='MinBias_TuneMonash13_13TeV-pythia8_MagnetOff'
sam["MinBias_TuneMonash13_13TeV-pythia8_MagnetOff"]["isData"]=False
sam["MinBias_TuneMonash13_13TeV-pythia8_MagnetOff"]["numEvents"]=953393
sam["MinBias_TuneMonash13_13TeV-pythia8_MagnetOff"]["pathSE"]='srm://maite.iihe.ac.be:8443/srm/managerv2?SFN=/pnfs/iihe/cms/store/user/hvanhaev/MinBias_TuneMonash13_13TeV-pythia8/Run2015A_B0T_lowPU_14102015_MinBias_TuneMonash13_13TeV-pythia8_MagnetOff/151014_225432/0000/'
sam["MinBias_TuneMonash13_13TeV-pythia8_MagnetOff"]["pathTrees"]='/XXXTMFTTree/store/user/hvanhaev/MinBias_TuneMonash13_13TeV-pythia8/Run2015A_B0T_lowPU_14102015_MinBias_TuneMonash13_13TeV-pythia8_MagnetOff/151014_225432/0000//'
sam["MinBias_TuneMonash13_13TeV-pythia8_MagnetOff"]["json"]=''
sam["MinBias_TuneMonash13_13TeV-pythia8_MagnetOff"]["lumiMinBias"]=1.2157771645430154e-05
sam["MinBias_TuneMonash13_13TeV-pythia8_MagnetOff"]["XS"]=78418400000.0
sam["MinBias_TuneMonash13_13TeV-pythia8_MagnetOff"]["pathPAT"]='/XXXTMFPAT/store/user/hvanhaev/MinBias_TuneMonash13_13TeV-pythia8/Run2015A_B0T_lowPU_14102015_MinBias_TuneMonash13_13TeV-pythia8_MagnetOff/151014_225432/0000//'
sam["MinBias_TuneMonash13_13TeV-pythia8_MagnetOff"]["DS"]='/MinBias_TuneMonash13_13TeV-pythia8/RunIISpring15DR74-NoPU0TRawReco_magnetOff_MCRUN2_740TV0-v1/GEN-SIM-RECO'

sam["MinBias_TuneZ2star_13TeV-pythia6_MagnetOff"]={}
sam["MinBias_TuneZ2star_13TeV-pythia6_MagnetOff"]["crabJobs"]=10
sam["MinBias_TuneZ2star_13TeV-pythia6_MagnetOff"]["GT"]='MCRUN2_740TV0'
sam["MinBias_TuneZ2star_13TeV-pythia6_MagnetOff"]["name"]='MinBias_TuneZ2star_13TeV-pythia6_MagnetOff'
sam["MinBias_TuneZ2star_13TeV-pythia6_MagnetOff"]["isData"]=False
sam["MinBias_TuneZ2star_13TeV-pythia6_MagnetOff"]["numEvents"]=998082
sam["MinBias_TuneZ2star_13TeV-pythia6_MagnetOff"]["pathSE"]='srm://maite.iihe.ac.be:8443/srm/managerv2?SFN=/pnfs/iihe/cms/store/user/hvanhaev/MinBias_TuneZ2star_13TeV-pythia6/Run2015A_B0T_lowPU_14102015_MinBias_TuneZ2star_13TeV-pythia6_MagnetOff/151014_225350/0000/'
sam["MinBias_TuneZ2star_13TeV-pythia6_MagnetOff"]["pathTrees"]='/XXXTMFTTree/store/user/hvanhaev/MinBias_TuneZ2star_13TeV-pythia6/Run2015A_B0T_lowPU_14102015_MinBias_TuneZ2star_13TeV-pythia6_MagnetOff/151014_225350/0000//'
sam["MinBias_TuneZ2star_13TeV-pythia6_MagnetOff"]["json"]=''
sam["MinBias_TuneZ2star_13TeV-pythia6_MagnetOff"]["lumiMinBias"]=1.2753411704574495e-05
sam["MinBias_TuneZ2star_13TeV-pythia6_MagnetOff"]["XS"]=78260000000.0
sam["MinBias_TuneZ2star_13TeV-pythia6_MagnetOff"]["pathPAT"]='/XXXTMFPAT/store/user/hvanhaev/MinBias_TuneZ2star_13TeV-pythia6/Run2015A_B0T_lowPU_14102015_MinBias_TuneZ2star_13TeV-pythia6_MagnetOff/151014_225350/0000//'
sam["MinBias_TuneZ2star_13TeV-pythia6_MagnetOff"]["DS"]='/MinBias_TuneZ2star_13TeV-pythia6/RunIISpring15DR74-NoPU0TRawReco_magnetOff_MCRUN2_740TV0-v1/GEN-SIM-RECO'

sam["ReggeGribovPartonMC_13TeV-EPOS_MagnetOff"]={}
sam["ReggeGribovPartonMC_13TeV-EPOS_MagnetOff"]["crabJobs"]=10
sam["ReggeGribovPartonMC_13TeV-EPOS_MagnetOff"]["GT"]='MCRUN2_740TV0'
sam["ReggeGribovPartonMC_13TeV-EPOS_MagnetOff"]["name"]='ReggeGribovPartonMC_13TeV-EPOS_MagnetOff'
sam["ReggeGribovPartonMC_13TeV-EPOS_MagnetOff"]["isData"]=False
sam["ReggeGribovPartonMC_13TeV-EPOS_MagnetOff"]["numEvents"]=998671
sam["ReggeGribovPartonMC_13TeV-EPOS_MagnetOff"]["pathSE"]='srm://maite.iihe.ac.be:8443/srm/managerv2?SFN=/pnfs/iihe/cms/store/user/hvanhaev/ReggeGribovPartonMC_13TeV-EPOS/Run2015A_B0T_lowPU_14102015_ReggeGribovPartonMC_13TeV-EPOS_MagnetOff/151014_225507/0000/'
sam["ReggeGribovPartonMC_13TeV-EPOS_MagnetOff"]["pathTrees"]='/XXXTMFTTree/store/user/hvanhaev/ReggeGribovPartonMC_13TeV-EPOS/Run2015A_B0T_lowPU_14102015_ReggeGribovPartonMC_13TeV-EPOS_MagnetOff/151014_225507/0000//'
sam["ReggeGribovPartonMC_13TeV-EPOS_MagnetOff"]["json"]=''
sam["ReggeGribovPartonMC_13TeV-EPOS_MagnetOff"]["lumiMinBias"]=1.2735161645736204e-05
sam["ReggeGribovPartonMC_13TeV-EPOS_MagnetOff"]["XS"]=78418400000.0
sam["ReggeGribovPartonMC_13TeV-EPOS_MagnetOff"]["pathPAT"]='/XXXTMFPAT/store/user/hvanhaev/ReggeGribovPartonMC_13TeV-EPOS/Run2015A_B0T_lowPU_14102015_ReggeGribovPartonMC_13TeV-EPOS_MagnetOff/151014_225507/0000//'
sam["ReggeGribovPartonMC_13TeV-EPOS_MagnetOff"]["DS"]='/ReggeGribovPartonMC_13TeV-EPOS/RunIISpring15DR74-NoPU0TRawReco_magnetOff_MCRUN2_740TV0-v1/GEN-SIM-RECO'

sam["ReggeGribovPartonMC_13TeV-QGSJetII_MagnetOff"]={}
sam["ReggeGribovPartonMC_13TeV-QGSJetII_MagnetOff"]["crabJobs"]=10
sam["ReggeGribovPartonMC_13TeV-QGSJetII_MagnetOff"]["GT"]='MCRUN2_740TV0'
sam["ReggeGribovPartonMC_13TeV-QGSJetII_MagnetOff"]["name"]='ReggeGribovPartonMC_13TeV-QGSJetII_MagnetOff'
sam["ReggeGribovPartonMC_13TeV-QGSJetII_MagnetOff"]["isData"]=False
sam["ReggeGribovPartonMC_13TeV-QGSJetII_MagnetOff"]["numEvents"]=980585
sam["ReggeGribovPartonMC_13TeV-QGSJetII_MagnetOff"]["pathSE"]='srm://maite.iihe.ac.be:8443/srm/managerv2?SFN=/pnfs/iihe/cms/store/user/hvanhaev/ReggeGribovPartonMC_13TeV-QGSJetII/Run2015A_B0T_lowPU_14102015_ReggeGribovPartonMC_13TeV-QGSJetII_MagnetOff/151014_225544/0000/'
sam["ReggeGribovPartonMC_13TeV-QGSJetII_MagnetOff"]["pathTrees"]='/XXXTMFTTree/store/user/hvanhaev/ReggeGribovPartonMC_13TeV-QGSJetII/Run2015A_B0T_lowPU_14102015_ReggeGribovPartonMC_13TeV-QGSJetII_MagnetOff/151014_225544/0000//'
sam["ReggeGribovPartonMC_13TeV-QGSJetII_MagnetOff"]["json"]=''
sam["ReggeGribovPartonMC_13TeV-QGSJetII_MagnetOff"]["lumiMinBias"]=1.2504526998765596e-05
sam["ReggeGribovPartonMC_13TeV-QGSJetII_MagnetOff"]["XS"]=78418400000.0
sam["ReggeGribovPartonMC_13TeV-QGSJetII_MagnetOff"]["pathPAT"]='/XXXTMFPAT/store/user/hvanhaev/ReggeGribovPartonMC_13TeV-QGSJetII/Run2015A_B0T_lowPU_14102015_ReggeGribovPartonMC_13TeV-QGSJetII_MagnetOff/151014_225544/0000//'
sam["ReggeGribovPartonMC_13TeV-QGSJetII_MagnetOff"]["DS"]='/ReggeGribovPartonMC_13TeV-QGSJetII/RunIISpring15DR74-NoPU0TRawReco_magnetOff_MCRUN2_740TV0-v1/GEN-SIM-RECO'

######################################################
#### Data with new CASTOR conditions #################
######################################################

sam["data_ZeroBias1_latestConditions"]={}
sam["data_ZeroBias1_latestConditions"]["crabJobs"]=0
sam["data_ZeroBias1_latestConditions"]["GT"]='74X_dataRun2_Prompt_v2'
sam["data_ZeroBias1_latestConditions"]["name"]='data_ZeroBias1_latestConditions'
sam["data_ZeroBias1_latestConditions"]["isData"]=True
sam["data_ZeroBias1_latestConditions"]["numEvents"]=-1
sam["data_ZeroBias1_latestConditions"]["json"]='CommonFSQFramework/Skim/lumi/Run2015A_lowPU_B0T.json'
sam["data_ZeroBias1_latestConditions"]["lumiMinBias"]=-1
sam["data_ZeroBias1_latestConditions"]["XS"]=-1
sam["data_ZeroBias1_latestConditions"]["DS"]='/ZeroBias1/hvanhaev-Run2015A-v1_B0T_LowPU_RERECO_74X_dataRun2_Prompt_v2_withCustomCond-v2-5f2ef5d60b472daaeedca9cb4892d16d/USER'
sam["data_ZeroBias1_latestConditions"]["pathPAT"]='/XXXTMFPAT/store/user/sbaur/ZeroBias1/Run2015A_B0T_lowPU_14102015_data_ZeroBias1_latestConditions/151120_160658/0000/'
sam["data_ZeroBias1_latestConditions"]["pathTrees"]='/XXXTMFTTree/store/user/sbaur/ZeroBias1/Run2015A_B0T_lowPU_14102015_data_ZeroBias1_latestConditions/151120_160658/0000/'
sam["data_ZeroBias1_latestConditions"]["pathSE"]='srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=/pnfs/desy.de/cms/tier2/store/user/sbaur/ZeroBias1/Run2015A_B0T_lowPU_14102015_data_ZeroBias1_latestConditions/151120_160658/0000/'


######################################################
#### Data with startup 2015 CASTOR conditions ########
######################################################

sam["data_EmptyBX"]={}
sam["data_EmptyBX"]["crabJobs"]=0
sam["data_EmptyBX"]["GT"]='74X_dataRun2_Prompt_v2'
sam["data_EmptyBX"]["name"]='data_EmptyBX'
sam["data_EmptyBX"]["isData"]=True
sam["data_EmptyBX"]["numEvents"]=-1
sam["data_EmptyBX"]["pathSE"]='srm://maite.iihe.ac.be:8443/srm/managerv2?SFN=/pnfs/iihe/cms/store/user/hvanhaev/EmptyBX/Run2015A_B0T_lowPU_14102015_data_EmptyBX/151014_123304/0000/'
sam["data_EmptyBX"]["pathTrees"]='/XXXTMFTTree/store/user/hvanhaev/EmptyBX/Run2015A_B0T_lowPU_14102015_data_EmptyBX/151014_123304/0000//'
sam["data_EmptyBX"]["json"]='CommonFSQFramework/Skim/lumi/Run2015A_lowPU_B0T_LHCf.json'
sam["data_EmptyBX"]["lumiMinBias"]=-1
sam["data_EmptyBX"]["XS"]=-1
sam["data_EmptyBX"]["pathPAT"]='/XXXTMFPAT/store/user/hvanhaev/EmptyBX/Run2015A_B0T_lowPU_14102015_data_EmptyBX/151014_123304/0000//'
sam["data_EmptyBX"]["DS"]='/EmptyBX/hvanhaev-Run2015A-v1_B0T_LowPU_RERECO_74X_dataRun2_Prompt_v2_withCustomCond-v2-5f2ef5d60b472daaeedca9cb4892d16d/USER'

sam["data_L1TechBPTXMinusOnly"]={}
sam["data_L1TechBPTXMinusOnly"]["crabJobs"]=0
sam["data_L1TechBPTXMinusOnly"]["GT"]='74X_dataRun2_Prompt_v2'
sam["data_L1TechBPTXMinusOnly"]["name"]='data_L1TechBPTXMinusOnly'
sam["data_L1TechBPTXMinusOnly"]["isData"]=True
sam["data_L1TechBPTXMinusOnly"]["numEvents"]=-1
sam["data_L1TechBPTXMinusOnly"]["pathSE"]='srm://maite.iihe.ac.be:8443/srm/managerv2?SFN=/pnfs/iihe/cms/store/user/hvanhaev/L1TechBPTXMinusOnly/Run2015A_B0T_lowPU_14102015_data_L1TechBPTXMinusOnly/151014_123442/0000/'
sam["data_L1TechBPTXMinusOnly"]["pathTrees"]='/XXXTMFTTree/store/user/hvanhaev/L1TechBPTXMinusOnly/Run2015A_B0T_lowPU_14102015_data_L1TechBPTXMinusOnly/151014_123442/0000//'
sam["data_L1TechBPTXMinusOnly"]["json"]='CommonFSQFramework/Skim/lumi/Run2015A_lowPU_B0T_247324.json'
sam["data_L1TechBPTXMinusOnly"]["lumiMinBias"]=-1
sam["data_L1TechBPTXMinusOnly"]["XS"]=-1
sam["data_L1TechBPTXMinusOnly"]["pathPAT"]='/XXXTMFPAT/store/user/hvanhaev/L1TechBPTXMinusOnly/Run2015A_B0T_lowPU_14102015_data_L1TechBPTXMinusOnly/151014_123442/0000//'
sam["data_L1TechBPTXMinusOnly"]["DS"]='/L1TechBPTXMinusOnly/hvanhaev-Run2015A-v1_B0T_LowPU_RERECO_74X_dataRun2_Prompt_v2_withCustomCond-v1-5f2ef5d60b472daaeedca9cb4892d16d/USER'

sam["data_L1TechBPTXPlusOnly"]={}
sam["data_L1TechBPTXPlusOnly"]["crabJobs"]=0
sam["data_L1TechBPTXPlusOnly"]["GT"]='74X_dataRun2_Prompt_v2'
sam["data_L1TechBPTXPlusOnly"]["name"]='data_L1TechBPTXPlusOnly'
sam["data_L1TechBPTXPlusOnly"]["isData"]=True
sam["data_L1TechBPTXPlusOnly"]["numEvents"]=-1
sam["data_L1TechBPTXPlusOnly"]["pathSE"]='srm://maite.iihe.ac.be:8443/srm/managerv2?SFN=/pnfs/iihe/cms/store/user/hvanhaev/L1TechBPTXPlusOnly/Run2015A_B0T_lowPU_14102015_data_L1TechBPTXPlusOnly/151014_123600/0000/'
sam["data_L1TechBPTXPlusOnly"]["pathTrees"]='/XXXTMFTTree/store/user/hvanhaev/L1TechBPTXPlusOnly/Run2015A_B0T_lowPU_14102015_data_L1TechBPTXPlusOnly/151014_123600/0000//'
sam["data_L1TechBPTXPlusOnly"]["json"]='CommonFSQFramework/Skim/lumi/Run2015A_lowPU_B0T_247324.json'
sam["data_L1TechBPTXPlusOnly"]["lumiMinBias"]=-1
sam["data_L1TechBPTXPlusOnly"]["XS"]=-1
sam["data_L1TechBPTXPlusOnly"]["pathPAT"]='/XXXTMFPAT/store/user/hvanhaev/L1TechBPTXPlusOnly/Run2015A_B0T_lowPU_14102015_data_L1TechBPTXPlusOnly/151014_123600/0000//'
sam["data_L1TechBPTXPlusOnly"]["DS"]='/L1TechBPTXPlusOnly/hvanhaev-Run2015A-v1_B0T_LowPU_RERECO_74X_dataRun2_Prompt_v2_withCustomCond-v1-5f2ef5d60b472daaeedca9cb4892d16d/USER'

sam["data_L1TechBPTXQuiet"]={}
sam["data_L1TechBPTXQuiet"]["crabJobs"]=0
sam["data_L1TechBPTXQuiet"]["GT"]='74X_dataRun2_Prompt_v2'
sam["data_L1TechBPTXQuiet"]["name"]='data_L1TechBPTXQuiet'
sam["data_L1TechBPTXQuiet"]["isData"]=True
sam["data_L1TechBPTXQuiet"]["numEvents"]=-1
sam["data_L1TechBPTXQuiet"]["pathSE"]='srm://maite.iihe.ac.be:8443/srm/managerv2?SFN=/pnfs/iihe/cms/store/user/hvanhaev/L1TechBPTXQuiet/Run2015A_B0T_lowPU_14102015_data_L1TechBPTXQuiet/151014_123320/0000/'
sam["data_L1TechBPTXQuiet"]["pathTrees"]='/XXXTMFTTree/store/user/hvanhaev/L1TechBPTXQuiet/Run2015A_B0T_lowPU_14102015_data_L1TechBPTXQuiet/151014_123320/0000//'
sam["data_L1TechBPTXQuiet"]["json"]='CommonFSQFramework/Skim/lumi/Run2015A_lowPU_B0T_247324.json'
sam["data_L1TechBPTXQuiet"]["lumiMinBias"]=-1
sam["data_L1TechBPTXQuiet"]["XS"]=-1
sam["data_L1TechBPTXQuiet"]["pathPAT"]='/XXXTMFPAT/store/user/hvanhaev/L1TechBPTXQuiet/Run2015A_B0T_lowPU_14102015_data_L1TechBPTXQuiet/151014_123320/0000//'
sam["data_L1TechBPTXQuiet"]["DS"]='/L1TechBPTXQuiet/hvanhaev-Run2015A-v1_B0T_LowPU_RERECO_74X_dataRun2_Prompt_v2_withCustomCond-v1-5f2ef5d60b472daaeedca9cb4892d16d/USER'

sam["data_ZeroBias1"]={}
sam["data_ZeroBias1"]["crabJobs"]=0
sam["data_ZeroBias1"]["GT"]='74X_dataRun2_Prompt_v2'
sam["data_ZeroBias1"]["name"]='data_ZeroBias1'
sam["data_ZeroBias1"]["isData"]=True
sam["data_ZeroBias1"]["numEvents"]=-1
sam["data_ZeroBias1"]["pathSE"]='srm://maite.iihe.ac.be:8443/srm/managerv2?SFN=/pnfs/iihe/cms/store/user/hvanhaev/ZeroBias1/Run2015A_B0T_lowPU_14102015_data_ZeroBias1/151014_123458/0000/'
sam["data_ZeroBias1"]["pathTrees"]='/XXXTMFTTree/store/user/hvanhaev/ZeroBias1/Run2015A_B0T_lowPU_14102015_data_ZeroBias1/151014_123458/0000//'
sam["data_ZeroBias1"]["json"]='CommonFSQFramework/Skim/lumi/Run2015A_lowPU_B0T.json'
sam["data_ZeroBias1"]["lumiMinBias"]=-1
sam["data_ZeroBias1"]["XS"]=-1
sam["data_ZeroBias1"]["pathPAT"]='/XXXTMFPAT/store/user/hvanhaev/ZeroBias1/Run2015A_B0T_lowPU_14102015_data_ZeroBias1/151014_123458/0000//'
sam["data_ZeroBias1"]["DS"]='/ZeroBias1/hvanhaev-Run2015A-v1_B0T_LowPU_RERECO_74X_dataRun2_Prompt_v2_withCustomCond-v2-5f2ef5d60b472daaeedca9cb4892d16d/USER'

######################################################
###### Data with Febr 2016 CASTOR conditions #########
######################################################

sam["data_EmptyBX_Feb2016"]={}
sam["data_EmptyBX_Feb2016"]["crabJobs"]=0
sam["data_EmptyBX_Feb2016"]["GT"]='74X_dataRun2_Prompt_v2'
sam["data_EmptyBX_Feb2016"]["name"]='data_EmptyBX_Feb2016'
sam["data_EmptyBX_Feb2016"]["isData"]=True
sam["data_EmptyBX_Feb2016"]["numEvents"]=-1
sam["data_EmptyBX_Feb2016"]["pathSE"]='srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=/pnfs/desy.de/cms/tier2/store/user/sbaur/EmptyBX/EmptyBX-PromptReco_Run2015A_lowPU_intercalibFeb2016/160227_085336/0000/'
sam["data_EmptyBX_Feb2016"]["pathTrees"]='/XXXTMFTTree/store/user/sbaurEmptyBX/EmptyBX-PromptReco_Run2015A_lowPU_intercalibFeb2016/160227_085336/0000/'
sam["data_EmptyBX_Feb2016"]["json"]='CommonFSQFramework/Skim/lumi/Run2015A_lowPU_B0T_LHCf.json'
sam["data_EmptyBX_Feb2016"]["lumiMinBias"]=-1
sam["data_EmptyBX_Feb2016"]["XS"]=-1
sam["data_EmptyBX_Feb2016"]["pathPAT"]='/XXXTMFPAT/store/user/sbaur/EmptyBX/EmptyBX-PromptReco_Run2015A_lowPU_intercalibFeb2016/160227_085336/0000/'
sam["data_EmptyBX_Feb2016"]["DS"]='/EmptyBX/Run2015A-PromptReco-v1/RECO'

sam["data_L1TechBPTXMinusOnly_Feb2016"]={}
sam["data_L1TechBPTXMinusOnly_Feb2016"]["crabJobs"]=0
sam["data_L1TechBPTXMinusOnly_Feb2016"]["GT"]='74X_dataRun2_Prompt_v2'
sam["data_L1TechBPTXMinusOnly_Feb2016"]["name"]='data_L1TechBPTXMinusOnly_Feb2016'
sam["data_L1TechBPTXMinusOnly_Feb2016"]["isData"]=True
sam["data_L1TechBPTXMinusOnly_Feb2016"]["numEvents"]=-1
sam["data_L1TechBPTXMinusOnly_Feb2016"]["pathSE"]='srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=/pnfs/desy.de/cms/tier2/store/user/sbaur/L1TechBPTXMinusOnly/L1TechBPTXMinusOnly-PromptReco_Run2015A_lowPU_intercalibFeb2016/160227_085300/0000/'
sam["data_L1TechBPTXMinusOnly_Feb2016"]["pathTrees"]='/XXXTMFTTree/store/user/sbaur/L1TechBPTXMinusOnly/L1TechBPTXMinusOnly-PromptReco_Run2015A_lowPU_intercalibFeb2016/160227_085300/0000/'
sam["data_L1TechBPTXMinusOnly_Feb2016"]["json"]='CommonFSQFramework/Skim/lumi/Run2015A_lowPU_B0T_247324.json'
sam["data_L1TechBPTXMinusOnly_Feb2016"]["lumiMinBias"]=-1
sam["data_L1TechBPTXMinusOnly_Feb2016"]["XS"]=-1
sam["data_L1TechBPTXMinusOnly_Feb2016"]["pathPAT"]='/XXXTMFPAT/store/user/sbaur/L1TechBPTXMinusOnly/L1TechBPTXMinusOnly-PromptReco_Run2015A_lowPU_intercalibFeb2016/160227_085300/0000/'
sam["data_L1TechBPTXMinusOnly_Feb2016"]["DS"]='/L1TechBPTXMinusOnly/Run2015A-PromptReco-v1/RECO'

sam["data_L1TechBPTXPlusOnly_Feb2016"]={}
sam["data_L1TechBPTXPlusOnly_Feb2016"]["crabJobs"]=0
sam["data_L1TechBPTXPlusOnly_Feb2016"]["GT"]='74X_dataRun2_Prompt_v2'
sam["data_L1TechBPTXPlusOnly_Feb2016"]["name"]='data_L1TechBPTXPlusOnly_Feb2016'
sam["data_L1TechBPTXPlusOnly_Feb2016"]["isData"]=True
sam["data_L1TechBPTXPlusOnly_Feb2016"]["numEvents"]=-1
sam["data_L1TechBPTXPlusOnly_Feb2016"]["pathSE"]='srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=/pnfs/desy.de/cms/tier2/store/user/sbaur/L1TechBPTXPlusOnly/L1TechBPTXPlusOnly-PromptReco_Run2015A_lowPU_intercalibFeb2016/160227_085412/0000'
sam["data_L1TechBPTXPlusOnly_Feb2016"]["pathTrees"]='/XXXTMFTTree/store/user/sbaur/L1TechBPTXPlusOnly/L1TechBPTXPlusOnly-PromptReco_Run2015A_lowPU_intercalibFeb2016/160227_085412/0000/'
sam["data_L1TechBPTXPlusOnly_Feb2016"]["json"]='CommonFSQFramework/Skim/lumi/Run2015A_lowPU_B0T_247324.json'
sam["data_L1TechBPTXPlusOnly_Feb2016"]["lumiMinBias"]=-1
sam["data_L1TechBPTXPlusOnly_Feb2016"]["XS"]=-1
sam["data_L1TechBPTXPlusOnly_Feb2016"]["pathPAT"]='/XXXTMFPAT/store/user/sbaur/L1TechBPTXPlusOnly/L1TechBPTXPlusOnly-PromptReco_Run2015A_lowPU_intercalibFeb2016/160227_085412/0000/'
sam["data_L1TechBPTXPlusOnly_Feb2016"]["DS"]='/L1TechBPTXPlusOnly/Run2015A-PromptReco-v1/RECO'

sam["data_L1TechBPTXQuiet_Feb2016"]={}
sam["data_L1TechBPTXQuiet_Feb2016"]["crabJobs"]=0
sam["data_L1TechBPTXQuiet_Feb2016"]["GT"]='74X_dataRun2_Prompt_v2'
sam["data_L1TechBPTXQuiet_Feb2016"]["name"]='data_L1TechBPTXQuiet'
sam["data_L1TechBPTXQuiet_Feb2016"]["isData"]=True
sam["data_L1TechBPTXQuiet_Feb2016"]["numEvents"]=-1
sam["data_L1TechBPTXQuiet_Feb2016"]["pathSE"]='srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=/pnfs/desy.de/cms/tier2/store/user/sbaur/L1TechBPTXQuiet/L1TechBPTXQuiet-PromptReco_Run2015A_lowPU_intercalibFeb2016/160227_085444/0000/'
sam["data_L1TechBPTXQuiet_Feb2016"]["pathTrees"]='/XXXTMFTTree/store/user/sbaur/L1TechBPTXQuiet/L1TechBPTXQuiet-PromptReco_Run2015A_lowPU_intercalibFeb2016/160227_085444/0000/'
sam["data_L1TechBPTXQuiet_Feb2016"]["json"]='CommonFSQFramework/Skim/lumi/Run2015A_lowPU_B0T_247324.json'
sam["data_L1TechBPTXQuiet_Feb2016"]["lumiMinBias"]=-1
sam["data_L1TechBPTXQuiet_Feb2016"]["XS"]=-1
sam["data_L1TechBPTXQuiet_Feb2016"]["pathPAT"]='/XXXTMFPAT/store/user/sbaur/L1TechBPTXQuiet/L1TechBPTXQuiet-PromptReco_Run2015A_lowPU_intercalibFeb2016/160227_085444/0000/'
sam["data_L1TechBPTXQuiet_Feb2016"]["DS"]='/L1TechBPTXQuiet/Run2015A-PromptReco-v1/RECO'

sam["data_ZeroBias1_Feb2016"]={}
sam["data_ZeroBias1_Feb2016"]["crabJobs"]=0
sam["data_ZeroBias1_Feb2016"]["GT"]='74X_dataRun2_Prompt_v2'
sam["data_ZeroBias1_Feb2016"]["name"]='data_ZeroBias1'
sam["data_ZeroBias1_Feb2016"]["isData"]=True
sam["data_ZeroBias1_Feb2016"]["numEvents"]=-1
sam["data_ZeroBias1_Feb2016"]["pathSE"]='srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=/pnfs/desy.de/cms/tier2/store/user/sbaur/ZeroBias1/ZeroBias-PromptReco_Run2015A_lowPU_intercalibFeb2016/160226_180255/0000/'
sam["data_ZeroBias1_Feb2016"]["pathTrees"]='/XXXTMFTTree/store/user/sbaur/ZeroBias1/ZeroBias-PromptReco_Run2015A_lowPU_intercalibFeb2016/160226_180255/0000/'
sam["data_ZeroBias1_Feb2016"]["json"]='CommonFSQFramework/Skim/lumi/Run2015A_lowPU_B0T.json'
sam["data_ZeroBias1_Feb2016"]["lumiMinBias"]=-1
sam["data_ZeroBias1_Feb2016"]["XS"]=-1
sam["data_ZeroBias1_Feb2016"]["pathPAT"]='/XXXTMFPAT/store/user/sbaur/ZeroBias1/ZeroBias-PromptReco_Run2015A_lowPU_intercalibFeb2016/160226_180255/0000/'
sam["data_ZeroBias1_Feb2016"]["DS"]='/ZeroBias1/Run2015A-PromptReco-v1/RECO'

##################################################
###### dN/deta Run ###############################
##################################################

sam["data_L1TechBPTXMinusOnly_Feb2016_dNdeta"]={}
sam["data_L1TechBPTXMinusOnly_Feb2016_dNdeta"]["crabJobs"]=0
sam["data_L1TechBPTXMinusOnly_Feb2016_dNdeta"]["GT"]='74X_dataRun2_Prompt_v2'
sam["data_L1TechBPTXMinusOnly_Feb2016_dNdeta"]["name"]='data_L1TechBPTXMinusOnly_Feb2016_dNdeta'
sam["data_L1TechBPTXMinusOnly_Feb2016_dNdeta"]["isData"]=True
sam["data_L1TechBPTXMinusOnly_Feb2016_dNdeta"]["numEvents"]=-1
sam["data_L1TechBPTXMinusOnly_Feb2016_dNdeta"]["pathSE"]='srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=/pnfs/desy.de/cms/tier2/store/user/sbaur/L1TechBPTXMinusOnly/L1TechBPTXMinusOnly-PromptReco_Run2015A_lowPU_intercalibFeb2016_dNdeta/160304_142319/0000/'
sam["data_L1TechBPTXMinusOnly_Feb2016_dNdeta"]["pathTrees"]='/XXXTMFTTree/store/user/sbaur/L1TechBPTXMinusOnly/L1TechBPTXMinusOnly-PromptReco_Run2015A_lowPU_intercalibFeb2016_dNdeta/160304_142319/0000/'
sam["data_L1TechBPTXMinusOnly_Feb2016_dNdeta"]["json"]='CommonFSQFramework/Skim/lumi/Run2015A_lowPU_B0T_247324.json'
sam["data_L1TechBPTXMinusOnly_Feb2016_dNdeta"]["lumiMinBias"]=-1
sam["data_L1TechBPTXMinusOnly_Feb2016_dNdeta"]["XS"]=-1
sam["data_L1TechBPTXMinusOnly_Feb2016_dNdeta"]["pathPAT"]='/XXXTMFPAT/store/user/sbaur/L1TechBPTXMinusOnly/L1TechBPTXMinusOnly-PromptReco_Run2015A_lowPU_intercalibFeb2016_dNdeta/160304_142319/0000/'
sam["data_L1TechBPTXMinusOnly_Feb2016_dNdeta"]["DS"]='/L1TechBPTXMinusOnly/Run2015A-PromptReco-v1/RECO'

sam["data_L1TechBPTXPlusOnly_Feb2016_dNdeta"]={}
sam["data_L1TechBPTXPlusOnly_Feb2016_dNdeta"]["crabJobs"]=0
sam["data_L1TechBPTXPlusOnly_Feb2016_dNdeta"]["GT"]='74X_dataRun2_Prompt_v2'
sam["data_L1TechBPTXPlusOnly_Feb2016_dNdeta"]["name"]='data_L1TechBPTXPlusOnly_Feb2016_dNdeta'
sam["data_L1TechBPTXPlusOnly_Feb2016_dNdeta"]["isData"]=True
sam["data_L1TechBPTXPlusOnly_Feb2016_dNdeta"]["numEvents"]=-1
sam["data_L1TechBPTXPlusOnly_Feb2016_dNdeta"]["pathSE"]='srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=/pnfs/desy.de/cms/tier2/store/user/sbaur/L1TechBPTXPlusOnly/L1TechBPTXPlusOnly-PromptReco_Run2015A_lowPU_intercalibFeb2016_dNdeta/160304_142250/0000'
sam["data_L1TechBPTXPlusOnly_Feb2016_dNdeta"]["pathTrees"]='/XXXTMFTTree/store/user/sbaur/L1TechBPTXPlusOnly/L1TechBPTXPlusOnly-PromptReco_Run2015A_lowPU_intercalibFeb2016_dNdeta/160304_142250/0000/'
sam["data_L1TechBPTXPlusOnly_Feb2016_dNdeta"]["json"]='CommonFSQFramework/Skim/lumi/Run2015A_lowPU_B0T_247324.json'
sam["data_L1TechBPTXPlusOnly_Feb2016_dNdeta"]["lumiMinBias"]=-1
sam["data_L1TechBPTXPlusOnly_Feb2016_dNdeta"]["XS"]=-1
sam["data_L1TechBPTXPlusOnly_Feb2016_dNdeta"]["pathPAT"]='/XXXTMFPAT/store/user/sbaur/L1TechBPTXPlusOnly/L1TechBPTXPlusOnly-PromptReco_Run2015A_lowPU_intercalibFeb2016_dNdeta/160304_142250/0000/'
sam["data_L1TechBPTXPlusOnly_Feb2016_dNdeta"]["DS"]='/L1TechBPTXPlusOnly/Run2015A-PromptReco-v1/RECO'

sam["data_L1TechBPTXQuiet_Feb2016_dNdeta"]={}
sam["data_L1TechBPTXQuiet_Feb2016_dNdeta"]["crabJobs"]=0
sam["data_L1TechBPTXQuiet_Feb2016_dNdeta"]["GT"]='74X_dataRun2_Prompt_v2'
sam["data_L1TechBPTXQuiet_Feb2016_dNdeta"]["name"]='data_L1TechBPTXQuiet_dNdeta'
sam["data_L1TechBPTXQuiet_Feb2016_dNdeta"]["isData"]=True
sam["data_L1TechBPTXQuiet_Feb2016_dNdeta"]["numEvents"]=-1
sam["data_L1TechBPTXQuiet_Feb2016_dNdeta"]["pathSE"]='srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=/pnfs/desy.de/cms/tier2/store/user/sbaur/L1TechBPTXQuiet/L1TechBPTXQuiet-PromptReco_Run2015A_lowPU_intercalibFeb2016_dNdeta/160304_142346/0000/'
sam["data_L1TechBPTXQuiet_Feb2016_dNdeta"]["pathTrees"]='/XXXTMFTTree/store/user/sbaur/L1TechBPTXQuiet/L1TechBPTXQuiet-PromptReco_Run2015A_lowPU_intercalibFeb2016_dNdeta/160304_142346/0000/'
sam["data_L1TechBPTXQuiet_Feb2016_dNdeta"]["json"]='CommonFSQFramework/Skim/lumi/Run2015A_lowPU_B0T_247324.json'
sam["data_L1TechBPTXQuiet_Feb2016_dNdeta"]["lumiMinBias"]=-1
sam["data_L1TechBPTXQuiet_Feb2016_dNdeta"]["XS"]=-1
sam["data_L1TechBPTXQuiet_Feb2016_dNdeta"]["pathPAT"]='/XXXTMFPAT/store/user/sbaur/L1TechBPTXQuiet/L1TechBPTXQuiet-PromptReco_Run2015A_lowPU_intercalibFeb2016_dNdeta/160304_142346/0000/'
sam["data_L1TechBPTXQuiet_Feb2016_dNdeta"]["DS"]='/L1TechBPTXQuiet/Run2015A-PromptReco-v1/RECO'

sam["data_ZeroBias1_Feb2016_dNdeta"]={}
sam["data_ZeroBias1_Feb2016_dNdeta"]["crabJobs"]=0
sam["data_ZeroBias1_Feb2016_dNdeta"]["GT"]='74X_dataRun2_Prompt_v2_dNdeta'
sam["data_ZeroBias1_Feb2016_dNdeta"]["name"]='data_ZeroBias1'
sam["data_ZeroBias1_Feb2016_dNdeta"]["isData"]=True
sam["data_ZeroBias1_Feb2016_dNdeta"]["numEvents"]=-1
sam["data_ZeroBias1_Feb2016_dNdeta"]["pathSE"]='srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=/pnfs/desy.de/cms/tier2/store/user/sbaur/ZeroBias1/ZeroBias-PromptReco_Run2015A_lowPU_intercalibFeb2016_dNdeta/160304_142130/0000/'
sam["data_ZeroBias1_Feb2016_dNdeta"]["pathTrees"]='/XXXTMFTTree/store/user/sbaur/ZeroBias1/ZeroBias-PromptReco_Run2015A_lowPU_intercalibFeb2016_dNdeta/160304_142130/0000/'
sam["data_ZeroBias1_Feb2016_dNdeta"]["json"]='CommonFSQFramework/Skim/lumi/Run2015A_lowPU_B0T.json'
sam["data_ZeroBias1_Feb2016_dNdeta"]["lumiMinBias"]=-1
sam["data_ZeroBias1_Feb2016_dNdeta"]["XS"]=-1
sam["data_ZeroBias1_Feb2016_dNdeta"]["pathPAT"]='/XXXTMFPAT/store/user/sbaur/ZeroBias1/ZeroBias-PromptReco_Run2015A_lowPU_intercalibFeb2016_dNdeta/160304_142130/0000/'
sam["data_ZeroBias1_Feb2016_dNdeta"]["DS"]='/ZeroBias1/Run2015A-PromptReco-v1/RECO'


##################################################
###### dN/deta Run ReReco Phi,HF #################
##################################################

sam["data_ZeroBias1_May2016_dNdeta"]={}
sam["data_ZeroBias1_May2016_dNdeta"]["crabJobs"]=0
sam["data_ZeroBias1_May2016_dNdeta"]["GT"]='74X_dataRun2_Prompt_v2_dNdeta'
sam["data_ZeroBias1_May2016_dNdeta"]["name"]='data_ZeroBias1'
sam["data_ZeroBias1_May2016_dNdeta"]["isData"]=True
sam["data_ZeroBias1_May2016_dNdeta"]["numEvents"]=-1
sam["data_ZeroBias1_May2016_dNdeta"]["pathSE"]='srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=/pnfs/desy.de/cms/tier2/store/user/sbaur/ZeroBias1/ZeroBias-ReReco_Run2015A_lowPU_intercalibMay2016_HFcorrection_dNdeta/160503_080304/0000'
sam["data_ZeroBias1_May2016_dNdeta"]["pathTrees"]='/XXXTMFTTree/store/user/sbaur/ZeroBias1/ZeroBias-ReReco_Run2015A_lowPU_intercalibMay2016_HFcorrection_dNdeta/160503_080304/0000'
sam["data_ZeroBias1_May2016_dNdeta"]["json"]='CommonFSQFramework/Skim/lumi/Run2015A_lowPU_B0T.json'
sam["data_ZeroBias1_May2016_dNdeta"]["lumiMinBias"]=-1
sam["data_ZeroBias1_May2016_dNdeta"]["XS"]=-1
sam["data_ZeroBias1_May2016_dNdeta"]["pathPAT"]='/XXXTMFPAT/store/user/sbaur/ZeroBias1/ZeroBias-ReReco_Run2015A_lowPU_intercalibMay2016_HFcorrection_dNdeta/160503_080304/0000'
sam["data_ZeroBias1_May2016_dNdeta"]["DS"]='/ZeroBias1/Run2015A-v1/RAW'

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
