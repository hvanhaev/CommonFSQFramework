anaVersion="MuonAna_CastorMuons"
anaType="MuonAna_CastorMuons"

cbSmartCommand="smartCopy"
cbSmartBlackList=""
cbWMS="https://wmscms.cern.ch:7443/glite_wms_wmproxy_server"
skimEfficiencyMethod="getSkimEff"

sam = {}


# CFF Skim using interfill data from run PARun2016B
# pPbRun on RAW data 

sam["data_ALICERun_2016"] = {}
sam["data_ALICERun_2016"]["crabJobs"] = 232
sam["data_ALICERun_2016"]["GT"] = '80X_dataRun2_Prompt_v15'
sam["data_ALICERun_2016"]["name"] = 'data_ALICERun_2016'
sam["data_ALICERun_2016"]["isData"] = True
sam["data_ALICERun_2016"]["numEvents"] = -1
sam["data_ALICERun_2016"]["pathSE"] = 'srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=/pnfs/desy.de/cms/tier2/store/user/rulrich/ALICERun2016/PACastor/MuonAna_CastorMuons_data_ALICERun_2016/170902_235259/0000'
sam["data_ALICERun_2016"]["pathTrees"] = 'XXXTMFTTree/ALICERun2016/PACastor/MuonAna_CastorMuons_data_ALICERun_2016/170902_235259/0000'
sam["data_ALICERun_2016"]["json"] = 'ALICERun2016.json'
sam["data_ALICERun_2016"]["lumiMinBias"] = -1
sam["data_ALICERun_2016"]["XS"] = -1
#sam["data_ALICERun_2016"]["pathPAT"]='/XXXTMFPAT/store/user/rulrich/CastorMuons/PACastor///'
sam["data_ALICERun_2016"]["DS"] = '/PACastor/PARun2016B-v1/RAW'




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
