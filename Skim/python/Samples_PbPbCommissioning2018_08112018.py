anaVersion="PbPbCommissioning2018_08112018"
anaType="PbPbCommissioning2018"

cbSmartCommand="smartCopy"
cbSmartBlackList=""
cbWMS="https://wmscms.cern.ch:7443/glite_wms_wmproxy_server"
skimEfficiencyMethod="getSkimEff"

sam = {}

sam["data_HIExpressPhysics"]={}
sam["data_HIExpressPhysics"]["crabJobs"]=0
sam["data_HIExpressPhysics"]["GT"]='103X_dataRun2_Express_v2'
sam["data_HIExpressPhysics"]["name"]='data_HIExpressPhysics'
sam["data_HIExpressPhysics"]["isData"]=True
sam["data_HIExpressPhysics"]["numEvents"]=-1
sam["data_HIExpressPhysics"]["pathSE"]='srm://maite.iihe.ac.be:8443/srm/managerv2?SFN=/pnfs/iihe/cms/store/user/hvanhaev/HIExpressPhysics/PbPbCommissioning2018_08112018_data_HIExpressPhysics/181108_155459/0000/'
sam["data_HIExpressPhysics"]["pathTrees"]='/XXXTMFTTree/store/user/hvanhaev/HIExpressPhysics/PbPbCommissioning2018_08112018_data_HIExpressPhysics/181108_155459/0000//'
sam["data_HIExpressPhysics"]["json"]='CommonFSQFramework/Skim/lumi/PbPbCommissioning2018.json'
sam["data_HIExpressPhysics"]["lumiMinBias"]=-1
sam["data_HIExpressPhysics"]["XS"]=-1
sam["data_HIExpressPhysics"]["pathPAT"]='/XXXTMFPAT/store/user/hvanhaev/HIExpressPhysics/PbPbCommissioning2018_08112018_data_HIExpressPhysics/181108_155459/0000//'
sam["data_HIExpressPhysics"]["DS"]='/HIExpressPhysics/HIRun2018-Express-v1/FEVT'


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
