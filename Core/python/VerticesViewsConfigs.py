import FWCore.ParameterSet.Config as cms

def get(todo):
    defs = {}

    # VerticesView
    defs["VerticesView"]  = cms.PSet(
        miniView = cms.string("VerticesView"),
        branchPrefix = cms.untracked.string("vtx"),
        src  = cms.InputTag("offlinePrimaryVertices")
    )

    # ZeroTesla VerticesView
    defs["ZeroTeslaVertexView_Pixel_PreSplitting"]  = cms.PSet(
        miniView = cms.string("ZeroTeslaVertexView"),
        branchPrefix = cms.untracked.string("ZeroTeslaPixelPreSplittingVtx"),
        usePixel = cms.bool(True),
        src = cms.InputTag("siPixelRecHitsPreSplitting"),
    )

    defs["ZeroTeslaVertexView_Pixel_noPreSplitting"]  = cms.PSet(
        miniView = cms.string("ZeroTeslaVertexView"),
        branchPrefix = cms.untracked.string("ZeroTeslaPixelnoPreSplittingVtx"),
        usePixel = cms.bool(True),
        src = cms.InputTag("siPixelRecHits"),
    )

    defs["ZeroTeslaVertexView_Strips"]  = cms.PSet(
        miniView = cms.string("ZeroTeslaVertexView"),
        branchPrefix = cms.untracked.string("ZeroTeslaStripVtx"),
        usePixel = cms.bool(False),
        src = cms.InputTag(""),
    )

 
    # main function
    ret = {}
    for t in todo:
        if t not in defs:
            raise Exception("miniView def not known "+t)

        ret[t] = defs[t]
    return ret


