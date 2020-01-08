from WMCore.Configuration import Configuration
config = Configuration()

config.section_("User")

config.section_("General")

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'treemaker_Eflow_103X.py'

config.section_("Data")
#config.Data.totalUnits = 1000000 # use this only for MC, when you want to limit number of events to process
config.Data.publication = False
config.Data.splitting='EventAwareLumiBased'
config.Data.unitsPerJob=100000

config.section_("Site")
config.Site.storageSite = "T2_BE_IIHE"
