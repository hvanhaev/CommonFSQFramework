



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



	void printHistosRICKv3 ()
	{
	char* rootFile = "plots_GENforPAPER_eta20_6-29-15.root";
	//char* curvesCSVfile = "Tune_CUETP8M1_PTmax_Eta20.csv";
	char* curvesCSVfile2 = "Tune_Monash_PTmax_Eta20.csv";
	char* curvesCSVfile = "Tune_CUETP8M1_PTmax_Eta20.csv";
	cout << "Loading ROOT file    " << rootFile << endl;
	cout << "Loading CSV file     " << curvesCSVfile << endl;
	TFile *fhist = new TFile(rootFile);

	double etaCut = 2.0;
	double scaleTotal = 1/(2*3.14159*2*etaCut); 
	double scaleThird  = 3/(2*3.14159*2*etaCut);
	double scaleSixth = 6/(2*3.14159*2*etaCut);

	TCanvas *c1 = new TCanvas("c1","c1",600,400);
	//Remove the statistics block:
	gStyle->SetOptStat(0);	

//We load the curves and Monte Carlo into arrays for ease of plotting.  A map would be more elegant, but the code is short. :)

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

TGraph *CURVE[17];

CURVE[0] = Curve_Nch_Total;
CURVE[1] = Curve_Nch_Assoc;
CURVE[2] = Curve_Nch_Toward;
CURVE[3] = Curve_Nch_Away;
CURVE[4] = Curve_Nch_TransAVE;
CURVE[5] = Curve_Nch_TransMAX;
CURVE[6] = Curve_Nch_TransMIN;
CURVE[7] = Curve_Nch_TransDIF;

CURVE[8] = Curve_PtSum_Total;
CURVE[9] = Curve_PtSum_Assoc;
CURVE[10] = Curve_PtSum_Toward;
CURVE[11] = Curve_PtSum_Away;
CURVE[12] = Curve_PtSum_TransAVE;
CURVE[13] = Curve_PtSum_TransMAX;
CURVE[14] = Curve_PtSum_TransMIN;
CURVE[15] = Curve_PtSum_TransDIF;

CURVE[16] = Curve_PtAve_Trans;

TGraph* Curve2_Nch_Total =         new TGraph(curvesCSVfile2, "%lg,%lg");
TGraph* Curve2_Nch_Assoc =         new TGraph(curvesCSVfile2, "%lg,%*lg,%lg");
TGraph* Curve2_Nch_Toward =        new TGraph(curvesCSVfile2, "%lg,%*lg,%*lg,%lg");
TGraph* Curve2_Nch_Away =          new TGraph(curvesCSVfile2, "%lg,%*lg,%*lg,%*lg,%lg");
TGraph* Curve2_Nch_TransAVE =      new TGraph(curvesCSVfile2, "%lg,%*lg,%*lg,%*lg,%*lg,%lg");
TGraph* Curve2_Nch_TransMAX =      new TGraph(curvesCSVfile2, "%lg,%*lg,%*lg,%*lg,%*lg,%*lg,%lg");
TGraph* Curve2_Nch_TransMIN =      new TGraph(curvesCSVfile2, "%lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%lg");
TGraph* Curve2_Nch_TransDIF =      new TGraph(curvesCSVfile2, "%lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%lg");

TGraph* Curve2_PtSum_Total =       new TGraph(curvesCSVfile2, "%lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%lg");
TGraph* Curve2_PtSum_Assoc =       new TGraph(curvesCSVfile2, "%lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%lg");
TGraph* Curve2_PtSum_Toward =      new TGraph(curvesCSVfile2, "%lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%lg");
TGraph* Curve2_PtSum_Away =        new TGraph(curvesCSVfile2, "%lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%lg");
TGraph* Curve2_PtSum_TransAVE =    new TGraph(curvesCSVfile2, "%lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%lg");
TGraph* Curve2_PtSum_TransMAX =    new TGraph(curvesCSVfile2, "%lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%lg");
TGraph* Curve2_PtSum_TransMIN =    new TGraph(curvesCSVfile2, "%lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%lg");
TGraph* Curve2_PtSum_TransDIF =    new TGraph(curvesCSVfile2, "%lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%lg");

TGraph* Curve2_PtAve_Trans =       new TGraph(curvesCSVfile2, "%lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%*lg,%lg");

TGraph *CURVE2[17];

CURVE2[0] = Curve2_Nch_Total;
CURVE2[1] = Curve2_Nch_Assoc;
CURVE2[2] = Curve2_Nch_Toward;
CURVE2[3] = Curve2_Nch_Away;
CURVE2[4] = Curve2_Nch_TransAVE;
CURVE2[5] = Curve2_Nch_TransMAX;
CURVE2[6] = Curve2_Nch_TransMIN;
CURVE2[7] = Curve2_Nch_TransDIF;

CURVE2[8] = Curve2_PtSum_Total;
CURVE2[9] = Curve2_PtSum_Assoc;
CURVE2[10] = Curve2_PtSum_Toward;
CURVE2[11] = Curve2_PtSum_Away;
CURVE2[12] = Curve2_PtSum_TransAVE;
CURVE2[13] = Curve2_PtSum_TransMAX;
CURVE2[14] = Curve2_PtSum_TransMIN;
CURVE2[15] = Curve2_PtSum_TransDIF;

CURVE2[16] = Curve2_PtAve_Trans;

	fhist->cd("MinBias_TuneCUETP8M1_13TeV-pythia8");

	//fhist->cd("MinBias_TuneCUETP8M1_13TeV-pythia8");
	//fhist->cd("MinBias_TuneMonash13_13TeV-pythia8");

        //TODO: replace duplicate toward plot with associated

TProfile *GEN[17];
gDirectory->GetObject("GEN_overallTotalNch_bh",GEN[0]); 
//gDirectory->GetObject("GEN_assocNch_bh",GEN[1]); 
gDirectory->GetObject("GEN_towardNch_bh",GEN[1]); 
gDirectory->GetObject("GEN_towardNch_bh",GEN[2]);
gDirectory->GetObject("GEN_awayNch_bh",GEN[3]);
gDirectory->GetObject("GEN_transNch_bh",GEN[4]);
gDirectory->GetObject("GEN_transMaxNch_bh",GEN[5]);
gDirectory->GetObject("GEN_transMinNch_bh",GEN[6]);
gDirectory->GetObject("GEN_transDifNch_bh",GEN[7]);
gDirectory->GetObject("GEN_overallTotal_bh",GEN[8]);
//gDirectory->GetObject("GEN_assoc_bh",GEN[9]); 
gDirectory->GetObject("GEN_toward_bh",GEN[9]); 
gDirectory->GetObject("GEN_toward_bh",GEN[10]);
gDirectory->GetObject("GEN_away_bh",GEN[11]);
gDirectory->GetObject("GEN_trans_bh",GEN[12]);
gDirectory->GetObject("GEN_transMax_bh",GEN[13]);
gDirectory->GetObject("GEN_transMin_bh",GEN[14]);
gDirectory->GetObject("GEN_transDif_bh",GEN[15]);
gDirectory->GetObject("GEN_transAvg_bh",GEN[16]);

	fhist->cd("MinBias_TuneCUETHS1_13TeV-herwigpp");

TProfile *GEN2[17];
gDirectory->GetObject("GEN_overallTotalNch_bh",GEN2[0]); 
//gDirectory->GetObject("GEN_assocNch_bh",GEN2[1]); 
gDirectory->GetObject("GEN_towardNch_bh",GEN2[1]); 
gDirectory->GetObject("GEN_towardNch_bh",GEN2[2]);
gDirectory->GetObject("GEN_awayNch_bh",GEN2[3]);
gDirectory->GetObject("GEN_transNch_bh",GEN2[4]);
gDirectory->GetObject("GEN_transMaxNch_bh",GEN2[5]);
gDirectory->GetObject("GEN_transMinNch_bh",GEN2[6]);
gDirectory->GetObject("GEN_transDifNch_bh",GEN2[7]);
gDirectory->GetObject("GEN_overallTotal_bh",GEN2[8]);
//gDirectory->GetObject("GEN_assoc_bh",GEN2[9]); 
gDirectory->GetObject("GEN_toward_bh",GEN2[9]); 
gDirectory->GetObject("GEN_toward_bh",GEN2[10]);
gDirectory->GetObject("GEN_away_bh",GEN2[11]);
gDirectory->GetObject("GEN_trans_bh",GEN2[12]);
gDirectory->GetObject("GEN_transMax_bh",GEN2[13]);
gDirectory->GetObject("GEN_transMin_bh",GEN2[14]);
gDirectory->GetObject("GEN_transDif_bh",GEN2[15]);
gDirectory->GetObject("GEN_transAvg_bh",GEN2[16]);


//cout << "Toward bin before scaling " << GEN[1]->GetBinContent(40) << endl;
for (unsigned int i = 0; i < 17; i++)
{
    //Skip Associated for now
    if ( (i == 1) || (i == 9) ): continue;

    GEN[i]->SetXTitle("p_{T} max (GeV/C)");
    GEN2[i]->SetXTitle("p_{T} max (GeV/C)");
    CURVE[i]->SetLineColor(2);
    CURVE2[i]->SetLineColor(8);

    if (i < 8)
    {
        GEN[i]->SetYTitle("<dN>/d#etad#phi");
        GEN2[i]->SetYTitle("<dN>/d#etad#phi");
    }
    else if (i == 16)
    {
        GEN[i]->SetYTitle("<p_{T}> (GeV/C)");
        GEN2[i]->SetYTitle("<p_{T}> (GeV/C)");
    }
    else
    {
        GEN[i]->SetYTitle("<#sump_{T}>/d#etad#phi");
        GEN2[i]->SetYTitle("<#sump_{T}>/d#etad#phi");
    }

    if (i < 8)
    {
        GEN[i]->SetAxisRange(0,3.5,"Y");
        GEN2[i]->SetAxisRange(0,3.5,"Y");
    }
    else if (7 < i < 12)
    {
        GEN[i]->SetAxisRange(0,7,"Y");
        GEN2[i]->SetAxisRange(0,7,"Y");
    }
    else
    {
        GEN[i]->SetAxisRange(0,4,"Y");
        GEN2[i]->SetAxisRange(0,4,"Y");
    }

    if ( (i == 0) || (i == 8) )
    {
	cout << i << " Total" << endl;
        GEN[i]->Scale(scaleTotal);
        GEN2[i]->Scale(scaleTotal);
    }
    else if ( (0 < i && i < 5) || (8 < i && i < 13) )
    {
	//cout << "i is " << i << " and is in (1,4) or (9,12)?" << endl; 
	//cout << "(8 < i < 13) is " << (8 < i < 13) << endl; 
	cout << i << " Third" << endl;
        GEN[i]->Scale(scaleThird);
        GEN2[i]->Scale(scaleThird);
    }
    else if ( (4 < i && i < 8) || (12 < i && i < 16) )
    {
	cout << i << " Sixth" << endl;
        GEN[i]->Scale(scaleSixth);
        GEN2[i]->Scale(scaleSixth);
    }
    //cout << i << " Toward bin during scaling " << GEN[1]->GetBinContent(40) << endl;

}

leg = new TLegend(0.6,0.6,0.89,0.89);
leg->AddEntry(CURVE2[0],"Monash","l");
leg->AddEntry(CURVE[0],"CUETP8M1","l");
leg->AddEntry(GEN[0],"CUETP8M1");

for (unsigned int i = 0; i < 17; i++)
{
    //Skip Associated for now
    if ( (i == 1) || (i == 9) ): continue;

    GEN[i]->Draw();
    CURVE[i]->Draw("c same");
    CURVE2[i]->Draw("c same");
    leg->Draw();

    if (i==0): c1->SaveAs("curvePlots/Nch_Total.png");
    if (i==1): c1->SaveAs("curvePlots/Nch_Assoc.png");
    if (i==2): c1->SaveAs("curvePlots/Nch_Toward.png");
    if (i==3): c1->SaveAs("curvePlots/Nch_Away.png");
    if (i==4): c1->SaveAs("curvePlots/Nch_TransAVE.png");
    if (i==5): c1->SaveAs("curvePlots/Nch_TransMAX.png");
    if (i==6): c1->SaveAs("curvePlots/Nch_TransMIN.png");
    if (i==7): c1->SaveAs("curvePlots/Nch_TransDIF.png");

    if (i==8): c1->SaveAs("curvePlots/PtSum_Total.png");
    if (i==9): c1->SaveAs("curvePlots/PtSum_Assoc.png");
    if (i==10): c1->SaveAs("curvePlots/PtSum_Toward.png");
    if (i==11): c1->SaveAs("curvePlots/PtSum_Away.png");
    if (i==12): c1->SaveAs("curvePlots/PtSum_TransAVE.png");
    if (i==13): c1->SaveAs("curvePlots/PtSum_TransMAX.png");
    if (i==14): c1->SaveAs("curvePlots/PtSum_TransMIN.png");
    if (i==15): c1->SaveAs("curvePlots/PtSum_TransDIF.png");

    if (i==16): c1->SaveAs("curvePlots/PtAve_Trans.png");


}


//GEN[0]->Draw();
//GEN[1]->Draw();
//GEN[2]->Draw();



//for (unsigned int i = 0; i < 17; i++)
//{
//    GEN[i]->Draw();
//}
/*
for (unsigned int i = 0; i < 17; i++)
{
    //Set axis labels
    GEN[i]->SetXTitle("p_{T} max (GeV/C)");
    GEN2[i]->SetXTitle("p_{T} max (GeV/C)");
    CURVE[i]->SetLineColor(2);
    CURVE2[i]->SetLineColor(8);
    if (i < 8)
    {
        GEN[i]->SetYTitle("dN/d#etad#phi");
        GEN2[i]->SetYTitle("dN/d#etad#phi");
    }

    else if (i == 16)
    {
        GEN[i]->SetYTitle("<p_{T}> (GeV/C)");
        GEN2[i]->SetYTitle("<p_{T}> (GeV/C)");
    }
    else
    {
        GEN[i]->SetYTitle("<#sump_{T}/d#etad#phi");
        GEN2[i]->SetYTitle("<#sump_{T}/d#etad#phi");
    }


    //Set Y ranges
    if (i < 8)
    {
        GEN[i]->SetAxisRange(0,3.5,"Y");
        GEN2[i]->SetAxisRange(0,3.5,"Y");
    }
    else if (7 < i < 12)
    {
        GEN[i]->SetAxisRange(0,7,"Y");
        GEN2[i]->SetAxisRange(0,7,"Y");
    }
    else
    {
        GEN[i]->SetAxisRange(0,4,"Y");
        GEN2[i]->SetAxisRange(0,4,"Y");
    }

    //Scale Plots if not already done
    if ( (i == 1) || (i == 8) )
    {
        GEN[i]->Scale(scaleTotal);
        GEN2[i]->Scale(scaleTotal);
    }
    else if ( (0 < i < 5) || (8 < i < 13) )
    {
        GEN[i]->Scale(scaleThird);
        GEN2[i]->Scale(scaleThird);
    }
    else if ( (4 < i < 8) || (12 < i < 16) )
    {
        GEN[i]->Scale(scaleSixth);
        GEN2[i]->Scale(scaleSixth);
    }

}
*/

/*
leg = new TLegend(0.6,0.6,0.89,0.89);
leg->AddEntry(CURVE[0],"Monash","l");
leg->AddEntry(CURVE2[0],"CUETP8M1","l");
leg->AddEntry(GEN[0],"Data");
*/
//leg->SetHeader("MC/data comparison");
/*
for (unsigned int i = 0; i < 17 < i++)
{
    GEN[i]->Draw();
    CURVE[i]->Draw("c same");
    leg->Draw();

    if (i==0): c1->SaveAs("curvePlots/Nch_Total.png");
    if (i==1): c1->SaveAs("curvePlots/Nch_Assoc.png");
    if (i==2): c1->SaveAs("curvePlots/Nch_Toward.png");
    if (i==3): c1->SaveAs("curvePlots/Nch_Away.png");
    if (i==4): c1->SaveAs("curvePlots/Nch_TransAVE.png");
    if (i==5): c1->SaveAs("curvePlots/Nch_TransMAX.png");
    if (i==6): c1->SaveAs("curvePlots/Nch_TransMIN.png");
    if (i==7): c1->SaveAs("curvePlots/Nch_TransDIF.png");

    if (i==8): c1->SaveAs("curvePlots/PtSum_Total.png");
    if (i==9): c1->SaveAs("curvePlots/PtSum_Assoc.png");
    if (i==10): c1->SaveAs("curvePlots/PtSum_Toward.png");
    if (i==11): c1->SaveAs("curvePlots/PtSum_Away.png");
    if (i==12): c1->SaveAs("curvePlots/PtSum_TransAVE.png");
    if (i==13): c1->SaveAs("curvePlots/PtSum_TransMAX.png");
    if (i==14): c1->SaveAs("curvePlots/PtSum_TransMIN.png");
    if (i==15): c1->SaveAs("curvePlots/PtSum_TransDIF.png");

    if (i==16): c1->SaveAs("curvePlots/PtAve_Trans.png");


}
*/






	//gStyle->SetTitleX("p_{T} max (GeV/C)");

// Color codes:
// 1 black, 2 red, 3 light green, 4 blue, 5 yellow, 6 magenta, 7 cyan, 8 green


// Specify option as follows (for comma delimited):
// "%lg,%lg" chooses "x,y1" from say "x,y1,y2,y3,y4..."
// Add a %*lg for each column to skip.  So "%lg,%*lg,%*lg,%lg" will read "x,y3" from list above.
// Comments in TGraph source code notes there is a way to skip using %*lg in favor of ",,," or something, but I cannot get it to work.




//GEN[0]->Scale(scaleTotal);
//GEN[0]->Draw();
//GEN[0]->SetXTitle("p_{T} max (GeV/C)");
//GEN[0]->SetYTitle("dN/d#etad#phi");


//leg->Draw();

//Curve_Nch_Total->SetLineColor(2);
//Curve_Nch_Total->Draw("c same");
//c1->SaveAs("curvePlots/Nch_Total_array.png");

/*
GEN_overallTotalNch_bh->Scale(scaleTotal);
GEN_overallTotalNch_bh->Draw();
GEN_overallTotalNch_bh->SetXTitle("p_{T} max (GeV/C)");
GEN_overallTotalNch_bh->SetYTitle("dN/d#etad#phi");

leg = new TLegend(0.4,0.6,0.89,0.89);
leg->AddEntry(Curve_Nch_Total,"Monash","l");
//leg->AddEntry(fun3,"CUETP1M8","l");
leg->AddEntry(GEN_overallTotalNch_bh,"Data");
leg->SetHeader("MC/data comparison");
leg->Draw();

Curve_Nch_Total->SetLineColor(2);
Curve_Nch_Total->Draw("c same");
c1->SaveAs("curvePlots/Nch_Total.png");


GEN_towardNch_bh->Scale(scaleThird);
GEN_towardNch_bh->Draw();
Curve_Nch_Toward->Draw("c same");
c1->SaveAs("curvePlots/Nch_Toward.png");


GEN_awayNch_bh->Scale(scaleThird);
GEN_awayNch_bh->Draw();
Curve_Nch_Away->Draw("c same");
c1->SaveAs("curvePlots/Nch_Away.png");


GEN_transNch_bh->Scale(scaleThird);
GEN_transNch_bh->Draw();
Curve_Nch_TransAVE->Draw("c same");
c1->SaveAs("curvePlots/Nch_TransAVE.png");


GEN_transMaxNch_bh->Scale(scaleSixth);
GEN_transMaxNch_bh->Draw();
Curve_Nch_TransMAX->Draw("c same");
c1->SaveAs("curvePlots/Nch_TransMAX.png");


GEN_transMinNch_bh->Scale(scaleSixth);
GEN_transMinNch_bh->Draw();
Curve_Nch_TransMIN->Draw("c same");
c1->SaveAs("curvePlots/Nch_TransMIN.png");


GEN_transDifNch_bh->Scale(scaleSixth);
GEN_transDifNch_bh->Draw();
Curve_Nch_TransDIF->Draw("c same");
c1->SaveAs("curvePlots/Nch_TransDIF.png");




GEN_overallTotal_bh->Scale(scaleTotal);
GEN_overallTotal_bh->Draw();
Curve_PtSum_Total->Draw("c same");
c1->SaveAs("curvePlots/PtSum_Total.png");


GEN_toward_bh->Scale(scaleThird);
GEN_toward_bh->Draw();
Curve_PtSum_Toward->Draw("c same");
c1->SaveAs("curvePlots/PtSum_Toward.png");


GEN_away_bh->Scale(scaleThird);
GEN_away_bh->Draw();
Curve_PtSum_Away->Draw("c same");
c1->SaveAs("curvePlots/PtSum_Away.png");


GEN_trans_bh->Scale(scaleThird);
GEN_trans_bh->Draw();
Curve_PtSum_TransAVE->Draw("c same");
c1->SaveAs("curvePlots/PtSum_TransAVE.png");


GEN_transMax_bh->Scale(scaleSixth);
GEN_transMax_bh->Draw();
Curve_PtSum_TransMAX->Draw("c same");
c1->SaveAs("curvePlots/PtSum_TransMAX.png");


GEN_transMin_bh->Scale(scaleSixth);
GEN_transMin_bh->Draw();
Curve_PtSum_TransMIN->Draw("c same");
c1->SaveAs("curvePlots/PtSum_TransMIN.png");


GEN_transDif_bh->Scale(scaleSixth);
GEN_transDif_bh->Draw();
Curve_PtSum_TransDIF->Draw("c same");
c1->SaveAs("curvePlots/PtSum_TransDIF.png");


GEN_transAvg_bh->Draw();
Curve_PtAve_Trans->Draw("c same");
c1->SaveAs("curvePlots/PtAve_Trans.png");
*/
	cout << "Out files written" << endl;
	fhist->Close();
	}
















