## import skeleton process
from PhysicsTools.PatAlgos.patTemplate_cfg import *
from PhysicsTools.PatAlgos.tools.coreTools import *
####################################3#####################################3
#
#  global constants
#
####################################3#####################################3
# export TMFSampleName=JetMETTau-Run2010A-Apr21ReReco-v1
process.XS =  cms.EDProducer("DoubleProducer",
    value = cms.double(-1),
)
import os
if "TMFSampleName" not in os.environ:
    print "#"*80
    print "#"
    print "#    Note: 'TMFSampleName' variable not found in environment. Exiting"
    print "#"
    print "#"*80
    import sys
    sys.exit()
else:
    s = os.environ["TMFSampleName"]
    print "Customizing to: ", s
    import MNTriggerStudies.MNTriggerAna.Util
    sampleList=MNTriggerStudies.MNTriggerAna.Util.getAnaDefinition("sam")
    anaVersion=MNTriggerStudies.MNTriggerAna.Util.getAnaDefinition("anaVersion")
    print anaVersion
    knownJEC = ["V17TFFull", "V17TFPart", "V16TFFull", "V16TFPart"]
    ver = None
    for k in knownJEC:
        if k in anaVersion:
            ver = k
            break
    print "JEC set to:", ver

    if ver == None:
        ver = "V16TFPart"
        print "Setting JEC to", ver
        #raise Exception("Cannot determine JECset to use")

    XS = sampleList[s]["XS"]
    process.GlobalTag.globaltag = sampleList[s]["GT"]
    isData =  sampleList[s]["isData"]
    if isData:
      runOnMC = False
    else:
      runOnMC = True

    currentSampleName = s

    print currentSampleName, runOnMC, process.GlobalTag.globaltag



    stringForProv = "\n"+"#"*80+"\n"
    stringForProv += "Ana version: " + anaVersion + "\n"
    stringForProv += "XS = " + str(XS) + "\n"
    process.XS.value = XS
    stringForProv += "isData = " + str(isData) + "\n" # not used...yet
    stringForProv += "GT = " + str(process.GlobalTag.globaltag) + "\n" # not used...yet
    stringForProv += "#"*80+"\n"

    print stringForProv
    # attach the string to one of the modules, so it will show in the prov data
    # (use edmProvDump on the PAT file to see it)
    process.XS.provHack = cms.string(stringForProv)

#print "Whoaaa! Run on MC overriden!\n"*10

enableTur = True
is2011Balance = False
#anaType="ZMuMu"
#anaType="DiJet"
anaType="DiJetBalance"
#anaType = "JetTriggerEff"



if anaType == "ZMuMu":
    minJetPT = 10
    minJets = 0
    minDiMuons = 1
elif anaType == "DiJetBalance":
    minJetPT = 20
    minJets =  2
    minDiMuons = 0
elif anaType == "DiJet":
    minJetPT =  130
    minJets =    1
    minDiMuons = 0
elif anaType == "JetTriggerEff":
    minJetPT =  25
    minJets =    0
    minDiMuons = 0

process.TFileService = cms.Service("TFileService", fileName = cms.string("trees.root") )

if is2011Balance:
    minJetPT = 30



if runOnMC:
    triggerProcess='RECO'
else:
    # No trigger information avaliable in MC :/
    triggerProcess='HLT'
    from PhysicsTools.PatAlgos.tools.trigTools import *
    switchOnTrigger(process, 'patTrigger', 'patTriggerEvent', 'patDefaultSequence', triggerProcess, 'out')

process.maxEvents.input = 100
process.source.skipEvents = cms.untracked.uint32(0)



