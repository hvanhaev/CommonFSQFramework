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

process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))

process.MessageLogger.cerr.FwkReport.reportEvery = 1000
process.options = cms.untracked.PSet(wantSummary = cms.untracked.bool(True))

# Source
process.source = cms.Source("PoolSource",
    #fileNames = cms.untracked.vstring('root://xrootd.ba.infn.it//store/himc/pPb816Summer16DR/ReggeGribovPartonMC_EposLHC_pPb_4080_4080_DataBS/AODSIM/MB_80X_mcRun2_pA_v4-v2/120000/003FC5B1-2009-E711-8AD2-0025904C6414.root')
    fileNames = cms.untracked.vstring('root://xrootd.ba.infn.it//store/hidata/PARun2016C/PAForward/AOD/PromptReco-v1/000/285/505/00000/027E73D6-84AF-E611-817F-FA163EEF6D32.root')
)

# Geometry and Detector Conditions
process.load("Configuration.Geometry.GeometryRecoDB_cff")
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
if isData: process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_data', '')
if not isData: process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_mc', '')
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load("Configuration.StandardSequences.Reconstruction_cff")

##### from Diego
# load low-pt charged GenJet configuration here
# get charged genParticles
process.load('QCDAnalysis.UEAnalysis.UEAnalysisParticles_cfi')
from RecoJets.JetProducers.ak5GenJets_cfi import ak5GenJets
from RecoJets.JetProducers.FastjetParameters_cfi import *
process.load("RecoJets.Configuration.GenJetParticles_cff")
process.chargeParticles.cut = cms.string('charge != 0 & pt > 0.5 & status = 1')
process.ak5ChgGenJets = ak5GenJets.clone(rParam = 0.5, jetPtMin=1.0, src = cms.InputTag("chargeParticles"), inputEtMin = cms.double(0.5)  )
process.chargedgenjets = cms.Path(process.UEAnalysisParticles*process.ak5ChgGenJets)

# set up tracks for trackjets
from CommonTools.RecoAlgos.TrackWithVertexRefSelector_cfi import *
from RecoJets.JetProducers.TracksForJets_cff import *
process.trackWithVertexRefSelector=trackWithVertexRefSelector.clone()
process.trackRefsForJets=trackRefsForJets.clone()
process.trackRefsForJets.cut= cms.string('charge != 0 & pt > 0.5 & status = 1 & quality = highPurity & ptErrorCut = 0.05 ')
from RecoJets.JetProducers.ak5TrackJets_cfi import ak5TrackJets
process.ak5TrackJets = ak5TrackJets.clone( rParam = 0.5, jetPtMin=1.0, UseOnlyVertexTracks=True, UseOnlyOnePV=True, src = cms.InputTag("trackRefsForJets"), inputEtMin = cms.double(0.5))
process.chargedjets = cms.Path(process.ak5TrackJets)
##### stop from Diego

##### CASTOR treatment
# construct the module which executes the RechitCorrector for data
process.rechitcorrector = cms.EDProducer("RecHitCorrector",
   rechitLabel = cms.InputTag("castorreco","","RECO"), # choose the original RecHit collection
   revertFactor = cms.double(1), 
   doInterCalib = cms.bool(True)
 )

# import Castor tower and jet reconstruction
process.load('RecoLocalCalo.Castor.Castor_cff')

# tell to the CastorTower reconstruction that he should use the new corrected rechits for releases>= 4.2.X
if isData: process.CastorTowerReco.inputprocess = "rechitcorrector"

# specify the correct database tag which contains the updated tags
process.load("CondCore.DBCommon.CondDBSetup_cfi")
process.CastorDbProducer = cms.ESProducer("CastorDbProducer")
process.es_ascii = cms.ESSource("CastorTextCalibrations",
    input = cms.VPSet(
                cms.PSet(
                    object = cms.string('Gains'),
                    file = cms.FileInPath('data/CastorConditions/InterCalibValues_2016_v2.txt')
                ),
		cms.PSet(
                    object = cms.string('ChannelQuality'),
                    file = cms.FileInPath('data/CastorConditions/BadChannels_2016.txt')
                ),
    )
)
process.es_prefer_castor = cms.ESPrefer('CastorTextCalibrations','es_ascii') 
process.CastorReRecoDATA = cms.Path(process.rechitcorrector*process.CastorFullReco) # calibrate rechits etc...
process.CastorReRecoMC = cms.Path(process.CastorFullReco) # just redo towers and jets but with removing bad channels
#####


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
import CommonFSQFramework.Core.CastorViewsConfigs

process.UETree= cms.EDAnalyzer("CFFTreeProducer")

if not isData: process.UETree._Parameterizable__setParameters(CommonFSQFramework.Core.GenLevelViewsConfigs.get(["ak5ChgGenJetView"]))
process.UETree._Parameterizable__setParameters(CommonFSQFramework.Core.JetViewsConfigs.get(["JetViewak5TrackJets"]))
#process.UETree._Parameterizable__setParameters(CommonFSQFramework.Core.RecoTrackViewsConfigs.get(["RecoTrackView"]))
process.UETree._Parameterizable__setParameters(CommonFSQFramework.Core.VerticesViewsConfigs.get(["VerticesView"]))
if not isData: process.UETree._Parameterizable__setParameters(CommonFSQFramework.Core.CastorViewsConfigs.get(["CastorRecHitViewFull","CastorTowerView","ak5CastorJetView"]))
if isData: process.UETree._Parameterizable__setParameters(CommonFSQFramework.Core.CastorViewsConfigs.get(["CastorRecHitViewFullCorrected","CastorTowerView","ak5CastorJetView"]))
if isData: process.UETree._Parameterizable__setParameters(CommonFSQFramework.Core.TriggerResultsViewsConfigs.get(["PARun2016CTriggerResultsView"]))

if not isData: process = CommonFSQFramework.Core.customizePAT.addPath(process,process.CastorReRecoMC)
if isData: process = CommonFSQFramework.Core.customizePAT.addPath(process,process.CastorReRecoDATA)
if not isData: process = CommonFSQFramework.Core.customizePAT.addPath(process,process.chargedgenjets)
process = CommonFSQFramework.Core.customizePAT.addPath(process,process.chargedjets)
process = CommonFSQFramework.Core.customizePAT.addTreeProducer(process, process.UETree)
