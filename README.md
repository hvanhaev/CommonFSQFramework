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

This master branch was used during the inital development phase with early Run II data in CMSSW 6 or 7 releases. As new CMSSW versions were released the compatibility of this framework and proper data analysis required the usage of different branches with developments tailored to a particular CMSSW release. 

<b>This master branch is thus not updated, but several other branches are, each for a different CMSSW release cycle.</b>

Current branches:<br>
- CMSSW_74X: intended for early Run II 2015 data analysis/development. Should be superseded by CMSSW_76X branch.
- CMSSW_76X: use it for Run II 2015 data analysis.
- CMSSW_80X: use it for Run II 2016 data analysis.
- CMSSW_92X: was intended for development.
- CMSSW_101X: was intended for development (and early Run II 2018 data analysis). Should be superseded by CMSSW_103X branch.
- CMSSW_103X: use it for Run II 2018 data analysis.

For use with CMSSW: clone this repository in your CMSSW/src directory and compile with scram b.

# Note for standalone operations:

In order to run CFF in standalone mode as a python library, just
execute the script ./makeStandalone.sh Afterwards you are ready to use
the library on any machine that has just python and PyROOT installed!

Make sure you don't load the libFWCoreFWLite.so anywhere in your code and
scripts. This will not work on normal computer systems without CMSSW. 