if enableTur:
    #print " see https://hypernews.cern.ch/HyperNews/CMS/get/physTools/2360/1/1.html"
    from RecoJets.Configuration.RecoPFJets_cff import kt6PFJets, ak5PFJets
    from RecoJets.Configuration.RecoJets_cff import kt6CaloJets, ak5CaloJets
    process.kt6CaloJets = copy.deepcopy(kt6CaloJets)
    process.kt6PFJets = copy.deepcopy(kt6PFJets)
    process.ak5PFJets = copy.deepcopy(ak5PFJets)
    process.ak5CaloJets = copy.deepcopy(ak5CaloJets)
    process.kt6PFJets.doRhoFastjet = True
    process.kt6CaloJets.doRhoFastjet = True
    process.ak5PFJets.doAreaFastjet = True
    process.ak5CaloJets.doAreaFastjet = True




#f = '/scratch/scratch0/data/store/mc/Summer12/QCD_Pt_40to80_fwdJet_TuneZ2star_HFshowerLibrary_7TeV_pythia6/AODSIM/LowPU2010_DR42-PU_S0_START42_V17B-v1/0000/7AE7F9AE-E7FC-E111-A5C1-E0CB4EA0A8FE.root'

#f = "/scratch/scratch0/tfruboes/DATA2/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/Summer11-PU_S4_START42_V11-v1/AODSIM/FE3430A0-BE9C-E011-AF2D-E0CB4E19F972.root"

#f = "/scratch/scratch0/data/store/data/Run2010B/Mu/AOD/Apr21ReReco-v1/0005/94F535FD-1771-E011-8502-E0CB4E4408E9.root"

#f = "/scratch/scratch0/data/store/data/Run2010B/METFwd/AOD/Apr21ReReco-v1/0005/9CC263B4-1974-E011-A817-0024E876839D.root"

if currentSampleName=="QCD_Pt-15to3000_TuneZ2star_Flat_HFshowerLibrary_7TeV_pythia6":
    f = "/scratch/scratch0/data/store/mc/Summer12/QCD_Pt-15to3000_TuneZ2star_Flat_HFshowerLibrary_7TeV_pythia6/AODSIM/LowPU2010_DR42_PU_S0_START42_V17B-v1/00000/7CFD2C30-ED2F-E211-9866-00215E2221AE.root"

elif currentSampleName=="QCD_Pt-15to1000_TuneEE3C_Flat_7TeV_herwigpp":
    f='/store/mc/Summer12/QCD_Pt-15to1000_TuneEE3C_Flat_7TeV_herwigpp/AODSIM/LowPU2010_DR42_BS2011_PU_S0_START42_V17B-v1/00000/7A7D8A2B-72CD-E311-9218-002590200B60.root'

elif currentSampleName=="JetMETTau-Run2010A-Apr21ReReco-v1":
    f='/store/data/Run2010A/JetMETTau/AOD/Apr21ReReco-v1/0000/E864253B-A66F-E011-8766-0018F3D096E6.root'

else:
    print ""
    f= "IdontCare.root"
    print "Warning: input file not set (fine if you are running with crab)"
    print ""



process.source.fileNames = [
     f
]


process.out.fileName = 'mnTrgAna_PAT.root'
process.options.wantSummary = False
process.MessageLogger.cerr.FwkReport.reportEvery = 1000
####################################################################
# Jets. Switch to pf, keep calo
####################################################################
# Setup correct JEC
####################################################
# https://twiki.cern.ch/twiki/bin/view/CMS/JECAnalysesRecommendations
#   The JEC group recommends that L1FastJet be used for PF and PFchs jets, while L1Offset be used for Calo and JPT jets. 
from PhysicsTools.PatAlgos.tools.jetTools import *
if runOnMC:
    JEClevels = ['L1FastJet', 'L2Relative', 'L3Absolute']
    JEClevelsCalo = ['L1FastJet', 'L2Relative', 'L3Absolute']
else:
    JEClevels = ['L1FastJet', 'L2Relative', 'L3Absolute', 'L2L3Residual' ]
    JEClevelsCalo = ['L1FastJet', 'L2Relative', 'L3Absolute', 'L2L3Residual']

addJetCollection(process,cms.InputTag('ak5CaloJets'),
                    'AK5', 'Calo',
                    doJTA        = True,
                    doBTagging   = True,
                    jetCorrLabel = ('AK5Calo', JEClevelsCalo),
                    doType1MET   = False,
                    genJetCollection=cms.InputTag("ak5GenJets"),
                    doJetID      = True,
                    jetIdLabel   = 'ak5')

