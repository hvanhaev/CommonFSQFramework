#!/usr/bin/env python
import sys,os,re,shutil
from optparse import OptionParser

import ROOT
ROOT.gROOT.SetBatch(True)

# for fileinpath
from ROOT import *
ROOT.gSystem.Load("libFWCoreFWLite.so")
AutoLibraryLoader.enable()

import MNTriggerStudies.MNTriggerAna.Util

sampleList=MNTriggerStudies.MNTriggerAna.Util.getAnaDefinition("sam")
anaVersion=MNTriggerStudies.MNTriggerAna.Util.getAnaDefinition("anaVersion")
blacklist=MNTriggerStudies.MNTriggerAna.Util.getAnaDefinition("cbSmartBlackList")

def dumpEnvVariable(var):
    ret = "# "+var+"="
    if var in os.environ:
        ret += str(os.environ[var])
    else:
        ret += "<not in env>"
    return ret+"\n"


print "Submitting jobs for", anaVersion


parser = OptionParser(usage="usage: %prog [options] filename",
                        version="%prog 1.0")

parser.add_option("-s", "--sample", action="store", type="string", dest="sample" )
#parser.add_option("-d", "--dataOnly", action="store", type="bool", dest="dataOnly" )
(options, args) = parser.parse_args()

if options.sample:
    sampleListTodo = []
    samplesListFromCLI = options.sample.split(",")
    for s in samplesListFromCLI:
        sampleListTodo.append(s)
else:
    sampleListTodo = sampleList.keys()

for s in sampleListTodo:

  isData=False
  if "isData" in sampleList[s]:
    isData=sampleList[s]["isData"]

  name=anaVersion+"_"+s
  if os.path.exists(name):
    print "Path", name, "allready exists. Doing nothing"
    continue    

 


  command="crab -USER.ui_working_dir="+name
  command+=" -create "
  command+=" -USER.publish_data_name="+name
  command+=" -CMSSW.datasetpath="+sampleList[s]["DS"]
  command+=" -CMSSW.number_of_jobs="+str(sampleList[s]["crabJobs"])
  command+=" -GRID.ce_black_list="+blacklist

  if int(sampleList[s]["crabJobs"]) < 500:
      command+=" -submit "

  if isData:
    print isData, sampleList[s]["json"]
    command+=" -CMSSW.total_number_of_lumis=-1"
    
    jsonFile=edm.FileInPath(sampleList[s]["json"])
    command+=" -CMSSW.lumi_mask="+jsonFile.fullPath()
  else:
    command+=" -CMSSW.total_number_of_events="+str(sampleList[s]["numEvents"])

  '''
  if isData:
    os.environ["isData"]="True"
  else:
    os.environ["isData"]="False"


  os.environ["TFGlobalTag"]=""
  gt = sampleList[s]["GT"]
  os.environ["TFGlobalTag"]=gt
  os.environ["TFSampleName"]=s
  ''' 

  '''
  if int(sampleList[s]["crabJobs"]) >= 500:
    i=1
    step = 400
    while i<int(sampleList[s]["crabJobs"]):
        range=str(i)+","+str(i+step)
        command+="crab -submit " + range + " -c " + name
        i+=step
  '''
  
  #sys.exit()



  print command
  sys.exit()
  #os.system(command)

  cfgName = None
  with open("crab.cfg", "r") as cfg:
    for l in cfg:
        line = l.strip()
        if "pset=" not in line: continue
        cfgName = line.split("=")[-1]


  '''
  if not cfgName:
    print "Unable to determine cfg name from crab.cfg!"
  else:
    fOut = name + "/" + cfgName
    shutil.copy(cfgName, fOut)
    with open(fOut,"a") as cfgFileCopy:
        strout = "Shell env dump:\n"
        strout += dumpEnvVariable("TFGlobalTag")
        strout += dumpEnvVariable("TFSampleName")
        strout += dumpEnvVariable("isData")
        cfgFileCopy.write(strout)
    
  # clean settings  
  os.environ["TFGlobalTag"]=""
  os.environ["TFSampleName"]=""
  os.environ["isData"]="" 
  '''




