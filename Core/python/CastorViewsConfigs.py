import FWCore.ParameterSet.Config as cms

def get(todo):
    defs = {}
    defs["ak5GenJetView"]= cms.PSet(   
        miniView = cms.string("GenJetView"),
        branchPrefix = cms.untracked.string("ak5GenJets"),
        maxEta = cms.double(7.0),
        minPt = cms.double(1.0),
        genJets = cms.InputTag("ak5GenJets"),
    )

    defs["ak5CastorJetView"]= cms.PSet(   
        miniView = cms.string("CastorJetView"),
        branchPrefix = cms.untracked.string("ak5CastorJets"),
        minCastorJetEnergy = cms.double(50.),
        jetRadius = cms.double(0.5)
    )

    defs["ak7CastorJetView"]= cms.PSet(   
        miniView = cms.string("CastorJetView"),
        branchPrefix = cms.untracked.string("ak7CastorJets"),
        minCastorJetEnergy = cms.double(50.),
        jetRadius = cms.double(0.7)
    )

    defs["VerticesView"]= cms.PSet(   
        miniView = cms.string("VerticesView"),
        branchPrefix = cms.untracked.string("Vtx"),
        src = cms.InputTag("offlinePrimaryVertices"),
    )

    defs["CastorRecHitView"]= cms.PSet(   
        miniView = cms.string("CastorRecHitView"),
        branchPrefix = cms.untracked.string("CastorRecHit"),
    )   

    defs["JetViewPFAK4CHS"]  = cms.PSet(
        miniView = cms.string("JetView"),
        storeageVersion = cms.untracked.int32(0),
        disableJetID = cms.bool(True),
        optionalCaloJets4ID = cms.InputTag(""),#ak5CaloJets","","RECO"),
        optionalCaloID4ID  = cms.InputTag(""),#ak5JetID"),
        branchPrefix = cms.untracked.string("PFAK4CHS"),
        maxEta = cms.double(5.2),
        minPt = cms.double(1),
        maxnum = cms.int32(3),
        input = cms.InputTag("selectedPatJetsAK4PFCHSCopy"),
        variations= cms.vstring(""),
        jerFactors = cms.vstring(  # PF10
                "5.5 1 0.007 0.07 0.072"),
    )

    ret = {}
    for t in todo:
        if t not in defs:
            raise Exception("miniView def not known "+t)

        ret[t] = defs[t]
    return ret


