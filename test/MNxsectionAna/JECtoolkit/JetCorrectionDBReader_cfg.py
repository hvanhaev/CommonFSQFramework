import FWCore.ParameterSet.Config as cms

process = cms.Process("myprocess")

process.load('Configuration.StandardSequences.Services_cff')
#process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
#gt='START42_V16'
#gt='START41_V0'
'''
process.GlobalTag.globaltag = gt+'::All'
'''
gt="START42_V16TFPartV2"

process.maxEvents = cms.untracked.PSet(
        input = cms.untracked.int32(1)
        )

process.source = cms.Source("EmptySource")

process.readAK5PF = cms.EDAnalyzer('JetCorrectorDBReader', 
        payloadName    = cms.untracked.string('AK5PF'),
   	    globalTag      = cms.untracked.string(gt),  
        printScreen    = cms.untracked.bool(False),
        createTextFile = cms.untracked.bool(True)
)


process.readAK5Calo = process.readAK5PF.clone(payloadName = 'AK5Calo')

process.p = cms.Path(process.readAK5PF * process.readAK5Calo)

#ver = "V16TFFull"
ver = "V16TFPart"
process.load("CondCore.DBCommon.CondDBCommon_cfi")
from CondCore.DBCommon.CondDBSetup_cfi import *
process.jec = cms.ESSource("PoolDBESSource",
      DBParameters = cms.PSet(
        messageLevel = cms.untracked.int32(0)
        ),
      timetype = cms.string('runnumber'),
      toGet = cms.VPSet(
      cms.PSet(
            record = cms.string('JetCorrectionsRecord'),
            tag    = cms.string('JetCorrectorParametersCollection_START42_'+ver+'_AK5PF'),
            label  = cms.untracked.string('AK5PF')
            ),
      cms.PSet(
            record = cms.string('JetCorrectionsRecord'),
            tag    = cms.string('JetCorrectorParametersCollection_START42_'+ver+'_AK5Calo'),
            label  = cms.untracked.string('AK5Calo')
            ),
      ),
      connect = cms.string('sqlite:START42_'+ver+'.db')
)
## add an es_prefer statement to resolve a possible conflict from simultaneous connection to a global tag
process.es_prefer_jec = cms.ESPrefer('PoolDBESSource','jec')

