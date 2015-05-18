import FWCore.ParameterSet.Config as cms

def get(todo):
    defs = {}

    # EnergyFlow
    defs["HFRecHitView"]  = cms.PSet(
        miniView = cms.string("HFRecHitView"),
        branchPrefix = cms.untracked.string("HFRecHit"),
    )

 
    # main function
    ret = {}
    for t in todo:
        if t not in defs:
            raise Exception("miniView def not known "+t)

        ret[t] = defs[t]
    return ret


