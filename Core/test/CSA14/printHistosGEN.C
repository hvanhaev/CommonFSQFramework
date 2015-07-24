



	//	#include "MZ_Selector_test_11_09_10.h"
	#include "TROOT.h"
	#include "TH2.h"
	#include "TH1.h"
	#include "TProfile.h"
	#include <TStyle.h>
	#include <iostream>
	#include <iomanip>
	#include "math.h" 
	#include "TCanvas.h"
	#include "TFile.h"
	#include "TTree.h"
	#include "TChain.h"
	#include "TProfile.h"
	#include "TPaveText.h"
	//	#include "TCanvas.h"
	#include "TLegend.h"
	#include <stdio.h>
	#include <stdlib.h>
	#include "TMath.h"
	#include "TInterpreter.h"
	#include "Print.h"
	#include "TDCacheFile.h"
	#include "TMatrixD.h"
	#include "TVectorD.h"
	#include "TMatrixDEigen.h"
	//	#include "TestFunc.h"
	#include <fstream>
	#include <time.h>
	#include <string.h>


	using namespace std;



	void printHistosGEN ()
	{



	TFile *fhist = new TFile("plotsGENTUNES.root");


	fhist->cd("MinBias_TuneEE5C_13TeV-herwigpp");

	TCanvas *c1 = new TCanvas("c1","c1",600,400);

cout << "MAKE SURE TO YOU ARE NOT LOADING THE TEST ROOT FILE!!!!!!" << endl;



TH1F *GEN_HIST_eta_ptH;
gDirectory->GetObject("GEN_HIST_eta_ptH",GEN_HIST_eta_ptH);
PrintHistogram(GEN_HIST_eta_ptH,1,1,"text/MinBias_TuneEE5C_13TeV-herwigpp/GEN/GEN_HIST_eta_ptH.txt");

TH1F *GEN_HIST_phi_all;
gDirectory->GetObject("GEN_HIST_phi_all",GEN_HIST_phi_all);
PrintHistogram(GEN_HIST_phi_all,1,1,"text/MinBias_TuneEE5C_13TeV-herwigpp/GEN/GEN_HIST_phi_all.txt");

TH1F *GEN_HIST_phi_eta;
gDirectory->GetObject("GEN_HIST_phi_eta",GEN_HIST_phi_eta);
PrintHistogram(GEN_HIST_phi_eta,1,1,"text/MinBias_TuneEE5C_13TeV-herwigpp/GEN/GEN_HIST_phi_eta.txt");

TH1F *GEN_HIST_phi_etaptH;
gDirectory->GetObject("GEN_HIST_phi_etaptH",GEN_HIST_phi_etaptH);
PrintHistogram(GEN_HIST_phi_etaptH,1,1,"text/MinBias_TuneEE5C_13TeV-herwigpp/GEN/GEN_HIST_phi_etaptH.txt");

TH1F *GEN_HIST_phi_ptH;
gDirectory->GetObject("GEN_HIST_phi_ptH",GEN_HIST_phi_ptH);
PrintHistogram(GEN_HIST_phi_ptH,1,1,"text/MinBias_TuneEE5C_13TeV-herwigpp/GEN/GEN_HIST_phi_ptH.txt");

TProfile *GEN_towardTotalAvg_b1;
gDirectory->GetObject("GEN_towardTotalAvg_b1",GEN_towardTotalAvg_b1);
PrintProfile(GEN_towardTotalAvg_b1,1,1,"text/MinBias_TuneEE5C_13TeV-herwigpp/GEN/towardTotalAvg_b1.txt");

TProfile *GEN_towardTotalAvg_b2;
gDirectory->GetObject("GEN_towardTotalAvg_b2",GEN_towardTotalAvg_b2);
PrintProfile(GEN_towardTotalAvg_b2,1,1,"text/MinBias_TuneEE5C_13TeV-herwigpp/GEN/towardTotalAvg_b2.txt");

TProfile *GEN_transDifNch_b1;
gDirectory->GetObject("GEN_transDifNch_b1",GEN_transDifNch_b1);
PrintProfile(GEN_transDifNch_b1,1,1,"text/MinBias_TuneEE5C_13TeV-herwigpp/GEN/transDifNch_b1.txt");

TH1F *GEN_HIST_nchMB;
gDirectory->GetObject("GEN_HIST_nchMB",GEN_HIST_nchMB);
PrintHistogram(GEN_HIST_nchMB,1,1,"text/MinBias_TuneEE5C_13TeV-herwigpp/GEN/HIST_nchMB.txt");

TProfile *GEN_towardNch_b2;
gDirectory->GetObject("GEN_towardNch_b2",GEN_towardNch_b2);
PrintProfile(GEN_towardNch_b2,1,1,"text/MinBias_TuneEE5C_13TeV-herwigpp/GEN/towardNch_b2.txt");

TH1F *GEN_HIST_ptSumMB;
gDirectory->GetObject("GEN_HIST_ptSumMB",GEN_HIST_ptSumMB);
PrintHistogram(GEN_HIST_ptSumMB,1,1,"text/MinBias_TuneEE5C_13TeV-herwigpp/GEN/HIST_ptSumMB.txt");

TProfile *GEN_trans_b2;
gDirectory->GetObject("GEN_trans_b2",GEN_trans_b2);
PrintProfile(GEN_trans_b2,1,1,"text/MinBias_TuneEE5C_13TeV-herwigpp/GEN/trans_b2.txt");

TProfile *GEN_trans_b1;
gDirectory->GetObject("GEN_trans_b1",GEN_trans_b1);
PrintProfile(GEN_trans_b1,1,1,"text/MinBias_TuneEE5C_13TeV-herwigpp/GEN/trans_b1.txt");

TProfile *GEN_transMax_bh;
gDirectory->GetObject("GEN_transMax_bh",GEN_transMax_bh);
PrintProfile(GEN_transMax_bh,1,1,"text/MinBias_TuneEE5C_13TeV-herwigpp/GEN/transMax_bh.txt");

TProfile *GEN_overallAvg_bh;
gDirectory->GetObject("GEN_overallAvg_bh",GEN_overallAvg_bh);
PrintProfile(GEN_overallAvg_bh,1,1,"text/MinBias_TuneEE5C_13TeV-herwigpp/GEN/overallAvg_bh.txt");

TProfile *GEN_toward_b2;
gDirectory->GetObject("GEN_toward_b2",GEN_toward_b2);
PrintProfile(GEN_toward_b2,1,1,"text/MinBias_TuneEE5C_13TeV-herwigpp/GEN/toward_b2.txt");

TProfile *GEN_toward_b1;
gDirectory->GetObject("GEN_toward_b1",GEN_toward_b1);
PrintProfile(GEN_toward_b1,1,1,"text/MinBias_TuneEE5C_13TeV-herwigpp/GEN/toward_b1.txt");

TProfile *GEN_overallTotal_b2;
gDirectory->GetObject("GEN_overallTotal_b2",GEN_overallTotal_b2);
PrintProfile(GEN_overallTotal_b2,1,1,"text/MinBias_TuneEE5C_13TeV-herwigpp/GEN/overallTotal_b2.txt");

TProfile *GEN_overallTotal_b1;
gDirectory->GetObject("GEN_overallTotal_b1",GEN_overallTotal_b1);
PrintProfile(GEN_overallTotal_b1,1,1,"text/MinBias_TuneEE5C_13TeV-herwigpp/GEN/overallTotal_b1.txt");

TProfile *GEN_trans_bh;
gDirectory->GetObject("GEN_trans_bh",GEN_trans_bh);
PrintProfile(GEN_trans_bh,1,1,"text/MinBias_TuneEE5C_13TeV-herwigpp/GEN/trans_bh.txt");

TProfile *GEN_towardNch_bh;
gDirectory->GetObject("GEN_towardNch_bh",GEN_towardNch_bh);
PrintProfile(GEN_towardNch_bh,1,1,"text/MinBias_TuneEE5C_13TeV-herwigpp/GEN/towardNch_bh.txt");

TProfile *GEN_transMaxNch_b2;
gDirectory->GetObject("GEN_transMaxNch_b2",GEN_transMaxNch_b2);
PrintProfile(GEN_transMaxNch_b2,1,1,"text/MinBias_TuneEE5C_13TeV-herwigpp/GEN/transMaxNch_b2.txt");

TH1F *GEN_HIST_etaMB;
gDirectory->GetObject("GEN_HIST_etaMB",GEN_HIST_etaMB);
PrintHistogram(GEN_HIST_etaMB,1,1,"text/MinBias_TuneEE5C_13TeV-herwigpp/GEN/HIST_etaMB.txt");

TProfile *GEN_towardTotalAvg_bh;
gDirectory->GetObject("GEN_towardTotalAvg_bh",GEN_towardTotalAvg_bh);
PrintProfile(GEN_towardTotalAvg_bh,1,1,"text/MinBias_TuneEE5C_13TeV-herwigpp/GEN/towardTotalAvg_bh.txt");

TProfile *GEN_towardNch_b1;
gDirectory->GetObject("GEN_towardNch_b1",GEN_towardNch_b1);
PrintProfile(GEN_towardNch_b1,1,1,"text/MinBias_TuneEE5C_13TeV-herwigpp/GEN/towardNch_b1.txt");

TProfile *GEN_overallTotalNch_b2;
gDirectory->GetObject("GEN_overallTotalNch_b2",GEN_overallTotalNch_b2);
PrintProfile(GEN_overallTotalNch_b2,1,1,"text/MinBias_TuneEE5C_13TeV-herwigpp/GEN/overallTotalNch_b2.txt");

TProfile *GEN_overallAvg_b2;
gDirectory->GetObject("GEN_overallAvg_b2",GEN_overallAvg_b2);
PrintProfile(GEN_overallAvg_b2,1,1,"text/MinBias_TuneEE5C_13TeV-herwigpp/GEN/overallAvg_b2.txt");

TProfile *GEN_overallAvg_b1;
gDirectory->GetObject("GEN_overallAvg_b1",GEN_overallAvg_b1);
PrintProfile(GEN_overallAvg_b1,1,1,"text/MinBias_TuneEE5C_13TeV-herwigpp/GEN/overallAvg_b1.txt");

TProfile *GEN_toward_bh;
gDirectory->GetObject("GEN_toward_bh",GEN_toward_bh);
PrintProfile(GEN_toward_bh,1,1,"text/MinBias_TuneEE5C_13TeV-herwigpp/GEN/toward_bh.txt");

TProfile *GEN_transDifNch_b2;
gDirectory->GetObject("GEN_transDifNch_b2",GEN_transDifNch_b2);
PrintProfile(GEN_transDifNch_b2,1,1,"text/MinBias_TuneEE5C_13TeV-herwigpp/GEN/transDifNch_b2.txt");

TProfile *GEN_transMax_b2;
gDirectory->GetObject("GEN_transMax_b2",GEN_transMax_b2);
PrintProfile(GEN_transMax_b2,1,1,"text/MinBias_TuneEE5C_13TeV-herwigpp/GEN/transMax_b2.txt");

TProfile *GEN_transMax_b1;
gDirectory->GetObject("GEN_transMax_b1",GEN_transMax_b1);
PrintProfile(GEN_transMax_b1,1,1,"text/MinBias_TuneEE5C_13TeV-herwigpp/GEN/transMax_b1.txt");

TH1F *GEN_HIST_pt_pt5;
gDirectory->GetObject("GEN_HIST_pt_pt5",GEN_HIST_pt_pt5);
PrintHistogram(GEN_HIST_pt_pt5,1,1,"text/MinBias_TuneEE5C_13TeV-herwigpp/GEN/HIST_pt_pt5.txt");

TProfile *GEN_ptMax_bh;
gDirectory->GetObject("GEN_ptMax_bh",GEN_ptMax_bh);
PrintProfile(GEN_ptMax_bh,1,1,"text/MinBias_TuneEE5C_13TeV-herwigpp/GEN/ptMax_bh.txt");

TProfile *GEN_transMinNch_bh;
gDirectory->GetObject("GEN_transMinNch_bh",GEN_transMinNch_bh);
PrintProfile(GEN_transMinNch_bh,1,1,"text/MinBias_TuneEE5C_13TeV-herwigpp/GEN/transMinNch_bh.txt");

TH1F *GEN_HIST_delPhiPt_pt5;
gDirectory->GetObject("GEN_HIST_delPhiPt_pt5",GEN_HIST_delPhiPt_pt5);
PrintHistogram(GEN_HIST_delPhiPt_pt5,1,1,"text/MinBias_TuneEE5C_13TeV-herwigpp/GEN/HIST_delPhiPt_pt5.txt");

TH1F *GEN_HIST_nch_pt5;
gDirectory->GetObject("GEN_HIST_nch_pt5",GEN_HIST_nch_pt5);
PrintHistogram(GEN_HIST_nch_pt5,1,1,"text/MinBias_TuneEE5C_13TeV-herwigpp/GEN/HIST_nch_pt5.txt");

TProfile *GEN_overallTotalNch_b1;
gDirectory->GetObject("GEN_overallTotalNch_b1",GEN_overallTotalNch_b1);
PrintProfile(GEN_overallTotalNch_b1,1,1,"text/MinBias_TuneEE5C_13TeV-herwigpp/GEN/overallTotalNch_b1.txt");

TH1F *GEN_HIST_ptSum;
gDirectory->GetObject("GEN_HIST_ptSum",GEN_HIST_ptSum);
PrintHistogram(GEN_HIST_ptSum,1,1,"text/MinBias_TuneEE5C_13TeV-herwigpp/GEN/HIST_ptSum.txt");

TProfile *GEN_transMaxNch_b1;
gDirectory->GetObject("GEN_transMaxNch_b1",GEN_transMaxNch_b1);
PrintProfile(GEN_transMaxNch_b1,1,1,"text/MinBias_TuneEE5C_13TeV-herwigpp/GEN/transMaxNch_b1.txt");

TProfile *GEN_towardAvg_bh;
gDirectory->GetObject("GEN_towardAvg_bh",GEN_towardAvg_bh);
PrintProfile(GEN_towardAvg_bh,1,1,"text/MinBias_TuneEE5C_13TeV-herwigpp/GEN/towardAvg_bh.txt");

TH1F *GEN_HIST_ptMax;
gDirectory->GetObject("GEN_HIST_ptMax",GEN_HIST_ptMax);
PrintHistogram(GEN_HIST_ptMax,1,1,"text/MinBias_TuneEE5C_13TeV-herwigpp/GEN/HIST_ptMax.txt");

TH1F *GEN_HIST_transPtSum_pt5;
gDirectory->GetObject("GEN_HIST_transPtSum_pt5",GEN_HIST_transPtSum_pt5);
PrintHistogram(GEN_HIST_transPtSum_pt5,1,1,"text/MinBias_TuneEE5C_13TeV-herwigpp/GEN/HIST_transPtSum_pt5.txt");

TProfile *GEN_transMinNch_b1;
gDirectory->GetObject("GEN_transMinNch_b1",GEN_transMinNch_b1);
PrintProfile(GEN_transMinNch_b1,1,1,"text/MinBias_TuneEE5C_13TeV-herwigpp/GEN/transMinNch_b1.txt");

TProfile *GEN_transMinNch_b2;
gDirectory->GetObject("GEN_transMinNch_b2",GEN_transMinNch_b2);
PrintProfile(GEN_transMinNch_b2,1,1,"text/MinBias_TuneEE5C_13TeV-herwigpp/GEN/transMinNch_b2.txt");

TProfile *GEN_ptMax_b2;
gDirectory->GetObject("GEN_ptMax_b2",GEN_ptMax_b2);
PrintProfile(GEN_ptMax_b2,1,1,"text/MinBias_TuneEE5C_13TeV-herwigpp/GEN/ptMax_b2.txt");

TProfile *GEN_ptMax_b1;
gDirectory->GetObject("GEN_ptMax_b1",GEN_ptMax_b1);
PrintProfile(GEN_ptMax_b1,1,1,"text/MinBias_TuneEE5C_13TeV-herwigpp/GEN/ptMax_b1.txt");

TH1F *GEN_HIST_transPt;
gDirectory->GetObject("GEN_HIST_transPt",GEN_HIST_transPt);
PrintHistogram(GEN_HIST_transPt,1,1,"text/MinBias_TuneEE5C_13TeV-herwigpp/GEN/HIST_transPt.txt");

TProfile *GEN_overallTotalNch_bh;
gDirectory->GetObject("GEN_overallTotalNch_bh",GEN_overallTotalNch_bh);
PrintProfile(GEN_overallTotalNch_bh,1,1,"text/MinBias_TuneEE5C_13TeV-herwigpp/GEN/overallTotalNch_bh.txt");

TProfile *GEN_transMaxNch_bh;
gDirectory->GetObject("GEN_transMaxNch_bh",GEN_transMaxNch_bh);
PrintProfile(GEN_transMaxNch_bh,1,1,"text/MinBias_TuneEE5C_13TeV-herwigpp/GEN/transMaxNch_bh.txt");

TProfile *GEN_towardAvg_b1;
gDirectory->GetObject("GEN_towardAvg_b1",GEN_towardAvg_b1);
PrintProfile(GEN_towardAvg_b1,1,1,"text/MinBias_TuneEE5C_13TeV-herwigpp/GEN/towardAvg_b1.txt");

TProfile *GEN_towardAvg_b2;
gDirectory->GetObject("GEN_towardAvg_b2",GEN_towardAvg_b2);
PrintProfile(GEN_towardAvg_b2,1,1,"text/MinBias_TuneEE5C_13TeV-herwigpp/GEN/towardAvg_b2.txt");

TH1F *GEN_HIST_delPhiPt;
gDirectory->GetObject("GEN_HIST_delPhiPt",GEN_HIST_delPhiPt);
PrintHistogram(GEN_HIST_delPhiPt,1,1,"text/MinBias_TuneEE5C_13TeV-herwigpp/GEN/HIST_delPhiPt.txt");

TH1F *GEN_HIST_ptMB;
gDirectory->GetObject("GEN_HIST_ptMB",GEN_HIST_ptMB);
PrintHistogram(GEN_HIST_ptMB,1,1,"text/MinBias_TuneEE5C_13TeV-herwigpp/GEN/HIST_ptMB.txt");

TProfile *GEN_transDif_b2;
gDirectory->GetObject("GEN_transDif_b2",GEN_transDif_b2);
PrintProfile(GEN_transDif_b2,1,1,"text/MinBias_TuneEE5C_13TeV-herwigpp/GEN/transDif_b2.txt");

TProfile *GEN_transDif_b1;
gDirectory->GetObject("GEN_transDif_b1",GEN_transDif_b1);
PrintProfile(GEN_transDif_b1,1,1,"text/MinBias_TuneEE5C_13TeV-herwigpp/GEN/transDif_b1.txt");

TProfile *GEN_transMin_b1;
gDirectory->GetObject("GEN_transMin_b1",GEN_transMin_b1);
PrintProfile(GEN_transMin_b1,1,1,"text/MinBias_TuneEE5C_13TeV-herwigpp/GEN/transMin_b1.txt");

TProfile *GEN_transMin_b2;
gDirectory->GetObject("GEN_transMin_b2",GEN_transMin_b2);
PrintProfile(GEN_transMin_b2,1,1,"text/MinBias_TuneEE5C_13TeV-herwigpp/GEN/transMin_b2.txt");

TH1F *GEN_HIST_delPhi;
gDirectory->GetObject("GEN_HIST_delPhi",GEN_HIST_delPhi);
PrintHistogram(GEN_HIST_delPhi,1,1,"text/MinBias_TuneEE5C_13TeV-herwigpp/GEN/HIST_delPhi.txt");

TProfile *GEN_transNch_bh;
gDirectory->GetObject("GEN_transNch_bh",GEN_transNch_bh);
PrintProfile(GEN_transNch_bh,1,1,"text/MinBias_TuneEE5C_13TeV-herwigpp/GEN/transNch_bh.txt");

TProfile *GEN_overall_bh;
gDirectory->GetObject("GEN_overall_bh",GEN_overall_bh);
PrintProfile(GEN_overall_bh,1,1,"text/MinBias_TuneEE5C_13TeV-herwigpp/GEN/overall_bh.txt");

TProfile *GEN_towardTotalNch_b1;
gDirectory->GetObject("GEN_towardTotalNch_b1",GEN_towardTotalNch_b1);
PrintProfile(GEN_towardTotalNch_b1,1,1,"text/MinBias_TuneEE5C_13TeV-herwigpp/GEN/towardTotalNch_b1.txt");

TProfile *GEN_towardTotalNch_b2;
gDirectory->GetObject("GEN_towardTotalNch_b2",GEN_towardTotalNch_b2);
PrintProfile(GEN_towardTotalNch_b2,1,1,"text/MinBias_TuneEE5C_13TeV-herwigpp/GEN/towardTotalNch_b2.txt");

TProfile *GEN_overallNch_bh;
gDirectory->GetObject("GEN_overallNch_bh",GEN_overallNch_bh);
PrintProfile(GEN_overallNch_bh,1,1,"text/MinBias_TuneEE5C_13TeV-herwigpp/GEN/overallNch_bh.txt");

TProfile *GEN_transMin_bh;
gDirectory->GetObject("GEN_transMin_bh",GEN_transMin_bh);
PrintProfile(GEN_transMin_bh,1,1,"text/MinBias_TuneEE5C_13TeV-herwigpp/GEN/transMin_bh.txt");

TH1F *GEN_HIST_transPtSum;
gDirectory->GetObject("GEN_HIST_transPtSum",GEN_HIST_transPtSum);
PrintHistogram(GEN_HIST_transPtSum,1,1,"text/MinBias_TuneEE5C_13TeV-herwigpp/GEN/HIST_transPtSum.txt");

TH1F *GEN_HIST_eta_pt5;
gDirectory->GetObject("GEN_HIST_eta_pt5",GEN_HIST_eta_pt5);
PrintHistogram(GEN_HIST_eta_pt5,1,1,"text/MinBias_TuneEE5C_13TeV-herwigpp/GEN/HIST_eta_pt5.txt");

TH1F *GEN_HIST_delPhi_pt5;
gDirectory->GetObject("GEN_HIST_delPhi_pt5",GEN_HIST_delPhi_pt5);
PrintHistogram(GEN_HIST_delPhi_pt5,1,1,"text/MinBias_TuneEE5C_13TeV-herwigpp/GEN/HIST_delPhi_pt5.txt");

TProfile *GEN_transDif_bh;
gDirectory->GetObject("GEN_transDif_bh",GEN_transDif_bh);
PrintProfile(GEN_transDif_bh,1,1,"text/MinBias_TuneEE5C_13TeV-herwigpp/GEN/transDif_bh.txt");

TProfile *GEN_overallNch_b2;
gDirectory->GetObject("GEN_overallNch_b2",GEN_overallNch_b2);
PrintProfile(GEN_overallNch_b2,1,1,"text/MinBias_TuneEE5C_13TeV-herwigpp/GEN/overallNch_b2.txt");

TProfile *GEN_overallNch_b1;
gDirectory->GetObject("GEN_overallNch_b1",GEN_overallNch_b1);
PrintProfile(GEN_overallNch_b1,1,1,"text/MinBias_TuneEE5C_13TeV-herwigpp/GEN/overallNch_b1.txt");

TProfile *GEN_towardTotalNch_bh;
gDirectory->GetObject("GEN_towardTotalNch_bh",GEN_towardTotalNch_bh);
PrintProfile(GEN_towardTotalNch_bh,1,1,"text/MinBias_TuneEE5C_13TeV-herwigpp/GEN/towardTotalNch_bh.txt");

TProfile *GEN_transAvg_b2;
gDirectory->GetObject("GEN_transAvg_b2",GEN_transAvg_b2);
PrintProfile(GEN_transAvg_b2,1,1,"text/MinBias_TuneEE5C_13TeV-herwigpp/GEN/transAvg_b2.txt");

TProfile *GEN_overall_b2;
gDirectory->GetObject("GEN_overall_b2",GEN_overall_b2);
PrintProfile(GEN_overall_b2,1,1,"text/MinBias_TuneEE5C_13TeV-herwigpp/GEN/overall_b2.txt");

TProfile *GEN_overall_b1;
gDirectory->GetObject("GEN_overall_b1",GEN_overall_b1);
PrintProfile(GEN_overall_b1,1,1,"text/MinBias_TuneEE5C_13TeV-herwigpp/GEN/overall_b1.txt");

TProfile *GEN_transNch_b1;
gDirectory->GetObject("GEN_transNch_b1",GEN_transNch_b1);
PrintProfile(GEN_transNch_b1,1,1,"text/MinBias_TuneEE5C_13TeV-herwigpp/GEN/transNch_b1.txt");

TProfile *GEN_transNch_b2;
gDirectory->GetObject("GEN_transNch_b2",GEN_transNch_b2);
PrintProfile(GEN_transNch_b2,1,1,"text/MinBias_TuneEE5C_13TeV-herwigpp/GEN/transNch_b2.txt");

TProfile *GEN_transAvg_b1;
gDirectory->GetObject("GEN_transAvg_b1",GEN_transAvg_b1);
PrintProfile(GEN_transAvg_b1,1,1,"text/MinBias_TuneEE5C_13TeV-herwigpp/GEN/transAvg_b1.txt");

TH1F *GEN_HIST_ptSum_pt5;
gDirectory->GetObject("GEN_HIST_ptSum_pt5",GEN_HIST_ptSum_pt5);
PrintHistogram(GEN_HIST_ptSum_pt5,1,1,"text/MinBias_TuneEE5C_13TeV-herwigpp/GEN/HIST_ptSum_pt5.txt");

TH1F *GEN_HIST_transNch_pt5;
gDirectory->GetObject("GEN_HIST_transNch_pt5",GEN_HIST_transNch_pt5);
PrintHistogram(GEN_HIST_transNch_pt5,1,1,"text/MinBias_TuneEE5C_13TeV-herwigpp/GEN/HIST_transNch_pt5.txt");

TProfile *GEN_towardTotal_bh;
gDirectory->GetObject("GEN_towardTotal_bh",GEN_towardTotal_bh);
PrintProfile(GEN_towardTotal_bh,1,1,"text/MinBias_TuneEE5C_13TeV-herwigpp/GEN/towardTotal_bh.txt");

TH1F *GEN_HIST_nch;
gDirectory->GetObject("GEN_HIST_nch",GEN_HIST_nch);
PrintHistogram(GEN_HIST_nch,1,1,"text/MinBias_TuneEE5C_13TeV-herwigpp/GEN/HIST_nch.txt");

TProfile *GEN_awayNch_b1;
gDirectory->GetObject("GEN_awayNch_b1",GEN_awayNch_b1);
PrintProfile(GEN_awayNch_b1,1,1,"text/MinBias_TuneEE5C_13TeV-herwigpp/GEN/awayNch_b1.txt");

TProfile *GEN_awayNch_b2;
gDirectory->GetObject("GEN_awayNch_b2",GEN_awayNch_b2);
PrintProfile(GEN_awayNch_b2,1,1,"text/MinBias_TuneEE5C_13TeV-herwigpp/GEN/awayNch_b2.txt");

TH1F *GEN_HIST_transPt_pt5;
gDirectory->GetObject("GEN_HIST_transPt_pt5",GEN_HIST_transPt_pt5);
PrintHistogram(GEN_HIST_transPt_pt5,1,1,"text/MinBias_TuneEE5C_13TeV-herwigpp/GEN/HIST_transPt_pt5.txt");

TProfile *GEN_overallTotalAvg_b1;
gDirectory->GetObject("GEN_overallTotalAvg_b1",GEN_overallTotalAvg_b1);
PrintProfile(GEN_overallTotalAvg_b1,1,1,"text/MinBias_TuneEE5C_13TeV-herwigpp/GEN/overallTotalAvg_b1.txt");

TProfile *GEN_overallTotalAvg_b2;
gDirectory->GetObject("GEN_overallTotalAvg_b2",GEN_overallTotalAvg_b2);
PrintProfile(GEN_overallTotalAvg_b2,1,1,"text/MinBias_TuneEE5C_13TeV-herwigpp/GEN/overallTotalAvg_b2.txt");

TProfile *GEN_transDifNch_bh;
gDirectory->GetObject("GEN_transDifNch_bh",GEN_transDifNch_bh);
PrintProfile(GEN_transDifNch_bh,1,1,"text/MinBias_TuneEE5C_13TeV-herwigpp/GEN/transDifNch_bh.txt");

TProfile *GEN_away_bh;
gDirectory->GetObject("GEN_away_bh",GEN_away_bh);
PrintProfile(GEN_away_bh,1,1,"text/MinBias_TuneEE5C_13TeV-herwigpp/GEN/away_bh.txt");

TProfile *GEN_awayAvg_bh;
gDirectory->GetObject("GEN_awayAvg_bh",GEN_awayAvg_bh);
PrintProfile(GEN_awayAvg_bh,1,1,"text/MinBias_TuneEE5C_13TeV-herwigpp/GEN/awayAvg_bh.txt");

TProfile *GEN_transAvg_bh;
gDirectory->GetObject("GEN_transAvg_bh",GEN_transAvg_bh);
PrintProfile(GEN_transAvg_bh,1,1,"text/MinBias_TuneEE5C_13TeV-herwigpp/GEN/transAvg_bh.txt");

TProfile *GEN_awayAvg_b1;
gDirectory->GetObject("GEN_awayAvg_b1",GEN_awayAvg_b1);
PrintProfile(GEN_awayAvg_b1,1,1,"text/MinBias_TuneEE5C_13TeV-herwigpp/GEN/awayAvg_b1.txt");

TProfile *GEN_away_b1;
gDirectory->GetObject("GEN_away_b1",GEN_away_b1);
PrintProfile(GEN_away_b1,1,1,"text/MinBias_TuneEE5C_13TeV-herwigpp/GEN/away_b1.txt");

TProfile *GEN_away_b2;
gDirectory->GetObject("GEN_away_b2",GEN_away_b2);
PrintProfile(GEN_away_b2,1,1,"text/MinBias_TuneEE5C_13TeV-herwigpp/GEN/away_b2.txt");

TProfile *GEN_awayAvg_b2;
gDirectory->GetObject("GEN_awayAvg_b2",GEN_awayAvg_b2);
PrintProfile(GEN_awayAvg_b2,1,1,"text/MinBias_TuneEE5C_13TeV-herwigpp/GEN/awayAvg_b2.txt");

TH1F *GEN_HIST_transNch;
gDirectory->GetObject("GEN_HIST_transNch",GEN_HIST_transNch);
PrintHistogram(GEN_HIST_transNch,1,1,"text/MinBias_TuneEE5C_13TeV-herwigpp/GEN/HIST_transNch.txt");

TProfile *GEN_overallTotalAvg_bh;
gDirectory->GetObject("GEN_overallTotalAvg_bh",GEN_overallTotalAvg_bh);
PrintProfile(GEN_overallTotalAvg_bh,1,1,"text/MinBias_TuneEE5C_13TeV-herwigpp/GEN/overallTotalAvg_bh.txt");

TProfile *GEN_overallTotal_bh;
gDirectory->GetObject("GEN_overallTotal_bh",GEN_overallTotal_bh);
PrintProfile(GEN_overallTotal_bh,1,1,"text/MinBias_TuneEE5C_13TeV-herwigpp/GEN/overallTotal_bh.txt");

TProfile *GEN_awayNch_bh;
gDirectory->GetObject("GEN_awayNch_bh",GEN_awayNch_bh);
PrintProfile(GEN_awayNch_bh,1,1,"text/MinBias_TuneEE5C_13TeV-herwigpp/GEN/awayNch_bh.txt");

TProfile *GEN_towardTotal_b1;
gDirectory->GetObject("GEN_towardTotal_b1",GEN_towardTotal_b1);
PrintProfile(GEN_towardTotal_b1,1,1,"text/MinBias_TuneEE5C_13TeV-herwigpp/GEN/towardTotal_b1.txt");

TProfile *GEN_towardTotal_b2;
gDirectory->GetObject("GEN_towardTotal_b2",GEN_towardTotal_b2);
PrintProfile(GEN_towardTotal_b2,1,1,"text/MinBias_TuneEE5C_13TeV-herwigpp/GEN/towardTotal_b2.txt");

// (" (" (" (" (" (" (" (" ", ", ", ", ", ", ", 



	fhist->cd("ReggeGribovPartonMC_13TeV-EPOS");


TH1F *GEN_HIST_eta_ptH;
gDirectory->GetObject("GEN_HIST_eta_ptH",GEN_HIST_eta_ptH);
PrintHistogram(GEN_HIST_eta_ptH,1,1,"text/ReggeGribovPartonMC_13TeV-EPOS/GEN/GEN_HIST_eta_ptH.txt");

TH1F *GEN_HIST_phi_all;
gDirectory->GetObject("GEN_HIST_phi_all",GEN_HIST_phi_all);
PrintHistogram(GEN_HIST_phi_all,1,1,"text/ReggeGribovPartonMC_13TeV-EPOS/GEN/GEN_HIST_phi_all.txt");

TH1F *GEN_HIST_phi_eta;
gDirectory->GetObject("GEN_HIST_phi_eta",GEN_HIST_phi_eta);
PrintHistogram(GEN_HIST_phi_eta,1,1,"text/ReggeGribovPartonMC_13TeV-EPOS/GEN/GEN_HIST_phi_eta.txt");

TH1F *GEN_HIST_phi_etaptH;
gDirectory->GetObject("GEN_HIST_phi_etaptH",GEN_HIST_phi_etaptH);
PrintHistogram(GEN_HIST_phi_etaptH,1,1,"text/ReggeGribovPartonMC_13TeV-EPOS/GEN/GEN_HIST_phi_etaptH.txt");

TH1F *GEN_HIST_phi_ptH;
gDirectory->GetObject("GEN_HIST_phi_ptH",GEN_HIST_phi_ptH);
PrintHistogram(GEN_HIST_phi_ptH,1,1,"text/ReggeGribovPartonMC_13TeV-EPOS/GEN/GEN_HIST_phi_ptH.txt");

TProfile *GEN_towardTotalAvg_b1;
gDirectory->GetObject("GEN_towardTotalAvg_b1",GEN_towardTotalAvg_b1);
PrintProfile(GEN_towardTotalAvg_b1,1,1,"text/ReggeGribovPartonMC_13TeV-EPOS/GEN/towardTotalAvg_b1.txt");

TProfile *GEN_towardTotalAvg_b2;
gDirectory->GetObject("GEN_towardTotalAvg_b2",GEN_towardTotalAvg_b2);
PrintProfile(GEN_towardTotalAvg_b2,1,1,"text/ReggeGribovPartonMC_13TeV-EPOS/GEN/towardTotalAvg_b2.txt");

TProfile *GEN_transDifNch_b1;
gDirectory->GetObject("GEN_transDifNch_b1",GEN_transDifNch_b1);
PrintProfile(GEN_transDifNch_b1,1,1,"text/ReggeGribovPartonMC_13TeV-EPOS/GEN/transDifNch_b1.txt");

TH1F *GEN_HIST_nchMB;
gDirectory->GetObject("GEN_HIST_nchMB",GEN_HIST_nchMB);
PrintHistogram(GEN_HIST_nchMB,1,1,"text/ReggeGribovPartonMC_13TeV-EPOS/GEN/HIST_nchMB.txt");

TProfile *GEN_towardNch_b2;
gDirectory->GetObject("GEN_towardNch_b2",GEN_towardNch_b2);
PrintProfile(GEN_towardNch_b2,1,1,"text/ReggeGribovPartonMC_13TeV-EPOS/GEN/towardNch_b2.txt");

TH1F *GEN_HIST_ptSumMB;
gDirectory->GetObject("GEN_HIST_ptSumMB",GEN_HIST_ptSumMB);
PrintHistogram(GEN_HIST_ptSumMB,1,1,"text/ReggeGribovPartonMC_13TeV-EPOS/GEN/HIST_ptSumMB.txt");

TProfile *GEN_trans_b2;
gDirectory->GetObject("GEN_trans_b2",GEN_trans_b2);
PrintProfile(GEN_trans_b2,1,1,"text/ReggeGribovPartonMC_13TeV-EPOS/GEN/trans_b2.txt");

TProfile *GEN_trans_b1;
gDirectory->GetObject("GEN_trans_b1",GEN_trans_b1);
PrintProfile(GEN_trans_b1,1,1,"text/ReggeGribovPartonMC_13TeV-EPOS/GEN/trans_b1.txt");

TProfile *GEN_transMax_bh;
gDirectory->GetObject("GEN_transMax_bh",GEN_transMax_bh);
PrintProfile(GEN_transMax_bh,1,1,"text/ReggeGribovPartonMC_13TeV-EPOS/GEN/transMax_bh.txt");

TProfile *GEN_overallAvg_bh;
gDirectory->GetObject("GEN_overallAvg_bh",GEN_overallAvg_bh);
PrintProfile(GEN_overallAvg_bh,1,1,"text/ReggeGribovPartonMC_13TeV-EPOS/GEN/overallAvg_bh.txt");

TProfile *GEN_toward_b2;
gDirectory->GetObject("GEN_toward_b2",GEN_toward_b2);
PrintProfile(GEN_toward_b2,1,1,"text/ReggeGribovPartonMC_13TeV-EPOS/GEN/toward_b2.txt");

TProfile *GEN_toward_b1;
gDirectory->GetObject("GEN_toward_b1",GEN_toward_b1);
PrintProfile(GEN_toward_b1,1,1,"text/ReggeGribovPartonMC_13TeV-EPOS/GEN/toward_b1.txt");

TProfile *GEN_overallTotal_b2;
gDirectory->GetObject("GEN_overallTotal_b2",GEN_overallTotal_b2);
PrintProfile(GEN_overallTotal_b2,1,1,"text/ReggeGribovPartonMC_13TeV-EPOS/GEN/overallTotal_b2.txt");

TProfile *GEN_overallTotal_b1;
gDirectory->GetObject("GEN_overallTotal_b1",GEN_overallTotal_b1);
PrintProfile(GEN_overallTotal_b1,1,1,"text/ReggeGribovPartonMC_13TeV-EPOS/GEN/overallTotal_b1.txt");

TProfile *GEN_trans_bh;
gDirectory->GetObject("GEN_trans_bh",GEN_trans_bh);
PrintProfile(GEN_trans_bh,1,1,"text/ReggeGribovPartonMC_13TeV-EPOS/GEN/trans_bh.txt");

TProfile *GEN_towardNch_bh;
gDirectory->GetObject("GEN_towardNch_bh",GEN_towardNch_bh);
PrintProfile(GEN_towardNch_bh,1,1,"text/ReggeGribovPartonMC_13TeV-EPOS/GEN/towardNch_bh.txt");

TProfile *GEN_transMaxNch_b2;
gDirectory->GetObject("GEN_transMaxNch_b2",GEN_transMaxNch_b2);
PrintProfile(GEN_transMaxNch_b2,1,1,"text/ReggeGribovPartonMC_13TeV-EPOS/GEN/transMaxNch_b2.txt");

TH1F *GEN_HIST_etaMB;
gDirectory->GetObject("GEN_HIST_etaMB",GEN_HIST_etaMB);
PrintHistogram(GEN_HIST_etaMB,1,1,"text/ReggeGribovPartonMC_13TeV-EPOS/GEN/HIST_etaMB.txt");

TProfile *GEN_towardTotalAvg_bh;
gDirectory->GetObject("GEN_towardTotalAvg_bh",GEN_towardTotalAvg_bh);
PrintProfile(GEN_towardTotalAvg_bh,1,1,"text/ReggeGribovPartonMC_13TeV-EPOS/GEN/towardTotalAvg_bh.txt");

TProfile *GEN_towardNch_b1;
gDirectory->GetObject("GEN_towardNch_b1",GEN_towardNch_b1);
PrintProfile(GEN_towardNch_b1,1,1,"text/ReggeGribovPartonMC_13TeV-EPOS/GEN/towardNch_b1.txt");

TProfile *GEN_overallTotalNch_b2;
gDirectory->GetObject("GEN_overallTotalNch_b2",GEN_overallTotalNch_b2);
PrintProfile(GEN_overallTotalNch_b2,1,1,"text/ReggeGribovPartonMC_13TeV-EPOS/GEN/overallTotalNch_b2.txt");

TProfile *GEN_overallAvg_b2;
gDirectory->GetObject("GEN_overallAvg_b2",GEN_overallAvg_b2);
PrintProfile(GEN_overallAvg_b2,1,1,"text/ReggeGribovPartonMC_13TeV-EPOS/GEN/overallAvg_b2.txt");

TProfile *GEN_overallAvg_b1;
gDirectory->GetObject("GEN_overallAvg_b1",GEN_overallAvg_b1);
PrintProfile(GEN_overallAvg_b1,1,1,"text/ReggeGribovPartonMC_13TeV-EPOS/GEN/overallAvg_b1.txt");

TProfile *GEN_toward_bh;
gDirectory->GetObject("GEN_toward_bh",GEN_toward_bh);
PrintProfile(GEN_toward_bh,1,1,"text/ReggeGribovPartonMC_13TeV-EPOS/GEN/toward_bh.txt");

TProfile *GEN_transDifNch_b2;
gDirectory->GetObject("GEN_transDifNch_b2",GEN_transDifNch_b2);
PrintProfile(GEN_transDifNch_b2,1,1,"text/ReggeGribovPartonMC_13TeV-EPOS/GEN/transDifNch_b2.txt");

TProfile *GEN_transMax_b2;
gDirectory->GetObject("GEN_transMax_b2",GEN_transMax_b2);
PrintProfile(GEN_transMax_b2,1,1,"text/ReggeGribovPartonMC_13TeV-EPOS/GEN/transMax_b2.txt");

TProfile *GEN_transMax_b1;
gDirectory->GetObject("GEN_transMax_b1",GEN_transMax_b1);
PrintProfile(GEN_transMax_b1,1,1,"text/ReggeGribovPartonMC_13TeV-EPOS/GEN/transMax_b1.txt");

TH1F *GEN_HIST_pt_pt5;
gDirectory->GetObject("GEN_HIST_pt_pt5",GEN_HIST_pt_pt5);
PrintHistogram(GEN_HIST_pt_pt5,1,1,"text/ReggeGribovPartonMC_13TeV-EPOS/GEN/HIST_pt_pt5.txt");

TProfile *GEN_ptMax_bh;
gDirectory->GetObject("GEN_ptMax_bh",GEN_ptMax_bh);
PrintProfile(GEN_ptMax_bh,1,1,"text/ReggeGribovPartonMC_13TeV-EPOS/GEN/ptMax_bh.txt");

TProfile *GEN_transMinNch_bh;
gDirectory->GetObject("GEN_transMinNch_bh",GEN_transMinNch_bh);
PrintProfile(GEN_transMinNch_bh,1,1,"text/ReggeGribovPartonMC_13TeV-EPOS/GEN/transMinNch_bh.txt");

TH1F *GEN_HIST_delPhiPt_pt5;
gDirectory->GetObject("GEN_HIST_delPhiPt_pt5",GEN_HIST_delPhiPt_pt5);
PrintHistogram(GEN_HIST_delPhiPt_pt5,1,1,"text/ReggeGribovPartonMC_13TeV-EPOS/GEN/HIST_delPhiPt_pt5.txt");

TH1F *GEN_HIST_nch_pt5;
gDirectory->GetObject("GEN_HIST_nch_pt5",GEN_HIST_nch_pt5);
PrintHistogram(GEN_HIST_nch_pt5,1,1,"text/ReggeGribovPartonMC_13TeV-EPOS/GEN/HIST_nch_pt5.txt");

TProfile *GEN_overallTotalNch_b1;
gDirectory->GetObject("GEN_overallTotalNch_b1",GEN_overallTotalNch_b1);
PrintProfile(GEN_overallTotalNch_b1,1,1,"text/ReggeGribovPartonMC_13TeV-EPOS/GEN/overallTotalNch_b1.txt");

TH1F *GEN_HIST_ptSum;
gDirectory->GetObject("GEN_HIST_ptSum",GEN_HIST_ptSum);
PrintHistogram(GEN_HIST_ptSum,1,1,"text/ReggeGribovPartonMC_13TeV-EPOS/GEN/HIST_ptSum.txt");

TProfile *GEN_transMaxNch_b1;
gDirectory->GetObject("GEN_transMaxNch_b1",GEN_transMaxNch_b1);
PrintProfile(GEN_transMaxNch_b1,1,1,"text/ReggeGribovPartonMC_13TeV-EPOS/GEN/transMaxNch_b1.txt");

TProfile *GEN_towardAvg_bh;
gDirectory->GetObject("GEN_towardAvg_bh",GEN_towardAvg_bh);
PrintProfile(GEN_towardAvg_bh,1,1,"text/ReggeGribovPartonMC_13TeV-EPOS/GEN/towardAvg_bh.txt");

TH1F *GEN_HIST_ptMax;
gDirectory->GetObject("GEN_HIST_ptMax",GEN_HIST_ptMax);
PrintHistogram(GEN_HIST_ptMax,1,1,"text/ReggeGribovPartonMC_13TeV-EPOS/GEN/HIST_ptMax.txt");

TH1F *GEN_HIST_transPtSum_pt5;
gDirectory->GetObject("GEN_HIST_transPtSum_pt5",GEN_HIST_transPtSum_pt5);
PrintHistogram(GEN_HIST_transPtSum_pt5,1,1,"text/ReggeGribovPartonMC_13TeV-EPOS/GEN/HIST_transPtSum_pt5.txt");

TProfile *GEN_transMinNch_b1;
gDirectory->GetObject("GEN_transMinNch_b1",GEN_transMinNch_b1);
PrintProfile(GEN_transMinNch_b1,1,1,"text/ReggeGribovPartonMC_13TeV-EPOS/GEN/transMinNch_b1.txt");

TProfile *GEN_transMinNch_b2;
gDirectory->GetObject("GEN_transMinNch_b2",GEN_transMinNch_b2);
PrintProfile(GEN_transMinNch_b2,1,1,"text/ReggeGribovPartonMC_13TeV-EPOS/GEN/transMinNch_b2.txt");

TProfile *GEN_ptMax_b2;
gDirectory->GetObject("GEN_ptMax_b2",GEN_ptMax_b2);
PrintProfile(GEN_ptMax_b2,1,1,"text/ReggeGribovPartonMC_13TeV-EPOS/GEN/ptMax_b2.txt");

TProfile *GEN_ptMax_b1;
gDirectory->GetObject("GEN_ptMax_b1",GEN_ptMax_b1);
PrintProfile(GEN_ptMax_b1,1,1,"text/ReggeGribovPartonMC_13TeV-EPOS/GEN/ptMax_b1.txt");

TH1F *GEN_HIST_transPt;
gDirectory->GetObject("GEN_HIST_transPt",GEN_HIST_transPt);
PrintHistogram(GEN_HIST_transPt,1,1,"text/ReggeGribovPartonMC_13TeV-EPOS/GEN/HIST_transPt.txt");

TProfile *GEN_overallTotalNch_bh;
gDirectory->GetObject("GEN_overallTotalNch_bh",GEN_overallTotalNch_bh);
PrintProfile(GEN_overallTotalNch_bh,1,1,"text/ReggeGribovPartonMC_13TeV-EPOS/GEN/overallTotalNch_bh.txt");

TProfile *GEN_transMaxNch_bh;
gDirectory->GetObject("GEN_transMaxNch_bh",GEN_transMaxNch_bh);
PrintProfile(GEN_transMaxNch_bh,1,1,"text/ReggeGribovPartonMC_13TeV-EPOS/GEN/transMaxNch_bh.txt");

TProfile *GEN_towardAvg_b1;
gDirectory->GetObject("GEN_towardAvg_b1",GEN_towardAvg_b1);
PrintProfile(GEN_towardAvg_b1,1,1,"text/ReggeGribovPartonMC_13TeV-EPOS/GEN/towardAvg_b1.txt");

TProfile *GEN_towardAvg_b2;
gDirectory->GetObject("GEN_towardAvg_b2",GEN_towardAvg_b2);
PrintProfile(GEN_towardAvg_b2,1,1,"text/ReggeGribovPartonMC_13TeV-EPOS/GEN/towardAvg_b2.txt");

TH1F *GEN_HIST_delPhiPt;
gDirectory->GetObject("GEN_HIST_delPhiPt",GEN_HIST_delPhiPt);
PrintHistogram(GEN_HIST_delPhiPt,1,1,"text/ReggeGribovPartonMC_13TeV-EPOS/GEN/HIST_delPhiPt.txt");

TH1F *GEN_HIST_ptMB;
gDirectory->GetObject("GEN_HIST_ptMB",GEN_HIST_ptMB);
PrintHistogram(GEN_HIST_ptMB,1,1,"text/ReggeGribovPartonMC_13TeV-EPOS/GEN/HIST_ptMB.txt");

TProfile *GEN_transDif_b2;
gDirectory->GetObject("GEN_transDif_b2",GEN_transDif_b2);
PrintProfile(GEN_transDif_b2,1,1,"text/ReggeGribovPartonMC_13TeV-EPOS/GEN/transDif_b2.txt");

TProfile *GEN_transDif_b1;
gDirectory->GetObject("GEN_transDif_b1",GEN_transDif_b1);
PrintProfile(GEN_transDif_b1,1,1,"text/ReggeGribovPartonMC_13TeV-EPOS/GEN/transDif_b1.txt");

TProfile *GEN_transMin_b1;
gDirectory->GetObject("GEN_transMin_b1",GEN_transMin_b1);
PrintProfile(GEN_transMin_b1,1,1,"text/ReggeGribovPartonMC_13TeV-EPOS/GEN/transMin_b1.txt");

TProfile *GEN_transMin_b2;
gDirectory->GetObject("GEN_transMin_b2",GEN_transMin_b2);
PrintProfile(GEN_transMin_b2,1,1,"text/ReggeGribovPartonMC_13TeV-EPOS/GEN/transMin_b2.txt");

TH1F *GEN_HIST_delPhi;
gDirectory->GetObject("GEN_HIST_delPhi",GEN_HIST_delPhi);
PrintHistogram(GEN_HIST_delPhi,1,1,"text/ReggeGribovPartonMC_13TeV-EPOS/GEN/HIST_delPhi.txt");

TProfile *GEN_transNch_bh;
gDirectory->GetObject("GEN_transNch_bh",GEN_transNch_bh);
PrintProfile(GEN_transNch_bh,1,1,"text/ReggeGribovPartonMC_13TeV-EPOS/GEN/transNch_bh.txt");

TProfile *GEN_overall_bh;
gDirectory->GetObject("GEN_overall_bh",GEN_overall_bh);
PrintProfile(GEN_overall_bh,1,1,"text/ReggeGribovPartonMC_13TeV-EPOS/GEN/overall_bh.txt");

TProfile *GEN_towardTotalNch_b1;
gDirectory->GetObject("GEN_towardTotalNch_b1",GEN_towardTotalNch_b1);
PrintProfile(GEN_towardTotalNch_b1,1,1,"text/ReggeGribovPartonMC_13TeV-EPOS/GEN/towardTotalNch_b1.txt");

TProfile *GEN_towardTotalNch_b2;
gDirectory->GetObject("GEN_towardTotalNch_b2",GEN_towardTotalNch_b2);
PrintProfile(GEN_towardTotalNch_b2,1,1,"text/ReggeGribovPartonMC_13TeV-EPOS/GEN/towardTotalNch_b2.txt");

TProfile *GEN_overallNch_bh;
gDirectory->GetObject("GEN_overallNch_bh",GEN_overallNch_bh);
PrintProfile(GEN_overallNch_bh,1,1,"text/ReggeGribovPartonMC_13TeV-EPOS/GEN/overallNch_bh.txt");

TProfile *GEN_transMin_bh;
gDirectory->GetObject("GEN_transMin_bh",GEN_transMin_bh);
PrintProfile(GEN_transMin_bh,1,1,"text/ReggeGribovPartonMC_13TeV-EPOS/GEN/transMin_bh.txt");

TH1F *GEN_HIST_transPtSum;
gDirectory->GetObject("GEN_HIST_transPtSum",GEN_HIST_transPtSum);
PrintHistogram(GEN_HIST_transPtSum,1,1,"text/ReggeGribovPartonMC_13TeV-EPOS/GEN/HIST_transPtSum.txt");

TH1F *GEN_HIST_eta_pt5;
gDirectory->GetObject("GEN_HIST_eta_pt5",GEN_HIST_eta_pt5);
PrintHistogram(GEN_HIST_eta_pt5,1,1,"text/ReggeGribovPartonMC_13TeV-EPOS/GEN/HIST_eta_pt5.txt");

TH1F *GEN_HIST_delPhi_pt5;
gDirectory->GetObject("GEN_HIST_delPhi_pt5",GEN_HIST_delPhi_pt5);
PrintHistogram(GEN_HIST_delPhi_pt5,1,1,"text/ReggeGribovPartonMC_13TeV-EPOS/GEN/HIST_delPhi_pt5.txt");

TProfile *GEN_transDif_bh;
gDirectory->GetObject("GEN_transDif_bh",GEN_transDif_bh);
PrintProfile(GEN_transDif_bh,1,1,"text/ReggeGribovPartonMC_13TeV-EPOS/GEN/transDif_bh.txt");

TProfile *GEN_overallNch_b2;
gDirectory->GetObject("GEN_overallNch_b2",GEN_overallNch_b2);
PrintProfile(GEN_overallNch_b2,1,1,"text/ReggeGribovPartonMC_13TeV-EPOS/GEN/overallNch_b2.txt");

TProfile *GEN_overallNch_b1;
gDirectory->GetObject("GEN_overallNch_b1",GEN_overallNch_b1);
PrintProfile(GEN_overallNch_b1,1,1,"text/ReggeGribovPartonMC_13TeV-EPOS/GEN/overallNch_b1.txt");

TProfile *GEN_towardTotalNch_bh;
gDirectory->GetObject("GEN_towardTotalNch_bh",GEN_towardTotalNch_bh);
PrintProfile(GEN_towardTotalNch_bh,1,1,"text/ReggeGribovPartonMC_13TeV-EPOS/GEN/towardTotalNch_bh.txt");

TProfile *GEN_transAvg_b2;
gDirectory->GetObject("GEN_transAvg_b2",GEN_transAvg_b2);
PrintProfile(GEN_transAvg_b2,1,1,"text/ReggeGribovPartonMC_13TeV-EPOS/GEN/transAvg_b2.txt");

TProfile *GEN_overall_b2;
gDirectory->GetObject("GEN_overall_b2",GEN_overall_b2);
PrintProfile(GEN_overall_b2,1,1,"text/ReggeGribovPartonMC_13TeV-EPOS/GEN/overall_b2.txt");

TProfile *GEN_overall_b1;
gDirectory->GetObject("GEN_overall_b1",GEN_overall_b1);
PrintProfile(GEN_overall_b1,1,1,"text/ReggeGribovPartonMC_13TeV-EPOS/GEN/overall_b1.txt");

TProfile *GEN_transNch_b1;
gDirectory->GetObject("GEN_transNch_b1",GEN_transNch_b1);
PrintProfile(GEN_transNch_b1,1,1,"text/ReggeGribovPartonMC_13TeV-EPOS/GEN/transNch_b1.txt");

TProfile *GEN_transNch_b2;
gDirectory->GetObject("GEN_transNch_b2",GEN_transNch_b2);
PrintProfile(GEN_transNch_b2,1,1,"text/ReggeGribovPartonMC_13TeV-EPOS/GEN/transNch_b2.txt");

TProfile *GEN_transAvg_b1;
gDirectory->GetObject("GEN_transAvg_b1",GEN_transAvg_b1);
PrintProfile(GEN_transAvg_b1,1,1,"text/ReggeGribovPartonMC_13TeV-EPOS/GEN/transAvg_b1.txt");

TH1F *GEN_HIST_ptSum_pt5;
gDirectory->GetObject("GEN_HIST_ptSum_pt5",GEN_HIST_ptSum_pt5);
PrintHistogram(GEN_HIST_ptSum_pt5,1,1,"text/ReggeGribovPartonMC_13TeV-EPOS/GEN/HIST_ptSum_pt5.txt");

TH1F *GEN_HIST_transNch_pt5;
gDirectory->GetObject("GEN_HIST_transNch_pt5",GEN_HIST_transNch_pt5);
PrintHistogram(GEN_HIST_transNch_pt5,1,1,"text/ReggeGribovPartonMC_13TeV-EPOS/GEN/HIST_transNch_pt5.txt");

TProfile *GEN_towardTotal_bh;
gDirectory->GetObject("GEN_towardTotal_bh",GEN_towardTotal_bh);
PrintProfile(GEN_towardTotal_bh,1,1,"text/ReggeGribovPartonMC_13TeV-EPOS/GEN/towardTotal_bh.txt");

TH1F *GEN_HIST_nch;
gDirectory->GetObject("GEN_HIST_nch",GEN_HIST_nch);
PrintHistogram(GEN_HIST_nch,1,1,"text/ReggeGribovPartonMC_13TeV-EPOS/GEN/HIST_nch.txt");

TProfile *GEN_awayNch_b1;
gDirectory->GetObject("GEN_awayNch_b1",GEN_awayNch_b1);
PrintProfile(GEN_awayNch_b1,1,1,"text/ReggeGribovPartonMC_13TeV-EPOS/GEN/awayNch_b1.txt");

TProfile *GEN_awayNch_b2;
gDirectory->GetObject("GEN_awayNch_b2",GEN_awayNch_b2);
PrintProfile(GEN_awayNch_b2,1,1,"text/ReggeGribovPartonMC_13TeV-EPOS/GEN/awayNch_b2.txt");

TH1F *GEN_HIST_transPt_pt5;
gDirectory->GetObject("GEN_HIST_transPt_pt5",GEN_HIST_transPt_pt5);
PrintHistogram(GEN_HIST_transPt_pt5,1,1,"text/ReggeGribovPartonMC_13TeV-EPOS/GEN/HIST_transPt_pt5.txt");

TProfile *GEN_overallTotalAvg_b1;
gDirectory->GetObject("GEN_overallTotalAvg_b1",GEN_overallTotalAvg_b1);
PrintProfile(GEN_overallTotalAvg_b1,1,1,"text/ReggeGribovPartonMC_13TeV-EPOS/GEN/overallTotalAvg_b1.txt");

TProfile *GEN_overallTotalAvg_b2;
gDirectory->GetObject("GEN_overallTotalAvg_b2",GEN_overallTotalAvg_b2);
PrintProfile(GEN_overallTotalAvg_b2,1,1,"text/ReggeGribovPartonMC_13TeV-EPOS/GEN/overallTotalAvg_b2.txt");

TProfile *GEN_transDifNch_bh;
gDirectory->GetObject("GEN_transDifNch_bh",GEN_transDifNch_bh);
PrintProfile(GEN_transDifNch_bh,1,1,"text/ReggeGribovPartonMC_13TeV-EPOS/GEN/transDifNch_bh.txt");

TProfile *GEN_away_bh;
gDirectory->GetObject("GEN_away_bh",GEN_away_bh);
PrintProfile(GEN_away_bh,1,1,"text/ReggeGribovPartonMC_13TeV-EPOS/GEN/away_bh.txt");

TProfile *GEN_awayAvg_bh;
gDirectory->GetObject("GEN_awayAvg_bh",GEN_awayAvg_bh);
PrintProfile(GEN_awayAvg_bh,1,1,"text/ReggeGribovPartonMC_13TeV-EPOS/GEN/awayAvg_bh.txt");

TProfile *GEN_transAvg_bh;
gDirectory->GetObject("GEN_transAvg_bh",GEN_transAvg_bh);
PrintProfile(GEN_transAvg_bh,1,1,"text/ReggeGribovPartonMC_13TeV-EPOS/GEN/transAvg_bh.txt");

TProfile *GEN_awayAvg_b1;
gDirectory->GetObject("GEN_awayAvg_b1",GEN_awayAvg_b1);
PrintProfile(GEN_awayAvg_b1,1,1,"text/ReggeGribovPartonMC_13TeV-EPOS/GEN/awayAvg_b1.txt");

TProfile *GEN_away_b1;
gDirectory->GetObject("GEN_away_b1",GEN_away_b1);
PrintProfile(GEN_away_b1,1,1,"text/ReggeGribovPartonMC_13TeV-EPOS/GEN/away_b1.txt");

TProfile *GEN_away_b2;
gDirectory->GetObject("GEN_away_b2",GEN_away_b2);
PrintProfile(GEN_away_b2,1,1,"text/ReggeGribovPartonMC_13TeV-EPOS/GEN/away_b2.txt");

TProfile *GEN_awayAvg_b2;
gDirectory->GetObject("GEN_awayAvg_b2",GEN_awayAvg_b2);
PrintProfile(GEN_awayAvg_b2,1,1,"text/ReggeGribovPartonMC_13TeV-EPOS/GEN/awayAvg_b2.txt");

TH1F *GEN_HIST_transNch;
gDirectory->GetObject("GEN_HIST_transNch",GEN_HIST_transNch);
PrintHistogram(GEN_HIST_transNch,1,1,"text/ReggeGribovPartonMC_13TeV-EPOS/GEN/HIST_transNch.txt");

TProfile *GEN_overallTotalAvg_bh;
gDirectory->GetObject("GEN_overallTotalAvg_bh",GEN_overallTotalAvg_bh);
PrintProfile(GEN_overallTotalAvg_bh,1,1,"text/ReggeGribovPartonMC_13TeV-EPOS/GEN/overallTotalAvg_bh.txt");

TProfile *GEN_overallTotal_bh;
gDirectory->GetObject("GEN_overallTotal_bh",GEN_overallTotal_bh);
PrintProfile(GEN_overallTotal_bh,1,1,"text/ReggeGribovPartonMC_13TeV-EPOS/GEN/overallTotal_bh.txt");

TProfile *GEN_awayNch_bh;
gDirectory->GetObject("GEN_awayNch_bh",GEN_awayNch_bh);
PrintProfile(GEN_awayNch_bh,1,1,"text/ReggeGribovPartonMC_13TeV-EPOS/GEN/awayNch_bh.txt");

TProfile *GEN_towardTotal_b1;
gDirectory->GetObject("GEN_towardTotal_b1",GEN_towardTotal_b1);
PrintProfile(GEN_towardTotal_b1,1,1,"text/ReggeGribovPartonMC_13TeV-EPOS/GEN/towardTotal_b1.txt");

TProfile *GEN_towardTotal_b2;
gDirectory->GetObject("GEN_towardTotal_b2",GEN_towardTotal_b2);
PrintProfile(GEN_towardTotal_b2,1,1,"text/ReggeGribovPartonMC_13TeV-EPOS/GEN/towardTotal_b2.txt");



	fhist->cd("MinBias_TuneZ2star_13TeV-pythia6");

TH1F *GEN_HIST_eta_ptH;
gDirectory->GetObject("GEN_HIST_eta_ptH",GEN_HIST_eta_ptH);
PrintHistogram(GEN_HIST_eta_ptH,1,1,"text/MinBias_TuneZ2star_13TeV-pythia6/GEN/GEN_HIST_eta_ptH.txt");

TH1F *GEN_HIST_phi_all;
gDirectory->GetObject("GEN_HIST_phi_all",GEN_HIST_phi_all);
PrintHistogram(GEN_HIST_phi_all,1,1,"text/MinBias_TuneZ2star_13TeV-pythia6/GEN/GEN_HIST_phi_all.txt");

TH1F *GEN_HIST_phi_eta;
gDirectory->GetObject("GEN_HIST_phi_eta",GEN_HIST_phi_eta);
PrintHistogram(GEN_HIST_phi_eta,1,1,"text/MinBias_TuneZ2star_13TeV-pythia6/GEN/GEN_HIST_phi_eta.txt");

TH1F *GEN_HIST_phi_etaptH;
gDirectory->GetObject("GEN_HIST_phi_etaptH",GEN_HIST_phi_etaptH);
PrintHistogram(GEN_HIST_phi_etaptH,1,1,"text/MinBias_TuneZ2star_13TeV-pythia6/GEN/GEN_HIST_phi_etaptH.txt");

TH1F *GEN_HIST_phi_ptH;
gDirectory->GetObject("GEN_HIST_phi_ptH",GEN_HIST_phi_ptH);
PrintHistogram(GEN_HIST_phi_ptH,1,1,"text/MinBias_TuneZ2star_13TeV-pythia6/GEN/GEN_HIST_phi_ptH.txt");

TProfile *GEN_towardTotalAvg_b1;
gDirectory->GetObject("GEN_towardTotalAvg_b1",GEN_towardTotalAvg_b1);
PrintProfile(GEN_towardTotalAvg_b1,1,1,"text/MinBias_TuneZ2star_13TeV-pythia6/GEN/towardTotalAvg_b1.txt");

TProfile *GEN_towardTotalAvg_b2;
gDirectory->GetObject("GEN_towardTotalAvg_b2",GEN_towardTotalAvg_b2);
PrintProfile(GEN_towardTotalAvg_b2,1,1,"text/MinBias_TuneZ2star_13TeV-pythia6/GEN/towardTotalAvg_b2.txt");

TProfile *GEN_transDifNch_b1;
gDirectory->GetObject("GEN_transDifNch_b1",GEN_transDifNch_b1);
PrintProfile(GEN_transDifNch_b1,1,1,"text/MinBias_TuneZ2star_13TeV-pythia6/GEN/transDifNch_b1.txt");

TH1F *GEN_HIST_nchMB;
gDirectory->GetObject("GEN_HIST_nchMB",GEN_HIST_nchMB);
PrintHistogram(GEN_HIST_nchMB,1,1,"text/MinBias_TuneZ2star_13TeV-pythia6/GEN/HIST_nchMB.txt");

TProfile *GEN_towardNch_b2;
gDirectory->GetObject("GEN_towardNch_b2",GEN_towardNch_b2);
PrintProfile(GEN_towardNch_b2,1,1,"text/MinBias_TuneZ2star_13TeV-pythia6/GEN/towardNch_b2.txt");

TH1F *GEN_HIST_ptSumMB;
gDirectory->GetObject("GEN_HIST_ptSumMB",GEN_HIST_ptSumMB);
PrintHistogram(GEN_HIST_ptSumMB,1,1,"text/MinBias_TuneZ2star_13TeV-pythia6/GEN/HIST_ptSumMB.txt");

TProfile *GEN_trans_b2;
gDirectory->GetObject("GEN_trans_b2",GEN_trans_b2);
PrintProfile(GEN_trans_b2,1,1,"text/MinBias_TuneZ2star_13TeV-pythia6/GEN/trans_b2.txt");

TProfile *GEN_trans_b1;
gDirectory->GetObject("GEN_trans_b1",GEN_trans_b1);
PrintProfile(GEN_trans_b1,1,1,"text/MinBias_TuneZ2star_13TeV-pythia6/GEN/trans_b1.txt");

TProfile *GEN_transMax_bh;
gDirectory->GetObject("GEN_transMax_bh",GEN_transMax_bh);
PrintProfile(GEN_transMax_bh,1,1,"text/MinBias_TuneZ2star_13TeV-pythia6/GEN/transMax_bh.txt");

TProfile *GEN_overallAvg_bh;
gDirectory->GetObject("GEN_overallAvg_bh",GEN_overallAvg_bh);
PrintProfile(GEN_overallAvg_bh,1,1,"text/MinBias_TuneZ2star_13TeV-pythia6/GEN/overallAvg_bh.txt");

TProfile *GEN_toward_b2;
gDirectory->GetObject("GEN_toward_b2",GEN_toward_b2);
PrintProfile(GEN_toward_b2,1,1,"text/MinBias_TuneZ2star_13TeV-pythia6/GEN/toward_b2.txt");

TProfile *GEN_toward_b1;
gDirectory->GetObject("GEN_toward_b1",GEN_toward_b1);
PrintProfile(GEN_toward_b1,1,1,"text/MinBias_TuneZ2star_13TeV-pythia6/GEN/toward_b1.txt");

TProfile *GEN_overallTotal_b2;
gDirectory->GetObject("GEN_overallTotal_b2",GEN_overallTotal_b2);
PrintProfile(GEN_overallTotal_b2,1,1,"text/MinBias_TuneZ2star_13TeV-pythia6/GEN/overallTotal_b2.txt");

TProfile *GEN_overallTotal_b1;
gDirectory->GetObject("GEN_overallTotal_b1",GEN_overallTotal_b1);
PrintProfile(GEN_overallTotal_b1,1,1,"text/MinBias_TuneZ2star_13TeV-pythia6/GEN/overallTotal_b1.txt");

TProfile *GEN_trans_bh;
gDirectory->GetObject("GEN_trans_bh",GEN_trans_bh);
PrintProfile(GEN_trans_bh,1,1,"text/MinBias_TuneZ2star_13TeV-pythia6/GEN/trans_bh.txt");

TProfile *GEN_towardNch_bh;
gDirectory->GetObject("GEN_towardNch_bh",GEN_towardNch_bh);
PrintProfile(GEN_towardNch_bh,1,1,"text/MinBias_TuneZ2star_13TeV-pythia6/GEN/towardNch_bh.txt");

TProfile *GEN_transMaxNch_b2;
gDirectory->GetObject("GEN_transMaxNch_b2",GEN_transMaxNch_b2);
PrintProfile(GEN_transMaxNch_b2,1,1,"text/MinBias_TuneZ2star_13TeV-pythia6/GEN/transMaxNch_b2.txt");

TH1F *GEN_HIST_etaMB;
gDirectory->GetObject("GEN_HIST_etaMB",GEN_HIST_etaMB);
PrintHistogram(GEN_HIST_etaMB,1,1,"text/MinBias_TuneZ2star_13TeV-pythia6/GEN/HIST_etaMB.txt");

TProfile *GEN_towardTotalAvg_bh;
gDirectory->GetObject("GEN_towardTotalAvg_bh",GEN_towardTotalAvg_bh);
PrintProfile(GEN_towardTotalAvg_bh,1,1,"text/MinBias_TuneZ2star_13TeV-pythia6/GEN/towardTotalAvg_bh.txt");

TProfile *GEN_towardNch_b1;
gDirectory->GetObject("GEN_towardNch_b1",GEN_towardNch_b1);
PrintProfile(GEN_towardNch_b1,1,1,"text/MinBias_TuneZ2star_13TeV-pythia6/GEN/towardNch_b1.txt");

TProfile *GEN_overallTotalNch_b2;
gDirectory->GetObject("GEN_overallTotalNch_b2",GEN_overallTotalNch_b2);
PrintProfile(GEN_overallTotalNch_b2,1,1,"text/MinBias_TuneZ2star_13TeV-pythia6/GEN/overallTotalNch_b2.txt");

TProfile *GEN_overallAvg_b2;
gDirectory->GetObject("GEN_overallAvg_b2",GEN_overallAvg_b2);
PrintProfile(GEN_overallAvg_b2,1,1,"text/MinBias_TuneZ2star_13TeV-pythia6/GEN/overallAvg_b2.txt");

TProfile *GEN_overallAvg_b1;
gDirectory->GetObject("GEN_overallAvg_b1",GEN_overallAvg_b1);
PrintProfile(GEN_overallAvg_b1,1,1,"text/MinBias_TuneZ2star_13TeV-pythia6/GEN/overallAvg_b1.txt");

TProfile *GEN_toward_bh;
gDirectory->GetObject("GEN_toward_bh",GEN_toward_bh);
PrintProfile(GEN_toward_bh,1,1,"text/MinBias_TuneZ2star_13TeV-pythia6/GEN/toward_bh.txt");

TProfile *GEN_transDifNch_b2;
gDirectory->GetObject("GEN_transDifNch_b2",GEN_transDifNch_b2);
PrintProfile(GEN_transDifNch_b2,1,1,"text/MinBias_TuneZ2star_13TeV-pythia6/GEN/transDifNch_b2.txt");

TProfile *GEN_transMax_b2;
gDirectory->GetObject("GEN_transMax_b2",GEN_transMax_b2);
PrintProfile(GEN_transMax_b2,1,1,"text/MinBias_TuneZ2star_13TeV-pythia6/GEN/transMax_b2.txt");

TProfile *GEN_transMax_b1;
gDirectory->GetObject("GEN_transMax_b1",GEN_transMax_b1);
PrintProfile(GEN_transMax_b1,1,1,"text/MinBias_TuneZ2star_13TeV-pythia6/GEN/transMax_b1.txt");

TH1F *GEN_HIST_pt_pt5;
gDirectory->GetObject("GEN_HIST_pt_pt5",GEN_HIST_pt_pt5);
PrintHistogram(GEN_HIST_pt_pt5,1,1,"text/MinBias_TuneZ2star_13TeV-pythia6/GEN/HIST_pt_pt5.txt");

TProfile *GEN_ptMax_bh;
gDirectory->GetObject("GEN_ptMax_bh",GEN_ptMax_bh);
PrintProfile(GEN_ptMax_bh,1,1,"text/MinBias_TuneZ2star_13TeV-pythia6/GEN/ptMax_bh.txt");

TProfile *GEN_transMinNch_bh;
gDirectory->GetObject("GEN_transMinNch_bh",GEN_transMinNch_bh);
PrintProfile(GEN_transMinNch_bh,1,1,"text/MinBias_TuneZ2star_13TeV-pythia6/GEN/transMinNch_bh.txt");

TH1F *GEN_HIST_delPhiPt_pt5;
gDirectory->GetObject("GEN_HIST_delPhiPt_pt5",GEN_HIST_delPhiPt_pt5);
PrintHistogram(GEN_HIST_delPhiPt_pt5,1,1,"text/MinBias_TuneZ2star_13TeV-pythia6/GEN/HIST_delPhiPt_pt5.txt");

TH1F *GEN_HIST_nch_pt5;
gDirectory->GetObject("GEN_HIST_nch_pt5",GEN_HIST_nch_pt5);
PrintHistogram(GEN_HIST_nch_pt5,1,1,"text/MinBias_TuneZ2star_13TeV-pythia6/GEN/HIST_nch_pt5.txt");

TProfile *GEN_overallTotalNch_b1;
gDirectory->GetObject("GEN_overallTotalNch_b1",GEN_overallTotalNch_b1);
PrintProfile(GEN_overallTotalNch_b1,1,1,"text/MinBias_TuneZ2star_13TeV-pythia6/GEN/overallTotalNch_b1.txt");

TH1F *GEN_HIST_ptSum;
gDirectory->GetObject("GEN_HIST_ptSum",GEN_HIST_ptSum);
PrintHistogram(GEN_HIST_ptSum,1,1,"text/MinBias_TuneZ2star_13TeV-pythia6/GEN/HIST_ptSum.txt");

TProfile *GEN_transMaxNch_b1;
gDirectory->GetObject("GEN_transMaxNch_b1",GEN_transMaxNch_b1);
PrintProfile(GEN_transMaxNch_b1,1,1,"text/MinBias_TuneZ2star_13TeV-pythia6/GEN/transMaxNch_b1.txt");

TProfile *GEN_towardAvg_bh;
gDirectory->GetObject("GEN_towardAvg_bh",GEN_towardAvg_bh);
PrintProfile(GEN_towardAvg_bh,1,1,"text/MinBias_TuneZ2star_13TeV-pythia6/GEN/towardAvg_bh.txt");

TH1F *GEN_HIST_ptMax;
gDirectory->GetObject("GEN_HIST_ptMax",GEN_HIST_ptMax);
PrintHistogram(GEN_HIST_ptMax,1,1,"text/MinBias_TuneZ2star_13TeV-pythia6/GEN/HIST_ptMax.txt");

TH1F *GEN_HIST_transPtSum_pt5;
gDirectory->GetObject("GEN_HIST_transPtSum_pt5",GEN_HIST_transPtSum_pt5);
PrintHistogram(GEN_HIST_transPtSum_pt5,1,1,"text/MinBias_TuneZ2star_13TeV-pythia6/GEN/HIST_transPtSum_pt5.txt");

TProfile *GEN_transMinNch_b1;
gDirectory->GetObject("GEN_transMinNch_b1",GEN_transMinNch_b1);
PrintProfile(GEN_transMinNch_b1,1,1,"text/MinBias_TuneZ2star_13TeV-pythia6/GEN/transMinNch_b1.txt");

TProfile *GEN_transMinNch_b2;
gDirectory->GetObject("GEN_transMinNch_b2",GEN_transMinNch_b2);
PrintProfile(GEN_transMinNch_b2,1,1,"text/MinBias_TuneZ2star_13TeV-pythia6/GEN/transMinNch_b2.txt");

TProfile *GEN_ptMax_b2;
gDirectory->GetObject("GEN_ptMax_b2",GEN_ptMax_b2);
PrintProfile(GEN_ptMax_b2,1,1,"text/MinBias_TuneZ2star_13TeV-pythia6/GEN/ptMax_b2.txt");

TProfile *GEN_ptMax_b1;
gDirectory->GetObject("GEN_ptMax_b1",GEN_ptMax_b1);
PrintProfile(GEN_ptMax_b1,1,1,"text/MinBias_TuneZ2star_13TeV-pythia6/GEN/ptMax_b1.txt");

TH1F *GEN_HIST_transPt;
gDirectory->GetObject("GEN_HIST_transPt",GEN_HIST_transPt);
PrintHistogram(GEN_HIST_transPt,1,1,"text/MinBias_TuneZ2star_13TeV-pythia6/GEN/HIST_transPt.txt");

TProfile *GEN_overallTotalNch_bh;
gDirectory->GetObject("GEN_overallTotalNch_bh",GEN_overallTotalNch_bh);
PrintProfile(GEN_overallTotalNch_bh,1,1,"text/MinBias_TuneZ2star_13TeV-pythia6/GEN/overallTotalNch_bh.txt");

TProfile *GEN_transMaxNch_bh;
gDirectory->GetObject("GEN_transMaxNch_bh",GEN_transMaxNch_bh);
PrintProfile(GEN_transMaxNch_bh,1,1,"text/MinBias_TuneZ2star_13TeV-pythia6/GEN/transMaxNch_bh.txt");

TProfile *GEN_towardAvg_b1;
gDirectory->GetObject("GEN_towardAvg_b1",GEN_towardAvg_b1);
PrintProfile(GEN_towardAvg_b1,1,1,"text/MinBias_TuneZ2star_13TeV-pythia6/GEN/towardAvg_b1.txt");

TProfile *GEN_towardAvg_b2;
gDirectory->GetObject("GEN_towardAvg_b2",GEN_towardAvg_b2);
PrintProfile(GEN_towardAvg_b2,1,1,"text/MinBias_TuneZ2star_13TeV-pythia6/GEN/towardAvg_b2.txt");

TH1F *GEN_HIST_delPhiPt;
gDirectory->GetObject("GEN_HIST_delPhiPt",GEN_HIST_delPhiPt);
PrintHistogram(GEN_HIST_delPhiPt,1,1,"text/MinBias_TuneZ2star_13TeV-pythia6/GEN/HIST_delPhiPt.txt");

TH1F *GEN_HIST_ptMB;
gDirectory->GetObject("GEN_HIST_ptMB",GEN_HIST_ptMB);
PrintHistogram(GEN_HIST_ptMB,1,1,"text/MinBias_TuneZ2star_13TeV-pythia6/GEN/HIST_ptMB.txt");

TProfile *GEN_transDif_b2;
gDirectory->GetObject("GEN_transDif_b2",GEN_transDif_b2);
PrintProfile(GEN_transDif_b2,1,1,"text/MinBias_TuneZ2star_13TeV-pythia6/GEN/transDif_b2.txt");

TProfile *GEN_transDif_b1;
gDirectory->GetObject("GEN_transDif_b1",GEN_transDif_b1);
PrintProfile(GEN_transDif_b1,1,1,"text/MinBias_TuneZ2star_13TeV-pythia6/GEN/transDif_b1.txt");

TProfile *GEN_transMin_b1;
gDirectory->GetObject("GEN_transMin_b1",GEN_transMin_b1);
PrintProfile(GEN_transMin_b1,1,1,"text/MinBias_TuneZ2star_13TeV-pythia6/GEN/transMin_b1.txt");

TProfile *GEN_transMin_b2;
gDirectory->GetObject("GEN_transMin_b2",GEN_transMin_b2);
PrintProfile(GEN_transMin_b2,1,1,"text/MinBias_TuneZ2star_13TeV-pythia6/GEN/transMin_b2.txt");

TH1F *GEN_HIST_delPhi;
gDirectory->GetObject("GEN_HIST_delPhi",GEN_HIST_delPhi);
PrintHistogram(GEN_HIST_delPhi,1,1,"text/MinBias_TuneZ2star_13TeV-pythia6/GEN/HIST_delPhi.txt");

TProfile *GEN_transNch_bh;
gDirectory->GetObject("GEN_transNch_bh",GEN_transNch_bh);
PrintProfile(GEN_transNch_bh,1,1,"text/MinBias_TuneZ2star_13TeV-pythia6/GEN/transNch_bh.txt");

TProfile *GEN_overall_bh;
gDirectory->GetObject("GEN_overall_bh",GEN_overall_bh);
PrintProfile(GEN_overall_bh,1,1,"text/MinBias_TuneZ2star_13TeV-pythia6/GEN/overall_bh.txt");

TProfile *GEN_towardTotalNch_b1;
gDirectory->GetObject("GEN_towardTotalNch_b1",GEN_towardTotalNch_b1);
PrintProfile(GEN_towardTotalNch_b1,1,1,"text/MinBias_TuneZ2star_13TeV-pythia6/GEN/towardTotalNch_b1.txt");

TProfile *GEN_towardTotalNch_b2;
gDirectory->GetObject("GEN_towardTotalNch_b2",GEN_towardTotalNch_b2);
PrintProfile(GEN_towardTotalNch_b2,1,1,"text/MinBias_TuneZ2star_13TeV-pythia6/GEN/towardTotalNch_b2.txt");

TProfile *GEN_overallNch_bh;
gDirectory->GetObject("GEN_overallNch_bh",GEN_overallNch_bh);
PrintProfile(GEN_overallNch_bh,1,1,"text/MinBias_TuneZ2star_13TeV-pythia6/GEN/overallNch_bh.txt");

TProfile *GEN_transMin_bh;
gDirectory->GetObject("GEN_transMin_bh",GEN_transMin_bh);
PrintProfile(GEN_transMin_bh,1,1,"text/MinBias_TuneZ2star_13TeV-pythia6/GEN/transMin_bh.txt");

TH1F *GEN_HIST_transPtSum;
gDirectory->GetObject("GEN_HIST_transPtSum",GEN_HIST_transPtSum);
PrintHistogram(GEN_HIST_transPtSum,1,1,"text/MinBias_TuneZ2star_13TeV-pythia6/GEN/HIST_transPtSum.txt");

TH1F *GEN_HIST_eta_pt5;
gDirectory->GetObject("GEN_HIST_eta_pt5",GEN_HIST_eta_pt5);
PrintHistogram(GEN_HIST_eta_pt5,1,1,"text/MinBias_TuneZ2star_13TeV-pythia6/GEN/HIST_eta_pt5.txt");

TH1F *GEN_HIST_delPhi_pt5;
gDirectory->GetObject("GEN_HIST_delPhi_pt5",GEN_HIST_delPhi_pt5);
PrintHistogram(GEN_HIST_delPhi_pt5,1,1,"text/MinBias_TuneZ2star_13TeV-pythia6/GEN/HIST_delPhi_pt5.txt");

TProfile *GEN_transDif_bh;
gDirectory->GetObject("GEN_transDif_bh",GEN_transDif_bh);
PrintProfile(GEN_transDif_bh,1,1,"text/MinBias_TuneZ2star_13TeV-pythia6/GEN/transDif_bh.txt");

TProfile *GEN_overallNch_b2;
gDirectory->GetObject("GEN_overallNch_b2",GEN_overallNch_b2);
PrintProfile(GEN_overallNch_b2,1,1,"text/MinBias_TuneZ2star_13TeV-pythia6/GEN/overallNch_b2.txt");

TProfile *GEN_overallNch_b1;
gDirectory->GetObject("GEN_overallNch_b1",GEN_overallNch_b1);
PrintProfile(GEN_overallNch_b1,1,1,"text/MinBias_TuneZ2star_13TeV-pythia6/GEN/overallNch_b1.txt");

TProfile *GEN_towardTotalNch_bh;
gDirectory->GetObject("GEN_towardTotalNch_bh",GEN_towardTotalNch_bh);
PrintProfile(GEN_towardTotalNch_bh,1,1,"text/MinBias_TuneZ2star_13TeV-pythia6/GEN/towardTotalNch_bh.txt");

TProfile *GEN_transAvg_b2;
gDirectory->GetObject("GEN_transAvg_b2",GEN_transAvg_b2);
PrintProfile(GEN_transAvg_b2,1,1,"text/MinBias_TuneZ2star_13TeV-pythia6/GEN/transAvg_b2.txt");

TProfile *GEN_overall_b2;
gDirectory->GetObject("GEN_overall_b2",GEN_overall_b2);
PrintProfile(GEN_overall_b2,1,1,"text/MinBias_TuneZ2star_13TeV-pythia6/GEN/overall_b2.txt");

TProfile *GEN_overall_b1;
gDirectory->GetObject("GEN_overall_b1",GEN_overall_b1);
PrintProfile(GEN_overall_b1,1,1,"text/MinBias_TuneZ2star_13TeV-pythia6/GEN/overall_b1.txt");

TProfile *GEN_transNch_b1;
gDirectory->GetObject("GEN_transNch_b1",GEN_transNch_b1);
PrintProfile(GEN_transNch_b1,1,1,"text/MinBias_TuneZ2star_13TeV-pythia6/GEN/transNch_b1.txt");

TProfile *GEN_transNch_b2;
gDirectory->GetObject("GEN_transNch_b2",GEN_transNch_b2);
PrintProfile(GEN_transNch_b2,1,1,"text/MinBias_TuneZ2star_13TeV-pythia6/GEN/transNch_b2.txt");

TProfile *GEN_transAvg_b1;
gDirectory->GetObject("GEN_transAvg_b1",GEN_transAvg_b1);
PrintProfile(GEN_transAvg_b1,1,1,"text/MinBias_TuneZ2star_13TeV-pythia6/GEN/transAvg_b1.txt");

TH1F *GEN_HIST_ptSum_pt5;
gDirectory->GetObject("GEN_HIST_ptSum_pt5",GEN_HIST_ptSum_pt5);
PrintHistogram(GEN_HIST_ptSum_pt5,1,1,"text/MinBias_TuneZ2star_13TeV-pythia6/GEN/HIST_ptSum_pt5.txt");

TH1F *GEN_HIST_transNch_pt5;
gDirectory->GetObject("GEN_HIST_transNch_pt5",GEN_HIST_transNch_pt5);
PrintHistogram(GEN_HIST_transNch_pt5,1,1,"text/MinBias_TuneZ2star_13TeV-pythia6/GEN/HIST_transNch_pt5.txt");

TProfile *GEN_towardTotal_bh;
gDirectory->GetObject("GEN_towardTotal_bh",GEN_towardTotal_bh);
PrintProfile(GEN_towardTotal_bh,1,1,"text/MinBias_TuneZ2star_13TeV-pythia6/GEN/towardTotal_bh.txt");

TH1F *GEN_HIST_nch;
gDirectory->GetObject("GEN_HIST_nch",GEN_HIST_nch);
PrintHistogram(GEN_HIST_nch,1,1,"text/MinBias_TuneZ2star_13TeV-pythia6/GEN/HIST_nch.txt");

TProfile *GEN_awayNch_b1;
gDirectory->GetObject("GEN_awayNch_b1",GEN_awayNch_b1);
PrintProfile(GEN_awayNch_b1,1,1,"text/MinBias_TuneZ2star_13TeV-pythia6/GEN/awayNch_b1.txt");

TProfile *GEN_awayNch_b2;
gDirectory->GetObject("GEN_awayNch_b2",GEN_awayNch_b2);
PrintProfile(GEN_awayNch_b2,1,1,"text/MinBias_TuneZ2star_13TeV-pythia6/GEN/awayNch_b2.txt");

TH1F *GEN_HIST_transPt_pt5;
gDirectory->GetObject("GEN_HIST_transPt_pt5",GEN_HIST_transPt_pt5);
PrintHistogram(GEN_HIST_transPt_pt5,1,1,"text/MinBias_TuneZ2star_13TeV-pythia6/GEN/HIST_transPt_pt5.txt");

TProfile *GEN_overallTotalAvg_b1;
gDirectory->GetObject("GEN_overallTotalAvg_b1",GEN_overallTotalAvg_b1);
PrintProfile(GEN_overallTotalAvg_b1,1,1,"text/MinBias_TuneZ2star_13TeV-pythia6/GEN/overallTotalAvg_b1.txt");

TProfile *GEN_overallTotalAvg_b2;
gDirectory->GetObject("GEN_overallTotalAvg_b2",GEN_overallTotalAvg_b2);
PrintProfile(GEN_overallTotalAvg_b2,1,1,"text/MinBias_TuneZ2star_13TeV-pythia6/GEN/overallTotalAvg_b2.txt");

TProfile *GEN_transDifNch_bh;
gDirectory->GetObject("GEN_transDifNch_bh",GEN_transDifNch_bh);
PrintProfile(GEN_transDifNch_bh,1,1,"text/MinBias_TuneZ2star_13TeV-pythia6/GEN/transDifNch_bh.txt");

TProfile *GEN_away_bh;
gDirectory->GetObject("GEN_away_bh",GEN_away_bh);
PrintProfile(GEN_away_bh,1,1,"text/MinBias_TuneZ2star_13TeV-pythia6/GEN/away_bh.txt");

TProfile *GEN_awayAvg_bh;
gDirectory->GetObject("GEN_awayAvg_bh",GEN_awayAvg_bh);
PrintProfile(GEN_awayAvg_bh,1,1,"text/MinBias_TuneZ2star_13TeV-pythia6/GEN/awayAvg_bh.txt");

TProfile *GEN_transAvg_bh;
gDirectory->GetObject("GEN_transAvg_bh",GEN_transAvg_bh);
PrintProfile(GEN_transAvg_bh,1,1,"text/MinBias_TuneZ2star_13TeV-pythia6/GEN/transAvg_bh.txt");

TProfile *GEN_awayAvg_b1;
gDirectory->GetObject("GEN_awayAvg_b1",GEN_awayAvg_b1);
PrintProfile(GEN_awayAvg_b1,1,1,"text/MinBias_TuneZ2star_13TeV-pythia6/GEN/awayAvg_b1.txt");

TProfile *GEN_away_b1;
gDirectory->GetObject("GEN_away_b1",GEN_away_b1);
PrintProfile(GEN_away_b1,1,1,"text/MinBias_TuneZ2star_13TeV-pythia6/GEN/away_b1.txt");

TProfile *GEN_away_b2;
gDirectory->GetObject("GEN_away_b2",GEN_away_b2);
PrintProfile(GEN_away_b2,1,1,"text/MinBias_TuneZ2star_13TeV-pythia6/GEN/away_b2.txt");

TProfile *GEN_awayAvg_b2;
gDirectory->GetObject("GEN_awayAvg_b2",GEN_awayAvg_b2);
PrintProfile(GEN_awayAvg_b2,1,1,"text/MinBias_TuneZ2star_13TeV-pythia6/GEN/awayAvg_b2.txt");

TH1F *GEN_HIST_transNch;
gDirectory->GetObject("GEN_HIST_transNch",GEN_HIST_transNch);
PrintHistogram(GEN_HIST_transNch,1,1,"text/MinBias_TuneZ2star_13TeV-pythia6/GEN/HIST_transNch.txt");

TProfile *GEN_overallTotalAvg_bh;
gDirectory->GetObject("GEN_overallTotalAvg_bh",GEN_overallTotalAvg_bh);
PrintProfile(GEN_overallTotalAvg_bh,1,1,"text/MinBias_TuneZ2star_13TeV-pythia6/GEN/overallTotalAvg_bh.txt");

TProfile *GEN_overallTotal_bh;
gDirectory->GetObject("GEN_overallTotal_bh",GEN_overallTotal_bh);
PrintProfile(GEN_overallTotal_bh,1,1,"text/MinBias_TuneZ2star_13TeV-pythia6/GEN/overallTotal_bh.txt");

TProfile *GEN_awayNch_bh;
gDirectory->GetObject("GEN_awayNch_bh",GEN_awayNch_bh);
PrintProfile(GEN_awayNch_bh,1,1,"text/MinBias_TuneZ2star_13TeV-pythia6/GEN/awayNch_bh.txt");

TProfile *GEN_towardTotal_b1;
gDirectory->GetObject("GEN_towardTotal_b1",GEN_towardTotal_b1);
PrintProfile(GEN_towardTotal_b1,1,1,"text/MinBias_TuneZ2star_13TeV-pythia6/GEN/towardTotal_b1.txt");

TProfile *GEN_towardTotal_b2;
gDirectory->GetObject("GEN_towardTotal_b2",GEN_towardTotal_b2);
PrintProfile(GEN_towardTotal_b2,1,1,"text/MinBias_TuneZ2star_13TeV-pythia6/GEN/towardTotal_b2.txt");



	fhist->cd("MinBias_TuneMonash13_13TeV-pythia8");


TH1F *GEN_HIST_eta_ptH;
gDirectory->GetObject("GEN_HIST_eta_ptH",GEN_HIST_eta_ptH);
PrintHistogram(GEN_HIST_eta_ptH,1,1,"text/MinBias_TuneMonash13_13TeV-pythia8/GEN/GEN_HIST_eta_ptH.txt");

TH1F *GEN_HIST_phi_all;
gDirectory->GetObject("GEN_HIST_phi_all",GEN_HIST_phi_all);
PrintHistogram(GEN_HIST_phi_all,1,1,"text/MinBias_TuneMonash13_13TeV-pythia8/GEN/GEN_HIST_phi_all.txt");

TH1F *GEN_HIST_phi_eta;
gDirectory->GetObject("GEN_HIST_phi_eta",GEN_HIST_phi_eta);
PrintHistogram(GEN_HIST_phi_eta,1,1,"text/MinBias_TuneMonash13_13TeV-pythia8/GEN/GEN_HIST_phi_eta.txt");

TH1F *GEN_HIST_phi_etaptH;
gDirectory->GetObject("GEN_HIST_phi_etaptH",GEN_HIST_phi_etaptH);
PrintHistogram(GEN_HIST_phi_etaptH,1,1,"text/MinBias_TuneMonash13_13TeV-pythia8/GEN/GEN_HIST_phi_etaptH.txt");

TH1F *GEN_HIST_phi_ptH;
gDirectory->GetObject("GEN_HIST_phi_ptH",GEN_HIST_phi_ptH);
PrintHistogram(GEN_HIST_phi_ptH,1,1,"text/MinBias_TuneMonash13_13TeV-pythia8/GEN/GEN_HIST_phi_ptH.txt");

TProfile *GEN_towardTotalAvg_b1;
gDirectory->GetObject("GEN_towardTotalAvg_b1",GEN_towardTotalAvg_b1);
PrintProfile(GEN_towardTotalAvg_b1,1,1,"text/MinBias_TuneMonash13_13TeV-pythia8/GEN/towardTotalAvg_b1.txt");

TProfile *GEN_towardTotalAvg_b2;
gDirectory->GetObject("GEN_towardTotalAvg_b2",GEN_towardTotalAvg_b2);
PrintProfile(GEN_towardTotalAvg_b2,1,1,"text/MinBias_TuneMonash13_13TeV-pythia8/GEN/towardTotalAvg_b2.txt");

TProfile *GEN_transDifNch_b1;
gDirectory->GetObject("GEN_transDifNch_b1",GEN_transDifNch_b1);
PrintProfile(GEN_transDifNch_b1,1,1,"text/MinBias_TuneMonash13_13TeV-pythia8/GEN/transDifNch_b1.txt");

TH1F *GEN_HIST_nchMB;
gDirectory->GetObject("GEN_HIST_nchMB",GEN_HIST_nchMB);
PrintHistogram(GEN_HIST_nchMB,1,1,"text/MinBias_TuneMonash13_13TeV-pythia8/GEN/HIST_nchMB.txt");

TProfile *GEN_towardNch_b2;
gDirectory->GetObject("GEN_towardNch_b2",GEN_towardNch_b2);
PrintProfile(GEN_towardNch_b2,1,1,"text/MinBias_TuneMonash13_13TeV-pythia8/GEN/towardNch_b2.txt");

TH1F *GEN_HIST_ptSumMB;
gDirectory->GetObject("GEN_HIST_ptSumMB",GEN_HIST_ptSumMB);
PrintHistogram(GEN_HIST_ptSumMB,1,1,"text/MinBias_TuneMonash13_13TeV-pythia8/GEN/HIST_ptSumMB.txt");

TProfile *GEN_trans_b2;
gDirectory->GetObject("GEN_trans_b2",GEN_trans_b2);
PrintProfile(GEN_trans_b2,1,1,"text/MinBias_TuneMonash13_13TeV-pythia8/GEN/trans_b2.txt");

TProfile *GEN_trans_b1;
gDirectory->GetObject("GEN_trans_b1",GEN_trans_b1);
PrintProfile(GEN_trans_b1,1,1,"text/MinBias_TuneMonash13_13TeV-pythia8/GEN/trans_b1.txt");

TProfile *GEN_transMax_bh;
gDirectory->GetObject("GEN_transMax_bh",GEN_transMax_bh);
PrintProfile(GEN_transMax_bh,1,1,"text/MinBias_TuneMonash13_13TeV-pythia8/GEN/transMax_bh.txt");

TProfile *GEN_overallAvg_bh;
gDirectory->GetObject("GEN_overallAvg_bh",GEN_overallAvg_bh);
PrintProfile(GEN_overallAvg_bh,1,1,"text/MinBias_TuneMonash13_13TeV-pythia8/GEN/overallAvg_bh.txt");

TProfile *GEN_toward_b2;
gDirectory->GetObject("GEN_toward_b2",GEN_toward_b2);
PrintProfile(GEN_toward_b2,1,1,"text/MinBias_TuneMonash13_13TeV-pythia8/GEN/toward_b2.txt");

TProfile *GEN_toward_b1;
gDirectory->GetObject("GEN_toward_b1",GEN_toward_b1);
PrintProfile(GEN_toward_b1,1,1,"text/MinBias_TuneMonash13_13TeV-pythia8/GEN/toward_b1.txt");

TProfile *GEN_overallTotal_b2;
gDirectory->GetObject("GEN_overallTotal_b2",GEN_overallTotal_b2);
PrintProfile(GEN_overallTotal_b2,1,1,"text/MinBias_TuneMonash13_13TeV-pythia8/GEN/overallTotal_b2.txt");

TProfile *GEN_overallTotal_b1;
gDirectory->GetObject("GEN_overallTotal_b1",GEN_overallTotal_b1);
PrintProfile(GEN_overallTotal_b1,1,1,"text/MinBias_TuneMonash13_13TeV-pythia8/GEN/overallTotal_b1.txt");

TProfile *GEN_trans_bh;
gDirectory->GetObject("GEN_trans_bh",GEN_trans_bh);
PrintProfile(GEN_trans_bh,1,1,"text/MinBias_TuneMonash13_13TeV-pythia8/GEN/trans_bh.txt");

TProfile *GEN_towardNch_bh;
gDirectory->GetObject("GEN_towardNch_bh",GEN_towardNch_bh);
PrintProfile(GEN_towardNch_bh,1,1,"text/MinBias_TuneMonash13_13TeV-pythia8/GEN/towardNch_bh.txt");

TProfile *GEN_transMaxNch_b2;
gDirectory->GetObject("GEN_transMaxNch_b2",GEN_transMaxNch_b2);
PrintProfile(GEN_transMaxNch_b2,1,1,"text/MinBias_TuneMonash13_13TeV-pythia8/GEN/transMaxNch_b2.txt");

TH1F *GEN_HIST_etaMB;
gDirectory->GetObject("GEN_HIST_etaMB",GEN_HIST_etaMB);
PrintHistogram(GEN_HIST_etaMB,1,1,"text/MinBias_TuneMonash13_13TeV-pythia8/GEN/HIST_etaMB.txt");

TProfile *GEN_towardTotalAvg_bh;
gDirectory->GetObject("GEN_towardTotalAvg_bh",GEN_towardTotalAvg_bh);
PrintProfile(GEN_towardTotalAvg_bh,1,1,"text/MinBias_TuneMonash13_13TeV-pythia8/GEN/towardTotalAvg_bh.txt");

TProfile *GEN_towardNch_b1;
gDirectory->GetObject("GEN_towardNch_b1",GEN_towardNch_b1);
PrintProfile(GEN_towardNch_b1,1,1,"text/MinBias_TuneMonash13_13TeV-pythia8/GEN/towardNch_b1.txt");

TProfile *GEN_overallTotalNch_b2;
gDirectory->GetObject("GEN_overallTotalNch_b2",GEN_overallTotalNch_b2);
PrintProfile(GEN_overallTotalNch_b2,1,1,"text/MinBias_TuneMonash13_13TeV-pythia8/GEN/overallTotalNch_b2.txt");

TProfile *GEN_overallAvg_b2;
gDirectory->GetObject("GEN_overallAvg_b2",GEN_overallAvg_b2);
PrintProfile(GEN_overallAvg_b2,1,1,"text/MinBias_TuneMonash13_13TeV-pythia8/GEN/overallAvg_b2.txt");

TProfile *GEN_overallAvg_b1;
gDirectory->GetObject("GEN_overallAvg_b1",GEN_overallAvg_b1);
PrintProfile(GEN_overallAvg_b1,1,1,"text/MinBias_TuneMonash13_13TeV-pythia8/GEN/overallAvg_b1.txt");

TProfile *GEN_toward_bh;
gDirectory->GetObject("GEN_toward_bh",GEN_toward_bh);
PrintProfile(GEN_toward_bh,1,1,"text/MinBias_TuneMonash13_13TeV-pythia8/GEN/toward_bh.txt");

TProfile *GEN_transDifNch_b2;
gDirectory->GetObject("GEN_transDifNch_b2",GEN_transDifNch_b2);
PrintProfile(GEN_transDifNch_b2,1,1,"text/MinBias_TuneMonash13_13TeV-pythia8/GEN/transDifNch_b2.txt");

TProfile *GEN_transMax_b2;
gDirectory->GetObject("GEN_transMax_b2",GEN_transMax_b2);
PrintProfile(GEN_transMax_b2,1,1,"text/MinBias_TuneMonash13_13TeV-pythia8/GEN/transMax_b2.txt");

TProfile *GEN_transMax_b1;
gDirectory->GetObject("GEN_transMax_b1",GEN_transMax_b1);
PrintProfile(GEN_transMax_b1,1,1,"text/MinBias_TuneMonash13_13TeV-pythia8/GEN/transMax_b1.txt");

TH1F *GEN_HIST_pt_pt5;
gDirectory->GetObject("GEN_HIST_pt_pt5",GEN_HIST_pt_pt5);
PrintHistogram(GEN_HIST_pt_pt5,1,1,"text/MinBias_TuneMonash13_13TeV-pythia8/GEN/HIST_pt_pt5.txt");

TProfile *GEN_ptMax_bh;
gDirectory->GetObject("GEN_ptMax_bh",GEN_ptMax_bh);
PrintProfile(GEN_ptMax_bh,1,1,"text/MinBias_TuneMonash13_13TeV-pythia8/GEN/ptMax_bh.txt");

TProfile *GEN_transMinNch_bh;
gDirectory->GetObject("GEN_transMinNch_bh",GEN_transMinNch_bh);
PrintProfile(GEN_transMinNch_bh,1,1,"text/MinBias_TuneMonash13_13TeV-pythia8/GEN/transMinNch_bh.txt");

TH1F *GEN_HIST_delPhiPt_pt5;
gDirectory->GetObject("GEN_HIST_delPhiPt_pt5",GEN_HIST_delPhiPt_pt5);
PrintHistogram(GEN_HIST_delPhiPt_pt5,1,1,"text/MinBias_TuneMonash13_13TeV-pythia8/GEN/HIST_delPhiPt_pt5.txt");

TH1F *GEN_HIST_nch_pt5;
gDirectory->GetObject("GEN_HIST_nch_pt5",GEN_HIST_nch_pt5);
PrintHistogram(GEN_HIST_nch_pt5,1,1,"text/MinBias_TuneMonash13_13TeV-pythia8/GEN/HIST_nch_pt5.txt");

TProfile *GEN_overallTotalNch_b1;
gDirectory->GetObject("GEN_overallTotalNch_b1",GEN_overallTotalNch_b1);
PrintProfile(GEN_overallTotalNch_b1,1,1,"text/MinBias_TuneMonash13_13TeV-pythia8/GEN/overallTotalNch_b1.txt");

TH1F *GEN_HIST_ptSum;
gDirectory->GetObject("GEN_HIST_ptSum",GEN_HIST_ptSum);
PrintHistogram(GEN_HIST_ptSum,1,1,"text/MinBias_TuneMonash13_13TeV-pythia8/GEN/HIST_ptSum.txt");

TProfile *GEN_transMaxNch_b1;
gDirectory->GetObject("GEN_transMaxNch_b1",GEN_transMaxNch_b1);
PrintProfile(GEN_transMaxNch_b1,1,1,"text/MinBias_TuneMonash13_13TeV-pythia8/GEN/transMaxNch_b1.txt");

TProfile *GEN_towardAvg_bh;
gDirectory->GetObject("GEN_towardAvg_bh",GEN_towardAvg_bh);
PrintProfile(GEN_towardAvg_bh,1,1,"text/MinBias_TuneMonash13_13TeV-pythia8/GEN/towardAvg_bh.txt");

TH1F *GEN_HIST_ptMax;
gDirectory->GetObject("GEN_HIST_ptMax",GEN_HIST_ptMax);
PrintHistogram(GEN_HIST_ptMax,1,1,"text/MinBias_TuneMonash13_13TeV-pythia8/GEN/HIST_ptMax.txt");

TH1F *GEN_HIST_transPtSum_pt5;
gDirectory->GetObject("GEN_HIST_transPtSum_pt5",GEN_HIST_transPtSum_pt5);
PrintHistogram(GEN_HIST_transPtSum_pt5,1,1,"text/MinBias_TuneMonash13_13TeV-pythia8/GEN/HIST_transPtSum_pt5.txt");

TProfile *GEN_transMinNch_b1;
gDirectory->GetObject("GEN_transMinNch_b1",GEN_transMinNch_b1);
PrintProfile(GEN_transMinNch_b1,1,1,"text/MinBias_TuneMonash13_13TeV-pythia8/GEN/transMinNch_b1.txt");

TProfile *GEN_transMinNch_b2;
gDirectory->GetObject("GEN_transMinNch_b2",GEN_transMinNch_b2);
PrintProfile(GEN_transMinNch_b2,1,1,"text/MinBias_TuneMonash13_13TeV-pythia8/GEN/transMinNch_b2.txt");

TProfile *GEN_ptMax_b2;
gDirectory->GetObject("GEN_ptMax_b2",GEN_ptMax_b2);
PrintProfile(GEN_ptMax_b2,1,1,"text/MinBias_TuneMonash13_13TeV-pythia8/GEN/ptMax_b2.txt");

TProfile *GEN_ptMax_b1;
gDirectory->GetObject("GEN_ptMax_b1",GEN_ptMax_b1);
PrintProfile(GEN_ptMax_b1,1,1,"text/MinBias_TuneMonash13_13TeV-pythia8/GEN/ptMax_b1.txt");

TH1F *GEN_HIST_transPt;
gDirectory->GetObject("GEN_HIST_transPt",GEN_HIST_transPt);
PrintHistogram(GEN_HIST_transPt,1,1,"text/MinBias_TuneMonash13_13TeV-pythia8/GEN/HIST_transPt.txt");

TProfile *GEN_overallTotalNch_bh;
gDirectory->GetObject("GEN_overallTotalNch_bh",GEN_overallTotalNch_bh);
PrintProfile(GEN_overallTotalNch_bh,1,1,"text/MinBias_TuneMonash13_13TeV-pythia8/GEN/overallTotalNch_bh.txt");

TProfile *GEN_transMaxNch_bh;
gDirectory->GetObject("GEN_transMaxNch_bh",GEN_transMaxNch_bh);
PrintProfile(GEN_transMaxNch_bh,1,1,"text/MinBias_TuneMonash13_13TeV-pythia8/GEN/transMaxNch_bh.txt");

TProfile *GEN_towardAvg_b1;
gDirectory->GetObject("GEN_towardAvg_b1",GEN_towardAvg_b1);
PrintProfile(GEN_towardAvg_b1,1,1,"text/MinBias_TuneMonash13_13TeV-pythia8/GEN/towardAvg_b1.txt");

TProfile *GEN_towardAvg_b2;
gDirectory->GetObject("GEN_towardAvg_b2",GEN_towardAvg_b2);
PrintProfile(GEN_towardAvg_b2,1,1,"text/MinBias_TuneMonash13_13TeV-pythia8/GEN/towardAvg_b2.txt");

TH1F *GEN_HIST_delPhiPt;
gDirectory->GetObject("GEN_HIST_delPhiPt",GEN_HIST_delPhiPt);
PrintHistogram(GEN_HIST_delPhiPt,1,1,"text/MinBias_TuneMonash13_13TeV-pythia8/GEN/HIST_delPhiPt.txt");

TH1F *GEN_HIST_ptMB;
gDirectory->GetObject("GEN_HIST_ptMB",GEN_HIST_ptMB);
PrintHistogram(GEN_HIST_ptMB,1,1,"text/MinBias_TuneMonash13_13TeV-pythia8/GEN/HIST_ptMB.txt");

TProfile *GEN_transDif_b2;
gDirectory->GetObject("GEN_transDif_b2",GEN_transDif_b2);
PrintProfile(GEN_transDif_b2,1,1,"text/MinBias_TuneMonash13_13TeV-pythia8/GEN/transDif_b2.txt");

TProfile *GEN_transDif_b1;
gDirectory->GetObject("GEN_transDif_b1",GEN_transDif_b1);
PrintProfile(GEN_transDif_b1,1,1,"text/MinBias_TuneMonash13_13TeV-pythia8/GEN/transDif_b1.txt");

TProfile *GEN_transMin_b1;
gDirectory->GetObject("GEN_transMin_b1",GEN_transMin_b1);
PrintProfile(GEN_transMin_b1,1,1,"text/MinBias_TuneMonash13_13TeV-pythia8/GEN/transMin_b1.txt");

TProfile *GEN_transMin_b2;
gDirectory->GetObject("GEN_transMin_b2",GEN_transMin_b2);
PrintProfile(GEN_transMin_b2,1,1,"text/MinBias_TuneMonash13_13TeV-pythia8/GEN/transMin_b2.txt");

TH1F *GEN_HIST_delPhi;
gDirectory->GetObject("GEN_HIST_delPhi",GEN_HIST_delPhi);
PrintHistogram(GEN_HIST_delPhi,1,1,"text/MinBias_TuneMonash13_13TeV-pythia8/GEN/HIST_delPhi.txt");

TProfile *GEN_transNch_bh;
gDirectory->GetObject("GEN_transNch_bh",GEN_transNch_bh);
PrintProfile(GEN_transNch_bh,1,1,"text/MinBias_TuneMonash13_13TeV-pythia8/GEN/transNch_bh.txt");

TProfile *GEN_overall_bh;
gDirectory->GetObject("GEN_overall_bh",GEN_overall_bh);
PrintProfile(GEN_overall_bh,1,1,"text/MinBias_TuneMonash13_13TeV-pythia8/GEN/overall_bh.txt");

TProfile *GEN_towardTotalNch_b1;
gDirectory->GetObject("GEN_towardTotalNch_b1",GEN_towardTotalNch_b1);
PrintProfile(GEN_towardTotalNch_b1,1,1,"text/MinBias_TuneMonash13_13TeV-pythia8/GEN/towardTotalNch_b1.txt");

TProfile *GEN_towardTotalNch_b2;
gDirectory->GetObject("GEN_towardTotalNch_b2",GEN_towardTotalNch_b2);
PrintProfile(GEN_towardTotalNch_b2,1,1,"text/MinBias_TuneMonash13_13TeV-pythia8/GEN/towardTotalNch_b2.txt");

TProfile *GEN_overallNch_bh;
gDirectory->GetObject("GEN_overallNch_bh",GEN_overallNch_bh);
PrintProfile(GEN_overallNch_bh,1,1,"text/MinBias_TuneMonash13_13TeV-pythia8/GEN/overallNch_bh.txt");

TProfile *GEN_transMin_bh;
gDirectory->GetObject("GEN_transMin_bh",GEN_transMin_bh);
PrintProfile(GEN_transMin_bh,1,1,"text/MinBias_TuneMonash13_13TeV-pythia8/GEN/transMin_bh.txt");

TH1F *GEN_HIST_transPtSum;
gDirectory->GetObject("GEN_HIST_transPtSum",GEN_HIST_transPtSum);
PrintHistogram(GEN_HIST_transPtSum,1,1,"text/MinBias_TuneMonash13_13TeV-pythia8/GEN/HIST_transPtSum.txt");

TH1F *GEN_HIST_eta_pt5;
gDirectory->GetObject("GEN_HIST_eta_pt5",GEN_HIST_eta_pt5);
PrintHistogram(GEN_HIST_eta_pt5,1,1,"text/MinBias_TuneMonash13_13TeV-pythia8/GEN/HIST_eta_pt5.txt");

TH1F *GEN_HIST_delPhi_pt5;
gDirectory->GetObject("GEN_HIST_delPhi_pt5",GEN_HIST_delPhi_pt5);
PrintHistogram(GEN_HIST_delPhi_pt5,1,1,"text/MinBias_TuneMonash13_13TeV-pythia8/GEN/HIST_delPhi_pt5.txt");

TProfile *GEN_transDif_bh;
gDirectory->GetObject("GEN_transDif_bh",GEN_transDif_bh);
PrintProfile(GEN_transDif_bh,1,1,"text/MinBias_TuneMonash13_13TeV-pythia8/GEN/transDif_bh.txt");

TProfile *GEN_overallNch_b2;
gDirectory->GetObject("GEN_overallNch_b2",GEN_overallNch_b2);
PrintProfile(GEN_overallNch_b2,1,1,"text/MinBias_TuneMonash13_13TeV-pythia8/GEN/overallNch_b2.txt");

TProfile *GEN_overallNch_b1;
gDirectory->GetObject("GEN_overallNch_b1",GEN_overallNch_b1);
PrintProfile(GEN_overallNch_b1,1,1,"text/MinBias_TuneMonash13_13TeV-pythia8/GEN/overallNch_b1.txt");

TProfile *GEN_towardTotalNch_bh;
gDirectory->GetObject("GEN_towardTotalNch_bh",GEN_towardTotalNch_bh);
PrintProfile(GEN_towardTotalNch_bh,1,1,"text/MinBias_TuneMonash13_13TeV-pythia8/GEN/towardTotalNch_bh.txt");

TProfile *GEN_transAvg_b2;
gDirectory->GetObject("GEN_transAvg_b2",GEN_transAvg_b2);
PrintProfile(GEN_transAvg_b2,1,1,"text/MinBias_TuneMonash13_13TeV-pythia8/GEN/transAvg_b2.txt");

TProfile *GEN_overall_b2;
gDirectory->GetObject("GEN_overall_b2",GEN_overall_b2);
PrintProfile(GEN_overall_b2,1,1,"text/MinBias_TuneMonash13_13TeV-pythia8/GEN/overall_b2.txt");

TProfile *GEN_overall_b1;
gDirectory->GetObject("GEN_overall_b1",GEN_overall_b1);
PrintProfile(GEN_overall_b1,1,1,"text/MinBias_TuneMonash13_13TeV-pythia8/GEN/overall_b1.txt");

TProfile *GEN_transNch_b1;
gDirectory->GetObject("GEN_transNch_b1",GEN_transNch_b1);
PrintProfile(GEN_transNch_b1,1,1,"text/MinBias_TuneMonash13_13TeV-pythia8/GEN/transNch_b1.txt");

TProfile *GEN_transNch_b2;
gDirectory->GetObject("GEN_transNch_b2",GEN_transNch_b2);
PrintProfile(GEN_transNch_b2,1,1,"text/MinBias_TuneMonash13_13TeV-pythia8/GEN/transNch_b2.txt");

TProfile *GEN_transAvg_b1;
gDirectory->GetObject("GEN_transAvg_b1",GEN_transAvg_b1);
PrintProfile(GEN_transAvg_b1,1,1,"text/MinBias_TuneMonash13_13TeV-pythia8/GEN/transAvg_b1.txt");

TH1F *GEN_HIST_ptSum_pt5;
gDirectory->GetObject("GEN_HIST_ptSum_pt5",GEN_HIST_ptSum_pt5);
PrintHistogram(GEN_HIST_ptSum_pt5,1,1,"text/MinBias_TuneMonash13_13TeV-pythia8/GEN/HIST_ptSum_pt5.txt");

TH1F *GEN_HIST_transNch_pt5;
gDirectory->GetObject("GEN_HIST_transNch_pt5",GEN_HIST_transNch_pt5);
PrintHistogram(GEN_HIST_transNch_pt5,1,1,"text/MinBias_TuneMonash13_13TeV-pythia8/GEN/HIST_transNch_pt5.txt");

TProfile *GEN_towardTotal_bh;
gDirectory->GetObject("GEN_towardTotal_bh",GEN_towardTotal_bh);
PrintProfile(GEN_towardTotal_bh,1,1,"text/MinBias_TuneMonash13_13TeV-pythia8/GEN/towardTotal_bh.txt");

TH1F *GEN_HIST_nch;
gDirectory->GetObject("GEN_HIST_nch",GEN_HIST_nch);
PrintHistogram(GEN_HIST_nch,1,1,"text/MinBias_TuneMonash13_13TeV-pythia8/GEN/HIST_nch.txt");

TProfile *GEN_awayNch_b1;
gDirectory->GetObject("GEN_awayNch_b1",GEN_awayNch_b1);
PrintProfile(GEN_awayNch_b1,1,1,"text/MinBias_TuneMonash13_13TeV-pythia8/GEN/awayNch_b1.txt");

TProfile *GEN_awayNch_b2;
gDirectory->GetObject("GEN_awayNch_b2",GEN_awayNch_b2);
PrintProfile(GEN_awayNch_b2,1,1,"text/MinBias_TuneMonash13_13TeV-pythia8/GEN/awayNch_b2.txt");

TH1F *GEN_HIST_transPt_pt5;
gDirectory->GetObject("GEN_HIST_transPt_pt5",GEN_HIST_transPt_pt5);
PrintHistogram(GEN_HIST_transPt_pt5,1,1,"text/MinBias_TuneMonash13_13TeV-pythia8/GEN/HIST_transPt_pt5.txt");

TProfile *GEN_overallTotalAvg_b1;
gDirectory->GetObject("GEN_overallTotalAvg_b1",GEN_overallTotalAvg_b1);
PrintProfile(GEN_overallTotalAvg_b1,1,1,"text/MinBias_TuneMonash13_13TeV-pythia8/GEN/overallTotalAvg_b1.txt");

TProfile *GEN_overallTotalAvg_b2;
gDirectory->GetObject("GEN_overallTotalAvg_b2",GEN_overallTotalAvg_b2);
PrintProfile(GEN_overallTotalAvg_b2,1,1,"text/MinBias_TuneMonash13_13TeV-pythia8/GEN/overallTotalAvg_b2.txt");

TProfile *GEN_transDifNch_bh;
gDirectory->GetObject("GEN_transDifNch_bh",GEN_transDifNch_bh);
PrintProfile(GEN_transDifNch_bh,1,1,"text/MinBias_TuneMonash13_13TeV-pythia8/GEN/transDifNch_bh.txt");

TProfile *GEN_away_bh;
gDirectory->GetObject("GEN_away_bh",GEN_away_bh);
PrintProfile(GEN_away_bh,1,1,"text/MinBias_TuneMonash13_13TeV-pythia8/GEN/away_bh.txt");

TProfile *GEN_awayAvg_bh;
gDirectory->GetObject("GEN_awayAvg_bh",GEN_awayAvg_bh);
PrintProfile(GEN_awayAvg_bh,1,1,"text/MinBias_TuneMonash13_13TeV-pythia8/GEN/awayAvg_bh.txt");

TProfile *GEN_transAvg_bh;
gDirectory->GetObject("GEN_transAvg_bh",GEN_transAvg_bh);
PrintProfile(GEN_transAvg_bh,1,1,"text/MinBias_TuneMonash13_13TeV-pythia8/GEN/transAvg_bh.txt");

TProfile *GEN_awayAvg_b1;
gDirectory->GetObject("GEN_awayAvg_b1",GEN_awayAvg_b1);
PrintProfile(GEN_awayAvg_b1,1,1,"text/MinBias_TuneMonash13_13TeV-pythia8/GEN/awayAvg_b1.txt");

TProfile *GEN_away_b1;
gDirectory->GetObject("GEN_away_b1",GEN_away_b1);
PrintProfile(GEN_away_b1,1,1,"text/MinBias_TuneMonash13_13TeV-pythia8/GEN/away_b1.txt");

TProfile *GEN_away_b2;
gDirectory->GetObject("GEN_away_b2",GEN_away_b2);
PrintProfile(GEN_away_b2,1,1,"text/MinBias_TuneMonash13_13TeV-pythia8/GEN/away_b2.txt");

TProfile *GEN_awayAvg_b2;
gDirectory->GetObject("GEN_awayAvg_b2",GEN_awayAvg_b2);
PrintProfile(GEN_awayAvg_b2,1,1,"text/MinBias_TuneMonash13_13TeV-pythia8/GEN/awayAvg_b2.txt");

TH1F *GEN_HIST_transNch;
gDirectory->GetObject("GEN_HIST_transNch",GEN_HIST_transNch);
PrintHistogram(GEN_HIST_transNch,1,1,"text/MinBias_TuneMonash13_13TeV-pythia8/GEN/HIST_transNch.txt");

TProfile *GEN_overallTotalAvg_bh;
gDirectory->GetObject("GEN_overallTotalAvg_bh",GEN_overallTotalAvg_bh);
PrintProfile(GEN_overallTotalAvg_bh,1,1,"text/MinBias_TuneMonash13_13TeV-pythia8/GEN/overallTotalAvg_bh.txt");

TProfile *GEN_overallTotal_bh;
gDirectory->GetObject("GEN_overallTotal_bh",GEN_overallTotal_bh);
PrintProfile(GEN_overallTotal_bh,1,1,"text/MinBias_TuneMonash13_13TeV-pythia8/GEN/overallTotal_bh.txt");

TProfile *GEN_awayNch_bh;
gDirectory->GetObject("GEN_awayNch_bh",GEN_awayNch_bh);
PrintProfile(GEN_awayNch_bh,1,1,"text/MinBias_TuneMonash13_13TeV-pythia8/GEN/awayNch_bh.txt");

TProfile *GEN_towardTotal_b1;
gDirectory->GetObject("GEN_towardTotal_b1",GEN_towardTotal_b1);
PrintProfile(GEN_towardTotal_b1,1,1,"text/MinBias_TuneMonash13_13TeV-pythia8/GEN/towardTotal_b1.txt");

TProfile *GEN_towardTotal_b2;
gDirectory->GetObject("GEN_towardTotal_b2",GEN_towardTotal_b2);
PrintProfile(GEN_towardTotal_b2,1,1,"text/MinBias_TuneMonash13_13TeV-pythia8/GEN/towardTotal_b2.txt");


	fhist->cd("MinBias_TuneCUETP8M1_13TeV-pythia8");


TH1F *GEN_HIST_eta_ptH;
gDirectory->GetObject("GEN_HIST_eta_ptH",GEN_HIST_eta_ptH);
PrintHistogram(GEN_HIST_eta_ptH,1,1,"text/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN/GEN_HIST_eta_ptH.txt");

TH1F *GEN_HIST_phi_all;
gDirectory->GetObject("GEN_HIST_phi_all",GEN_HIST_phi_all);
PrintHistogram(GEN_HIST_phi_all,1,1,"text/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN/GEN_HIST_phi_all.txt");

TH1F *GEN_HIST_phi_eta;
gDirectory->GetObject("GEN_HIST_phi_eta",GEN_HIST_phi_eta);
PrintHistogram(GEN_HIST_phi_eta,1,1,"text/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN/GEN_HIST_phi_eta.txt");

TH1F *GEN_HIST_phi_etaptH;
gDirectory->GetObject("GEN_HIST_phi_etaptH",GEN_HIST_phi_etaptH);
PrintHistogram(GEN_HIST_phi_etaptH,1,1,"text/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN/GEN_HIST_phi_etaptH.txt");

TH1F *GEN_HIST_phi_ptH;
gDirectory->GetObject("GEN_HIST_phi_ptH",GEN_HIST_phi_ptH);
PrintHistogram(GEN_HIST_phi_ptH,1,1,"text/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN/GEN_HIST_phi_ptH.txt");

TProfile *GEN_towardTotalAvg_b1;
gDirectory->GetObject("GEN_towardTotalAvg_b1",GEN_towardTotalAvg_b1);
PrintProfile(GEN_towardTotalAvg_b1,1,1,"text/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN/towardTotalAvg_b1.txt");

TProfile *GEN_towardTotalAvg_b2;
gDirectory->GetObject("GEN_towardTotalAvg_b2",GEN_towardTotalAvg_b2);
PrintProfile(GEN_towardTotalAvg_b2,1,1,"text/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN/towardTotalAvg_b2.txt");

TProfile *GEN_transDifNch_b1;
gDirectory->GetObject("GEN_transDifNch_b1",GEN_transDifNch_b1);
PrintProfile(GEN_transDifNch_b1,1,1,"text/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN/transDifNch_b1.txt");

TH1F *GEN_HIST_nchMB;
gDirectory->GetObject("GEN_HIST_nchMB",GEN_HIST_nchMB);
PrintHistogram(GEN_HIST_nchMB,1,1,"text/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN/HIST_nchMB.txt");

TProfile *GEN_towardNch_b2;
gDirectory->GetObject("GEN_towardNch_b2",GEN_towardNch_b2);
PrintProfile(GEN_towardNch_b2,1,1,"text/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN/towardNch_b2.txt");

TH1F *GEN_HIST_ptSumMB;
gDirectory->GetObject("GEN_HIST_ptSumMB",GEN_HIST_ptSumMB);
PrintHistogram(GEN_HIST_ptSumMB,1,1,"text/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN/HIST_ptSumMB.txt");

TProfile *GEN_trans_b2;
gDirectory->GetObject("GEN_trans_b2",GEN_trans_b2);
PrintProfile(GEN_trans_b2,1,1,"text/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN/trans_b2.txt");

TProfile *GEN_trans_b1;
gDirectory->GetObject("GEN_trans_b1",GEN_trans_b1);
PrintProfile(GEN_trans_b1,1,1,"text/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN/trans_b1.txt");

TProfile *GEN_transMax_bh;
gDirectory->GetObject("GEN_transMax_bh",GEN_transMax_bh);
PrintProfile(GEN_transMax_bh,1,1,"text/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN/transMax_bh.txt");

TProfile *GEN_overallAvg_bh;
gDirectory->GetObject("GEN_overallAvg_bh",GEN_overallAvg_bh);
PrintProfile(GEN_overallAvg_bh,1,1,"text/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN/overallAvg_bh.txt");

TProfile *GEN_toward_b2;
gDirectory->GetObject("GEN_toward_b2",GEN_toward_b2);
PrintProfile(GEN_toward_b2,1,1,"text/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN/toward_b2.txt");

TProfile *GEN_toward_b1;
gDirectory->GetObject("GEN_toward_b1",GEN_toward_b1);
PrintProfile(GEN_toward_b1,1,1,"text/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN/toward_b1.txt");

TProfile *GEN_overallTotal_b2;
gDirectory->GetObject("GEN_overallTotal_b2",GEN_overallTotal_b2);
PrintProfile(GEN_overallTotal_b2,1,1,"text/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN/overallTotal_b2.txt");

TProfile *GEN_overallTotal_b1;
gDirectory->GetObject("GEN_overallTotal_b1",GEN_overallTotal_b1);
PrintProfile(GEN_overallTotal_b1,1,1,"text/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN/overallTotal_b1.txt");

TProfile *GEN_trans_bh;
gDirectory->GetObject("GEN_trans_bh",GEN_trans_bh);
PrintProfile(GEN_trans_bh,1,1,"text/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN/trans_bh.txt");

TProfile *GEN_towardNch_bh;
gDirectory->GetObject("GEN_towardNch_bh",GEN_towardNch_bh);
PrintProfile(GEN_towardNch_bh,1,1,"text/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN/towardNch_bh.txt");

TProfile *GEN_transMaxNch_b2;
gDirectory->GetObject("GEN_transMaxNch_b2",GEN_transMaxNch_b2);
PrintProfile(GEN_transMaxNch_b2,1,1,"text/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN/transMaxNch_b2.txt");

TH1F *GEN_HIST_etaMB;
gDirectory->GetObject("GEN_HIST_etaMB",GEN_HIST_etaMB);
PrintHistogram(GEN_HIST_etaMB,1,1,"text/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN/HIST_etaMB.txt");

TProfile *GEN_towardTotalAvg_bh;
gDirectory->GetObject("GEN_towardTotalAvg_bh",GEN_towardTotalAvg_bh);
PrintProfile(GEN_towardTotalAvg_bh,1,1,"text/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN/towardTotalAvg_bh.txt");

TProfile *GEN_towardNch_b1;
gDirectory->GetObject("GEN_towardNch_b1",GEN_towardNch_b1);
PrintProfile(GEN_towardNch_b1,1,1,"text/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN/towardNch_b1.txt");

TProfile *GEN_overallTotalNch_b2;
gDirectory->GetObject("GEN_overallTotalNch_b2",GEN_overallTotalNch_b2);
PrintProfile(GEN_overallTotalNch_b2,1,1,"text/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN/overallTotalNch_b2.txt");

TProfile *GEN_overallAvg_b2;
gDirectory->GetObject("GEN_overallAvg_b2",GEN_overallAvg_b2);
PrintProfile(GEN_overallAvg_b2,1,1,"text/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN/overallAvg_b2.txt");

TProfile *GEN_overallAvg_b1;
gDirectory->GetObject("GEN_overallAvg_b1",GEN_overallAvg_b1);
PrintProfile(GEN_overallAvg_b1,1,1,"text/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN/overallAvg_b1.txt");

TProfile *GEN_toward_bh;
gDirectory->GetObject("GEN_toward_bh",GEN_toward_bh);
PrintProfile(GEN_toward_bh,1,1,"text/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN/toward_bh.txt");

TProfile *GEN_transDifNch_b2;
gDirectory->GetObject("GEN_transDifNch_b2",GEN_transDifNch_b2);
PrintProfile(GEN_transDifNch_b2,1,1,"text/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN/transDifNch_b2.txt");

TProfile *GEN_transMax_b2;
gDirectory->GetObject("GEN_transMax_b2",GEN_transMax_b2);
PrintProfile(GEN_transMax_b2,1,1,"text/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN/transMax_b2.txt");

TProfile *GEN_transMax_b1;
gDirectory->GetObject("GEN_transMax_b1",GEN_transMax_b1);
PrintProfile(GEN_transMax_b1,1,1,"text/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN/transMax_b1.txt");

TH1F *GEN_HIST_pt_pt5;
gDirectory->GetObject("GEN_HIST_pt_pt5",GEN_HIST_pt_pt5);
PrintHistogram(GEN_HIST_pt_pt5,1,1,"text/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN/HIST_pt_pt5.txt");

TProfile *GEN_ptMax_bh;
gDirectory->GetObject("GEN_ptMax_bh",GEN_ptMax_bh);
PrintProfile(GEN_ptMax_bh,1,1,"text/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN/ptMax_bh.txt");

TProfile *GEN_transMinNch_bh;
gDirectory->GetObject("GEN_transMinNch_bh",GEN_transMinNch_bh);
PrintProfile(GEN_transMinNch_bh,1,1,"text/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN/transMinNch_bh.txt");

TH1F *GEN_HIST_delPhiPt_pt5;
gDirectory->GetObject("GEN_HIST_delPhiPt_pt5",GEN_HIST_delPhiPt_pt5);
PrintHistogram(GEN_HIST_delPhiPt_pt5,1,1,"text/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN/HIST_delPhiPt_pt5.txt");

TH1F *GEN_HIST_nch_pt5;
gDirectory->GetObject("GEN_HIST_nch_pt5",GEN_HIST_nch_pt5);
PrintHistogram(GEN_HIST_nch_pt5,1,1,"text/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN/HIST_nch_pt5.txt");

TProfile *GEN_overallTotalNch_b1;
gDirectory->GetObject("GEN_overallTotalNch_b1",GEN_overallTotalNch_b1);
PrintProfile(GEN_overallTotalNch_b1,1,1,"text/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN/overallTotalNch_b1.txt");

TH1F *GEN_HIST_ptSum;
gDirectory->GetObject("GEN_HIST_ptSum",GEN_HIST_ptSum);
PrintHistogram(GEN_HIST_ptSum,1,1,"text/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN/HIST_ptSum.txt");

TProfile *GEN_transMaxNch_b1;
gDirectory->GetObject("GEN_transMaxNch_b1",GEN_transMaxNch_b1);
PrintProfile(GEN_transMaxNch_b1,1,1,"text/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN/transMaxNch_b1.txt");

TProfile *GEN_towardAvg_bh;
gDirectory->GetObject("GEN_towardAvg_bh",GEN_towardAvg_bh);
PrintProfile(GEN_towardAvg_bh,1,1,"text/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN/towardAvg_bh.txt");

TH1F *GEN_HIST_ptMax;
gDirectory->GetObject("GEN_HIST_ptMax",GEN_HIST_ptMax);
PrintHistogram(GEN_HIST_ptMax,1,1,"text/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN/HIST_ptMax.txt");

TH1F *GEN_HIST_transPtSum_pt5;
gDirectory->GetObject("GEN_HIST_transPtSum_pt5",GEN_HIST_transPtSum_pt5);
PrintHistogram(GEN_HIST_transPtSum_pt5,1,1,"text/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN/HIST_transPtSum_pt5.txt");

TProfile *GEN_transMinNch_b1;
gDirectory->GetObject("GEN_transMinNch_b1",GEN_transMinNch_b1);
PrintProfile(GEN_transMinNch_b1,1,1,"text/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN/transMinNch_b1.txt");

TProfile *GEN_transMinNch_b2;
gDirectory->GetObject("GEN_transMinNch_b2",GEN_transMinNch_b2);
PrintProfile(GEN_transMinNch_b2,1,1,"text/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN/transMinNch_b2.txt");

TProfile *GEN_ptMax_b2;
gDirectory->GetObject("GEN_ptMax_b2",GEN_ptMax_b2);
PrintProfile(GEN_ptMax_b2,1,1,"text/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN/ptMax_b2.txt");

TProfile *GEN_ptMax_b1;
gDirectory->GetObject("GEN_ptMax_b1",GEN_ptMax_b1);
PrintProfile(GEN_ptMax_b1,1,1,"text/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN/ptMax_b1.txt");

TH1F *GEN_HIST_transPt;
gDirectory->GetObject("GEN_HIST_transPt",GEN_HIST_transPt);
PrintHistogram(GEN_HIST_transPt,1,1,"text/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN/HIST_transPt.txt");

TProfile *GEN_overallTotalNch_bh;
gDirectory->GetObject("GEN_overallTotalNch_bh",GEN_overallTotalNch_bh);
PrintProfile(GEN_overallTotalNch_bh,1,1,"text/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN/overallTotalNch_bh.txt");

TProfile *GEN_transMaxNch_bh;
gDirectory->GetObject("GEN_transMaxNch_bh",GEN_transMaxNch_bh);
PrintProfile(GEN_transMaxNch_bh,1,1,"text/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN/transMaxNch_bh.txt");

TProfile *GEN_towardAvg_b1;
gDirectory->GetObject("GEN_towardAvg_b1",GEN_towardAvg_b1);
PrintProfile(GEN_towardAvg_b1,1,1,"text/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN/towardAvg_b1.txt");

TProfile *GEN_towardAvg_b2;
gDirectory->GetObject("GEN_towardAvg_b2",GEN_towardAvg_b2);
PrintProfile(GEN_towardAvg_b2,1,1,"text/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN/towardAvg_b2.txt");

TH1F *GEN_HIST_delPhiPt;
gDirectory->GetObject("GEN_HIST_delPhiPt",GEN_HIST_delPhiPt);
PrintHistogram(GEN_HIST_delPhiPt,1,1,"text/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN/HIST_delPhiPt.txt");

TH1F *GEN_HIST_ptMB;
gDirectory->GetObject("GEN_HIST_ptMB",GEN_HIST_ptMB);
PrintHistogram(GEN_HIST_ptMB,1,1,"text/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN/HIST_ptMB.txt");

TProfile *GEN_transDif_b2;
gDirectory->GetObject("GEN_transDif_b2",GEN_transDif_b2);
PrintProfile(GEN_transDif_b2,1,1,"text/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN/transDif_b2.txt");

TProfile *GEN_transDif_b1;
gDirectory->GetObject("GEN_transDif_b1",GEN_transDif_b1);
PrintProfile(GEN_transDif_b1,1,1,"text/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN/transDif_b1.txt");

TProfile *GEN_transMin_b1;
gDirectory->GetObject("GEN_transMin_b1",GEN_transMin_b1);
PrintProfile(GEN_transMin_b1,1,1,"text/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN/transMin_b1.txt");

TProfile *GEN_transMin_b2;
gDirectory->GetObject("GEN_transMin_b2",GEN_transMin_b2);
PrintProfile(GEN_transMin_b2,1,1,"text/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN/transMin_b2.txt");

TH1F *GEN_HIST_delPhi;
gDirectory->GetObject("GEN_HIST_delPhi",GEN_HIST_delPhi);
PrintHistogram(GEN_HIST_delPhi,1,1,"text/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN/HIST_delPhi.txt");

TProfile *GEN_transNch_bh;
gDirectory->GetObject("GEN_transNch_bh",GEN_transNch_bh);
PrintProfile(GEN_transNch_bh,1,1,"text/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN/transNch_bh.txt");

TProfile *GEN_overall_bh;
gDirectory->GetObject("GEN_overall_bh",GEN_overall_bh);
PrintProfile(GEN_overall_bh,1,1,"text/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN/overall_bh.txt");

TProfile *GEN_towardTotalNch_b1;
gDirectory->GetObject("GEN_towardTotalNch_b1",GEN_towardTotalNch_b1);
PrintProfile(GEN_towardTotalNch_b1,1,1,"text/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN/towardTotalNch_b1.txt");

TProfile *GEN_towardTotalNch_b2;
gDirectory->GetObject("GEN_towardTotalNch_b2",GEN_towardTotalNch_b2);
PrintProfile(GEN_towardTotalNch_b2,1,1,"text/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN/towardTotalNch_b2.txt");

TProfile *GEN_overallNch_bh;
gDirectory->GetObject("GEN_overallNch_bh",GEN_overallNch_bh);
PrintProfile(GEN_overallNch_bh,1,1,"text/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN/overallNch_bh.txt");

TProfile *GEN_transMin_bh;
gDirectory->GetObject("GEN_transMin_bh",GEN_transMin_bh);
PrintProfile(GEN_transMin_bh,1,1,"text/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN/transMin_bh.txt");

TH1F *GEN_HIST_transPtSum;
gDirectory->GetObject("GEN_HIST_transPtSum",GEN_HIST_transPtSum);
PrintHistogram(GEN_HIST_transPtSum,1,1,"text/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN/HIST_transPtSum.txt");

TH1F *GEN_HIST_eta_pt5;
gDirectory->GetObject("GEN_HIST_eta_pt5",GEN_HIST_eta_pt5);
PrintHistogram(GEN_HIST_eta_pt5,1,1,"text/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN/HIST_eta_pt5.txt");

TH1F *GEN_HIST_delPhi_pt5;
gDirectory->GetObject("GEN_HIST_delPhi_pt5",GEN_HIST_delPhi_pt5);
PrintHistogram(GEN_HIST_delPhi_pt5,1,1,"text/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN/HIST_delPhi_pt5.txt");

TProfile *GEN_transDif_bh;
gDirectory->GetObject("GEN_transDif_bh",GEN_transDif_bh);
PrintProfile(GEN_transDif_bh,1,1,"text/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN/transDif_bh.txt");

TProfile *GEN_overallNch_b2;
gDirectory->GetObject("GEN_overallNch_b2",GEN_overallNch_b2);
PrintProfile(GEN_overallNch_b2,1,1,"text/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN/overallNch_b2.txt");

TProfile *GEN_overallNch_b1;
gDirectory->GetObject("GEN_overallNch_b1",GEN_overallNch_b1);
PrintProfile(GEN_overallNch_b1,1,1,"text/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN/overallNch_b1.txt");

TProfile *GEN_towardTotalNch_bh;
gDirectory->GetObject("GEN_towardTotalNch_bh",GEN_towardTotalNch_bh);
PrintProfile(GEN_towardTotalNch_bh,1,1,"text/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN/towardTotalNch_bh.txt");

TProfile *GEN_transAvg_b2;
gDirectory->GetObject("GEN_transAvg_b2",GEN_transAvg_b2);
PrintProfile(GEN_transAvg_b2,1,1,"text/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN/transAvg_b2.txt");

TProfile *GEN_overall_b2;
gDirectory->GetObject("GEN_overall_b2",GEN_overall_b2);
PrintProfile(GEN_overall_b2,1,1,"text/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN/overall_b2.txt");

TProfile *GEN_overall_b1;
gDirectory->GetObject("GEN_overall_b1",GEN_overall_b1);
PrintProfile(GEN_overall_b1,1,1,"text/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN/overall_b1.txt");

TProfile *GEN_transNch_b1;
gDirectory->GetObject("GEN_transNch_b1",GEN_transNch_b1);
PrintProfile(GEN_transNch_b1,1,1,"text/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN/transNch_b1.txt");

TProfile *GEN_transNch_b2;
gDirectory->GetObject("GEN_transNch_b2",GEN_transNch_b2);
PrintProfile(GEN_transNch_b2,1,1,"text/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN/transNch_b2.txt");

TProfile *GEN_transAvg_b1;
gDirectory->GetObject("GEN_transAvg_b1",GEN_transAvg_b1);
PrintProfile(GEN_transAvg_b1,1,1,"text/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN/transAvg_b1.txt");

TH1F *GEN_HIST_ptSum_pt5;
gDirectory->GetObject("GEN_HIST_ptSum_pt5",GEN_HIST_ptSum_pt5);
PrintHistogram(GEN_HIST_ptSum_pt5,1,1,"text/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN/HIST_ptSum_pt5.txt");

TH1F *GEN_HIST_transNch_pt5;
gDirectory->GetObject("GEN_HIST_transNch_pt5",GEN_HIST_transNch_pt5);
PrintHistogram(GEN_HIST_transNch_pt5,1,1,"text/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN/HIST_transNch_pt5.txt");

TProfile *GEN_towardTotal_bh;
gDirectory->GetObject("GEN_towardTotal_bh",GEN_towardTotal_bh);
PrintProfile(GEN_towardTotal_bh,1,1,"text/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN/towardTotal_bh.txt");

TH1F *GEN_HIST_nch;
gDirectory->GetObject("GEN_HIST_nch",GEN_HIST_nch);
PrintHistogram(GEN_HIST_nch,1,1,"text/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN/HIST_nch.txt");

TProfile *GEN_awayNch_b1;
gDirectory->GetObject("GEN_awayNch_b1",GEN_awayNch_b1);
PrintProfile(GEN_awayNch_b1,1,1,"text/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN/awayNch_b1.txt");

TProfile *GEN_awayNch_b2;
gDirectory->GetObject("GEN_awayNch_b2",GEN_awayNch_b2);
PrintProfile(GEN_awayNch_b2,1,1,"text/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN/awayNch_b2.txt");

TH1F *GEN_HIST_transPt_pt5;
gDirectory->GetObject("GEN_HIST_transPt_pt5",GEN_HIST_transPt_pt5);
PrintHistogram(GEN_HIST_transPt_pt5,1,1,"text/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN/HIST_transPt_pt5.txt");

TProfile *GEN_overallTotalAvg_b1;
gDirectory->GetObject("GEN_overallTotalAvg_b1",GEN_overallTotalAvg_b1);
PrintProfile(GEN_overallTotalAvg_b1,1,1,"text/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN/overallTotalAvg_b1.txt");

TProfile *GEN_overallTotalAvg_b2;
gDirectory->GetObject("GEN_overallTotalAvg_b2",GEN_overallTotalAvg_b2);
PrintProfile(GEN_overallTotalAvg_b2,1,1,"text/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN/overallTotalAvg_b2.txt");

TProfile *GEN_transDifNch_bh;
gDirectory->GetObject("GEN_transDifNch_bh",GEN_transDifNch_bh);
PrintProfile(GEN_transDifNch_bh,1,1,"text/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN/transDifNch_bh.txt");

TProfile *GEN_away_bh;
gDirectory->GetObject("GEN_away_bh",GEN_away_bh);
PrintProfile(GEN_away_bh,1,1,"text/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN/away_bh.txt");

TProfile *GEN_awayAvg_bh;
gDirectory->GetObject("GEN_awayAvg_bh",GEN_awayAvg_bh);
PrintProfile(GEN_awayAvg_bh,1,1,"text/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN/awayAvg_bh.txt");

TProfile *GEN_transAvg_bh;
gDirectory->GetObject("GEN_transAvg_bh",GEN_transAvg_bh);
PrintProfile(GEN_transAvg_bh,1,1,"text/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN/transAvg_bh.txt");

TProfile *GEN_awayAvg_b1;
gDirectory->GetObject("GEN_awayAvg_b1",GEN_awayAvg_b1);
PrintProfile(GEN_awayAvg_b1,1,1,"text/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN/awayAvg_b1.txt");

TProfile *GEN_away_b1;
gDirectory->GetObject("GEN_away_b1",GEN_away_b1);
PrintProfile(GEN_away_b1,1,1,"text/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN/away_b1.txt");

TProfile *GEN_away_b2;
gDirectory->GetObject("GEN_away_b2",GEN_away_b2);
PrintProfile(GEN_away_b2,1,1,"text/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN/away_b2.txt");

TProfile *GEN_awayAvg_b2;
gDirectory->GetObject("GEN_awayAvg_b2",GEN_awayAvg_b2);
PrintProfile(GEN_awayAvg_b2,1,1,"text/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN/awayAvg_b2.txt");

TH1F *GEN_HIST_transNch;
gDirectory->GetObject("GEN_HIST_transNch",GEN_HIST_transNch);
PrintHistogram(GEN_HIST_transNch,1,1,"text/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN/HIST_transNch.txt");

TProfile *GEN_overallTotalAvg_bh;
gDirectory->GetObject("GEN_overallTotalAvg_bh",GEN_overallTotalAvg_bh);
PrintProfile(GEN_overallTotalAvg_bh,1,1,"text/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN/overallTotalAvg_bh.txt");

TProfile *GEN_overallTotal_bh;
gDirectory->GetObject("GEN_overallTotal_bh",GEN_overallTotal_bh);
PrintProfile(GEN_overallTotal_bh,1,1,"text/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN/overallTotal_bh.txt");

TProfile *GEN_awayNch_bh;
gDirectory->GetObject("GEN_awayNch_bh",GEN_awayNch_bh);
PrintProfile(GEN_awayNch_bh,1,1,"text/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN/awayNch_bh.txt");

TProfile *GEN_towardTotal_b1;
gDirectory->GetObject("GEN_towardTotal_b1",GEN_towardTotal_b1);
PrintProfile(GEN_towardTotal_b1,1,1,"text/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN/towardTotal_b1.txt");

TProfile *GEN_towardTotal_b2;
gDirectory->GetObject("GEN_towardTotal_b2",GEN_towardTotal_b2);
PrintProfile(GEN_towardTotal_b2,1,1,"text/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN/towardTotal_b2.txt");




	fhist->cd("ReggeGribovPartonMC_13TeV-QGSJetII");

TH1F *GEN_HIST_eta_ptH;
gDirectory->GetObject("GEN_HIST_eta_ptH",GEN_HIST_eta_ptH);
PrintHistogram(GEN_HIST_eta_ptH,1,1,"text/ReggeGribovPartonMC_13TeV-QGSJetII/GEN/GEN_HIST_eta_ptH.txt");

TH1F *GEN_HIST_phi_all;
gDirectory->GetObject("GEN_HIST_phi_all",GEN_HIST_phi_all);
PrintHistogram(GEN_HIST_phi_all,1,1,"text/ReggeGribovPartonMC_13TeV-QGSJetII/GEN/GEN_HIST_phi_all.txt");

TH1F *GEN_HIST_phi_eta;
gDirectory->GetObject("GEN_HIST_phi_eta",GEN_HIST_phi_eta);
PrintHistogram(GEN_HIST_phi_eta,1,1,"text/ReggeGribovPartonMC_13TeV-QGSJetII/GEN/GEN_HIST_phi_eta.txt");

TH1F *GEN_HIST_phi_etaptH;
gDirectory->GetObject("GEN_HIST_phi_etaptH",GEN_HIST_phi_etaptH);
PrintHistogram(GEN_HIST_phi_etaptH,1,1,"text/ReggeGribovPartonMC_13TeV-QGSJetII/GEN/GEN_HIST_phi_etaptH.txt");

TH1F *GEN_HIST_phi_ptH;
gDirectory->GetObject("GEN_HIST_phi_ptH",GEN_HIST_phi_ptH);
PrintHistogram(GEN_HIST_phi_ptH,1,1,"text/ReggeGribovPartonMC_13TeV-QGSJetII/GEN/GEN_HIST_phi_ptH.txt");

TProfile *GEN_towardTotalAvg_b1;
gDirectory->GetObject("GEN_towardTotalAvg_b1",GEN_towardTotalAvg_b1);
PrintProfile(GEN_towardTotalAvg_b1,1,1,"text/ReggeGribovPartonMC_13TeV-QGSJetII/GEN/towardTotalAvg_b1.txt");

TProfile *GEN_towardTotalAvg_b2;
gDirectory->GetObject("GEN_towardTotalAvg_b2",GEN_towardTotalAvg_b2);
PrintProfile(GEN_towardTotalAvg_b2,1,1,"text/ReggeGribovPartonMC_13TeV-QGSJetII/GEN/towardTotalAvg_b2.txt");

TProfile *GEN_transDifNch_b1;
gDirectory->GetObject("GEN_transDifNch_b1",GEN_transDifNch_b1);
PrintProfile(GEN_transDifNch_b1,1,1,"text/ReggeGribovPartonMC_13TeV-QGSJetII/GEN/transDifNch_b1.txt");

TH1F *GEN_HIST_nchMB;
gDirectory->GetObject("GEN_HIST_nchMB",GEN_HIST_nchMB);
PrintHistogram(GEN_HIST_nchMB,1,1,"text/ReggeGribovPartonMC_13TeV-QGSJetII/GEN/HIST_nchMB.txt");

TProfile *GEN_towardNch_b2;
gDirectory->GetObject("GEN_towardNch_b2",GEN_towardNch_b2);
PrintProfile(GEN_towardNch_b2,1,1,"text/ReggeGribovPartonMC_13TeV-QGSJetII/GEN/towardNch_b2.txt");

TH1F *GEN_HIST_ptSumMB;
gDirectory->GetObject("GEN_HIST_ptSumMB",GEN_HIST_ptSumMB);
PrintHistogram(GEN_HIST_ptSumMB,1,1,"text/ReggeGribovPartonMC_13TeV-QGSJetII/GEN/HIST_ptSumMB.txt");

TProfile *GEN_trans_b2;
gDirectory->GetObject("GEN_trans_b2",GEN_trans_b2);
PrintProfile(GEN_trans_b2,1,1,"text/ReggeGribovPartonMC_13TeV-QGSJetII/GEN/trans_b2.txt");

TProfile *GEN_trans_b1;
gDirectory->GetObject("GEN_trans_b1",GEN_trans_b1);
PrintProfile(GEN_trans_b1,1,1,"text/ReggeGribovPartonMC_13TeV-QGSJetII/GEN/trans_b1.txt");

TProfile *GEN_transMax_bh;
gDirectory->GetObject("GEN_transMax_bh",GEN_transMax_bh);
PrintProfile(GEN_transMax_bh,1,1,"text/ReggeGribovPartonMC_13TeV-QGSJetII/GEN/transMax_bh.txt");

TProfile *GEN_overallAvg_bh;
gDirectory->GetObject("GEN_overallAvg_bh",GEN_overallAvg_bh);
PrintProfile(GEN_overallAvg_bh,1,1,"text/ReggeGribovPartonMC_13TeV-QGSJetII/GEN/overallAvg_bh.txt");

TProfile *GEN_toward_b2;
gDirectory->GetObject("GEN_toward_b2",GEN_toward_b2);
PrintProfile(GEN_toward_b2,1,1,"text/ReggeGribovPartonMC_13TeV-QGSJetII/GEN/toward_b2.txt");

TProfile *GEN_toward_b1;
gDirectory->GetObject("GEN_toward_b1",GEN_toward_b1);
PrintProfile(GEN_toward_b1,1,1,"text/ReggeGribovPartonMC_13TeV-QGSJetII/GEN/toward_b1.txt");

TProfile *GEN_overallTotal_b2;
gDirectory->GetObject("GEN_overallTotal_b2",GEN_overallTotal_b2);
PrintProfile(GEN_overallTotal_b2,1,1,"text/ReggeGribovPartonMC_13TeV-QGSJetII/GEN/overallTotal_b2.txt");

TProfile *GEN_overallTotal_b1;
gDirectory->GetObject("GEN_overallTotal_b1",GEN_overallTotal_b1);
PrintProfile(GEN_overallTotal_b1,1,1,"text/ReggeGribovPartonMC_13TeV-QGSJetII/GEN/overallTotal_b1.txt");

TProfile *GEN_trans_bh;
gDirectory->GetObject("GEN_trans_bh",GEN_trans_bh);
PrintProfile(GEN_trans_bh,1,1,"text/ReggeGribovPartonMC_13TeV-QGSJetII/GEN/trans_bh.txt");

TProfile *GEN_towardNch_bh;
gDirectory->GetObject("GEN_towardNch_bh",GEN_towardNch_bh);
PrintProfile(GEN_towardNch_bh,1,1,"text/ReggeGribovPartonMC_13TeV-QGSJetII/GEN/towardNch_bh.txt");

TProfile *GEN_transMaxNch_b2;
gDirectory->GetObject("GEN_transMaxNch_b2",GEN_transMaxNch_b2);
PrintProfile(GEN_transMaxNch_b2,1,1,"text/ReggeGribovPartonMC_13TeV-QGSJetII/GEN/transMaxNch_b2.txt");

TH1F *GEN_HIST_etaMB;
gDirectory->GetObject("GEN_HIST_etaMB",GEN_HIST_etaMB);
PrintHistogram(GEN_HIST_etaMB,1,1,"text/ReggeGribovPartonMC_13TeV-QGSJetII/GEN/HIST_etaMB.txt");

TProfile *GEN_towardTotalAvg_bh;
gDirectory->GetObject("GEN_towardTotalAvg_bh",GEN_towardTotalAvg_bh);
PrintProfile(GEN_towardTotalAvg_bh,1,1,"text/ReggeGribovPartonMC_13TeV-QGSJetII/GEN/towardTotalAvg_bh.txt");

TProfile *GEN_towardNch_b1;
gDirectory->GetObject("GEN_towardNch_b1",GEN_towardNch_b1);
PrintProfile(GEN_towardNch_b1,1,1,"text/ReggeGribovPartonMC_13TeV-QGSJetII/GEN/towardNch_b1.txt");

TProfile *GEN_overallTotalNch_b2;
gDirectory->GetObject("GEN_overallTotalNch_b2",GEN_overallTotalNch_b2);
PrintProfile(GEN_overallTotalNch_b2,1,1,"text/ReggeGribovPartonMC_13TeV-QGSJetII/GEN/overallTotalNch_b2.txt");

TProfile *GEN_overallAvg_b2;
gDirectory->GetObject("GEN_overallAvg_b2",GEN_overallAvg_b2);
PrintProfile(GEN_overallAvg_b2,1,1,"text/ReggeGribovPartonMC_13TeV-QGSJetII/GEN/overallAvg_b2.txt");

TProfile *GEN_overallAvg_b1;
gDirectory->GetObject("GEN_overallAvg_b1",GEN_overallAvg_b1);
PrintProfile(GEN_overallAvg_b1,1,1,"text/ReggeGribovPartonMC_13TeV-QGSJetII/GEN/overallAvg_b1.txt");

TProfile *GEN_toward_bh;
gDirectory->GetObject("GEN_toward_bh",GEN_toward_bh);
PrintProfile(GEN_toward_bh,1,1,"text/ReggeGribovPartonMC_13TeV-QGSJetII/GEN/toward_bh.txt");

TProfile *GEN_transDifNch_b2;
gDirectory->GetObject("GEN_transDifNch_b2",GEN_transDifNch_b2);
PrintProfile(GEN_transDifNch_b2,1,1,"text/ReggeGribovPartonMC_13TeV-QGSJetII/GEN/transDifNch_b2.txt");

TProfile *GEN_transMax_b2;
gDirectory->GetObject("GEN_transMax_b2",GEN_transMax_b2);
PrintProfile(GEN_transMax_b2,1,1,"text/ReggeGribovPartonMC_13TeV-QGSJetII/GEN/transMax_b2.txt");

TProfile *GEN_transMax_b1;
gDirectory->GetObject("GEN_transMax_b1",GEN_transMax_b1);
PrintProfile(GEN_transMax_b1,1,1,"text/ReggeGribovPartonMC_13TeV-QGSJetII/GEN/transMax_b1.txt");

TH1F *GEN_HIST_pt_pt5;
gDirectory->GetObject("GEN_HIST_pt_pt5",GEN_HIST_pt_pt5);
PrintHistogram(GEN_HIST_pt_pt5,1,1,"text/ReggeGribovPartonMC_13TeV-QGSJetII/GEN/HIST_pt_pt5.txt");

TProfile *GEN_ptMax_bh;
gDirectory->GetObject("GEN_ptMax_bh",GEN_ptMax_bh);
PrintProfile(GEN_ptMax_bh,1,1,"text/ReggeGribovPartonMC_13TeV-QGSJetII/GEN/ptMax_bh.txt");

TProfile *GEN_transMinNch_bh;
gDirectory->GetObject("GEN_transMinNch_bh",GEN_transMinNch_bh);
PrintProfile(GEN_transMinNch_bh,1,1,"text/ReggeGribovPartonMC_13TeV-QGSJetII/GEN/transMinNch_bh.txt");

TH1F *GEN_HIST_delPhiPt_pt5;
gDirectory->GetObject("GEN_HIST_delPhiPt_pt5",GEN_HIST_delPhiPt_pt5);
PrintHistogram(GEN_HIST_delPhiPt_pt5,1,1,"text/ReggeGribovPartonMC_13TeV-QGSJetII/GEN/HIST_delPhiPt_pt5.txt");

TH1F *GEN_HIST_nch_pt5;
gDirectory->GetObject("GEN_HIST_nch_pt5",GEN_HIST_nch_pt5);
PrintHistogram(GEN_HIST_nch_pt5,1,1,"text/ReggeGribovPartonMC_13TeV-QGSJetII/GEN/HIST_nch_pt5.txt");

TProfile *GEN_overallTotalNch_b1;
gDirectory->GetObject("GEN_overallTotalNch_b1",GEN_overallTotalNch_b1);
PrintProfile(GEN_overallTotalNch_b1,1,1,"text/ReggeGribovPartonMC_13TeV-QGSJetII/GEN/overallTotalNch_b1.txt");

TH1F *GEN_HIST_ptSum;
gDirectory->GetObject("GEN_HIST_ptSum",GEN_HIST_ptSum);
PrintHistogram(GEN_HIST_ptSum,1,1,"text/ReggeGribovPartonMC_13TeV-QGSJetII/GEN/HIST_ptSum.txt");

TProfile *GEN_transMaxNch_b1;
gDirectory->GetObject("GEN_transMaxNch_b1",GEN_transMaxNch_b1);
PrintProfile(GEN_transMaxNch_b1,1,1,"text/ReggeGribovPartonMC_13TeV-QGSJetII/GEN/transMaxNch_b1.txt");

TProfile *GEN_towardAvg_bh;
gDirectory->GetObject("GEN_towardAvg_bh",GEN_towardAvg_bh);
PrintProfile(GEN_towardAvg_bh,1,1,"text/ReggeGribovPartonMC_13TeV-QGSJetII/GEN/towardAvg_bh.txt");

TH1F *GEN_HIST_ptMax;
gDirectory->GetObject("GEN_HIST_ptMax",GEN_HIST_ptMax);
PrintHistogram(GEN_HIST_ptMax,1,1,"text/ReggeGribovPartonMC_13TeV-QGSJetII/GEN/HIST_ptMax.txt");

TH1F *GEN_HIST_transPtSum_pt5;
gDirectory->GetObject("GEN_HIST_transPtSum_pt5",GEN_HIST_transPtSum_pt5);
PrintHistogram(GEN_HIST_transPtSum_pt5,1,1,"text/ReggeGribovPartonMC_13TeV-QGSJetII/GEN/HIST_transPtSum_pt5.txt");

TProfile *GEN_transMinNch_b1;
gDirectory->GetObject("GEN_transMinNch_b1",GEN_transMinNch_b1);
PrintProfile(GEN_transMinNch_b1,1,1,"text/ReggeGribovPartonMC_13TeV-QGSJetII/GEN/transMinNch_b1.txt");

TProfile *GEN_transMinNch_b2;
gDirectory->GetObject("GEN_transMinNch_b2",GEN_transMinNch_b2);
PrintProfile(GEN_transMinNch_b2,1,1,"text/ReggeGribovPartonMC_13TeV-QGSJetII/GEN/transMinNch_b2.txt");

TProfile *GEN_ptMax_b2;
gDirectory->GetObject("GEN_ptMax_b2",GEN_ptMax_b2);
PrintProfile(GEN_ptMax_b2,1,1,"text/ReggeGribovPartonMC_13TeV-QGSJetII/GEN/ptMax_b2.txt");

TProfile *GEN_ptMax_b1;
gDirectory->GetObject("GEN_ptMax_b1",GEN_ptMax_b1);
PrintProfile(GEN_ptMax_b1,1,1,"text/ReggeGribovPartonMC_13TeV-QGSJetII/GEN/ptMax_b1.txt");

TH1F *GEN_HIST_transPt;
gDirectory->GetObject("GEN_HIST_transPt",GEN_HIST_transPt);
PrintHistogram(GEN_HIST_transPt,1,1,"text/ReggeGribovPartonMC_13TeV-QGSJetII/GEN/HIST_transPt.txt");

TProfile *GEN_overallTotalNch_bh;
gDirectory->GetObject("GEN_overallTotalNch_bh",GEN_overallTotalNch_bh);
PrintProfile(GEN_overallTotalNch_bh,1,1,"text/ReggeGribovPartonMC_13TeV-QGSJetII/GEN/overallTotalNch_bh.txt");

TProfile *GEN_transMaxNch_bh;
gDirectory->GetObject("GEN_transMaxNch_bh",GEN_transMaxNch_bh);
PrintProfile(GEN_transMaxNch_bh,1,1,"text/ReggeGribovPartonMC_13TeV-QGSJetII/GEN/transMaxNch_bh.txt");

TProfile *GEN_towardAvg_b1;
gDirectory->GetObject("GEN_towardAvg_b1",GEN_towardAvg_b1);
PrintProfile(GEN_towardAvg_b1,1,1,"text/ReggeGribovPartonMC_13TeV-QGSJetII/GEN/towardAvg_b1.txt");

TProfile *GEN_towardAvg_b2;
gDirectory->GetObject("GEN_towardAvg_b2",GEN_towardAvg_b2);
PrintProfile(GEN_towardAvg_b2,1,1,"text/ReggeGribovPartonMC_13TeV-QGSJetII/GEN/towardAvg_b2.txt");

TH1F *GEN_HIST_delPhiPt;
gDirectory->GetObject("GEN_HIST_delPhiPt",GEN_HIST_delPhiPt);
PrintHistogram(GEN_HIST_delPhiPt,1,1,"text/ReggeGribovPartonMC_13TeV-QGSJetII/GEN/HIST_delPhiPt.txt");

TH1F *GEN_HIST_ptMB;
gDirectory->GetObject("GEN_HIST_ptMB",GEN_HIST_ptMB);
PrintHistogram(GEN_HIST_ptMB,1,1,"text/ReggeGribovPartonMC_13TeV-QGSJetII/GEN/HIST_ptMB.txt");

TProfile *GEN_transDif_b2;
gDirectory->GetObject("GEN_transDif_b2",GEN_transDif_b2);
PrintProfile(GEN_transDif_b2,1,1,"text/ReggeGribovPartonMC_13TeV-QGSJetII/GEN/transDif_b2.txt");

TProfile *GEN_transDif_b1;
gDirectory->GetObject("GEN_transDif_b1",GEN_transDif_b1);
PrintProfile(GEN_transDif_b1,1,1,"text/ReggeGribovPartonMC_13TeV-QGSJetII/GEN/transDif_b1.txt");

TProfile *GEN_transMin_b1;
gDirectory->GetObject("GEN_transMin_b1",GEN_transMin_b1);
PrintProfile(GEN_transMin_b1,1,1,"text/ReggeGribovPartonMC_13TeV-QGSJetII/GEN/transMin_b1.txt");

TProfile *GEN_transMin_b2;
gDirectory->GetObject("GEN_transMin_b2",GEN_transMin_b2);
PrintProfile(GEN_transMin_b2,1,1,"text/ReggeGribovPartonMC_13TeV-QGSJetII/GEN/transMin_b2.txt");

TH1F *GEN_HIST_delPhi;
gDirectory->GetObject("GEN_HIST_delPhi",GEN_HIST_delPhi);
PrintHistogram(GEN_HIST_delPhi,1,1,"text/ReggeGribovPartonMC_13TeV-QGSJetII/GEN/HIST_delPhi.txt");

TProfile *GEN_transNch_bh;
gDirectory->GetObject("GEN_transNch_bh",GEN_transNch_bh);
PrintProfile(GEN_transNch_bh,1,1,"text/ReggeGribovPartonMC_13TeV-QGSJetII/GEN/transNch_bh.txt");

TProfile *GEN_overall_bh;
gDirectory->GetObject("GEN_overall_bh",GEN_overall_bh);
PrintProfile(GEN_overall_bh,1,1,"text/ReggeGribovPartonMC_13TeV-QGSJetII/GEN/overall_bh.txt");

TProfile *GEN_towardTotalNch_b1;
gDirectory->GetObject("GEN_towardTotalNch_b1",GEN_towardTotalNch_b1);
PrintProfile(GEN_towardTotalNch_b1,1,1,"text/ReggeGribovPartonMC_13TeV-QGSJetII/GEN/towardTotalNch_b1.txt");

TProfile *GEN_towardTotalNch_b2;
gDirectory->GetObject("GEN_towardTotalNch_b2",GEN_towardTotalNch_b2);
PrintProfile(GEN_towardTotalNch_b2,1,1,"text/ReggeGribovPartonMC_13TeV-QGSJetII/GEN/towardTotalNch_b2.txt");

TProfile *GEN_overallNch_bh;
gDirectory->GetObject("GEN_overallNch_bh",GEN_overallNch_bh);
PrintProfile(GEN_overallNch_bh,1,1,"text/ReggeGribovPartonMC_13TeV-QGSJetII/GEN/overallNch_bh.txt");

TProfile *GEN_transMin_bh;
gDirectory->GetObject("GEN_transMin_bh",GEN_transMin_bh);
PrintProfile(GEN_transMin_bh,1,1,"text/ReggeGribovPartonMC_13TeV-QGSJetII/GEN/transMin_bh.txt");

TH1F *GEN_HIST_transPtSum;
gDirectory->GetObject("GEN_HIST_transPtSum",GEN_HIST_transPtSum);
PrintHistogram(GEN_HIST_transPtSum,1,1,"text/ReggeGribovPartonMC_13TeV-QGSJetII/GEN/HIST_transPtSum.txt");

TH1F *GEN_HIST_eta_pt5;
gDirectory->GetObject("GEN_HIST_eta_pt5",GEN_HIST_eta_pt5);
PrintHistogram(GEN_HIST_eta_pt5,1,1,"text/ReggeGribovPartonMC_13TeV-QGSJetII/GEN/HIST_eta_pt5.txt");

TH1F *GEN_HIST_delPhi_pt5;
gDirectory->GetObject("GEN_HIST_delPhi_pt5",GEN_HIST_delPhi_pt5);
PrintHistogram(GEN_HIST_delPhi_pt5,1,1,"text/ReggeGribovPartonMC_13TeV-QGSJetII/GEN/HIST_delPhi_pt5.txt");

TProfile *GEN_transDif_bh;
gDirectory->GetObject("GEN_transDif_bh",GEN_transDif_bh);
PrintProfile(GEN_transDif_bh,1,1,"text/ReggeGribovPartonMC_13TeV-QGSJetII/GEN/transDif_bh.txt");

TProfile *GEN_overallNch_b2;
gDirectory->GetObject("GEN_overallNch_b2",GEN_overallNch_b2);
PrintProfile(GEN_overallNch_b2,1,1,"text/ReggeGribovPartonMC_13TeV-QGSJetII/GEN/overallNch_b2.txt");

TProfile *GEN_overallNch_b1;
gDirectory->GetObject("GEN_overallNch_b1",GEN_overallNch_b1);
PrintProfile(GEN_overallNch_b1,1,1,"text/ReggeGribovPartonMC_13TeV-QGSJetII/GEN/overallNch_b1.txt");

TProfile *GEN_towardTotalNch_bh;
gDirectory->GetObject("GEN_towardTotalNch_bh",GEN_towardTotalNch_bh);
PrintProfile(GEN_towardTotalNch_bh,1,1,"text/ReggeGribovPartonMC_13TeV-QGSJetII/GEN/towardTotalNch_bh.txt");

TProfile *GEN_transAvg_b2;
gDirectory->GetObject("GEN_transAvg_b2",GEN_transAvg_b2);
PrintProfile(GEN_transAvg_b2,1,1,"text/ReggeGribovPartonMC_13TeV-QGSJetII/GEN/transAvg_b2.txt");

TProfile *GEN_overall_b2;
gDirectory->GetObject("GEN_overall_b2",GEN_overall_b2);
PrintProfile(GEN_overall_b2,1,1,"text/ReggeGribovPartonMC_13TeV-QGSJetII/GEN/overall_b2.txt");

TProfile *GEN_overall_b1;
gDirectory->GetObject("GEN_overall_b1",GEN_overall_b1);
PrintProfile(GEN_overall_b1,1,1,"text/ReggeGribovPartonMC_13TeV-QGSJetII/GEN/overall_b1.txt");

TProfile *GEN_transNch_b1;
gDirectory->GetObject("GEN_transNch_b1",GEN_transNch_b1);
PrintProfile(GEN_transNch_b1,1,1,"text/ReggeGribovPartonMC_13TeV-QGSJetII/GEN/transNch_b1.txt");

TProfile *GEN_transNch_b2;
gDirectory->GetObject("GEN_transNch_b2",GEN_transNch_b2);
PrintProfile(GEN_transNch_b2,1,1,"text/ReggeGribovPartonMC_13TeV-QGSJetII/GEN/transNch_b2.txt");

TProfile *GEN_transAvg_b1;
gDirectory->GetObject("GEN_transAvg_b1",GEN_transAvg_b1);
PrintProfile(GEN_transAvg_b1,1,1,"text/ReggeGribovPartonMC_13TeV-QGSJetII/GEN/transAvg_b1.txt");

TH1F *GEN_HIST_ptSum_pt5;
gDirectory->GetObject("GEN_HIST_ptSum_pt5",GEN_HIST_ptSum_pt5);
PrintHistogram(GEN_HIST_ptSum_pt5,1,1,"text/ReggeGribovPartonMC_13TeV-QGSJetII/GEN/HIST_ptSum_pt5.txt");

TH1F *GEN_HIST_transNch_pt5;
gDirectory->GetObject("GEN_HIST_transNch_pt5",GEN_HIST_transNch_pt5);
PrintHistogram(GEN_HIST_transNch_pt5,1,1,"text/ReggeGribovPartonMC_13TeV-QGSJetII/GEN/HIST_transNch_pt5.txt");

TProfile *GEN_towardTotal_bh;
gDirectory->GetObject("GEN_towardTotal_bh",GEN_towardTotal_bh);
PrintProfile(GEN_towardTotal_bh,1,1,"text/ReggeGribovPartonMC_13TeV-QGSJetII/GEN/towardTotal_bh.txt");

TH1F *GEN_HIST_nch;
gDirectory->GetObject("GEN_HIST_nch",GEN_HIST_nch);
PrintHistogram(GEN_HIST_nch,1,1,"text/ReggeGribovPartonMC_13TeV-QGSJetII/GEN/HIST_nch.txt");

TProfile *GEN_awayNch_b1;
gDirectory->GetObject("GEN_awayNch_b1",GEN_awayNch_b1);
PrintProfile(GEN_awayNch_b1,1,1,"text/ReggeGribovPartonMC_13TeV-QGSJetII/GEN/awayNch_b1.txt");

TProfile *GEN_awayNch_b2;
gDirectory->GetObject("GEN_awayNch_b2",GEN_awayNch_b2);
PrintProfile(GEN_awayNch_b2,1,1,"text/ReggeGribovPartonMC_13TeV-QGSJetII/GEN/awayNch_b2.txt");

TH1F *GEN_HIST_transPt_pt5;
gDirectory->GetObject("GEN_HIST_transPt_pt5",GEN_HIST_transPt_pt5);
PrintHistogram(GEN_HIST_transPt_pt5,1,1,"text/ReggeGribovPartonMC_13TeV-QGSJetII/GEN/HIST_transPt_pt5.txt");

TProfile *GEN_overallTotalAvg_b1;
gDirectory->GetObject("GEN_overallTotalAvg_b1",GEN_overallTotalAvg_b1);
PrintProfile(GEN_overallTotalAvg_b1,1,1,"text/ReggeGribovPartonMC_13TeV-QGSJetII/GEN/overallTotalAvg_b1.txt");

TProfile *GEN_overallTotalAvg_b2;
gDirectory->GetObject("GEN_overallTotalAvg_b2",GEN_overallTotalAvg_b2);
PrintProfile(GEN_overallTotalAvg_b2,1,1,"text/ReggeGribovPartonMC_13TeV-QGSJetII/GEN/overallTotalAvg_b2.txt");

TProfile *GEN_transDifNch_bh;
gDirectory->GetObject("GEN_transDifNch_bh",GEN_transDifNch_bh);
PrintProfile(GEN_transDifNch_bh,1,1,"text/ReggeGribovPartonMC_13TeV-QGSJetII/GEN/transDifNch_bh.txt");

TProfile *GEN_away_bh;
gDirectory->GetObject("GEN_away_bh",GEN_away_bh);
PrintProfile(GEN_away_bh,1,1,"text/ReggeGribovPartonMC_13TeV-QGSJetII/GEN/away_bh.txt");

TProfile *GEN_awayAvg_bh;
gDirectory->GetObject("GEN_awayAvg_bh",GEN_awayAvg_bh);
PrintProfile(GEN_awayAvg_bh,1,1,"text/ReggeGribovPartonMC_13TeV-QGSJetII/GEN/awayAvg_bh.txt");

TProfile *GEN_transAvg_bh;
gDirectory->GetObject("GEN_transAvg_bh",GEN_transAvg_bh);
PrintProfile(GEN_transAvg_bh,1,1,"text/ReggeGribovPartonMC_13TeV-QGSJetII/GEN/transAvg_bh.txt");

TProfile *GEN_awayAvg_b1;
gDirectory->GetObject("GEN_awayAvg_b1",GEN_awayAvg_b1);
PrintProfile(GEN_awayAvg_b1,1,1,"text/ReggeGribovPartonMC_13TeV-QGSJetII/GEN/awayAvg_b1.txt");

TProfile *GEN_away_b1;
gDirectory->GetObject("GEN_away_b1",GEN_away_b1);
PrintProfile(GEN_away_b1,1,1,"text/ReggeGribovPartonMC_13TeV-QGSJetII/GEN/away_b1.txt");

TProfile *GEN_away_b2;
gDirectory->GetObject("GEN_away_b2",GEN_away_b2);
PrintProfile(GEN_away_b2,1,1,"text/ReggeGribovPartonMC_13TeV-QGSJetII/GEN/away_b2.txt");

TProfile *GEN_awayAvg_b2;
gDirectory->GetObject("GEN_awayAvg_b2",GEN_awayAvg_b2);
PrintProfile(GEN_awayAvg_b2,1,1,"text/ReggeGribovPartonMC_13TeV-QGSJetII/GEN/awayAvg_b2.txt");

TH1F *GEN_HIST_transNch;
gDirectory->GetObject("GEN_HIST_transNch",GEN_HIST_transNch);
PrintHistogram(GEN_HIST_transNch,1,1,"text/ReggeGribovPartonMC_13TeV-QGSJetII/GEN/HIST_transNch.txt");

TProfile *GEN_overallTotalAvg_bh;
gDirectory->GetObject("GEN_overallTotalAvg_bh",GEN_overallTotalAvg_bh);
PrintProfile(GEN_overallTotalAvg_bh,1,1,"text/ReggeGribovPartonMC_13TeV-QGSJetII/GEN/overallTotalAvg_bh.txt");

TProfile *GEN_overallTotal_bh;
gDirectory->GetObject("GEN_overallTotal_bh",GEN_overallTotal_bh);
PrintProfile(GEN_overallTotal_bh,1,1,"text/ReggeGribovPartonMC_13TeV-QGSJetII/GEN/overallTotal_bh.txt");

TProfile *GEN_awayNch_bh;
gDirectory->GetObject("GEN_awayNch_bh",GEN_awayNch_bh);
PrintProfile(GEN_awayNch_bh,1,1,"text/ReggeGribovPartonMC_13TeV-QGSJetII/GEN/awayNch_bh.txt");

TProfile *GEN_towardTotal_b1;
gDirectory->GetObject("GEN_towardTotal_b1",GEN_towardTotal_b1);
PrintProfile(GEN_towardTotal_b1,1,1,"text/ReggeGribovPartonMC_13TeV-QGSJetII/GEN/towardTotal_b1.txt");

TProfile *GEN_towardTotal_b2;
gDirectory->GetObject("GEN_towardTotal_b2",GEN_towardTotal_b2);
PrintProfile(GEN_towardTotal_b2,1,1,"text/ReggeGribovPartonMC_13TeV-QGSJetII/GEN/towardTotal_b2.txt");





	cout << "Out file written" << endl;

	//	f->Close();
	}




















