import FWCore.ParameterSet.Config as cms


def setPrimarySecondaryFile(process, raw, aod):
    process.source = cms.Source("PoolSource",
        secondaryFileNames = cms.untracked.vstring(raw),
        fileNames = cms.untracked.vstring(aod)
    )
    return process


def setFilesForDevel(process):
    aod = "root://xrootd.ba.infn.it//store/mc/Spring14dr/QCD_Pt-50to80_Tune4C_13TeV_pythia8/AODSIM/castor_Flat0to10_POSTLS170_V5-v1/00000/363D5394-CF12-E411-A75C-002590596484.root"

    raw = "root://xrootd.ba.infn.it//store/mc/Spring14dr/QCD_Pt-50to80_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_Flat0to10_POSTLS170_V5-v1/00000/BCDF1B07-B212-E411-A99A-00248C55CC9D.root"
    return setPrimarySecondaryFile(process, raw, aod)



