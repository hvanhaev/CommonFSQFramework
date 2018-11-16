import FWCore.ParameterSet.Config as cms
import CommonFSQFramework.Core.Util
import os

useCustomCond = False

# this is important to get the right trigger setup
from Configuration.StandardSequences.Eras import eras

process = cms.Process("Treemaker", eras.Run2_2018_pp_on_AA) # eras.Run2_2018)

process.load("FWCore.MessageService.MessageLogger_cfi")
process.load("Configuration.Geometry.GeometryRecoDB_cff")
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load("Configuration.StandardSequences.Reconstruction_cff")
process.load("Configuration.StandardSequences.RawToDigi_cff")

from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_data', '')

# Source
process.source = cms.Source("PoolSource",
# fileNames = cms.untracked.vstring('root://cmsxrootd.fnal.gov///store/data/Run2018C/ZeroBias/RAW/v1/000/320/249/00000/A4958224-1890-E811-BBA0-FA163E5BFF9D.root')
# fileNames = cms.untracked.vstring("file:/eos/cms/store/hidata/HIRun2018/ZeroBias/RAW/v1/000/325/868/00000/508F66C5-C194-EC44-A4D9-7315007BC0A1.root") # ZB with Random
  # fileNames = cms.untracked.vstring("file:/eos/cms/store/hidata/HIRun2018/MinimumBias/RAW/v1/000/325/868/00000/05CAB9AB-4FF9-5F4C-A474-C30493F69246.root",
  #                                   "file:/eos/cms/store/hidata/HIRun2018/MinimumBias/RAW/v1/000/325/868/00000/22180267-1667-3C43-8E68-93DE4F3E95B9.root",
  #                                   "file:/eos/cms/store/hidata/HIRun2018/MinimumBias/RAW/v1/000/325/868/00000/27F4332D-1199-BA45-B442-9E48CE07899D.root",
  #                                   "file:/eos/cms/store/hidata/HIRun2018/MinimumBias/RAW/v1/000/325/868/00000/288D0862-5B58-BD4A-AF5D-6444E53A31E0.root",
  #                                   "file:/eos/cms/store/hidata/HIRun2018/MinimumBias/RAW/v1/000/325/868/00000/2CD3B964-7A9E-FA47-B0BB-E693BAF30CFC.root",
  #                                   "file:/eos/cms/store/hidata/HIRun2018/MinimumBias/RAW/v1/000/325/868/00000/2EDE9A90-FAAE-7847-87C7-64B9E0B9951F.root",
  #                                   "file:/eos/cms/store/hidata/HIRun2018/MinimumBias/RAW/v1/000/325/868/00000/3AD4F4D5-706A-0F40-A4F9-A60E6ACE2E60.root",
  #                                   "file:/eos/cms/store/hidata/HIRun2018/MinimumBias/RAW/v1/000/325/868/00000/45E4F367-D511-1C45-B389-8B6F8A00C4C7.root",
  #                                   "file:/eos/cms/store/hidata/HIRun2018/MinimumBias/RAW/v1/000/325/868/00000/4A56E661-1DB7-8441-AB14-4BE40BD203E7.root",
  #                                   "file:/eos/cms/store/hidata/HIRun2018/MinimumBias/RAW/v1/000/325/868/00000/4D393CDD-0FFE-344D-8B2D-5F460F275B41.root",
  #                                   "file:/eos/cms/store/hidata/HIRun2018/MinimumBias/RAW/v1/000/325/868/00000/56CAED43-910F-A747-A2DC-D8B7D75171A3.root",
  #                                   "file:/eos/cms/store/hidata/HIRun2018/MinimumBias/RAW/v1/000/325/868/00000/703EC88F-9C94-D148-8434-D642E9127078.root",
  #                                   "file:/eos/cms/store/hidata/HIRun2018/MinimumBias/RAW/v1/000/325/868/00000/7AB36BFD-DBD0-254A-BAE5-F5BF9A2599F3.root",
  #                                   "file:/eos/cms/store/hidata/HIRun2018/MinimumBias/RAW/v1/000/325/868/00000/8A6BABAF-97BA-8942-BF26-09A9E5C22D81.root",
  #                                   )

# more:
# A55F1F9B-4E94-0F41-BD9B-60431A8B2E40.root
# A96DB0BC-45B1-814A-8C07-7577D8138094.root
# DCBEB5ED-3F1B-F048-AEB3-A46B58F997CD.root
# E3061A8E-4894-1643-BA81-116ABCB62A9A.root
# E4A075AA-26C8-DB48-B5C3-03AD1133A09E.root
# F3E1BB35-C968-7A42-B125-3289CFE0B4A2.root
# F5995E28-698D-2247-AFFD-FA232B351C29.root


#   fileNames = cms.untracked.vstring("file:/eos/cms/store/hidata/HIRun2018/MinimumBias/RAW/v1/000/325/943/00000/37D6F92E-B2C0-904C-93FC-23B54CCDA1A2.root",
 #                                    "file:/eos/cms/store/hidata/HIRun2018/MinimumBias/RAW/v1/000/325/943/00000/64F43C08-DFF7-884A-B3F4-4C1A0BCEE9C9.root"
  #                                   )

   fileNames = cms.untracked.vstring(
        # for RC meeting Nov 6th 2018
        #"file:/eos/cms/store/hidata/HIRun2018/ZeroBias/RAW/v1/000/325/947/00000/05F28463-1136-1046-AFAA-F12C4A0A629D.root",
        #"file:/eos/cms/store/hidata/HIRun2018/ZeroBias/RAW/v1/000/325/947/00000/5AB32F6D-6866-194B-B476-F58B0D9D3FE7.root",
        #"file:/eos/cms/store/hidata/HIRun2018/ZeroBias/RAW/v1/000/325/947/00000/8F10C6FB-A06F-F147-8FBC-A92BA916DB75.root"
        # first stable beams
        #"file:/eos/cms/store/hidata/HIRun2018A/HIMinimumBias0/RAW/v1/000/326/383/00000/A0CCB8F0-C349-0F49-9EF3-335D7889CE5B.root"
        # trigger fixed
        #'file:/eos/cms/store/hidata/HIRun2018A/ZeroBias/RAW/v1/000/326/495/00000/32BC1FB4-963A-6B4E-808F-0E1C5CC78364.root'
# epxress test
 'file:/eos/cms/store/hidata/HIRun2018A/ZeroBias/RAW/v1/000/326/613/00000/FB0F533A-195C-B34B-96B0-669334A8A734.root'

# first HLT castor muons!!! HLT_L1CastorMuons
# 'file:/eos/cms/store/hidata/HIRun2018A/MinimumBias/RAW/v1/000/326/683/00000/01E9DF98-E7D7-D44D-AFB3-1FEDA27574F1.root',
# 'file:/eos/cms/store/hidata/HIRun2018A/MinimumBias/RAW/v1/000/326/683/00000/2977F8B1-E29D-B14D-9994-A06E4BF94428.root',
# 'file:/eos/cms/store/hidata/HIRun2018A/MinimumBias/RAW/v1/000/326/683/00000/631534FE-CDC9-D84E-BEBD-35782C003398.root',
# 'file:/eos/cms/store/hidata/HIRun2018A/MinimumBias/RAW/v1/000/326/683/00000/746C8FF2-1F17-2041-8E1C-F54CAA10C016.root',
# 'file:/eos/cms/store/hidata/HIRun2018A/MinimumBias/RAW/v1/000/326/683/00000/A2FE1625-1090-AF46-B39B-5D0C9465C62B.root',
# 'file:/eos/cms/store/hidata/HIRun2018A/MinimumBias/RAW/v1/000/326/683/00000/BB6D6A75-014A-6C45-A416-C55499C5023A.root',
# 'file:/eos/cms/store/hidata/HIRun2018A/MinimumBias/RAW/v1/000/326/683/00000/F296A946-0712-DF4F-B683-3EDACE3C2E40.root',

# first HLT castor muons!!! HLT_Random
# 'file:/eos/cms/store/hidata/HIRun2018A/ZeroBias/RAW/v1/000/326/683/00000/17F933F7-A94E-F249-8594-A2DB663714BE.root',
# 'file:/eos/cms/store/hidata/HIRun2018A/ZeroBias/RAW/v1/000/326/683/00000/72B58400-4F77-E846-9203-2E9BB0B59A80.root',
# 'file:/eos/cms/store/hidata/HIRun2018A/ZeroBias/RAW/v1/000/326/683/00000/9969141F-74EF-A843-BB07-5CE0E27A7543.root',
# 'file:/eos/cms/store/hidata/HIRun2018A/ZeroBias/RAW/v1/000/326/683/00000/B123B857-148B-4D43-8393-21A2D951FA04.root',
# 'file:/eos/cms/store/hidata/HIRun2018A/ZeroBias/RAW/v1/000/326/683/00000/C1FF7BAF-66B7-574A-B8A4-2D78BBD2F590.root',
# 'file:/eos/cms/store/hidata/HIRun2018A/ZeroBias/RAW/v1/000/326/683/00000/CBEE5535-3F43-6A40-B880-CBDD26942879.root',
# 'file:/eos/cms/store/hidata/HIRun2018A/ZeroBias/RAW/v1/000/326/683/00000/FA114F40-8BDA-5045-A55A-7F191AE86F79.root',
# 'file:/eos/cms/store/hidata/HIRun2018A/ZeroBias/RAW/v1/000/326/683/00000/FF264181-09C7-CB43-B094-81CD88A4251F.root',


#'file:/eos/cms/store/hidata/HIRun2018A/ZeroBias/RAW/v1/000/326/710/00000/A9C7A5A9-11D3-5148-988C-BC0D2ACC0DD2.root',
#'file:/eos/cms/store/hidata/HIRun2018A/ZeroBias/RAW/v1/000/326/710/00000/C1332E16-0928-DC47-9C71-92F1E4F1024D.root',

#'file:/eos/cms/store/hidata/HIRun2018A/MinimumBias/RAW/v1/000/326/710/00000/35E47230-62E0-4F45-AC30-29FBF6C5328A.root',
#'file:/eos/cms/store/hidata/HIRun2018A/MinimumBias/RAW/v1/000/326/710/00000/5BEAC802-2AA5-9A4D-91B6-39A45FC89637.root',
#'file:/eos/cms/store/hidata/HIRun2018A/MinimumBias/RAW/v1/000/326/710/00000/78D6B4A0-3783-454C-B9C5-816C2B96F863.root',
#'file:/eos/cms/store/hidata/HIRun2018A/MinimumBias/RAW/v1/000/326/710/00000/87203823-6818-E448-9BBA-6F9EF31289A4.root',


        )

)             

