import os, sys, subprocess, imp
import distutils.spawn



def getCrabVersion():
    try:
        #ver=subprocess.check_output(["crab", "--version"])#,, "v3"
        # python 2.6 compat
        p = subprocess.Popen(["crab", "--version"], stdout=subprocess.PIPE)
        ver = p.communicate()[0]
    except OSError:
        print ("Seems that crab environment is not defined. Exit... stage left")
        sys.exit(1)
    ret = 2
    if "v3" in ver:
        ret = 3 
    return ret



def getVariant():
    if  "SmallXAnaVersion" not in  os.environ:
        m = " Cannot get ana variant from env. Set SmallXAnaVersion "
        m += "to desired value (e.g. by sourcing one of files from CommonFSQFramework.Core/env/ directory) "
        print (m)
        sys.exit(1)
    variant = os.environ["SmallXAnaVersion"]
    return variant



def getFullPathToAnaDefinitionFile():
    variant = getVariant()
    command = "import " + variant + " as tmpxxx"
    exec command
    return tmpxxx.__file__



def readAnaConfig():
    import os,imp
    if "SmallXAnaDefFile" not in os.environ:
        print ("Please set SmallXAnaDefFile environment variable:")
        print ("export SmallXAnaDefFile=FullPathToFile")
        print ("Whooops! SmallXAnaDefFile env var not defined")
        sys.exit(1)
    anaDefFile = os.environ["SmallXAnaDefFile"]
    mod_dir, filename = os.path.split(anaDefFile)
    mod, ext = os.path.splitext(filename)
    f, filename, desc = imp.find_module(mod, [mod_dir])
    mod = imp.load_module(mod, f, filename, desc)
    localBasePathPAT = ""
    localBasePathTrees = ""
    ROOTPrefix="..none.." # don't change this!
    if hasattr(mod, "ROOTPrefix"):
        ROOTPrefix = mod.ROOTPrefix
    if hasattr(mod, "ROOTprefix"):
        ROOTPrefix = mod.ROOTprefix
    if hasattr(mod, "PATbasePATH"):
        localBasePathPAT = mod.PATbasePATH
    if hasattr(mod, "TTreeBasePATH"):
        localBasePathTrees = mod.TTreeBasePATH
    return localBasePathTrees, localBasePathPAT, ROOTPrefix

        

def fixLocalPaths(sam):
    if (not isinstance(sam, dict)):
        return sam
    localBasePathTrees, localBasePathPAT, ROOTPrefix = readAnaConfig()
    for sample in sam:
        if "pathSE" in sam[sample]:
            sam[sample]["pathSE"] = sam[sample]["pathSE"].rstrip('/')
        if "pathPAT" in sam[sample]:
            sam[sample]["pathPAT"] = sam[sample]["pathPAT"].replace("XXXTMFPAT", localBasePathPAT)
            sam[sample]["pathPAT"] = sam[sample]["pathPAT"].replace("@CFF_LOCALPATDIR@", localBasePathPAT)
            sam[sample]["pathPAT"] = sam[sample]["pathPAT"].rstrip('/')
        if "pathTrees" in sam[sample]:
            sam[sample]["pathTrees"] = sam[sample]["pathTrees"].replace("XXXTMFTTree", localBasePathTrees)
            sam[sample]["pathTrees"] = sam[sample]["pathTrees"].replace("@CFF_LOCALTreeDIR@", localBasePathTrees)
            sam[sample]["pathTrees"] = sam[sample]["pathTrees"].rstrip('/')
    return sam



def getAnaDefinition(varname, toGlobal=False):
    variant = getVariant()
    command = "from " + variant + " import " + varname
    if toGlobal:
        exec(command, globals(), globals())
    else:
        exec(command)
    obj = eval(varname)
    return fixLocalPaths(obj)




def preventExit():
    print " "
    py3 = sys.version_info[0] > 2 #creates boolean value for test that Python major version > 2
    if py3:
        response = input("Press enter to exit ")
    else:
        response = raw_input("Press enter to exit ")
    return 1



def getFileListGFAL(path, subdir=''):
    ret = []
    cnt = 0
    if not  distutils.spawn.find_executable("gfal-ls"):
        print ("Cannot find gfal-ls executable. Check your grid environment!")
        sys.exit(1)
    command = ["gfal-ls", "-a", path.rstrip('/') + '/' + subdir]
    lineCnt = 0
    print "Obtaining file list for ", path.rstrip('/') + '/' + subdir, " with gfal"
    proc = subprocess.Popen(command, stdout=subprocess.PIPE)
    for read_line in iter(proc.stdout.readline, ''):
        lineCnt += 1
        line =  read_line.strip()
        if ("fail" in line): continue
        if ("/log" in line): continue
        fname = line.split("/")[-1]
        if not fname.endswith(".root"):
            # could be directory...
            ret2 = getFileListGFAL(path, fname)
            ret += ret2
            cnt += len(ret2)
            continue
        srcFile = subdir
        if (subdir!=''):
            srcFile += '/'
        srcFile += fname
        cnt += 1
        ret.append(srcFile)
    if lineCnt < 1:
        err = "Cannot get filelist for  " + path + "\n"
        err += " - if  some files were copied allready this probably means some server related problems."
        err += " Please retry in couple of minutes. \n"  
        err += " - if none of the files were copied please check your certificate proxy.\n"
        print err
    print ("Found " + str(len(ret)) + " files ")
    return ret
