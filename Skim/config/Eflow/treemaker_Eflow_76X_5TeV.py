import FWCore.ParameterSet.Config as cms
import CommonFSQFramework.Core.Util
import os

isData = False

if "TMFSampleName" not in os.environ:
    print "TMFSampleName not found, assuming we are running on MC"
else:
    s = os.environ["TMFSampleName"]
    sampleList=CommonFSQFramework.Core.Util.getAnaDefinition("sam")
    isData =  sampleList[s]["isData"]
    if isData: print "Disabling MC-specific features for sample",s
        
	

process = cms.Process("Treemaker")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(1000))

process.MessageLogger.cerr.FwkReport.reportEvery = 1000
process.options = cms.untracked.PSet(wantSummary = cms.untracked.bool(True))

# Source
process.source = cms.Source("PoolSource",
    #fileNames = cms.untracked.vstring('root://xrootd-cms.infn.it//store/user/katkov/MinBias_CUETP8M1_pp502TeV-pythia8/MinBias_CUETP8M1_pp502TeV-pythia8_MagnetOn_CASTOR00SL_RECO_v02/160223_131547/0000/MinBias_CUETP8M1_pp502TeV-pythia8_CASTOR00_MagnetOn_RECO_1.root')
    fileNames = cms.untracked.vstring('root://xrootd-cms.infn.it//store/data/Run2015E/ZeroBias/RECO/PromptReco-v1/000/262/169/00000/34DAC4FF-3D94-E511-8980-02163E014150.root')
)

# Geometry and Detector Conditions
process.load("Configuration.Geometry.GeometryRecoDB_cff")
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
if isData: process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_data', '')
if not isData: process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_mc', '')
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load("Configuration.StandardSequences.Reconstruction_cff")


# produce HF PFClusters
process.PFClustersHF = cms.Path(process.particleFlowRecHitHF*process.particleFlowClusterHF)

# Here starts the CFF specific part
import CommonFSQFramework.Core.customizePAT
process = CommonFSQFramework.Core.customizePAT.customize(process)

# GT customization
#process = CommonFSQFramework.Core.customizePAT.customizeGT(process)

# define treeproducer
process.EflowTree = cms.EDAnalyzer("CFFTreeProducer")

import CommonFSQFramework.Core.VerticesViewsConfigs
import CommonFSQFramework.Core.CaloRecHitViewsConfigs
import CommonFSQFramework.Core.CaloTowerViewsConfigs
import CommonFSQFramework.Core.CastorViewsConfigs
import CommonFSQFramework.Core.PFObjectsViewsConfigs
import CommonFSQFramework.Core.TriggerResultsViewsConfigs

if not isData:
    import CommonFSQFramework.Core.GenLevelViewsConfigs
    

process.EflowTree._Parameterizable__setParameters(CommonFSQFramework.Core.VerticesViewsConfigs.get(["VerticesView"]))
process.EflowTree._Parameterizable__setParameters(CommonFSQFramework.Core.CaloRecHitViewsConfigs.get(["EcalRecHitView","HBHERecHitView","HFRecHitView"]))
process.EflowTree._Parameterizable__setParameters(CommonFSQFramework.Core.CaloTowerViewsConfigs.get(["CaloTowerView"]))
process.EflowTree._Parameterizable__setParameters(CommonFSQFramework.Core.CastorViewsConfigs.get(["CastorRecHitViewFull","CastorTowerView"]))
process.EflowTree._Parameterizable__setParameters(CommonFSQFramework.Core.PFObjectsViewsConfigs.get(["PFCandidateView","ecalPFClusterView","hcalPFClusterView","hfPFClusterView"]))
if isData: process.EflowTree._Parameterizable__setParameters(CommonFSQFramework.Core.TriggerResultsViewsConfigs.get(["ZeroBiasWithPSRun2015E","L1GTriggerResultsView"]))

if not isData:
    process.EflowTree._Parameterizable__setParameters(CommonFSQFramework.Core.GenLevelViewsConfigs.get(["GenPartView"]))


process = CommonFSQFramework.Core.customizePAT.addPath(process, process.PFClustersHF)
process = CommonFSQFramework.Core.customizePAT.addTreeProducer(process, process.EflowTree)
