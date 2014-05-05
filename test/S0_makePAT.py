## import skeleton process
# based on patTuple_addJets_cfg_DONOTEDIT.py
from PhysicsTools.PatAlgos.patTemplate_cfg import *
## switch to uncheduled mode
process.options.allowUnscheduled = cms.untracked.bool(True)
########################################################################
#
# Configure event selection here
#
########################################################################
minJetPT = 28
minJets  = 2
# on which jets should I base my event selection?
usePFJetsInSelection = True
useCaloJetsInSelection = True
usePFCHSJetsInSelection = False
#
# above setting means: save all events having two PF jets with pt>35
#                        or  two  calo jets with pt>35
# PFCHS jets are not used in selection (warning/TODO - currently they 
#                                                  will be saved anyway)
########################################################################
#
# Input file, global tag
#
########################################################################
## See  https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideFrontierConditions
process.GlobalTag.globaltag = "START62_V1::All" 

process.maxEvents.input = 150
indir = '/scratch/scratch0/data/store/mc/Fall13dr/QCD_Pt-50to80_Tune4C_13TeV_pythia8/AODSIM/castor_tsg_PU1bx50_POSTLS162_V1-v1/00000/'
f = indir + '00108F5C-D873-E311-BD7F-002618943914.root'
process.source.fileNames = [
     'file:'+f
]
process.out.fileName = 'mnTrgAna_PAT.root'
process.options.wantSummary = False
process.MessageLogger.cerr.FwkReport.reportEvery = 50


process.TFileService = cms.Service("TFileService", fileName = cms.string("trees.root") )
## to run in un-scheduled mode uncomment the following lines
process.load("PhysicsTools.PatAlgos.producersLayer1.patCandidates_cff")
process.load("PhysicsTools.PatAlgos.selectionLayer1.selectedPatCandidates_cff")
from PhysicsTools.PatAlgos.tools.metTools import addMETCollection

from PhysicsTools.PatAlgos.tools.jetTools import addJetCollection
from PhysicsTools.PatAlgos.tools.jetTools import switchJetCollection

## uncomment the following lines to add ak5JPTJets to your PAT output
#addJetCollection(process,cms.InputTag('JetPlusTrackZSPCorJetAntiKt5'),
#                 'AK5', 'JPT',
#                 doJTA        = True,
#                 doBTagging   = True,
#                 jetCorrLabel = ('AK5JPT', cms.vstring(['L1Offset', 'L1JPTOffset', 'L2Relative', 'L3Absolute'])),
#                 doType1MET   = False,
#                 doL1Cleaning = False,
#                 doL1Counters = True,
#                 genJetCollection = cms.InputTag("ak5GenJets"),
#                 doJetID      = True,
#                 jetIdLabel   = "ak5"
#                 )

## uncomment the following lines to add ak5PFJetsCHS to your PAT output
addJetCollection(
   process,
   labelName = 'AK5PFCHS',
   jetSource = cms.InputTag('ak5PFJetsCHS'),
   jetCorrections = ('AK5PFchs', cms.vstring(['L1FastJet', 'L2Relative', 'L3Absolute']), 'Type-2')
   )
process.patJetsAK5PFCHS.addJetID=True
process.patJetsAK5PFCHS.jetIDMap="ak5JetID"

## uncomment the following lines to add kt6CaloJets to your PAT output
postfixAK5Calo = 'Copy'
addJetCollection(
   process,
   postfix   = postfixAK5Calo,
   labelName = 'AK5Calo',
   jetSource = cms.InputTag('ak5CaloJets'),
   jetCorrections = ('AK5Calo', cms.vstring(['L1Offset', 'L2Relative', 'L3Absolute']), 'Type-2'),
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
getattr(process, 'patJetsAK5Calo' + postfixAK5Calo).addJetID=True
getattr(process, 'patJetsAK5Calo' + postfixAK5Calo).jetIDMap="ak5JetID"
process.out.outputCommands.append( 'drop *_selectedPatJetsAK5Calo%s_pfCandidates_*'%(postfixAK5Calo) )
#process.patJetsAK5Calo.addJetID=True
#process.patJetsAK5Calo.jetIDMap="ak5JetID"

## uncomment the following lines to add ak5PFJets to your PAT output
switchJetCollection(
   process,
   jetSource = cms.InputTag('ak5PFJets'),
   jetCorrections = ('AK5PF', cms.vstring(['L1FastJet', 'L2Relative', 'L3Absolute']), 'Type-2'),
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



keepProds = cms.untracked.vstring() 
keepProds.append("keep *_addPileupInfo_*_*")
keepProds.append("keep recoVertexs_offlinePrimaryVertices__RECO")
#keepProds.append("keep recoVertexs_offlinePrimaryVerticesWithBS__RECO") # what to keep - with or wo beamspot?
keepProds.append("keep GenEventInfoProduct_generator__SIM")
keepProds.append("keep edmMergeableCounter_*_*_*") # for event counters inside lumi tree
# TODO - generator weight

keepProds.extend(['keep edmTriggerResults_*_*_HLT',
                  'keep triggerTriggerEvent_*_*_*',
                  'keep *_hltL1extraParticlesCentral_*_*',
                  'keep *_hltL1extraParticlesNonIsolated_*_*',
                  'keep *_hltL1extraParticlesTau_*_*',
                  'keep l1extra*_*_*_*']
)





process.out.outputCommands.extend(keepProds)

process.initialCntr = cms.EDProducer("EventCountProducer")
process.initialSequence = cms.Sequence(process.initialCntr)

jetSel = "pt > " + str(minJetPT)

interestingJetsCollections = {}
if usePFJetsInSelection:
    interestingJetsCollections["PF"] = "selectedPatJets"
if useCaloJetsInSelection:
    interestingJetsCollections["Calo"] = "selectedPatJetsAK5CaloCopy"
if usePFCHSJetsInSelection:
    interestingJetsCollections["PFCHS"] = "selectedPatJetsAK5PFCHS"


selectorPaths = cms.vstring()
process.schedule = cms.Schedule()
for jc in interestingJetsCollections:
    selector = cms.EDFilter("PATJetSelector",
        src = cms.InputTag(interestingJetsCollections[jc]),
        cut = cms.string(jetSel)
    )
    selectorLabel = "selectedTFJets"+jc

    filter = cms.EDFilter("PATCandViewCountFilter",
        maxNumber = cms.uint32(999999),
        src = cms.InputTag(selectorLabel),
        minNumber = cms.uint32(minJets)
    )
    filterLabel = "filterTFJets"+jc

    counter = cms.EDProducer("EventCountProducer")
    counterLabel = "countTFJets"+jc

    setattr(process, selectorLabel, selector)
    setattr(process, filterLabel, filter)
    setattr(process, counterLabel, counter)

    pathTF = cms.Path( process.initialSequence
                      *getattr(process,selectorLabel)
                      *getattr(process,filterLabel) 
                      *getattr(process,counterLabel) 
                     )
    pathTFlabel="p"+jc
    setattr(process, pathTFlabel, pathTF)
    selectorPaths.append(pathTFlabel)
    process.schedule.append(getattr(process, pathTFlabel))


process.treeProd1 = cms.EDAnalyzer("ExampleTreeProducer")
process.p = cms.Path(process.treeProd1)
process.schedule.append(process.p) # TODO tree producer will run through all events, not depending on the filtering results
process.schedule.append(process.outpath)






process.out.SelectEvents = cms.untracked.PSet(
        SelectEvents = selectorPaths
)

