import FWCore.ParameterSet.Config as cms

def get(todo):
    defs = {}
    
    defs["CastorDigiView"] = cms.PSet(
        miniView = cms.string("CastorDigiView"),
        branchPrefix = cms.untracked.string("CastorDigi"),
        firstTS = cms.int32(0),
        lastTS = cms.int32(9),
        inputcoll = cms.InputTag('castorDigis')
    )

    
    ret = {}
    for t in todo:
        if t not in defs:
            raise Exception("miniView def not known "+t)
        ret[t] = defs[t]
    return ret
