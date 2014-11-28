#! /usr/bin/env python
import os
indir = "../../../CondFormats/JetMETObjects/data/"


#START42_V16A_L1FastJet_AK5PF.txt
#START42_V16A_AK5Calo_L1FastJet.txt

for dirpath, dirnames, files in os.walk(indir):
    for f in files:
        if not "START42_" in f: continue
        outname = f.replace(".txt","").replace("_AK5PF", "").replace("_AK5Calo","")
        if "_AK5Calo" in f:
            outname += "_AK5Calo.txt"
        elif "_AK5PF" in f:
            outname += "_AK5PF.txt"
        else:
            raise ""

        os.system("cp " + dirpath+f + " " + dirpath+outname)


