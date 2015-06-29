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
