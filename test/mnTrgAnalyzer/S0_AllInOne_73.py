#! /usr/bin/env python
import imp
import FWCore.ParameterSet.Config as cms


# hlt config files preparation:
# hltGetConfiguration /dev/CMSSW_7_3_0/HLT/V105 --full --offline --mc --unprescale --process TEST --globaltag auto:run2_mc_GRun --l1-emulator 'gct,gt' > hlt_gctgt.py
#  hltGetConfiguration /dev/CMSSW_7_3_0/GRun --full --offline --mc --unprescale --process TEST --globaltag auto:run2_mc_GRun --l1-emulator 'stage1,gt' --l1Xml L1Menu_Collisions2015_25ns_v2_L1T_Scales_20141121_Imp0_0x1030.xml > hlt.py

# we can redo only one type of trigger a time
# note: auto GT setting at the end
l1SeedThr = 5
#todo = "legacy"
todo = "stage1"


if todo == "stage1":
    filename = "hlt.py"
elif todo == "legacy":
    filename = "hlt_gctgt.py"
handle = open(filename, 'r')
cfo = imp.load_source("pycfg", filename, handle)
process = cfo.process
handle.close()

#print cmsProcess.dumpPython()
import FWCore.ParameterSet.SequenceTypes as st
for a in dir(process):
    attr = getattr(process, a)
    if type(attr) == st.Path:
        delattr(process, a)

process.load("RecoJets.Configuration.GenJetParticles_cff")
process.load("RecoJets.Configuration.RecoGenJets_cff")
process.jets = cms.Path( process.HLTBeginSequence + process.HLTAK4CaloJetsSequence + process.HLTAK4PFJetsSequence 
                       + process.genParticlesForJets + process.ak4GenJets + process.HLTEndSequence )





process.source.fileNames = cms.untracked.vstring(
#        '/store/mc/Spring14dr/QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8/GEN-SIM-RAW/Flat0to10_POSTLS170_V5-v1/00000/0002A86F-3408-E411-B90A-E0CB4E19F961.root'
        '/store/mc/Phys14DR/Neutrino_Pt-2to20_gun/GEN-SIM-RAW/Flat20to50BX50_tsg_PHYS14_ST_V1-v1/00000/04BC0DAC-6F8A-E411-BA02-0025905A6084.root'
)


del process.hltOutputA.SelectEvents
#'''
del process.hltOutputA
del process.dqmOutput

del process.AOutput
del process.DQMOutput
#'''
#del process.hltOutputA.outputCommands

import MNTriggerStudies.MNTriggerAna.customizePAT
process = MNTriggerStudies.MNTriggerAna.customizePAT.customize(process)

process = MNTriggerStudies.MNTriggerAna.customizePAT.addPath(process, process.jets)

#process.MNTriggerAnaHLTJECOnFly = cms.EDAnalyzer("MNTriggerAnaHLTJECOnFly")
#process = MNTriggerStudies.MNTriggerAna.customizePAT.addTreeProducer(process, process.MNTriggerAnaHLTJECOnFly)

import MNTriggerStudies.MNTriggerAna.MNTrgAnalyzer
triggerProcess = "TEST"
#process = MNTriggerStudies.MNTriggerAna.MNTrgAnalyzer.addTreeProducer(process, triggerResults=triggerProcess, disable = ["hlt", "l1"])
process = MNTriggerStudies.MNTriggerAna.MNTrgAnalyzer.addTreeProducer(process, triggerResults=triggerProcess)
del process.MNTriggerAnaNew.JetViewPF
del process.MNTriggerAnaNew.JetViewCalo
del process.MNTriggerAnaNew.JetViewPFAK4CHS
del process.MNTriggerAnaNew.JetViewPFAK5CHS

