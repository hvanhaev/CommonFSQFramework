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

process = cms.Process("TreeMaker")
process.load("CondCore.DBCommon.CondDBSetup_cfi")
process.load("FWCore.MessageService.MessageLogger_cfi")

process.source = cms.Source("HcalTBSource",
    streams = cms.untracked.vstring(
		'HCAL_Trigger', 
        'HCAL_DCC690',
        'HCAL_DCC691',
        'HCAL_DCC692'
    ),
    fileNames = cms.untracked.vstring(
		"file:/afs/cern.ch/user/m/mpieters/YOURWORKINGAREA/CMSSW_10_3_0/src/USC_325838.root" 
    )   
)

    
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1500)
    #input = cms.untracked.int32(-1)
)

#Merijn try to add some output since run over 1M evts.
process.load('FWCore.MessageService.MessageLogger_cfi')
#process.MessageLogger.cerr.FwkReport.reportEvery = 1000
#process.options = cms.untracked.PSet(wantSummary = cms.untracked.bool(True))

process.castorDigis = cms.EDProducer("CastorRawToDigi",
    # Optional filter to remove any digi with "data valid" off, "error" on, 
    # or capids not rotating
    FilterDataQuality = cms.bool(True),
    # Number of the first CASTOR FED.  If this is not specified, the
    # default from FEDNumbering is used.
    CastorFirstFED = cms.int32(690),
    ZDCFirstFED = cms.int32(693),                         
    # FED numbers to unpack.  If this is not specified, all FEDs from
    # FEDNumbering will be unpacked.
    FEDs = cms.untracked.vint32( 690, 691, 692, 693, 722),
    # Do not complain about missing FEDs
    ExceptionEmptyData = cms.untracked.bool(False),
    # Do not complain about missing FEDs
    ComplainEmptyData = cms.untracked.bool(False),
    # At most ten samples can be put into a digi, if there are more
    # than ten, firstSample and lastSample select which samples
    # will be copied to the digi
    firstSample = cms.int32(0),
    lastSample = cms.int32(9),
    # castor technical trigger processor
    UnpackTTP = cms.bool(True),
    # report errors
    silent = cms.untracked.bool(False),
    #
    InputLabel = cms.InputTag("source"),
    CastorCtdc = cms.bool(False),
    UseNominalOrbitMessageTime = cms.bool(True),
    ExpectedOrbitMessageTime = cms.int32(-1),
    UnpackZDC = cms.bool(False)
)
process.raw2digi = cms.Path(process.castorDigis)

#process.out = cms.OutputModule("PoolOutputModule",
#    fileName = cms.untracked.string('USC_XXXXXX_unpacked.root')
#)


#process.dumpRaw = cms.EDAnalyzer( "DumpFEDRawDataProduct",
#    feds = cms.untracked.vint32( 690,691,692,693 ),
#    dumpPayload = cms.untracked.bool( True )
#)

#process.m = cms.EDAnalyzer("HcalDigiDump")

#process.dump = cms.EDAnalyzer(
#	'HcalTBObjectDump',
#	hcalTBTriggerDataTag = cms.InputTag('tbunpack'),
#	hcalTBRunDataTag = cms.InputTag('tbunpack'),
#	hcalTBEventPositionTag = cms.InputTag('tbunpack'),
#	hcalTBTimingTag = cms.InputTag('tbunpack')
#)

#process.dumpECA = cms.EDAnalyzer("EventContentAnalyzer")

process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
from Configuration.AlCa.GlobalTag import GlobalTag
from CondCore.CondDB.CondDB_cfi import *
process.GlobalTag = GlobalTag(process.GlobalTag, '101X_dataRun2_Prompt_v11', '')


# Here starts the CFF specific part
import CommonFSQFramework.Core.customizePAT
process = CommonFSQFramework.Core.customizePAT.customize(process)

# define treeproducer
process.digisTree = cms.EDAnalyzer("CFFTreeProducer")

import CommonFSQFramework.Core.CastorDigiViewConfigs
process.digisTree._Parameterizable__setParameters(CommonFSQFramework.Core.CastorDigiViewConfigs.get(["CastorDigiView"]))

process = CommonFSQFramework.Core.customizePAT.addPath(process, process.raw2digi)
process = CommonFSQFramework.Core.customizePAT.addTreeProducer(process, process.digisTree)


#process.ep = cms.EndPath(process.out)

