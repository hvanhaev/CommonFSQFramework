import FWCore.ParameterSet.Config as cms

process = cms.Process("Treemaker")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(1000))

process.MessageLogger.cerr.FwkReport.reportEvery = 10000
process.options = cms.untracked.PSet(wantSummary = cms.untracked.bool(True))

# Source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('file:../GenLevel/00E5660A-47C7-E411-9E5B-0025905A48F0.root')
)

# Geometry and Detector Conditions
process.load("Configuration.Geometry.GeometryRecoDB_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_mc')
process.load("Configuration.StandardSequences.MagneticField_cff")

##### from Diego
# load low-pt charged GenJet configuration here
# get charged genParticles
process.load('QCDAnalysis.UEAnalysis.UEAnalysisParticles_cfi')

from RecoJets.JetProducers.sc5GenJets_cfi import sisCone5GenJets
from RecoJets.JetProducers.ak5GenJets_cfi import ak5GenJets
from RecoJets.JetProducers.FastjetParameters_cfi import *

process.load("RecoJets.Configuration.GenJetParticles_cff")

process.chargeParticles.cut = cms.string('charge != 0 & pt > 0.5 & status = 1')

process.sisCone5ChgGenJets = sisCone5GenJets.clone(rParam = 0.5, jetPtMin=1.0, src = cms.InputTag("chargeParticles"), inputEtMin     = cms.double(0.5) )
process.sisCone7ChgGenJets = sisCone5GenJets.clone(rParam = 0.7, jetPtMin=1.0, src = cms.InputTag("chargeParticles"), inputEtMin     = cms.double(0.5) )

process.ak5ChgGenJets = ak5GenJets.clone(rParam = 0.5, jetPtMin=1.0, src = cms.InputTag("chargeParticles"), inputEtMin     = cms.double(0.5)  )
process.ak4ChgGenJets = ak5GenJets.clone(rParam = 0.4, jetPtMin=1.0, src = cms.InputTag("chargeParticles"), inputEtMin     = cms.double(0.5)  )
process.ak7ChgGenJets = ak5GenJets.clone(rParam = 0.7, jetPtMin=1.0, src = cms.InputTag("chargeParticles"), inputEtMin     = cms.double(0.5)  )
process.ak10ChgGenJets = ak5GenJets.clone(rParam = 1., jetPtMin=1.0, src = cms.InputTag("chargeParticles"), inputEtMin     = cms.double(0.5)  )

process.chargedgenjets = cms.Path(process.UEAnalysisParticles*process.sisCone5ChgGenJets*process.sisCone7ChgGenJets*process.ak4ChgGenJets
					*process.ak5ChgGenJets*process.ak7ChgGenJets*process.ak10ChgGenJets)

##### stop from Diego



# Here starts the CFF specific part
import CommonFSQFramework.Core.customizePAT
process = CommonFSQFramework.Core.customizePAT.customize(process)

# GT customization
process = CommonFSQFramework.Core.customizePAT.customizeGT(process)

# define treeproducer
process.GenLevelTree = cms.EDAnalyzer("CFFTreeProducer")
import CommonFSQFramework.Core.GenLevelViewsConfigs
process.GenLevelTree._Parameterizable__setParameters(CommonFSQFramework.Core.GenLevelViewsConfigs.get(
	["GenPartView","ak4ChgGenJetView","ak5ChgGenJetView","ak7ChgGenJetView","ak10ChgGenJetView","sisCone5ChgGenJetView","sisCone7ChgGenJetView"]))

# add paths
process = CommonFSQFramework.Core.customizePAT.addPath(process,process.chargedgenjets)
process = CommonFSQFramework.Core.customizePAT.addTreeProducer(process, process.GenLevelTree)