if todo == "legacy":
    print "Warning, stage1 disabled"
    del process.MNTriggerAnaNew.L1JetsViewStage1
    process.MNTriggerAnaNew.L1JetsViewRedone = process.MNTriggerAnaNew.L1JetsView.clone()
    process.MNTriggerAnaNew.L1JetsViewRedone.branchPrefix = cms.untracked.string('oldRedone')

    process.MNTriggerAnaNew.L1JetsViewRedone.src = cms.VInputTag(cms.InputTag("hltL1extraParticles","Central", "TEST"), 
                                                           cms.InputTag("hltL1extraParticles","Forward", "TEST"), 
                                                       cms.InputTag("hltL1extraParticles","Tau", "TEST"))

    process.load('L1TriggerConfig.GctConfigProducers.l1GctConfig_cfi')
    process.L1GctConfigProducers.JetFinderCentralJetSeed = cms.double(l1SeedThr)
    process.L1GctConfigProducers.JetFinderForwardJetSeed = cms.double(l1SeedThr)
elif todo == "stage1":
    process.caloStage1Params.jetSeedThreshold = cms.double(l1SeedThr) 


process = MNTriggerStudies.MNTriggerAna.customizePAT.removeEdmOutput(process)
#process.GlobalTag.globaltag = "PHYS14_25_V2::All"

'''
primary = "file:/nfs/dust/cms/user/fruboest/2015.01.ProduceAndTestJECFromFeng/CMSSW_7_3_0/src/outputA.root"
process.source = cms.Source("PoolSource",
#    secondaryFileNames = cms.untracked.vstring([sec1, sec2]),
    fileNames = cms.untracked.vstring([primary]),
    bypassVersionCheck = cms.untracked.bool(True)
)
'''

process.source = cms.Source( "PoolSource",
    secondaryFileNames = cms.untracked.vstring(
        'file:/nfs/dust/cms/user/fruboest/2014.08.TriggerStudies/CMSSW_7_1_5/src/MNTriggerStudies/MNTriggerAna/test/mnTrgAnalyzer/infiles/BCDF1B07-B212-E411-A99A-00248C55CC9D_QCD_Pt-50to80_Tune4C_13TeV_pythia8_flat0to10_RAW.root',
    ),
    #secondaryFileNames = cms.untracked.vstring(
    fileNames = cms.untracked.vstring(
        'file:/nfs/dust/cms/user/fruboest/2014.08.TriggerStudies/CMSSW_7_1_5/src/MNTriggerStudies/MNTriggerAna/test/mnTrgAnalyzer/infiles/363D5394-CF12-E411-A75C-002590596484.root_AODSIM'
    )
)

GT= "MCRUN2_72_V4A" # 62 produced 50 ns
#GT= "MCRUN2_72_V3A::All" # 62 produced 25 ns

import os
if "TMFSampleName" in os.environ:
    sample = os.environ["TMFSampleName"]
    if "QCD" in sample:
        GT = "PHYS14_25_V1"

    print "XXXX",  sample, GT

#GT = "PHYS14_25_V1"
process.GlobalTag.globaltag = cms.string(GT)

'''
process.load("CondCore.DBCommon.CondDBCommon_cfi")

# JetCorrectorParametersCollection_EcalMultifitHCALMethod2_AK4PFHLT
from CondCore.DBCommon.CondDBSetup_cfi import *
process.jec = cms.ESSource("PoolDBESSource",
      DBParameters = cms.PSet(
        messageLevel = cms.untracked.int32(0)
        ),
      timetype = cms.string('runnumber'),
      toGet = cms.VPSet(
      cms.PSet(
            record = cms.string('JetCorrectionsRecord'),
            tag    = cms.string('JetCorrectorParametersCollection_EcalMultifitHCALMethod2_AK4PFHLT'),
            label  = cms.untracked.string('AK4PFTMF')
            ),
      ),
      connect = cms.string('sqlite:EcalMultifitHCALMethod2.db')
      #connect = cms.string('frontier://FrontierProd/CMS_COND_31X_GLOBALTAG')
)
## add an es_prefer statement to resolve a possible conflict from simultaneous connection to a global tag
process.es_prefer_jec = cms.ESPrefer('PoolDBESSource','jec')
'''



