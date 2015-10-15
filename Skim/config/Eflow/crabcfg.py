from WMCore.Configuration import Configuration
config = Configuration()

config.section_("User")
config.User.voGroup = 'becms'

config.section_("General")

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'treemaker_Eflow_74X.py'

config.section_("Data")


config.section_("Site")
config.Site.storageSite = "T2_BE_IIHE"
