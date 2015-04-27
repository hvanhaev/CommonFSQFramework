import FWCore.ParameterSet.Config as cms

def get(todo):
    defs = {}

    # GenParticles
    defs["GenPartView"]  = cms.PSet(
        miniView = cms.string("GenPartView"),
        branchPrefix = cms.untracked.string("genParticles"),
        # maxEta = -1: no eta cut; maxEta > 0: eta cut
        maxEta = cms.double(-1),
        minPt = cms.double(0.0),
	#charge parameter: -1(save all)/0(save neutrals)/1(save charged)
        charge = cms.int32(-1),
        genParticles = cms.InputTag("genParticles"),
        
    )

    # GenJets
    defs["ak4GenJetView"]= cms.PSet(
        miniView = cms.string("GenJetView"),
        branchPrefix = cms.untracked.string("ak4GenJets"),
        maxEta = cms.double(7.0),
        minPt = cms.double(1.0),
        genJets = cms.InputTag("ak4GenJets"),
    )

    defs["ak5GenJetView"]= cms.PSet(   
        miniView = cms.string("GenJetView"),
        branchPrefix = cms.untracked.string("ak5GenJets"),
        maxEta = cms.double(7.0),
        minPt = cms.double(1.0),
        genJets = cms.InputTag("ak5GenJets"),
    )

    # Charged GenJets for UE
    defs["ak4ChgGenJetView"]= cms.PSet(
        miniView = cms.string("GenJetView"),
        branchPrefix = cms.untracked.string("ak4ChgGenJets"),
        maxEta = cms.double(3.0),
        minPt = cms.double(0.3),
        genJets = cms.InputTag("ak4ChgGenJets"),
    )

    defs["ak5ChgGenJetView"]= cms.PSet(
        miniView = cms.string("GenJetView"),
        branchPrefix = cms.untracked.string("ak5ChgGenJets"),
        maxEta = cms.double(3.0),
        minPt = cms.double(0.3),
        genJets = cms.InputTag("ak5ChgGenJets"),
    )

    # main function
    ret = {}
    for t in todo:
        if t not in defs:
            raise Exception("miniView def not known "+t)

        ret[t] = defs[t]
    return ret


