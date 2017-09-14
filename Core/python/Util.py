import os, sys, subprocess, imp



def getCrabVersion():
    try:
        #ver=subprocess.check_output(["crab", "--version"])#,, "v3"
        # python 2.6 compat
        p = subprocess.Popen(["crab", "--version"], stdout=subprocess.PIPE)
        ver = p.communicate()[0]
    except OSError:
        raise Exception("Seems that crab environment is not defined. Exit... stage left")
    ret = 2
    if "v3" in ver:
        ret = 3 
    return ret



def getVariant():
    if  "SmallXAnaVersion" not in  os.environ:
        m = " Cannot get ana variant from env. Set SmallXAnaVersion "
        m += "to desired value (e.g. by sourcing one of files from CommonFSQFramework.Core/env/ directory) "
        raise Exception(m)
    variant = os.environ["SmallXAnaVersion"]
    return variant



def getFullPathToAnaDefinitionFile():
    variant = getVariant()
    command = "import "+variant+" as tmpxxx"
    exec command
    return tmpxxx.__file__



def getAnaDefinition(varname, toGlobal=False):
    variant = getVariant()
    command = "from "+variant+" import "+varname
    if toGlobal:
        exec(command, globals(), globals())
    else:
        exec(command)
    obj = eval(varname)
    return obj



def getROOTPrefix():
    if "SmallXAnaDefFile" not in os.environ:
        print "Please set SmallXAnaDefFile environment variable:"
        print "export SmallXAnaDefFile=FullPathToFile"
        raise Exception("Whooops! SmallXAnaDefFile env var not defined")
    anaDefFile = os.environ["SmallXAnaDefFile"]
    mod_dir, filename = os.path.split(anaDefFile)
    mod, ext = os.path.splitext(filename)
    f, filename, desc = imp.find_module(mod, [mod_dir])
    mod = imp.load_module(mod, f, filename, desc)    
    return mod.ROOTPrefix



def getTTreeBasePath():
    if "SmallXAnaDefFile" not in os.environ:
        print "Please set SmallXAnaDefFile environment variable:"
        print "export SmallXAnaDefFile=FullPathToFile"
        raise Exception("Whooops! SmallXAnaDefFile env var not defined")
    anaDefFile = os.environ["SmallXAnaDefFile"]
    mod_dir, filename = os.path.split(anaDefFile)
    mod, ext = os.path.splitext(filename)
    f, filename, desc = imp.find_module(mod, [mod_dir])
    mod = imp.load_module(mod, f, filename, desc)
    return mod.TTreeBasePATH



def getPATBasePath():
    if "SmallXAnaDefFile" not in os.environ:
        print "Please set SmallXAnaDefFile environment variable:"
        print "export SmallXAnaDefFile=FullPathToFile"
        raise Exception("Whooops! SmallXAnaDefFile env var not defined")
    anaDefFile = os.environ["SmallXAnaDefFile"]
    mod_dir, filename = os.path.split(anaDefFile)
    mod, ext = os.path.splitext(filename)
    f, filename, desc = imp.find_module(mod, [mod_dir])
    mod = imp.load_module(mod, f, filename, desc)

    return mod.PATbasePATH



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
        raise Exception("Cannot find gfal-ls executable. Check your grid environment!")
    command = ["gfal-ls", "-a", path + subdir]
    lineCnt = 0
    print "Obtaining file list for ", path, " with gfal"
    proc = subprocess.Popen(command, stdout=subprocess.PIPE)
    for line in iter(proc.stdout.readline,''):
        lineCnt += 1
        l =  line.strip()
        fname = l.split("/")[-1]
        if not fname.endswith(".root"):
            # could be directory...
            ret2 = getFileListGFAL(path, '/' + fname)
            ret += ret2
            cnt += len(ret2)
            continue
        srcFile = path + "/" + fname
        cnt += 1
        ret.append(srcFile)
    if lineCnt < 1:
        err = "Cannot get filelist for  " + path + "\n"
        err += " - if  some files were copied allready this probably means some server related problems."
        err += " Please retry in couple of minutes. \n"  
        err += " - if none of the files were copied please check your certificate proxy.\n"
        print err
#        raise Exception(err)
    return ret