#        "file:/eos/cms/store/hidata/HIRun2018A/ZeroBias/RAW/v1/000/326/614/00000/4983FF8A-2894-824A-A9A2-6DD6E4100F9D.root"

# "file:/eos/cms/store/hidata/HIRun2018A/ZeroBias/RAW/v1/000/326/612/00000/9EF7F37B-F33F-954B-93FC-F5C1A10DC527.root",
# "file:/eos/cms/store/hidata/HIRun2018A/ZeroBias/RAW/v1/000/326/611/00000/A506B97D-9ED7-5445-8AE7-D3FBB7B4C74A.root",
# "file:/eos/cms/store/hidata/HIRun2018A/ZeroBias/RAW/v1/000/326/610/00000/EF9840FF-55A9-ED41-A95D-88BEB0905528.root",
# "file:/eos/cms/store/hidata/HIRun2018A/ZeroBias/RAW/v1/000/326/609/00000/77419629-73A1-BC40-AE84-583371BB087D.root",


#        'file:/eos/cms/store/hidata/HIRun2018A/ZeroBias/RAW/v1/000/326/613/00000/A385468F-5777-554B-8781-2CC27680859D.root'

# /eos/cms/store/hidata/HIRun2018/ZeroBias/RAW/v1/000/325/860/00000/0A4C73CB-ED9A-4C4E-B145-9EFF69C456E0.root")
# /eos/cms/store/hidata/HIRun2018/ZeroBias/RAW/v1/000/325/867/00000/29DCC16A-4E7A-6A46-9A0F-D821DD8A2BC7.root")




