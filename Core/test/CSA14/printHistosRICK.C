



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



	void printHistosRICK ()
	{
	char* rootFile = "plotsGENTUNES.root";
	//char* curvesCSVfile = "Tune_CUETP8M1_PTmax_Eta20.csv";
	char* curvesCSVfile = "Tune_Monash_PTmax_Eta20.csv";
	cout << "Loading ROOT file    " << rootFile << endl;
	cout << "Loading CSV file     " << curvesCSVfile << endl;
	TFile *fhist = new TFile(rootFile);
	//fhist->cd("MinBias_TuneCUETP8M1_13TeV-pythia8");
	fhist->cd("MinBias_TuneMonash13_13TeV-pythia8");

	double etaCut = 2.0;
	double scaleTotal = 1/(2*3.14159*2*etaCut); 
	double scaleThird  = 3/(2*3.14159*2*etaCut);
	double scaleSixth = 6/(2*3.14159*2*etaCut);

	TCanvas *c1 = new TCanvas("c1","c1",600,400);

// Specify option as follows (for comma delimited):
// "%lg,%lg" chooses "x,y1" from say "x,y1,y2,y3,y4..."
// Add a %*lg for each column to skip.  So "%lg,%*lg,%*lg,%lg" will read "x,y3" from list above.
// Comments in TGraph source code notes there is a way to skip using %*lg in favor of ",,," or something, but I cannot get it to work.

TGraph* Curve_Nch_Total =         new TGraph(curvesCSVfile, "%lg,%lg");
TGraph* Curve_Nch_Assoc =         new TGraph(curvesCSVfile, "%lg,%*lg,%lg");
TGraph* Curve_Nch_Toward =        new TGraph(curvesCSVfile, "%lg,%*lg,%*lg,%lg");
TGraph* Curve_Nch_Away =          new TGraph(curvesCSVfile, "%lg,%*lg,%*lg,%*lg,%lg");
TGraph* Curve_Nch_TransAVE =      new TGraph(curvesCSVfile, "%lg,%*lg,%*lg,%*lg,%*lg,%lg");
TGraph* Curve_Nch_TransMAX =      new TGraph(curvesCSVfile, "%lg,%*lg,%*lg,%*lg,%*lg,%*lg,%lg");
TGraph* Curve_Nch_TransMIN =      new TGraph(curvesCSVfile, "%lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%lg");
TGraph* Curve_Nch_TransDIF =      new TGraph(curvesCSVfile, "%lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%lg");

TGraph* Curve_PtSum_Total =       new TGraph(curvesCSVfile, "%lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%lg");
TGraph* Curve_PtSum_Assoc =       new TGraph(curvesCSVfile, "%lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%lg");
TGraph* Curve_PtSum_Toward =      new TGraph(curvesCSVfile, "%lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%lg");
TGraph* Curve_PtSum_Away =        new TGraph(curvesCSVfile, "%lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%lg");
TGraph* Curve_PtSum_TransAVE =    new TGraph(curvesCSVfile, "%lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%lg");
TGraph* Curve_PtSum_TransMAX =    new TGraph(curvesCSVfile, "%lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%lg");
TGraph* Curve_PtSum_TransMIN =    new TGraph(curvesCSVfile, "%lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%lg");
TGraph* Curve_PtSum_TransDIF =    new TGraph(curvesCSVfile, "%lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%lg");

TGraph* Curve_PtAve_Trans =       new TGraph(curvesCSVfile, "%lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%lg");


TProfile *GEN_overallTotalNch_bh;
gDirectory->GetObject("GEN_overallTotalNch_bh",GEN_overallTotalNch_bh);
GEN_overallTotalNch_bh->Scale(scaleTotal);
GEN_overallTotalNch_bh->Draw();
Curve_Nch_Total->Draw("c same");
c1->SaveAs("curvePlots/Nch_Total.png");

TProfile *GEN_towardNch_bh;
gDirectory->GetObject("GEN_towardNch_bh",GEN_towardNch_bh);
GEN_towardNch_bh->Scale(scaleThird);
GEN_towardNch_bh->Draw();
Curve_Nch_Toward->Draw("c same");
c1->SaveAs("curvePlots/Nch_Toward.png");

TProfile *GEN_awayNch_bh;
gDirectory->GetObject("GEN_awayNch_bh",GEN_awayNch_bh);
GEN_awayNch_bh->Scale(scaleThird);
GEN_awayNch_bh->Draw();
Curve_Nch_Away->Draw("c same");
c1->SaveAs("curvePlots/Nch_Away.png");

TProfile *GEN_transNch_bh;
gDirectory->GetObject("GEN_transNch_bh",GEN_transNch_bh);
GEN_transNch_bh->Scale(scaleThird);
GEN_transNch_bh->Draw();
Curve_Nch_TransAVE->Draw("c same");
c1->SaveAs("curvePlots/Nch_TransAVE.png");

TProfile *GEN_transMaxNch_bh;
gDirectory->GetObject("GEN_transMaxNch_bh",GEN_transMaxNch_bh);
GEN_transMaxNch_bh->Scale(scaleSixth);
GEN_transMaxNch_bh->Draw();
Curve_Nch_TransMAX->Draw("c same");
c1->SaveAs("curvePlots/Nch_TransMAX.png");

TProfile *GEN_transMinNch_bh;
gDirectory->GetObject("GEN_transMinNch_bh",GEN_transMinNch_bh);
GEN_transMinNch_bh->Scale(scaleSixth);
GEN_transMinNch_bh->Draw();
Curve_Nch_TransMIN->Draw("c same");
c1->SaveAs("curvePlots/Nch_TransMIN.png");

TProfile *GEN_transDifNch_bh;
gDirectory->GetObject("GEN_transDifNch_bh",GEN_transDifNch_bh);
GEN_transDifNch_bh->Scale(scaleSixth);
GEN_transDifNch_bh->Draw();
Curve_Nch_TransDIF->Draw("c same");
c1->SaveAs("curvePlots/Nch_TransDIF.png");



TProfile *GEN_overallTotal_bh;
gDirectory->GetObject("GEN_overallTotal_bh",GEN_overallTotal_bh);
GEN_overallTotal_bh->Scale(scaleTotal);
GEN_overallTotal_bh->Draw();
Curve_PtSum_Total->Draw("c same");
c1->SaveAs("curvePlots/PtSum_Total.png");

TProfile *GEN_toward_bh;
gDirectory->GetObject("GEN_toward_bh",GEN_toward_bh);
GEN_toward_bh->Scale(scaleThird);
GEN_toward_bh->Draw();
Curve_PtSum_Toward->Draw("c same");
c1->SaveAs("curvePlots/PtSum_Toward.png");

TProfile *GEN_away_bh;
gDirectory->GetObject("GEN_away_bh",GEN_away_bh);
GEN_away_bh->Scale(scaleThird);
GEN_away_bh->Draw();
Curve_PtSum_Away->Draw("c same");
c1->SaveAs("curvePlots/PtSum_Away.png");

TProfile *GEN_trans_bh;
gDirectory->GetObject("GEN_trans_bh",GEN_trans_bh);
GEN_trans_bh->Scale(scaleThird);
GEN_trans_bh->Draw();
Curve_PtSum_TransAVE->Draw("c same");
c1->SaveAs("curvePlots/PtSum_TransAVE.png");

TProfile *GEN_transMax_bh;
gDirectory->GetObject("GEN_transMax_bh",GEN_transMax_bh);
GEN_transMax_bh->Scale(scaleSixth);
GEN_transMax_bh->Draw();
Curve_PtSum_TransMAX->Draw("c same");
c1->SaveAs("curvePlots/PtSum_TransMAX.png");

TProfile *GEN_transMin_bh;
gDirectory->GetObject("GEN_transMin_bh",GEN_transMin_bh);
GEN_transMin_bh->Scale(scaleSixth);
GEN_transMin_bh->Draw();
Curve_PtSum_TransMIN->Draw("c same");
c1->SaveAs("curvePlots/PtSum_TransMIN.png");

TProfile *GEN_transDif_bh;
gDirectory->GetObject("GEN_transDif_bh",GEN_transDif_bh);
GEN_transDif_bh->Scale(scaleSixth);
GEN_transDif_bh->Draw();
Curve_PtSum_TransDIF->Draw("c same");
c1->SaveAs("curvePlots/PtSum_TransDIF.png");

TProfile *GEN_transAvg_bh;
gDirectory->GetObject("GEN_transAvg_bh",GEN_transAvg_bh);
GEN_transAvg_bh->Draw();
Curve_PtAve_Trans->Draw("c same");
c1->SaveAs("curvePlots/PtAve_Trans.png");

	cout << "Out files written" << endl;
	fhist->Close();
	}















