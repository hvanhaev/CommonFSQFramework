#!/usr/bin/env python
import CommonFSQFramework.Core.ExampleProofReader
from  CommonFSQFramework.Core.RecoTracksGetter import RecoTracksGetter
from  CommonFSQFramework.Core.RecoVertexGetter import RecoVertexGetter
from  CommonFSQFramework.Core.GenParticlesGetter import GenParticlesGetter
import sys, os, time
sys.path.append(os.path.dirname(__file__))

import ROOT
ROOT.gROOT.SetBatch(True)


#Some of these may not be necessary.  This is for testing.
from ROOT import gSystem
#from config.RooUnfold import library
#gSystem.Load(library)
gSystem.Load("/home/rankdw/RooUnfold-1.1.1/libRooUnfold")
from ROOT import RooUnfoldResponse
from ROOT import RooUnfold
from ROOT import RooUnfoldBayes
from ROOT import RooUnfoldSvd
from ROOT import RooUnfoldTUnfold
#from rootpy import asrootpy

import math

class CSA14_dndeta_GENTEST(CommonFSQFramework.Core.ExampleProofReader.ExampleProofReader):
    def init( self):
        #self.triggers   = ["minbias", "zerobias"]
        self.triggers   = ["minbias", ]
        self.variations = ["central"] # only a central value now
        
        self.hist = {}


        histPrefix = "HIST_"
        binHalf = "_bh"
        binOne = "_b1"
        binTwo = "_b2"
	binFour = "_b4"
        genPrefix = "GEN_"


        self.eventCounter = 0

        self.maxAvgTrans = 0

	

        #Nch_response_Name = histPrefix+"Nch_response"

        ptMaxName_GEN_b4 = genPrefix+"ptMax"+binFour
        towardName_GEN_b4 = genPrefix+"toward"+binFour
        awayName_GEN_b4 = genPrefix+"away"+binFour
        transMaxName_GEN_b4 = genPrefix+"transMax"+binFour
        transMinName_GEN_b4 = genPrefix+"transMin"+binFour
        towardNchName_GEN_b4 = genPrefix+"towardNch"+binFour
        awayNchName_GEN_b4 = genPrefix+"awayNch"+binFour
        transMaxNchName_GEN_b4 = genPrefix+"transMaxNch"+binFour
        transMinNchName_GEN_b4 = genPrefix+"transMinNch"+binFour

        transDifName_GEN_b4 = genPrefix+"transDif"+binFour
        transDifNchName_GEN_b4 = genPrefix+"transDifNch"+binFour
        towardTotalName_GEN_b4= genPrefix+"towardTotal"+binFour
        towardTotalNchName_GEN_b4= genPrefix+"towardTotalNch"+binFour
        towardTotalAvgName_GEN_b4= genPrefix+"towardTotalAvg"+binFour
        overallTotalName_GEN_b4= genPrefix+"overallTotal"+binFour
        overallTotalNchName_GEN_b4= genPrefix+"overallTotalNch"+binFour
        overallTotalAvgName_GEN_b4= genPrefix+"overallTotalAvg"+binFour        

        transName_GEN_b4 = genPrefix+"trans"+binFour
        transNchName_GEN_b4 = genPrefix+"transNch"+binFour
        transAvgName_GEN_b4 = genPrefix+"transAvg"+binFour
        towardAvgName_GEN_b4 = genPrefix+"towardAvg"+binFour
        awayAvgName_GEN_b4 = genPrefix+"awayAvg"+binFour
        overallName_GEN_b4 = genPrefix+"overall"+binFour
        overallNchName_GEN_b4 = genPrefix+"overallNch"+binFour
        overallAvgName_GEN_b4 = genPrefix+"overallAvg"+binFour



        #SIM PLOTS

        #CUT PLOTS

        dZ_vs_vtxZ_Name = "dZ_vs_vtxZ"

        CUT_TFF_TTF_NchMB_Name = histPrefix+"CUT_TFF_TTF_NchMB"

        CUT_FFF_eta_Name = histPrefix+"CUT_FFF_eta"
        CUT_TFF_eta_Name = histPrefix+"CUT_TFF_eta"
        CUT_TTF_eta_Name = histPrefix+"CUT_TTF_eta"
        CUT_TTT_eta_Name = histPrefix+"CUT_TTT_eta"
        CUT_TFT_eta_Name = histPrefix+"CUT_TFT_eta"

        CUT_FFF_phi_Name = histPrefix+"CUT_FFF_phi"
        CUT_TFF_phi_Name = histPrefix+"CUT_TFF_phi"
        CUT_TTF_phi_Name = histPrefix+"CUT_TTF_phi"
        CUT_TTT_phi_Name = histPrefix+"CUT_TTT_phi"
        CUT_TFT_phi_Name = histPrefix+"CUT_TFT_phi"



        CUT_TFF_NchMB_Name = histPrefix+"CUT_TFF_NchMB"
        CUT_TTF_NchMB_Name = histPrefix+"CUT_TTF_NchMB"
        CUT_TTT_NchMB_Name = histPrefix+"CUT_TTT_NchMB"

        CUT_TFF_d0_Name = histPrefix+"CUT_TFF_d0"
        CUT_TTF_d0_Name = histPrefix+"CUT_TTF_d0"
        CUT_TTT_d0_Name = histPrefix+"CUT_TTT_d0"

        CUT_TFF_dz_Name = histPrefix+"CUT_TFF_dz"
        CUT_TTF_dz_Name = histPrefix+"CUT_TTF_dz"
        CUT_TTT_dz_Name = histPrefix+"CUT_TTT_dz"

        CUT_TFF_d0dzMax_Name = histPrefix+"CUT_TFF_d0dzMax"
        CUT_TTF_d0dzMax_Name = histPrefix+"CUT_TTF_d0dzMax"
        CUT_TTT_d0dzMax_Name = histPrefix+"CUT_TTT_d0dzMax"

        CUT_TFT_NchMB_Name = histPrefix+"CUT_TFT_NchMB"
        CUT_TFT_d0_Name = histPrefix+"CUT_TFT_d0"
        CUT_TFT_dz_Name = histPrefix+"CUT_TFT_dz"
        CUT_TFT_d0dzMax_Name = histPrefix+"CUT_TFT_d0dzMax"

        CUT_FFF_NchMB_Name = histPrefix+"CUT_FFF_NchMB"
        CUT_FFF_d0_Name = histPrefix+"CUT_FFF_d0"
        CUT_FFF_dz_Name = histPrefix+"CUT_FFF_dz"
        CUT_FFF_d0dzMax_Name = histPrefix+"CUT_FFF_d0dzMax"

        VTX_nTrk_Name = histPrefix+"VTX_nTrk"
        VTX_ndof_Name = histPrefix+"VTX_ndof"
        VTX_Zpos_Name = histPrefix+"VTX_Zpos"
        VTX_chi2_Name = histPrefix+"VTX_chi2"

        TRK_PtErr_Name = histPrefix+"TRK_PtErr"

        CUT_FFF_PtErr_Name = histPrefix+"CUT_FFF_PtErr"
        CUT_TFF_PtErr_Name = histPrefix+"CUT_TFF_PtErr"
        CUT_TTF_PtErr_Name = histPrefix+"CUT_TTF_PtErr"
        CUT_TTT_PtErr_Name = histPrefix+"CUT_TTT_PtErr"
        CUT_TFT_PtErr_Name = histPrefix+"CUT_TFT_PtErr"

        #NEW PLOTS 3-24-15

        eta_ptH_Name_GEN = genPrefix+histPrefix+"eta_ptH"
        phi_all_Name_GEN = genPrefix+histPrefix+"phi_all"
        phi_eta_Name_GEN = genPrefix+histPrefix+"phi_eta"
        phi_etaptH_Name_GEN = genPrefix+histPrefix+"phi_etaptH"

        eta_ptH_Name = histPrefix+"eta_ptH"
        phi_etaptH_Name = histPrefix+"phi_etaptH"

        phi_ptH_Name_GEN = genPrefix+histPrefix+"phi_ptH"
        

        #HISTOGRAMS
        ptMBName = histPrefix+"ptMB" #+histPostfix
        etaMBName = histPrefix+"etaMB" #+histPostfix
        ptName = histPrefix+"pt" #+histPostfix
        etaName = histPrefix+"eta" #+histPostfix
        delPhiName = histPrefix+"delPhi" #+histPostfix
        delPhiPtName = histPrefix+"delPhiPt" #+histPostfix
        nchName = histPrefix+"nch" #+histPostfix
        ptSumName = histPrefix+"ptSum" #+histPostfix
        nchMBName = histPrefix+"nchMB" #+histPostfix
        ptSumMBName = histPrefix+"ptSumMB" #+histPostfix
        transNchName = histPrefix+"transNch" #+histPostfix
        transPtSumName = histPrefix+"transPtSum" #+histPostfix
        transPtName = histPrefix+"transPt" #+histPostfix
        ptMaxName = histPrefix+"ptMax"

        trans12Name = histPrefix+"trans12"
        trans12Name_pt5 = histPrefix+"trans12_pt5"
        phiName = histPrefix+"phi"
        phiMaxName = histPrefix+"phiMax"
        phiName_pt5 = histPrefix+"phi_pt5"
        phiMaxName_pt5 = histPrefix+"phiMax_pt5"

        #PT GREATER THAN 5 GeV/C
        delPhiName_pt5 = histPrefix+"delPhi_pt5" #+histPostfix
        delPhiPtName_pt5 = histPrefix+"delPhiPt_pt5" #+histPostfix
        etaName_pt5 = histPrefix+"eta_pt5" #+histPostfix
        ptName_pt5 = histPrefix+"pt_pt5" #+histPostfix
        nchName_pt5 = histPrefix+"nch_pt5" #+histPostfix
        ptSumName_pt5 = histPrefix+"ptSum_pt5" #+histPostfix
        transNchName_pt5 = histPrefix+"transNch_pt5" #+histPostfix
        transPtSumName_pt5 = histPrefix+"transPtSum_pt5" #+histPostfix
        transPtName_pt5 = histPrefix+"transPt_pt5" #+histPostfix



        #PROFILES

        #BIN 0.5
        ptMaxName_bh = "ptMax"+binHalf
        towardName_bh = "toward"+binHalf
        awayName_bh = "away"+binHalf
        transMaxName_bh = "transMax"+binHalf
        transMinName_bh = "transMin"+binHalf
        towardNchName_bh = "towardNch"+binHalf
        awayNchName_bh = "awayNch"+binHalf
        transMaxNchName_bh = "transMaxNch"+binHalf
        transMinNchName_bh = "transMinNch"+binHalf

        transDifName_bh = "transDif"+binHalf
        transDifNchName_bh = "transDifNch"+binHalf
        towardTotalName_bh= "towardTotal"+binHalf
        towardTotalNchName_bh= "towardTotalNch"+binHalf
        towardTotalAvgName_bh= "towardTotalAvg"+binHalf
        overallTotalName_bh= "overallTotal"+binHalf
        overallTotalNchName_bh= "overallTotalNch"+binHalf
        overallTotalAvgName_bh= "overallTotalAvg"+binHalf

        transName_bh = "trans"+binHalf
        transNchName_bh = "transNch"+binHalf
        transAvgName_bh = "transAvg"+binHalf
        towardAvgName_bh = "towardAvg"+binHalf
        awayAvgName_bh = "awayAvg"+binHalf
        overallName_bh = "overall"+binHalf
        overallNchName_bh = "overallNch"+binHalf
        overallAvgName_bh = "overallAvg"+binHalf



        #BIN 1
        ptMaxName_b1 = "ptMax"+binOne
        towardName_b1 = "toward"+binOne
        awayName_b1 = "away"+binOne
        transMaxName_b1 = "transMax"+binOne
        transMinName_b1 = "transMin"+binOne
        towardNchName_b1 = "towardNch"+binOne
        awayNchName_b1 = "awayNch"+binOne
        transMaxNchName_b1 = "transMaxNch"+binOne
        transMinNchName_b1 = "transMinNch"+binOne

        transDifName_b1 = "transDif"+binOne
        transDifNchName_b1 = "transDifNch"+binOne
        towardTotalName_b1= "towardTotal"+binOne
        towardTotalNchName_b1= "towardTotalNch"+binOne
        towardTotalAvgName_b1= "towardTotalAvg"+binOne
        overallTotalName_b1= "overallTotal"+binOne
        overallTotalNchName_b1= "overallTotalNch"+binOne
        overallTotalAvgName_b1= "overallTotalAvg"+binOne        

        transName_b1 = "trans"+binOne
        transNchName_b1 = "transNch"+binOne
        transAvgName_b1 = "transAvg"+binOne
        towardAvgName_b1 = "towardAvg"+binOne
        awayAvgName_b1 = "awayAvg"+binOne
        overallName_b1 = "overall"+binOne
        overallNchName_b1 = "overallNch"+binOne
        overallAvgName_b1 = "overallAvg"+binOne


        #BIN 2
        ptMaxName_b2 = "ptMax"+binTwo
        towardName_b2 = "toward"+binTwo
        awayName_b2 = "away"+binTwo
        transMaxName_b2 = "transMax"+binTwo
        transMinName_b2 = "transMin"+binTwo
        towardNchName_b2 = "towardNch"+binTwo
        awayNchName_b2 = "awayNch"+binTwo
        transMaxNchName_b2 = "transMaxNch"+binTwo
        transMinNchName_b2 = "transMinNch"+binTwo

        transDifName_b2 = "transDif"+binTwo
        transDifNchName_b2 = "transDifNch"+binTwo
        towardTotalName_b2= "towardTotal"+binTwo
        towardTotalNchName_b2= "towardTotalNch"+binTwo
        towardTotalAvgName_b2= "towardTotalAvg"+binTwo
        overallTotalName_b2= "overallTotal"+binTwo
        overallTotalNchName_b2= "overallTotalNch"+binTwo
        overallTotalAvgName_b2= "overallTotalAvg"+binTwo        

        transName_b2 = "trans"+binTwo
        transNchName_b2 = "transNch"+binTwo
        transAvgName_b2 = "transAvg"+binTwo
        towardAvgName_b2 = "towardAvg"+binTwo
        awayAvgName_b2 = "awayAvg"+binTwo
        overallName_b2 = "overall"+binTwo
        overallNchName_b2 = "overallNch"+binTwo
        overallAvgName_b2 = "overallAvg"+binTwo

        #GEN PLOTS

        #ptMBName_GEN = genPrefix+histPrefix+"ptMB" #+histPostfix

        #NEW 3-10-15

        eta_all_Name_GEN = genPrefix+histPrefix+"eta_all"

        #NEW GEN HISTOGRAMS 1-16-15

        nch_all_Name_GEN = genPrefix+histPrefix+"nch_all"
        nch_eta_Name_GEN = genPrefix+histPrefix+"nch_eta"
        nch_etaptH_Name_GEN = genPrefix+histPrefix+"nch_etaptH"

        pt_all_Name_GEN = genPrefix+histPrefix+"pt_all"
        pt_eta_Name_GEN = genPrefix+histPrefix+"pt_eta"
        pt_etaptH_Name_GEN = genPrefix+histPrefix+"pt_etaptH"

        #HISTOGRAMS
        ptMBName_GEN = genPrefix+histPrefix+"ptMB" #+histPostfix
        etaMBName_GEN = genPrefix+histPrefix+"etaMB" #+histPostfix
        ptName_GEN = genPrefix+histPrefix+"pt" #+histPostfix
        etaName_GEN = genPrefix+histPrefix+"eta" #+histPostfix
        delPhiName_GEN = genPrefix+histPrefix+"delPhi" #+histPostfix
        delPhiPtName_GEN = genPrefix+histPrefix+"delPhiPt" #+histPostfix
        nchName_GEN = genPrefix+histPrefix+"nch" #+histPostfix
        ptSumName_GEN = genPrefix+histPrefix+"ptSum" #+histPostfix
        nchMBName_GEN = genPrefix+histPrefix+"nchMB" #+histPostfix
        ptSumMBName_GEN = genPrefix+histPrefix+"ptSumMB" #+histPostfix
        transNchName_GEN = genPrefix+histPrefix+"transNch" #+histPostfix
        transPtSumName_GEN = genPrefix+histPrefix+"transPtSum" #+histPostfix
        transPtName_GEN = genPrefix+histPrefix+"transPt" #+histPostfix
        ptMaxName_GEN = genPrefix+histPrefix+"ptMax"

        trans12Name_GEN = genPrefix+histPrefix+"trans12"
        trans12Name_GEN_pt5 = genPrefix+histPrefix+"trans12_pt5"

        phiName_GEN = genPrefix+histPrefix+"phi"
        phiMaxName_GEN = genPrefix+histPrefix+"phiMax"
        phiName_GEN_pt5 = genPrefix+histPrefix+"phi_pt5"
        phiMaxName_GEN_pt5 = genPrefix+histPrefix+"phiMax_pt5"

        #PT GREATER THAN 5 GeV/C
        delPhiName_GEN_pt5 = genPrefix+histPrefix+"delPhi_pt5" #+histPostfix
        delPhiPtName_GEN_pt5 = genPrefix+histPrefix+"delPhiPt_pt5" #+histPostfix
        etaName_GEN_pt5 = genPrefix+histPrefix+"eta_pt5" #+histPostfix
        ptName_GEN_pt5 = genPrefix+histPrefix+"pt_pt5" #+histPostfix
        nchName_GEN_pt5 = genPrefix+histPrefix+"nch_pt5" #+histPostfix
        ptSumName_GEN_pt5 = genPrefix+histPrefix+"ptSum_pt5" #+histPostfix
        transNchName_GEN_pt5 = genPrefix+histPrefix+"transNch_pt5" #+histPostfix
        transPtSumName_GEN_pt5 = genPrefix+histPrefix+"transPtSum_pt5" #+histPostfix
        transPtName_GEN_pt5 = genPrefix+histPrefix+"transPt_pt5" #+histPostfix



        #PROFILES

        #BIN 0.5
        ptMaxName_GEN_bh = genPrefix+"ptMax"+binHalf
        towardName_GEN_bh = genPrefix+"toward"+binHalf
        awayName_GEN_bh = genPrefix+"away"+binHalf
        transMaxName_GEN_bh = genPrefix+"transMax"+binHalf
        transMinName_GEN_bh = genPrefix+"transMin"+binHalf
        towardNchName_GEN_bh = genPrefix+"towardNch"+binHalf
        awayNchName_GEN_bh = genPrefix+"awayNch"+binHalf
        transMaxNchName_GEN_bh = genPrefix+"transMaxNch"+binHalf
        transMinNchName_GEN_bh = genPrefix+"transMinNch"+binHalf

        transDifName_GEN_bh = genPrefix+"transDif"+binHalf
        transDifNchName_GEN_bh = genPrefix+"transDifNch"+binHalf
        towardTotalName_GEN_bh= genPrefix+"towardTotal"+binHalf
        towardTotalNchName_GEN_bh= genPrefix+"towardTotalNch"+binHalf
        towardTotalAvgName_GEN_bh= genPrefix+"towardTotalAvg"+binHalf
        overallTotalName_GEN_bh= genPrefix+"overallTotal"+binHalf
        overallTotalNchName_GEN_bh= genPrefix+"overallTotalNch"+binHalf
        overallTotalAvgName_GEN_bh= genPrefix+"overallTotalAvg"+binHalf

        transName_GEN_bh = genPrefix+"trans"+binHalf
        transNchName_GEN_bh = genPrefix+"transNch"+binHalf
        transAvgName_GEN_bh = genPrefix+"transAvg"+binHalf
        towardAvgName_GEN_bh = genPrefix+"towardAvg"+binHalf
        awayAvgName_GEN_bh = genPrefix+"awayAvg"+binHalf
        overallName_GEN_bh = genPrefix+"overall"+binHalf
        overallNchName_GEN_bh = genPrefix+"overallNch"+binHalf
        overallAvgName_GEN_bh = genPrefix+"overallAvg"+binHalf

        #BIN 1
        ptMaxName_GEN_b1 = genPrefix+"ptMax"+binOne
        towardName_GEN_b1 = genPrefix+"toward"+binOne
        awayName_GEN_b1 = genPrefix+"away"+binOne
        transMaxName_GEN_b1 = genPrefix+"transMax"+binOne
        transMinName_GEN_b1 = genPrefix+"transMin"+binOne
        towardNchName_GEN_b1 = genPrefix+"towardNch"+binOne
        awayNchName_GEN_b1 = genPrefix+"awayNch"+binOne
        transMaxNchName_GEN_b1 = genPrefix+"transMaxNch"+binOne
        transMinNchName_GEN_b1 = genPrefix+"transMinNch"+binOne

        transDifName_GEN_b1 = genPrefix+"transDif"+binOne
        transDifNchName_GEN_b1 = genPrefix+"transDifNch"+binOne
        towardTotalName_GEN_b1= genPrefix+"towardTotal"+binOne
        towardTotalNchName_GEN_b1= genPrefix+"towardTotalNch"+binOne
        towardTotalAvgName_GEN_b1= genPrefix+"towardTotalAvg"+binOne
        overallTotalName_GEN_b1= genPrefix+"overallTotal"+binOne
        overallTotalNchName_GEN_b1= genPrefix+"overallTotalNch"+binOne
        overallTotalAvgName_GEN_b1= genPrefix+"overallTotalAvg"+binOne        

        transName_GEN_b1 = genPrefix+"trans"+binOne
        transNchName_GEN_b1 = genPrefix+"transNch"+binOne
        transAvgName_GEN_b1 = genPrefix+"transAvg"+binOne
        towardAvgName_GEN_b1 = genPrefix+"towardAvg"+binOne
        awayAvgName_GEN_b1 = genPrefix+"awayAvg"+binOne
        overallName_GEN_b1 = genPrefix+"overall"+binOne
        overallNchName_GEN_b1 = genPrefix+"overallNch"+binOne
        overallAvgName_GEN_b1 = genPrefix+"overallAvg"+binOne

        #BIN 2
        ptMaxName_GEN_b2 = genPrefix+"ptMax"+binTwo
        towardName_GEN_b2 = genPrefix+"toward"+binTwo
        awayName_GEN_b2 = genPrefix+"away"+binTwo
        transMaxName_GEN_b2 = genPrefix+"transMax"+binTwo
        transMinName_GEN_b2 = genPrefix+"transMin"+binTwo
        towardNchName_GEN_b2 = genPrefix+"towardNch"+binTwo
        awayNchName_GEN_b2 = genPrefix+"awayNch"+binTwo
        transMaxNchName_GEN_b2 = genPrefix+"transMaxNch"+binTwo
        transMinNchName_GEN_b2 = genPrefix+"transMinNch"+binTwo

        transDifName_GEN_b2 = genPrefix+"transDif"+binTwo
        transDifNchName_GEN_b2 = genPrefix+"transDifNch"+binTwo
        towardTotalName_GEN_b2= genPrefix+"towardTotal"+binTwo
        towardTotalNchName_GEN_b2= genPrefix+"towardTotalNch"+binTwo
        towardTotalAvgName_GEN_b2= genPrefix+"towardTotalAvg"+binTwo
        overallTotalName_GEN_b2= genPrefix+"overallTotal"+binTwo
        overallTotalNchName_GEN_b2= genPrefix+"overallTotalNch"+binTwo
        overallTotalAvgName_GEN_b2= genPrefix+"overallTotalAvg"+binTwo        

        transName_GEN_b2 = genPrefix+"trans"+binTwo
        transNchName_GEN_b2 = genPrefix+"transNch"+binTwo
        transAvgName_GEN_b2 = genPrefix+"transAvg"+binTwo
        towardAvgName_GEN_b2 = genPrefix+"towardAvg"+binTwo
        awayAvgName_GEN_b2 = genPrefix+"awayAvg"+binTwo
        overallName_GEN_b2 = genPrefix+"overall"+binTwo
        overallNchName_GEN_b2 = genPrefix+"overallNch"+binTwo
        overallAvgName_GEN_b2 = genPrefix+"overallAvg"+binTwo


        for t in self.triggers:
            for v in self.variations:

                #HISTOGRAMS
                #self.hist[Nch_reseponse_Name] = ROOT.TH1F(Nch_response_Name, Nch_response_Name, 100, 0, 100)



                #CUT ANALYSIS HISTOGRAMS

                #self.hist[CUT_TFF_TTF_NchMB_Name] = ROOT.TH2F(CUT_TFF_TTF_NchMB_Name,CUT_TFF_TTF_NchMB_Name, 100, -0.5, 99.5, 100, -99.5, 0.5)

                self.hist[CUT_FFF_eta_Name] =  ROOT.TH1F(CUT_FFF_eta_Name, CUT_FFF_eta_Name, 100, -10, 10)
                self.hist[CUT_TFF_eta_Name] =  ROOT.TH1F(CUT_TFF_eta_Name, CUT_TFF_eta_Name, 100, -10, 10)
                self.hist[CUT_TTF_eta_Name] =  ROOT.TH1F(CUT_TTF_eta_Name, CUT_TTF_eta_Name, 100, -10, 10)
                self.hist[CUT_TTT_eta_Name] =  ROOT.TH1F(CUT_TTT_eta_Name, CUT_TTT_eta_Name, 100, -10, 10)
                self.hist[CUT_TFT_eta_Name] =  ROOT.TH1F(CUT_TFT_eta_Name, CUT_TFT_eta_Name, 100, -10, 10)

                self.hist[CUT_FFF_phi_Name] =  ROOT.TH1F(CUT_FFF_phi_Name, CUT_FFF_phi_Name, 72, 0, 360)
                self.hist[CUT_TFF_phi_Name] =  ROOT.TH1F(CUT_TFF_phi_Name, CUT_TFF_phi_Name, 72, 0, 360)
                self.hist[CUT_TTF_phi_Name] =  ROOT.TH1F(CUT_TTF_phi_Name, CUT_TTF_phi_Name, 72, 0, 360)
                self.hist[CUT_TTT_phi_Name] =  ROOT.TH1F(CUT_TTT_phi_Name, CUT_TTT_phi_Name, 72, 0, 360)
                self.hist[CUT_TFT_phi_Name] =  ROOT.TH1F(CUT_TFT_phi_Name, CUT_TFT_phi_Name, 72, 0, 360)

                self.hist[dZ_vs_vtxZ_Name] = ROOT.TProfile(dZ_vs_vtxZ_Name,dZ_vs_vtxZ_Name, 120, -15, 15)

                self.hist[CUT_TFF_NchMB_Name] =  ROOT.TH1F(CUT_TFF_NchMB_Name, CUT_TFF_NchMB_Name+";Nch",  100,  0, 100)
                self.hist[CUT_TTF_NchMB_Name] =  ROOT.TH1F(CUT_TTF_NchMB_Name, CUT_TTF_NchMB_Name+";Nch",  100,  0, 100)
                self.hist[CUT_TTT_NchMB_Name] =  ROOT.TH1F(CUT_TTT_NchMB_Name, CUT_TTT_NchMB_Name+";Nch",  100,  0, 100)

                self.hist[CUT_TFF_d0_Name] =  ROOT.TH1F(CUT_TFF_d0_Name, CUT_TFF_d0_Name+";Nch",  400,  0, 200)
                self.hist[CUT_TTF_d0_Name] =  ROOT.TH1F(CUT_TTF_d0_Name, CUT_TTF_d0_Name+";Nch",  400,  0, 200)
                self.hist[CUT_TTT_d0_Name] =  ROOT.TH1F(CUT_TTT_d0_Name, CUT_TTT_d0_Name+";Nch",  400,  0, 200)

                self.hist[CUT_TFF_dz_Name] =  ROOT.TH1F(CUT_TFF_dz_Name, CUT_TFF_dz_Name+";Nch",  400,  0, 200)
                self.hist[CUT_TTF_dz_Name] =  ROOT.TH1F(CUT_TTF_dz_Name, CUT_TTF_dz_Name+";Nch",  400,  0, 200)
                self.hist[CUT_TTT_dz_Name] =  ROOT.TH1F(CUT_TTT_dz_Name, CUT_TTT_dz_Name+";Nch",  400,  0, 200)

                self.hist[CUT_TFF_d0dzMax_Name] =  ROOT.TH1F(CUT_TFF_d0dzMax_Name, CUT_TFF_d0dzMax_Name+";Nch",  400,  0, 200)
                self.hist[CUT_TTF_d0dzMax_Name] =  ROOT.TH1F(CUT_TTF_d0dzMax_Name, CUT_TTF_d0dzMax_Name+";Nch",  400,  0, 200)
                self.hist[CUT_TTT_d0dzMax_Name] =  ROOT.TH1F(CUT_TTT_d0dzMax_Name, CUT_TTT_d0dzMax_Name+";Nch",  400,  0, 200)

                self.hist[CUT_TFT_NchMB_Name] =  ROOT.TH1F(CUT_TFT_NchMB_Name,CUT_TFT_NchMB_Name, 100, 0, 100)
                self.hist[CUT_TFT_d0_Name] =  ROOT.TH1F(CUT_TFT_d0_Name,CUT_TFT_d0_Name, 400, 0, 200)
                self.hist[CUT_TFT_dz_Name] =  ROOT.TH1F(CUT_TFT_dz_Name,CUT_TFT_dz_Name, 400, 0, 200)
                self.hist[CUT_TFT_d0dzMax_Name] =  ROOT.TH1F(CUT_TFT_d0dzMax_Name,CUT_TFT_d0dzMax_Name, 400, 0, 200)

                self.hist[CUT_FFF_NchMB_Name] =  ROOT.TH1F(CUT_FFF_NchMB_Name,CUT_FFF_NchMB_Name, 100, 0, 100)
                self.hist[CUT_FFF_d0_Name] =  ROOT.TH1F(CUT_FFF_d0_Name,CUT_FFF_d0_Name, 400, 0, 200)
                self.hist[CUT_FFF_dz_Name] =  ROOT.TH1F(CUT_FFF_dz_Name,CUT_FFF_dz_Name, 400, 0, 200)
                self.hist[CUT_FFF_d0dzMax_Name] =  ROOT.TH1F(CUT_FFF_d0dzMax_Name,CUT_FFF_d0dzMax_Name, 400, 0, 200)

                self.hist[VTX_nTrk_Name] =  ROOT.TH1F(VTX_nTrk_Name,VTX_nTrk_Name, 100, 0, 100)
                self.hist[VTX_ndof_Name] =  ROOT.TH1F(VTX_ndof_Name,VTX_ndof_Name, 50, 0, 50)
                self.hist[VTX_Zpos_Name] =  ROOT.TH1F(VTX_Zpos_Name,VTX_Zpos_Name, 80, -20, 20)
                self.hist[VTX_chi2_Name] =  ROOT.TH1F(VTX_chi2_Name,VTX_chi2_Name, 200, 0, 200)

                self.hist[TRK_PtErr_Name] =  ROOT.TH1F(TRK_PtErr_Name,TRK_PtErr_Name, 100, 0, 1)

                self.hist[CUT_FFF_PtErr_Name] =  ROOT.TH1F(CUT_FFF_PtErr_Name,CUT_FFF_PtErr_Name, 100, 0, 1)
                self.hist[CUT_TFF_PtErr_Name] =  ROOT.TH1F(CUT_TFF_PtErr_Name,CUT_TFF_PtErr_Name, 100, 0, 1)
                self.hist[CUT_TTF_PtErr_Name] =  ROOT.TH1F(CUT_TTF_PtErr_Name,CUT_TTF_PtErr_Name, 100, 0, 1)
                self.hist[CUT_TTT_PtErr_Name] =  ROOT.TH1F(CUT_TTT_PtErr_Name,CUT_TTT_PtErr_Name, 100, 0, 1)
                self.hist[CUT_TFT_PtErr_Name] =  ROOT.TH1F(CUT_TFT_PtErr_Name,CUT_TFT_PtErr_Name, 100, 0, 1)



        #NEW PLOTS 3-24-15


                self.hist[eta_ptH_Name_GEN] =  ROOT.TH1F(eta_ptH_Name_GEN,eta_ptH_Name_GEN, 100, -10, 10)
                self.hist[phi_all_Name_GEN] =  ROOT.TH1F(phi_all_Name_GEN,phi_all_Name_GEN, 72, -180, 180)
                self.hist[phi_eta_Name_GEN] =  ROOT.TH1F(phi_eta_Name_GEN,phi_eta_Name_GEN, 72, -180, 180)
                self.hist[phi_etaptH_Name_GEN] =  ROOT.TH1F(phi_etaptH_Name_GEN,phi_etaptH_Name_GEN, 72, -180, 180)
                self.hist[eta_ptH_Name] =  ROOT.TH1F(eta_ptH_Name,eta_ptH_Name, 100, -10, 10)
                self.hist[phi_etaptH_Name] =  ROOT.TH1F(phi_etaptH_Name,phi_etaptH_Name, 72, -180, 180)

                self.hist[phi_ptH_Name_GEN] =  ROOT.TH1F(phi_ptH_Name_GEN,phi_ptH_Name_GEN, 72, -180, 180)


                self.hist[ptMBName] =  ROOT.TH1F(ptMBName, ptMBName+";p_T [GeV]",  100,  0, 50)
                self.hist[etaMBName] =  ROOT.TH1F(etaMBName, etaMBName+"; #eta",  100, -10, 10)
                self.hist[etaName] =  ROOT.TH1F(etaName, etaName+"; #eta",  100, -10, 10)
                self.hist[ptName] =  ROOT.TH1F(ptName, ptName+";p_T [GeV]",  100,  0, 50)
                self.hist[delPhiName] =  ROOT.TH1F(delPhiName, delPhiName+";delPhi [deg]",  72,  -180, 180)
                self.hist[delPhiPtName] =  ROOT.TH1F(delPhiPtName, delPhiPtName+";delPhiPt [Pt deg]",  72,  -180, 180)
                self.hist[nchName] =  ROOT.TH1F(nchName, nchName+";Nch",  100,  0, 100)
                self.hist[ptSumName] =  ROOT.TH1F(ptSumName, ptSumName+";ptSum",  100,  0, 100)
                self.hist[nchMBName] =  ROOT.TH1F(nchMBName, nchMBName+";Nch",  100,  0, 100)
                self.hist[ptSumMBName] =  ROOT.TH1F(ptSumMBName, ptSumMBName+";ptSum",  100,  0, 100)
                self.hist[transNchName] =  ROOT.TH1F(transNchName, transNchName+";Nch",  100,  0, 100)
                self.hist[transPtSumName] =  ROOT.TH1F(transPtSumName, transPtSumName+";ptSum",  100,  0, 100)
                self.hist[transPtName] =  ROOT.TH1F(transPtName, transPtName+";pt",  100,  0, 50)
                self.hist[ptMaxName] = ROOT.TH1F(ptMaxName, ptMaxName+";pt", 100, 0, 50)

                #PT GREATER THAN 5 GeV/C

                self.hist[delPhiName_pt5] =  ROOT.TH1F(delPhiName_pt5, delPhiName_pt5+";delPhi [deg]",  72,  -180, 180)
                self.hist[delPhiPtName_pt5] =  ROOT.TH1F(delPhiPtName_pt5, delPhiPtName_pt5+";delPhiPt_pt5 [Pt deg]",  72,  -180, 180)
                self.hist[etaName_pt5] =  ROOT.TH1F(etaName_pt5, etaName_pt5+"; #eta",  20, -2, 2)
                self.hist[ptName_pt5] =  ROOT.TH1F(ptName_pt5, ptName_pt5+";p_T [GeV]",  100,  0, 50)
                self.hist[nchName_pt5] =  ROOT.TH1F(nchName_pt5, nchName_pt5+";Nch",  100,  0, 100)
                self.hist[ptSumName_pt5] =  ROOT.TH1F(ptSumName_pt5, ptSumName_pt5+";ptSum",  100,  0, 100)
                self.hist[transNchName_pt5] =  ROOT.TH1F(transNchName_pt5, transNchName_pt5+";Nch",  100,  0, 100)
                self.hist[transPtSumName_pt5] =  ROOT.TH1F(transPtSumName_pt5, transPtSumName_pt5+";ptSum",  100,  0, 100)
                self.hist[transPtName_pt5] =  ROOT.TH1F(transPtName_pt5, transPtName_pt5+";pt",  100,  0, 50)
                self.hist[trans12Name] = ROOT.TH1F(trans12Name, trans12Name, 3, -1.5, 1.5)
                self.hist[trans12Name_pt5] = ROOT.TH1F(trans12Name_pt5, trans12Name_pt5, 3, -1.5, 1.5)
                self.hist[phiName] =  ROOT.TH1F(phiName, phiName+";delPhi [deg]",  72,  -180, 180)
                self.hist[phiName_pt5] =  ROOT.TH1F(phiName_pt5, phiName_pt5+";delPhi [deg]",  72,  -180, 180)
                self.hist[phiMaxName] =  ROOT.TH1F(phiMaxName, phiMaxName+";delPhi [deg]",  72,  -180, 180)
                self.hist[phiMaxName_pt5] =  ROOT.TH1F(phiMaxName_pt5, phiMaxName_pt5+";delPhi [deg]",  72,  -180, 180)


                #PROFILES

                #NEW 10-20-14
                self.hist[ptMaxName_bh] =  ROOT.TProfile(ptMaxName_bh,ptMaxName_bh, 100, 0, 50)
                self.hist[transDifName_bh] =  ROOT.TProfile(transDifName_bh,transDifName_bh, 100, 0, 50)
                self.hist[transDifNchName_bh] =  ROOT.TProfile(transDifNchName_bh,transDifNchName_bh, 100, 0, 50)
                self.hist[towardTotalName_bh] =  ROOT.TProfile(towardTotalName_bh,towardTotalName_bh, 100, 0, 50)
                self.hist[towardTotalNchName_bh] =  ROOT.TProfile(towardTotalNchName_bh,towardTotalNchName_bh, 100, 0, 50)
                self.hist[towardTotalAvgName_bh] =  ROOT.TProfile(towardTotalAvgName_bh,towardTotalAvgName_bh, 100, 0, 50)
                self.hist[overallTotalName_bh] =  ROOT.TProfile(overallTotalName_bh,overallTotalName_bh, 100, 0, 50)
                self.hist[overallTotalNchName_bh] =  ROOT.TProfile(overallTotalNchName_bh,overallTotalNchName_bh, 100, 0, 50)
                self.hist[overallTotalAvgName_bh] =  ROOT.TProfile(overallTotalAvgName_bh,overallTotalAvgName_bh, 100, 0, 50)
                self.hist[ptMaxName_b1] =  ROOT.TProfile(ptMaxName_b1,ptMaxName_b1, 50, 0, 50)
                self.hist[transDifName_b1] =  ROOT.TProfile(transDifName_b1,transDifName_b1, 50, 0, 50)
                self.hist[transDifNchName_b1] =  ROOT.TProfile(transDifNchName_b1,transDifNchName_b1, 50, 0, 50)
                self.hist[towardTotalName_b1] =  ROOT.TProfile(towardTotalName_b1,towardTotalName_b1, 50, 0, 50)
                self.hist[towardTotalNchName_b1] =  ROOT.TProfile(towardTotalNchName_b1,towardTotalNchName_b1, 50, 0, 50)
                self.hist[towardTotalAvgName_b1] =  ROOT.TProfile(towardTotalAvgName_b1,towardTotalAvgName_b1, 50, 0, 50)
                self.hist[overallTotalName_b1] =  ROOT.TProfile(overallTotalName_b1,overallTotalName_b1, 50, 0, 50)
                self.hist[overallTotalNchName_b1] =  ROOT.TProfile(overallTotalNchName_b1,overallTotalNchName_b1, 50, 0, 50)
                self.hist[overallTotalAvgName_b1] =  ROOT.TProfile(overallTotalAvgName_b1,overallTotalAvgName_b1, 50, 0, 50)
                self.hist[ptMaxName_b2] =  ROOT.TProfile(ptMaxName_b2,ptMaxName_b2, 25, 0, 50)
                self.hist[transDifName_b2] =  ROOT.TProfile(transDifName_b2,transDifName_b2, 25, 0, 50)
                self.hist[transDifNchName_b2] =  ROOT.TProfile(transDifNchName_b2,transDifNchName_b2, 25, 0, 50)
                self.hist[towardTotalName_b2] =  ROOT.TProfile(towardTotalName_b2,towardTotalName_b2, 25, 0, 50)
                self.hist[towardTotalNchName_b2] =  ROOT.TProfile(towardTotalNchName_b2,towardTotalNchName_b2, 25, 0, 50)
                self.hist[towardTotalAvgName_b2] =  ROOT.TProfile(towardTotalAvgName_b2,towardTotalAvgName_b2, 25, 0, 50)
                self.hist[overallTotalName_b2] =  ROOT.TProfile(overallTotalName_b2,overallTotalName_b2, 25, 0, 50)
                self.hist[overallTotalNchName_b2] =  ROOT.TProfile(overallTotalNchName_b2,overallTotalNchName_b2, 25, 0, 50)
                self.hist[overallTotalAvgName_b2] =  ROOT.TProfile(overallTotalAvgName_b2,overallTotalAvgName_b2, 25, 0, 50)

                #BIN 0.5
                self.hist[towardName_bh] =  ROOT.TProfile(towardName_bh, towardName_bh+";toward [pT]",  100,  0, 50)
                self.hist[awayName_bh] =  ROOT.TProfile(awayName_bh, awayName_bh+";away [pT]",  100,  0, 50)
                self.hist[transMaxName_bh] =  ROOT.TProfile(transMaxName_bh, transMaxName_bh+";transMax [pT]",  100,  0, 50)
                self.hist[transMinName_bh] =  ROOT.TProfile(transMinName_bh, transMinName_bh+";transMin [pT]",  100,  0, 50)
                self.hist[towardNchName_bh] =  ROOT.TProfile(towardNchName_bh, towardNchName_bh+";toward [Nch]",  100,  0, 50)
                self.hist[awayNchName_bh] =  ROOT.TProfile(awayNchName_bh, awayNchName_bh+";away [Nch]",  100,  0, 50)
                self.hist[transMaxNchName_bh] =  ROOT.TProfile(transMaxNchName_bh, transMaxNchName_bh+";transMax [Nch]",  100,  0, 50)
                self.hist[transMinNchName_bh] =  ROOT.TProfile(transMinNchName_bh, transMinNchName_bh+";transMin [Nch]",  100,  0, 50)

                self.hist[transName_bh] =  ROOT.TProfile(transName_bh, transName_bh+";trans [pT]",  100,  0, 50)
                self.hist[transNchName_bh] =  ROOT.TProfile(transNchName_bh, transNchName_bh+";trans [Nch]",  100,  0, 50)
                self.hist[transAvgName_bh] =  ROOT.TProfile(transAvgName_bh, transAvgName_bh+";trans [pT]",  100,  0, 50)
                self.hist[towardAvgName_bh] =  ROOT.TProfile(towardAvgName_bh, towardAvgName_bh+";toward [Avg pT]",  100,  0, 50)
                self.hist[awayAvgName_bh] =  ROOT.TProfile(awayAvgName_bh, awayAvgName_bh+";away [Avg pT]",  100,  0, 50)
                self.hist[overallName_bh] =  ROOT.TProfile(overallName_bh, overallName_bh+";overall [pT]",  100,  0, 50)
                self.hist[overallNchName_bh] =  ROOT.TProfile(overallNchName_bh, overallNchName_bh+";overall [Nch]",  100,  0, 50)
                self.hist[overallAvgName_bh] =  ROOT.TProfile(overallAvgName_bh, overallAvgName_bh+";overall [Avg pT]",  100,  0, 50)

                #BIN 1
                self.hist[towardName_b1] =  ROOT.TProfile(towardName_b1, towardName_b1+";toward [pT]",  50,  0, 50)
                self.hist[awayName_b1] =  ROOT.TProfile(awayName_b1, awayName_b1+";away [pT]",  50,  0, 50)
                self.hist[transMaxName_b1] =  ROOT.TProfile(transMaxName_b1, transMaxName_b1+";transMax [pT]",  50,  0, 50)
                self.hist[transMinName_b1] =  ROOT.TProfile(transMinName_b1, transMinName_b1+";transMin [pT]",  50,  0, 50)
                self.hist[towardNchName_b1] =  ROOT.TProfile(towardNchName_b1, towardNchName_b1+";toward [Nch]",  50,  0, 50)
                self.hist[awayNchName_b1] =  ROOT.TProfile(awayNchName_b1, awayNchName_b1+";away [Nch]",  50,  0, 50)
                self.hist[transMaxNchName_b1] =  ROOT.TProfile(transMaxNchName_b1, transMaxNchName_b1+";transMax [Nch]",  50,  0, 50)
                self.hist[transMinNchName_b1] =  ROOT.TProfile(transMinNchName_b1, transMinNchName_b1+";transMin [Nch]",  50,  0, 50)

                self.hist[transName_b1] =  ROOT.TProfile(transName_b1, transName_b1+";trans [pT]",  50,  0, 50)
                self.hist[transNchName_b1] =  ROOT.TProfile(transNchName_b1, transNchName_b1+";trans [Nch]",  50,  0, 50)
                self.hist[transAvgName_b1] =  ROOT.TProfile(transAvgName_b1, transAvgName_b1+";trans [pT]",  50,  0, 50)
                self.hist[towardAvgName_b1] =  ROOT.TProfile(towardAvgName_b1, towardAvgName_b1+";toward [Avg pT]",  50,  0, 50)
                self.hist[awayAvgName_b1] =  ROOT.TProfile(awayAvgName_b1, awayAvgName_b1+";away [Avg pT]",  50,  0, 50)
                self.hist[overallName_b1] =  ROOT.TProfile(overallName_b1, overallName_b1+";overall [pT]",  50,  0, 50)
                self.hist[overallNchName_b1] =  ROOT.TProfile(overallNchName_b1, overallNchName_b1+";overall [Nch]",  50,  0, 50)
                self.hist[overallAvgName_b1] =  ROOT.TProfile(overallAvgName_b1, overallAvgName_b1+";overall [Avg pT]",  50,  0, 50)

                #BIN 2
                self.hist[towardName_b2] =  ROOT.TProfile(towardName_b2, towardName_b2+";toward [pT]",  25,  0, 50)
                self.hist[awayName_b2] =  ROOT.TProfile(awayName_b2, awayName_b2+";away [pT]",  25,  0, 50)
                self.hist[transMaxName_b2] =  ROOT.TProfile(transMaxName_b2, transMaxName_b2+";transMax [pT]",  25,  0, 50)
                self.hist[transMinName_b2] =  ROOT.TProfile(transMinName_b2, transMinName_b2+";transMin [pT]",  25,  0, 50)
                self.hist[towardNchName_b2] =  ROOT.TProfile(towardNchName_b2, towardNchName_b2+";toward [Nch]",  25,  0, 50)
                self.hist[awayNchName_b2] =  ROOT.TProfile(awayNchName_b2, awayNchName_b2+";away [Nch]",  25,  0, 50)
                self.hist[transMaxNchName_b2] =  ROOT.TProfile(transMaxNchName_b2, transMaxNchName_b2+";transMax [Nch]",  25,  0, 50)
                self.hist[transMinNchName_b2] =  ROOT.TProfile(transMinNchName_b2, transMinNchName_b2+";transMin [Nch]",  25,  0, 50)

                self.hist[transName_b2] =  ROOT.TProfile(transName_b2, transName_b2+";trans [pT]",  25,  0, 50)
                self.hist[transNchName_b2] =  ROOT.TProfile(transNchName_b2, transNchName_b2+";trans [Nch]",  25,  0, 50)
                self.hist[transAvgName_b2] =  ROOT.TProfile(transAvgName_b2, transAvgName_b2+";trans [pT]",  25,  0, 50)
                self.hist[towardAvgName_b2] =  ROOT.TProfile(towardAvgName_b2, towardAvgName_b2+";toward [Avg pT]",  25,  0, 50)
                self.hist[awayAvgName_b2] =  ROOT.TProfile(awayAvgName_b2, awayAvgName_b2+";away [Avg pT]",  25,  0, 50)
                self.hist[overallName_b2] =  ROOT.TProfile(overallName_b2, overallName_b2+";overall [pT]",  25,  0, 50)
                self.hist[overallNchName_b2] =  ROOT.TProfile(overallNchName_b2, overallNchName_b2+";overall [Nch]",  25,  0, 50)
                self.hist[overallAvgName_b2] =  ROOT.TProfile(overallAvgName_b2, overallAvgName_b2+";overall [Avg pT]",  25,  0, 50)



                #GEN PLOTS

                #NEW 3-10-15

                self.hist[eta_all_Name_GEN] = ROOT.TH1F(eta_all_Name_GEN, eta_all_Name_GEN+";eta",  100,  -10, 10)

                #NEW GEN HISTOGRAMS 1-16-15
                self.hist[nch_all_Name_GEN] = ROOT.TH1F(nch_all_Name_GEN, nch_all_Name_GEN+";Nch",  100,  0, 100)
                self.hist[nch_eta_Name_GEN] = ROOT.TH1F(nch_eta_Name_GEN, nch_eta_Name_GEN+";Nch",  100,  0, 100)
                self.hist[nch_etaptH_Name_GEN] = ROOT.TH1F(nch_etaptH_Name_GEN, nch_etaptH_Name_GEN+";Nch",  100,  0, 100)
                self.hist[pt_all_Name_GEN] = ROOT.TH1F(pt_all_Name_GEN, pt_all_Name_GEN+";pt",  100,  0, 50)
                self.hist[pt_eta_Name_GEN] = ROOT.TH1F(pt_eta_Name_GEN, pt_eta_Name_GEN+";pt",  100,  0, 50)
                self.hist[pt_etaptH_Name_GEN] = ROOT.TH1F(pt_etaptH_Name_GEN, pt_etaptH_Name_GEN+";pt",  100,  0, 50)

                #HISTOGRAMS
                self.hist[ptMBName_GEN] =  ROOT.TH1F(ptMBName_GEN, ptMBName_GEN+";p_T [GeV]",  100,  0, 50)
                self.hist[etaMBName_GEN] =  ROOT.TH1F(etaMBName_GEN, etaMBName_GEN+"; #eta",  20, -2, 2)
                self.hist[etaName_GEN] =  ROOT.TH1F(etaName_GEN, etaName_GEN+"; #eta",  100, -10, 10)
                self.hist[ptName_GEN] =  ROOT.TH1F(ptName_GEN, ptName_GEN+";p_T [GeV]",  100,  0, 50)

                self.hist[delPhiName_GEN] =  ROOT.TH1F(delPhiName_GEN, delPhiName_GEN+";delPhi [deg]",  72,  -180, 180)
                self.hist[delPhiPtName_GEN] =  ROOT.TH1F(delPhiPtName_GEN, delPhiPtName_GEN+";delPhiPt [Pt deg]",  72,  -180, 180)
                self.hist[nchName_GEN] =  ROOT.TH1F(nchName_GEN, nchName_GEN+";Nch",  100,  0, 100)
                self.hist[ptSumName_GEN] =  ROOT.TH1F(ptSumName_GEN, ptSumName_GEN+";ptSum",  100,  0, 100)
                self.hist[nchMBName_GEN] =  ROOT.TH1F(nchMBName_GEN, nchMBName_GEN+";Nch",  100,  0, 100)
                self.hist[ptSumMBName_GEN] =  ROOT.TH1F(ptSumMBName_GEN, ptSumMBName_GEN+";ptSum",  100,  0, 100)
                self.hist[transNchName_GEN] =  ROOT.TH1F(transNchName_GEN, transNchName_GEN+";Nch",  100,  0, 100)
                self.hist[transPtSumName_GEN] =  ROOT.TH1F(transPtSumName_GEN, transPtSumName_GEN+";ptSum",  100,  0, 100)
                self.hist[transPtName_GEN] =  ROOT.TH1F(transPtName_GEN, transPtName_GEN+";pt",  100,  0, 50)
                self.hist[ptMaxName_GEN] = ROOT.TH1F(ptMaxName_GEN, ptMaxName_GEN+";pt", 100, 0, 50)

                #PT GREATER THAN 5 GeV/C
                self.hist[delPhiName_GEN_pt5] =  ROOT.TH1F(delPhiName_GEN_pt5, delPhiName_GEN_pt5+";delPhi [deg]",  72,  -180, 180)
                self.hist[delPhiPtName_GEN_pt5] =  ROOT.TH1F(delPhiPtName_GEN_pt5, delPhiPtName_GEN_pt5+";delPhiPt_pt5 [Pt deg]",  72,  -180, 180)
                self.hist[etaName_GEN_pt5] =  ROOT.TH1F(etaName_GEN_pt5, etaName_GEN_pt5+"; #eta",  20, -2, 2)
                self.hist[ptName_GEN_pt5] =  ROOT.TH1F(ptName_GEN_pt5, ptName_GEN_pt5+";p_T [GeV]",  100,  0, 50)
                self.hist[nchName_GEN_pt5] =  ROOT.TH1F(nchName_GEN_pt5, nchName_GEN_pt5+";Nch",  100,  0, 100)
                self.hist[ptSumName_GEN_pt5] =  ROOT.TH1F(ptSumName_GEN_pt5, ptSumName_GEN_pt5+";ptSum",  100,  0, 100)
                self.hist[transNchName_GEN_pt5] =  ROOT.TH1F(transNchName_GEN_pt5, transNchName_GEN_pt5+";Nch",  100,  0, 100)
                self.hist[transPtSumName_GEN_pt5] =  ROOT.TH1F(transPtSumName_GEN_pt5, transPtSumName_GEN_pt5+";ptSum",  100,  0, 100)
                self.hist[transPtName_GEN_pt5] =  ROOT.TH1F(transPtName_GEN_pt5, transPtName_GEN_pt5+";pt",  100,  0, 50)
                self.hist[trans12Name_GEN] = ROOT.TH1F(trans12Name_GEN, trans12Name_GEN, 3, -1.5, 1.5)
                self.hist[trans12Name_GEN_pt5] = ROOT.TH1F(trans12Name_GEN_pt5, trans12Name_GEN_pt5, 3, -1.5, 1.5)
                self.hist[phiName_GEN] =  ROOT.TH1F(phiName_GEN, phiName_GEN+";delPhi [deg]",  72,  -180, 180)
                self.hist[phiName_GEN_pt5] =  ROOT.TH1F(phiName_GEN_pt5, phiName_GEN_pt5+";delPhi [deg]",  72,  -180, 180)
                self.hist[phiMaxName_GEN] =  ROOT.TH1F(phiMaxName_GEN, phiMaxName_GEN+";delPhi [deg]",  72,  -180, 180)
                self.hist[phiMaxName_GEN_pt5] =  ROOT.TH1F(phiMaxName_GEN_pt5, phiMaxName_GEN_pt5+";delPhi [deg]",  72,  -180, 180)


                #PROFILES

                #NEW 10-20-14
                self.hist[ptMaxName_GEN_bh] =  ROOT.TProfile(ptMaxName_GEN_bh,ptMaxName_GEN_bh, 100, 0, 50)
                self.hist[transDifName_GEN_bh] =  ROOT.TProfile(transDifName_GEN_bh,transDifName_GEN_bh, 100, 0, 50)
                self.hist[transDifNchName_GEN_bh] =  ROOT.TProfile(transDifNchName_GEN_bh,transDifNchName_GEN_bh, 100, 0, 50)
                self.hist[towardTotalName_GEN_bh] =  ROOT.TProfile(towardTotalName_GEN_bh,towardTotalName_GEN_bh, 100, 0, 50)
                self.hist[towardTotalNchName_GEN_bh] =  ROOT.TProfile(towardTotalNchName_GEN_bh,towardTotalNchName_GEN_bh, 100, 0, 50)
                self.hist[towardTotalAvgName_GEN_bh] =  ROOT.TProfile(towardTotalAvgName_GEN_bh,towardTotalAvgName_GEN_bh, 100, 0, 50)
                self.hist[overallTotalName_GEN_bh] =  ROOT.TProfile(overallTotalName_GEN_bh,overallTotalName_GEN_bh, 100, 0, 50)
                self.hist[overallTotalNchName_GEN_bh] =  ROOT.TProfile(overallTotalNchName_GEN_bh,overallTotalNchName_GEN_bh, 100, 0, 50)
                self.hist[overallTotalAvgName_GEN_bh] =  ROOT.TProfile(overallTotalAvgName_GEN_bh,overallTotalAvgName_GEN_bh, 100, 0, 50)
                self.hist[ptMaxName_GEN_b1] =  ROOT.TProfile(ptMaxName_GEN_b1,ptMaxName_GEN_b1, 50, 0, 50)
                self.hist[transDifName_GEN_b1] =  ROOT.TProfile(transDifName_GEN_b1,transDifName_GEN_b1, 50, 0, 50)
                self.hist[transDifNchName_GEN_b1] =  ROOT.TProfile(transDifNchName_GEN_b1,transDifNchName_GEN_b1, 50, 0, 50)
                self.hist[towardTotalName_GEN_b1] =  ROOT.TProfile(towardTotalName_GEN_b1,towardTotalName_GEN_b1, 50, 0, 50)
                self.hist[towardTotalNchName_GEN_b1] =  ROOT.TProfile(towardTotalNchName_GEN_b1,towardTotalNchName_GEN_b1, 50, 0, 50)
                self.hist[towardTotalAvgName_GEN_b1] =  ROOT.TProfile(towardTotalAvgName_GEN_b1,towardTotalAvgName_GEN_b1, 50, 0, 50)
                self.hist[overallTotalName_GEN_b1] =  ROOT.TProfile(overallTotalName_GEN_b1,overallTotalName_GEN_b1, 50, 0, 50)
                self.hist[overallTotalNchName_GEN_b1] =  ROOT.TProfile(overallTotalNchName_GEN_b1,overallTotalNchName_GEN_b1, 50, 0, 50)
                self.hist[overallTotalAvgName_GEN_b1] =  ROOT.TProfile(overallTotalAvgName_GEN_b1,overallTotalAvgName_GEN_b1, 50, 0, 50)
                self.hist[ptMaxName_GEN_b2] =  ROOT.TProfile(ptMaxName_GEN_b2,ptMaxName_GEN_b2, 25, 0, 50)
                self.hist[transDifName_GEN_b2] =  ROOT.TProfile(transDifName_GEN_b2,transDifName_GEN_b2, 25, 0, 50)
                self.hist[transDifNchName_GEN_b2] =  ROOT.TProfile(transDifNchName_GEN_b2,transDifNchName_GEN_b2, 25, 0, 50)
                self.hist[towardTotalName_GEN_b2] =  ROOT.TProfile(towardTotalName_GEN_b2,towardTotalName_GEN_b2, 25, 0, 50)
                self.hist[towardTotalNchName_GEN_b2] =  ROOT.TProfile(towardTotalNchName_GEN_b2,towardTotalNchName_GEN_b2, 25, 0, 50)
                self.hist[towardTotalAvgName_GEN_b2] =  ROOT.TProfile(towardTotalAvgName_GEN_b2,towardTotalAvgName_GEN_b2, 25, 0, 50)
                self.hist[overallTotalName_GEN_b2] =  ROOT.TProfile(overallTotalName_GEN_b2,overallTotalName_GEN_b2, 25, 0, 50)
                self.hist[overallTotalNchName_GEN_b2] =  ROOT.TProfile(overallTotalNchName_GEN_b2,overallTotalNchName_GEN_b2, 25, 0, 50)
                self.hist[overallTotalAvgName_GEN_b2] =  ROOT.TProfile(overallTotalAvgName_GEN_b2,overallTotalAvgName_GEN_b2, 25, 0, 50)

                self.hist[ptMaxName_GEN_b4] =  ROOT.TProfile(ptMaxName_GEN_b4,ptMaxName_GEN_b4, 25, 0, 50)
                self.hist[transDifName_GEN_b4] =  ROOT.TProfile(transDifName_GEN_b4,transDifName_GEN_b4, 25, 0, 50)
                self.hist[transDifNchName_GEN_b4] =  ROOT.TProfile(transDifNchName_GEN_b4,transDifNchName_GEN_b4, 25, 0, 50)
                self.hist[towardTotalName_GEN_b4] =  ROOT.TProfile(towardTotalName_GEN_b4,towardTotalName_GEN_b4, 25, 0, 50)
                self.hist[towardTotalNchName_GEN_b4] =  ROOT.TProfile(towardTotalNchName_GEN_b4,towardTotalNchName_GEN_b4, 25, 0, 50)
                self.hist[towardTotalAvgName_GEN_b4] =  ROOT.TProfile(towardTotalAvgName_GEN_b4,towardTotalAvgName_GEN_b4, 25, 0, 50)
                self.hist[overallTotalName_GEN_b4] =  ROOT.TProfile(overallTotalName_GEN_b4,overallTotalName_GEN_b4, 25, 0, 50)
                self.hist[overallTotalNchName_GEN_b4] =  ROOT.TProfile(overallTotalNchName_GEN_b4,overallTotalNchName_GEN_b4, 25, 0, 50)
                self.hist[overallTotalAvgName_GEN_b4] =  ROOT.TProfile(overallTotalAvgName_GEN_b4,overallTotalAvgName_GEN_b4, 25, 0, 50)


                #BIN 0.5
                self.hist[towardName_GEN_bh] =  ROOT.TProfile(towardName_GEN_bh, towardName_GEN_bh+";toward [pT]",  100,  0, 50)
                self.hist[awayName_GEN_bh] =  ROOT.TProfile(awayName_GEN_bh, awayName_GEN_bh+";away [pT]",  100,  0, 50)
                self.hist[transMaxName_GEN_bh] =  ROOT.TProfile(transMaxName_GEN_bh, transMaxName_GEN_bh+";transMax [pT]",  100,  0, 50)
                self.hist[transMinName_GEN_bh] =  ROOT.TProfile(transMinName_GEN_bh, transMinName_GEN_bh+";transMin [pT]",  100,  0, 50)
                self.hist[towardNchName_GEN_bh] =  ROOT.TProfile(towardNchName_GEN_bh, towardNchName_GEN_bh+";toward [Nch]",  100,  0, 50)
                self.hist[awayNchName_GEN_bh] =  ROOT.TProfile(awayNchName_GEN_bh, awayNchName_GEN_bh+";away [Nch]",  100,  0, 50)
                self.hist[transMaxNchName_GEN_bh] =  ROOT.TProfile(transMaxNchName_GEN_bh, transMaxNchName_GEN_bh+";transMax [Nch]",  100,  0, 50)
                self.hist[transMinNchName_GEN_bh] =  ROOT.TProfile(transMinNchName_GEN_bh, transMinNchName_GEN_bh+";transMin [Nch]",  100,  0, 50)

                self.hist[transName_GEN_bh] =  ROOT.TProfile(transName_GEN_bh, transName_GEN_bh+";trans [pT]",  100,  0, 50)
                self.hist[transNchName_GEN_bh] =  ROOT.TProfile(transNchName_GEN_bh, transNchName_GEN_bh+";trans [Nch]",  100,  0, 50)
                self.hist[transAvgName_GEN_bh] =  ROOT.TProfile(transAvgName_GEN_bh, transAvgName_GEN_bh+";trans [pT]",  100,  0, 50)
                self.hist[towardAvgName_GEN_bh] =  ROOT.TProfile(towardAvgName_GEN_bh, towardAvgName_GEN_bh+";toward [Avg pT]",  100,  0, 50)
                self.hist[awayAvgName_GEN_bh] =  ROOT.TProfile(awayAvgName_GEN_bh, awayAvgName_GEN_bh+";away [Avg pT]",  100,  0, 50)
                self.hist[overallName_GEN_bh] =  ROOT.TProfile(overallName_GEN_bh, overallName_GEN_bh+";overall [pT]",  100,  0, 50)
                self.hist[overallNchName_GEN_bh] =  ROOT.TProfile(overallNchName_GEN_bh, overallNchName_GEN_bh+";overall [Nch]",  100,  0, 50)
                self.hist[overallAvgName_GEN_bh] =  ROOT.TProfile(overallAvgName_GEN_bh, overallAvgName_GEN_bh+";overall [Avg pT]",  100,  0, 50)

                #BIN 1
                self.hist[towardName_GEN_b1] =  ROOT.TProfile(towardName_GEN_b1, towardName_GEN_b1+";toward [pT]",  50,  0, 50)
                self.hist[awayName_GEN_b1] =  ROOT.TProfile(awayName_GEN_b1, awayName_GEN_b1+";away [pT]",  50,  0, 50)
                self.hist[transMaxName_GEN_b1] =  ROOT.TProfile(transMaxName_GEN_b1, transMaxName_GEN_b1+";transMax [pT]",  50,  0, 50)
                self.hist[transMinName_GEN_b1] =  ROOT.TProfile(transMinName_GEN_b1, transMinName_GEN_b1+";transMin [pT]",  50,  0, 50)
                self.hist[towardNchName_GEN_b1] =  ROOT.TProfile(towardNchName_GEN_b1, towardNchName_GEN_b1+";toward [Nch]",  50,  0, 50)
                self.hist[awayNchName_GEN_b1] =  ROOT.TProfile(awayNchName_GEN_b1, awayNchName_GEN_b1+";away [Nch]",  50,  0, 50)
                self.hist[transMaxNchName_GEN_b1] =  ROOT.TProfile(transMaxNchName_GEN_b1, transMaxNchName_GEN_b1+";transMax [Nch]",  50,  0, 50)
                self.hist[transMinNchName_GEN_b1] =  ROOT.TProfile(transMinNchName_GEN_b1, transMinNchName_GEN_b1+";transMin [Nch]",  50,  0, 50)

                self.hist[transName_GEN_b1] =  ROOT.TProfile(transName_GEN_b1, transName_GEN_b1+";trans [pT]",  50,  0, 50)
                self.hist[transNchName_GEN_b1] =  ROOT.TProfile(transNchName_GEN_b1, transNchName_GEN_b1+";trans [Nch]",  50,  0, 50)
                self.hist[transAvgName_GEN_b1] =  ROOT.TProfile(transAvgName_GEN_b1, transAvgName_GEN_b1+";trans [pT]",  50,  0, 50)
                self.hist[towardAvgName_GEN_b1] =  ROOT.TProfile(towardAvgName_GEN_b1, towardAvgName_GEN_b1+";toward [Avg pT]",  50,  0, 50)
                self.hist[awayAvgName_GEN_b1] =  ROOT.TProfile(awayAvgName_GEN_b1, awayAvgName_GEN_b1+";away [Avg pT]",  50,  0, 50)
                self.hist[overallName_GEN_b1] =  ROOT.TProfile(overallName_GEN_b1, overallName_GEN_b1+";overall [pT]",  50,  0, 50)
                self.hist[overallNchName_GEN_b1] =  ROOT.TProfile(overallNchName_GEN_b1, overallNchName_GEN_b1+";overall [Nch]",  50,  0, 50)
                self.hist[overallAvgName_GEN_b1] =  ROOT.TProfile(overallAvgName_GEN_b1, overallAvgName_GEN_b1+";overall [Avg pT]",  50,  0, 50)

                #BIN 2
                self.hist[towardName_GEN_b2] =  ROOT.TProfile(towardName_GEN_b2, towardName_GEN_b2+";toward [pT]",  25,  0, 50)
                self.hist[awayName_GEN_b2] =  ROOT.TProfile(awayName_GEN_b2, awayName_GEN_b2+";away [pT]",  25,  0, 50)
                self.hist[transMaxName_GEN_b2] =  ROOT.TProfile(transMaxName_GEN_b2, transMaxName_GEN_b2+";transMax [pT]",  25,  0, 50)
                self.hist[transMinName_GEN_b2] =  ROOT.TProfile(transMinName_GEN_b2, transMinName_GEN_b2+";transMin [pT]",  25,  0, 50)
                self.hist[towardNchName_GEN_b2] =  ROOT.TProfile(towardNchName_GEN_b2, towardNchName_GEN_b2+";toward [Nch]",  25,  0, 50)
                self.hist[awayNchName_GEN_b2] =  ROOT.TProfile(awayNchName_GEN_b2, awayNchName_GEN_b2+";away [Nch]",  25,  0, 50)
                self.hist[transMaxNchName_GEN_b2] =  ROOT.TProfile(transMaxNchName_GEN_b2, transMaxNchName_GEN_b2+";transMax [Nch]",  25,  0, 50)
                self.hist[transMinNchName_GEN_b2] =  ROOT.TProfile(transMinNchName_GEN_b2, transMinNchName_GEN_b2+";transMin [Nch]",  25,  0, 50)

                self.hist[transName_GEN_b2] =  ROOT.TProfile(transName_GEN_b2, transName_GEN_b2+";trans [pT]",  25,  0, 50)
                self.hist[transNchName_GEN_b2] =  ROOT.TProfile(transNchName_GEN_b2, transNchName_GEN_b2+";trans [Nch]",  25,  0, 50)
                self.hist[transAvgName_GEN_b2] =  ROOT.TProfile(transAvgName_GEN_b2, transAvgName_GEN_b2+";trans [pT]",  25,  0, 50)
                self.hist[towardAvgName_GEN_b2] =  ROOT.TProfile(towardAvgName_GEN_b2, towardAvgName_GEN_b2+";toward [Avg pT]",  25,  0, 50)
                self.hist[awayAvgName_GEN_b2] =  ROOT.TProfile(awayAvgName_GEN_b2, awayAvgName_GEN_b2+";away [Avg pT]",  25,  0, 50)
                self.hist[overallName_GEN_b2] =  ROOT.TProfile(overallName_GEN_b2, overallName_GEN_b2+";overall [pT]",  25,  0, 50)
                self.hist[overallNchName_GEN_b2] =  ROOT.TProfile(overallNchName_GEN_b2, overallNchName_GEN_b2+";overall [Nch]",  25,  0, 50)
                self.hist[overallAvgName_GEN_b2] =  ROOT.TProfile(overallAvgName_GEN_b2, overallAvgName_GEN_b2+";overall [Avg pT]",  25,  0, 50)

                #BIN 4
                self.hist[towardName_GEN_b4] =  ROOT.TProfile(towardName_GEN_b4, towardName_GEN_b4+";toward [pT]",  12,  0, 48)
                self.hist[awayName_GEN_b4] =  ROOT.TProfile(awayName_GEN_b4, awayName_GEN_b4+";away [pT]",  12,  0, 48)
                self.hist[transMaxName_GEN_b4] =  ROOT.TProfile(transMaxName_GEN_b4, transMaxName_GEN_b4+";transMax [pT]",  12,  0, 48)
                self.hist[transMinName_GEN_b4] =  ROOT.TProfile(transMinName_GEN_b4, transMinName_GEN_b4+";transMin [pT]",  12,  0, 48)
                self.hist[towardNchName_GEN_b4] =  ROOT.TProfile(towardNchName_GEN_b4, towardNchName_GEN_b4+";toward [Nch]",  12,  0, 48)
                self.hist[awayNchName_GEN_b4] =  ROOT.TProfile(awayNchName_GEN_b4, awayNchName_GEN_b4+";away [Nch]",  12,  0, 48)
                self.hist[transMaxNchName_GEN_b4] =  ROOT.TProfile(transMaxNchName_GEN_b4, transMaxNchName_GEN_b4+";transMax [Nch]",  12,  0, 48)
                self.hist[transMinNchName_GEN_b4] =  ROOT.TProfile(transMinNchName_GEN_b4, transMinNchName_GEN_b4+";transMin [Nch]",  12,  0, 48)

                self.hist[transName_GEN_b4] =  ROOT.TProfile(transName_GEN_b4, transName_GEN_b4+";trans [pT]",  12,  0, 48)
                self.hist[transNchName_GEN_b4] =  ROOT.TProfile(transNchName_GEN_b4, transNchName_GEN_b4+";trans [Nch]",  12,  0, 48)
                self.hist[transAvgName_GEN_b4] =  ROOT.TProfile(transAvgName_GEN_b4, transAvgName_GEN_b4+";trans [pT]",  12,  0, 48)
                self.hist[towardAvgName_GEN_b4] =  ROOT.TProfile(towardAvgName_GEN_b4, towardAvgName_GEN_b4+";toward [Avg pT]",  12,  0, 48)
                self.hist[awayAvgName_GEN_b4] =  ROOT.TProfile(awayAvgName_GEN_b4, awayAvgName_GEN_b4+";away [Avg pT]",  12,  0, 48)
                self.hist[overallName_GEN_b4] =  ROOT.TProfile(overallName_GEN_b4, overallName_GEN_b4+";overall [pT]",  12,  0, 48)
                self.hist[overallNchName_GEN_b4] =  ROOT.TProfile(overallNchName_GEN_b4, overallNchName_GEN_b4+";overall [Nch]",  12,  0, 48)
                self.hist[overallAvgName_GEN_b4] =  ROOT.TProfile(overallAvgName_GEN_b4, overallAvgName_GEN_b4+";overall [Avg pT]",  12,  0, 48)




                self.Nch_response = RooUnfoldResponse(100, 0, 100, "Nch_response_name", "Nch_response_title");
                self.Nch_response2 = RooUnfoldResponse(100, 0, 100, "Nch_response_name2", "Nch_response_title2");

                #self.hist[CUT_TFF_TTF_NchMB_Name] = ROOT.TH2F(CUT_TFF_TTF_NchMB_Name,CUT_TFF_TTF_NchMB_Name, 100, -0.5, 99.5, 100, -99.5, 0.5)

                #self.hist["2DHIST_transAvgName_GEN_bh"] =  ROOT.TH2F("2DHIST_transAvgName_GEN_bh","2DHIST_transAvgName_GEN_bh",  200,  0, 100, 2000, 0, 20);

                #self.hist["2DHIST_transAvgName_bh"] =  ROOT.TH2F("2DHIST_transAvgName_bh","2DHIST_transAvgName_bh",  200,  0, 100, 2000, 0, 20);




                #BE VERY CAREFUL IN ALLOCATING SPACE!!!!  A BIG TH2F TAKES A LOT OF SPACE!!!

                #self.hist["2DHIST_transAvgName_GEN_bh"] =  ROOT.TH2F("2DHIST_transAvgName_GEN_bh","2DHIST_transAvgName_GEN_bh",  100,  0, 50, 50, 0, 10);

                #self.hist["2DHIST_transAvgName_bh"] =  ROOT.TH2F("2DHIST_transAvgName_bh","2DHIST_transAvgName_bh",  100,  0, 50, 50, 0, 10);
		"""
                self.hist["2DHIST_transAvgName_GEN_bh"] =  ROOT.TH2F("2DHIST_transAvgName_GEN_bh","2DHIST_transAvgName_GEN_bh",  100,  0, 50, 20, 0, 10);

                self.hist["2DHIST_transAvgName_bh"] =  ROOT.TH2F("2DHIST_transAvgName_bh","2DHIST_transAvgName_bh",  100,  0, 50, 20, 0, 10);

                self.transName_response = RooUnfoldResponse(self.hist["2DHIST_transAvgName_bh"], self.hist["2DHIST_transAvgName_GEN_bh"], "transName_response", "transName_response_title");


                self.hist["2DHIST_transNchName_GEN_bh"] =  ROOT.TH2F("2DHIST_transNchName_GEN_bh","2DHIST_transNchName_GEN_bh",  100,  0, 50, 50, -0.5, 49.5);
                self.hist["2DHIST_transNchName_bh"] =  ROOT.TH2F("2DHIST_transNchName_bh","2DHIST_transNchName_bh",  100,  0, 50, 50, -0.5, 49.5);

                self.transNch_response = RooUnfoldResponse(self.hist["2DHIST_transNchName_bh"], self.hist["2DHIST_transNchName_GEN_bh"], "transNch_Unfold", "transNch_Unfold_title");



                self.hist["2DHIST_transName_GEN_bh"] =  ROOT.TH2F("2DHIST_transName_GEN_bh","2DHIST_transName_GEN_bh",  100,  0, 50, 80, 0.5, 20.5);
                self.hist["2DHIST_transName_bh"] =  ROOT.TH2F("2DHIST_transName_bh","2DHIST_transName_bh",  100,  0, 50, 80, 0.5, 20.5);

                self.trans_response = RooUnfoldResponse(self.hist["2DHIST_transName_bh"], self.hist["2DHIST_transName_GEN_bh"], "trans_Unfold", "trans_Unfold_title");
		"""


                #self.trans_response = RooUnfoldResponse(self.hist[transName_bh], self.hist[transName_GEN_bh]);
                #self.transNch_response = RooUnfoldResponse(self.hist[transNchName_bh], self.hist[transNchName_GEN_bh]);



        for h in self.hist:
            self.hist[h].Sumw2()
            self.GetOutputList().Add(self.hist[h])