process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))

process.MessageLogger.cerr.FwkReport.reportEvery = 1
process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True),
#    SkipEvent = cms.untracked.vstring('ProductNotFound')
    )

 # HLT path filter 
import HLTrigger.HLTfilters.hltHighLevel_cfi 
process.TriggerFilter = HLTrigger.HLTfilters.hltHighLevel_cfi.hltHighLevel.clone(
     TriggerResultsTag = cms.InputTag("TriggerResults", "", "HLT"),
     #HLTPaths = ['HLT_L1CastorMuon_v*','HLT_L1Tech59_CASTORHaloMuon_v*'], #  # provide list of HLT paths (or patterns) you want
     #HLTPaths = ['HLT_Random_v*'],
     HLTPaths = ['HLT_L1CastorMuon_v*'],
     #HLTPaths = ['*'],
     andOr = cms.bool(True),   # how to deal with multiple triggers: True (OR) accept if ANY is true, False (AND) accept if ALL are true
     throw = cms.bool(True)  ## NNED THis FOR 2015 June since the HLT trigger was renamed! 
) 


# get custom CASTOR conditions to mark/remove bad channels
if useCustomCond:
    process.load("CondCore.DBCommon.CondDBSetup_cfi")
    process.CastorDbProducer = cms.ESProducer("CastorDbProducer")

    process.es_ascii = cms.ESSource("CastorTextCalibrations",
                                    input = cms.VPSet(
            cms.PSet(
                object = cms.string('ChannelQuality'),
                file = cms.FileInPath('data/customcond/castor/BadChannels2015.txt')
                ),
            )
                                    )

    process.es_prefer_castor = cms.ESPrefer('CastorTextCalibrations', 'es_ascii')