switchJetCollection(process,cms.InputTag('ak5PFJets'),
                    doJTA        = True,
                    doBTagging   = True,
                    jetCorrLabel = ('AK5PF', JEClevels),
                    doType1MET   = False,
                    genJetCollection=cms.InputTag("ak5GenJets"),
                    doJetID      = True,
                    jetIdLabel   = 'ak5'
                    )


print "TODO jetID in calo and area computation"
process.patJetsAK5Calo.addJetID = cms.bool(False)



# XXX
if not runOnMC:
    process.patJets.addGenPartonMatch = cms.bool(False)
    #xxx process.patJetsAK5Calo.addGenPartonMatch = cms.bool(False)

process.initialCntr = cms.EDProducer("EventCountProducer")
process.finalCntrPF = cms.EDProducer("EventCountProducer")
process.finalCntrCalo = cms.EDProducer("EventCountProducer")


# Jet Preselection

#jetSel = "pt > " + str(minJetPT) + " & abs(eta) > 3.0 "
jetSel = "pt > " + str(minJetPT) 
process.selectedTFJets = cms.EDFilter("PATJetSelector",
     src = cms.InputTag("selectedPatJets"),
     cut = cms.string(jetSel)
)



process.countTFJets = cms.EDFilter("PATCandViewCountFilter",
    maxNumber = cms.uint32(999999),
    src = cms.InputTag("selectedTFJets"),
    minNumber = cms.uint32(minJets)
)


process.selectedTFCaloJets = cms.EDFilter("PATJetSelector",
     src = cms.InputTag("selectedPatJetsAK5Calo"),
     cut = cms.string(jetSel)
)

process.countTFCaloJets = cms.EDFilter("PATCandViewCountFilter",
    maxNumber = cms.uint32(999999),
    src = cms.InputTag("selectedTFCaloJets"),
    minNumber = cms.uint32(minJets)
)




# Usuall stuff
process.noscraping = cms.EDFilter("FilterOutScraping",
                                applyfilter = cms.untracked.bool(True),
                                debugOn = cms.untracked.bool(False),
                                numtrack = cms.untracked.uint32(10),
                                thresh = cms.untracked.double(0.25)
                                )

#process.load('CommonTools.RecoAlgos.HBHENoiseFilter_cfi')
process.load('CommonTools/RecoAlgos/HBHENoiseFilterResultProducer_cfi')
process.HBHENoiseFilterResultProducer2 = process.HBHENoiseFilterResultProducer.clone()
process.HBHENoiseFilterResultProducer2.minIsolatedNoiseSumE        = 999999.
process.HBHENoiseFilterResultProducer2.minNumIsolatedNoiseChannels = 999999
process.HBHENoiseFilterResultProducer2.minIsolatedNoiseSumEt       = 999999.






# TODO - MC Z cut
process.primaryVertexFilter = cms.EDFilter("GoodVertexFilter",
                                           vertexCollection = cms.InputTag('offlinePrimaryVertices'),
                                           minimumNDOF = cms.uint32(4) ,
                                           maxAbsZ = cms.double(24), 
                                           maxd0 = cms.double(2) 
                                           )


################################################################
################################################################
################################################################
## Muons 
################################################################
################################################################
################################################################
from PhysicsTools.PatAlgos.tools.muonTools import *
addMuonUserIsolation(process)
from PhysicsTools.PatAlgos.tools.trigTools import *

