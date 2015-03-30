import FWCore.ParameterSet.Config as cms

def addTreeProducer(process, prod):
    if not hasattr(process, "schedule"):
        raise Exception("Given process seems not to have a valid scheduler. Run the base customize function first")
    pathName = "p"+prod.label()
    if hasattr(process, pathName):
        raise Exception("Path " + pathName + "allready in process definition. Try using different name")
    setattr(process, pathName, cms.Path(prod))
    # this inserts the path on last possible possition - just before the endPath
    process.schedule.insert(-1, getattr(process, pathName)) 
    return process

def addPath(process, path):
    if not hasattr(process, "schedule"):
        raise Exception("Given process seems not to have a valid scheduler. Run the base customize function first")

    process.schedule.insert(-1, path)
    return process

# TODO: remove jobs output
def customize(process):
    if hasattr(process, "out"):
        process.out.outputCommands  = [ 'drop *' ]
        process.out.fileName = 'mnTrgAna_PAT.root'
    if hasattr(process, "options"):
        process.options.wantSummary = False   ##  (to suppress the long output at the end of the job)
    if hasattr(process, "MessageLogger"):
        process.MessageLogger.cerr.FwkReport.reportEvery = 50
    process.TFileService = cms.Service("TFileService", fileName = cms.string("trees.root") )

    process.infoHisto = cms.EDAnalyzer("SaveCountHistoInTreeFile")
    #process.pTreeProducers = cms.Path(process.infoHisto*process.exampleTree*process.mnTriggerAna*process.mnTriggerAnaNew)
    #process.pTreeProducers = cms.Path(process.infoHisto*process.exampleTree)
    process.pTreeProducers = cms.Path(process.infoHisto)

    # Note: despite we are putting this value into every event waste of space is neglible thanks to root branch compression.
    process.XS =  cms.EDProducer("DoubleProducer",
        value = cms.double(-1),
    )

    process.initialCntr = cms.EDProducer("EventCountProducer")
    process.initialSequence = cms.Sequence(process.initialCntr)

    import FWCore.ParameterSet.SequenceTypes as st
    for a in dir(process):
        attr = getattr(process, a)
        if type(attr) == st.Path:
            #l1 = len(attr._seq.__str__().split("+"))
            #attr._seq = process.initialSequence * attr._seq
            attr.insert(0, process.initialSequence)
            #l2 = len(attr._seq.__str__().split("+"))
            #print l1, l2



    import types
    process.pUtil = cms.Path(process.XS)
    if not hasattr(process, "schedule") or type(process.schedule) == types.NoneType:
       process.schedule = cms.Schedule()
    process.pUtil = cms.Path(process.XS)
    process.schedule.append(process.pUtil)
    process.schedule.append(process.pTreeProducers)
    if hasattr(process, "outpath"):
        process.schedule.append(process.outpath)

    import os
    if "TMFSampleName" not in os.environ:
        print "#"*80
        print "#"
        print "#    Note: 'TMFSampleName' variable not found in environment."
        print "#             Will embed default values (XS wont be set)"
        print "#"
        print "#"*80
    else:
        s = os.environ["TMFSampleName"]
        print "Customizing to: ", s
        import MNTriggerStudies.MNTriggerAna.Util
        sampleList=MNTriggerStudies.MNTriggerAna.Util.getAnaDefinition("sam")
        anaVersion=MNTriggerStudies.MNTriggerAna.Util.getAnaDefinition("anaVersion")
        XS = sampleList[s]["XS"]
        isData =  sampleList[s]["isData"]
        
        stringForProv = "\n"+"#"*80+"\n"
        stringForProv += "Ana version: " + anaVersion + "\n"
        stringForProv += "XS = " + str(XS) + "\n"
        process.XS.value = XS
        stringForProv += "isData = " + str(isData) + "\n" # not used...yet
        stringForProv += "#"*80+"\n"

        print stringForProv
        # attach the string to one of the modules, so it will show in the prov data
        # (use edmProvDump on the PAT file to see it)
        process.XS.provHack = cms.string(stringForProv)
        process.TMFDataForProv = cms.PSet(notes = cms.string("test"))

    # also - GT 

    #process.out.SelectEvents = cms.untracked.PSet(
    #        SelectEvents = selectorPaths
    #)

   
    return process

def removeEdmOutput(process):
    if hasattr(process, "outpath"):
        if hasattr(process, "schedule"):
            process.schedule.remove(process.outpath)
        del process.outpath

    # TODO: identify output modules and path that own them
    if hasattr(process, "out"):
        del process.out

    return process


