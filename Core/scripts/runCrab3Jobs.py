#!/usr/bin/env python
import sys,os,re,shutil
from optparse import OptionParser

# TODO: voms-proxy-init --voms cms --valid 168:00

import ROOT
#ROOT.gROOT.SetBatch(True)

# for fileinpath
from ROOT import *
ROOT.gSystem.Load("libFWCoreFWLite.so")
FWLiteEnabler.enable()

import CommonFSQFramework.Core.Util

sampleList=CommonFSQFramework.Core.Util.getAnaDefinition("sam")
anaVersion=CommonFSQFramework.Core.Util.getAnaDefinition("anaVersion")
blacklist=CommonFSQFramework.Core.Util.getAnaDefinition("cbSmartBlackList")

def dumpEnvVariable(var):
    ret = "# "+var+"="
    if var in os.environ:
        ret += str(os.environ[var])
    else:
        ret += "<not in env>"
    return ret+"\n"


print "Submitting jobs for:", anaVersion
print "Using black list:", blacklist

parser = OptionParser(usage="usage: %prog [options] filename",
                        version="%prog 1.0")

parser.add_option("-s", "--sample", action="store", type="string", dest="sample" )
parser.add_option("-c", "--config", action="store", type="string", dest="config" )
#parser.add_option("-d", "--dataOnly", action="store", type="bool", dest="dataOnly" )
(options, args) = parser.parse_args()

configFile = "crabcfg.py"
if options.config != None and options.config != "":
    configFile = options.config
print "Reading crab config file: ", configFile


if options.sample == None or options.sample == "":
    print "You must specify one or more valid sample(s) from your sample-list, or \"all\": "
    print "Use the -s or --sample option and comma separation if needed"
    print "List of valid samples:"
    for sample in sampleList:
        print " - ", sample
    sys.exit()


if options.sample == "all":
    sampleListTodo = sampleList.keys()
else:
    sampleListTodo = []
    samplesListFromCLI = options.sample.split(",")
    for s in samplesListFromCLI:
        sampleListTodo.append(s)
        if s not in sampleList.keys():
            print "Invalid sample name ", s
            sys.exit(1)

for s in sampleListTodo:

  isData=False
  if "isData" in sampleList[s]:
    isData=sampleList[s]["isData"]

  name=anaVersion + "_" + s

  targetPath = anaVersion + "/" + "crab_" + name
  if os.path.exists(targetPath):
    print "Path", targetPath, "allready exists. Doing nothing"
    continue    

  # crab is creating the directory
  print "Create working directory: ", targetPath

  pycfgextra = []  
  pycfgextracheck = []  
  pycfgextra.append("config.General.workArea='"+anaVersion+"'")
  pycfgextra.append("config.General.requestName='"+name+"'")
  pycfgextra.append("config.Data.outputDatasetTag='"+name+"'")
  pycfgextra.append("config.Data.inputDataset='"+sampleList[s]["DS"]+"'")
  # customize when running on private datasets
  if "/USER" in sampleList[s]["DS"]: 
      print "Submitting jobs with a private USER made input dataset"
      pycfgextra.append("config.Data.inputDBS = 'phys03'")

  
  if isData:
    print "Input is \"data\" with lumi file: " + sampleList[s]["json"]
    pycfgextracheck.append("config.Data.splitting='LumiBased'")
    pycfgextracheck.append("config.Data.unitsPerJob=10")
    if os.path.exists(sampleList[s]["json"]):
        jsonFile = open(sampleList[s]["json"])
        pycfgextra.append("config.Data.lumiMask='" + os.path.abspath(sampleList[s]["json"]) + "'")
    else:
        jsonFile = edm.FileInPath(sampleList[s]["json"])
        pycfgextra.append("config.Data.lumiMask='"+jsonFile.fullPath()+"'")
    
  else:
    print "Input is \"MC\""
    pycfgextracheck.append("config.Data.splitting='EventAwareLumiBased'")
    pycfgextracheck.append("config.Data.unitsPerJob=100000")
  

  # TODO save old value and set it at exit   
  os.environ["TMFSampleName"] = s


  cfgName = None
  with open("tmp.py", "w") as myfile:
      checklines = []
      with open(configFile, "r") as infile:
          for inline in infile:
              myfile.write(inline)
              # search for cmssw job config file while reading
              line = inline.strip()
              if len(line) > 0 and line[0] == "#":
                  continue
              checklines.append(inline)
              if "config.JobType.psetName"  not in line:
                  continue
              cfgName = line.split("=")[-1].replace("'","").replace('"',"").strip()
      # append custom config, no-check
      for l in pycfgextra:
          myfile.write(l+"\n")
      # append custom config, WITH-check
      for extraline in pycfgextracheck:
          found = False
          for check in checklines:
              assign = extraline.split('=')
              if (len(assign)>0):
                  if check.strip().find(assign[0].strip()) != 0:
                      found = True
                      break
          if not found:
              myfile.write(extraline+"\n")
      myfile.close()

  if not cfgName:
    print "ERROR: Unable to determine cmssw-jobcfg name from crab.cfg!"
    sys.exit()
  else:
    if not os.path.isfile(cfgName):
        print "ERROR: cannot determine the cmssw-jobcfg name. Tried: ", cfgName
        sys.exit()

  os.system("crab submit -c tmp.py")

  fOut = targetPath + "/" + cfgName
  shutil.copy(cfgName, fOut)

sys.exit()
