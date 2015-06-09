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

 
    # main function
    ret = {}
    for t in todo:
        if t not in defs:
            raise Exception("miniView def not known "+t)

        ret[t] = defs[t]
    return ret


