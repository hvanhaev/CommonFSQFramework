anaVersion="NoiseAna_Castor"
anaType="NoiseAna_Castor"

cbSmartCommand="smartCopy"
cbSmartBlackList=""
cbWMS="https://wmscms.cern.ch:7443/glite_wms_wmproxy_server"
skimEfficiencyMethod="getSkimEff"

sam = {}


sam["data_MinimumBias_2015_JuneNoise"]={}
sam["data_MinimumBias_2015_JuneNoise"]["crabJobs"]=232
sam["data_MinimumBias_2015_JuneNoise"]["GT"]='80X_dataRun2_v13'
sam["data_MinimumBias_2015_JuneNoise"]["name"]='data_MinimumBias_2015_JuneNoise'
sam["data_MinimumBias_2015_JuneNoise"]["isData"]=True
sam["data_MinimumBias_2015_JuneNoise"]["numEvents"]=-1
sam["data_MinimumBias_2015_JuneNoise"]["pathSE"]='srm://grid-srm.physik.rwth-aachen.de:8443/srm/managerv2?SFN=/pnfs/physik.rwth-aachen.de/cms/store/user/rulrich/CastorNoise/EmptyBX/NoiseAna_Castor_data_MinimumBias_2015_JuneNoise/170902_232917/0000'
sam["data_MinimumBias_2015_JuneNoise"]["pathTrees"]='XXXTMFTTree/CastorNoise/EmptyBX/NoiseAna_Castor_data_MinimumBias_2015_JuneNoise/170902_232917/0000'
sam["data_MinimumBias_2015_JuneNoise"]["json"]='muon_2015_0.0T_RUN247920.json'
sam["data_MinimumBias_2015_JuneNoise"]["lumiMinBias"]=-1
sam["data_MinimumBias_2015_JuneNoise"]["XS"]=-1
#sam["data_MinimumBias_2015_JuneNoise"]["pathPAT"]='/XXXTMFPAT/store/user/makbiyik/CastorMuon2015/muon_2015_JuneNoise//'
#sam["data_MinimumBias_2015_JuneNoise"]["DS"]='/EmptyBX/Run2015A-27Jan2016-v1/MINIAOD' # NO castor at all in miniaod ?????
sam["data_MinimumBias_2015_JuneNoise"]["DS"]='/EmptyBX/Run2015A-v1/RAW'


sam["data_MinimumBias_2015_JuneZB"]={}
sam["data_MinimumBias_2015_JuneZB"]["crabJobs"]=232
sam["data_MinimumBias_2015_JuneZB"]["GT"]='80X_dataRun2_v13'
sam["data_MinimumBias_2015_JuneZB"]["name"]='data_MinimumBias_2015_JuneZB'
sam["data_MinimumBias_2015_JuneZB"]["isData"]=True
sam["data_MinimumBias_2015_JuneZB"]["numEvents"]=-1
sam["data_MinimumBias_2015_JuneZB"]["pathSE"]='srm://grid-srm.physik.rwth-aachen.de:8443/srm/managerv2?SFN=/pnfs/physik.rwth-aachen.de/cms/store/user/rulrich/CastorNoise/ZeroBias/NoiseAna_Castor_data_MinimumBias_2015_JuneZB/170903_234710/0000'
sam["data_MinimumBias_2015_JuneZB"]["pathTrees"]='XXXTMFTTree/CastorNoise/ZeroBias/NoiseAna_Castor_data_MinimumBias_2015_JuneZB/170903_234710/0000'
sam["data_MinimumBias_2015_JuneZB"]["json"]='muon_2015_0.0T_RUN247920.json'
sam["data_MinimumBias_2015_JuneZB"]["lumiMinBias"]=-1
sam["data_MinimumBias_2015_JuneZB"]["XS"]=-1
#sam["data_MinimumBias_2015_JuneZB"]["pathPAT"]='/XXXTMFPAT/store/user/makbiyik/CastorMuon2015/muon_2015_JuneZB//'
#sam["data_MinimumBias_2015_JuneZB"]["DS"]='/ZeroBias/Run2015A-v1/RAW'
sam["data_MinimumBias_2015_JuneZB"]["DS"]='/ZeroBias/Run2015A-27Jan2016-v2/AOD' # T2_HU_Budapest


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
