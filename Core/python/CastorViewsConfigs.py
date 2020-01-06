import FWCore.ParameterSet.Config as cms

def get(todo):
    defs = {}

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

    defs["CastorRecHitViewFull"]= cms.PSet(   
        miniView = cms.string("CastorRecHitView"),
        branchPrefix = cms.untracked.string("CastorRecHit"),
        onlyGoodRecHits = cms.bool(False),
        writeSaturationInfo = cms.bool(True),
        inputcoll = cms.InputTag("castorreco")         
    )
    
    defs["CastorRecHitViewFullCorrected"]= cms.PSet(
        miniView = cms.string("CastorRecHitView"),
        branchPrefix = cms.untracked.string("CastorRecHit"),
        onlyGoodRecHits = cms.bool(False),
        writeSaturationInfo = cms.bool(True),
        inputcoll = cms.InputTag("rechitcorrector")
    )
   
    defs["CastorRecHitViewBasic"]= cms.PSet( 
        miniView = cms.string("CastorRecHitView"),
        branchPrefix = cms.untracked.string("CastorRecHit"),
        onlyGoodRecHits = cms.bool(True),
        writeSaturationInfo = cms.bool(False),       
        inputcoll = cms.InputTag("castorreco")         
    )
 
    defs["CastorRecHitViewBasicCorrected"]= cms.PSet(
        miniView = cms.string("CastorRecHitView"),
        branchPrefix = cms.untracked.string("CastorRecHit"),
        onlyGoodRecHits = cms.bool(True),
        writeSaturationInfo = cms.bool(False),
        inputcoll = cms.InputTag("rechitcorrector")
    )
    
    defs["CastorTowerView"]  = cms.PSet(
        miniView = cms.string("CastorTowerView"),
        branchPrefix = cms.untracked.string("CastorTower"),
        inputcoll = cms.InputTag("CastorTowerReco")
    )

    ret = {}
    for t in todo:
        if t not in defs:
            raise Exception("miniView def not known "+t)

        ret[t] = defs[t]
    return ret



