import FWCore.ParameterSet.Config as cms

def get(todo):
    defs = {}

    # CaloTowerView
    defs["CaloTowerView"]  = cms.PSet(
        miniView = cms.string("CaloTowerView"),
        branchPrefix = cms.untracked.string("CaloTowers"),
        inputcoll = cms.InputTag("towerMaker")
    )

 
    # main function
    ret = {}
    for t in todo:
        if t not in defs:
            raise Exception("miniView def not known "+t)

        ret[t] = defs[t]
    return ret


