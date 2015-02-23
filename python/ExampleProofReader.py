#!/usr/bin/env python
###############################################################################
#
#  TODO: 
#   1. Select output root file when calling runAll
#   2. Same for datasets
#   4. Fetch generator weight, create histos with sumw
#   5. Add protection agains returning anything different than 1/0 from process
#
###############################################################################
#
# Example proof reader of trees produced with framework. This script reads
#  trees produced by ExampleTreeProducer. During execution pt of the leading
#  jet is read in two ways - from float tree branch (leadJetPt) and by using
#  collection of all jets momenta saved in pfJets branch.
#
#  Two histograms are produced - distribution of pt of leading jet and ratio
#   of pt obtained from both methods
#
#   Additional notes:
#
#     1. change "workers" parameter to run on more cores
#     2. This script needs to be called from a directory where it is placed, 
#        (that is by typing ExampleProofReader.py). You can use symbolic 
#        link to overcome this
#     3.  Histos will be saved in ~/tmp/plots.root (this is currently 
#         hardcoded, change if needed)
#     4. You can see proof execution logs under  
#
#           ~/.proof/<long string coresponding to your directory name>/last-lite-session/worker-0.0.log
#
#         Your print statements will go there. 
#
#     5. Debugging proof analyzer (ie this analyzer) is often difficult, since
#        you dont see err messages (not even in file above). Often the only 
#        way is to comment/uncomment suspected parts of code and see if crash
#        persists
#       
#     6. Often problems are caused by having a bare return statement (without a 
#        value) in Process function. You should always return 1 (0 value is 
#        is used once, see below and dont touch :) )
#
#
###############################################################################

import sys, os, time, traceback
sys.path.append(os.path.dirname(__file__))
import ROOT
ROOT.gROOT.SetBatch(True)

from array import *

from MNTriggerStudies.MNTriggerAna.GetDatasetInfo import getTreeFilesAndNormalizations
import MNTriggerStudies.MNTriggerAna.Util


