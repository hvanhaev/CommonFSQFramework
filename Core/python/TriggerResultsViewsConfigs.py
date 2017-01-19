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

    # L1 trigger configuration - please do not edit this
    defs["L1GTriggerResultsView"] = cms.PSet(
        miniView = cms.string("TriggerResultsView"),
        branchPrefix = cms.untracked.string("trgl1"),
        process = cms.string("HLT"),
        storePrescales = cms.bool(False),
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


