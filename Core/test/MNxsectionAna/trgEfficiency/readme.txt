

hltEffHistos_XXX.root:

1. Run crab jobs for both mu_2010 datasets - S_HLTEfficiency directory
2. Prepare histograms by running HLTEfficiency.py

- note that you must link the file so it is visible in your working directory
  (the one containing crab dirs):
       ln -s ../scripts/HLTEfficiency.py

- Run seperately for each trigger. Currently supported triggers are
    HLT_Jet15U - option name "j15"
   and
    HLT_DoubleJet15U_ForwardBackward - option name "dj15fb"

- for other triggers you may need to check what HLT trigger object collection
  was used and rerun the crab jobs. HLT PT threshold must be set inside
  HLTEfficiency class

-  The script (after the link was done) is invoked by

 ./HLTEfficiency.py -t dj15fb Jets-Run*
 ./HLTEfficiency.py -r -t dj15fb Jets-Run*
 ./HLTEfficiency.py -r -t j15 Jets-Run*
 ./HLTEfficiency.py -r -l -t j15 Jets-Run*


 (for both currently supported triggers). Jets-MuRun* correspond to  two crab directories from step 1.

 Rootfiles will be saved in your  ~/tmp/ directory
###############################################################################
prescales data:
1. Install lumi scripts https://twiki.cern.ch/twiki/bin/viewauth/CMS/LumiCalc
2. Use ../../scripts/getPrescales.py to dump the prescales to a pickle
file

 -- set desired trigger and path to good lumi json inside the script

usefull aqdditional commands:

# compare contents of two datatags
lumiCalc2.py lumibyls --hltpath "HLT_Jet15U*" -r 146511  --datatag v11
lumiCalc2.py lumibyls --hltpath "HLT_Jet15U*" -r 146511  --datatag v12 
###############################################################################
lumi per run data
1. Install lumi scripts https://twiki.cern.ch/twiki/bin/viewauth/CMS/LumiCalc
2. Use getLumiPerRunFromCERT.py to dump lumi data

 -- set desired trigger and path to good lumi json inside the script





