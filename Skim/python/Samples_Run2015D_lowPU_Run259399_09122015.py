anaVersion="Run2015D_lowPU_Run259399_09122015"
anaType="Run2015D_lowPU"

cbSmartCommand="smartCopy"
cbSmartBlackList=""
cbWMS="https://wmscms.cern.ch:7443/glite_wms_wmproxy_server"
skimEfficiencyMethod="getSkimEff"

sam = {}

sam["data_EmptyBX"]={}
sam["data_EmptyBX"]["crabJobs"]=0
sam["data_EmptyBX"]["GT"]='74X_dataRun2_Prompt_v4'
sam["data_EmptyBX"]["name"]='data_EmptyBX'
sam["data_EmptyBX"]["isData"]=True
sam["data_EmptyBX"]["numEvents"]=-1
sam["data_EmptyBX"]["pathSE"]='srm://maite.iihe.ac.be:8443/srm/managerv2?SFN=/pnfs/iihe/cms/store/user/hvanhaev/EmptyBX/Run2015D_lowPU_Run259399_09122015_data_EmptyBX/151209_215632/0000/'
sam["data_EmptyBX"]["pathTrees"]='/XXXTMFTTree/store/user/hvanhaev/EmptyBX/Run2015D_lowPU_Run259399_09122015_data_EmptyBX/151209_215632/0000//'
sam["data_EmptyBX"]["json"]='CommonFSQFramework/Skim/lumi/Run259399.json'
sam["data_EmptyBX"]["lumiMinBias"]=-1
sam["data_EmptyBX"]["XS"]=-1
sam["data_EmptyBX"]["pathPAT"]='/XXXTMFPAT/store/user/hvanhaev/EmptyBX/Run2015D_lowPU_Run259399_09122015_data_EmptyBX/151209_215632/0000//'
sam["data_EmptyBX"]["DS"]='/EmptyBX/Run2015D-PromptReco-v4/RECO'

sam["data_ZeroBias"]={}
sam["data_ZeroBias"]["crabJobs"]=0
sam["data_ZeroBias"]["GT"]='74X_dataRun2_Prompt_v4'
sam["data_ZeroBias"]["name"]='data_ZeroBias'
sam["data_ZeroBias"]["isData"]=True
sam["data_ZeroBias"]["numEvents"]=-1
sam["data_ZeroBias"]["pathSE"]='srm://maite.iihe.ac.be:8443/srm/managerv2?SFN=/pnfs/iihe/cms/store/user/hvanhaev/ZeroBias/Run2015D_lowPU_Run259399_09122015_data_ZeroBias/151209_215649/0000/'
sam["data_ZeroBias"]["pathTrees"]='/XXXTMFTTree/store/user/hvanhaev/ZeroBias/Run2015D_lowPU_Run259399_09122015_data_ZeroBias/151209_215649/0000//'
sam["data_ZeroBias"]["json"]='CommonFSQFramework/Skim/lumi/Run259399.json'
sam["data_ZeroBias"]["lumiMinBias"]=-1
sam["data_ZeroBias"]["XS"]=-1
sam["data_ZeroBias"]["pathPAT"]='/XXXTMFPAT/store/user/hvanhaev/ZeroBias/Run2015D_lowPU_Run259399_09122015_data_ZeroBias/151209_215649/0000//'
sam["data_ZeroBias"]["DS"]='/ZeroBias/Run2015D-PromptReco-v4/RECO'


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
