import FWCore.ParameterSet.Config as cms

def get(todo):
    defs = {}

    # ZeroBias trigger configuration
    defs["ZeroBiasTriggerResultsView"]  = cms.PSet(
        miniView = cms.string("TriggerResultsView"),
        branchPrefix = cms.untracked.string("trg"),
        process = cms.string("HLT"),
        triggers = cms.vstring("ZeroBias"),
        ZeroBias = cms.vstring("HLT_ZeroBias_part*")
    )

    defs["L1GTriggerResultsView"] = cms.PSet(
        miniView = cms.string("TriggerResultsView"),
        branchPrefix = cms.untracked.string("trgl1"),
        process = cms.string("HLT"),
        triggers = cms.vstring("L1GTTech","L1GTAlgo")
    )
 
    # main function
    ret = {}
    for t in todo:
        if t not in defs:
            raise Exception("miniView def not known "+t)

        ret[t] = defs[t]
    return ret


