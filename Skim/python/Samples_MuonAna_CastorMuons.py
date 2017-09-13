anaVersion="MuonAna_CastorMuons"
anaType="MuonAna_CastorMuons"

cbSmartCommand="smartCopy"
cbSmartBlackList=""
cbWMS="https://wmscms.cern.ch:7443/glite_wms_wmproxy_server"
skimEfficiencyMethod="getSkimEff"

sam = {}


# 2011 noise
# 2011 DS+runs


############################################################
# CFF Skims using interfill data from run PARun2016B
# pPbRun on RAW data 

sam["data_PACastor_Muon_2016B"] = {}
#sam["data_PACastor_Muon_2016B"]["crabJobs"] = 232
# sam["data_PACastor_Muon_2016"]["numEvents"]=4486825
sam["data_PACastor_Muon_2016B"]["GT"] = '80X_dataRun2_Prompt_v15'
sam["data_PACastor_Muon_2016B"]["name"] = 'data_PACastor_Muon_2016B'
sam["data_PACastor_Muon_2016B"]["isData"] = True
sam["data_PACastor_Muon_2016B"]["pathSE"] = 'srm://grid-srm.physik.rwth-aachen.de:8443/srm/managerv2?SFN=/pnfs/physik.rwth-aachen.de/cms/store/user/makbiyik/CastorMuon2016/PACastor/MuonAna_CastorMuon2016_data_PACastor_Muon_2016B/161215_143102/0000/'
# a few more files are split into directory:
#      srm://grid-srm.physik.rwth-aachen.de:8443/srm/managerv2?SFN=/pnfs/physik.rwth-aachen.de/cms/store/user/makbiyik/CastorMuon2016/PACastor/MuonAna_CastorMuon2016_data_PACastor_Muon_2016/161215_105329/0000/
sam["data_PACastor_Muon_2016B"]["pathTrees"]='XXXTMFTTree/CastorMuons/PACastor/MuonAna_CastorMuons2016_data_PACastor_Muon_2016B/161215_143102/0000/'
sam["data_PACastor_Muon_2016B"]["json"] = 'muon_2016_3.8T_halo.json'
sam["data_PACastor_Muon_2016B"]["lumiMinBias"] = -1
sam["data_PACastor_Muon_2016B"]["XS"] = -1
#sam["data_PACastor_Muon_2016"]["pathPAT"]='XXXTMFPAT/store/user/makbiyik/CastorMuon2016/PACastor/MuonAna_CastorMuon2016_data_PACastor_Muon_2016/161215_143102/0000//'
sam["data_PACastor_Muon_2016B"]["DS"] = '/PACastor/PARun2016B-v1/RAW'


sam["data_PACastor_Muon_2016C"]={}
#sam["data_PACastor_Muon_2016C"]["crabJobs"]=232
# sam["data_PACastor_Muon_2016"]["numEvents"]=4486825
sam["data_PACastor_Muon_2016C"]["GT"]='80X_dataRun2_Prompt_v15'
sam["data_PACastor_Muon_2016C"]["name"]='data_PACastor_Muon_2016C'
sam["data_PACastor_Muon_2016C"]["isData"]=True
sam["data_PACastor_Muon_2016C"]["pathSE"]='srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=/pnfs/desy.de/cms/tier2/store/user/rulrich/CastorMuons/PACastor/MuonAna_CastorMuons_data_PACastor_Muon_2016C/170903_105332/0000'
# more data sam["data_PACastor_Muon_2016C"]["pathSE"]='srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=/pnfs/desy.de/cms/tier2/store/user/rulrich/CastorMuons/PACastor/MuonAna_CastorMuons_data_PACastor_Muon_2016C/170903_105332/0001'
sam["data_PACastor_Muon_2016C"]["pathTrees"]='XXXTMFTTree/CastorMuons/PACastor/MuonAna_CastorMuons_data_PACastor_Muon_2016C/170903_105332/0000'
sam["data_PACastor_Muon_2016C"]["json"]='muon_2016_3.8T_halo.json'
sam["data_PACastor_Muon_2016C"]["lumiMinBias"]=-1
sam["data_PACastor_Muon_2016C"]["XS"]=-1
#sam["data_PACastor_Muon_2016"]["pathPAT"]='XXXTMFPAT/store/user/makbiyik/CastorMuon2016/PACastor/MuonAna_CastorMuon2016_data_PACastor_Muon_2016/161215_143102/0000//'
#sam["data_PACastor_Muon_2016C"]["DS"]='/PACastor/PARun2016C-v1/RAW' not on disk So 3. Sep 11:12:29 CEST 2017
sam["data_PACastor_Muon_2016C"]["DS"]='/PACastor/PARun2016C-PromptReco-v1/AOD' # at vanderbilt


