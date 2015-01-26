## import skeleton process
# from  $CMSSW_RELEASE_BASE/src/PhysicsTools/PatAlgos/test/patTuple_addJets_cfg.py
from PhysicsTools.PatAlgos.patTemplate_cfg import *
## switch to uncheduled mode
process.options.allowUnscheduled = cms.untracked.bool(True)
#process.Tracer = cms.Service("Tracer")

process.load("PhysicsTools.PatAlgos.producersLayer1.patCandidates_cff")
process.load("PhysicsTools.PatAlgos.selectionLayer1.selectedPatCandidates_cff")

from PhysicsTools.PatAlgos.tools.metTools import addMETCollection
addMETCollection(process, labelName='patMETCalo', metSource='met')
addMETCollection(process, labelName='patMETPF', metSource='pfType1CorrectedMet')
addMETCollection(process, labelName='patMETTC', metSource='tcMet')

## uncomment the following line to add different jet collections
## to the event content
from PhysicsTools.PatAlgos.tools.jetTools import addJetCollection
from PhysicsTools.PatAlgos.tools.jetTools import switchJetCollection

#runOn62 = True
runOn62 = False


## uncomment the following lines to add ak5PFJetsCHS to your PAT output
labelAK5PFCHS = 'AK5PFCHS'
postfixAK5PFCHS = 'Copy'
addJetCollection(
   process,
   postfix   = postfixAK5PFCHS,
   labelName = labelAK5PFCHS,
   jetSource = cms.InputTag('ak5PFJetsCHS'),
   jetCorrections = ('AK5PFchsOwca', cms.vstring(['L1FastJet', 'L2Relative', 'L3Absolute']), 'Type-2')
   )
process.out.outputCommands.append( 'drop *_selectedPatJets%s%s_caloTowers_*'%( labelAK5PFCHS, postfixAK5PFCHS ) )


if not runOn62:
# ak4PFJetsCHS
    labelAK4PFCHS = 'AK4PFCHS'
    postfixAK4PFCHS = 'Copy'
    addJetCollection(
       process,
       postfix   = postfixAK4PFCHS,
       labelName = labelAK4PFCHS,
       jetSource = cms.InputTag('ak4PFJetsCHS'),
       jetCorrections = ('AK4PFchsOwca', cms.vstring(['L1FastJet', 'L2Relative', 'L3Absolute']), 'Type-2')
       )
    process.out.outputCommands.append( 'drop *_selectedPatJets%s%s_caloTowers_*'%( labelAK4PFCHS, postfixAK4PFCHS ) )



# uncomment the following lines to add ak5PFJets to your PAT output
labelAK5PF = 'AK5PF'
addJetCollection(
   process,
   labelName = labelAK5PF,
   jetSource = cms.InputTag('ak5PFJets'),
   jetCorrections = ('AK5PFOwca', cms.vstring(['L1FastJet', 'L2Relative', 'L3Absolute']), 'Type-1'),
   btagDiscriminators = [
       'jetBProbabilityBJetTags'
     , 'jetProbabilityBJetTags'
     , 'trackCountingHighPurBJetTags'
     , 'trackCountingHighEffBJetTags'
     , 'simpleSecondaryVertexHighEffBJetTags'
     , 'simpleSecondaryVertexHighPurBJetTags'
     , 'combinedSecondaryVertexBJetTags'
     ],
   )
process.out.outputCommands.append( 'drop *_selectedPatJets%s_caloTowers_*'%( labelAK5PF ) )

# uncomment the following lines to add ca8PFJetsCHSPruned to your PAT output
'''
labelCA8PFCHSPruned = 'CA8PFCHSPruned'
addJetCollection(
   process,
   labelName = labelCA8PFCHSPruned,
   jetSource = cms.InputTag('ca8PFJetsCHSPruned'),
   algo = 'CA8',
   rParam = 0.8,
   genJetCollection = cms.InputTag('ak8GenJets'),
   jetCorrections = ('AK5PFchsOwca', cms.vstring(['L1FastJet', 'L2Relative', 'L3Absolute']), 'None'), # FIXME: Use proper JECs, as soon as available
   btagDiscriminators = [
       'combinedSecondaryVertexBJetTags'
     ],
   )
process.out.outputCommands.append( 'drop *_selectedPatJets%s_caloTowers_*'%( labelCA8PFCHSPruned ) )
'''

