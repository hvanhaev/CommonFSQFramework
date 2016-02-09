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

    # default GenJets
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

    defs["lowPtak5GenJetView"]= cms.PSet(   
        miniView = cms.string("GenJetView"),
        branchPrefix = cms.untracked.string("ak5GenJets"),
        maxEta = cms.double(7.0),
        minPt = cms.double(1.0),
        genJets = cms.InputTag("lowPtak5GenJets"),
    )

    # Charged GenJets for UE
    defs["ak4ChgGenJetView"]= cms.PSet(
        miniView = cms.string("GenJetView"),
        branchPrefix = cms.untracked.string("ak4ChgGenJets"),
        maxEta = cms.double(3.0),
        minPt = cms.double(1.0),
        genJets = cms.InputTag("ak4ChgGenJets"),
    )

    defs["ak5ChgGenJetView"]= cms.PSet(
        miniView = cms.string("GenJetView"),
        branchPrefix = cms.untracked.string("ak5ChgGenJets"),
        maxEta = cms.double(3.0),
        minPt = cms.double(1.0),
        genJets = cms.InputTag("ak5ChgGenJets"),
    )
    
    defs["ak7ChgGenJetView"]= cms.PSet(
        miniView = cms.string("GenJetView"),
        branchPrefix = cms.untracked.string("ak7ChgGenJets"),
        maxEta = cms.double(3.0),
        minPt = cms.double(1.0),
        genJets = cms.InputTag("ak7ChgGenJets"),
    )
    
    defs["ak10ChgGenJetView"]= cms.PSet(
        miniView = cms.string("GenJetView"),
        branchPrefix = cms.untracked.string("ak10ChgGenJets"),
        maxEta = cms.double(3.0),
        minPt = cms.double(1.0),
        genJets = cms.InputTag("ak10ChgGenJets"),
    )
    
    defs["sisCone5ChgGenJetView"]= cms.PSet(
        miniView = cms.string("GenJetView"),
        branchPrefix = cms.untracked.string("sisCone5ChgGenJets"),
        maxEta = cms.double(3.0),
        minPt = cms.double(1.0),
        genJets = cms.InputTag("sisCone5ChgGenJets"),
    )
    
    defs["sisCone7ChgGenJetView"]= cms.PSet(
        miniView = cms.string("GenJetView"),
        branchPrefix = cms.untracked.string("sisCone7ChgGenJets"),
        maxEta = cms.double(3.0),
        minPt = cms.double(1.0),
        genJets = cms.InputTag("sisCone7ChgGenJets"),
    )

    # main function
    ret = {}
    for t in todo:
        if t not in defs:
            raise Exception("miniView def not known "+t)

        ret[t] = defs[t]
    return ret