if not runOnMC:
    switchOnTrigger(process, 'patTrigger', 'patTriggerEvent', 'patDefaultSequence', triggerProcess, 'out')
    process.patMuonMatch = cms.EDProducer("PATTriggerMatcherDRDPtLessByR",
        #matchedCuts = cms.string('type( "TriggerL1Mu" ) || type( "TriggerMu" )'),
        matchedCuts = cms.string('type( "TriggerMuon" )'),
        src = cms.InputTag("selectedPatMuons"),
        maxDPtRel = cms.double(0.5),
        resolveByMatchQuality = cms.bool(False),
        maxDeltaR = cms.double(0.5),
        resolveAmbiguities = cms.bool(True),
        matched = cms.InputTag("patTrigger")
    )

    switchOnTriggerMatchEmbedding( process, [ "patMuonMatch"],   'patTrigger', 'patDefaultSequence',  triggerProcess, 'out' )

### TODO
#'''
process.load("CommonTools.ParticleFlow.ParticleSelectors.pfCandsForIsolation_cff")
process.load("MNTriggerStudies.MNTriggerAna.muonPFIsolation_cff")
process.patMuons.isoDeposits = cms.PSet(
        particle         = cms.InputTag("muPFIsoDepositChargedAll"),
        pfChargedHadrons = cms.InputTag("muPFIsoDepositCharged"),
        pfNeutralHadrons = cms.InputTag("muPFIsoDepositNeutral"),
        pfPhotons        = cms.InputTag("muPFIsoDepositGamma")
  )


process.patMuons.isolationValues = cms.PSet(
            particle         = cms.InputTag("muPFIsoValueChargedAll04"),
            pfChargedHadrons = cms.InputTag("muPFIsoValueCharged04"),
            pfNeutralHadrons = cms.InputTag("muPFIsoValueNeutral04"),
            pfPhotons        = cms.InputTag("muPFIsoValueGamma04"),
#            user = cms.VInputTag(
#                         cms.InputTag("muPFIsoValuePU")
#           )

)

process.pfPileUp.PFCandidates = "particleFlow"
process.pfNoPileUp.bottomCollection = "particleFlow"
process.pfPileUpCandidates.bottomCollection = cms.InputTag("particleFlow")
#'''

process.myMuons = cms.EDFilter("PATMuonSelector",
    src = cms.InputTag("selectedPatMuonsTriggerMatch"),
    cut = cms.string('pt > 15. & abs(eta) < 2.4 ')
)

if  runOnMC:
    process.myMuons.src = cms.InputTag("selectedPatMuons")

process.dimuons = cms.EDProducer("CandViewShallowCloneCombiner",
    checkCharge = cms.bool(True),
    cut = cms.string('mass > 20 & charge = 0'),
    decay = cms.string('myMuons@+ myMuons@-')
)

process.dimuonsSelector  = cms.EDFilter("CandViewRefSelector",
    src = cms.InputTag("dimuons"),
    cut = cms.string('charge = 0 & mass > 20 & ( daughter(0).isGlobalMuon= 1 &  daughter(1).isGlobalMuon = 1 )   ')
)

process.dimuonsFilter = cms.EDFilter("CandViewCountFilter",
    src = cms.InputTag("dimuonsSelector"),
    minNumber = cms.uint32(minDiMuons)
)


'''
process.p = cms.Path(
               process.muonPrePFIsolationSequence
               + process.muonPFIsolationSequence
#               + process.diMuSeq

)
'''
#process.seq1 = cms.Sequence(process.muonPrePFIsolationSequence * process.muonPFIsolationSequence)



import HLTrigger.HLTfilters.triggerResultsFilter_cfi as hlt
process.hltJet = hlt.triggerResultsFilter.clone(
     triggerConditions = cms.vstring('HLT_DoubleJet15U_ForwardBackward* OR HLT_Jet15U* OR HLT_DiJetAve15U_*',),
     hltResults = cms.InputTag( "TriggerResults", "", "HLT" ),
     l1tResults = cms.InputTag(""),
     throw = cms.bool( False )
     )

if is2011Balance:
    process.hltJet.triggerConditions = cms.vstring('HLT_DiJetAve30_* OR  HLT_DiJetAve60_* OR HLT_Jet30_* OR HLT_Jet60_*')


