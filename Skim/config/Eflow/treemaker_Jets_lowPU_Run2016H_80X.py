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

process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(500))

process.MessageLogger.cerr.FwkReport.reportEvery = 100
process.options = cms.untracked.PSet(wantSummary = cms.untracked.bool(False))

# Source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('root://xrootd.unl.edu//store/data/Run2016B/HINPFJets/MINIAOD/PromptReco-v2/000/273/523/00000/7C3F8816-531F-E611-A37C-02163E014133.root')
)

# Geometry and Detector Conditions
process.load("Configuration.Geometry.GeometryRecoDB_cff")
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
if isData: process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_data', '')
if not isData: process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_mc', '')
process.load("Configuration.StandardSequences.MagneticField_cff")
#process.load("Configuration.StandardSequences.Reconstruction_cff")

# produce HF PFClusters
#process.PFClustersHF = cms.Path(process.particleFlowRecHitHF*process.particleFlowClusterHF)

# Here starts the CFF specific part
import CommonFSQFramework.Core.customizePAT
process = CommonFSQFramework.Core.customizePAT.customize(process)

# GT customization
process = CommonFSQFramework.Core.customizePAT.customizeGT(process)

# Add jet collection (able to go to lower pT as 10)
# with these lines of code one can alter the jetcollection, e.g. lower the pT treshold below the standard of 10 GeV and choose which corrections one applies
#from RecoJets.JetProducers.ak4PFJets_cfi import ak4PFJets
#ak4PFJetsCHS = ak4PFJets.clone(
#    src = cms.InputTag("packedPFCandidates"),
#    doAreaFastjet = True,
#    jetPtMin = 1.
#)
#setattr(process,"ak4PFJetsCHS",ak4PFJetsCHS)


#from PhysicsTools.PatAlgos.tools.jetTools import addJetCollection

#jecLevels = ['L1FastJet', 'L2Relative', 'L3Absolute', 'L2L3Residual']
#addJetCollection(
#   process,
#   labelName = 'AK4PFCHS',
#   jetSource = cms.InputTag('ak4PFJetsCHS'),
#   pfCandidates = cms.InputTag("packedPFCandidates"),
#   pvSource = cms.InputTag('offlineSlimmedPrimaryVertices'),
#   svSource = cms.InputTag('slimmedSecondaryVertices'),
#   algo = 'AK',
#   rParam = 0.4,
#   getJetMCFlavour = False, # seems to be enough for hadronFlavour()
#   genJetCollection = cms.InputTag('slimmedGenJets'),
#   genParticles = cms.InputTag('prunedGenParticles'), # likely needed for hadronFlavour()....
#   jetCorrections = ('AK4PFchs', jecLevels, 'None'),
#   muSource = cms.InputTag("slimmedMuons"),
#   elSource = cms.InputTag("slimmedElectrons")
#)
## turn on/off GEN matching (different than hadronFlavour()?)
#getattr(process,'patJetsAK4PFCHS').addGenPartonMatch = cms.bool(False)
#getattr(process,'patJetsAK4PFCHS').addGenJetMatch = cms.bool(False)
#process.jetSequence = cms.Path(process.patJetsAK4PFCHS)



# JEC part
# here one can manually choose which jet corrections to apply
from PhysicsTools.PatAlgos.tools.jetTools import updateJetCollection
updateJetCollection(
   process,
   jetSource = cms.InputTag('slimmedJets'),
   labelName = 'UpdatedJEC',
   jetCorrections = ('AK4PFchs', cms.vstring(['L1FastJet', 'L2Relative', 'L3Absolute', 'L2L3Residual']), 'None')  # Update: Safe to always add 'L2L3Residual' as MC contains dummy L2L3Residual corrections (always set to 1)
)
process.jecSequence = cms.Path(process.patJetCorrFactorsUpdatedJEC * process.updatedPatJetsUpdatedJEC)

# define treeproducer
process.EflowTree = cms.EDAnalyzer("CFFTreeProducer")

import CommonFSQFramework.Core.VerticesViewsConfigs
import CommonFSQFramework.Core.TriggerResultsViewsConfigs
import CommonFSQFramework.Core.JetViewsConfigs

if not isData:
    import CommonFSQFramework.Core.GenLevelViewsConfigs
    

process.EflowTree._Parameterizable__setParameters(CommonFSQFramework.Core.VerticesViewsConfigs.get(["VerticesView"]))
if isData: process.EflowTree._Parameterizable__setParameters(CommonFSQFramework.Core.TriggerResultsViewsConfigs.get(["TriggersRun2016H"]))
process.EflowTree._Parameterizable__setParameters(CommonFSQFramework.Core.JetViewsConfigs.get(["JetViewPFAK4CHS","JetMET"]))

if not isData:
    process.EflowTree._Parameterizable__setParameters(CommonFSQFramework.Core.GenLevelViewsConfigs.get(["GenPartView","ak4GenJetView"]))


# add paths
process = CommonFSQFramework.Core.customizePAT.addPath(process, process.jecSequence) # this line is due to the updateJetCollection function, if one works with the addJetColleciton then jecSequence -> jetSequence
process = CommonFSQFramework.Core.customizePAT.addTreeProducer(process, process.EflowTree)

process.options = cms.untracked.PSet(
    SkipEvent = cms.untracked.vstring('ProductNotFound'),
    allowUnscheduled = cms.untracked.bool(True)
    )
    
