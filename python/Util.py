import os

def getVariant():
    if  "SmallXAnaVersion" not in  os.environ:
        m = " Cannot get ana variant from env. Set SmallXAnaVersion "
        m += "to desired value (e.g. by sourcing one of files from MNTriggerStudies/MNTriggerAna/env/ directory) "
        raise Exception(m)

    variant = os.environ["SmallXAnaVersion"]
    return variant


def getAnaDefinition(varname, toGlobal=False):
    variant = getVariant()
    command = "from "+variant+" import "+varname
    if toGlobal:
        exec(command, globals(), globals())
    else:
        exec(command)

    obj = eval(varname)

    return obj