sam["data_PAMinimumBias1_Noise_2016"]={}
#sam["data_PAMinimumBias1_Noise_2016"]["crabJobs"]=232
# sam["data_PAMinimumBias1_Noise_2016"]["numEvents"]=4486825
sam["data_PAMinimumBias1_Noise_2016"]["GT"]='80X_dataRun2_Prompt_v15'
sam["data_PAMinimumBias1_Noise_2016"]["name"]='data_PAMinimumBias1_Noise_2016'
sam["data_PAMinimumBias1_Noise_2016"]["isData"]=True
sam["data_PAMinimumBias1_Noise_2016"]["pathSE"]='srm://grid-srm.physik.rwth-aachen.de:8443/srm/managerv2?SFN=/pnfs/physik.rwth-aachen.de/cms/store/user/makbiyik/CastorMuon2016/MinimumBias/MuonAna_CastorMuon2016_data_PAMinimumBias1_Noise_2016/161215_144035/0000'
# a few more files are split into:
#       srm://grid-srm.physik.rwth-aachen.de:8443/srm/managerv2?SFN=/pnfs/physik.rwth-aachen.de/cms/store/user/makbiyik/CastorMuon2016/MinimumBias/MuonAna_CastorMuon2016_data_PAMinimumBias1_Noise_2016/161215_105719/0000
sam["data_PAMinimumBias1_Noise_2016"]["pathTrees"]='XXXTMFTTree/CastorMuons/MinimumBias/MuonAna_CastorMuon2016_data_PAMinimumBias1_Noise_2016/161215_144035/0000'
sam["data_PAMinimumBias1_Noise_2016"]["json"]='muon_2016_3.8T_halo.json'
sam["data_PAMinimumBias1_Noise_2016"]["lumiMinBias"]=-1
sam["data_PAMinimumBias1_Noise_2016"]["XS"]=-1
#sam["data_PAMinimumBias1_Noise_2016"]["pathPAT"]='XXXTMFPAT/store/user/makbiyik/CastorMuon2016/MinimumBias/MuonAna_CastorMuon2016_data_PAMinimumBias1_Noise_2016/161215_144035/0000//'
sam["data_PAMinimumBias1_Noise_2016"]["DS"]='/MinimumBias/PARun2016B-PromptReco-v1/AOD'



############################################################
# CFF Skims using 0 Tesla June Run2015A

sam["data_MinimumBias_2015_0T_June"]={}
#sam["data_MinimumBias_2015_0T_June"]["crabJobs"]=232
#sam["data_MinimumBias_2015_0T_June"]["numEvents"]=-1
sam["data_MinimumBias_2015_0T_June"]["GT"]='80X_dataRun2_v13'
sam["data_MinimumBias_2015_0T_June"]["name"]='data_MinimumBias_2015_0T_June'
sam["data_MinimumBias_2015_0T_June"]["isData"]=True
sam["data_MinimumBias_2015_0T_June"]["pathSE"]='srm://grid-srm.physik.rwth-aachen.de:8443/srm/managerv2?SFN=/pnfs/physik.rwth-aachen.de/cms/store/user/rulrich/CastorMuons/MinimumBias/MuonAna_CastorMuons_data_MinimumBias_2015_0T_June/170902_112723/0000'
sam["data_MinimumBias_2015_0T_June"]["pathTrees"]='XXXTMFTTree/CastorMuons/MinimumBias/MuonAna_CastorMuons_data_MinimumBias_2015_0T_June/170902_112723/0000'
sam["data_MinimumBias_2015_0T_June"]["json"]='muon_2015_0.0T_halo.json'
sam["data_MinimumBias_2015_0T_June"]["lumiMinBias"]=-1
sam["data_MinimumBias_2015_0T_June"]["XS"]=-1
#sam["data_MinimumBias_2015_0T_June"]["pathPAT"]='XXXTMFPAT/store/user/rulrich/CastorMuons/'
sam["data_MinimumBias_2015_0T_June"]["DS"]='/MinimumBias/Run2015A-v1/RAW'


