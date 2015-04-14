anaVersion="RunIIWinter15GS_14042015"
anaType="RunIIWinter15GS"



sam = {}

sam["MinBias_TuneMonash13_13TeV-pythia8"]={}
sam["MinBias_TuneMonash13_13TeV-pythia8"]["crabJobs"]=100
sam["MinBias_TuneMonash13_13TeV-pythia8"]["GT"]='MCRUN2_71_V0::All'
sam["MinBias_TuneMonash13_13TeV-pythia8"]["name"]='MinBias_TuneMonash13_13TeV-pythia8'
sam["MinBias_TuneMonash13_13TeV-pythia8"]["isData"]=False
sam["MinBias_TuneMonash13_13TeV-pythia8"]["numEvents"]=998368
sam["MinBias_TuneMonash13_13TeV-pythia8"]["json"]=''
sam["MinBias_TuneMonash13_13TeV-pythia8"]["lumiMinBias"]=1.273129775664895e-05
sam["MinBias_TuneMonash13_13TeV-pythia8"]["XS"]=78418400000.0
sam["MinBias_TuneMonash13_13TeV-pythia8"]["DS"]='/MinBias_TuneMonash13_13TeV-pythia8/RunIIWinter15GS-castor_MCRUN2_71_V0-v1/GEN-SIM'


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
