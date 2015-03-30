#!/usr/bin/env python
import MNTriggerStudies.MNTriggerAna.ExampleProofReader
from  MNTriggerStudies.MNTriggerAna.RecoTracksGetter import RecoTracksGetter
from  MNTriggerStudies.MNTriggerAna.RecoVertexGetter import RecoVertexGetter
from  MNTriggerStudies.MNTriggerAna.GenTracksGetter import GenTracksGetter

import sys, os, time, math
sys.path.append(os.path.dirname(__file__))

import ROOT
ROOT.gROOT.SetBatch(True)

class CSA14_dndeta(MNTriggerStudies.MNTriggerAna.ExampleProofReader.ExampleProofReader):
    def init( self):
        self.triggers   = ["minbias"]
        self.variations = ["central"] # only a central value now
        
        self.hist = {}
        for t in self.triggers:
            for v in self.variations:
                histPostfix = "_" + v + "_" + t
				# gen level histos
                self.hist["numGenTracks"+histPostfix] =  ROOT.TH1F("numGenTracks"+histPostfix,   "numGenTracks"+histPostfix,  150, 0, 150)
                self.hist["etaGenTracks"+histPostfix] =  ROOT.TH1F("etaGenTracks"+histPostfix,   "etaGenTracks"+histPostfix,  24, -2.4, 2.4)
                self.hist["phiGenTracks"+histPostfix] =  ROOT.TH1F("phiGenTracks"+histPostfix,   "phiGenTracks"+histPostfix,  25, -math.pi, math.pi)
                self.hist["ptGenTracks"+histPostfix] =  ROOT.TH1F("ptGenTracks"+histPostfix,   "ptGenTracks"+histPostfix,  120, 0, 6)
                self.hist["pdgIDGenTracks"+histPostfix] =  ROOT.TH1F("pdgIDGenTracks"+histPostfix,   "pdgIDGenTracks"+histPostfix,  100, -50, 50)
				# reco level histos
                self.hist["numRecoTracks"+histPostfix] =  ROOT.TH1F("numRecoTracks"+histPostfix,   "numRecoTracks"+histPostfix,  150, 0, 150)
                self.hist["etaRecoTracks"+histPostfix] =  ROOT.TH1F("etaRecoTracks"+histPostfix,   "etaRecoTracks"+histPostfix,  24, -2.4, 2.4)
                self.hist["phiRecoTracks"+histPostfix] =  ROOT.TH1F("phiRecoTracks"+histPostfix,   "phiRecoTracks"+histPostfix,  25, -math.pi, math.pi)
                self.hist["ptRecoTracks"+histPostfix] =  ROOT.TH1F("ptRecoTracks"+histPostfix,   "ptRecoTracks"+histPostfix,  100, 0, 1000)
                self.hist["dzRecoTracks"+histPostfix] =  ROOT.TH1F("dzRecoTracks"+histPostfix,   "dzRecoTracks"+histPostfix,  100, -200, 200)
                self.hist["d0RecoTracks"+histPostfix] =  ROOT.TH1F("d0RecoTracks"+histPostfix,   "d0RecoTracks"+histPostfix,  100, -200, 200)

                self.hist["numgoodRecoVertex"+histPostfix] =  ROOT.TH1F("numgoodRecoVertex"+histPostfix,   "numgoodRecoVertex"+histPostfix,  10, 0, 10)
                self.hist["nTracksRecoVertex"+histPostfix] =  ROOT.TH1F("nTracksRecoVertex"+histPostfix,   "nTracksRecoVertex"+histPostfix,  50, 0, 200)
                self.hist["zRecoVertex"+histPostfix] =  ROOT.TH1F("zRecoVertex"+histPostfix,   "zRecoVertex"+histPostfix,  60, -30, 30)
                self.hist["rhoRecoVertex"+histPostfix] =  ROOT.TH1F("rhoRecoVertex"+histPostfix,   "rhoRecoVertex"+histPostfix, 20, 0, 5)
                self.hist["ndofRecoVertex"+histPostfix] =  ROOT.TH1F("ndofRecoVertex"+histPostfix,   "ndofRecoVertex"+histPostfix,  300, 0, 300)

        for h in self.hist:
            self.hist[h].Sumw2()
            self.GetOutputList().Add(self.hist[h])

        self.tracks = RecoTracksGetter("recoTracks")
        self.vertices = RecoVertexGetter("vtx")
        self.genparts = GenTracksGetter("genTracks")

    def analyze(self):
        weight = 1 # 
        # weight = self.fChain.genWeight to obtain gen level weight. For min bias datasets we are using for CSA14 always eq to 1

        # initialize event record
        self.tracks.newEvent(self.fChain)
        self.vertices.newEvent(self.fChain)
        self.genparts.newEvent(self.fChain)

        # iterate over all triggers we use
        for trg in self.triggers:

            # iterate over all variations
            for variation in self.variations: 
                histPostfix = "_" + variation + "_" + trg
				
				# before event selection, fill vertex histos
                numgoodvtx = 0
                for vtx in self.vertices.get(variation):
                    vtxrho = math.sqrt(vtx.x*vtx.x + vtx.y*vtx.y)
                    self.hist["nTracksRecoVertex"+histPostfix].Fill(vtx.nTracks, weight)
                    self.hist["zRecoVertex"+histPostfix].Fill(vtx.z, weight)
                    self.hist["rhoRecoVertex"+histPostfix].Fill(vtxrho, weight)
                    self.hist["ndofRecoVertex"+histPostfix].Fill(vtx.ndof, weight)
                    if not vtx.isFake and abs(vtx.z) <= 15 and vtx.ndof >= 4 and vtxrho <= 2: # count only good primary vertices
                        numgoodvtx+=1
						
                self.hist["numgoodRecoVertex"+histPostfix].Fill(numgoodvtx, weight)
				
				# trigger and event selection
                trigger = False
                if trg == "minbias":
                    if numgoodvtx == 1: trigger = True # trigger on exactly one good primary vertex
 			
                if not trigger: continue

                if not self.isData:
				    # fill gen histos
                    numgen = 0
                    for genpart in self.genparts.get(variation):
                        genpartp4 = genpart.genTracks # wrong naming in Samples_CSA14_Tracks_20140904 skim, should become genpartp4 = genpart.p4 in next version
                        if genpartp4.pt() > 0.5 and abs(genpartp4.eta()) < 2.4 and genpart.charge != 0 and genpart.status == 1:
                            numgen+=1
                            self.hist["etaGenTracks"+histPostfix].Fill(genpartp4.eta(), weight)
                            self.hist["phiGenTracks"+histPostfix].Fill(genpartp4.phi(), weight)
                            self.hist["ptGenTracks"+histPostfix].Fill(genpartp4.pt(), weight)
                            self.hist["pdgIDGenTracks"+histPostfix].Fill(genpart.pdg, weight)
				
                    self.hist["numGenTracks"+histPostfix].Fill(numgen, weight)
				
				# fill reco histos
                numreco = 0
                for track in self.tracks.get(variation):
                    trackp4 = track.recoTracks # wrong naming in Samples_CSA14_Tracks_20140904 skim, this will evolve to trackp4 = track.p4 in next version
                    if trackp4.pt() > 0.5 and abs(trackp4.eta()) < 2.4 and track.highpurity == True:
                        numreco+=1
                        self.hist["etaRecoTracks"+histPostfix].Fill(trackp4.eta(), weight)
                        self.hist["phiRecoTracks"+histPostfix].Fill(trackp4.phi(), weight)
                        self.hist["ptRecoTracks"+histPostfix].Fill(trackp4.pt(), weight)
                        self.hist["dzRecoTracks"+histPostfix].Fill(track.dz, weight)
                        self.hist["d0RecoTracks"+histPostfix].Fill(track.d0, weight)

                self.hist["numRecoTracks"+histPostfix].Fill(numreco, weight)

    # note: this is executed on the slave (ie output will appear in logs),
    #       - before merging the histograms. Here we should apply the histogram 
    #         normalization factor (since this depend on how many events were processed
    #         by given slave)
    def finalize(self):
        print "Finalize:"
        normFactor = self.getNormalizationFactor()
        print "  isData", self.isData
        print "  normFactor",  normFactor
        #print "  perfect, but now just normalize to integral to have more robust shape comparisons"
        #for h in self.hist:
        #    self.hist[h].Scale(1./self.hist[h].Integral())

    # this is executed once at the master after merging the histograms from slaves
    # (note: all histograms registered via self.GetOutputList().Add above are merged)
    def finalizeWhenMerged(self):
        #olist =  self.GetOutputList() # rebuild the histos list
        #histos = {}
        #for o in olist:
        #    if not "TH1" in o.ClassName(): continue
        #    histos[o.GetName()]=o
        #    print " TH1 histogram in output: ", o.GetName()

        # you can save further histograms to the output file by calling:
        #self.GetOutputList().Add(myNewHisto)
        
        pass


if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    ROOT.gSystem.Load("libFWCoreFWLite.so")
    ROOT.AutoLibraryLoader.enable()

    sampleList = None
    maxFilesMC = None
    maxFilesData = None
    nWorkers = None # Use all cores

    quickTest = True
    
    if quickTest:
        # Run printTTree.py alone to get the samples list
        #sampleList = []
        #sampleList.append("data_MinBias_TuneCUETP8S1-HERAPDF_13TeV-pythia8")
        maxFilesMC = 1
        maxFilesData = 1
        nWorkers = 4

    # only processin part of data will lead to wrong normalization of the data histograms
    # - since lumi values are not automatically updated to reflect the fact that only
    # part of sample was processed
    #
    # This is not a problem for MC, while here normalization factor is calculated using
    # number of processed events


    slaveParams = {}
    slaveParams["maxEta"] = 2.


    # use printTTree.py <sampleName> to see what trees are avaliable inside the skim file
    CSA14_dndeta.runAll(treeName="tracksTree",
                               slaveParameters=slaveParams,
                               sampleList=sampleList,
                               maxFilesMC = maxFilesMC,
                               maxFilesData = maxFilesData,
                               nWorkers=nWorkers,
                               outFile = "plotsCSA14_dndeta.root" )