#
if enableTur:
    process.initialSequence = cms.Sequence(process.initialCntr  
                        * process.hltJet
                        * process.kt6PFJets * process.kt6CaloJets * process.ak5PFJets * process.ak5CaloJets
                        * process.patPFCandidateIsoDepositSelection
                        * process.muonPrePFIsolationSequence
                        #* process.pfSortByTypeSequence
                        * process.muonPFIsolationSequence
                        * process.patDefaultSequence
                        * process.HBHENoiseFilterResultProducer
                        * process.HBHENoiseFilterResultProducer2
                        * process.noscraping * process.primaryVertexFilter)
else:
    process.initialSequence = cms.Sequence(process.initialCntr
                        * process.hltJet
                        * process.patDefaultSequence
                        * process.HBHENoiseFilterResultProducer
                        * process.HBHENoiseFilterResultProducer2
                        * process.noscraping * process.primaryVertexFilter)

if runOnMC or anaType == "ZMuMu":
    process.initialSequence.remove(process.hltJet)

process.tfMuons = cms.Sequence(process.initialSequence * process.myMuons * process.dimuons * process.dimuonsSelector*process.dimuonsFilter)
process.tfMuonsP = cms.Path( process.tfMuons)


process.pPF = cms.Path(     process.initialSequence
                          * process.selectedTFJets 
                          * process.countTFJets
                          * process.finalCntrPF    )


'''
process.pCalo = cms.Path (   process.initialSequence
                           * process.selectedTFCaloJets 
                           * process.countTFCaloJets
                           * process.finalCntrCalo )
'''



process.schedule = cms.Schedule()
if anaType == "JetTriggerEff":
    '''
    process.selectRawJetsPF = cms.EDFilter("PATGenericParticleSelector",
            src = cms.InputTag("ak5PFJets"),
            cut = cms.string("pt > 12"),
    )

    process.countRawJets = cms.EDFilter("PATCandViewCountFilter",
        maxNumber = cms.uint32(999999),
        src = cms.InputTag("selectRawJetsPF"),
        minNumber =cms.uint32(1)
    )
    process.rawJets = cms.Path(process.selectRawJetsPF*process.countRawJets)
    '''
    '''
    process.rawJetSelect = cms.EDFilter("PtMinPFJetSelector",
         src = cms.InputTag("ak5PFJets"),
         ptMin = cms.double(12.0)
    )
    process.rawJets = cms.Path(process.rawJetSelect)

    process.schedule.extend([process.rawJets])
    process.initialSequence.remove(process.hltJet)
    process.out.SelectEvents = cms.untracked.PSet(
            SelectEvents = cms.vstring('rawJets')
        )
    #process.initialSequence.replace(process.hltJet, process.selectRawJetsPF*process.countRawJets)
    '''
    #process.out.SelectEvents = cms.untracked.PSet(
    #        SelectEvents = cms.vstring('')
    #    )

    del process.out.SelectEvents
    process.initialSequence.remove(process.hltJet)
    #//iEvent.getByLabel( edm::InputTag("selectedPatJets"), patJets );
    #//iEvent.getByLabel( edm::InputTag("selectedPatJetsAK5Calo"), patJets );

    
    process.jetTrgEffPF =  cms.EDAnalyzer("TrgEfficiency",
            jetCol = cms.InputTag("selectedPatJets"),
            triggerSelection = cms.string("HLT_Jet15U*"),
            triggerConfiguration =  cms.PSet(
              hltResults = cms.InputTag('TriggerResults','','HLT'),
              l1tResults = cms.InputTag('gtDigis'),
              daqPartitions = cms.uint32(1),
              l1tIgnoreMask = cms.bool( False ),
              l1techIgnorePrescales = cms.bool( False ),
              throw  = cms.bool( False )
            )
    )
    process.jetTrgEffCalo = process.jetTrgEffPF.clone(jetCol = cms.InputTag("selectedPatJetsAK5Calo"))
    #process.tfMuons.replace(process.myMuons, process.myMuons*process.jetTrgEffPF * process.jetTrgEffCalo )
    #process.tfMuons.replace(process.myMuons, process.jetTrgEff)

