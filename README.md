# CommonFSQFramework

This is the common software analysis package of the Forward and Small-x QCD group in the CMS experiment at CERN to process LHC Run2 data.

For more information regarding this framework, please look at the following pages: <br>
https://twiki.cern.ch/twiki/bin/viewauth/CMS/FSQCommonFW (General analysis use)
https://twiki.cern.ch/twiki/bin/viewauth/CMS/FSQCommonFWTutorialP2 (information on how to create your own skims/code)<br>

Twiki page with existing skims:<br>
https://twiki.cern.ch/twiki/bin/view/CMS/CFFSkims

Special tutorial session on how to work with python analyzers: <br>
https://twiki.cern.ch/twiki/bin/view/CMS/FSQCommonFW201504Jets

Or look into the /Core/doc directory for information.

# Compatibility and Usage

In order to get the code compiled you need to install a CMSSW release CMSSW_7_6_X with X >= 7. 

<b>This branch version is intended for analysis of Run II 2015 data.</b> 

For use with CMSSW: clone this repository in your CMSSW/src directory and compile with scram b.

# Note for standalone operations:

In order to run CFF in standalone mode as a python library, just
execute the script ./makeStandalone.sh Afterwards you are ready to use
the library on any machine that has just python and PyROOT installed!

Make sure you don't load the libFWCoreFWLite.so anywhere in your code and
scripts. This will not work on normal computer systems without CMSSW. 

