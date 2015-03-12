import ROOT
ROOT.gROOT.SetBatch(True)

def getHistos(infile):
    if isinstance(infile, basestring):
        f = ROOT.TFile(infile, "r")
        lst = f.GetListOfKeys()
    else: # handle TDirectory
        lst = infile.GetListOfKeys()

    finalMap = {}
    targetsToSamples = {}


    for l in lst:
        currentDir = l.ReadObj()
        if not currentDir:
            print "Problem reading", l.GetName(), " - skipping"
            continue
        if type(currentDir) != ROOT.TDirectoryFile:
            print "Expected TDirectoryFile,", type(currentDir), "found"
            continue

        target =  l.GetName()#.replace("_j15", "_jet15")
        dirContents = currentDir.GetListOfKeys()
        for c in dirContents:
            curObj = c.ReadObj()
            curObjName = curObj.GetName()
            clsname = curObj.ClassName()
            if not clsname.startswith("TH") and not curObjName.startswith("response_"): 
                #print "Skip: ", curObj.GetName(), clsname, target
                continue

            #print "Found", curObj.GetName(), target
            curObjClone = curObj.Clone()
            if clsname.startswith("TH"):
                curObjClone.SetDirectory(0)
            finalMap.setdefault(target, {})
            targetsToSamples.setdefault(target, set()) # keep empty
            if curObjClone.GetName() in finalMap[target]:
                finalMap[target][curObjClone.GetName()].Add(curObjClone)
            else:
                finalMap[target][curObjClone.GetName()] = curObjClone
    return finalMap