# minimal set of unprescaled muon triggers
# HLT_Mu15_v1
# HLT_Mu11
# HLT_Mu9

process.schedule.extend([process.pPF])
#process.schedule.extend([process.pPF, process.pCalo])
#process.schedule = cms.Schedule(process.pCalo, process.outpath)
process.schedule.extend([process.tfMuonsP,])

'''
        //m_caloBase = iConfig.getParameter<edm::InputTag>("optionalCaloJets4ID");
        //m_caloBaseID = iConfig.getParameter<edm::InputTag>("optionalCaloID4ID");
        //iEvent.getByLabel(edm::InputTag("ak5CaloJets","","RECO"), hJets );
        //iEvent.getByLabel( "ak5JetID", hJetIDMap );
'''

#process.exampleTree = cms.EDAnalyzer("ExampleTreeProducer")
process.mnXS = cms.EDAnalyzer("MNXSTreeProducer", 
    minGenPT = cms.double(25),
    RawCaloJetsView = cms.PSet(
        src = cms.VInputTag(cms.InputTag("ak5CaloJets")),
        branchPrefix = cms.untracked.string("CaloRaw"),
    ),
    JetViewPF  = cms.PSet(
        storeageVersion = cms.untracked.int32(1),
        disableJetID = cms.bool(False),
        optionalCaloJets4ID = cms.InputTag("ak5CaloJets","","RECO"),
        optionalCaloID4ID  = cms.InputTag("ak5JetID"),
        branchPrefix = cms.untracked.string("PFAK5"),
        maxEta = cms.double(4.9999),
        minPt = cms.double(3),
        maxnum = cms.int32(3),
        input = cms.InputTag("selectedPatJets"),
        variations= cms.vstring("", "jecUp", "jecDown", "jerUp", "jerDown"),
        jerFactors = cms.vstring(  # PF10
                "1.1 1.066 0.007 0.07 0.072",
                "1.7 1.191 0.019 0.06 0.062",
                "2.3 1.096 0.030 0.08 0.085",
                "5.0 1.166 0.050 0.19 0.199"),
    ),

    JetViewCalo  = cms.PSet(
        storeageVersion = cms.untracked.int32(1),
        disableJetID = cms.bool(False),
        optionalCaloJets4ID = cms.InputTag("ak5CaloJets","","RECO"),
        optionalCaloID4ID = cms.InputTag("ak5JetID"),
        branchPrefix = cms.untracked.string("Calo"),
        maxEta = cms.double(4.9999),
        minPt = cms.double(3),
        maxnum = cms.int32(3),
        input = cms.InputTag("selectedPatJetsAK5Calo"),
        variations= cms.vstring("", "jecUp", "jecDown", "jerUp", "jerDown"),
        jerFactors = cms.vstring(  # Calo10
            "1.1 1.088 0.007 0.07 0.075",
            "1.7 1.139 0.019 0.08 0.084",
            "2.3 1.082 0.030 0.14 0.139",
            "5.0 1.065 0.042 0.23 0.235"
        ),
    ),

    TriggerResultsView =  cms.PSet(
        branchPrefix = cms.untracked.string("trg"),
        process = cms.string("HLT"), # usually HLT
        triggers = cms.vstring("dj15fb", "djave15", "jet15"),
        dj15fb =  cms.vstring("HLT_DoubleJet15U_ForwardBackward*"),
        djave15 =  cms.vstring("HLT_DiJetAve15U*"), 
        jet15 =  cms.vstring("HLT_Jet15U*"), 
    ),

)
'''
        calo.append("1.1 1.088 0.007 0.07 0.075")
        calo.append("1.7 1.139 0.019 0.08 0.084")
        calo.append("2.3 1.082 0.030 0.14 0.139")
        calo.append("5.0 1.065 0.042 0.23 0.235")

        pf = []
        pf.append("1.1 1.066 0.007 0.07 0.072")
        pf.append("1.7 1.191 0.019 0.06 0.062")
        pf.append("2.3 1.096 0.030 0.08 0.085")
        pf.append("5.0 1.166 0.050 0.19 0.199")  #ORG!

        #print "XXXX wrong JER"*50
        #pf.append("2.8 1.166 0.050 0.19 0.199") # keep org till 2.8
        #pf.append("5.0 1.288 0.127 0.155 0.153") # use factors from 2011

        pf11 = []
        pf11.append("0.5 1.052 0.012 0.062 0.061")
        pf11.append("1.1 1.057 0.012 0.056 0.055")
        pf11.append("1.7 1.096 0.017 0.063 0.062")
        pf11.append("2.3 1.134 0.035 0.087 0.085")
        pf11.append("5.0 1.288 0.127 0.155 0.153")
'''