sam["data_MinimumBias_2015_JuneNoise"]={}
#sam["data_MinimumBias_2015_JuneNoise"]["crabJobs"]=232
#sam["data_MinimumBias_2015_JuneNoise"]["numEvents"]=-1
sam["data_MinimumBias_2015_JuneNoise"]["GT"]='80X_dataRun2_v13'
sam["data_MinimumBias_2015_JuneNoise"]["name"]='data_MinimumBias_2015_JuneNoise_Objects'
sam["data_MinimumBias_2015_JuneNoise"]["isData"]=True
sam["data_MinimumBias_2015_JuneNoise"]["pathSE"]='srm://grid-srm.physik.rwth-aachen.de:8443/srm/managerv2?SFN=/pnfs/physik.rwth-aachen.de/cms/store/user/rulrich/CastorMuons/MinimumBias/MuonAna_CastorMuons_data_MinimumBias_2015_JuneNoise/170902_151248/0000'
sam["data_MinimumBias_2015_JuneNoise"]["pathTrees"]='XXXTMFTTree/CastorMuons/MinimumBias/MuonAna_CastorMuons_data_MinimumBias_2015_JuneNoise/170902_151248/0000'
sam["data_MinimumBias_2015_JuneNoise"]["json"]='muon_2015_0.0T_halo.json'
sam["data_MinimumBias_2015_JuneNoise"]["lumiMinBias"]=-1
sam["data_MinimumBias_2015_JuneNoise"]["XS"]=-1
#sam["data_MinimumBias_2015_JuneNoise"]["pathPAT"]='XXXTMFPAT/store/user/makbiyik/CastorMuon2015/muon_2015_JuneNoise//'
sam["data_MinimumBias_2015_JuneNoise"]["DS"]='/MinimumBias/Run2015A-v1/RAW'




############################################################
# CFF Skim using 0 Tesla Nov Run2015E

sam["data_MinimumBias_2015_0T_Nov"]={}
#sam["data_MinimumBias_2015_0T_Nov"]["crabJobs"]=232
#sam["data_MinimumBias_2015_0T_Nov"]["numEvents"]=-1
sam["data_MinimumBias_2015_0T_Nov"]["GT"]='80X_dataRun2_v13'
sam["data_MinimumBias_2015_0T_Nov"]["name"]='data_MinimumBias_2015_0T_Nov'
sam["data_MinimumBias_2015_0T_Nov"]["isData"]=True
sam["data_MinimumBias_2015_0T_Nov"]["pathSE"]='srm://grid-srm.physik.rwth-aachen.de:8443/srm/managerv2?SFN=/pnfs/physik.rwth-aachen.de/cms/store/user/makbiyik/CastorMuon2015/muon_2015_0T_Nov/Cosmics/MuonAna_CastorMuon2016_data_MinimumBias_2015_0T_Nov/161220_135402/0000'
sam["data_MinimumBias_2015_0T_Nov"]["pathTrees"]='XXXTMFTTree/CastorMuons/muon_2015_0T_Nov/Cosmics/MuonAna_CastorMuon2016_data_MinimumBias_2015_0T_Nov/161220_135402/0000'
sam["data_MinimumBias_2015_0T_Nov"]["json"]='muon_2015_0.0T_Nov_halo.json'
sam["data_MinimumBias_2015_0T_Nov"]["lumiMinBias"]=-1
sam["data_MinimumBias_2015_0T_Nov"]["XS"]=-1
#sam["data_MinimumBias_2015_0T_Nov"]["pathPAT"]='XXXTMFPAT/store/user/makbiyik/CastorMuon2015/muon_2015_0T_Nov/Cosmics/MuonAna_CastorMuons_data_MinimumBias_2015_0T_Nov/161220_135402/0000//'
sam["data_MinimumBias_2015_0T_Nov"]["DS"]='/Cosmics/Run2015E-v1/RAW'


