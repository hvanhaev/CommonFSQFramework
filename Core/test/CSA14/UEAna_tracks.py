#!/usr/bin/env python
import CommonFSQFramework.Core.ExampleProofReader

import sys, os, time, math
sys.path.append(os.path.dirname(__file__))

import ROOT
ROOT.gROOT.SetBatch(True)
from ROOT import edm, JetCorrectionUncertainty


from array import *

p1="_post"

class UEAna_tracks(CommonFSQFramework.Core.ExampleProofReader.ExampleProofReader):
    def init( self):
        self.etacut = 2.
	self.hist = {}
        self.hist_vertex = {}
	self.hist_pre = {}
	self.hist_post = {}
	self.hist_gen = {}

	self.hist_gent = {}
	self.hist_trans = {}
	self.hist_tow = {}
	self.hist_away = {}
	self.hist_gentow = {}
        self.hist_genaway = {}

	self.hist_full_tracks = {}

        self.hist_full_gentracks = {}

     


        self.hist_full_gentracks["fgen_trackPt"] =  ROOT.TH1F("fgen_tracksPt",   "tracksPt",  5000, 0, 500)



        self.hist_full_tracks["f_trackPt"] =  ROOT.TH1F("f_trackPt",   "tracksPt",  5000, 0, 500)


        #p = "_central_B" # a placeholder for different triggers ("B") and uncertainty variations
                         #  "central" means this is a central value (ie no variations were applied)
        self.hist_vertex["nVtx"] =  ROOT.TH1F("nVtx",   "nVtx",  100, 0, 100)
        self.hist_vertex["ndfVtx"] =  ROOT.TH1F("ndfVtx",   "ndfVtx",  100, 0, 100)

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

	for h in self.hist_full_gentracks:
            self.hist_full_gentracks[h].Sumw2()
            self.GetOutputList().Add(self.hist_full_gentracks[h])

        for h in self.hist_full_tracks:
            self.hist_full_tracks[h].Sumw2()
            self.GetOutputList().Add(self.hist_full_tracks[h])

         


    def analyze(self):
        # note: use printTTree.py asamplename in order to learn what trees/branches are avaliable

        #GEN GEN GEN GEN GEN GEN GEN GEN GEN GEN GEN GEN GEN GEN GEN GEN GEN GEN GEN GEN GEN GEN GEN GEN 
        #GEN GEN GEN GEN GEN GEN GEN GEN GEN GEN GEN GEN GEN GEN GEN GEN GEN GEN GEN GEN GEN GEN GEN GEN 
        #GEN GEN GEN GEN GEN GEN GEN GEN GEN GEN GEN GEN GEN GEN GEN GEN GEN GEN GEN GEN GEN GEN GEN GEN 
        #GEN GEN GEN GEN GEN GEN GEN GEN GEN GEN GEN GEN GEN GEN GEN GEN GEN GEN GEN GEN GEN GEN GEN GEN 

        weight = 1 # 
        num = 0
        num = self.fChain.genParticlesp4.size()
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

 


        for track in self.fChain.genParticlesp4:
                  self.hist_full_gentracks["fgen_trackPt"].Fill(track.pt()) 	

	#print self.tracks.getSize()
	#for tracksg in self.tracks.get(""):
        #          track=tracksg.p4
        #          self.hist_full_tracks["f_trackPt"].Fill(track.pt())


        #FIND AND DEFINE THE LEADING TRACK
        #CHECK FOR ETA AND PT CUT?
	for i in  xrange(0, self.fChain.genParticlesp4.size()): # SisCone5
		trackp4=self.fChain.genParticlesp4.at(i)	
        	if trackp4.pt()>pt_gen and trackp4.pt() > 0.5 and math.fabs(trackp4.eta()) < self.etacut:
                    pt_gen=trackp4.pt()
                    phi_gen=trackp4.phi()
                    eta_gen=trackp4.eta()
			

        #ONLY PROCEED IF THERE IS A LEADING TRACK
	if not pt_gen < 0. and math.fabs(eta_gen)<self.etacut: # and trackjetg._genJets_number_of_tracks>1 :
               self.hist["gen_ptSisCone5"].Fill(pt_gen)
               self.hist["gen_phiSisCone5"].Fill(phi_gen)
               self.hist["gen_etaSisCone5"].Fill(eta_gen)
	#if True:
	       for track in self.fChain.genParticlesp4:
                  dphi_gen=track.phi()-phi_gen

                  while dphi_gen > math.pi:
                         dphi_gen=dphi_gen-2*math.pi
                  while dphi_gen < -math.pi:
                         dphi_gen=dphi_gen+2*math.pi
         
                  #FILL THE REGIONS WITH NCH AND PTSUM
                  if track.pt()>0.5 and math.fabs(track.eta())<self.etacut : #and self.genTracks.getSize()>4:
		     self.hist_gen["gen_trackDeltaPhi"].Fill(dphi_gen)	
		     self.hist_gen["gen_trackPt"].Fill(track.pt())
                     self.hist_gen["gen_trackEta"].Fill(track.eta())
                     self.hist_gen["gen_trackPhi"].Fill(track.phi())

                     #ONLY PROCEED IF THERE IS A LEADING TRACK (REDUNDANT?...)
		     if not pt_gen < 0. and math.fabs(eta_gen)<self.etacut :
		      n_tot_gen=n_tot_gen+1	
			
                      if (dphi_gen > math.pi/3. and dphi_gen < 2*math.pi/3.):
                            n_gen=n_gen+1.
                            sumpt_gen=sumpt_gen+track.pt()
		  	    
			    n1_gen=n1_gen+1
                            sumpt1_gen=sumpt1_gen+track.pt()

                      if (dphi_gen < -math.pi/3. and dphi_gen > -2*math.pi/3.):
                            n_gen=n_gen+1.
                            sumpt_gen=sumpt_gen+track.pt()

                            n2_gen=n2_gen+1
                            sumpt2_gen=sumpt2_gen+track.pt()

                      if (dphi_gen < math.pi/3. and dphi_gen > -math.pi/3):
                            n_tow_gen=n_tow_gen+1
                            sumpt_tow_gen=sumpt_tow_gen+track.pt()

                      if (dphi_gen > 2*math.pi/3. or dphi_gen < -2*math.pi/3):
                            n_away_gen=n_away_gen+1
                            sumpt_away_gen=sumpt_away_gen+track.pt()		

               #FILL HISTOGRAMS (ONLY IF TOTAL NCH > 0)
 	       if n_tot_gen > 0:
      		 self.hist["gen_nTot_SisCone5"].Fill(n_tot_gen,pt_gen)
	#	if n_gen>0:
               	 self.hist_gent["gen_ptTrans_SisCone5"].Fill(sumpt_gen,pt_gen)
		 if sumpt1_gen>sumpt2_gen:
                        sumpt_max_gen=sumpt1_gen
                        n_max_gen=n1_gen
                        sumpt_min_gen=sumpt2_gen
                        n_min_gen=n2_gen
                 else :
                        sumpt_max_gen=sumpt2_gen
                        n_max_gen=n2_gen
                        sumpt_min_gen=sumpt1_gen
                        n_min_gen=n1_gen
                 self.hist_gent["gen_nTrans_SisCone5"].Fill(n_max_gen+n_min_gen,pt_gen) 
