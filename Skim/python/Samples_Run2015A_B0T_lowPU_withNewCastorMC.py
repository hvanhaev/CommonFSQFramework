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


########################################################################
## Samples with Hans Noise fix and various zero Tesla Tracking tests  ##
########################################################################

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

sam["MinBias_EPOS_13TeV_MagnetOff_CASTORmeasured_newNoise_newTracking"]={}
sam["MinBias_EPOS_13TeV_MagnetOff_CASTORmeasured_newNoise_newTracking"]["crabJobs"]=100
sam["MinBias_EPOS_13TeV_MagnetOff_CASTORmeasured_newNoise_newTracking"]["GT"]='76X_mcRun2_asymptotic_v14'
sam["MinBias_EPOS_13TeV_MagnetOff_CASTORmeasured_newNoise_newTracking"]["name"]='MinBias_EPOS_13TeV_MagnetOff_CASTORmeasured_newNoise_newTracking'
sam["MinBias_EPOS_13TeV_MagnetOff_CASTORmeasured_newNoise_newTracking"]["isData"]=False
sam["MinBias_EPOS_13TeV_MagnetOff_CASTORmeasured_newNoise_newTracking"]["numEvents"]=4978400
sam["MinBias_EPOS_13TeV_MagnetOff_CASTORmeasured_newNoise_newTracking"]["pathSE"]='srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=/pnfs/desy.de/cms/tier2/store/user/sbaur/MinBias_EPOS_13TeV/MinBias_EPOS_13TeV_MagnetOff_CASTORmeasured_newCASTORnoise_newTracking_CFF/170111_165443/0000/'
sam["MinBias_EPOS_13TeV_MagnetOff_CASTORmeasured_newNoise_newTracking"]["pathTrees"]='/XXXTMFTTree/store/user/sbaur/MinBias_EPOS_13TeV/MinBias_EPOS_13TeV_MagnetOff_CASTORmeasured_newCASTORnoise_newTracking_CFF/170111_165443/0000/'
sam["MinBias_EPOS_13TeV_MagnetOff_CASTORmeasured_newNoise_newTracking"]["json"]=''
sam["MinBias_EPOS_13TeV_MagnetOff_CASTORmeasured_newNoise_newTracking"]["lumiMinBias"]=-1
sam["MinBias_EPOS_13TeV_MagnetOff_CASTORmeasured_newNoise_newTracking"]["XS"]=-1
sam["MinBias_EPOS_13TeV_MagnetOff_CASTORmeasured_newNoise_newTracking"]["pathPAT"]='/XXXTMFPAT/store/user/sbaur/MinBias_EPOS_13TeV/MinBias_EPOS_13TeV_MagnetOff_CASTORmeasured_newCASTORnoise_newTracking_CFF/170111_165443/0000/'
sam["MinBias_EPOS_13TeV_MagnetOff_CASTORmeasured_newNoise_newTracking"]["DS"]='/MinBias_EPOS_13TeV/sbaur-MinBias_EPOS_13TeV_MagnetOff_CASTORmeasured_newCASTORnoise_RECO-288ab5be9a42aa4a7ffd90fa253c6744/USER'

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


########################################################
###### all LHCf Runs based on 27Jan2016 reReco #########
########################################################

sam["data_ZeroBias_27Jan2016_LHCf"]={}
sam["data_ZeroBias_27Jan2016_LHCf"]["crabJobs"]=0
sam["data_ZeroBias_27Jan2016_LHCf"]["GT"]=''
sam["data_ZeroBias_27Jan2016_LHCf"]["name"]='data_ZeroBias_27Jan2016_LHCf'
sam["data_ZeroBias_27Jan2016_LHCf"]["isData"]=True
sam["data_ZeroBias_27Jan2016_LHCf"]["numEvents"]=-1
sam["data_ZeroBias_27Jan2016_LHCf"]["pathSE"]='srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=/pnfs/desy.de/cms/tier2/store/user/sbaur/ZeroBiasAll/ZeroBias-27Jan2016_LHCf_CFF'
sam["data_ZeroBias_27Jan2016_LHCf"]["pathTrees"]='/XXXTMFTTree/store/user/sbaur/ZeroBiasAll/ZeroBias-27Jan2016_LHCf_CFF'
sam["data_ZeroBias_27Jan2016_LHCf"]["json"]=''
sam["data_ZeroBias_27Jan2016_LHCf"]["lumiMinBias"]=-1
sam["data_ZeroBias_27Jan2016_LHCf"]["XS"]=-1
sam["data_ZeroBias_27Jan2016_LHCf"]["pathPAT"]='/XXXTMFPAT/store/user/sbaur/ZeroBiasAll/ZeroBias-27Jan2016_LHCf_CFF'
sam["data_ZeroBias_27Jan2016_LHCf"]["DS"]='/ZeroBias1/Run2015A-27Jan2016-v1/RECO'


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
