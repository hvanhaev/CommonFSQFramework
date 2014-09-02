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

## uncomment the following lines to add ak5PFJetsCHS to your PAT output
labelAK5PFCHS = 'AK5PFCHS'
postfixAK5PFCHS = 'Copy'
addJetCollection(
   process,
   postfix   = postfixAK5PFCHS,
   labelName = labelAK5PFCHS,
   jetSource = cms.InputTag('ak5PFJetsCHS'),
   jetCorrections = ('AK5PFchs', cms.vstring(['L1FastJet', 'L2Relative', 'L3Absolute']), 'Type-2')
   )
process.out.outputCommands.append( 'drop *_selectedPatJets%s%s_caloTowers_*'%( labelAK5PFCHS, postfixAK5PFCHS ) )

# ak4PFJetsCHS
labelAK4PFCHS = 'AK4PFCHS'
postfixAK4PFCHS = 'Copy'
addJetCollection(
   process,
   postfix   = postfixAK4PFCHS,
   labelName = labelAK4PFCHS,
   jetSource = cms.InputTag('ak4PFJetsCHS'),
   jetCorrections = ('AK5PFchs', cms.vstring(['L1FastJet', 'L2Relative', 'L3Absolute']), 'Type-2')
   )
process.out.outputCommands.append( 'drop *_selectedPatJets%s%s_caloTowers_*'%( labelAK4PFCHS, postfixAK4PFCHS ) )



# uncomment the following lines to add ak5PFJets to your PAT output
labelAK5PF = 'AK5PF'
addJetCollection(
   process,
   labelName = labelAK5PF,
   jetSource = cms.InputTag('ak5PFJets'),
   jetCorrections = ('AK5PF', cms.vstring(['L1FastJet', 'L2Relative', 'L3Absolute']), 'Type-1'),
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
   jetCorrections = ('AK5PFchs', cms.vstring(['L1FastJet', 'L2Relative', 'L3Absolute']), 'None'), # FIXME: Use proper JECs, as soon as available
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
process.GlobalTag.globaltag = "POSTLS170_V6::All"
f= "0012A88B-D4EB-E311-9B1E-0025905A6094.root"
f = '/nfs/dust/cms/user/fruboest/2014.07.CSA14/data/66211A89-3DF8-E311-A6CB-02163E00E9CC.root'
process.source.fileNames = [
     'file:'+f
]


import MNTriggerStudies.MNTriggerAna.customizePAT
process = MNTriggerStudies.MNTriggerAna.customizePAT.customize(process)

process.MNTriggerAnaNew = cms.EDAnalyzer("MNTriggerAnaNew",
    JetViewPFAK4CHS  = cms.PSet(
        disableJetID = cms.bool(True),
        optionalCaloJets4ID = cms.InputTag("ak5CaloJets","","RECO"),
        optionalCaloID4ID  = cms.InputTag("ak5JetID"),
        branchPrefix = cms.untracked.string("PFAK4CHS"),
        maxEta = cms.double(4.9999),
        minPt = cms.double(3),
        maxnum = cms.int32(3),
        input = cms.InputTag("selectedPatJetsAK4PFCHSCopy"),
        variations= cms.vstring("", "jecUp", "jecDown"),
        jerFactors = cms.vstring(  # PF10
                "5.5 1 0.007 0.07 0.072"),
    ),

    JetViewPFAK5CHS  = cms.PSet(
        disableJetID = cms.bool(True),
        optionalCaloJets4ID = cms.InputTag("ak5CaloJets","","RECO"),
        optionalCaloID4ID  = cms.InputTag("ak5JetID"),
        branchPrefix = cms.untracked.string("PFAK5CHS"),
        maxEta = cms.double(4.9999),
        minPt = cms.double(3),
        maxnum = cms.int32(3),
        input = cms.InputTag("selectedPatJetsAK5PFCHSCopy"),
        variations= cms.vstring("", "jecUp", "jecDown"),
        jerFactors = cms.vstring(  # PF10
                "5.5 1 0.007 0.07 0.072"),
    ),



    JetViewPF  = cms.PSet(
        disableJetID = cms.bool(True),
        optionalCaloJets4ID = cms.InputTag("ak5CaloJets","","RECO"),
        optionalCaloID4ID  = cms.InputTag("ak5JetID"),
        branchPrefix = cms.untracked.string("PF"),
        maxEta = cms.double(4.9999),
        minPt = cms.double(3),
        maxnum = cms.int32(3),
        input = cms.InputTag("selectedPatJets"),
        variations= cms.vstring("", "jecUp", "jecDown"),
        jerFactors = cms.vstring(  # PF10
                "5.5 1 0.007 0.07 0.072"),
    ),


    L1JetsView  = cms.PSet(
        branchPrefix = cms.untracked.string("old"),
        src =  cms.VInputTag(cms.InputTag("l1extraParticles","Central"),
                cms.InputTag("l1extraParticles","Forward"),
                cms.InputTag("l1extraParticles","Tau")
        ),
    ),

    L1JetsViewStage1  = cms.PSet(
        branchPrefix = cms.untracked.string("stage1"),
        src =  cms.VInputTag(cms.InputTag("l1ExtraReEmul","Central"),
                cms.InputTag("l1ExtraReEmul","Forward")
        ),
    ),




)
process = MNTriggerStudies.MNTriggerAna.customizePAT.addTreeProducer(process, process.MNTriggerAnaNew)

prefix='root://xrootd.ba.infn.it/'
sec1=prefix+"/store/mc/Spring14dr/QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8/AODSIM/Flat20to50_POSTLS170_V5-v1/00000/9480AA58-E3DD-E311-8FE3-002590D0AFEC.root"
sec2=prefix+"/store/mc/Spring14dr/QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8/AODSIM/Flat20to50_POSTLS170_V5-v1/00000/3A28427D-DEDD-E311-8C68-20CF305616E0.root"
primary='file:/pnfs/desy.de/cms/tier2/store/user/fruboes/QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8/20140812_HLTJets/db6fe0c1c3daf8225c4ac7289ea45cd0/outputFULL_3_1_4FA.root'

primary= "file:/pnfs/desy.de/cms/tier2/store/user/fruboes/QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8/20140813_HLTJets/db6fe0c1c3daf8225c4ac7289ea45cd0/outputFULL_11_1_WVC.root"
primary = "file:/pnfs/desy.de/cms/tier2/store/user/fruboes/QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8/20140813C_HLTJets/1914e7f200d7a3952c1631dd40280690/outputFULL_17_1_UZk.root"

primary="file:/nfs/dust/cms/user/fruboest/2014.09.TestL1Stage1/CMSSW_7_1_5/src/ProduceHLTAndL1/outputFULL.root"

process.source = cms.Source("PoolSource",
#    secondaryFileNames = cms.untracked.vstring([sec1, sec2]),
    fileNames = cms.untracked.vstring([primary]),
    bypassVersionCheck = cms.untracked.bool(True)
)

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





