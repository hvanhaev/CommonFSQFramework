#! /usr/bin/env python

import os
import fnmatch



#todoSteps = ["proof", "hadd", "draw", "unfold", "merge"]
#todoCat = ["InclusiveBasic", "InclusiveAsym", "InclusiveWindow", "MNBasic", "MNAsym", "MNWindow"]
#todoCat = ["InclusiveBasic", "InclusiveAsym", "InclusiveWindow", "MNBasic", "MNAsym", "MNWindow", "FWD11_002"]
#todoCat = ["InclusiveBasic"]
#todoCat = ["MNAsym"]
todoCat = ["MNWindow"]
#todoCat = ["FWD11_002"]
#todoCat = ["InclusiveBasic"]
todoSteps = []
#todoSteps.append("proof")
todoSteps.append("simpleMCplots")
#todoSteps.append("hadd")
#todoSteps.append("draw")
#todoSteps.append("unfold")
#todoSteps.append("merge")

for cat in todoCat:
    for step in todoSteps:
        if step == "proof":
            os.system("./MNxsAnalyzerClean.py -v {}".format(cat))

        elif step == "draw":
            command="./mnDraw.py -i plotsMNxs_XXS.root -o ~/tmp/MNXS_XXS_detectorLevel_XXM/ -v XXM"
            os.system(command.replace("XXS", cat).replace("XXM", "herwig"))
            os.system(command.replace("XXS", cat).replace("XXM", "pythia"))
        elif step == "hadd":
            target = "plotsMNxs_{}.root".format(cat)
            os.system("rm "+target)
            infiles = []
            for file in os.listdir('.'):
                if fnmatch.fnmatch(file, 'plotsMNxs_{}_*.root'.format(cat)):
                    infiles.append(file)
            os.system("./hadd.py " + target + " " + " ".join(infiles) )
        elif step == "simpleMCplots":
            todo=["ptHat"]
            samples = ["QCD_Pt-15to3000_TuneZ2star_Flat_HFshowerLibrary_7TeV_pythia6", "QCD_Pt-15to1000_TuneEE3C_Flat_7TeV_herwigpp"]
            triggers = ["jet15", "dj15fb"]
            for t in todo:
                os.system("../simpleMCplots.py -a {0},{1} -b {0},{2} -v {3}".format(t,samples[0], samples[1], cat))
                #os.system("../simpleMCplots.py -d -a {0},{1} -b {0},{2} -v {3}".format(t,samples[0], samples[1], cat))

            ptypes = ["fake" , "miss"]
            for ptype in ptypes:
                for s in samples:
                    for trg in triggers:
                        if ptype == "fake":
                            nom = "fakeresponse_central_{}".format(trg)
                            denom =  "measuredresponse_central_{}".format(trg)
                        elif ptype == "miss":
                            nom = "miss_central_{}".format(trg)
                            denom =  "truthresponse_central_{}".format(trg)

                        command = "../simpleMCplots.py -d -a {1},{0} -b {2},{0} -v {3}".format(s, nom, denom,cat)
                        label = "pythia"
                        if label not in s: label = "herwig"
                        command += " -l "+label
                        os.system(command)



        elif step == "unfold":
            os.system("./unfoldMN.py -v {}".format(cat))
        elif step == "merge":
            if cat == "FWD11_002":
                os.system("./mergeUnfoldedResult.py -v {} -n xs  -b -s 5.6".format(cat))
            else:
                os.system("./mergeUnfoldedResult.py -v {} -n xs".format(cat))
                os.system("./mergeUnfoldedResult.py -v {} -n area".format(cat))
