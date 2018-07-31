import FWCore.ParameterSet.Config as cms
import CommonFSQFramework.Core.Util
import os

isData = False
useCustomCond = False

# this is important to get the right trigger setup
from Configuration.StandardSequences.Eras import eras

process = cms.Process("Treemaker")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.load("Configuration.Geometry.GeometryRecoDB_cff")
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load("Configuration.StandardSequences.Reconstruction_cff")
process.load("Configuration.StandardSequences.RawToDigi_cff")

from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_data', '')

# Source
process.source = cms.Source("PoolSource",
     fileNames = cms.untracked.vstring('root://cmsxrootd.fnal.gov///store/data/Run2018C/ZeroBias/RAW/v1/000/320/249/00000/A4958224-1890-E811-BBA0-FA163E5BFF9D.root')
)

process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(100))
process.MessageLogger.cerr.FwkReport.reportEvery = 1
process.options = cms.untracked.PSet(wantSummary = cms.untracked.bool(True))


# get custom CASTOR conditions to mark/remove bad channels
if useCustomCond:
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


# Here starts the CFF specific part
import CommonFSQFramework.Core.customizePAT
process = CommonFSQFramework.Core.customizePAT.customize(process)
process = CommonFSQFramework.Core.customizePAT.customizeGT(process)

# define treeproducer
process.CFFTree = cms.EDAnalyzer("CFFTreeProducer")


#import CommonFSQFramework.Core.CaloRecHitViewsConfigs
#import CommonFSQFramework.Core.CaloTowerViewsConfigs
import CommonFSQFramework.Core.CastorViewsConfigs
#import CommonFSQFramework.Core.PFObjectsViewsConfigs
import CommonFSQFramework.Core.TriggerResultsViewsConfigs


process.CFFTree._Parameterizable__setParameters(CommonFSQFramework.Core.CastorViewsConfigs.get(["CastorRecHitViewFull"]))
#process.CFFTree._Parameterizable__setParameters(CommonFSQFramework.Core.TriggerResultsViewsConfigs.get(["L1GTriggerResultsView"]))
#process.CFFTree._Parameterizable__setParameters(CommonFSQFramework.Core.CaloRecHitViewsConfigs.get(["HFRecHitView"]))
#process.CFFTree._Parameterizable__setParameters(CommonFSQFramework.Core.CaloTowerViewsConfigs.get(["CaloTowerView"]))
#process.CFFTree._Parameterizable__setParameters(CommonFSQFramework.Core.CastorViewsConfigs.get(["CastorRecHitViewFull","CastorTowerView"]))
#process.CFFTree._Parameterizable__setParameters(CommonFSQFramework.Core.PFObjectsViewsConfigs.get(["PFCandidateView","ecalPFClusterView","hcalPFClusterView","hfPFClusterView"]))

process.raw2digi_step = cms.Path(process.L1TRawToDigi*process.castorDigis)
process.raw2digi_step = cms.Path(process.castorDigis)
#process.castorreco_step = cms.Path(process.reconstruction)
process.castorreco_step = cms.Path(process.castorreco) # CastorFullReco)

process = CommonFSQFramework.Core.customizePAT.addPath(process, process.raw2digi_step)
process = CommonFSQFramework.Core.customizePAT.addPath(process, process.castorreco_step)
process = CommonFSQFramework.Core.customizePAT.addTreeProducer(process, process.CFFTree)
