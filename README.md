# CommonFSQFramework

This is the common software analysis package of the Forward and Small-x QCD group in the CMS experiment at CERN to process LHC Run2 data.

For more information regarding this framework, please look at the following pages: <br>
https://twiki.cern.ch/twiki/bin/viewauth/CMS/FSQCommonFW
https://twiki.cern.ch/twiki/bin/viewauth/CMS/FSQCommonFWTutorialP2 (currently not up to date)<br>

Twiki page with existing skims:<br>
https://twiki.cern.ch/twiki/bin/view/CMS/CFFSkims

Special tutorial session on how to work with python analyzers: <br>
https://twiki.cern.ch/twiki/bin/view/CMS/FSQCommonFW201504Jets

Or look into the /Core/doc directory for information.

Please note that the code is still developing and improving. 


# NOTE (for standalone operations):

In order to tun CFF in standalone mode as a python library, just
execute the script ./makeStandalone.sh Afterwards you are ready to use
the library on any machine that has just python an PyROOT installed!

Make sure you don't load the libFWCoreFWLite.so anywhere in your code and
scripts. This will not work on normal computer systems witout CMSSW. 

