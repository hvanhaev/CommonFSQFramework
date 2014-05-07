import FWCore.ParameterSet.Config as cms

process = cms.Process("treeProdDevel")
process.load("FWCore.MessageLogger.MessageLogger_cfi")

indir = "/scratch/scratch0/tfruboes/DJNewFW/PATFiles/store/user/fruboes/QCD_Pt-80to120_Tune4C_13TeV_pythia8/DiJet_20140411_QCD_Pt-80to120_Tune4C_13TeV_pythia8/2b7f6fbfa4bcda451fe51ee9c9d04565/"

f= indir+ "mnTrgAna_PAT_11_1_Hqy.root"
f = "mnTrgAna_PAT.root"

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('file:'+f)
)

process.options = cms.untracked.PSet( wantSummary = cms.untracked.bool(False) )

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(100) )


process.TFileService = cms.Service("TFileService", fileName = cms.string("trees.root") )



process.exampleTree = cms.EDAnalyzer("ExampleTreeProducer")
process.infoHisto = cms.EDAnalyzer("SaveCountHistoInTreeFile")


process.p = cms.Path(process.treeProd1*process.infoHisto)