process.infoHisto = cms.EDAnalyzer("SaveCountHistoInTreeFile")
#process.initialSequence.remove(process.hltJet)
#process.pTreeProducers = cms.Path(process.initialSequence*process.infoHisto*process.exampleTree*process.mnXS)
process.pTreeProducers = cms.Path(process.initialSequence*process.infoHisto*process.mnXS)
process.pUtil = cms.Path(process.XS)
process.schedule.append(process.pUtil)
process.schedule.append(process.pTreeProducers)

if anaType != "JetTriggerEff":
    process.schedule.extend([process.outpath,]) #xxx
else:
    del process.outpath


if anaType == "ZMuMu":
    process.out.SelectEvents = cms.untracked.PSet(
            SelectEvents = cms.vstring("tfMuonsP")
        )
elif anaType == "DiJet" or anaType == "DiJetBalance":
    process.out.SelectEvents = cms.untracked.PSet(
        #    SelectEvents = cms.vstring('pPF', 'pCalo')
            SelectEvents = cms.vstring('pPF')
        )



#removeCleaning(process)





restrictInputToAOD(process) 
if not runOnMC:
    runOnData(process)      # Warning - this changes JEC levels!!!
    #process.patJetCorrFactors.levels = JEClevels
    #process.patJetCorrFactorsAK5Calo.levels =  JEClevelsCalo
    removeMCMatching(process, ['All'])  
    remove = [process.patJetPartonMatchAK5Calo, process.patJetGenJetMatchAK5Calo]
    remove.extend([process.patJetPartons, process.patJetPartonAssociation, process.patJetPartonAssociationAK5Calo])
    remove.extend([process.patJetFlavourAssociation,process.patJetFlavourAssociationAK5Calo])
    for rem in remove:
        process.patDefaultSequence.remove(rem)
    process.patJetsAK5Calo.embedGenPartonMatch = cms.bool(False)
    process.patJetsAK5Calo.addGenJetMatch = cms.bool(False)   
    process.patJetsAK5Calo.getJetMCFlavour = cms.bool(False)  
                                                              
    process.patJets.embedGenPartonMatch = cms.bool(False)     
    process.patJets.addGenJetMatch = cms.bool(False)          
    process.patJets.getJetMCFlavour = cms.bool(False) 





