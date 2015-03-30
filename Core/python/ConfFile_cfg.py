import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(10) )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(
#        'file:myfile.root'
        'file:/scratch/scratch0/data/store/mc/Fall13dr/QCD_Pt-50to80_Tune4C_13TeV_pythia8/AODSIM/castor_tsg_PU1bx50_POSTLS162_V1-v1/00000/00108F5C-D873-E311-BD7F-002618943914.root'
    )
)

process.demo = cms.EDAnalyzer('MNTriggerAna'
)


process.p = cms.Path(process.demo)
