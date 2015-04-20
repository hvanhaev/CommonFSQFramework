import FWCore.ParameterSet.Config as cms

process = cms.Process("Treemaker")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(1000))

process.MessageLogger.cerr.FwkReport.reportEvery = 10000
process.options = cms.untracked.PSet(wantSummary = cms.untracked.bool(True))

# Source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('file:00E5660A-47C7-E411-9E5B-0025905A48F0.root')
)

# Geometry and Detector Conditions
process.load("Configuration.Geometry.GeometryRecoDB_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_mc')
process.load("Configuration.StandardSequences.MagneticField_cff")

######################
# load low-pt charged GenJet configuration here
# get charged genParticles
process.load('QCDAnalysis.UEAnalysis.UEAnalysisParticles_cfi')
process.chargeParticles.cut = cms.string('charge != 0 & pt > 0.3 & status = 1')
# get genjet definitions
from RecoJets.JetProducers.ak4GenJets_cfi import ak4GenJets
from RecoJets.JetProducers.ak5GenJets_cfi import ak5GenJets
# clone normal ak4 genjets
process.ak4ChgGenJets = ak4GenJets.clone(
src = cms.InputTag("chargeParticles"),
jetPtMin = cms.double(0.3)
)
# clone normal ak5 genjets
process.ak5ChgGenJets = ak5GenJets.clone( 
src = cms.InputTag("chargeParticles"),
jetPtMin = cms.double(0.3)
)
# add the processes
process.chargedgenjets = cms.Path(process.UEAnalysisParticles*process.ak4ChgGenJets*process.ak5ChgGenJets)
######################

# Here starts the CFF specific part
import CommonFSQFramework.Core.customizePAT
process = CommonFSQFramework.Core.customizePAT.customize(process)

# GT customization
process = CommonFSQFramework.Core.customizePAT.customizeGT(process)

# define treeproducer
process.GenLevelTree = cms.EDAnalyzer("CFFTreeProducer")
import CommonFSQFramework.Core.GenLevelViewsConfigs
process.GenLevelTree._Parameterizable__setParameters(CommonFSQFramework.Core.GenLevelViewsConfigs.get(["GenPartView","ak4GenJetView","ak5GenJetView","ak4ChgGenJetView","ak5ChgGenJetView"]))

# add paths
process = CommonFSQFramework.Core.customizePAT.addPath(process,process.chargedgenjets)
process = CommonFSQFramework.Core.customizePAT.addTreeProducer(process, process.GenLevelTree)
