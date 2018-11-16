import FWCore.ParameterSet.Config as cms

def get(todo):
    defs = {}
    
    defs["CastorDigiView"] = cms.PSet(
		miniView = cms.string("CastorDigiView"),
		m_firstTS = cms.untracked.int32(0),
		m_lastTS = cms.untracked.int32(10),
		m_Digis = cms.InputTag('castorDigis')
	)


