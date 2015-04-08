This file describes process of new skim creation. Most importantly it explains how to attach 
services of the CFF to the existing python configuration.

For jet based analyses (ie the jet skim) we want to use basic PAT
configuration, since it merges all the scaterred information into a single
object (pat::Jet). It also takes care of applying JEC.

Note: for different analysis (e.g. track based) we could start with a 
basic configuration file with only source/geometry/gt/... definitions. There
is nothing that forces us to use PAT if we dont need it.

1. Create python config

 Configuration with different jet collections processed by PAT is avaliable in

PhysicsTools/PatAlgos/test/patTuple_addJets_cfg.py

 This file was copied and saved as S0_makePAT_74.py


2. Add basic CFF services

at the end of the file append
------
import CommonFSQFramework.Core.customizePAT
process = CommonFSQFramework.Core.customizePAT.customize(process)
------
note: it should also work on regular, ie non-PAT, configurations. If not -
contact CFF developers

Above customization peforms the following
- Add CFF event counters
- Add TFileService
- Remove the edm output module if present in configuration 
(may need fixing, if it doesnt work contact CFF  developers)

Since event data is saved in our trees it makes no sense to produce a standard
edm output (we dont use it in the framework). Keeping the edm output in
configuration will make your crab jobs to run significantly longer (note:
removing the output most likely will prevent large number of CMSSW modules
from running thanks to magic of unscheduled execution)


3. Add plugins










