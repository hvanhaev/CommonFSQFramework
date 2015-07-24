#!/usr/bin/env python
import CommonFSQFramework.Core.ExampleProofReader

import sys, os, time, math
sys.path.append(os.path.dirname(__file__))

import ROOT
ROOT.gROOT.SetBatch(True)
from ROOT import edm, JetCorrectionUncertainty


from array import *

p1="_post"

class CSA14_UEAna(CommonFSQFramework.Core.ExampleProofReader.ExampleProofReader):
    def init( self):
	self.hist = {}
        self.hist_vertex = {}
	self.hist_pre = {}
	self.hist_post = {}
	self.hist_gen = {}
        self.hist_jet = {}
	self.hist_gent = {}
	self.hist_trans = {}
	self.hist_tow = {}
	self.hist_away = {}
	self.hist_gentow = {}
        self.hist_genaway = {}
	self.hist_full_jet = {}
	self.hist_full_tracks = {}
	self.hist_full_genjet = {}
        self.hist_full_gentracks = {}
        self.Trans_SisCon5 = {}
        self.other_SisCon5 = {}
     
	self.hist_full_genjet["fgen_ptSisCone5"] =  ROOT.TH1F("fgen_pt_SisCone5",   "ptTrackJets",  200, 0, 200)
        self.hist_full_genjet["fgen_etaSisCone5"] =  ROOT.TH1F("fgen_eta_SisCone5",   "etaTrackJets",  100 , -5, 5)
        self.hist_full_genjet["fgen_phiSisCone5"] =  ROOT.TH1F("fgen_phi_SisCone5",   "phiTrackJets",  628 , -3.14, 3.14)

        self.hist_full_gentracks["fgen_trackPt"] =  ROOT.TH1F("fgen_tracksPt",   "tracksPt",  5000, 0, 500)

        self.hist_full_jet["f_ptSisCone5"] =  ROOT.TH1F("f_pt_SisCone5",   "ptTrackJets",  200, 0, 200)
        self.hist_full_jet["f_etaSisCone5"] =  ROOT.TH1F("f_eta_SisCone5",   "etaTrackJets",  100 , -5, 5)
        self.hist_full_jet["f_phiSisCone5"] =  ROOT.TH1F("f_phi_SisCone5",   "phiTrackJets",  628 , -3.14, 3.14
)

        self.hist_full_tracks["f_trackPt"] =  ROOT.TH1F("f_trackPt",   "tracksPt",  5000, 0, 500)


        #p = "_central_B" # a placeholder for different triggers ("B") and uncertainty variations
                         #  "central" means this is a central value (ie no variations were applied)
        self.hist_vertex["nVtx"] =  ROOT.TH1F("nVtx",   "nVtx",  100, 0, 100)
        self.hist_vertex["ndfVtx"] =  ROOT.TH1F("ndfVtx",   "ndfVtx",  100, 0, 100)
	self.hist_vertex["gen_nJets"] = ROOT.TH1F("gen_nJets",   "nJets",  100, 0, 100)
	self.hist_vertex["nJets"] = ROOT.TH1F("nJets",   "nJets",  100, 0, 100)
