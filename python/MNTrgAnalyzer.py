import FWCore.ParameterSet.Config as cms
import MNTriggerStudies.MNTriggerAna.customizePAT

def addTreeProducer(process, **kwargs):
    stage1extralabel = "hltL1extraParticles"
    if "stage1extralabel" in kwargs:
        stage1extralabel = kwargs["stage1extralabel"]

    triggerResults = "HLT"

    if "triggerResults" in kwargs:
       triggerResults = kwargs["triggerResults"]

    disable = []
    if "disable" in kwargs:
        disable = kwargs["disable"]

    process.MNTriggerAnaNew = cms.EDAnalyzer("MNTriggerAnaNew",
        JetViewPFAK4CHS  = cms.PSet(
            disableJetID = cms.bool(True),
            optionalCaloJets4ID = cms.InputTag("ak5CaloJets","","RECO"),
            optionalCaloID4ID  = cms.InputTag("ak5JetID"),
            branchPrefix = cms.untracked.string("PFAK4CHS"),
            maxEta = cms.double(5.2),
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
            maxEta = cms.double(5.2),
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
            branchPrefix = cms.untracked.string("PFAK5"),
            maxEta = cms.double(5.2),
            minPt = cms.double(3),
            maxnum = cms.int32(3),
            #input = cms.InputTag("selectedPatJets"),
            input = cms.InputTag("patJetsAK5PF"),
            variations= cms.vstring("", "jecUp", "jecDown"),
            jerFactors = cms.vstring(  # PF10
                    "5.5 1 0.007 0.07 0.072"),
        ),


        JetViewCalo  = cms.PSet(
            disableJetID = cms.bool(True),
            optionalCaloJets4ID = cms.InputTag("ak5CaloJets","","RECO"),
            optionalCaloID4ID  = cms.InputTag("ak5JetID"),
            branchPrefix = cms.untracked.string("Calo"),
            maxEta = cms.double(5.2),
            minPt = cms.double(3),
            maxnum = cms.int32(3),
            input = cms.InputTag("selectedPatJets"),
            variations= cms.vstring("", "jecUp", "jecDown"),
            jerFactors = cms.vstring(  # PF10
                    "5.5 1 0.007 0.07 0.072"),
        ),

        L1JetsViewStage1  = cms.PSet(
            branchPrefix = cms.untracked.string("stage1"),
            src =  cms.VInputTag(cms.InputTag(stage1extralabel,"Central"),
                    cms.InputTag(stage1extralabel,"Forward")
            ),
        ),


        L1JetsView  = cms.PSet(
            branchPrefix = cms.untracked.string("old"),
            src =  cms.VInputTag(cms.InputTag("l1extraParticles","Central"),
                    cms.InputTag("l1extraParticles","Forward"),
                    cms.InputTag("l1extraParticles","Tau")
            ),
        ),


        TriggerResultsView =  cms.PSet(
            branchPrefix = cms.untracked.string("trg"),
            process = cms.string(triggerResults), # usually HLT
            #triggers = cms.vstring("HLT_DiPFJetAve60_CentralForward_v1", "HLT_DiPFJetAve60_CentralForward*", "viaClass"),
            #triggers = cms.vstring("ptAve60CenFwd", "ptAve80CenFwd", "diPFJet20CntrFwdEta3", "diPFJet20rFwdBckwEta2", \
            #                       "diPFJet20rFwdBckwEta3", "FwdPFJet20Eta2", "FwdPFJet20Eta3", "PFJet20"),
            triggers = cms.vstring(),
            #triggers = cms.vstring("ptAve60CenFwd"),
            #triggers = cms.vstring("ptAve60CenFwd", "ptAve80CenFwd", "ptAve100CenFwd","ptAve160CenFwd",  "newAve60", "newAve80"),
            ptAve60CenFwd = cms.vstring("HLT_DiPFJetAve60_HFJEC"),
            ptAve80CenFwd = cms.vstring("HLT_DiPFJetAve80_CentralForward_v1"),
            ptAve100CenFwd = cms.vstring("HLT_DiPFJetAve100_CentralForward_v1"),
            ptAve160CenFwd = cms.vstring("HLT_DiPFJetAve160_CentralForward_v1"),
            diPFJet20CntrFwdEta3 = cms.vstring("HLT_DiPFJet20_CntrFwdEta3_v1"),
            diPFJet20rFwdBckwEta2 = cms.vstring("HLT_DiPFJet20_FwdBckwEta2_v1"),
            diPFJet20rFwdBckwEta3 = cms.vstring("HLT_DiPFJet20_FwdBckwEta3_v1"),
            FwdPFJet20Eta2 = cms.vstring("HLT_FwdPFJet20_Eta2_v1"),
            FwdPFJet20Eta3 = cms.vstring("HLT_FwdPFJet20_Eta3_v1"),
            PFJet20 = cms.vstring("HLT_PFJet20_v1"),
            newAve60 = cms.vstring("HLT_newAve60_v1"),
            newAve80 = cms.vstring("HLT_newAve80_v1")
        ),
    )
    if "hlt" in disable:
        del process.MNTriggerAnaNew.TriggerResultsView

    if "l1" in disable:
        del process.MNTriggerAnaNew.L1JetsView
        del process.MNTriggerAnaNew.L1JetsViewStage1


    process = MNTriggerStudies.MNTriggerAna.customizePAT.addTreeProducer(process, process.MNTriggerAnaNew)
    return process
