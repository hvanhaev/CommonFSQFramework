#!/bin/tcsh

echo "Configure for CASTOR fast feedback RAW data 2018"
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
echo $DIR

export SmallXAnaDefFile="$PWD/MyAnalysis.py"
export SmallXAnaVersion="Samples_Local"

#
#
#
#
# not needed in lxplus6
#source /afs/cern.ch/cms/LCG/LCG-2/UI/cms_ui_env.csh

# for lxplus6
# source /afs/cern.ch/cms/ccs/wm/scripts/Crab/crab.csh

# for crab3
#if [ -f /cvmfs/cms.cern.ch/crab3/crab.sh ]; then
#    source /cvmfs/cms.cern.ch/crab3/crab.sh
#    cp -rf data ../
#    cp -rf data ../..
#fi

export PYTHONPATH=$PYTHONPATH:$DIR:./
export PATH=$PATH:$DIR/../../../../CommonFSQFramework/Core/scripts/
 
printTTree.py
