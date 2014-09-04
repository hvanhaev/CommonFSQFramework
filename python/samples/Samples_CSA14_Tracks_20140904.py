anaVersion="CSA14_Tracks_20140904"
anaType="CSA14_Tracks"

cbSmartCommand="smartCopy"
cbSmartBlackList=""
cbWMS="https://wmscms.cern.ch:7443/glite_wms_wmproxy_server"
skimEfficiencyMethod="getSkimEff"
MyVariablesAllEvents="DiJetAnalysis.DiJetAna.ana.BaseVariables"

rootPath="/scratch/scratch0/tfruboes/DATA_dijet/CSA14_Tracks_20140904/"
sam = {}

sam["MinBias_TuneMonash13_13TeV-pythia8"]={}
sam["MinBias_TuneMonash13_13TeV-pythia8"]["sgeJobs"]=50
sam["MinBias_TuneMonash13_13TeV-pythia8"]["numEvents"]=-1
sam["MinBias_TuneMonash13_13TeV-pythia8"]["GT"]='POSTLS170_V6::All'
sam["MinBias_TuneMonash13_13TeV-pythia8"]["weightJet15"]='RooFormulaVar("weight","weight", "xsOverEvents*puWeightJet15V4*trgWeightJet15RawTF2*trgWeightJet15L1RawTF2", RooArgList(v["puWeightJet15V4"]["RooVar"],v["trgWeightJet15RawTF2"]["RooVar"],v["trgWeightJet15L1RawTF2"]["RooVar"]))'
sam["MinBias_TuneMonash13_13TeV-pythia8"]["name"]='MinBias_TuneMonash13_13TeV-pythia8'
sam["MinBias_TuneMonash13_13TeV-pythia8"]["isData"]=False
sam["MinBias_TuneMonash13_13TeV-pythia8"]["weightPuOnly"]='RooFormulaVar("weight","weight", "xsOverEvents*puWeightJet15V4", RooArgList(v["puWeightJet15V4"]["RooVar"]))'
sam["MinBias_TuneMonash13_13TeV-pythia8"]["weightJet15Inverse"]='RooFormulaVar("weight","weight", "xsOverEvents*puWeightJet15V4", RooArgList(v["puWeightJet15V4"]["RooVar"]))'
sam["MinBias_TuneMonash13_13TeV-pythia8"]["crabJobs"]=100
sam["MinBias_TuneMonash13_13TeV-pythia8"]["weightNoPu"]='RooFormulaVar("weight","weight", "xsOverEvents", RooArgList())'
sam["MinBias_TuneMonash13_13TeV-pythia8"]["json"]=''
sam["MinBias_TuneMonash13_13TeV-pythia8"]["lumiMinBias"]='crashMeMC'
sam["MinBias_TuneMonash13_13TeV-pythia8"]["XS"]=78000000000.0
sam["MinBias_TuneMonash13_13TeV-pythia8"]["DS"]='/MinBias_TuneMonash13_13TeV-pythia8/Spring14dr-castor_NoPileUp_POSTLS170_V6-v1/AODSIM'

sam["data_MinBias_TuneCUETP8S1-HERAPDF_13TeV-pythia8"]={}
sam["data_MinBias_TuneCUETP8S1-HERAPDF_13TeV-pythia8"]["sgeJobs"]=50
sam["data_MinBias_TuneCUETP8S1-HERAPDF_13TeV-pythia8"]["numEvents"]=-1
sam["data_MinBias_TuneCUETP8S1-HERAPDF_13TeV-pythia8"]["GT"]='POSTLS170_V6::All'
sam["data_MinBias_TuneCUETP8S1-HERAPDF_13TeV-pythia8"]["name"]='data_MinBias_TuneCUETP8S1-HERAPDF_13TeV-pythia8'
sam["data_MinBias_TuneCUETP8S1-HERAPDF_13TeV-pythia8"]["isData"]=True
sam["data_MinBias_TuneCUETP8S1-HERAPDF_13TeV-pythia8"]["weightJet15Inverse"]='RooFormulaVar("weight","weight", "invtrgWeightJet15RawTF2", RooArgList(v["invtrgWeightJet15RawTF2"]["RooVar"]))'
sam["data_MinBias_TuneCUETP8S1-HERAPDF_13TeV-pythia8"]["crabJobs"]=100
sam["data_MinBias_TuneCUETP8S1-HERAPDF_13TeV-pythia8"]["json"]=''
sam["data_MinBias_TuneCUETP8S1-HERAPDF_13TeV-pythia8"]["lumiMinBias"]=0.00012219984697781178
sam["data_MinBias_TuneCUETP8S1-HERAPDF_13TeV-pythia8"]["XS"]=-1
sam["data_MinBias_TuneCUETP8S1-HERAPDF_13TeV-pythia8"]["DS"]='/MinBias_TuneCUETP8S1-HERAPDF_13TeV-pythia8/Spring14dr-castor_NoPileUp_POSTLS170_V6-v1/AODSIM'

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