#######        
	self.hist_pre["trackD0"] =  ROOT.TH1F("tracksD0",   "tracksD0",  2000, -10, 10)
 	self.hist_pre["trackD0Err"] =  ROOT.TH1F("tracksD0Err",   "tracksD0Err",  1000, 0, 10)
        self.hist_pre["trackD0Significance"] =  ROOT.TH1F("tracksD0Significance",   "tracksD0Sig",  2000, -100, 100)
	self.hist_pre["trackDz"] =  ROOT.TH1F("tracksDz",   "tracksDz",  20000, -100 , 100)
        self.hist_pre["trackDzErr"] =  ROOT.TH1F("tracksDzErr",   "tracksDzErr",  1000, 0, 10)
        self.hist_pre["trackDzSignificance"] =  ROOT.TH1F("tracksDzSignificance",   "tracksDzSig",  2000, -100, 100)

        self.hist_pre["trackPt"] =  ROOT.TH1F("tracksPt",   "tracksPt",  5000, 0, 500) 
	self.hist_pre["trackPtErr"] =  ROOT.TH1F("tracksPtErr",   "tracksPtErr",  5000, 0, 50)	
        self.hist_pre["trackPtSigma"] =  ROOT.TH1F("tracksPtSigma",   "tracksPtSigma",  5000, 0, 50)

	self.hist_pre["trackEta"] =  ROOT.TH1F("tracksEta",   "tracksEta",  100, -5, 5)
	self.hist_pre["trackPhi"] =  ROOT.TH1F("tracksPhi",   "tracksPhi",  628, -3.14, 3.14)
        self.hist_pre["trackDeltaPhi"] =  ROOT.TH1F("tracksDeltaPhi",   "tracksDeltaPhi",  62800, -3.14, 3.14)

	self.hist_pre["purity"] =  ROOT.TH1F("purity",   "purity",  2, 0., 2)
	self.hist_pre["imp0"] =  ROOT.TH1F("imp0",   "imp0",  2, 0., 2)
	self.hist_pre["impz"] =  ROOT.TH1F("impz",   "impz",  2, 0., 2)
	self.hist_pre["dpt"] =  ROOT.TH1F("dpt",   "dpt",  2, 0., 2)
	self.hist_pre["kin"] =  ROOT.TH1F("kin",   "kin",  2, 0., 2)
######
        self.hist_post["trackD0"+p1] =  ROOT.TH1F("tracksD0"+p1,   "tracksD0",  2000, -10, 10)
        self.hist_post["trackD0Err"+p1] =  ROOT.TH1F("tracksD0Err"+p1,   "tracksD0Err",  1000, 0, 10)
        self.hist_post["trackD0Significance"+p1] =  ROOT.TH1F("tracksD0Significance"+p1,   "tracksD0Sig",  2000, -100, 100)
        self.hist_post["trackDz"+p1] =  ROOT.TH1F("tracksDz"+p1,   "tracksD0",  20000, -100 , 100)
        self.hist_post["trackDzErr"+p1] =  ROOT.TH1F("tracksDzErr"+p1,   "tracksDzErr",  1000, 0, 10)
        self.hist_post["trackDzSignificance"+p1] =  ROOT.TH1F("tracksDzSignificance"+p1,   "tracksDzSig",  2000, -100, 100)

        self.hist_post["trackPt"+p1] =  ROOT.TH1F("tracksPt"+p1,   "tracksPt",  5000, 0, 500) 
        self.hist_post["trackPtErr"+p1] =  ROOT.TH1F("tracksPtErr"+p1,   "tracksPtErr",  5000, 0, 50)      
        self.hist_post["trackPtSigma"+p1] =  ROOT.TH1F("tracksPtSigma"+p1,   "tracksPtSigma",  5000, 0, 50)

        self.hist_post["trackEta"+p1] =  ROOT.TH1F("tracksEta"+p1,   "tracksEta",  100, -5, 5)
        self.hist_post["trackPhi"+p1] =  ROOT.TH1F("tracksPhi"+p1,   "tracksPhi",  628, -3.14, 3.14)
        self.hist_post["trackDeltaPhi"+p1] =  ROOT.TH1F("tracksDeltaPhi"+p1,   "tracksDeltaPhi",  62800, -3.14, 3.14)

	self.hist_gen["gen_trackDeltaPhi"] =  ROOT.TH1F("gen_tracksDeltaPhi",   "tracksDeltaPhi",  62800, -3.14, 3.14)
        self.hist_gen["gen_trackPt"] =  ROOT.TH1F("gen_tracksPt",   "tracksPt",  5000, 0, 500)
	self.hist_gen["gen_trackEta"] =  ROOT.TH1F("gen_tracksEta",   "tracksEta",  100, -5, 5)
        self.hist_gen["gen_trackPhi"] =  ROOT.TH1F("gen_tracksPhi",   "tracksPhi",  628, -3.14, 3.14)