# uncomment the following lines to switch to ak5CaloJets in your PAT output
switchJetCollection(
   process,
   jetSource = cms.InputTag('ak5CaloJets'),
   jetCorrections = ('AK5Calo', cms.vstring(['L1Offset', 'L2Relative', 'L3Absolute']), 'Type-1'),
   btagDiscriminators = [
       'jetBProbabilityBJetTags'
     , 'jetProbabilityBJetTags'
     , 'trackCountingHighPurBJetTags'
     , 'trackCountingHighEffBJetTags'
     , 'simpleSecondaryVertexHighEffBJetTags'
     , 'simpleSecondaryVertexHighPurBJetTags'
     , 'combinedSecondaryVertexBJetTags'
     ],
   )
process.patJets.addJetID=True
process.patJets.jetIDMap="ak5JetID"
process.patJets.useLegacyJetMCFlavour=True # Need to use legacy flavour since the new flavour requires jet constituents which are dropped for CaloJets from AOD
process.out.outputCommands.append( 'keep *_selectedPatJets_caloTowers_*' )
process.out.outputCommands.append( 'drop *_selectedPatJets_pfCandidates_*' )

#print process.out.outputCommands

## ------------------------------------------------------
#  In addition you usually want to change the following
#  parameters:
## ------------------------------------------------------
#
#   process.GlobalTag.globaltag =  ...    ##  (according to https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideFrontierConditions)
#                                         ##
#                                         ##
process.maxEvents.input = 100
#                                         ##
#   process.out.outputCommands = [ ... ]  ##  (e.g. taken from PhysicsTools/PatAlgos/python/patEventContent_cff.py)
#                                         ##
#process.out.fileName = '0012A88B-D4EB-E311-9B1E-0025905A6094.root'
process.out.fileName = 'pat.root'
process.GlobalTag.globaltag = "POSTLS170_V7::All"

#switchOnTrigger(process, 'patTrigger', 'patTriggerEvent', 'patDefaultSequence', triggerProcess, 'out')
from PhysicsTools.PatAlgos.tools.trigTools import *
switchOnTrigger( process, hltProcess="TEST" )



import MNTriggerStudies.MNTriggerAna.customizePAT
process = MNTriggerStudies.MNTriggerAna.customizePAT.customize(process)
process.MNTriggerAnaHLTJECOnFly = cms.EDAnalyzer("MNTriggerAnaHLTJECOnFly")

process = MNTriggerStudies.MNTriggerAna.customizePAT.addTreeProducer(process, process.MNTriggerAnaHLTJECOnFly)

prefix='root://xrootd.ba.infn.it/'
sec1=prefix+"/store/mc/Spring14dr/QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8/AODSIM/Flat20to50_POSTLS170_V5-v1/00000/9480AA58-E3DD-E311-8FE3-002590D0AFEC.root"
sec2=prefix+"/store/mc/Spring14dr/QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8/AODSIM/Flat20to50_POSTLS170_V5-v1/00000/3A28427D-DEDD-E311-8C68-20CF305616E0.root"
primary='file:/pnfs/desy.de/cms/tier2/store/user/fruboes/QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8/20140812_HLTJets/db6fe0c1c3daf8225c4ac7289ea45cd0/outputFULL_3_1_4FA.root'

primary= "file:/pnfs/desy.de/cms/tier2/store/user/fruboes/QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8/20140813_HLTJets/db6fe0c1c3daf8225c4ac7289ea45cd0/outputFULL_11_1_WVC.root"
primary = "file:/pnfs/desy.de/cms/tier2/store/user/fruboes/QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8/20140813C_HLTJets/1914e7f200d7a3952c1631dd40280690/outputFULL_17_1_UZk.root"

