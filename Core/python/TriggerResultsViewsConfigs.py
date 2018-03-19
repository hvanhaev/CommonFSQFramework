import FWCore.ParameterSet.Config as cms

def get(todo):
    defs = {}

    # ZeroBias trigger configuration
    defs["ZeroBiasTriggerResultsView"]  = cms.PSet(
        miniView = cms.string("TriggerResultsView"),
        branchPrefix = cms.untracked.string("trg"),
        process = cms.string("HLT"),
        storePrescales = cms.bool(False),
        triggers = cms.vstring("ZeroBias"),
        ZeroBias = cms.vstring("HLT_ZeroBias_part*")
    )

    defs["ZeroBiasTriggerResultsViewWithPS"]  = cms.PSet(
        miniView = cms.string("TriggerResultsView"),
        branchPrefix = cms.untracked.string("trg"),
        process = cms.string("HLT"),
        storePrescales = cms.bool(True),
        triggers = cms.vstring("ZeroBias"),
        ZeroBias = cms.vstring("HLT_ZeroBias_part0_v1","HLT_ZeroBias_part1_v1","HLT_ZeroBias_part2_v1","HLT_ZeroBias_part3_v1","HLT_ZeroBias_part4_v1","HLT_ZeroBias_part5_v1","HLT_ZeroBias_part6_v1","HLT_ZeroBias_part7_v1")
    )

    defs["ZeroBiasWithPSRun2015D"]  = cms.PSet(
        miniView = cms.string("TriggerResultsView"),
        branchPrefix = cms.untracked.string("trg"),
        process = cms.string("HLT"),
        storePrescales = cms.bool(True),
        triggers = cms.vstring("ZeroBias"),
        ZeroBias = cms.vstring("HLT_ZeroBias_v1")
    )

    defs["ZeroBiasWithPSRun2015E"]  = cms.PSet(
        miniView = cms.string("TriggerResultsView"),
        branchPrefix = cms.untracked.string("trg"),
        process = cms.string("HLT"),
        storePrescales = cms.bool(True),
        triggers = cms.vstring("ZeroBias","Random"),
        ZeroBias = cms.vstring("HLT_ZeroBias_v2"),
        Random = cms.vstring("HLT_Random_v1")
    )
    
    defs["TriggersRun2016H"]  = cms.PSet(
        miniView = cms.string("TriggerResultsView"),
        branchPrefix = cms.untracked.string("trg"),
        process = cms.string("HLT"),
        storePrescales = cms.bool(True),
        triggers = cms.vstring("AK4PFJet30","DiPFJet15","DiPFJet25","PFJet15","PFJet25","L1MinimumBiasHFOR0","L1MinimumBiasHFOR1","L1MinimumBiasHFOR2","L1MinimumBiasHFOR3","L1MinimumBiasHFOR4","L1MinimumBiasHFOR5","L1MinimumBiasHFOR6","L1MinimumBiasHFOR7","L1MinimumBiasHFOR8","L1MinimumBiasHFOR9"),
        AK4PFJet30 = cms.vstring("HLT_AK4PFJet30_v7"),
        DiPFJet15 = cms.vstring("HLT_DiPFJet15_NoCaloMatched_v5"),
        DiPFJet25 = cms.vstring("HLT_DiPFJet25_NoCaloMatched_v5"),
        PFJet15 = cms.vstring("HLT_PFJet15_NoCaloMatched_v7"),
        PFJet25 = cms.vstring("HLT_PFJet25_NoCaloMatched_v5"),
        L1MinimumBiasHFOR0 = cms.vstring("HLT_L1MinimumBiasHF_OR_part0_v2"), 
        L1MinimumBiasHFOR1 = cms.vstring("HLT_L1MinimumBiasHF_OR_part1_v2"),
        L1MinimumBiasHFOR2 = cms.vstring("HLT_L1MinimumBiasHF_OR_part2_v2"),
        L1MinimumBiasHFOR3 = cms.vstring("HLT_L1MinimumBiasHF_OR_part3_v2"),
        L1MinimumBiasHFOR4 = cms.vstring("HLT_L1MinimumBiasHF_OR_part4_v2"),
        L1MinimumBiasHFOR5 = cms.vstring("HLT_L1MinimumBiasHF_OR_part5_v2"),
        L1MinimumBiasHFOR6 = cms.vstring("HLT_L1MinimumBiasHF_OR_part6_v2"),
        L1MinimumBiasHFOR7 = cms.vstring("HLT_L1MinimumBiasHF_OR_part7_v2"),
        L1MinimumBiasHFOR8 = cms.vstring("HLT_L1MinimumBiasHF_OR_part8_v2"),
        L1MinimumBiasHFOR9 = cms.vstring("HLT_L1MinimumBiasHF_OR_part9_v2")
    )
    
    defs["TriggersRun2016B"]  = cms.PSet(
        miniView = cms.string("TriggerResultsView"),
        branchPrefix = cms.untracked.string("trg"),
        process = cms.string("HLT"),
        storePrescales = cms.bool(True),
        triggers = cms.vstring("DiPFJet15","DiPFJet25","DiPFJetAve40","DiPFJetAve60","DiPFJetAve80","PFJet15","PFJet25","L1MinimumBiasHFOR0","L1MinimumBiasHFOR1","L1MinimumBiasHFOR2","L1MinimumBiasHFOR3","L1MinimumBiasHFOR4","L1MinimumBiasHFOR5","L1MinimumBiasHFOR6","L1MinimumBiasHFOR7","L1MinimumBiasHFOR8","L1MinimumBiasHFOR9","DiPFJetAve15F","DiPFJetAve25F","DiPFJetAve35F","DiPFJetAve60F","DiPFJetAve80F","DiPFJetAve100F"),
        DiPFJet15 = cms.vstring("HLT_DiPFJet15_NoCaloMatched_v1"),
        DiPFJet25 = cms.vstring("HLT_DiPFJet25_NoCaloMatched_v1"),
        DiPFJetAve40 = cms.vstring("HLT_DiPFJetAve40_v2"),
        DiPFJetAve60 = cms.vstring("HLT_DiPFJetAve60_v2"),
        DiPFJetAve80 = cms.vstring("HLT_DiPFJetAve80_v2"),
        PFJet15 = cms.vstring("HLT_PFJet15_NoCaloMatched_v3"),
        PFJet25 = cms.vstring("HLT_PFJet25_NoCaloMatched_v1"),
        L1MinimumBiasHFOR0 = cms.vstring("HLT_L1MinimumBiasHF_OR_part0_v1"), 
        L1MinimumBiasHFOR1 = cms.vstring("HLT_L1MinimumBiasHF_OR_part1_v1"),
        L1MinimumBiasHFOR2 = cms.vstring("HLT_L1MinimumBiasHF_OR_part2_v1"),
        L1MinimumBiasHFOR3 = cms.vstring("HLT_L1MinimumBiasHF_OR_part3_v1"),
        L1MinimumBiasHFOR4 = cms.vstring("HLT_L1MinimumBiasHF_OR_part4_v1"),
        L1MinimumBiasHFOR5 = cms.vstring("HLT_L1MinimumBiasHF_OR_part5_v1"),
        L1MinimumBiasHFOR6 = cms.vstring("HLT_L1MinimumBiasHF_OR_part6_v1"),
        L1MinimumBiasHFOR7 = cms.vstring("HLT_L1MinimumBiasHF_OR_part7_v1"),
        L1MinimumBiasHFOR8 = cms.vstring("HLT_L1MinimumBiasHF_OR_part8_v1"),
        L1MinimumBiasHFOR9 = cms.vstring("HLT_L1MinimumBiasHF_OR_part9_v1"),
        DiPFJetAve15F = cms.vstring("HLT_DiPFJetAve15_HFJEC_v1"),
        DiPFJetAve25F = cms.vstring("HLT_DiPFJetAve25_HFJEC_v1"),
        DiPFJetAve35F = cms.vstring("HLT_DiPFJetAve35_HFJEC_v1"),
        DiPFJetAve60F = cms.vstring("HLT_DiPFJetAve60_HFJEC_v3"),
        DiPFJetAve80F = cms.vstring("HLT_DiPFJetAve80_HFJEC_v3"),
        DiPFJetAve100F = cms.vstring("HLT_DiPFJetAve100_HFJEC_v3")     
    )
    

    # L1 trigger configuration - please do not edit this
    defs["L1GTriggerResultsView"] = cms.PSet(
        miniView = cms.string("TriggerResultsView"),
        branchPrefix = cms.untracked.string("trgl1"),
        process = cms.string("HLT"),
        storePrescales = cms.bool(True),
        triggers = cms.vstring("L1GTTech","L1GTAlgo")
    )






    defs["AK4CaloJetTriggerResultsView"]  = cms.PSet(
       miniView = cms.string("TriggerResultsView"),
       branchPrefix = cms.untracked.string("trgAK4Calo"),
       process = cms.string("HLT"),
       storePrescales = cms.bool(False),
       triggers = cms.vstring("Jet30","Jet40","Jet50"),
       Jet30 = cms.vstring("HLT_AK4CaloJet30ForEndOfFill_v1"),
       Jet40 = cms.vstring("HLT_AK4CaloJet40ForEndOfFill_v1"),
       Jet50 = cms.vstring("HLT_AK4CaloJet50ForEndOfFill_v1")
    )

    defs["AK4CaloJetTriggerResultsViewWithPS"]  = cms.PSet(
       miniView = cms.string("TriggerResultsView"),
       branchPrefix = cms.untracked.string("trgAK4Calo"),
       process = cms.string("HLT"),
       storePrescales = cms.bool(True),
       triggers = cms.vstring("Jet30","Jet40","Jet50"),
       Jet30 = cms.vstring("HLT_AK4CaloJet30ForEndOfFill_v1"),
       Jet40 = cms.vstring("HLT_AK4CaloJet40ForEndOfFill_v1"),
       Jet50 = cms.vstring("HLT_AK4CaloJet50ForEndOfFill_v1")
    )

    defs["FullTrackTriggerResultsView"]  = cms.PSet(
       miniView = cms.string("TriggerResultsView"),
       branchPrefix = cms.untracked.string("trgTracks"),
       process = cms.string("HLT"),
       storePrescales = cms.bool(False),
       triggers = cms.vstring("FullTrack12"),
       FullTrack12 = cms.vstring("HLT_FullTrack12ForEndOfFill_v1")
    )

    defs["FullTrackTriggerResultsViewWithPS"]  = cms.PSet(
       miniView = cms.string("TriggerResultsView"),
       branchPrefix = cms.untracked.string("trgTracks"),
       process = cms.string("HLT"),
       storePrescales = cms.bool(True),
       triggers = cms.vstring("FullTrack12"),
       FullTrack12 = cms.vstring("HLT_FullTrack12ForEndOfFill_v1")
    )

    defs["CastorSpecialJetTriggerResultsView"]  = cms.PSet(
        miniView = cms.string("TriggerResultsView"),
        branchPrefix = cms.untracked.string("CasTrg"),
        process = cms.string("HLT"),
        storePrescales = cms.bool(False),
        triggers = cms.vstring("ZeroBias","MinBias","Random","CastorMedJet","CastorHighJet","CastorDiJet"),
        ZeroBias = cms.vstring("HLT_ZeroBias*"),
        MinBias = cms.vstring("HLT_L1MinimumBias*"),
        Random = cms.vstring("HLT_Random*"),
        CastorMedJet = cms.vstring("HLT_L1CastorMediumJet_v*"),
        CastorHighJet = cms.vstring("HLT_L1CastorHighJet_v*"),
        CastorDiJet = cms.vstring("HLT_L1CastorMediumJet_PFJet15_v*")
    )

 
    # main function
    ret = {}
    for t in todo:
        if t not in defs:
            raise Exception("miniView def not known "+t)

        ret[t] = defs[t]
    return ret