######
	self.hist["gen_ptSisCone5"] =  ROOT.TH1F("gen_pt_SisCone5",   "ptTrackJets",  200, 0, 200)
        self.hist["gen_etaSisCone5"] =  ROOT.TH1F("gen_eta_SisCone5",   "etaTrackJets",  100 , -5, 5)
        self.hist["gen_phiSisCone5"] =  ROOT.TH1F("gen_phi_SisCone5",   "phiTrackJets",  628 , -3.14, 3.14)

        self.hist_jet["ptSisCone5"] =  ROOT.TH1F("pt_SisCone5",   "ptTrackJets",  200, 0, 200)
	self.hist_jet["etaSisCone5"] =  ROOT.TH1F("eta_SisCone5",   "etaTrackJets",  100 , -5, 5)
	self.hist_jet["phiSisCone5"] =  ROOT.TH1F("phi_SisCone5",   "phiTrackJets",  628 , -3.14, 3.14)
	self.hist_jet["nTracksSisCone5"] =  ROOT.TH1F("nTracks_SisCone5",   "nTracks_TracksJets",  100 , 0, 100)

	self.hist["gen_nJetTracks"] =  ROOT.TH1F("gen_nJetTracks",   "nTracks_TracksJets",  100 , 0, 100)

#	self.hist["ptSisCone7"] =  ROOT.TH1F("pt_SisCone7",   "ptTrackJets",  20, 0, 20)

