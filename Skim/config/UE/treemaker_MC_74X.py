import FWCore.ParameterSet.Config as cms

process = cms.Process("Treemaker")

process.load("FWCore.MessageService.MessageLogger_cfi")

#process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(1000))

process.MessageLogger.cerr.FwkReport.reportEvery = 100
process.options = cms.untracked.PSet(wantSummary = cms.untracked.bool(True))

# Source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('/store/mc/RunIISpring15DR74/MinBias_TuneCUETP8S1-HERAPDF_13TeV-pythia8/AODSIM/NoPU_MCRUN2_74_V8-v3/00000/043F0F18-3D08-E511-8E01-00259073E456.root')
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

process.chargedgenjets = cms.Path(process.UEAnalysisParticles*process.sisCone5ChgGenJets*
					process.sisCone7ChgGenJets*process.ak4ChgGenJets
					*process.ak5ChgGenJets*process.ak7ChgGenJets*process.ak10ChgGenJets)

from CommonTools.RecoAlgos.TrackWithVertexRefSelector_cfi import *
from RecoJets.JetProducers.TracksForJets_cff import *

process.trackWithVertexRefSelector=trackWithVertexRefSelector.clone()
process.trackRefsForJets=trackRefsForJets.clone()

process.trackRefsForJets.cut= cms.string('charge != 0 & pt > 0.5 & status = 1 & quality = highPurity & ptErrorCut = 0.05 ')


from RecoJets.JetProducers.sc5TrackJets_cfi import sisCone5TrackJets
from RecoJets.JetProducers.ak5TrackJets_cfi import ak5TrackJets


process.sisCone5TrackJets = sisCone5TrackJets.clone( rParam = 0.5, jetPtMin=1.0, UseOnlyVertexTracks=True, UseOnlyOnePV=True, src = cms.InputTag("trackRefsForJets"), inputEtMin     = cms.double(0.5))
process.sisCone7TrackJets = sisCone5TrackJets.clone(rParam = 0.7, jetPtMin=1.0, UseOnlyVertexTracks=True, UseOnlyOnePV=True, src = cms.InputTag("trackRefsForJets"), inputEtMin     = cms.double(0.5))


process.ak5TrackJets = ak5TrackJets.clone( rParam = 0.5, jetPtMin=1.0, UseOnlyVertexTracks=True, UseOnlyOnePV=True, src = cms.InputTag("trackRefsForJets"), inputEtMin     = cms.double(0.5))
process.ak4TrackJets = ak5TrackJets.clone( rParam = 0.4, jetPtMin=1.0, UseOnlyVertexTracks=True, UseOnlyOnePV=True, src = cms.InputTag("trackRefsForJets"), inputEtMin     = cms.double(0.5))
process.ak7TrackJets = ak5TrackJets.clone( rParam = 0.7, jetPtMin=1.0, UseOnlyVertexTracks=True, UseOnlyOnePV=True, src = cms.InputTag("trackRefsForJets"), inputEtMin     = cms.double(0.5))
process.ak10TrackJets = ak5TrackJets.clone( rParam = 1.0, jetPtMin=1.0, UseOnlyVertexTracks=True, UseOnlyOnePV=True, src = cms.InputTag("trackRefsForJets"), inputEtMin     = cms.double(0.5))


process.chargedjets = cms.Path(process.sisCone5TrackJets*
                                        process.sisCone7TrackJets*process.ak4TrackJets
                                        *process.ak5TrackJets*process.ak7TrackJets*process.ak10TrackJets)

##### stop from Diego




# Here starts the CFF specific part
import CommonFSQFramework.Core.customizePAT
process = CommonFSQFramework.Core.customizePAT.customize(process)

# GT customization
process = CommonFSQFramework.Core.customizePAT.customizeGT(process)

# define treeproducer
import CommonFSQFramework.Core.GenLevelViewsConfigs
import CommonFSQFramework.Core.JetViewsConfigs
import CommonFSQFramework.Core.RecoTrackViewsConfigs
import CommonFSQFramework.Core.VerticesViewsConfigs
import CommonFSQFramework.Core.TriggerResultsViewsConfigs

process.UETree= cms.EDAnalyzer("CFFTreeProducer")

process.UETree._Parameterizable__setParameters(CommonFSQFramework.Core.GenLevelViewsConfigs.get(
        ["GenPartView","ak4ChgGenJetView","ak5ChgGenJetView","ak7ChgGenJetView","ak10ChgGenJetView","sisCone5ChgGenJetView","sisCone7ChgGenJetView"]))

process.UETree._Parameterizable__setParameters(
        CommonFSQFramework.Core.JetViewsConfigs.get(["JetViewSisCone5TrackJets"]))

process.UETree._Parameterizable__setParameters(
	CommonFSQFramework.Core.RecoTrackViewsConfigs.get(["RecoTrackView"]) 
)
process.UETree._Parameterizable__setParameters(
        CommonFSQFramework.Core.VerticesViewsConfigs.get(["VerticesView"])
)

#process.UETree._Parameterizable__setParameters(
#        CommonFSQFramework.Core.TriggerResultsViewsConfigs.get(["All"])
#)

process = CommonFSQFramework.Core.customizePAT.addPath(process,process.chargedgenjets)
process = CommonFSQFramework.Core.customizePAT.addPath(process,process.chargedjets)
process = CommonFSQFramework.Core.customizePAT.addTreeProducer(process, process.UETree)
