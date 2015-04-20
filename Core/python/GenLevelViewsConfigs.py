import FWCore.ParameterSet.Config as cms

def get(todo):
    defs = {}
    defs["GenPartView"]  = cms.PSet(
        miniView = cms.string("GenPartView"),
        branchPrefix = cms.untracked.string("genParticles"),
        maxEta = cms.double(7.0),
        minPt = cms.double(0.2),
	#charge parameter: -1(save all)/0(save neutrals)/1(save charged)
        charge = cms.int32(-1),
        genParticles = cms.InputTag("genParticles"),
        
    )
    # and so on
    # defs["JetViewAK4Calo"]= cmsPSet(...

    ret = {}
    for t in todo:
        if t not in defs:
            raise Exception("miniView def not known "+t)

        ret[t] = defs[t]
    return ret


