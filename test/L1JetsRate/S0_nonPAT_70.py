import FWCore.ParameterSet.Config as cms

process = cms.Process("FluffyBunniesSoFluffyFluffyFluffy")
process.load("FWCore.MessageLogger.MessageLogger_cfi")

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('root://xrootd.ba.infn.it//store/mc/Spring14dr/QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8/AODSIM/Flat20to50_POSTLS170_V5-v1/00000/9480AA58-E3DD-E311-8FE3-002590D0AFEC.root')
)


import MNTriggerStudies.MNTriggerAna.customizePAT
process = MNTriggerStudies.MNTriggerAna.customizePAT.customize(process)

process.L1JetsRateAna = cms.EDAnalyzer("L1JetsRateAna",
    L1JetsView  = cms.PSet(
        src =  cms.VInputTag(cms.InputTag("l1extraParticles","Central"),
                cms.InputTag("l1extraParticles","Forward"),
                cms.InputTag("l1extraParticles","Tau")
        ),
    ),
)
process = MNTriggerStudies.MNTriggerAna.customizePAT.addTreeProducer(process, process.L1JetsRateAna)