#####ATTEMPT TO MAKE A PLOT LIST#######
        f = open("plotlist.txt", "w")
        print "We try to open plotlist.txt"
        for h in self.hist:
            #print "Write", h
            f.write(h)
            f.write("\n")

        f.close()
#####END ATTEMPT#######################

        self.tracks = RecoTracksGetter("recoTracks")

        self.gentracks = GenParticlesGetter("genParticles")

    def analyze(self):
        weight = 1 # 
        # weight = self.fChain.genWeight to obtain gen level weight. For min bias datasets we are using for CSA14 always eq to 1

        # direct access to branch to compare efficiency as when getter is used:
        #for i in xrange(self.fChain.recoTracksrecoTracks.size()):
        #    trackp4 = self.fChain.recoTracksrecoTracks.at(i)


        histPrefix = "HIST_"
        binHalf = "_bh"
        binOne = "_b1"
        binTwo = "_b2"
	binFour = "_b4"
        genPrefix = "GEN_"

        ETAMAX = 0.8

        #HISTOGRAMS
        #Nch_response_Name = histPrefix+"Nch_response"


        ptMaxName_GEN_b4 = genPrefix+"ptMax"+binFour
        towardName_GEN_b4 = genPrefix+"toward"+binFour
        awayName_GEN_b4 = genPrefix+"away"+binFour
        transMaxName_GEN_b4 = genPrefix+"transMax"+binFour
        transMinName_GEN_b4 = genPrefix+"transMin"+binFour
        towardNchName_GEN_b4 = genPrefix+"towardNch"+binFour
        awayNchName_GEN_b4 = genPrefix+"awayNch"+binFour
        transMaxNchName_GEN_b4 = genPrefix+"transMaxNch"+binFour
        transMinNchName_GEN_b4 = genPrefix+"transMinNch"+binFour

        transDifName_GEN_b4 = genPrefix+"transDif"+binFour
        transDifNchName_GEN_b4 = genPrefix+"transDifNch"+binFour
        towardTotalName_GEN_b4= genPrefix+"towardTotal"+binFour
        towardTotalNchName_GEN_b4= genPrefix+"towardTotalNch"+binFour
        towardTotalAvgName_GEN_b4= genPrefix+"towardTotalAvg"+binFour
        overallTotalName_GEN_b4= genPrefix+"overallTotal"+binFour
        overallTotalNchName_GEN_b4= genPrefix+"overallTotalNch"+binFour
        overallTotalAvgName_GEN_b4= genPrefix+"overallTotalAvg"+binFour        

        transName_GEN_b4 = genPrefix+"trans"+binFour
        transNchName_GEN_b4 = genPrefix+"transNch"+binFour
        transAvgName_GEN_b4 = genPrefix+"transAvg"+binFour
        towardAvgName_GEN_b4 = genPrefix+"towardAvg"+binFour
        awayAvgName_GEN_b4 = genPrefix+"awayAvg"+binFour
        overallName_GEN_b4 = genPrefix+"overall"+binFour
        overallNchName_GEN_b4 = genPrefix+"overallNch"+binFour
        overallAvgName_GEN_b4 = genPrefix+"overallAvg"+binFour

        #CUT ANALYSIS HISTOGRAMS

        CUT_FFF_eta_Name = histPrefix+"CUT_FFF_eta"
        CUT_TFF_eta_Name = histPrefix+"CUT_TFF_eta"
        CUT_TTF_eta_Name = histPrefix+"CUT_TTF_eta"
        CUT_TTT_eta_Name = histPrefix+"CUT_TTT_eta"
        CUT_TFT_eta_Name = histPrefix+"CUT_TFT_eta"

        CUT_FFF_phi_Name = histPrefix+"CUT_FFF_phi"
        CUT_TFF_phi_Name = histPrefix+"CUT_TFF_phi"
        CUT_TTF_phi_Name = histPrefix+"CUT_TTF_phi"
        CUT_TTT_phi_Name = histPrefix+"CUT_TTT_phi"
        CUT_TFT_phi_Name = histPrefix+"CUT_TFT_phi"

        dZ_vs_vtxZ_Name = "dZ_vs_vtxZ"

        CUT_TFF_TTF_NchMB_Name = histPrefix+"CUT_TFF_TTF_NchMB"

        CUT_TFF_NchMB_Name = histPrefix+"CUT_TFF_NchMB"
        CUT_TTF_NchMB_Name = histPrefix+"CUT_TTF_NchMB"
        CUT_TTT_NchMB_Name = histPrefix+"CUT_TTT_NchMB"

        CUT_TFF_d0_Name = histPrefix+"CUT_TFF_d0"
        CUT_TTF_d0_Name = histPrefix+"CUT_TTF_d0"
        CUT_TTT_d0_Name = histPrefix+"CUT_TTT_d0"

        CUT_TFF_dz_Name = histPrefix+"CUT_TFF_dz"
        CUT_TTF_dz_Name = histPrefix+"CUT_TTF_dz"
        CUT_TTT_dz_Name = histPrefix+"CUT_TTT_dz"

        CUT_TFF_d0dzMax_Name = histPrefix+"CUT_TFF_d0dzMax"
        CUT_TTF_d0dzMax_Name = histPrefix+"CUT_TTF_d0dzMax"
        CUT_TTT_d0dzMax_Name = histPrefix+"CUT_TTT_d0dzMax"

        CUT_TFT_NchMB_Name = histPrefix+"CUT_TFT_NchMB"
        CUT_TFT_d0_Name = histPrefix+"CUT_TFT_d0"
        CUT_TFT_dz_Name = histPrefix+"CUT_TFT_dz"
        CUT_TFT_d0dzMax_Name = histPrefix+"CUT_TFT_d0dzMax"

        CUT_FFF_NchMB_Name = histPrefix+"CUT_FFF_NchMB"
        CUT_FFF_d0_Name = histPrefix+"CUT_FFF_d0"
        CUT_FFF_dz_Name = histPrefix+"CUT_FFF_dz"
        CUT_FFF_d0dzMax_Name = histPrefix+"CUT_FFF_d0dzMax"

        VTX_nTrk_Name = histPrefix+"VTX_nTrk"
        VTX_ndof_Name = histPrefix+"VTX_ndof"
        VTX_Zpos_Name = histPrefix+"VTX_Zpos"
        VTX_chi2_Name = histPrefix+"VTX_chi2"

        TRK_PtErr_Name = histPrefix+"TRK_PtErr"

        CUT_FFF_PtErr_Name = histPrefix+"CUT_FFF_PtErr"
        CUT_TFF_PtErr_Name = histPrefix+"CUT_TFF_PtErr"
        CUT_TTF_PtErr_Name = histPrefix+"CUT_TTF_PtErr"
        CUT_TTT_PtErr_Name = histPrefix+"CUT_TTT_PtErr"
        CUT_TFT_PtErr_Name = histPrefix+"CUT_TFT_PtErr"



        #NEW PLOTS 3-24-15

        eta_ptH_Name_GEN = genPrefix+histPrefix+"eta_ptH"
        phi_all_Name_GEN = genPrefix+histPrefix+"phi_all"
        phi_eta_Name_GEN = genPrefix+histPrefix+"phi_eta"
        phi_etaptH_Name_GEN = genPrefix+histPrefix+"phi_etaptH"

        eta_ptH_Name = histPrefix+"eta_ptH"
        phi_etaptH_Name = histPrefix+"phi_etaptH"

        phi_ptH_Name_GEN = genPrefix+histPrefix+"phi_ptH"



        ptMBName = histPrefix+"ptMB" #+histPostfix
        etaMBName = histPrefix+"etaMB" #+histPostfix
        ptName = histPrefix+"pt" #+histPostfix
        etaName = histPrefix+"eta" #+histPostfix
        delPhiName = histPrefix+"delPhi" #+histPostfix
        delPhiPtName = histPrefix+"delPhiPt" #+histPostfix
        nchName = histPrefix+"nch" #+histPostfix
        ptSumName = histPrefix+"ptSum" #+histPostfix
        nchMBName = histPrefix+"nchMB" #+histPostfix
        ptSumMBName = histPrefix+"ptSumMB" #+histPostfix
        transNchName = histPrefix+"transNch" #+histPostfix
        transPtSumName = histPrefix+"transPtSum" #+histPostfix
        transPtName = histPrefix+"transPt" #+histPostfix
        ptMaxName = histPrefix+"ptMax"

        trans12Name = histPrefix+"trans12"
        trans12Name_pt5 = histPrefix+"trans12_pt5"

        phiName = histPrefix+"phi"
        phiMaxName = histPrefix+"phiMax"
        phiName_pt5 = histPrefix+"phi_pt5"
        phiMaxName_pt5 = histPrefix+"phiMax_pt5"
        #PT GREATER THAN 5 GeV/C

        delPhiName_pt5 = histPrefix+"delPhi_pt5" #+histPostfix
        delPhiPtName_pt5 = histPrefix+"delPhiPt_pt5" #+histPostfix
        etaName_pt5 = histPrefix+"eta_pt5" #+histPostfix
        ptName_pt5 = histPrefix+"pt_pt5" #+histPostfix
        nchName_pt5 = histPrefix+"nch_pt5" #+histPostfix
        ptSumName_pt5 = histPrefix+"ptSum_pt5" #+histPostfix
        transNchName_pt5 = histPrefix+"transNch_pt5" #+histPostfix
        transPtSumName_pt5 = histPrefix+"transPtSum_pt5" #+histPostfix
        transPtName_pt5 = histPrefix+"transPt_pt5" #+histPostfix



        #PROFILES

        #BIN 0.5

        ptMaxName_bh = "ptMax"+binHalf
        towardName_bh = "toward"+binHalf
        awayName_bh = "away"+binHalf
        transMaxName_bh = "transMax"+binHalf
        transMinName_bh = "transMin"+binHalf
        towardNchName_bh = "towardNch"+binHalf
        awayNchName_bh = "awayNch"+binHalf
        transMaxNchName_bh = "transMaxNch"+binHalf
        transMinNchName_bh = "transMinNch"+binHalf

        transDifName_bh = "transDif"+binHalf
        transDifNchName_bh = "transDifNch"+binHalf
        towardTotalName_bh= "towardTotal"+binHalf
        towardTotalNchName_bh= "towardTotalNch"+binHalf
        towardTotalAvgName_bh= "towardTotalAvg"+binHalf
        overallTotalName_bh= "overallTotal"+binHalf
        overallTotalNchName_bh= "overallTotalNch"+binHalf
        overallTotalAvgName_bh= "overallTotalAvg"+binHalf

        transName_bh = "trans"+binHalf
        transNchName_bh = "transNch"+binHalf
        transAvgName_bh = "transAvg"+binHalf
        towardAvgName_bh = "towardAvg"+binHalf
        awayAvgName_bh = "awayAvg"+binHalf
        overallName_bh = "overall"+binHalf
        overallNchName_bh = "overallNch"+binHalf
        overallAvgName_bh = "overallAvg"+binHalf



        #BIN 1
        ptMaxName_b1 = "ptMax"+binOne
        towardName_b1 = "toward"+binOne
        awayName_b1 = "away"+binOne
        transMaxName_b1 = "transMax"+binOne
        transMinName_b1 = "transMin"+binOne
        towardNchName_b1 = "towardNch"+binOne
        awayNchName_b1 = "awayNch"+binOne
        transMaxNchName_b1 = "transMaxNch"+binOne
        transMinNchName_b1 = "transMinNch"+binOne

        transDifName_b1 = "transDif"+binOne
        transDifNchName_b1 = "transDifNch"+binOne
        towardTotalName_b1= "towardTotal"+binOne
        towardTotalNchName_b1= "towardTotalNch"+binOne
        towardTotalAvgName_b1= "towardTotalAvg"+binOne
        overallTotalName_b1= "overallTotal"+binOne
        overallTotalNchName_b1= "overallTotalNch"+binOne
        overallTotalAvgName_b1= "overallTotalAvg"+binOne        

        transName_b1 = "trans"+binOne
        transNchName_b1 = "transNch"+binOne
        transAvgName_b1 = "transAvg"+binOne
        towardAvgName_b1 = "towardAvg"+binOne
        awayAvgName_b1 = "awayAvg"+binOne
        overallName_b1 = "overall"+binOne
        overallNchName_b1 = "overallNch"+binOne
        overallAvgName_b1 = "overallAvg"+binOne


        #BIN 2
        ptMaxName_b2 = "ptMax"+binTwo
        towardName_b2 = "toward"+binTwo
        awayName_b2 = "away"+binTwo
        transMaxName_b2 = "transMax"+binTwo
        transMinName_b2 = "transMin"+binTwo
        towardNchName_b2 = "towardNch"+binTwo
        awayNchName_b2 = "awayNch"+binTwo
        transMaxNchName_b2 = "transMaxNch"+binTwo
        transMinNchName_b2 = "transMinNch"+binTwo

        transDifName_b2 = "transDif"+binTwo
        transDifNchName_b2 = "transDifNch"+binTwo
        towardTotalName_b2= "towardTotal"+binTwo
        towardTotalNchName_b2= "towardTotalNch"+binTwo
        towardTotalAvgName_b2= "towardTotalAvg"+binTwo
        overallTotalName_b2= "overallTotal"+binTwo
        overallTotalNchName_b2= "overallTotalNch"+binTwo
        overallTotalAvgName_b2= "overallTotalAvg"+binTwo        

        transName_b2 = "trans"+binTwo
        transNchName_b2 = "transNch"+binTwo
        transAvgName_b2 = "transAvg"+binTwo
        towardAvgName_b2 = "towardAvg"+binTwo
        awayAvgName_b2 = "awayAvg"+binTwo
        overallName_b2 = "overall"+binTwo
        overallNchName_b2 = "overallNch"+binTwo
        overallAvgName_b2 = "overallAvg"+binTwo

        #GEN PLOTS

        #NEW 3-10-15

        eta_all_Name_GEN = genPrefix+histPrefix+"eta_all"

        #NEW GEN HISTOGRAMS 1-16-15

        nch_all_Name_GEN = genPrefix+histPrefix+"nch_all"
        nch_eta_Name_GEN = genPrefix+histPrefix+"nch_eta"
        nch_etaptH_Name_GEN = genPrefix+histPrefix+"nch_etaptH"

        pt_all_Name_GEN = genPrefix+histPrefix+"pt_all"
        pt_eta_Name_GEN = genPrefix+histPrefix+"pt_eta"
        pt_etaptH_Name_GEN = genPrefix+histPrefix+"pt_etaptH"

        #HISTOGRAMS
        ptMBName_GEN = genPrefix+histPrefix+"ptMB" #+histPostfix
        etaMBName_GEN = genPrefix+histPrefix+"etaMB" #+histPostfix
        ptName_GEN = genPrefix+histPrefix+"pt" #+histPostfix
        etaName_GEN = genPrefix+histPrefix+"eta" #+histPostfix
        delPhiName_GEN = genPrefix+histPrefix+"delPhi" #+histPostfix
        delPhiPtName_GEN = genPrefix+histPrefix+"delPhiPt" #+histPostfix
        nchName_GEN = genPrefix+histPrefix+"nch" #+histPostfix
        ptSumName_GEN = genPrefix+histPrefix+"ptSum" #+histPostfix
        nchMBName_GEN = genPrefix+histPrefix+"nchMB" #+histPostfix
        ptSumMBName_GEN = genPrefix+histPrefix+"ptSumMB" #+histPostfix
        transNchName_GEN = genPrefix+histPrefix+"transNch" #+histPostfix
        transPtSumName_GEN = genPrefix+histPrefix+"transPtSum" #+histPostfix
        transPtName_GEN = genPrefix+histPrefix+"transPt" #+histPostfix
        ptMaxName_GEN = genPrefix+histPrefix+"ptMax"

        trans12Name_GEN = genPrefix+histPrefix+"trans12"
        trans12Name_GEN_pt5 = genPrefix+histPrefix+"trans12_pt5"

        phiName_GEN = genPrefix+histPrefix+"phi"
        phiMaxName_GEN = genPrefix+histPrefix+"phiMax"
        phiName_GEN_pt5 = genPrefix+histPrefix+"phi_pt5"
        phiMaxName_GEN_pt5 = genPrefix+histPrefix+"phiMax_pt5"

        #PT GREATER THAN 5 GeV/C

        delPhiName_GEN_pt5 = genPrefix+histPrefix+"delPhi_pt5" #+histPostfix
        delPhiPtName_GEN_pt5 = genPrefix+histPrefix+"delPhiPt_pt5" #+histPostfix
        etaName_GEN_pt5 = genPrefix+histPrefix+"eta_pt5" #+histPostfix
        ptName_GEN_pt5 = genPrefix+histPrefix+"pt_pt5" #+histPostfix
        nchName_GEN_pt5 = genPrefix+histPrefix+"nch_pt5" #+histPostfix
        ptSumName_GEN_pt5 = genPrefix+histPrefix+"ptSum_pt5" #+histPostfix
        transNchName_GEN_pt5 = genPrefix+histPrefix+"transNch_pt5" #+histPostfix
        transPtSumName_GEN_pt5 = genPrefix+histPrefix+"transPtSum_pt5" #+histPostfix
        transPtName_GEN_pt5 = genPrefix+histPrefix+"transPt_pt5" #+histPostfix



        #PROFILES

        #BIN 0.5

        ptMaxName_GEN_bh = genPrefix+"ptMax"+binHalf
        towardName_GEN_bh = genPrefix+"toward"+binHalf
        awayName_GEN_bh = genPrefix+"away"+binHalf
        transMaxName_GEN_bh = genPrefix+"transMax"+binHalf
        transMinName_GEN_bh = genPrefix+"transMin"+binHalf
        towardNchName_GEN_bh = genPrefix+"towardNch"+binHalf
        awayNchName_GEN_bh = genPrefix+"awayNch"+binHalf
        transMaxNchName_GEN_bh = genPrefix+"transMaxNch"+binHalf
        transMinNchName_GEN_bh = genPrefix+"transMinNch"+binHalf

        transDifName_GEN_bh = genPrefix+"transDif"+binHalf
        transDifNchName_GEN_bh = genPrefix+"transDifNch"+binHalf
        towardTotalName_GEN_bh= genPrefix+"towardTotal"+binHalf
        towardTotalNchName_GEN_bh= genPrefix+"towardTotalNch"+binHalf
        towardTotalAvgName_GEN_bh= genPrefix+"towardTotalAvg"+binHalf
        overallTotalName_GEN_bh= genPrefix+"overallTotal"+binHalf
        overallTotalNchName_GEN_bh= genPrefix+"overallTotalNch"+binHalf
        overallTotalAvgName_GEN_bh= genPrefix+"overallTotalAvg"+binHalf

        transName_GEN_bh = genPrefix+"trans"+binHalf
        transNchName_GEN_bh = genPrefix+"transNch"+binHalf
        transAvgName_GEN_bh = genPrefix+"transAvg"+binHalf
        towardAvgName_GEN_bh = genPrefix+"towardAvg"+binHalf
        awayAvgName_GEN_bh = genPrefix+"awayAvg"+binHalf
        overallName_GEN_bh = genPrefix+"overall"+binHalf
        overallNchName_GEN_bh = genPrefix+"overallNch"+binHalf
        overallAvgName_GEN_bh = genPrefix+"overallAvg"+binHalf



        #BIN 1
        ptMaxName_GEN_b1 = genPrefix+"ptMax"+binOne
        towardName_GEN_b1 = genPrefix+"toward"+binOne
        awayName_GEN_b1 = genPrefix+"away"+binOne
        transMaxName_GEN_b1 = genPrefix+"transMax"+binOne
        transMinName_GEN_b1 = genPrefix+"transMin"+binOne
        towardNchName_GEN_b1 = genPrefix+"towardNch"+binOne
        awayNchName_GEN_b1 = genPrefix+"awayNch"+binOne
        transMaxNchName_GEN_b1 = genPrefix+"transMaxNch"+binOne
        transMinNchName_GEN_b1 = genPrefix+"transMinNch"+binOne

        transDifName_GEN_b1 = genPrefix+"transDif"+binOne
        transDifNchName_GEN_b1 = genPrefix+"transDifNch"+binOne
        towardTotalName_GEN_b1= genPrefix+"towardTotal"+binOne
        towardTotalNchName_GEN_b1= genPrefix+"towardTotalNch"+binOne
        towardTotalAvgName_GEN_b1= genPrefix+"towardTotalAvg"+binOne
        overallTotalName_GEN_b1= genPrefix+"overallTotal"+binOne
        overallTotalNchName_GEN_b1= genPrefix+"overallTotalNch"+binOne
        overallTotalAvgName_GEN_b1= genPrefix+"overallTotalAvg"+binOne        

        transName_GEN_b1 = genPrefix+"trans"+binOne
        transNchName_GEN_b1 = genPrefix+"transNch"+binOne
        transAvgName_GEN_b1 = genPrefix+"transAvg"+binOne
        towardAvgName_GEN_b1 = genPrefix+"towardAvg"+binOne
        awayAvgName_GEN_b1 = genPrefix+"awayAvg"+binOne
        overallName_GEN_b1 = genPrefix+"overall"+binOne
        overallNchName_GEN_b1 = genPrefix+"overallNch"+binOne
        overallAvgName_GEN_b1 = genPrefix+"overallAvg"+binOne


        #BIN 2
        ptMaxName_GEN_b2 = genPrefix+"ptMax"+binTwo
        towardName_GEN_b2 = genPrefix+"toward"+binTwo
        awayName_GEN_b2 = genPrefix+"away"+binTwo
        transMaxName_GEN_b2 = genPrefix+"transMax"+binTwo
        transMinName_GEN_b2 = genPrefix+"transMin"+binTwo
        towardNchName_GEN_b2 = genPrefix+"towardNch"+binTwo
        awayNchName_GEN_b2 = genPrefix+"awayNch"+binTwo
        transMaxNchName_GEN_b2 = genPrefix+"transMaxNch"+binTwo
        transMinNchName_GEN_b2 = genPrefix+"transMinNch"+binTwo

        transDifName_GEN_b2 = genPrefix+"transDif"+binTwo
        transDifNchName_GEN_b2 = genPrefix+"transDifNch"+binTwo
        towardTotalName_GEN_b2= genPrefix+"towardTotal"+binTwo
        towardTotalNchName_GEN_b2= genPrefix+"towardTotalNch"+binTwo
        towardTotalAvgName_GEN_b2= genPrefix+"towardTotalAvg"+binTwo
        overallTotalName_GEN_b2= genPrefix+"overallTotal"+binTwo
        overallTotalNchName_GEN_b2= genPrefix+"overallTotalNch"+binTwo
        overallTotalAvgName_GEN_b2= genPrefix+"overallTotalAvg"+binTwo        

        transName_GEN_b2 = genPrefix+"trans"+binTwo
        transNchName_GEN_b2 = genPrefix+"transNch"+binTwo
        transAvgName_GEN_b2 = genPrefix+"transAvg"+binTwo
        towardAvgName_GEN_b2 = genPrefix+"towardAvg"+binTwo
        awayAvgName_GEN_b2 = genPrefix+"awayAvg"+binTwo
        overallName_GEN_b2 = genPrefix+"overall"+binTwo
        overallNchName_GEN_b2 = genPrefix+"overallNch"+binTwo
        overallAvgName_GEN_b2 = genPrefix+"overallAvg"+binTwo




        self.tracks.newEvent(self.fChain)

        self.gentracks.newEvent(self.fChain)

        self.eventCounter += 1

        #if self.eventCounter == 10000: sys.exit("You have set the program to exit at 10000 events!")

        #IS it possible this trigger step skips events? -DR
        for trg in self.triggers: # iterate over all triggers we use
            trigger = False
            if trg == "minbias":
                trigger = True  # TODO in future versions: actually check for trigger
            elif trg == "zerobias":
                trigger = True  # TODO: as above

            if not trigger: continue

            # iterate over all variations (again - placs is a placeeholder for future)
            #  eg.  if we would use jets our variations would look like
            #   ["central", "jecUp", "jecDown"]  
            #   our JetGetter (not used here) is smart enough to give jets with momentum variaed for +1sigma
            #     when calling self.jetGetter.get("jecUp") (and -1sigma for jecDown)
            for variation in self.variations: 
                #histPostfix = "_" + variation + "_" + trg




                #NOW WE DO THE SAME THING AT GEN LEVEL

                #i_track = 0
                pTsumToward = 0
                pTsumTrans1 = 0
                pTsumTrans2 = 0
                pTsumAway = 0
                NchToward = 0
                NchTrans1 = 0
                NchTrans2 = 0
                NchAway = 0
                ptMax = 0

                NchTrans = 0
                pTsumTrans = 0

                Nch = 0
                pTsum = 0

                #etaphi = 8*math.pi/3
                #etaphi_half = 4*math.pi/3
                #etaphi_three = 8*math.pi
                etaphi = 1
                etaphi_half = 1
                etaphi_three = 1

                i_ptMax = -1
                #i_track = 0
                firstTime = True

                N_all = 0
                N_eta = 0
                N_etaptH = 0

                print "We start a new event"
                #GEN
                #THIS IS JUST THE LOOP TO FIND PTMAX!!!
                for i_track, track in enumerate(self.gentracks.get(variation)):
                    #if firstTime == False: i_track += 1
                    #firstTime = False
                    trackp4 = track.p4 # wrong naming in Samples_CSA14_Tracks_20140904 skim. 
                                               # this will evolve to trackp4 = track.p4 in next version

		    #trackp4 = track
                    eta = trackp4.eta()
                    pt =    trackp4.pt()
                    phi = trackp4.phi()
                    #print "event", self.eventCounter
                    #print "eta pt phi", eta, pt, phi
                    if pt < 0.5: continue
                    if math.fabs(eta) > ETAMAX: continue

                    #if self.fChain.genTrackscharge == 0:
                    if track.charge == 0: continue
                    #print "track is charged", track.charge
                    #self.hist[ptMBName_GEN].Fill(pt, weight)
                
                    if(pt > ptMax):
                        ptMax = pt
                        phiMax = phi
                        i_ptMax = i_track
                        #print "new phiMax", phiMax
                
                    #i_track += 1

                #GEN

                for i_track, track in enumerate(self.gentracks.get(variation)):
                    trackp4 = track.p4 # wrong naming in Samples_CSA14_Tracks_20140904 skim. 
                                               # this will evolve to trackp4 = track.p4 in next version

                    etaptH_inc = False
                    NchMB_inc = False
                    if N_all == 0: one_pTmax = False
 
                    eta = trackp4.eta()
                    pt =    trackp4.pt()
                    phi = trackp4.phi()

                    #if track.status == 0:
                    #    print "GEN PART WITH STATUS 0 @ INDEX", i_track
                    #    continue

                    N_all += 1

                    self.hist[pt_all_Name_GEN].Fill(pt, weight)
                    self.hist[eta_all_Name_GEN].Fill(eta, weight)

                    self.hist[phi_all_Name_GEN].Fill(phi*180/math.pi, weight)

                    if math.fabs(eta) <= ETAMAX: 
                        N_eta += 1
                        self.hist[pt_eta_Name_GEN].Fill(pt, weight)
                        self.hist[phi_eta_Name_GEN].Fill(phi*180/math.pi, weight)

                    if pt >= 0.5: 
                        self.hist[eta_ptH_Name_GEN].Fill(eta, weight)
                        self.hist[phi_ptH_Name_GEN].Fill(phi*180/math.pi, weight)

                    if math.fabs(eta) <= ETAMAX and pt >= 0.5: 
                        N_etaptH += 1
                        self.hist[pt_etaptH_Name_GEN].Fill(pt, weight)
                        self.hist[phi_etaptH_Name_GEN].Fill(phi*180/math.pi, weight)
                        etaptH_inc = True

                    if math.fabs(eta) > ETAMAX or pt < 0.5 or track.charge == 0:
                        continue




                    if i_track == i_ptMax:
                        if one_pTmax: 
                            print "WARNING, YOU HAVE MORE THAN ONE PTMAX"
                            print i_track, i_ptMax, pt, Nch, N_etaptH
                        ptMax = pt
                        phiMax = phi
                        #self.hist[intentionalBREAK].Fill(pt, weight)
                        self.hist[ptMBName_GEN].Fill(pt, weight)
                        self.hist[etaMBName_GEN].Fill(eta, weight)
                        self.hist[ptMaxName_GEN].Fill(ptMax, weight)
                        self.hist[ptMaxName_GEN_bh].Fill(ptMax, ptMax, weight)
                        self.hist[ptMaxName_GEN_b1].Fill(ptMax, ptMax, weight)
                        self.hist[ptMaxName_GEN_b2].Fill(ptMax, ptMax, weight)

                        self.hist[phiMaxName_GEN].Fill(phiMax*180/math.pi, weight)
                        if ptMax > 5: self.hist[phiMaxName_GEN_pt5].Fill(phiMax*180/math.pi, weight)

                        one_pTmax = True
                        NchMB_inc = True
                        #print "ptMax = ", ptMax
                    if i_track != i_ptMax:
                        #phiMax = 2.0
                        #print "WARNING: phiMax is set to 2.0 for bug check"
                        delPhi = phiMax - phi
                        if delPhi > math.pi:
                            delPhi -= 2*math.pi
                        if delPhi < -math.pi:
                            delPhi += 2*math.pi
                        delPhiDeg = delPhi*180/math.pi

                        self.hist[phiName_GEN].Fill(phi*180/math.pi, weight)
                        if ptMax > 5: self.hist[phiName_GEN_pt5].Fill(phi*180/math.pi, weight)

                        #print "PhiMax = ", phiMax
                        #print "phi    = ", phi
                        #print "delPhi = ", delPhi
                        #print "degree = ", delPhiDeg
                        #print " \n "
                        #print "pt = ", pt

                        Nch += 1
                        pTsum += pt

                        NchMB_inc = True


                        if math.fabs(delPhi) < math.pi/3:
                            pTsumToward += pt
                            NchToward += 1
                        if math.fabs(delPhi) > math.pi*2/3:
                            pTsumAway += pt
                            NchAway += 1
                        if delPhi >= math.pi/3 and delPhi <= math.pi*2/3:
                            pTsumTrans1 += pt
                            NchTrans1 += 1
                            self.hist[trans12Name_GEN].Fill(1, weight)
                            if ptMax < 5: self.hist[trans12Name_GEN_pt5].Fill(1, weight)
                        if delPhi <= -math.pi/3 and delPhi >= -math.pi*2/3:
                            pTsumTrans2 += pt
                            NchTrans2 += 1
                            self.hist[trans12Name_GEN].Fill(-1, weight)
                            if ptMax < 5: self.hist[trans12Name_GEN_pt5].Fill(-1, weight)

                        if math.fabs(delPhi) >= math.pi/3 and math.fabs(delPhi) <= math.pi*2/3:
                            pTsumTrans += pt
                            NchTrans += 1

                            self.hist[transPtName_GEN].Fill(pt, weight)
                            if ptMax > 5: self.hist[transPtName_GEN_pt5].Fill(pt, weight)


                        self.hist[ptMBName_GEN].Fill(pt, weight)
                        self.hist[etaMBName_GEN].Fill(eta, weight)

                        self.hist[ptName_GEN].Fill(pt, weight)
                        self.hist[etaName_GEN].Fill(eta, weight)

                        self.hist[delPhiName_GEN].Fill(delPhiDeg, weight)
                        self.hist[delPhiPtName_GEN].Fill(delPhiDeg, pt)

                        if ptMax > 5:
                            self.hist[delPhiName_GEN_pt5].Fill(delPhiDeg, weight)
                            self.hist[delPhiPtName_GEN_pt5].Fill(delPhiDeg, pt)
                            self.hist[ptName_GEN_pt5].Fill(pt, weight)
                            self.hist[etaName_GEN_pt5].Fill(eta, weight)          

                    #i_track += 1

                    if NchMB_inc and not etaptH_inc:
                        print "WARNING: NchMB was inced but pteta5 was not!"
                        print i_track, i_ptMax, pt, Nch, N_etaptH

                #END PARTICLE LOOP


                self.hist[nch_all_Name_GEN].Fill(N_all, weight)
                self.hist[nch_eta_Name_GEN].Fill(N_eta, weight)
                self.hist[nch_etaptH_Name_GEN].Fill(N_etaptH, weight)

                if ptMax != 0:

                    #self.hist[nch_all_Name_GEN].Fill(N_all, weight)
                    #self.hist[nch_eta_Name_GEN].Fill(N_eta, weight)
                    #self.hist[nch_etaptH_Name_GEN].Fill(N_etaptH, weight)

                    self.hist[ptSumName_GEN].Fill(pTsum, weight)
                    self.hist[nchName_GEN].Fill(Nch, weight)
                    self.hist[ptSumMBName_GEN].Fill(pTsum+ptMax, weight)
                    self.hist[nchMBName_GEN].Fill(Nch+1, weight)

                    self.hist[transPtSumName_GEN].Fill(pTsumTrans, weight)
                    self.hist[transNchName_GEN].Fill(NchTrans, weight)


                    if ptMax > 5:
                        self.hist[ptSumName_GEN_pt5].Fill(pTsum, weight)
                        self.hist[nchName_GEN_pt5].Fill(Nch, weight)
                        self.hist[transPtSumName_GEN_pt5].Fill(pTsumTrans, weight)
                        self.hist[transNchName_GEN_pt5].Fill(NchTrans, weight)

                    self.hist[towardName_GEN_bh].Fill(ptMax, pTsumToward/etaphi, weight)
                    self.hist[awayName_GEN_bh].Fill(ptMax, pTsumAway/etaphi, weight)
                    if NchToward != 0: self.hist[towardAvgName_GEN_bh].Fill(ptMax, (pTsumToward/NchToward), weight)
                    if NchAway != 0: self.hist[awayAvgName_GEN_bh].Fill(ptMax, (pTsumAway/NchAway), weight)
                    self.hist[transName_GEN_bh].Fill(ptMax, pTsumTrans/etaphi, weight)
                    self.hist[transNchName_GEN_bh].Fill(ptMax, NchTrans/etaphi, weight)
                    if NchTrans != 0: self.hist[transAvgName_GEN_bh].Fill(ptMax, (pTsumTrans/NchTrans), weight)
                    self.hist[overallName_GEN_bh].Fill(ptMax, pTsum/(etaphi_three), weight)
                    self.hist[overallNchName_GEN_bh].Fill(ptMax, Nch/(etaphi_three), weight)
                    if Nch != 0: self.hist[overallAvgName_GEN_bh].Fill(ptMax, (pTsum/Nch), weight)

                    self.hist[towardTotalName_GEN_bh].Fill(ptMax, (pTsumToward+ptMax)/etaphi, weight)
                    self.hist[towardTotalNchName_GEN_bh].Fill(ptMax, (NchToward+1)/etaphi, weight)
                    if NchToward != 0: self.hist[towardTotalAvgName_GEN_bh].Fill(ptMax, ( (pTsumToward+ptMax)/(NchToward+1) ), weight)
                    self.hist[overallTotalName_GEN_bh].Fill(ptMax, (pTsum+ptMax)/(etaphi_three), weight)
                    self.hist[overallTotalNchName_GEN_bh].Fill(ptMax, (Nch+1)/(etaphi_three), weight)
                    if Nch != 0: self.hist[overallTotalAvgName_GEN_bh].Fill(ptMax, ( (pTsum+ptMax)/(Nch+1) ), weight)

                    self.hist[towardName_GEN_b1].Fill(ptMax, pTsumToward/etaphi, weight)
                    self.hist[awayName_GEN_b1].Fill(ptMax, pTsumAway/etaphi, weight)
                    if NchToward != 0: self.hist[towardAvgName_GEN_b1].Fill(ptMax, (pTsumToward/NchToward), weight)
                    if NchAway != 0: self.hist[awayAvgName_GEN_b1].Fill(ptMax, (pTsumAway/NchAway), weight)
                    self.hist[transName_GEN_b1].Fill(ptMax, pTsumTrans/etaphi, weight)
                    self.hist[transNchName_GEN_b1].Fill(ptMax, NchTrans/etaphi, weight)
                    if NchTrans != 0: self.hist[transAvgName_GEN_b1].Fill(ptMax, (pTsumTrans/NchTrans), weight)
                    self.hist[overallName_GEN_b1].Fill(ptMax, pTsum/(etaphi_three), weight)
                    self.hist[overallNchName_GEN_b1].Fill(ptMax, Nch/(etaphi_three), weight)
                    if Nch != 0: self.hist[overallAvgName_GEN_b1].Fill(ptMax, (pTsum/Nch), weight)

                    self.hist[towardTotalName_GEN_b1].Fill(ptMax, (pTsumToward+ptMax)/etaphi, weight)
                    self.hist[towardTotalNchName_GEN_b1].Fill(ptMax, (NchToward+1)/etaphi, weight)
                    if NchToward != 0: self.hist[towardTotalAvgName_GEN_b1].Fill(ptMax, ( (pTsumToward+ptMax)/(NchToward+1) ), weight)
                    self.hist[overallTotalName_GEN_b1].Fill(ptMax, (pTsum+ptMax)/(etaphi_three), weight)
                    self.hist[overallTotalNchName_GEN_b1].Fill(ptMax, (Nch+1)/(etaphi_three), weight)
                    if Nch != 0: self.hist[overallTotalAvgName_GEN_b1].Fill(ptMax, ( (pTsum+ptMax)/(Nch+1) ), weight)

                    self.hist[towardName_GEN_b2].Fill(ptMax, pTsumToward/etaphi, weight)
                    self.hist[awayName_GEN_b2].Fill(ptMax, pTsumAway/etaphi, weight)
                    if NchToward != 0: self.hist[towardAvgName_GEN_b2].Fill(ptMax, (pTsumToward/NchToward), weight)
                    if NchAway != 0: self.hist[awayAvgName_GEN_b2].Fill(ptMax, (pTsumAway/NchAway), weight)
                    self.hist[transName_GEN_b2].Fill(ptMax, pTsumTrans/etaphi, weight)
                    self.hist[transNchName_GEN_b2].Fill(ptMax, NchTrans/etaphi, weight)
                    if NchTrans != 0: self.hist[transAvgName_GEN_b2].Fill(ptMax, (pTsumTrans/NchTrans), weight)
                    self.hist[overallName_GEN_b2].Fill(ptMax, pTsum/(etaphi_three), weight)
                    self.hist[overallNchName_GEN_b2].Fill(ptMax, Nch/(etaphi_three), weight)
                    if Nch != 0: self.hist[overallAvgName_GEN_b2].Fill(ptMax, (pTsum/Nch), weight)

                    self.hist[towardTotalName_GEN_b2].Fill(ptMax, (pTsumToward+ptMax)/etaphi, weight)
                    self.hist[towardTotalNchName_GEN_b2].Fill(ptMax, (NchToward+1)/etaphi, weight)
                    if NchToward != 0: self.hist[towardTotalAvgName_GEN_b2].Fill(ptMax, ( (pTsumToward+ptMax)/(NchToward+1) ), weight)
                    self.hist[overallTotalName_GEN_b2].Fill(ptMax, (pTsum+ptMax)/(etaphi_three), weight)
                    self.hist[overallTotalNchName_GEN_b2].Fill(ptMax, (Nch+1)/(etaphi_three), weight)
                    if Nch != 0: self.hist[overallTotalAvgName_GEN_b2].Fill(ptMax, ( (pTsum+ptMax)/(Nch+1) ), weight)

                    self.hist[towardName_GEN_b4].Fill(ptMax, pTsumToward/etaphi, weight)
                    self.hist[awayName_GEN_b4].Fill(ptMax, pTsumAway/etaphi, weight)
                    if NchToward != 0: self.hist[towardAvgName_GEN_b4].Fill(ptMax, (pTsumToward/NchToward), weight)
                    if NchAway != 0: self.hist[awayAvgName_GEN_b4].Fill(ptMax, (pTsumAway/NchAway), weight)
                    self.hist[transName_GEN_b4].Fill(ptMax, pTsumTrans/etaphi, weight)
                    self.hist[transNchName_GEN_b4].Fill(ptMax, NchTrans/etaphi, weight)
                    if NchTrans != 0: self.hist[transAvgName_GEN_b4].Fill(ptMax, (pTsumTrans/NchTrans), weight)
                    self.hist[overallName_GEN_b4].Fill(ptMax, pTsum/(etaphi_three), weight)
                    self.hist[overallNchName_GEN_b4].Fill(ptMax, Nch/(etaphi_three), weight)
                    if Nch != 0: self.hist[overallAvgName_GEN_b4].Fill(ptMax, (pTsum/Nch), weight)

                    self.hist[towardTotalName_GEN_b4].Fill(ptMax, (pTsumToward+ptMax)/etaphi, weight)
                    self.hist[towardTotalNchName_GEN_b4].Fill(ptMax, (NchToward+1)/etaphi, weight)
                    if NchToward != 0: self.hist[towardTotalAvgName_GEN_b4].Fill(ptMax, ( (pTsumToward+ptMax)/(NchToward+1) ), weight)
                    self.hist[overallTotalName_GEN_b4].Fill(ptMax, (pTsum+ptMax)/(etaphi_three), weight)
                    self.hist[overallTotalNchName_GEN_b4].Fill(ptMax, (Nch+1)/(etaphi_three), weight)
                    if Nch != 0: self.hist[overallTotalAvgName_GEN_b4].Fill(ptMax, ( (pTsum+ptMax)/(Nch+1) ), weight)




                    if pTsumTrans1 > pTsumTrans2:
                        self.hist[transMaxName_GEN_bh].Fill(ptMax, pTsumTrans1/(etaphi_half), weight) # always use weight when filling
                        self.hist[transMinName_GEN_bh].Fill(ptMax, pTsumTrans2/(etaphi_half), weight) # always use weight when filling
                        self.hist[transMaxName_GEN_b1].Fill(ptMax, pTsumTrans1/(etaphi_half), weight) # always use weight when filling
                        self.hist[transMinName_GEN_b1].Fill(ptMax, pTsumTrans2/(etaphi_half), weight) # always use weight when filling
                        self.hist[transMaxName_GEN_b2].Fill(ptMax, pTsumTrans1/(etaphi_half), weight) # always use weight when filling
                        self.hist[transMinName_GEN_b2].Fill(ptMax, pTsumTrans2/(etaphi_half), weight) # always use weight when filling
                        self.hist[transMaxName_GEN_b4].Fill(ptMax, pTsumTrans1/(etaphi_half), weight) # always use weight when filling
                        self.hist[transMinName_GEN_b4].Fill(ptMax, pTsumTrans2/(etaphi_half), weight) # always use weight when filling

                    else:
                        self.hist[transMinName_GEN_bh].Fill(ptMax, pTsumTrans1/(etaphi_half), weight) # always use weight when filling
                        self.hist[transMaxName_GEN_bh].Fill(ptMax, pTsumTrans2/(etaphi_half), weight) # always use weight when filling
                        self.hist[transMinName_GEN_b1].Fill(ptMax, pTsumTrans1/(etaphi_half), weight) # always use weight when filling
                        self.hist[transMaxName_GEN_b1].Fill(ptMax, pTsumTrans2/(etaphi_half), weight) # always use weight when filling
                        self.hist[transMinName_GEN_b2].Fill(ptMax, pTsumTrans1/(etaphi_half), weight) # always use weight when filling
                        self.hist[transMaxName_GEN_b2].Fill(ptMax, pTsumTrans2/(etaphi_half), weight) # always use weight when filling
                        self.hist[transMinName_GEN_b4].Fill(ptMax, pTsumTrans1/(etaphi_half), weight) # always use weight when filling
                        self.hist[transMaxName_GEN_b4].Fill(ptMax, pTsumTrans2/(etaphi_half), weight) # always use weight when filling

                        
                    self.hist[towardNchName_GEN_bh].Fill(ptMax, NchToward/etaphi, weight) # always use weight when filling
                    self.hist[awayNchName_GEN_bh].Fill(ptMax, NchAway/etaphi, weight) # always use weight when filling
                    self.hist[towardNchName_GEN_b1].Fill(ptMax, NchToward/etaphi, weight) # always use weight when filling
                    self.hist[awayNchName_GEN_b1].Fill(ptMax, NchAway/etaphi, weight) # always use weight when filling
                    self.hist[towardNchName_GEN_b2].Fill(ptMax, NchToward/etaphi, weight) # always use weight when filling
                    self.hist[awayNchName_GEN_b2].Fill(ptMax, NchAway/etaphi, weight) # always use weight when filling
                    self.hist[towardNchName_GEN_b4].Fill(ptMax, NchToward/etaphi, weight) # always use weight when filling
                    self.hist[awayNchName_GEN_b4].Fill(ptMax, NchAway/etaphi, weight) # always use weight when filling


                    self.hist[transDifName_GEN_bh].Fill(ptMax, math.fabs(pTsumTrans1-pTsumTrans2)/(etaphi_half), weight)
                    self.hist[transDifNchName_GEN_bh].Fill(ptMax, math.fabs(NchTrans1-NchTrans2)/(etaphi_half), weight)
                    self.hist[transDifName_GEN_b1].Fill(ptMax, math.fabs(pTsumTrans1-pTsumTrans2)/(etaphi_half), weight)
                    self.hist[transDifNchName_GEN_b1].Fill(ptMax, math.fabs(NchTrans1-NchTrans2)/(etaphi_half), weight)
                    self.hist[transDifName_GEN_b2].Fill(ptMax, math.fabs(pTsumTrans1-pTsumTrans2)/(etaphi_half), weight)
                    self.hist[transDifNchName_GEN_b2].Fill(ptMax, math.fabs(NchTrans1-NchTrans2)/(etaphi_half), weight)
                    self.hist[transDifName_GEN_b4].Fill(ptMax, math.fabs(pTsumTrans1-pTsumTrans2)/(etaphi_half), weight)
                    self.hist[transDifNchName_GEN_b4].Fill(ptMax, math.fabs(NchTrans1-NchTrans2)/(etaphi_half), weight)


                    if NchTrans1 > NchTrans2:
                        self.hist[transMaxNchName_GEN_bh].Fill(ptMax, NchTrans1/(etaphi_half), weight) # always use weight when filling
                        self.hist[transMinNchName_GEN_bh].Fill(ptMax, NchTrans2/(etaphi_half), weight) # always use weight when filling
                        self.hist[transMaxNchName_GEN_b1].Fill(ptMax, NchTrans1/(etaphi_half), weight) # always use weight when filling
                        self.hist[transMinNchName_GEN_b1].Fill(ptMax, NchTrans2/(etaphi_half), weight) # always use weight when filling
                        self.hist[transMaxNchName_GEN_b2].Fill(ptMax, NchTrans1/(etaphi_half), weight) # always use weight when filling
                        self.hist[transMinNchName_GEN_b2].Fill(ptMax, NchTrans2/(etaphi_half), weight) # always use weight when filling
                        self.hist[transMaxNchName_GEN_b4].Fill(ptMax, NchTrans1/(etaphi_half), weight) # always use weight when filling
                        self.hist[transMinNchName_GEN_b4].Fill(ptMax, NchTrans2/(etaphi_half), weight) # always use weight when filling

                    else:
                        self.hist[transMinNchName_GEN_bh].Fill(ptMax, NchTrans1/(etaphi_half), weight) # always use weight when filling
                        self.hist[transMaxNchName_GEN_bh].Fill(ptMax, NchTrans2/(etaphi_half), weight) # always use weight when filling
                        self.hist[transMinNchName_GEN_b1].Fill(ptMax, NchTrans1/(etaphi_half), weight) # always use weight when filling
                        self.hist[transMaxNchName_GEN_b1].Fill(ptMax, NchTrans2/(etaphi_half), weight) # always use weight when filling
                        self.hist[transMinNchName_GEN_b2].Fill(ptMax, NchTrans1/(etaphi_half), weight) # always use weight when filling
                        self.hist[transMaxNchName_GEN_b2].Fill(ptMax, NchTrans2/(etaphi_half), weight) # always use weight when filling
                        self.hist[transMinNchName_GEN_b4].Fill(ptMax, NchTrans1/(etaphi_half), weight) # always use weight when filling
                        self.hist[transMaxNchName_GEN_b4].Fill(ptMax, NchTrans2/(etaphi_half), weight) # always use weight when filling





                    #if NchTrans != 0: self.hist["2DHIST_transAvgName_GEN_bh"].Fill(ptMax, (pTsumTrans/NchTrans), weight)
                    #self.hist["2DHIST_transNchName_GEN_bh"].Fill(ptMax, NchTrans/etaphi, weight)

                    #self.hist["2DHIST_transName_GEN_bh"].Fill(ptMax, pTsumTrans, weight)


		#SIM REMOVED HERE!

		#END SIM REMOVE!



    # note: this is executed on the slave (ie output will appear in logs),
    #       - before merging the histograms. Here we should apply the histogram 
    #         normalization factor (since this depend on how many events were processed
    #         by given slave)
    def finalize(self):
        print "Finalize:"
        normFactor = self.getNormalizationFactor()
        print "  isData", self.isData




        #Temporarily commented out because it takes a LOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOONG time.
        '''
        self.transAvg_unfold = RooUnfoldBayes(self.transName_response, self.hist["2DHIST_transAvgName_bh"], 3);
        self.transAvg_RECO = self.transAvg_unfold.Hreco();
        self.GetOutputList().Add(self.transAvg_RECO);
        '''
        #self.Nch_unfold2 = RooUnfoldBayes(self.Nch_response2, self.hist["HIST_nch"], 30);
        #self.Nch_RECO2 = self.Nch_unfold2.Hreco();
        #self.GetOutputList().Add(self.Nch_RECO2);


	'''
        unfoldStartTime = time.time()

        self.Nch_unfold = RooUnfoldBayes(self.Nch_response, self.hist["HIST_nchMB"], 4);
        self.Nch_RECO = self.Nch_unfold.Hreco();
        self.GetOutputList().Add(self.Nch_RECO);


        self.transNch_unfold = RooUnfoldBayes(self.transNch_response, self.hist["2DHIST_transNchName_bh"], 2);
        self.transNch_RECO = self.transNch_unfold.Hreco();
        self.GetOutputList().Add(self.transNch_RECO);


        unfoldEndTime = time.time()

        unfoldTime = unfoldEndTime - unfoldStartTime

        print "Unfolding transNch took %d seconds." % unfoldTime

        unfoldStartTime = time.time()

        self.trans_unfold = RooUnfoldBayes(self.trans_response, self.hist["2DHIST_transName_bh"], 2);
        self.trans_RECO = self.trans_unfold.Hreco();
        self.GetOutputList().Add(self.trans_RECO);


        unfoldEndTime = time.time()

        unfoldTime = unfoldEndTime - unfoldStartTime

        print "Unfolding trans took %d seconds." % unfoldTime
	'''


        #self.Nch_RECO = ROOT.(* self.Nch_unfold.Hreco() );
        #self.GetOutputList().Add(self.Nch_RECO);

        #self.hist["XXXXXX"] =  ROOT.TH1F(XXXXXX, XXXXXX,  10,  0, 10)
        #self.hist["XXXXXX"].Fill[5]
        #self.hist["XXXXXX"].Fill[8]
        #self.GetOutputList().Add(self.hist["XXXXXX"])


        #self.Nch_unfold = RooUnfoldBayes(self.Nch_response, self.hist["HIST_nch"], 4);
        #ROOT.TH1F Nch_RECO = self.Nch_unfold.Hreco();
        #self.GetOutputList().Add(self.Nch_RECO);
        '''
        self.trans_unfold = RooUnfoldBayes(self.trans_response, self.hist["trans_bh"], 4);
        self.trans_RECO = self.trans_unfold.Hreco();
        self.GetOutputList().Add(self.trans_RECO);

        self.transNch_unfold = RooUnfoldBayes(self.transNch_response, self.hist["transNch_bh"], 4);
        self.transNch_RECO = self.transNch_unfold.Hreco();
        self.GetOutputList().Add(self.transNch_RECO);
        '''



        #print "  applying norm",  normFactor
        #I HAVE TEMPORARILY DISABLED THIS BECAUSE IT APPEARS TO MESS UP PROFILE PLOTS
        #for h in self.hist:
        #    self.hist[h].Scale(normFactor)

    # this is executed once at the master after merging the histograms from slaves
    # (note: all histograms registered via self.GetOutputList().Add above are merged)
    def finalizeWhenMerged(self):
        #olist =  self.GetOutputList() # rebuild the histos list
        #histos = {}
        #for o in olist:
        #    if not "TH1" in o.ClassName(): continue
        #    histos[o.GetName()]=o

        #self.YYYYYY =  ROOT.TH1F(YYYYYY, YYYYYY,  10,  0, 10)
        #self.YYYYYY.Fill[2]
        #self.GetOutputList().Add(self.YYYYYY);


        #
        # you can save further histograms to the output file by calling:
        #self.GetOutputList().Add(myNewHisto)
        #
        pass


