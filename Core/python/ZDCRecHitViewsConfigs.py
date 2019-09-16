import FWCore.ParameterSet.Config as cms

def get(todo):
    defs = {}

    # ZDCRecHits
    defs["ZDCRecHitView"]  = cms.PSet(
        miniView = cms.string("ZDCRecHitView"),
        branchPrefix = cms.untracked.string("ZDCRecHit"),
    )

    # main function
    ret = {}
    for t in todo:
        if t not in defs:
            raise Exception("miniView def not known "+t)

        ret[t] = defs[t]
    return ret


