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

  #if int(sampleList[s]["crabJobs"]) < 500:
  #    command+=" -submit 1-10"

  #''' XXX csa
  if isData and not "CSA14" in name:
    print isData, sampleList[s]["json"]
    command+=" -CMSSW.total_number_of_lumis=-1"
    
    jsonFile=edm.FileInPath(sampleList[s]["json"])
    command+=" -CMSSW.lumi_mask="+jsonFile.fullPath()
  else:
    command+=" -CMSSW.total_number_of_events="+str(sampleList[s]["numEvents"])
  #'''

  # TODO save old value and set it at exit   
  os.environ["TMFSampleName"]=s
  os.environ["TMFDSName"]=sampleList[s]["DS"]

  # crab is not able to submit more than 500 jobs at once
  # note, there was a limit of ~2000 jobs per task (one could
  # submit more than 2000, but job status check resulted in crash
  if int(sampleList[s]["crabJobs"]) >= 500:
    # XXX TODO       
    command.replace("-submit", " ")
    print "#"*40
    print "Note: submission of more then 500 jobs is currently not supported. Jobs will be created, please submit manually"
    print "#"*40
    os.system(command)
    #i=1
    #step = 400
    #while i<int(sampleList[s]["crabJobs"]):
    #    range=str(i)+","+str(i+step)
    #    command+="crab -submit " + range + " -c " + name
    #    i+=step
  else:
      #print command
      #sys.exit()
      os.system(command)

  cfgName = None
  with open("crab.cfg", "r") as cfg:
    for l in cfg:
        line = l.strip()
        if "pset=" not in line: continue
        cfgName = line.split("=")[-1]


  if not cfgName:
    print "Unable to determine cfg name from crab.cfg!"
  else:
    fOut = name + "/" + cfgName
    shutil.copy(cfgName, fOut)