keepProds = cms.untracked.vstring("drop *", 
                                "keep l1extraL1JetParticles_l1extraParticles_Central_RECO",
                                "keep l1extraL1JetParticles_l1extraParticles_Forward_RECO",
                                "keep *_dimuons_*_*",
                                "keep *_myMuons_*_*",
                                "keep *_addPileupInfo_*_*",
                                "keep *_initialCntr_*_*",
                                "keep *_finalCntrPF_*_*",
                                "keep *_finalCntrCalo_*_*",
                                "keep *_offlinePrimaryVertices_*_*",
                                "keep GenEventInfoProduct_generator__*",
                                "keep recoGenJets_selectedPatJets_genJets_PAT",
                                "keep recoGenJets_selectedPatJetsAK5Calo_genJets_PAT",
                                "keep recoGenJets_ak5GenJets__*",
                                "keep PileupSummaryInfos_addPileupInfo__*",
                                "keep recoGenJets_ak5GenJets__*",
                                'keep patTriggerObjects_patTrigger_*_PAT', 
                                'keep patTriggerFilters_patTrigger_*_PAT', 
                                'keep patTriggerPaths_patTrigger_*_PAT', 
                                'keep patTriggerEvent_patTriggerEvent_*_PAT', 
                                #"keep *_selectedTFJets_*_*",
                                #"keep *_selectedTFCaloJets_*_*",
                                "keep *_selectedPatJets_tagInfos_PAT",
                                "keep *_selectedPatJets_caloTowers_PAT",
                                "keep *_selectedPatJets_pfCandidates_PAT",
                                "keep recoTracks_generalTracks__RECO", # for vtx
                                "keep *_selectedPatJets__PAT",
                                "keep *_selectedPatJetsAK5Calo_tagInfos_PAT",
                                "keep *_selectedPatJetsAK5Calo_caloTowers_PAT",
                                "keep *_selectedPatJetsAK5Calo__PAT",
                                "keep recoGenParticles_genParticles__*",
                                "keep double_kt6PFJets_rho_PAT",
                                "keep double_kt6CaloJets_rho_PAT",
                                #"keep recoPFCandidates_particleFlow__RECO",
                                #"keep double_kt6PFJetsTur_rho_PAT",
                                #"keep double_kt6CaloJetsTur_rho_PAT",
                                #"keep recoPFJets_ak5PFJetsTur__PAT",
                                #"keep recoPFJets_ak5PFJets__PAT",
                                "keep HcalNoiseSummary_hcalnoise__*",
                                #"keep *"
                                )
                                


#keepProds = cms.untracked.vstring("keep *")
#print process.out.outputCommands

process.out.outputCommands = keepProds

keepProdsTrgEffStudy = cms.untracked.vstring("drop *",
    "keep HcalNoiseSummary_hcalnoise__*",
    "keep *_myMuons_*_*",
    "keep double_kt6PFJets_rho_PAT",
    "keep *_ak5PFJets__PAT",
    'keep patTriggerObjects_patTrigger_*_PAT',
    'keep patTriggerFilters_patTrigger_*_PAT',
    'keep patTriggerPaths_patTrigger_*_PAT', 
    'keep patTriggerEvent_patTriggerEvent_*_PAT',
)
#    process.out.outputCommands = keepProdsTrgEffStudy



'''
print "Warning! My json !!!" * 50
import FWCore.ParameterSet.Config as cms
import PhysicsTools.PythonAnalysis.LumiList as LumiList
json = "../lumi/Cert_136033-149442_7TeV_Apr21ReReco_Collisions10_JSON.txt"
myLumis = LumiList.LumiList(filename = json).getCMSSWString().split(',')
process.source.lumisToProcess = cms.untracked.VLuminosityBlockRange()
process.source.lumisToProcess.extend(myLumis)
#'''

process.patJetCorrFactorsAK5Calo.rho = cms.InputTag("kt6PFJets","rho")
process.patJetCorrFactorsAK5Calo.useNPV = cms.bool(False)


# please note, that this should be performed at the very end:
'''
process.patJetsAK5CaloORG = process.patJetsAK5Calo.clone()
process.patJetsAK5Calo = cms.EDProducer("JetUserValProducer", 
            jetCol = cms.InputTag("patJetsAK5CaloORG"))
process.patDefaultSequence.replace(process.patJetsAK5Calo, process.patJetsAK5CaloORG*process.patJetsAK5Calo)


process.patJetsORG = process.patJets.clone()
process.patJets = cms.EDProducer("JetUserValProducer", 
            jetCol = cms.InputTag("patJetsORG"))
process.patDefaultSequence.replace(process.patJets, process.patJetsORG*process.patJets)
'''


if anaType == "JetTriggerEff":
    del process.out


#'''

#ver = "V17TFFull"
#ver = "V17TFPart"
#ver = "V16TFFull"
ver = "V16TFPart"
#ver = "V16TFPartV2"

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
# '''


process.schedule.remove(process.outpath)
del process.outpath
del process.out


