import FWCore.ParameterSet.Config as cms

def get(todo):
    defs = {}

    # VerticesView
    defs["VerticesView"]  = cms.PSet(
        miniView = cms.string("VerticesView"),
        branchPrefix = cms.untracked.string("vtx"),
        src  = cms.InputTag("offlinePrimaryVertices")
    )

 
    # main function
    ret = {}
    for t in todo:
        if t not in defs:
            raise Exception("miniView def not known "+t)

        ret[t] = defs[t]
    return ret


