## import skeleton process
# based on patTuple_addJets_cfg_DONOTEDIT.py
#from PhysicsTools.PatAlgos.patTemplate_cfg import *
from patTemplate_cfg_mod import *


doHLTPFJets = True

## switch to uncheduled mode
process.options.allowUnscheduled = cms.untracked.bool(True)
########################################################################
#
# Configure event selection here
#
########################################################################
minJetPT = 30
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
#process.GlobalTag.globaltag = "START62_V1::All" 
process.GlobalTag.globaltag = "POSTLS162_V2::All" 

process.maxEvents.input = 100
#indir = '/scratch/scratch0/data/store/mc/Fall13dr/QCD_Pt-50to80_Tune4C_13TeV_pythia8/AODSIM/castor_tsg_PU1bx50_POSTLS162_V1-v1/00000/'
#f = indir + '00108F5C-D873-E311-BD7F-002618943914.root'

indir = '/scratch/scratch0/data/store/mc/Fall13dr/QCD_Pt-15to30_Tune4C_13TeV_pythia8/AODSIM/castor_tsg_PU1bx50_POSTLS162_V1-v1/00000/'
f = indir + '1EB67544-9074-E311-B8F7-0025905A6132.root'
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


from PhysicsTools.PatAlgos.tools.trigTools import *
triggerProcess='HLT'
switchOnTrigger(process)

from PhysicsTools.PatAlgos.triggerLayer1.triggerMatcherExamples_cfi import somePatJetTriggerMatchHLTPFJet40
process.triggerMatchPF = somePatJetTriggerMatchHLTPFJet40.clone(matchedCuts='type("TriggerJet" )', src="selectedPatJets")
process.triggerMatchPFCHS = somePatJetTriggerMatchHLTPFJet40.clone(matchedCuts='type("TriggerJet" )', src="selectedPatJetsAK5PFCHS")
process.triggerMatchCalo = somePatJetTriggerMatchHLTPFJet40.clone(matchedCuts='type("TriggerJet" )', src="selectedPatJetsAK5CaloCopy")

switchOnTriggerMatching(process, ["triggerMatchPF", "triggerMatchPFCHS", "triggerMatchCalo"] )
# seems not to change anything:
#switchOnTriggerMatchEmbedding(process, ["triggerMatchPF", "triggerMatchPFCHS", "triggerMatchCalo"] )
#switchOnTriggerMatchEmbedding(process)

#switchOnTrigger(process, 'patTrigger', 'patTriggerEvent', 'patDefaultSequence', triggerProcess, 'out')


keepProds = cms.untracked.vstring() 
keepProds.append("keep *_addPileupInfo_*_*")
keepProds.append("keep *_XS_*_*")
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


"selectedPatJets"
"selectedPatJetsAK5CaloCopy"
"selectedPatJetsAK5PFCHS"



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


process.exampleTree = cms.EDAnalyzer("ExampleTreeProducer")
process.mnTriggerAna = cms.EDAnalyzer("MNTriggerAna")
process.infoHisto = cms.EDAnalyzer("SaveCountHistoInTreeFile")
process.pTreeProducers = cms.Path(process.infoHisto*process.exampleTree*process.mnTriggerAna)

# Note: despite we are putting this value into every event waste of space is neglible thanks to root branch compression.
process.XS =  cms.EDProducer("DoubleProducer",
    value = cms.double(-1),
)

process.pUtil = cms.Path(process.XS)

process.schedule.append(process.pUtil)
process.schedule.append(process.pTreeProducers) # TODO tree producer will run through all events, not depending on the filtering results
process.schedule.append(process.outpath)

import os
if "TMFSampleName" not in os.environ:
    print "#"*80
    print "#"
    print "#    Note: 'TMFSampleName' variable not found in environment."
    print "#             Will embed default values (XS wont be set)"
    print "#"
    print "#"*80
else:
    s = os.environ["TMFSampleName"]
    print "Customizing to: ", s
    import MNTriggerStudies.MNTriggerAna.Util
    sampleList=MNTriggerStudies.MNTriggerAna.Util.getAnaDefinition("sam")
    anaVersion=MNTriggerStudies.MNTriggerAna.Util.getAnaDefinition("anaVersion")
    XS = sampleList[s]["XS"]
    isData =  sampleList[s]["isData"]
    
    stringForProv = "\n"+"#"*80+"\n"
    stringForProv += "Ana version: " + anaVersion + "\n"
    stringForProv += "XS = " + str(XS) + "\n"
    process.XS.value = XS
    stringForProv += "isData = " + str(isData) + "\n" # not used...yet
    stringForProv += "#"*80+"\n"

    print stringForProv
    # attach the string to one of the modules, so it will show in the prov data
    # (use edmProvDump on the PAT file to see it)
    process.XS.provHack = cms.string(stringForProv)
    process.TMFDataForProv = cms.PSet(notes = cms.string("test"))

    # also - GT 

