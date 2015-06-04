import FWCore.ParameterSet.Config as cms

def get(todo):
    defs = {}

    # Get all PFCandidates from the general collection
    defs["PFCandidateView"]  = cms.PSet(
        miniView = cms.string("PFCandidateView"),
        branchPrefix = cms.untracked.string("PFCandidates"),
        inputcoll = cms.InputTag("particleFlow")
    )

 
    # main function
    ret = {}
    for t in todo:
        if t not in defs:
            raise Exception("miniView def not known "+t)

        ret[t] = defs[t]
    return ret


