import FWCore.ParameterSet.Config as cms

def get(todo):
    defs = {}

    # RecoTrackView
    defs["RecoTrackView"]  = cms.PSet(
        miniView = cms.string("RecoTrackView"),
        branchPrefix = cms.untracked.string("recoTracks"),
        maxEta = cms.double(5.),
        maxDZ  = cms.double(999),
        minPt = cms.double(-1),
        tracks = cms.InputTag("generalTracks")
    )

 
    # main function
    ret = {}
    for t in todo:
        if t not in defs:
            raise Exception("miniView def not known "+t)

        ret[t] = defs[t]
    return ret