# Here starts the CFF specific part
import CommonFSQFramework.Core.customizePAT
process = CommonFSQFramework.Core.customizePAT.customize(process)
process = CommonFSQFramework.Core.customizePAT.customizeGT(process)

# define treeproducer
process.CFFTree = cms.EDAnalyzer("CFFTreeProducer")


#import CommonFSQFramework.Core.CaloRecHitViewsConfigs
import CommonFSQFramework.Core.CaloTowerViewsConfigs
import CommonFSQFramework.Core.CastorViewsConfigs
#import CommonFSQFramework.Core.PFObjectsViewsConfigs
import CommonFSQFramework.Core.TriggerResultsViewsConfigs


#process.CFFTree._Parameterizable__setParameters(CommonFSQFramework.Core.CastorViewsConfigs.get(["CastorRecHitViewFull"]))
process.CFFTree._Parameterizable__setParameters(CommonFSQFramework.Core.CastorViewsConfigs.get(["CastorRecHitViewFull","CastorTowerView"]))
process.CFFTree._Parameterizable__setParameters(CommonFSQFramework.Core.TriggerResultsViewsConfigs.get(["L1GTriggerResultsView"]))
#process.CFFTree._Parameterizable__setParameters(CommonFSQFramework.Core.CaloRecHitViewsConfigs.get(["HFRecHitView"]))
#process.CFFTree._Parameterizable__setParameters(CommonFSQFramework.Core.CaloTowerViewsConfigs.get(["CaloTowerView"]))
#process.CFFTree._Parameterizable__setParameters(CommonFSQFramework.Core.PFObjectsViewsConfigs.get(["PFCandidateView","ecalPFClusterView","hcalPFClusterView","hfPFClusterView"]))



# process.dttfDigis.DTTF_FED_Source = 'rawDataRepacker'
# process.gctDigis.inputLabel = 'rawDataRepacker'
# process.gtDigis.DaqGtInputTag = 'rawDataRepacker'
# process.gtEvmDigis.EvmGtInputTag = 'rawDataRepacker'
# process.castorDigis.InputLabel = 'rawDataRepacker'
# process.scalersRawToDigi.scalersInputTag = 'rawDataRepacker'
# process.csctfDigis.producer = 'rawDataRepacker'


process.dump=cms.EDAnalyzer('EventContentAnalyzer')

#process.FiltererdTree = cms.Path(process.dump*process.TriggerFilter*process.CFFTree)
process.FiltererdTree = cms.Path(process.TriggerFilter*process.CFFTree)

#process.raw2digi_custom_step = cms.Path(process.RawToDigi) # L1TRawToDigi*process.castorDigis)
process.raw2digi_custom_step = cms.Path(process.L1TRawToDigi*process.castorDigis)
#process.raw2digi_step = cms.Path(process.castorDigis)
#process.castorreco_step = cms.Path(process.reconstruction)
process.castorreco_step = cms.Path(process.castorreco*process.CastorFullReco)

process = CommonFSQFramework.Core.customizePAT.addPath(process, process.raw2digi_custom_step)
process = CommonFSQFramework.Core.customizePAT.addPath(process, process.castorreco_step)
process = CommonFSQFramework.Core.customizePAT.addPath(process, process.FiltererdTree)