primary="file:/pnfs/desy.de/cms/tier2/store/user/fruboes/QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8/20140902_HLTJetsPu0to10_withL1Stage1/dc64037346fa4f0c87471d40dfb5e9cf/outputFULL_99_1_Py7.root"
primary="file:/nfs/dust/cms/user/fruboest/2014.09.TestL1Stage1/CMSSW_7_1_5/src/ProduceHLTAndL1/outputFULL.root"
primary="file:/nfs/dust/cms/user/fruboest/2014.09.TestL1Stage1/CMSSW_7_1_5/src/MNTriggerStudies/MNTriggerAna/test/mnTrgAnalyzer/HLTObjectsProduction_testMyPath/outputFULL.root"


#'''
primary = 'file:/nfs/dust/cms/user/fruboest/2014.09.L1Stage1With72/CMSSW_7_2_0_pre6/src/outputFULL.root'
primary = 'file:/pnfs/desy.de/cms/tier2/store/user/fruboes/QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8/20140919_HLTJetsPu20to50_withL1Stage1_TRGJECMN_72pre6A/22e6fbeb4962d1fd2d06350795e9100e/outputFULL_1_1_VsT.root'
primary = 'file:/pnfs/desy.de/cms/tier2/store/user/fruboes/QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8/20140919_HLTJetsPu20to50_withL1Stage1_715hats/cdce4465565d0fe93d53b358060cc01e/outputFULL_1_1_mB7.root'

primary = 'file:/nfs/dust/cms/user/fruboest/2014.09.TestL1Stage1/CMSSW_7_1_5/src/MNTriggerStudies/MNTriggerAna/test/mnTrgAnalyzer/HLTObjectsProduction_20140917DoubleJetForJEC_V10/outputFULL.root'
primary = 'file:/nfs/dust/cms/user/fruboest/2014.09.TestL1Stage1/CMSSW_7_1_5/src/MNTriggerStudies/MNTriggerAna/test/mnTrgAnalyzer/HLTObjectsProduction_20140917DoubleJetForJEC_V14/outputFULL.root'
primary = 'file:/nfs/dust/cms/user/fruboest/2014.09.L1Stage1With72/CMSSW_7_2_0_pre6/src/test/outputFULL.root'
primary = 'file:/pnfs/desy.de/cms/tier2/store/user/fruboes/QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8/20141020_HLTJetsPu20to50_720pre8/ab4d935ec80dcf1194b09139dbb3a385/outputFULL_10_1_GMu.root'


primary = 'file:/nfs/dust/cms/user/fruboest/2014.10.720HLTJec/CMSSW_7_2_0/src/outputFULL.root'
primart = 'file:/pnfs/desy.de/cms/tier2/store/user/fruboes/Neutrino_Pt-2to20_gun/20141023_NuGun_HLTJetsPu20to50_720/5bf11c64ebfcb1bed227f4f3ad2897d4/outputFULL_150_1_78Y.root'
primary = "file:/pnfs/desy.de/cms/tier2//store/user/fruboes/Neutrino_Pt-2to20_gun/20141023_NuGun162_HLTJetsPu20_720/2f37f2cc398b18482efdc56e9384d725/outputFULL_1200_1_Wxg.root"

primary = "file:/nfs/dust/cms/user/fruboest/2014.10.720HLTJec/CMSSW_7_2_0/src/outputFULL.root"
primary = "file:/pnfs/desy.de/cms/tier2/store/user/fruboes/QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8/20141023V2_QCD_HLTJetsPu20to50_720/3a89b834271012cd860a1a9609fca634/outputFULL_1_1_RMc.root"

primary = "file:/nfs/dust/cms/user/fruboest/2014.11.HLT721p2/CMSSW_7_2_1_patch2/src/outputFULL.root"
primary = "file:/pnfs/desy.de/cms/tier2/store/user/fruboes/Neutrino_Pt-2to20_gun/20141119_NuGun162_HLTJetsPu20_721p2_10GeVnoAOD/e3d82636941608cd8311020ee663aad9/outputFULL_43_1_0rl.root"