sam["data_MinimumBias_2015_NovNoise"]={}
sam["data_MinimumBias_2015_NovNoise"]["crabJobs"]=232
sam["data_MinimumBias_2015_NovNoise"]["GT"]='80X_dataRun2_v13'
sam["data_MinimumBias_2015_NovNoise"]["name"]='data_MinimumBias_2015_Noise'
sam["data_MinimumBias_2015_NovNoise"]["isData"]=True
sam["data_MinimumBias_2015_NovNoise"]["numEvents"]=-1
sam["data_MinimumBias_2015_NovNoise"]["pathSE"]='srm://grid-srm.physik.rwth-aachen.de:8443/srm/managerv2?SFN=/pnfs/physik.rwth-aachen.de/cms/store/user/makbiyik/CastorMuon2015/muon_2015_Noise/MinimumBias/MuonAna_CastorMuon2016_data_MinimumBias_2015_Noise/161222_114545/0000'
sam["data_MinimumBias_2015_NovNoise"]["pathTrees"]='XXXTMFTTree/CastorMuons/muon_2015_Noise/MinimumBias/MuonAna_CastorMuon2016_data_MinimumBias_2015_Noise/161222_114545/0000'
sam["data_MinimumBias_2015_NovNoise"]["json"]='muon_2015_0.0T_Nov_halo.json'
sam["data_MinimumBias_2015_NovNoise"]["lumiMinBias"]=-1
sam["data_MinimumBias_2015_NovNoise"]["XS"]=-1
#sam["data_MinimumBias_2015_NovNoise"]["pathPAT"]='XXXTMFPAT/store/user/makbiyik/CastorMuon2015/muon_2015_Noise/MinimumBias/MuonAna_CastorMuon2016_data_MinimumBias_2015_Noise/161222_114545/0000//'
sam["data_MinimumBias_2015_NovNoise"]["DS"]='/MinimumBias/Run2015E-v1/RAW'


# muon_2015_3.8T_Nov_halo.json, /Cosmics/Run2015E-v1/RAW

sam["data_MinimumBias_2015_38T_Nov"]={}
sam["data_MinimumBias_2015_38T_Nov"]["crabJobs"]=232
sam["data_MinimumBias_2015_38T_Nov"]["GT"]='80X_dataRun2_v13'
sam["data_MinimumBias_2015_38T_Nov"]["name"]='data_MinimumBias_2015_38T_Nov'
sam["data_MinimumBias_2015_38T_Nov"]["isData"]=True
sam["data_MinimumBias_2015_38T_Nov"]["numEvents"]=-1
sam["data_MinimumBias_2015_38T_Nov"]["pathSE"]='srm://grid-srm.physik.rwth-aachen.de:8443/srm/managerv2?SFN=/pnfs/physik.rwth-aachen.de/cms/store/user/makbiyik/CastorMuon2015/muon_2015_38T_Nov/Cosmics/MuonAna_CastorMuon2016_data_MinimumBias_2015_38T_Nov/161220_135728/0000'
sam["data_MinimumBias_2015_38T_Nov"]["pathTrees"]='XXXTMFTTree/store/user/makbiyik/CastorMuons/muon_2015_38T_Nov/Cosmics/MuonAna_CastorMuon2016_data_MinimumBias_2015_38T_Nov/161220_135728/0000'
sam["data_MinimumBias_2015_38T_Nov"]["json"]='muon_2015_3.8T_Nov_halo.json'
sam["data_MinimumBias_2015_38T_Nov"]["lumiMinBias"]=-1
sam["data_MinimumBias_2015_38T_Nov"]["XS"]=-1
#sam["data_MinimumBias_2015_38T_Nov"]["pathPAT"]='XXXTMFPAT/store/user/makbiyik/CastorMuon2015/muon_2015_38T_Nov/Cosmics/MuonAna_CastorMuon2016_data_MinimumBias_2015_38T_Nov/161220_135728/0000//'
sam["data_MinimumBias_2015_38T_Nov"]["DS"]='/Cosmics/Run2015E-v1/RAW'


# muon_2015_38T_Nov_halo.json, /HIRun /Cosmics/Run2015E-v1/RAW