#        self.hist["ptak5"] =  ROOT.TH1F("pt_ak5",   "ptTrackJets",  20, 0, 20)
#        self.hist["ptak7"] =  ROOT.TH1F("pt_ak7",   "ptTrackJets",  20, 0, 20) 
  
	self.hist["gen_nTot_SisCone5"] = ROOT.TH2F("gen_nTot_SisCone5",   "n_tot",  800, -0.5,799.5,400, 0, 200)
	self.hist_gent["gen_nTrans_SisCone5"] = ROOT.TH2F("gen_nTrans_SisCone5",   "n_trans",  80,-0.5,79.5,400, 0, 200)
        self.hist_gent["gen_ptTrans_SisCone5"] = ROOT.TH2F("gen_ptTrans_SisCone5",   "n_trans",  400, 0.,40.,400, 0, 200)
	self.hist_gent["gen_nTransMax_SisCone5"] = ROOT.TH2F("gen_nTransMax_SisCone5",   "n_trans",  80, -0.5,79.5,400, 0, 200)
        self.hist_gent["gen_ptTransMax_SisCone5"] = ROOT.TH2F("gen_ptTransMax_SisCone5",   "n_trans",  400, 0.,40.,400, 0, 200)

        self.hist_gent["gen_nTransMin_SisCone5"] = ROOT.TH2F("gen_nTransMin_SisCone5",   "n_trans",  80, -0.5,79.5,400, 0, 200)
        self.hist_gent["gen_ptTransMin_SisCone5"] = ROOT.TH2F("gen_ptTransMin_SisCone5",   "n_trans",  400, 0.,40.,200, 0, 100) 

        self.hist_gent["gen_nTransDiff_SisCone5"] = ROOT.TH2F("gen_nTransDiff_SisCone5",   "n_trans",  160, -80.5,79.5,400, 0, 200)
        self.hist_gent["gen_ptTransDiff_SisCone5"] = ROOT.TH2F("gen_ptTransDiff_SisCone5",   "n_trans",  160, -80.5,79.5,200, 0, 100)


        self.hist_genaway["gen_nAway_SisCone5"] = ROOT.TH2F("gen_nAway_SisCone5",   "n_away",  80, -0.5,79.5,200, 0, 100)
        self.hist_genaway["gen_ptAway_SisCone5"] = ROOT.TH2F("gen_ptAway_SisCone5",   "pt_away",  1000, 0.,10.,200, 0, 100)

        self.hist_gentow["gen_nTow_SisCone5"] = ROOT.TH2F("gen_nTow_SisCone5",   "n_tow",  80, -0.5,79.5,200, 0, 100)
        self.hist_gentow["gen_ptTow_SisCone5"] = ROOT.TH2F("gen_ptTow_SisCone5",   "pt_tow",  80, -0.5,79.5,200, 0, 100)


        self.hist_jet["nTot_SisCone5"] = ROOT.TH2F("nTot_SisCone5",   "n_tot",  800, -0.5,799.5,400, 0, 200)

	self.hist_trans["nTrans_SisCone5"] = ROOT.TH2F("nTrans_SisCone5",   "n_trans",  80, -0.5,79.5,400, 0, 200)
        self.hist_trans["ptTrans_SisCone5"] = ROOT.TH2F("ptTrans_SisCone5",   "pt_trans",  400, 0.,40.,200, 0, 100)
	
	self.hist_trans["nTransMax_SisCone5"] = ROOT.TH2F("nTransMax_SisCone5",   "n_trans",  80, -0.5,79.5,400, 0, 200)
        self.hist_trans["ptTransMax_SisCone5"] = ROOT.TH2F("ptTransMax_SisCone5",   "pt_trans",  400, 0.,40.,200, 0, 100)
	
	self.hist_trans["nTransMin_SisCone5"] = ROOT.TH2F("nTransMin_SisCone5",   "n_trans",  80, -0.5,79.5,400, 0, 200)
        self.hist_trans["ptTransMin_SisCone5"] = ROOT.TH2F("ptTransMin_SisCone5",   "pt_trans",  400, 0.,40.,200, 0, 100)		

        self.hist_trans["nTransDiff_SisCone5"] = ROOT.TH2F("nTransDiff_SisCone5",   "n_trans",  160, -80.5,79.5,400, 0, 200)
        self.hist_trans["ptTransDiff_SisCone5"] = ROOT.TH2F("ptTransDiff_SisCone5",   "pt_trans",  160, -80.,80.,200, 0, 100)

        self.hist_away["nAway_SisCone5"] = ROOT.TH2F("nAway_SisCone5",   "n_away",  80, -0.5,79.5,200, 0, 100)
        self.hist_away["ptAway_SisCone5"] = ROOT.TH2F("ptAway_SisCone5",   "pt_away",  1000, 0.,10.,200, 0, 100)

        self.hist_tow["nTow_SisCone5"] = ROOT.TH2F("nTow_SisCone5",   "n_tow",  80, -0.5,79.5,200, 0, 100)
        self.hist_tow["ptTow_SisCone5"] = ROOT.TH2F("ptTow_SisCone5",   "pt_tow",  1000, 0.,10.,200, 0, 100)

        for h in self.hist:
            self.hist[h].Sumw2()
            self.GetOutputList().Add(self.hist[h])
	for h in self.hist_vertex:
            self.hist_vertex[h].Sumw2()
            self.GetOutputList().Add(self.hist_vertex[h])
	for h in self.hist_gen:
            self.hist_gen[h].Sumw2()
            self.GetOutputList().Add(self.hist_gen[h])
	for h in self.hist_gent:
            self.hist_gent[h].Sumw2()
            self.GetOutputList().Add(self.hist_gent[h])
	for h in self.hist_trans:
            self.hist_trans[h].Sumw2()
            self.GetOutputList().Add(self.hist_trans[h])
	for h in self.hist_pre:
            self.hist_pre[h].Sumw2()
            self.GetOutputList().Add(self.hist_pre[h])
	for h in self.hist_post:
            self.hist_post[h].Sumw2()
            self.GetOutputList().Add(self.hist_post[h])	
	for h in self.hist_jet:
            self.hist_jet[h].Sumw2()
            self.GetOutputList().Add(self.hist_jet[h])
	for h in self.hist_tow:
            self.hist_tow[h].Sumw2()
            self.GetOutputList().Add(self.hist_tow[h])
	for h in self.hist_away:
            self.hist_away[h].Sumw2()
            self.GetOutputList().Add(self.hist_away[h])
	for h in self.hist_gentow:
            self.hist_gentow[h].Sumw2()
            self.GetOutputList().Add(self.hist_gentow[h])
        for h in self.hist_genaway:
            self.hist_genaway[h].Sumw2()
            self.GetOutputList().Add(self.hist_genaway[h])
	for h in self.hist_full_genjet:
            self.hist_full_genjet[h].Sumw2()
            self.GetOutputList().Add(self.hist_full_genjet[h])	
	for h in self.hist_full_gentracks:
            self.hist_full_gentracks[h].Sumw2()
            self.GetOutputList().Add(self.hist_full_gentracks[h])
	for h in self.hist_full_jet:
            self.hist_full_jet[h].Sumw2()
            self.GetOutputList().Add(self.hist_full_jet[h])
        for h in self.hist_full_tracks:
            self.hist_full_tracks[h].Sumw2()
            self.GetOutputList().Add(self.hist_full_tracks[h])


	 	

        self.Trans_SisCon5["nTransDensity"] = ROOT.TProfile("nTransDensity_SisCon5",   "n_trans",  200, 0, 100)
        self.Trans_SisCon5["ptTransDensity"] = ROOT.TProfile("ptTransDensity_SisCon5",   "pt_trans",  200, 0, 100)
	self.Trans_SisCon5["nTow"] = ROOT.TProfile("nTow_SisCon5",   "n_tow",  200, 0, 100)
        self.Trans_SisCon5["nAway"] = ROOT.TProfile("nAway_SisCon5",   "n_away",  200, 0, 100)
        self.Trans_SisCon5["ptTow"] = ROOT.TProfile("ptTow_SisCon5",   "pt_tow",  200, 0, 100)
        self.Trans_SisCon5["ptAway"] = ROOT.TProfile("ptAway_SisCon5",   "pt_away",  200, 0, 100)
        self.Trans_SisCon5["nTot"] = ROOT.TProfile("nTot_SisCon5",   "pt_away",  200, 0, 100)
        self.Trans_SisCon5["ptTot"] = ROOT.TProfile("ptTot_SisCon5",   "pt_away",  200, 0, 100)

	for h in self.Trans_SisCon5:
            self.Trans_SisCon5[h].Sumw2()
            self.GetOutputList().Add(self.Trans_SisCon5[h])	

        self.other_SisCon5["nTransMax"] = ROOT.TProfile("nTransMax_SisCon5",   "n_trans",  200, 0, 100)
        self.other_SisCon5["nTransMin"] = ROOT.TProfile("nTransMin_SisCon5",   "n_trans",  200, 0, 100)
	self.other_SisCon5["ptTransMax"] = ROOT.TProfile("ptTransMax_SisCon5",   "pt_trans",  200, 0, 100)
        self.other_SisCon5["ptTransMin"] = ROOT.TProfile("ptTransMin_SisCon5",   "pt_trans",  200, 0, 100)
	self.other_SisCon5["nDiff"] = ROOT.TProfile("nDiff_SisCon5",   "pt_diff",  200, 0, 100)
        self.other_SisCon5["ptDiff"] = ROOT.TProfile("ptDiff_SisCon5",   "pt_diff",  200, 0, 100)	

        for h in self.other_SisCon5:
            self.other_SisCon5[h].Sumw2()
            self.GetOutputList().Add(self.other_SisCon5[h])
         


    def analyze(self):
        # note: use printTTree.py asamplename in order to learn what tries/branches are avaliable

        weight = 1 # 
        num = 0
        #self.hist["numGenTracks"].Fill(num, weight)
        #for t in self.fChain.genParticlesp4: # this collection contains four-momenta of charged genparticles
        #    self.hist["etaGenTracks"].Fill(t.eta(), weight)

        # consistency xcheck
        ''' - disabled
        sizes = set()
        sizes.add(self.fChain.dxy.size())
        sizes.add(self.fChain.dz.size())
        sizes.add(self.fChain.recoTracks.size())
        sizes.add(self.fChain.testTrkData.size())
        if len(sizes)!= 1:
            print "Wrong collection lengths:", sizes
            raise Exception("Inonsistent data")
        # '''

        #for i in xrange(0, self.fChain.dz.size()):
        #for i in xrange(0, self.fChain.testTrkData.size()):
        #for i in xrange(0, self.fChain.recoTracksp4.size()):
         #   self.hist["etaRecoTracks"].Fill(self.fChain.recoTracksp4.at(i).eta())
            
        sumpt_gen=0.
        pt_gen=-1.
        dphi_gen=999
	phi_gen=0
        eta_gen=999
        n_gen=0.
        ntracks_gen=0
        n_tow_gen=0.
        sumpt_tow_gen=0.
        n_away_gen=0.
        sumpt_away_gen=0.
	n_tot_gen=0.

        sumpt1_gen=0
        sumpt2_gen=0
        n1_gen=0
        n2_gen=0
        sumpt_max_gen=0
        sumpt_min_gen=0
        n_max_gen=0
        n_min_gen=0

        nconst=0


        weight = 1  
        num = 0

        numgoodvtx = 0
	nu=0

        vtx_x=0
        vtx_y=0
	vtx_z=0


        if self.fChain.lumi >= 90:  
         for i in xrange(0, self.fChain.vtxisFake.size()):
                    
                    vtxrho = math.sqrt(self.fChain.vtxx.at(i)*self.fChain.vtxx.at(i) + self.fChain.vtxy.at(i)*self.fChain.vtxy.at(i))

		    nu=nu+1	
                    if not self.fChain.vtxisFake.at(i) and abs(self.fChain.vtxz.at(i)) <= 10 and self.fChain.vtxndof.at(i) > 4 and vtxrho <= 2: # count only good primary vertices
                        numgoodvtx+=1
			if numgoodvtx==1:
			 vtx_x=self.fChain.vtxx.at(i)
			 vtx_y=self.fChain.vtxy.at(i)
			 vtx_z=self.fChain.vtxz.at(i)
			self.hist_vertex["ndfVtx"].Fill(self.fChain.vtxndof.at(i))	
        self.hist_vertex["nVtx"].Fill(numgoodvtx) 

        sumpt=0.
        pt=-1.
        dphi=999
	phi=0
        eta=999
        n=0.
        ntracks=0
        n_tow=0.
        sumpt_tow=0.
        n_away=0.
        sumpt_away=0.

	sumpt1=0
	sumpt2=0
	n1=0
	n2=0
	sumpt_max=0
	sumpt_min=0
	n_max=0
	n_min=0
	
	ptf=0
	phif=0
	etaf=0

	self.hist_vertex["nJets"].Fill(self.fChain.SisCone5CHp4.size())

		
	for i in xrange(0, self.fChain.SisCone5CHp4.size()): # SisCone5
                    trackp4 = self.fChain.SisCone5CHp4.at(i)
                    if trackp4.pt()>ptf:
                        ptf=trackp4.pt()
                        phif=trackp4.phi()
                        etaf=trackp4.eta()
	self.hist_full_jet["f_ptSisCone5"].Fill(ptf)
        self.hist_full_jet["f_phiSisCone5"].Fill(phif)
        self.hist_full_jet["f_etaSisCone5"].Fill(etaf)
        if numgoodvtx == 1:
	    for i in xrange(0, self.fChain.SisCone5CHp4.size()): # SisCone5
                    trackp4 = self.fChain.SisCone5CHp4.at(i)	
                    if self.fChain.SisCone5CHnConst.at(i)>1:
                     if trackp4.pt()>pt:
                        pt=trackp4.pt()
                        phi=trackp4.phi()
			eta=trackp4.eta()
			ntracks=self.fChain.SisCone5CHnConst.at(i)
			#d0
			#d0err	
            if not pt < 1 and math.fabs(eta)<2.:
                self.hist_jet["ptSisCone5"].Fill(pt)
		self.hist_jet["phiSisCone5"].Fill(phi)
		self.hist_jet["etaSisCone5"].Fill(eta)
		self.hist_jet["nTracksSisCone5"].Fill(ntracks)
	    #if True:	
		print self.fChain.recoTracksd0Err.size()
                for i in xrange(0, self.fChain.recoTracksd0Err.size()):
		  track= self.fChain.recoTracksp4.at(i)
		  #tr_d0=self.fChain.recoTracksd0.at(i)
		  tr_d0Err=self.fChain.recoTracksd0Err.at(i)
		  tr_dzErr=self.fChain.recoTracksdzErr.at(i) 	
		  tr_ptErr=self.fChain.recoTracksptErr.at(i)	

		  tr_x=self.fChain.recoTracksvx.at(i)
		  tr_y=self.fChain.recoTracksvy.at(i)		
		  tr_z=self.fChain.recoTracksvz.at(i) 

		  tr_d0= (- (tr_x-vtx_x) * track.py() + (tr_y-vtx_y) * track.px() ) / track.pt() 

	          tr_dz=  (tr_z-vtx_z) - ((tr_x-vtx_x)*track.px()+(tr_y-vtx_y)*track.py())/track.pt() * (track.pz()/track.pt())		 

		  purity=0
        	  imp0= 0
        	  impz= 0
                  dpt= 0
                  kin= 0
		  dphi=track.phi()-phi
                  while dphi > math.pi:
                         dphi=dphi-2*math.pi
                  while dphi < -math.pi:
                         dphi=dphi+2*math.pi	
		  self.hist_pre["trackD0"].Fill(tr_d0)
		  self.hist_pre["trackD0Err"].Fill(tr_d0Err)
		  self.hist_pre["trackD0Significance"].Fill(tr_d0/tr_d0Err)	
		  self.hist_pre["trackDz"].Fill(tr_dz)
                  self.hist_pre["trackDzErr"].Fill(tr_dzErr)
                  self.hist_pre["trackDzSignificance"].Fill(tr_dz/tr_dzErr)	
		  self.hist_pre["trackPt"].Fill(track.pt())
		  self.hist_pre["trackPtErr"].Fill(tr_ptErr)
		  self.hist_pre["trackPtSigma"].Fill(tr_ptErr/track.pt())
		  self.hist_pre["trackEta"].Fill(track.eta())
		  self.hist_pre["trackPhi"].Fill(track.phi())
		  self.hist_pre["trackDeltaPhi"].Fill(dphi)
		  if self.fChain.recoTrackshighPurity.at(i):
		   #purity=1	
		   if math.fabs(tr_d0/tr_d0Err)<3:
		    # imp0=1	
		     if math.fabs(tr_dz/tr_dzErr)<3:
		     # impz=1	
		      if tr_ptErr/track.pt()<0.05:
		       #dpt=1	
		       if track.pt()>0.5 and math.fabs(track.eta())<2.:	
		  	kin=1
			if not pt < 1 and math.fabs(eta)<2.:# and ntracks > 1:	 		
			   self.hist_post["trackD0"+p1].Fill(tr_d0)
                 	   self.hist_post["trackD0Err"+p1].Fill(tr_d0Err)
                 	   self.hist_post["trackD0Significance"+p1].Fill(tr_d0/tr_d0Err)
                 	   self.hist_post["trackDz"+p1].Fill(tr_dz)
                 	   self.hist_post["trackDzErr"+p1].Fill(tr_dzErr)
                  	   self.hist_post["trackDzSignificance"+p1].Fill(tr_dz/tr_dzErr)
                  	   self.hist_post["trackPt"+p1].Fill(track.pt())
                  	   self.hist_post["trackPtErr"+p1].Fill(tr_ptErr)
                  	   self.hist_post["trackPtSigma"+p1].Fill(tr_ptErr/track.pt())
                  	   self.hist_post["trackEta"+p1].Fill(track.eta())
                  	   self.hist_post["trackPhi"+p1].Fill(track.phi())	
                           self.hist_post["trackDeltaPhi"+p1].Fill(dphi)	
			   
                           if (dphi > math.pi/3. and dphi < 2*math.pi/3.):
                            n=n+1.
			    sumpt=sumpt+track.pt()

			    n1=n1+1
			    sumpt1=sumpt1+track.pt()		    			   

			   if (dphi < -math.pi/3. and dphi > -2*math.pi/3.):	
			    n=n+1.
                            sumpt=sumpt+track.pt()				   
	 		
			    n2=n2+1
			    sumpt2=sumpt2+track.pt()

			   if (dphi < math.pi/3. and dphi > -math.pi/3):
			    n_tow=n_tow+1
			    sumpt_tow=sumpt_tow+track.pt()	

			   if (dphi > 2*math.pi/3. or dphi < -2*math.pi/3):
			    n_away=n_away+1
                            sumpt_away=sumpt_away+track.pt()

                  self.hist_pre["purity"].Fill(purity)
        	  self.hist_pre["imp0"].Fill(imp0)
        	  self.hist_pre["impz"].Fill(impz)
                  self.hist_pre["dpt"].Fill(dpt)
                  self.hist_pre["kin"].Fill(kin)
		if n+n_tow+n_away>-1:
  	    	 self.hist_jet["nTot_SisCone5"].Fill(n+n_tow+n_away,pt)
                 self.Trans_SisCon5["nTot"].Fill(pt,n+n_tow+n_away)

                 self.Trans_SisCon5["ptTot"].Fill(pt,sumpt+sumpt_away+sumpt_tow)
	         #if n+n_tow+n_away>0:
                 self.hist_trans["nTrans_SisCone5"].Fill(n,pt)
		 self.Trans_SisCon5["nTransDensity"].Fill(pt,n)

                 self.Trans_SisCon5["ptTransDensity"].Fill(pt,sumpt)
                 self.hist_trans["ptTrans_SisCone5"].Fill(sumpt,pt)	
		 if sumpt1>sumpt2:
			sumpt_max=sumpt1
			sumpt_min=sumpt2
		 else :
			sumpt_max=sumpt2
                        sumpt_min=sumpt1
		 if n1>n2:
                        n_max=n1
                        n_min=n2
                 else :
                        n_max=n2
                        n_min=n1
  
		 self.hist_trans["nTransMax_SisCone5"].Fill(n_max,pt)
                 self.other_SisCon5["nTransMax"].Fill(pt,n_max)
		  	
                 self.hist_trans["ptTransMax_SisCone5"].Fill(sumpt_max,pt)
	         self.other_SisCon5["ptTransMax"].Fill(pt,sumpt_max)  

                 self.hist_trans["nTransMin_SisCone5"].Fill(n_min,pt)
		 self.other_SisCon5["nTransMin"].Fill(pt,n_min)  
			
                 self.hist_trans["ptTransMin_SisCone5"].Fill(sumpt_min,pt)	
		 self.other_SisCon5["ptTransMin"].Fill(pt,sumpt_min)

		 self.hist_trans["nTransDiff_SisCone5"].Fill(-n_min+n_max,pt)
		 self.other_SisCon5["nDiff"].Fill(pt,-n_min+n_max)

                 self.hist_trans["ptTransDiff_SisCone5"].Fill(-sumpt_min+sumpt_max,pt)
		 self.other_SisCon5["ptDiff"].Fill(pt,-sumpt_min+sumpt_max)	

		 self.hist_tow["nTow_SisCone5"].Fill(n_tow,pt)
		 self.Trans_SisCon5["nTow"].Fill(pt,n_tow)
			
                 self.hist_tow["ptTow_SisCone5"].Fill(sumpt_tow,pt)
		 self.Trans_SisCon5["ptTow"].Fill(pt,sumpt_tow)	

		 self.hist_away["nAway_SisCone5"].Fill(n_away,pt)
		 self.Trans_SisCon5["nAway"].Fill(pt,n_away)

                 self.hist_away["ptAway_SisCone5"].Fill(sumpt_away,pt)
		 self.Trans_SisCon5["ptAway"].Fill(pt,sumpt_away)	

        return 1

    def finalize(self):
        print "Finalize:"
        normFactor = self.getNormalizationFactor()
        print "  applying norm", normFactor

	for h in self.Trans_SisCon5:
           self.Trans_SisCon5[h].Scale(3/(2*4*math.pi))
	for h in self.other_SisCon5:
           self.other_SisCon5[h].Scale(3/(4*math.pi))

        for h in self.hist:
            self.hist[h].Scale(normFactor)

if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    ROOT.gSystem.Load("libFWCoreFWLite.so")
    ROOT.AutoLibraryLoader.enable()

    sampleList = None
    maxFilesMC = None
    maxFilesData = None
    nWorkers = None # Use all

    # debug config:
    #'''
    # Run printTTree.py alone to get the samples list
    #sampleList = []
    #sampleList.append("QCD_Pt-15to3000_TuneZ2star_Flat_HFshowerLibrary_7TeV_pythia6")
    maxFilesMC = 20 
    maxFilesData = 200
    #nWorkers = 16
    #maxFilesData = 1
    nWorkers =12 
    # '''


    slaveParams = {}
    #slaveParams["maxEta"] = 2.


    # use printTTree.py <sampleName> to see what trees are avaliable inside the skim file
    CSA14_UEAna.runAll(treeName="UETree",
                               slaveParameters=slaveParams,
                               sampleList=sampleList,
                               maxFilesMC = maxFilesMC,
                               maxFilesData = maxFilesData,
                               nWorkers=nWorkers,
				outFile = "plots_UETrackJet_lowPU.root" )