##### 3./(2.*4*math.pi)
                 self.hist_gent["gen_nTransMax_SisCone5"].Fill(n_max_gen,pt_gen)
                 self.hist_gent["gen_ptTransMax_SisCone5"].Fill(sumpt_max_gen,pt_gen)
                 self.hist_gent["gen_nTransMin_SisCone5"].Fill(n_min_gen,pt_gen)
                 self.hist_gent["gen_ptTransMin_SisCone5"].Fill(sumpt_min_gen,pt_gen)
		 self.hist_gent["gen_nTransDiff_SisCone5"].Fill(-n_min_gen+n_max_gen,pt_gen)
                 self.hist_gent["gen_ptTransDiff_SisCone5"].Fill(-sumpt_min_gen+sumpt_max_gen,pt_gen)
                 #if n_tow_gen>0:
                 self.hist_gentow["gen_nTow_SisCone5"].Fill(n_tow_gen,pt_gen)
                 self.hist_gentow["gen_ptTow_SisCone5"].Fill(sumpt_tow_gen,pt_gen)
                 #if n_away_gen>0:
                 self.hist_genaway["gen_nAway_SisCone5"].Fill(n_away_gen,pt_gen)
                 self.hist_genaway["gen_ptAway_SisCone5"].Fill(sumpt_away_gen,pt_gen)
    

        #RECO RECO RECO RECO RECO RECO RECO RECO RECO RECO RECO RECO RECO RECO RECO RECO RECO RECO RECO RECO RECO 
        #RECO RECO RECO RECO RECO RECO RECO RECO RECO RECO RECO RECO RECO RECO RECO RECO RECO RECO RECO RECO RECO 
        #RECO RECO RECO RECO RECO RECO RECO RECO RECO RECO RECO RECO RECO RECO RECO RECO RECO RECO RECO RECO RECO 
        #RECO RECO RECO RECO RECO RECO RECO RECO RECO RECO RECO RECO RECO RECO RECO RECO RECO RECO RECO RECO RECO 
        #RECO RECO RECO RECO RECO RECO RECO RECO RECO RECO RECO RECO RECO RECO RECO RECO RECO RECO RECO RECO RECO 

        weight = 1  
        num = 0

        numgoodvtx = 0
	nu=0

        vtx_x=0
        vtx_y=0
	vtx_z=0

        #COUNT NUMBER OF GOOD VERTICES
        for i in xrange(0, self.fChain.vtxisFake.size()):
                    
                    vtxrho = math.sqrt(self.fChain.vtxx.at(i)*self.fChain.vtxx.at(i) + self.fChain.vtxy.at(i)*self.fChain.vtxy.at(i))

		    nu=nu+1	
                    if not self.fChain.vtxisFake.at(i) and abs(self.fChain.vtxz.at(i)) <= 10 and self.fChain.vtxndof.at(i) > 4 and vtxrho <= 2:
                        numgoodvtx+=1
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


        #FIND AND DEFINE THE LEADING TRACK WITHOUT REGARD FOR VERTEX REQUIREMENT
        #CHECK FOR ETA AND PT CUT?  ALSO TRACK CRITERIA?
	for i in xrange(0, self.fChain.recoTracksp4.size()):
                    trackp4 = self.fChain.recoTracksp4.at(i)
                    if trackp4.pt()>ptf:
                        ptf=trackp4.pt()
                        phif=trackp4.phi()
                        etaf=trackp4.eta()
	self.hist_full_jet["f_ptSisCone5"].Fill(ptf)
        self.hist_full_jet["f_phiSisCone5"].Fill(phif)
        self.hist_full_jet["f_etaSisCone5"].Fill(etaf)

        #FIND AND DEFINE THE LEADING TRACK
        #CHECK FOR ETA AND PT CUT?  ALSO TRACK CRITERIA?
        if numgoodvtx == 1:
	    for i in xrange(0, self.fChain.recoTracksp4.size()): # SisCone5
                    trackp4 = self.fChain.recoTracksp4.at(i)	
                    #if self.fChain.SisCone5CHnConst.at(i)>1:
                    #The below "if" statement was conditional on the above one.
                    if trackp4.pt()>pt:
                        pt=trackp4.pt()
                        phi=trackp4.phi()
			eta=trackp4.eta()
			#d0
			#d0err	

            #ONLY PROCEED IF THERE IS A LEADING TRACK
            if not pt < 0. and math.fabs(eta)<self.etacut:
                self.hist_jet["ptSisCone5"].Fill(pt)
		self.hist_jet["phiSisCone5"].Fill(phi)
		self.hist_jet["etaSisCone5"].Fill(eta)
		self.hist_jet["nTracksSisCone5"].Fill(ntracks)
	    #if True:	
                for i in xrange(0, self.fChain.recoTracksp4.size()):
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
		       if track.pt()>0.5 and math.fabs(track.eta())<self.etacut:	
		  	kin=1
			if not pt < 0. and math.fabs(eta)<self.etacut:# and ntracks > 1:	 		
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
		if n+n_tow+n_away>0:
  	    	  self.hist_jet["nTot_SisCone5"].Fill(n+n_tow+n_away,pt)
	 #       if n>0:
                  self.hist_trans["nTrans_SisCone5"].Fill(n,pt)
		  self.Trans_SisCon5["nTransDensity"].Fill(pt,n)

                  self.Trans_SisCon5["ptTransDensity"].Fill(pt,sumpt)
                  self.hist_trans["ptTrans_SisCone5"].Fill(sumpt,pt)	
		  if sumpt1>sumpt2:
			sumpt_max=sumpt1
			n_max=n1
			sumpt_min=sumpt2
			n_min=n2
		  else :
			sumpt_max=sumpt2
                        n_max=n2
                        sumpt_min=sumpt1
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
		  self.other_SisCon5["nTow"].Fill(pt,n_tow)
			
                  self.hist_tow["ptTow_SisCone5"].Fill(sumpt_tow,pt)
		  self.other_SisCon5["ptTow"].Fill(pt,sumpt_tow)	

		  self.hist_away["nAway_SisCone5"].Fill(n_away,pt)
		  self.other_SisCon5["nAway"].Fill(pt,n_away)

                  self.hist_away["ptAway_SisCone5"].Fill(sumpt_away,pt)
		  self.other_SisCon5["ptAway"].Fill(pt,sumpt_away)	

        return 1

    def finalize(self):
        print "Finalize:"
        normFactor = self.getNormalizationFactor()
        print "  applying norm", normFactor

	for h in self.Trans_SisCon5:
           self.Trans_SisCon5[h].Scale(3/(4*2*self.etacut*math.pi))
	for h in self.other_SisCon5:
           self.other_SisCon5[h].Scale(3/(2*2*self.etacut*math.pi))

        for h in self.hist:
            self.hist[h].Scale(normFactor)

if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    ROOT.gSystem.Load("libFWCoreFWLite.so")
    ROOT.AutoLibraryLoader.enable()

    sampleList = None
    maxFilesMC = None
    maxFilesData = None
    nWorkers = 10 # "None" to use all.  Set to 10 so Bockjoo doesn't tell me I'm melting the UF cluster.

    # debug config:
    #'''
    # Run printTTree.py alone to get the samples list
    #sampleList = []
    #sampleList.append("QCD_Pt-15to3000_TuneZ2star_Flat_HFshowerLibrary_7TeV_pythia6")
    maxFilesMC = 1
    maxFilesData = 1
    #nWorkers = 16
    #maxFilesData = 1
    nWorkers = 4
    # '''


    slaveParams = {}
    slaveParams["maxEta"] = 2.


    # use printTTree.py <sampleName> to see what trees are avaliable inside the skim file
    UEAna_tracks.runAll(treeName="UETree",
                               slaveParameters=slaveParams,
                               sampleList=sampleList,
                               maxFilesMC = maxFilesMC,
                               maxFilesData = maxFilesData,
                               nWorkers=nWorkers,
                               outFile = "plotsUEAna_tracks.root" )