sam["data_MinimumBias_2015_38T_HIRunNov"]={}
sam["data_MinimumBias_2015_38T_HIRunNov"]["crabJobs"]=232
sam["data_MinimumBias_2015_38T_HIRunNov"]["GT"]='80X_dataRun2_v13'
sam["data_MinimumBias_2015_38T_HIRunNov"]["name"]='data_MinimumBias_2015_38T_Nov_HIRunNov'
sam["data_MinimumBias_2015_38T_HIRunNov"]["isData"]=True
sam["data_MinimumBias_2015_38T_HIRunNov"]["numEvents"]=-1
sam["data_MinimumBias_2015_38T_HIRunNov"]["pathSE"]='srm://grid-srm.physik.rwth-aachen.de:8443/srm/managerv2?SFN=/pnfs/physik.rwth-aachen.de/cms/store/user/makbiyik/CastorMuon2015/muon_2015_38T_HIRunNov/Cosmics/MuonAna_CastorMuon2016_data_MinimumBias_2015_38T_HIRunNov/161223_132204/0000'
sam["data_MinimumBias_2015_38T_HIRunNov"]["pathTrees"]='XXXTMFTTree/CastorMuons/muon_2015_38T_HIRunNov/Cosmics/MuonAna_CastorMuon2016_data_MinimumBias_2015_38T_HIRunNov/161223_132204/0000'
sam["data_MinimumBias_2015_38T_HIRunNov"]["json"]='muon_2015_3.8T_Nov_halo.json'
sam["data_MinimumBias_2015_38T_HIRunNov"]["lumiMinBias"]=-1
sam["data_MinimumBias_2015_38T_HIRunNov"]["XS"]=-1
#sam["data_MinimumBias_2015_38T_HIRunNov"]["pathPAT"]='XXXTMFPAT/store/user/makbiyik/CastorMuon2015/muon_2015_38T_HIRunNov/Cosmics/MuonAna_CastorMuon2016_data_MinimumBias_2015_38T_HIRunNov/161223_132204/0000//'
sam["data_MinimumBias_2015_38T_HIRunNov"]["DS"]='/Cosmics/HIRun2015-v1/RAW'


# muon_2015_38T_Nov_halo.json, /ppHV. /Cosmics/Run2015E-v1/RAW

sam["data_MinimumBias_2015_38T_ppHVNov"]={}
sam["data_MinimumBias_2015_38T_ppHVNov"]["crabJobs"]=232
sam["data_MinimumBias_2015_38T_ppHVNov"]["GT"]='80X_dataRun2_v13'
sam["data_MinimumBias_2015_38T_ppHVNov"]["name"]='data_MinimumBias_2015_38T_ppHVNov'
sam["data_MinimumBias_2015_38T_ppHVNov"]["isData"]=True
sam["data_MinimumBias_2015_38T_ppHVNov"]["numEvents"]=-1
sam["data_MinimumBias_2015_38T_ppHVNov"]["pathSE"]='srm://grid-srm.physik.rwth-aachen.de:8443/srm/managerv2?SFN=/pnfs/physik.rwth-aachen.de/cms/store/user/makbiyik/CastorMuon2015/muon_2015_38T_ppHVNov/Cosmics/MuonAna_CastorMuon2016_data_MinimumBias_2015_38T_ppHVNov/161223_131855/0000'
sam["data_MinimumBias_2015_38T_ppHVNov"]["pathTrees"]='XXXTMFTTree/CastorMuons/muon_2015_38T_ppHVNov/Cosmics/MuonAna_CastorMuon2016_data_MinimumBias_2015_38T_ppHVNov/161223_131855/0000'
sam["data_MinimumBias_2015_38T_ppHVNov"]["json"]='muon_2015_3.8T_Nov_halo_ppHV.json'
sam["data_MinimumBias_2015_38T_ppHVNov"]["lumiMinBias"]=-1
sam["data_MinimumBias_2015_38T_ppHVNov"]["XS"]=-1
#sam["data_MinimumBias_2015_38T_ppHVNov"]["pathPAT"]='XXXTMFPAT/store/user/makbiyik/CastorMuon2015/muon_2015_38T_ppHVNov/Cosmics/MuonAna_CastorMuon2016_data_MinimumBias_2015_38T_ppHVNov/161223_131855/0000//'
sam["data_MinimumBias_2015_38T_ppHVNov"]["DS"]='/Cosmics/HIRun2015-v1/RAW'