process.out.SelectEvents = cms.untracked.PSet(
        SelectEvents = selectorPaths
)



if doHLTPFJets:
    process.load('Configuration.StandardSequences.Services_cff')
    process.load('HLTrigger.Configuration.HLT_GRun_cff')

    # remove all paths that were imported. Unscheduled execution may try running it all otherwise
    import FWCore.ParameterSet.SequenceTypes as st
    for a in dir(process):
        attr = getattr(process, a)
        if type(attr) == st.Path:
            if not a.startswith("HLT_"): continue
            #print "Removing", a
            del attr

    


    #from HLTrigger.Configuration.HLT_GRun_cff import hltPrePFJet40, HLTBeginSequence, HLTPFL1FastL2L3ReconstructionSequence

    #process.hltL1sL1SingleJet8 =  process.hltL1sL1SingleJet16.clone( L1SeedsLogicalExpression = cms.string( "L1_SingleJet8" ) )
    process.hltPrePFJet15  = process.hltPrePFJet40.clone()
    process.hlt1PFJet15 = process.hlt1PFJet40.clone( MinPt = cms.double(15.0), inputTag = cms.InputTag("hltAK5PFJetL1FastL2L3Corrected"))

    # note L1 seeding is disabled, since low enough L1 seed is not present in L1 menu
    process.HLT_PFJet15_v1 = cms.Path( process.HLTBeginSequence+
                                       #process.hltL1sL1SingleJet8 +  # TODO
                                       process.hltPrePFJet15 +  # TODO
                                       process.HLTPFL1FastL2L3ReconstructionSequence +
                                       process.HLTPFnoPUL1FastL2L3ReconstructionSequence + 
                                       ##process.hltPFJetsL1Matched + 
                                       process.hlt1PFJet15 + #  TODO
                                       process.HLTEndSequence )

    placeAt = len(process.schedule)-2
    process.schedule.insert(placeAt, process.HLT_PFJet15_v1)

    keepProds = cms.untracked.vstring()
    keepProds.append("keep *_hltAK5PFJetL1FastL2L3Corrected_*_*")
    keepProds.append("keep *_hltAK5PFJetL1FastL2L3CorrectedNoPU_*_*")
    process.out.outputCommands.extend(keepProds)

    fAOD = "/scratch/scratch0/data/store/mc/Fall13dr/QCD_Pt-15to30_Tune4C_13TeV_pythia8/AODSIM/castor_tsg_PU1bx50_POSTLS162_V1-v1/00000/C2DF7978-8A74-E311-BFCC-00304867920C.root"

    #fRAW = "/scratch/scratch0/data/store/mc/Fall13dr/QCD_Pt-15to30_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU1bx50_POSTLS162_V1-v1/00000/00352658-5774-E311-AD39-0025905A60B6.root"
    fRAW = "/scratch/scratch0/data/store/mc/Fall13dr/QCD_Pt-15to30_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU1bx50_POSTLS162_V1-v1/00000/D0D5CE25-5774-E311-8FB2-0025905A605E.root"
    process.source = cms.Source("PoolSource",
        secondaryFileNames = cms.untracked.vstring('file:'+fRAW),
        fileNames = cms.untracked.vstring('file:'+fAOD)
    )

    # customisation of the process.
    # Automatic addition of the customisation function from HLTrigger.Configuration.customizeHLTforMC
    from HLTrigger.Configuration.customizeHLTforMC import customizeHLTforMC
    #call to customisation function customizeHLTforMC imported from HLTrigger.Configuration.customizeHLTforMC
    process = customizeHLTforMC(process)
    # Automatic addition of the customisation function from SLHCUpgradeSimulations.Configuration.postLS1Customs
    from SLHCUpgradeSimulations.Configuration.postLS1Customs import customisePostLS1
    #call to customisation function customisePostLS1 imported from SLHCUpgradeSimulations.Configuration.postLS1Customs
    process = customisePostLS1(process)





            
           