primary = "file:/nfs/dust/cms/user/fruboest/2015.01.ProduceAndTestJECFromFeng/CMSSW_7_2_1_patch2/src/outputA.root"
primary = "file:/nfs/dust/cms/user/fruboest/2015.01.ProduceAndTestJECFromFeng/CMSSW_7_3_0/src/outputA.root"

process.source = cms.Source("PoolSource",
#    secondaryFileNames = cms.untracked.vstring([sec1, sec2]),
    fileNames = cms.untracked.vstring([primary]),
    bypassVersionCheck = cms.untracked.bool(True)
)
#'''



if not runOn62:
    process.patJetsAK4PFCHSCopy.addGenJetMatch = cms.bool(False)
    process.patJetsAK4PFCHSCopy.embedGenJetMatch = cms.bool(False)
    process.patJetsAK4PFCHSCopy.addGenPartonMatch = cms.bool(False)
    process.patJetsAK4PFCHSCopy.embedGenPartonMatch = cms.bool(False)
    process.patJetsAK4PFCHSCopy.useLegacyJetMCFlavour = cms.bool(False)
    process.patJetsAK4PFCHSCopy.getJetMCFlavour = cms.bool(False)

process.schedule.remove(process.outpath)
del process.outpath
del process.out

boolToFalse = ["addJetCharge",  "embedGenJetMatch", "addAssociatedTracks", "addBTagInfo", "addDiscriminators"]
boolToFalse.extend(["addGenPartonMatch", "embedGenPartonMatch", "useLegacyJetMCFlavour", "getJetMCFlavour", "addGenJetMatch"])
for m in process.__dict__:
    mod = getattr(process, m)
    for t in boolToFalse:
        if hasattr(mod, t):
            setattr(mod, t, cms.bool(False))


'''
todo = ["selectedPatJetsAK5PFCHSCopy", "selectedPatJetsAK4PFCHSCopy", "selectedPatJets"]
todoDict = {}
outsideThisProcess = set()


cnt = 0

while cnt < len(todo):
    s = todo[cnt]
    cnt += 1
    if not hasattr(process, s):
        #print "Found", s, todoDict[s]
        outsideThisProcess.add(s)
    else:
        source = getattr(process, s)
        for p in source.__dict__:
            param = getattr(source,p)
            if type(param)==cms.InputTag:
                todo.append(param.getModuleLabel())
                todoDict[param.getModuleLabel()]=param
                #print param, type(param), type(param)==cms.InputTag
                #print param.getModuleLabel()
                #print dir(param)

for s in outsideThisProcess:
    #print s#, todoDict[s]
    print "'keep *_"+s+"_*_*',"


'''



'''
process.source.dropDescendantsOfDroppedBranches = cms.untracked.bool(False)
process.source.inputCommands = cms.untracked.vstring(["drop *"])
process.source.inputCommands.extend([
#['keep *_generalTracks_*_*',
'keep *_offlinePrimaryVertices_*_*',
'keep *_generator_*_*',
'keep *_ak5JetID_*_*',
'keep *_ak5CaloJets_*_*',
'keep *_ak5GenJets_*_*',
'keep *_ak4PFJetsCHS_*_*',
'keep *_genParticles_*_*',
'keep *_ak5PFJetsCHS_*_*',
'keep *_hltAK4PFJets_*_*',
'keep *_hltAK4PFJetsCorrected_*_*',
'keep *_hltPFJetsCorrectedMatchedToL1_*_*',
'keep *_addPileupInfo_*_*',
'keep *_fixedGridRhoFastjetAll*_*_*',
'keep l1extraL1JetParticles_*_*_*'
#'keep *__*_*',
])
#'''


# JetCorrectorParametersCollection_CSA14_V4_MC_AK4PFchs
#'''
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
#'''

'''
for d in dir(process.MNTriggerAnaNew):
    if "View" not in d: continue
    if "L1" in d or "Trigger" in d: continue
    delattr(process.MNTriggerAnaNew, d)
'''