###############################################################
# muon_2013_38T_Nov_halo.json, /ppHV. reco
sam["data_PAMinBiasUPC_Run2013"]={}
sam["data_PAMinBiasUPC_Run2013"]["crabJobs"]=5736
sam["data_PAMinBiasUPC_Run2013"]["GT"]='GR_R_75_V5A'
sam["data_PAMinBiasUPC_Run2013"]["name"]='data_PAMinBiasUPC_Run2013'
sam["data_PAMinBiasUPC_Run2013"]["isData"]=True
sam["data_PAMinBiasUPC_Run2013"]["numEvents"]=286814246
sam["data_PAMinBiasUPC_Run2013"]["pathSE"]='srm://grid-srm.physik.rwth-aachen.de:8443/srm/managerv2?SFN=/pnfs/physik.rwth-aachen.de/cms/store/user/makbiyik/CastorMuon2013/HIRun2013A/PAMinBiasUPC/MuonAna_CastorMuon2016_data_PAMinBiasUPC_Run2013/170120_142642/0000'
# more data in 'srm://grid-srm.physik.rwth-aachen.de:8443/srm/managerv2?SFN=/pnfs/physik.rwth-aachen.de/cms/store/user/makbiyik/CastorMuon2013/HIRun2013A/PAMinBiasUPC/MuonAna_CastorMuon2016_data_PAMinBiasUPC_Run2013/170120_142642/0001'
# and more data in #'srm://grid-srm.physik.rwth-aachen.de:8443/srm/managerv2?SFN=/pnfs/physik.rwth-aachen.de/cms/store/user/makbiyik/CastorMuon2013/HIRun2013A/PAMinBiasUPC/MuonAna_CastorMuon2016_data_PAMinBiasUPC_Run2013/170120_142642/0002'
sam["data_PAMinBiasUPC_Run2013"]["pathTrees"]='XXXTMFPAT/store/user/makbiyik/CastorMuons/HIRun2013A/PAMinBiasUPC/MuonAna_CastorMuon2016_data_PAMinBiasUPC_Run2013/170120_142642/0000'
sam["data_PAMinBiasUPC_Run2013"]["json"]='muon_2013_3.8T_halo.json'
sam["data_PAMinBiasUPC_Run2013"]["lumiMinBias"]=-1
sam["data_PAMinBiasUPC_Run2013"]["XS"]=-1
#sam["data_PAMinBiasUPC_Run2013"]["pathPAT"]='XXXTMFPAT/store/user/makbiyik/CastorMuon2013/HIRun2013A/HIRun2013A/PAMinBiasUPC/MuonAna_CastorMuon2016_data_PAMinBiasUPC_Run2013/170111_103934/0000//'
sam["data_PAMinBiasUPC_Run2013"]["DS"]='/PAMinBiasUPC/HIRun2013-PromptReco-v1/RECO'


sam["data_PAMNoise_Run2013"]={}
sam["data_PAMNoise_Run2013"]["crabJobs"]=5736
sam["data_PAMNoise_Run2013"]["GT"]='GR_R_75_V5A'
sam["data_PAMNoise_Run2013"]["name"]='data_PAMNoise_Run2013'
sam["data_PAMNoise_Run2013"]["isData"]=True
sam["data_PAMNoise_Run2013"]["numEvents"]=286814246
sam["data_PAMNoise_Run2013"]["pathSE"]='srm://grid-srm.physik.rwth-aachen.de:8443/srm/managerv2?SFN=/pnfs/physik.rwth-aachen.de/cms/store/user/rulrich/CastorMuons/'
sam["data_PAMNoise_Run2013"]["pathTrees"]='XXXTMFPAT/'
sam["data_PAMNoise_Run2013"]["json"]='muon_2013_3.8T_halo.json'
sam["data_PAMNoise_Run2013"]["lumiMinBias"]=-1
sam["data_PAMNoise_Run2013"]["XS"]=-1
# sam["data_PAMNoise_Run2013"]["pathPAT"]='XXXTMFPAT/store/user/makbiyik/CastorMuon2013/HIRun2013A//'
sam["data_PAMNoise_Run2013"]["DS"]='/MinimumBias/HIRun2013-v1/RAW'



######################################################################
# /ForwardTriggers/Run2011A

sam["data_ForwardTriggers_2011"]={}
sam["data_ForwardTriggers_2011"]["crabJobs"]=232
sam["data_ForwardTriggers_2011"]["GT"]='FT_R_53_LV5::All'
sam["data_ForwardTriggers_2011"]["name"]='data_ForwardTriggers_2011'
sam["data_ForwardTriggers_2011"]["isData"]=True
sam["data_ForwardTriggers_2011"]["numEvents"]=-1
sam["data_ForwardTriggers_2011"]["pathSE"]='srm://grid-srm.physik.rwth-aachen.de:8443/srm/managerv2?SFN=/pnfs/physik.rwth-aachen.de/cms/store/user/rulrich/CastorMuons/ForwardTriggers/CastorMuons_data_ForwardTriggers_2011/170317_104733/0000'
sam["data_ForwardTriggers_2011"]["pathTrees"]='XXXTMFTTree/CastorMuons/ForwardTriggers/CastorMuons_data_ForwardTriggers_2011/170317_104733/0000'
sam["data_ForwardTriggers_2011"]["json"]='muon_2011_3.8T_halo.json'
sam["data_ForwardTriggers_2011"]["lumiMinBias"]=-1
sam["data_ForwardTriggers_2011"]["XS"]=-1
#sam["data_ForwardTriggers_2011"]["pathPAT"]='XXXTMFPAT/store/user/rulrich/CastorMuons/'
sam["data_ForwardTriggers_2011"]["DS"]='/ForwardTriggers/Run2011A-12Oct2013-v2/AOD'

