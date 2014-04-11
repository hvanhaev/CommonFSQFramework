## import skeleton process
# based on patTuple_addJets_cfg_DONOTEDIT.py

from PhysicsTools.PatAlgos.patTemplate_cfg import *
## switch to uncheduled mode
process.options.allowUnscheduled = cms.untracked.bool(True)

## to run in un-scheduled mode uncomment the following lines
process.load("PhysicsTools.PatAlgos.producersLayer1.patCandidates_cff")
process.load("PhysicsTools.PatAlgos.selectionLayer1.selectedPatCandidates_cff")
from PhysicsTools.PatAlgos.tools.metTools import addMETCollection

#addMETCollection(process, labelName='patMETTC', metSource='tcMet')
#addMETCollection(process, labelName='patMETPF', metSource='pfType1CorrectedMet')

## uncomment the following line to add different jet collections
## to the event content
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


##process.Tracer = cms.Service("Tracer")
#process.p = cms.Path(
    #process.selectedPatCandidates
    #*process.selectedPatJetsAK5Calo
    #*process.selectedPatJetsAK7Calo
    #)


keepProds = cms.untracked.vstring() 
keepProds.append("keep *_addPileupInfo_*_*")
keepProds.append("keep recoVertexs_offlinePrimaryVertices__RECO")
#keepProds.append("keep recoVertexs_offlinePrimaryVerticesWithBS__RECO") # what to keep - with or wo beamspot?
keepProds.append("keep GenEventInfoProduct_generator__SIM")

process.maxEvents.input = 10
#process.out.outputCommands = [ ... ] 
process.out.outputCommands.extend(keepProds)
print process.out.outputCommands

process.out.fileName = 'mnTrgAna_PAT.root'
process.options.wantSummary = False

process.GlobalTag.globaltag = "START62_V1::All" ## (according to https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideFrontierConditions)
indir = '/scratch/scratch0/data/store/mc/Fall13dr/QCD_Pt-50to80_Tune4C_13TeV_pythia8/AODSIM/castor_tsg_PU1bx50_POSTLS162_V1-v1/00000/'
f = indir + '00108F5C-D873-E311-BD7F-002618943914.root'
process.source.fileNames = [
     'file:'+f
]






