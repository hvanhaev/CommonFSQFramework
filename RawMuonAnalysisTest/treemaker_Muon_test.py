import FWCore.ParameterSet.Config as cms
import CommonFSQFramework.Core.Util
import os

# this is important to get the right trigger setup
from Configuration.StandardSequences.Eras import eras
process = cms.Process("Treemaker",eras.Run2_2016)

process.load("FWCore.MessageService.MessageLogger_cfi")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff')
process.load('Configuration.StandardSequences.RawToDigi_Data_cff')
process.load('Configuration.StandardSequences.Reconstruction_Data_cff')
process.load("CondCore.CondDB.CondDB_cfi")

process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(100))
process.MessageLogger.cerr.FwkReport.reportEvery = 1
process.options = cms.untracked.PSet(wantSummary = cms.untracked.bool(True))


# Source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        '/store/data/PARun2016A/PACastor/RAW/v1/000/284/717/00000/586B780E-1AA4-E611-BA30-02163E012710.root' # example file from circulating beam run 284717
    )
)


# Geometry and Detector Conditions
process.load("Configuration.Geometry.GeometryRecoDB_cff")
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '80X_dataRun2_Prompt_v14', '')

# Here starts the CFF specific part
import CommonFSQFramework.Core.customizePAT
process = CommonFSQFramework.Core.customizePAT.customize(process)

# GT customization
process = CommonFSQFramework.Core.customizePAT.customizeGT(process)

# define treeproducer
process.CFFTree = cms.EDAnalyzer("CFFTreeProducer")

import CommonFSQFramework.Core.CastorViewsConfigs
import CommonFSQFramework.Core.TriggerResultsViewsConfigs

process.CFFTree._Parameterizable__setParameters(CommonFSQFramework.Core.CastorViewsConfigs.get(["CastorRecHitViewFull"]))
process.CFFTree._Parameterizable__setParameters(CommonFSQFramework.Core.TriggerResultsViewsConfigs.get(["CastorPATriggerResultsView","L1GTriggerResultsView"]))

# add paths

# need global CMS reconstruction if we run on RAW data!
process.raw2digi_step = cms.Path(process.RawToDigi)
process.reconstruction_step = cms.Path(process.reconstruction)

process = CommonFSQFramework.Core.customizePAT.addPath(process, process.raw2digi_step)
process = CommonFSQFramework.Core.customizePAT.addPath(process, process.reconstruction_step)
process = CommonFSQFramework.Core.customizePAT.addTreeProducer(process, process.CFFTree)