sam["data_ForwardTriggers_2011_0T"]={}
sam["data_ForwardTriggers_2011_0T"]["crabJobs"]=232
sam["data_ForwardTriggers_2011_0T"]["GT"]='FT_R_53_LV5::All'
sam["data_ForwardTriggers_2011_0T"]["name"]='data_ForwardTriggers_2011_0T'
sam["data_ForwardTriggers_2011_0T"]["isData"]=True
sam["data_ForwardTriggers_2011_0T"]["numEvents"]=-1
sam["data_ForwardTriggers_2011_0T"]["pathSE"]='srm://grid-srm.physik.rwth-aachen.de:8443/srm/managerv2?SFN=/pnfs/physik.rwth-aachen.de/cms/store/user/rulrich/CastorMuons/ForwardTriggers/CastorMuons_data_ForwardTriggers_2011_0T/170317_172044/0000'
sam["data_ForwardTriggers_2011_0T"]["pathTrees"]='XXXTMFTTree/CastorMuons/ForwardTriggers/CastorMuons_data_ForwardTriggers_2011_0T/170317_172044/0000'
sam["data_ForwardTriggers_2011_0T"]["json"]='muon_2011_0.0T_halo.json'
sam["data_ForwardTriggers_2011_0T"]["lumiMinBias"]=-1
sam["data_ForwardTriggers_2011_0T"]["XS"]=-1
#sam["data_ForwardTriggers_2011_0T"]["pathPAT"]='XXXTMFPAT/store/user/rulrich/CastorMuons/'
sam["data_ForwardTriggers_2011_0T"]["DS"]='/ForwardTriggers/Run2011A-12Oct2013-v2/AOD'

sam["data_ForwardTriggers_2011_2T"]={}
sam["data_ForwardTriggers_2011_2T"]["crabJobs"]=232
sam["data_ForwardTriggers_2011_2T"]["GT"]='FT_R_53_LV5::All'
sam["data_ForwardTriggers_2011_2T"]["name"]='data_ForwardTriggers_2011_2T'
sam["data_ForwardTriggers_2011_2T"]["isData"]=True
sam["data_ForwardTriggers_2011_2T"]["numEvents"]=-1
sam["data_ForwardTriggers_2011_2T"]["pathSE"]='srm://grid-srm.physik.rwth-aachen.de:8443/srm/managerv2?SFN=/pnfs/physik.rwth-aachen.de/cms/store/user/rulrich/CastorMuons/ForwardTriggers/CastorMuons_data_ForwardTriggers_2011_2T/170317_172017/0000'
sam["data_ForwardTriggers_2011_2T"]["pathTrees"]='XXXTMFTTree/CastorMuons/ForwardTriggers/CastorMuons_data_ForwardTriggers_2011_2T/170317_172017/0000'
sam["data_ForwardTriggers_2011_2T"]["json"]='muon_2011_2.0T_halo.json'
sam["data_ForwardTriggers_2011_2T"]["lumiMinBias"]=-1
sam["data_ForwardTriggers_2011_2T"]["XS"]=-1
#sam["data_ForwardTriggers_2011_2T"]["pathPAT"]='XXXTMFPAT/store/user/rulrich/CastorMuons/'
sam["data_ForwardTriggers_2011_2T"]["DS"]='/ForwardTriggers/Run2011A-12Oct2013-v2/AOD'




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
                if not sam[s]["pathPAT"].endswith('/'):
                        sam[s]["pathPAT"] += '/'
            if "pathTrees" in sam[s]:
                sam[s]["pathTrees"] = sam[s]["pathTrees"].replace("XXXTMFTTree", localBasePathTrees)
                if not sam[s]["pathTrees"].endswith('/'):
                        sam[s]["pathTrees"] += '/'
        return sam

sam = fixLocalPaths(sam)

