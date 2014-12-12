import os, sys, subprocess

def getCrabVersion():
    try:
        #ver=subprocess.check_output(["crab", "--version"])#,, "v3"
        # python 2.6 compat
        p = subprocess.Popen(["crab", "--version"], stdout=subprocess.PIPE)
        ver = p.communicate()[0]


    except OSError:
        raise Exeption("Seems that crab environment is not defined. Exit... stage left")

    ret = 2
    if "v3" in ver:
        ret = 3 

    return ret


def getVariant():
    if  "SmallXAnaVersion" not in  os.environ:
        m = " Cannot get ana variant from env. Set SmallXAnaVersion "
        m += "to desired value (e.g. by sourcing one of files from MNTriggerStudies/MNTriggerAna/env/ directory) "
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


