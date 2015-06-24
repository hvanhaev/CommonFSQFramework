import FWCore.ParameterSet.Config as cms

def get(todo):
    defs = {}

    # HFRecHits
    defs["HFRecHitView"]  = cms.PSet(
        miniView = cms.string("HFRecHitView"),
        branchPrefix = cms.untracked.string("HFRecHit"),
    )

    # HBHERecHits 
    defs["HBHERecHitView"]  = cms.PSet(
        miniView = cms.string("HBHERecHitView"),
        branchPrefix = cms.untracked.string("HBHERecHit"),
    )

   # EcalRecHits
    defs["EcalRecHitView"]  = cms.PSet(
        miniView = cms.string("EcalRecHitView"),
        branchPrefix = cms.untracked.string("EcalRecHit"),
    )
 
    # main function
    ret = {}
    for t in todo:
        if t not in defs:
            raise Exception("miniView def not known "+t)

        ret[t] = defs[t]
    return ret


