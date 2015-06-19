import FWCore.ParameterSet.Config as cms

def get(todo):
    defs = {}
    defs["JetViewPFAK4CHS"]  = cms.PSet(
        miniView = cms.string("JetView"),
        storeageVersion = cms.untracked.int32(1),
        disableJetID = cms.bool(True),
        optionalCaloJets4ID = cms.InputTag("ak5CaloJets","","RECO"),
        optionalCaloID4ID  = cms.InputTag("ak5JetID"),
        branchPrefix = cms.untracked.string("PFAK4CHS"),
        maxEta = cms.double(5.2),
        minPt = cms.double(3),
        maxnum = cms.int32(3),
        input = cms.InputTag("selectedPatJetsAK4PFCHSCopy"),
        variations= cms.vstring("", "jecUp", "jecDown"),
        jerFactors = cms.vstring(  # PF10
                "5.5 1 0.007 0.07 0.072"),
    )
    # and so on
    defs["JetViewSisCone5TrackJets"]= cms.PSet(
        miniView = cms.string("TrackJetView"),
	maxEta = cms.double(2),
        minPt = cms.double(1),
	branchPrefix = cms.untracked.string("SisCone5CH"),
        input = cms.InputTag("sisCone5TrackJets"),	
    )

    ret = {}
    for t in todo:
        if t not in defs:
            raise Exception("miniView def not known "+t)

        ret[t] = defs[t]
    return ret


