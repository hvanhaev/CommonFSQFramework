import FWCore.ParameterSet.Config as cms
import CommonFSQFramework.Core.Util
import os

isData = False

process = cms.Process("Treemaker")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(100))

process.MessageLogger.cerr.FwkReport.reportEvery = 1
process.options = cms.untracked.PSet(wantSummary = cms.untracked.bool(True))

# Source
process.source = cms.Source("PoolSource",
    #fileNames = cms.untracked.vstring('/store/data/Run2015A/ZeroBias1/RECO/PromptReco-v1/000/247/324/00000/02BDFA64-B40E-E511-8CB7-02163E012ACF.root')
    fileNames = cms.untracked.vstring('/store/user/sbaur/MinBias_CUETP8M1_13TeV-pythia8/MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORmeasured_RECO/160207_214204/0000/MinBias_CUETP8M1_13TeV-pythia8_CASTORmeasured_RECO_1.root')
    #fileNames = cms.untracked.vstring('/store/data/Run2015A/CastorJets/RECO/PromptReco-v1/000/247/607/00000/5AB25486-9410-E511-91D5-02163E0133E6.root')
)

# Geometry and Detector Conditions
process.load("Configuration.Geometry.GeometryRecoDB_cff")
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
if isData: process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_data', '')
if not isData: process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_mc', '')
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load("Configuration.StandardSequences.Reconstruction_cff")

# get custom CASTOR conditions to mark/remove bad channels
process.load("CondCore.DBCommon.CondDBSetup_cfi")
process.CastorDbProducer = cms.ESProducer("CastorDbProducer")

process.es_ascii = cms.ESSource("CastorTextCalibrations",
   input = cms.VPSet(
       cms.PSet(
           object = cms.string('ChannelQuality'),
           file = cms.FileInPath('data/customcond/castor/BadChannels2015.txt')
       ),
   )
)

process.es_prefer_castor = cms.ESPrefer('CastorTextCalibrations','es_ascii')

# for MC reproduce the CastorTowers and CastorJets to remove the bad channels there
if not isData:
    process.load('RecoLocalCalo.Castor.Castor_cff')
    process.CastorReReco = cms.Path(process.CastorFullReco)

# produce HF PFClusters
process.PFClustersHF = cms.Path(process.particleFlowRecHitHF*process.particleFlowClusterHF)

# in data produce Tracker RecHits
if isData:
    process.PixelRecHits = cms.Path(process.siPixelRecHits)
process.StripMatchedRecHits = cms.Path(process.siStripMatchedRecHits)

if not isData:
    # Add ak5GenJets #
    process.load('RecoJets.Configuration.GenJetParticles_cff')
    process.load('RecoJets.Configuration.RecoGenJets_cff')
    from RecoJets.JetProducers.ak5GenJets_cfi import ak5GenJets
    from RecoJets.JetProducers.ak5GenJets_cfi import ak5GenJets
    process.lowPtak5GenJets = ak5GenJets.clone(jetPtMin = 0.5 )
    process.LowPtGenJetsReCluster = cms.Path(process.genParticlesForJets*process.lowPtak5GenJets) 

# Here starts the CFF specific part
import CommonFSQFramework.Core.customizePAT
process = CommonFSQFramework.Core.customizePAT.customize(process)

# GT customization
process = CommonFSQFramework.Core.customizePAT.customizeGT(process)

# define treeproducer
process.CFFTree = cms.EDAnalyzer("CFFTreeProducer")

import CommonFSQFramework.Core.VerticesViewsConfigs
import CommonFSQFramework.Core.CaloRecHitViewsConfigs
import CommonFSQFramework.Core.CaloTowerViewsConfigs
import CommonFSQFramework.Core.CastorViewsConfigs
import CommonFSQFramework.Core.PFObjectsViewsConfigs
import CommonFSQFramework.Core.TriggerResultsViewsConfigs

if not isData:
    process.CFFTree._Parameterizable__setParameters(CommonFSQFramework.Core.VerticesViewsConfigs.get(["VerticesView","ZeroTeslaVertexView_Pixel_PreSplitting","ZeroTeslaVertexView_Pixel_noPreSplitting","ZeroTeslaVertexView_Strips"]))
if isData:
    process.CFFTree._Parameterizable__setParameters(CommonFSQFramework.Core.VerticesViewsConfigs.get(["VerticesView","ZeroTeslaVertexView_Pixel_noPreSplitting","ZeroTeslaVertexView_Strips"]))

process.CFFTree._Parameterizable__setParameters(CommonFSQFramework.Core.CaloRecHitViewsConfigs.get(["EcalRecHitView","HBHERecHitView","HFRecHitView"]))
process.CFFTree._Parameterizable__setParameters(CommonFSQFramework.Core.CaloTowerViewsConfigs.get(["CaloTowerView"]))
process.CFFTree._Parameterizable__setParameters(CommonFSQFramework.Core.CastorViewsConfigs.get(["CastorRecHitViewFull","CastorTowerView","ak5CastorJetView"]))
process.CFFTree._Parameterizable__setParameters(CommonFSQFramework.Core.PFObjectsViewsConfigs.get(["PFCandidateView","ecalPFClusterView","hcalPFClusterView","hfPFClusterView"]))
process.CFFTree._Parameterizable__setParameters(CommonFSQFramework.Core.TriggerResultsViewsConfigs.get(["CastorSpecialJetTriggerResultsView","L1GTriggerResultsView"]))

if isData:
    process.CFFTree._Parameterizable__setParameters(CommonFSQFramework.Core.TriggerResultsViewsConfigs.get(["ZeroBiasTriggerResultsViewWithPS"]))
if not isData:
    import CommonFSQFramework.Core.GenLevelViewsConfigs
    process.CFFTree._Parameterizable__setParameters(CommonFSQFramework.Core.GenLevelViewsConfigs.get(["GenPartView","lowPtak5GenJetView"]))

# add paths
if not isData:
    process = CommonFSQFramework.Core.customizePAT.addPath(process, process.CastorReReco)
    process = CommonFSQFramework.Core.customizePAT.addPath(process, process.LowPtGenJetsReCluster)

process = CommonFSQFramework.Core.customizePAT.addPath(process, process.PFClustersHF)
if isData:
    process = CommonFSQFramework.Core.customizePAT.addPath(process, process.PixelRecHits)
process = CommonFSQFramework.Core.customizePAT.addPath(process, process.StripMatchedRecHits)

process = CommonFSQFramework.Core.customizePAT.addTreeProducer(process, process.CFFTree)
