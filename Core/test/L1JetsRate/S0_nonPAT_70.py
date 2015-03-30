import FWCore.ParameterSet.Config as cms

process = cms.Process("FluffyBunniesSoFluffyFluffyFluffy")
process.load('Configuration.StandardSequences.Services_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration/StandardSequences/FrontierConditions_GlobalTag_cff')
process.load('Configuration.Geometry.GeometryIdeal_cff')


#process.source = cms.Source("PoolSource",
#    fileNames = cms.untracked.vstring('root://xrootd.ba.infn.it//store/mc/Spring14dr/QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8/AODSIM/Flat20to50_POSTLS170_V5-v1/00000/9480AA58-E3DD-E311-8FE3-002590D0AFEC.root')
#)


process.source = cms.Source( "PoolSource",
    #fileNames = cms.untracked.vstring(
    secondaryFileNames = cms.untracked.vstring(
        'file:/nfs/dust/cms/user/fruboest/2014.08.TriggerStudies/CMSSW_7_1_5/src/MNTriggerStudies/MNTriggerAna/test/mnTrgAnalyzer/infiles/BCDF1B07-B212-E411-A99A-00248C55CC9D_QCD_Pt-50to80_Tune4C_13TeV_pythia8_flat0to10_RAW.root',
    ),
    #secondaryFileNames = cms.untracked.vstring(
    fileNames = cms.untracked.vstring(
        'file:/nfs/dust/cms/user/fruboest/2014.08.TriggerStudies/CMSSW_7_1_5/src/MNTriggerStudies/MNTriggerAna/test/mnTrgAnalyzer/infiles/363D5394-CF12-E411-A75C-002590596484.root_AODSIM'
    ),
    inputCommands = cms.untracked.vstring(
        'keep *'
    )
)


process.GlobalTag.globaltag = 'PRE_LS171V9A::All'

process.load('L1Trigger.L1TCalorimeter.L1TCaloStage1_PPFromRaw_cff')
process.p1 = cms.Path(
    process.L1TCaloStage1_PPFromRaw
)
process.schedule = cms.Schedule([process.p1])
#process.schedule = cms.Schedule(*[ process.pUtil, process.pL1JetsRateAna, process.pTreeProducers ])
#from SLHCUpgradeSimulations.Configuration.postLS1Customs import *
#process = customise_HLT(process)


import MNTriggerStudies.MNTriggerAna.customizePAT
process = MNTriggerStudies.MNTriggerAna.customizePAT.customize(process)

process.L1JetsRateAna = cms.EDAnalyzer("L1JetsRateAna",
    L1JetsView  = cms.PSet(
        branchPrefix = cms.untracked.string("old"),
        src =  cms.VInputTag(cms.InputTag("l1extraParticles","Central"),
                cms.InputTag("l1extraParticles","Forward"),
                cms.InputTag("l1extraParticles","Tau")
        ),
    ),
    L1JetsViewStage1  = cms.PSet(
        branchPrefix = cms.untracked.string("stage1"),
        src =  cms.VInputTag(cms.InputTag("l1ExtraReEmul","Central"),
                cms.InputTag("l1ExtraReEmul","Forward")
        ),
    ),


)
process = MNTriggerStudies.MNTriggerAna.customizePAT.addTreeProducer(process, process.L1JetsRateAna)







