import FWCore.ParameterSet.Config as cms

# TODO: remove jobs output
def customize(process):
    process.out.outputCommands  = [ 'drop *' ]
    process.options.wantSummary = False   ##  (to suppress the long output at the end of the job)
    process.MessageLogger.cerr.FwkReport.reportEvery = 50
    process.out.fileName = 'mnTrgAna_PAT.root'
    process.TFileService = cms.Service("TFileService", fileName = cms.string("trees.root") )

    process.exampleTree = cms.EDAnalyzer("ExampleTreeProducer")
    #process.mnTriggerAna = cms.EDAnalyzer("MNTriggerAna")
    #process.mnTriggerAnaNew = cms.EDAnalyzer("MNTriggerAnaNew")
    process.infoHisto = cms.EDAnalyzer("SaveCountHistoInTreeFile")
    #process.pTreeProducers = cms.Path(process.infoHisto*process.exampleTree*process.mnTriggerAna*process.mnTriggerAnaNew)
    process.pTreeProducers = cms.Path(process.infoHisto*process.exampleTree)

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



    process.pUtil = cms.Path(process.XS)
    process.schedule = cms.Schedule()
    process.pUtil = cms.Path(process.XS)
    process.schedule.append(process.pUtil)
    process.schedule.append(process.pTreeProducers) # TODO tree producer will run through all events, not depending on the filtering results
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



