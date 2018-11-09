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
    fileNames = cms.untracked.vstring("root://cms-xrd-global.cern.ch//store/express/HIRun2018/HIExpressPhysics/FEVT/Express-v1/000/326/176/00000/614D3946-4465-3248-853F-9C214A33CFF8.root")
)

# Geometry and Detector Conditions
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
if isData: process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_data', '')
if not isData: process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_mc', '')


# Here starts the CFF specific part
import CommonFSQFramework.Core.customizePAT
process = CommonFSQFramework.Core.customizePAT.customize(process)

# GT customization
process = CommonFSQFramework.Core.customizePAT.customizeGT(process)

# define treeproducer
process.EflowTree = cms.EDAnalyzer("CFFTreeProducer")

import CommonFSQFramework.Core.CaloTowerViewsConfigs
import CommonFSQFramework.Core.CastorViewsConfigs

process.EflowTree._Parameterizable__setParameters(CommonFSQFramework.Core.CaloTowerViewsConfigs.get(["CaloTowerView"]))
process.EflowTree._Parameterizable__setParameters(CommonFSQFramework.Core.CastorViewsConfigs.get(["CastorRecHitViewFull","CastorTowerView","ak5CastorJetView"]))

process = CommonFSQFramework.Core.customizePAT.addTreeProducer(process, process.EflowTree)
