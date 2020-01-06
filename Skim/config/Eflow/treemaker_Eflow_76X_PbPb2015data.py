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
    fileNames = cms.untracked.vstring("root://cms-xrd-global.cern.ch//store/hidata/HIRun2015/HIMinimumBias1/AOD/02May2016-v1/120002/0AA1E877-7013-E711-A48A-002481CFE864.root")
)

# Geometry and Detector Conditions
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
if isData: process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_data', '')
if not isData: process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_mc', '')

# load offline CASTOR conditions
process.load("CondCore.DBCommon.CondDBSetup_cfi") 
process.CastorDbProducer = cms.ESProducer("CastorDbProducer") 
 
process.es_ascii = cms.ESSource("CastorTextCalibrations", 
   input = cms.VPSet( 
       cms.PSet( 
            object = cms.string('Gains'), 
            file = cms.FileInPath('data/CastorCond/intercalibration_2015_HI_4T_Nov.txt') 
        ), 
       cms.PSet( 
           object = cms.string('ChannelQuality'), 
           file = cms.FileInPath('data/CastorCond/BadChannels_2015pp5TeV.txt') 
       ),  
   ) 
)
process.es_prefer_castor = cms.ESPrefer('CastorTextCalibrations','es_ascii')

# Castor ReReco
process.load('RecoLocalCalo.Castor.Castor_cff')
process.rechitcorrector = cms.EDProducer("RecHitCorrector",
        rechitLabel = cms.InputTag("castorreco","","ppRECO"), # choose the original RecHit collection
        revertFactor = cms.double(1),
        doInterCalib = cms.bool(True)
) # do intercalibration
process.CastorTowerReco.inputprocess = "rechitcorrector"
process.CastorReReco = cms.Path(process.rechitcorrector*process.CastorFullReco)

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
process.EflowTree._Parameterizable__setParameters(CommonFSQFramework.Core.CastorViewsConfigs.get(["CastorRecHitViewFullCorrected","CastorTowerView","ak5CastorJetView"]))
if isData: process.EflowTree._Parameterizable__setParameters(CommonFSQFramework.Core.TriggerResultsViewsConfigs.get(["HIRun2015Triggers"]))

# add paths
if isData:
    process = CommonFSQFramework.Core.customizePAT.addPath(process, process.CastorReReco)

process = CommonFSQFramework.Core.customizePAT.addTreeProducer(process, process.EflowTree)

