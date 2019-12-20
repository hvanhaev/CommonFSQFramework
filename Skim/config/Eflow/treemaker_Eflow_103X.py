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

process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(10000))

process.MessageLogger.cerr.FwkReport.reportEvery = 1000
process.options = cms.untracked.PSet(wantSummary = cms.untracked.bool(True))

# Source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring("root://cms-xrd-global.cern.ch//store/hidata/HIRun2018A/HIForward/AOD/04Apr2019-v1/280000/A0C075F1-F488-4547-8CA5-27034DB0F114.root")
    #fileNames = cms.untracked.vstring("root://cms-xrd-global.cern.ch//store/user/hvanhaev/MinBias/HINPbPb2018-RECO-00003_103X_upgrade2018_realistic_HI_v9/181112_130435/0000/step2_99.root")    
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
import CommonFSQFramework.Core.VerticesViewsConfigs
import CommonFSQFramework.Core.TriggerResultsViewsConfigs

process.EflowTree._Parameterizable__setParameters(CommonFSQFramework.Core.VerticesViewsConfigs.get(["VerticesView"]))
process.EflowTree._Parameterizable__setParameters(CommonFSQFramework.Core.CaloTowerViewsConfigs.get(["CaloTowerView"]))
process.EflowTree._Parameterizable__setParameters(CommonFSQFramework.Core.CastorViewsConfigs.get(["CastorRecHitViewFull","CastorTowerView","ak5CastorJetView"]))
if isData: process.EflowTree._Parameterizable__setParameters(CommonFSQFramework.Core.TriggerResultsViewsConfigs.get(["HIRun2018ATriggers"]))

process = CommonFSQFramework.Core.customizePAT.addTreeProducer(process, process.EflowTree)