# please note that python selector class name (here: ExampleProofReader) 
# should be consistent with this file name (ExampleProofReader.py)
#from ROOT import TPySelector
class ExampleProofReader( ROOT.TPySelector ):
    uniqueEnvString = "TMFTMFqWeRtY_"

    @classmethod
    def encodeEnvString(cls, s):
        return s+cls.uniqueEnvString

    @classmethod
    def decodeEnvString(cls, s):
        spl = s.split(cls.uniqueEnvString)
        if len(spl)!=1:
            err = "Cannot env decode:", s
            print err
            sys.stdout.flush()
            raise Exception(err)
        return spl[0]

    def getVariables(self):
        #self.dsName = ROOT.gSystem.Getenv("TMFDatasetName")
        variablesToFetch = ROOT.gSystem.Getenv(self.encodeEnvString("VariablesToFetch") )
        #print variablesToFetch
        split = variablesToFetch.split(",")
        for s in split:
            attrRaw = ROOT.gSystem.Getenv(self.encodeEnvString(s))
            #print s, attr
            attrSpl = attrRaw.split(";;;")
            print s, attrSpl
            attr = attrSpl[0]
            attrType = attrSpl[1]

            if attrType == "int":
                setattr(self, s, int(attr))
            elif attrType == "float":
                setattr(self, s, float(attr))
            elif attrType == "str":
                setattr(self, s, attr)
            elif attrType == "bool":
                if attr == "True":
                    setattr(self, s, True)
                elif attr == "False":
                    setattr(self, s, False)
                else:
                    print "Cannot set bool attribute", s, "from", attr
            else:
                print "Dont know what to do with", s, attrType
            
        #print "XXX1", self.YODA, self.LUKE, self.VADER, self.LEIA, self.LEIA2



    def Begin( self ):
        #print 'py: beginning'
        self.getVariables()

    def SlaveBegin( self, tree ):
        #print 'py: slave beginning'
        try:
            self.getVariables() # needed for 
        except:
            print "Exception catched during worker configuration. Traceback:"
            traceback.print_exc(file=sys.stdout)
            sys.stdout.flush()

        if self.useProofOFile:
            self.newStyleOutputList = []
            curPath = ROOT.gDirectory.GetPath()
            bigFileName = self.outFile.replace(".root","")+"_"+ self.datasetName+".root"
            self.proofFile=ROOT.TProofOutputFile(bigFileName,"M")
            self.oFileViaPOF = self.proofFile.OpenFile("RECREATE") 
            self.outDirViaPOF = self.oFileViaPOF.mkdir(self.datasetName)

            ROOT.gDirectory.cd(curPath)

        try:
            self.init() 
        except:
            print "Exception catched during worker configuration. Traceback:"
            traceback.print_exc(file=sys.stdout)
            sys.stdout.flush()
            raise Exception("Whooopps!")

    def addToOutput(self, obj):
        if self.useProofOFile:
            self.newStyleOutputList.append(obj)
            # this fixes "inmemory" trees problem
            if "TTree" in obj.ClassName():
                obj.SetDirectory(self.outDirViaPOF)


        else:
            self.GetOutputList().Add(obj)

    # this method will be overridden in derived class
    def init(self):

        self.histograms = {}
        self.ptLeadHisto = ROOT.TH1F("ptLead",   "ptLead",  100, 0, 100)      
        self.ptRatioHisto = ROOT.TH1F("ptRatio", "ptRatio", 100, -0.0001, 10)      
        self.GetOutputList().Add(self.ptLeadHisto)
        self.GetOutputList().Add(self.ptRatioHisto)
        sys.stdout.flush()
    
    # protect from returning None or other nonsense by 
    # putting analysis stuff in separate function
    def Process( self, entry ):
        if self.fChain.GetEntry( entry ) <= 0:
           return 0

        try:
            self.analyze()
        except:
            print "Exception catched from analyze function. Traceback:"
            traceback.print_exc(file=sys.stdout)
            sys.stdout.flush()
            raise Exception("Whooopps!")
        return 1

    # this method will be overridden in derived class
    def analyze(self):
        #event = self.fChain.event
        #run = self.fChain.run
        #lumi = self.fChain.lumi
        #print event

        weight = 1. # calculate your event weight here

        leadJetPtFromFloatBranch = self.fChain.leadJetPt

        pfJetsMomenta = self.fChain.pfJets
        leadJetPtFromVectorBranch = 0
        # once again we will exploit the fact, that jets should be pt ordered
        if pfJetsMomenta.size() > 0: # note: here we are accessing size method from c++ std::vector. You can use any method..
            leadJetPtFromVectorBranch = pfJetsMomenta.at(0).pt()

        if leadJetPtFromVectorBranch != 0 and leadJetPtFromFloatBranch !=0:
            ratio = leadJetPtFromVectorBranch/leadJetPtFromFloatBranch
            self.ptRatioHisto.Fill(ratio, weight)
        elif leadJetPtFromVectorBranch != leadJetPtFromFloatBranch:
            self.ptRatioHisto.Fill(0, weight)

        #for j in pfJetsMomenta: # iterate over all jets:
        #    print j.pt()
        #print "XX",leadJetPtFromFloatBranch, leadJetPtFromVectorBranch

        if leadJetPtFromVectorBranch > 0:
           self.ptLeadHisto.Fill( leadJetPtFromVectorBranch, weight)
        return 1

    def SlaveTerminate( self ):
        print 'py: slave terminating'
        try:
            self.finalize()
        except:
            print ""
            print ""
            print "Exception catched in finalize function. Traceback:"
            print ""
            traceback.print_exc(file=sys.stdout)
            print ""
            print ""
            print ""
            sys.stdout.flush()
            raise Exception("Whooopps!")

        if self.oFileViaPOF:
            curPath = ROOT.gDirectory.GetPath()
            self.outDirViaPOF.cd()
            for o in self.newStyleOutputList:
                o.Write()
            self.oFileViaPOF.cd()
            self.oFileViaPOF.Write()
            self.GetOutputList().Add(self.proofFile)
            ROOT.gDirectory.cd(curPath)



    def finalize(self):
        print "finalize function called from base class. You may want to implement this."

    def finalizeWhenMerged(self):
        print "finalizeWhenMerged function called from base class. You may want to implement this."


    def getNormalizationFactor(self):
        if self.isData:
            return 1.
        else:
            return self.normalizationFactor

    def checkUnderOverFlow(self):
        print "Checking for possible under - and overflow problems in your histograms..."
        olist = self.GetOutputList()
        problems = False
        for o in olist:
            if not "TH1" in o.ClassName(): continue
            grandeTotale =  o.GetBinContent(o.GetNbinsX()+1)+ o.GetBinContent(0)+o.Integral()
            if grandeTotale == 0: continue
            if o.GetBinContent(o.GetNbinsX()+1) != 0:
                print "!!WARNING!! histogram", o.GetName(), "has overflow ==> fraction of events in overflow bin:", \
                    (o.GetBinContent(o.GetNbinsX()+1)/grandeTotale)*100, "%"
                problems = True
            if o.GetBinContent(0) != 0:
                print "!!WARNING!! histogram", o.GetName(), "has underflow ==> fraction of events in underflow bin:", \
                    (o.GetBinContent(0)/grandeTotale)*100, "%"
                problems = True

        if not problems: print "everything is fine!"

    def Terminate( self ): # executed once on client

        try:
            self.checkUnderOverFlow()
        except:
            print ""
            print ""
            print "Exception catched in checkUnderOverFlow function. Traceback:"
            print ""
            traceback.print_exc(file=sys.stdout)
            print ""
            print ""
            print ""
            sys.stdout.flush()
            raise Exception("Whooopps!")

        try:
            self.finalizeWhenMerged()
        except:
            print ""
            print ""
            print "Exception catched in finalizeWhenMerged function. Traceback:"
            print ""
            traceback.print_exc(file=sys.stdout)
            print ""
            print ""
            print ""
            sys.stdout.flush()
            raise Exception("Whooopps!")




        #print 'py: terminating' 
        olist =  self.GetOutputList()

        if not self.useProofOFile:
            of = ROOT.TFile(self.outFile, "UPDATE") # TODO - take dir name from Central file
            outDir = of.mkdir(self.datasetName)
            outDir.cd()
            for o in olist:
                o.Write()
            of.Close()

    @classmethod
    def runAll(cls, treeName, outFile, sampleList = None, \
                maxFilesMC=None, maxFilesData=None, \
                slaveParameters = None, nWorkers=None, usePickle=False, useProofOFile = False):


        if slaveParameters == None: # When default param is used reset contents on every call to runAll
            slaveParameters = {}

        cwd = os.getcwd()+"/"
        treeFilesAndNormalizations = getTreeFilesAndNormalizations(maxFilesMC=maxFilesMC, 
                                maxFilesData=maxFilesData, samplesToProcess=sampleList, usePickle=usePickle)

        if sampleList == None:
            todo = treeFilesAndNormalizations.keys() # run them all
        else:
            todo = sampleList

        slaveParameters["useProofOFile"] = useProofOFile


        if not useProofOFile:
            of = ROOT.TFile(outFile,"RECREATE")
            if not of:
                print "Cannot create outfile:", outFile
                sys.exit()
            of.Close() # so we dont mess with file opens during proof ana
        
        slaveParameters["outFile"] = outFile



        skipped = []

        sampleListFullInfo = MNTriggerStudies.MNTriggerAna.Util.getAnaDefinition("sam")
        sampleCnt = 0
        for t in todo:
            sampleCnt += 1
            print "#"*60
            print "Next sample:", t, "("+str(sampleCnt)+"/"+str(len(todo))+")"
            print "#"*60
            if len(treeFilesAndNormalizations[t]["files"])==0:
                print "Skipping, empty filelist for",t
                skipped.append(t)
                continue

            dataset = ROOT.TDSet( 'TTree', 'data', treeName) # the last name is the directory name inside the root file
            for file in treeFilesAndNormalizations[t]["files"]:
                dataset.Add(file)
            
            slaveParameters["datasetName"] = t
            slaveParameters["isData"] = sampleListFullInfo[t]["isData"]
            slaveParameters["normalizationFactor"] =  treeFilesAndNormalizations[t]["normFactor"]

            ROOT.TProof.AddEnvVar("PATH2",ROOT.gSystem.Getenv("PYTHONPATH")+":"+os.getcwd())

            #ROOT.gSystem.Setenv("TMFDatasetName", t)

            supportedTypes = set(["int", "str", "float", "bool"])
            variablesToFetch = ""
            coma = ""

            variablesToSetInProof = {}
            for p in slaveParameters:
                encodedName = cls.encodeEnvString(p)

                # Check if parameter is supported. Adding another type is easy - see
                #       getVariables method
                paramType = slaveParameters[p].__class__.__name__
                if paramType not in supportedTypes:
                    raise Exception("Parameter of type "+paramType \
                          + " is not of currently supported types: " + ", ".join(supportedTypes) )
                ROOT.gSystem.Setenv(encodedName, str(slaveParameters[p])+";;;"+paramType)
                variablesToSetInProof[encodedName] =  str(slaveParameters[p])+";;;"+paramType
                variablesToFetch += coma + p
                coma = ","
            ROOT.gSystem.Setenv(cls.encodeEnvString("VariablesToFetch"), variablesToFetch)
            variablesToSetInProof[cls.encodeEnvString("VariablesToFetch")] = variablesToFetch

            proofConnectionString = None
            if "proofConnectionString" in os.environ:
                proofConnectionString = os.environ["proofConnectionString"]
                print "Found proof environment. Will try to connect to", proofConnectionString

            if not proofConnectionString:
                if nWorkers == None:
                    proof = ROOT.TProof.Open('')
                else:
                    proof = ROOT.TProof.Open('workers='+str(nWorkers))
            else:
                proof = ROOT.TProof.Open(proofConnectionString)

            
            proof.Exec( 'gSystem->Setenv("PYTHONPATH",gSystem->Getenv("PATH2"));') # for some reason cannot use method below for python path
            proof.Exec( 'gSystem->Setenv("PATH", "'+ROOT.gSystem.Getenv("PATH") + '");')
            for v in variablesToSetInProof:  
                # if you get better implemenation (GetParameter?) mail me
                proof.Exec('gSystem->Setenv("'+v+'","'+variablesToSetInProof[v]+'");')
            print dataset.Process( 'TPySelector',  cls.__name__)

            try:
                print "Logs saved to:"
                logs = proof.GetManager().GetSessionLogs().GetListOfLogs()
                for l in logs:
                    print l.GetTitle()
            except:
                print "Cannot get lognames"

            curPath = ROOT.gDirectory.GetPath()

            if useProofOFile:
                bigFileName = outFile.replace(".root","")+"_"+t+".root"
                of = ROOT.TFile(bigFileName,"UPDATE")
            else:
                of = ROOT.TFile(outFile,"UPDATE")

            # Write norm value and other info
            saveDir = of.Get(t)
            if not saveDir:
                print "Cannot get directory from plot file"
                continue
            saveDir.cd()

            norm = treeFilesAndNormalizations[t]["normFactor"]
            hist = ROOT.TH1D("norm", "norm", 1,0,1)
            hist.SetBinContent(1, norm)
            #saveDir.WriteObject(hist, hist.GetName())
            hist.Write(hist.GetName())

            of.Close()
            ROOT.gDirectory.cd(curPath)

            # clean environment
            for v in variablesToSetInProof:  
                #command = 'gSystem->Unsetenv("'+v+'");'
                #print command
                proof.Exec('gSystem->Unsetenv("'+v+'");')

        if len(skipped)>0:
            print "Note: following samples were skipped:"
            for sk in skipped:
                print "  ",sk

        print "Analyzed:"
        done = set(todo)-set(skipped)
        for t in done:
            print t

        if useProofOFile:
            partFiles = []
            for t in done:
                partFiles.append(outFile.replace(".root","")+"_"+t+".root")
            print "Running hadd"
            os.system("hadd -f " + outFile + " " + " ".join(partFiles))

if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    ROOT.gSystem.Load("libFWCoreFWLite.so")
    ROOT.AutoLibraryLoader.enable()

    slaveParams = {}

    #ExampleProofReader.runAll(treeName="exampleTree", outFile = "~/tmp/plots.root")

    '''
    slaveParams["YODA"] = 1234
    slaveParams["LUKE"] = "theForce"
    slaveParams["VADER"] = 3.14
    slaveParams["LEIA"] = True
    slaveParams["LEIA2"] = False
    #'''

    ExampleProofReader.runAll(treeName="exampleTree", maxFilesMC = 10, \
                              slaveParameters=slaveParams, \
                              outFile = "~/tmp/plots.root")
                              
    # '''