if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    ROOT.gSystem.Load("libFWCoreFWLite.so")
    ROOT.AutoLibraryLoader.enable()

    sampleList = None
    maxFilesMC = None
    maxFilesData = None
    nWorkers = None # "None" to Use all cores

    #quickTest = False
    quickTest = True
    
    if quickTest:
        # Run printTTree.py alone to get the samples list
        #sampleList = []
        #sampleList.append("data_MinBias_TuneCUETP8S1-HERAPDF_13TeV-pythia8")
        maxFilesMC = 1
        maxFilesData = 1
        nWorkers = None

    # another possibility to process bit faster: process only part of MC
    #maxFilesMC = 4
    #maxFilesData = 4
    #nWorkers = 1

    # only processin part of data will lead to wrong normalization of the data histograms
    # - since lumi values are not automatically updated to reflect the fact that only
    # part of sample was processed
    #
    # This is not a problem for MC, while here normalization factor is calculated using
    # number of processed events


    slaveParams = {}
    slaveParams["maxEta"] = 2. #This is not implemented yet? -DR


    # use printTTree.py <sampleName> to see what trees are avaliable inside the skim file
    #CSA14_dndeta_GENTEST.runAll(treeName="GenLevelTree",
    CSA14_dndeta_GENTEST.runAll(treeName="UETree",
                               slaveParameters=slaveParams,
                               sampleList=sampleList,
                               maxFilesMC = maxFilesMC,
                               maxFilesData = maxFilesData,
                               nWorkers=nWorkers,
                               outFile = "plots_GENTEST_7-18-15.root" )





