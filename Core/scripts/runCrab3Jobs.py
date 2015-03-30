#!/usr/bin/env python
import sys,os,re,shutil
from optparse import OptionParser

# TODO: voms-proxy-init --voms cms --valid 168:00

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

  targetPath = anaVersion + "/" + "crab_" + name
  if os.path.exists(targetPath):
    print "Path", name, "allready exists. Doing nothing"
    continue    

 


  pycfgextra = []  
  pycfgextra.append("config.General.workArea='"+anaVersion+"'")
  pycfgextra.append("config.General.requestName='"+name+"'")
  pycfgextra.append("config.Data.publishDataName='"+name+"'")
  pycfgextra.append("config.Data.inputDataset='"+sampleList[s]["DS"]+"'")

  '''
  if isData:
    print isData, sampleList[s]["json"]
    command+=" -CMSSW.total_number_of_lumis=-1"
    
    jsonFile=edm.FileInPath(sampleList[s]["json"])
    command+=" -CMSSW.lumi_mask="+jsonFile.fullPath()
  else:
    command+=" -CMSSW.total_number_of_events="+str(sampleList[s]["numEvents"])
    '''

  # TODO save old value and set it at exit   
  os.environ["TMFSampleName"]=s

  # crab is not able to submit more than 500 jobs at once
  # note, there was a limit of ~2000 jobs per task (one could
  # submit more than 2000, but job status check resulted in crash
  '''
  if int(sampleList[s]["crabJobs"]) >= 500:
    i=1
    step = 400
    while i<int(sampleList[s]["crabJobs"]):
        range=str(i)+","+str(i+step)
        command+="crab -submit " + range + " -c " + name
        i+=step
  else:
      #print command
      #sys.exit()
      os.system(command)
  '''

  os.system("cp crabcfg.py  tmp.py")
  with open("tmp.py", "a") as myfile:
    for l in pycfgextra:
        myfile.write(l+"\n")

  #os.system("./crab submit -c tmp.py")
  os.system("crab submit -c tmp.py")

  cfgName = None
  with open("crabcfg.py", "r") as cfg:
    for l in cfg:
        line = l.strip()
        #if "pset=" not in line: continue
        if len(line) > 0 and line[0] == "#": continue
        if "config.JobType.psetName"  not in line: continue
        cfgName = line.split("=")[-1].replace("'","").replace('"',"").strip()


  if not cfgName:
    print "Unable to determine cfg name from crab.cfg!"
  else:
    if not os.path.isfile(cfgName):
        print "Warning: cannot determine the pset. Tried:", cfgName
    else:
        fOut = targetPath + "/" + cfgName
        shutil.copy(cfgName, fOut)
  sys.exit()  
