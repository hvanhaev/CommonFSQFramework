{
  gROOT->Reset();
  gStyle->SetCanvasColor(0);
  gStyle->SetFrameBorderMode(0);
  gStyle->SetOptStat(0);
  gStyle->SetPalette(1,0);
  gStyle->SetTitleX(0.5); //title X location 
  gStyle->SetTitleY(0.96); //title Y location 
  gStyle->SetPaintTextFormat(".2f");

  TStyle *tdrStyle = new TStyle("tdrStyle","Style for P-TDR");

  // For the canvas:
  tdrStyle->SetCanvasBorderMode(0);
  tdrStyle->SetCanvasColor(kWhite);
  tdrStyle->SetCanvasDefH(600); //Height of canvas
  tdrStyle->SetCanvasDefW(600); //Width of canvas
  tdrStyle->SetCanvasDefX(0);   //POsition on screen
  tdrStyle->SetCanvasDefY(0);

  // For the Pad:
  tdrStyle->SetPadBorderMode(0);
  // tdrStyle->SetPadBorderSize(Width_t size = 1);
  tdrStyle->SetPadColor(kWhite);
  tdrStyle->SetPadGridX(false);
  tdrStyle->SetPadGridY(true);
  tdrStyle->SetGridColor(1);
  tdrStyle->SetGridStyle(3);
  tdrStyle->SetGridWidth(1);

  // For the frame:
  tdrStyle->SetFrameBorderMode(0);
  tdrStyle->SetFrameBorderSize(1);
  tdrStyle->SetFrameFillColor(0);
  tdrStyle->SetFrameFillStyle(0);
  tdrStyle->SetFrameLineColor(1);
  tdrStyle->SetFrameLineStyle(1);
  tdrStyle->SetFrameLineWidth(1);

  // For the histo:
  tdrStyle->SetHistFillColor(63);
  // tdrStyle->SetHistFillStyle(0);
  tdrStyle->SetHistLineColor(1);
  tdrStyle->SetHistLineStyle(0);
  tdrStyle->SetHistLineWidth(1);
  // tdrStyle->SetLegoInnerR(Float_t rad = 0.5);
  // tdrStyle->SetNumberContours(Int_t number = 20);

//  tdrStyle->SetEndErrorSize(0);
  tdrStyle->SetErrorX(0.);
//  tdrStyle->SetErrorMarker(20);
  
  tdrStyle->SetMarkerStyle(20);

  //For the fit/function:
  tdrStyle->SetOptFit(1);
  tdrStyle->SetFitFormat("5.4g");
  tdrStyle->SetFuncColor(2);
  tdrStyle->SetFuncStyle(1);
  tdrStyle->SetFuncWidth(1);

  //For the date:
  tdrStyle->SetOptDate(0);
  // tdrStyle->SetDateX(Float_t x = 0.01);
  // tdrStyle->SetDateY(Float_t y = 0.01);

  // For the statistics box:
  tdrStyle->SetOptFile(0);
  tdrStyle->SetOptStat(0); // To display the mean and RMS:   SetOptStat("mr");
  tdrStyle->SetStatColor(kWhite);
  tdrStyle->SetStatFont(42);
  tdrStyle->SetStatFontSize(0.025);
  tdrStyle->SetStatTextColor(1);
  tdrStyle->SetStatFormat("6.4g");
  tdrStyle->SetStatBorderSize(2);
  tdrStyle->SetStatH(0.1);
  tdrStyle->SetStatW(0.15);
  // tdrStyle->SetStatStyle(Style_t style = 1001);
  // tdrStyle->SetStatX(Float_t x = 0);
  // tdrStyle->SetStatY(Float_t y = 0);

  // Margins:
  tdrStyle->SetPadTopMargin(0.05);
  tdrStyle->SetPadBottomMargin(0.13);
  tdrStyle->SetPadLeftMargin(0.23);
  tdrStyle->SetPadRightMargin(0.05);

  // For the Global title:

  tdrStyle->SetOptTitle(0);
  tdrStyle->SetTitleFont(42);
  tdrStyle->SetTitleColor(1);
  tdrStyle->SetTitleTextColor(1);
  tdrStyle->SetTitleFillColor(10);
  tdrStyle->SetTitleFontSize(0.05);
  // tdrStyle->SetTitleH(0); // Set the height of the title box
  // tdrStyle->SetTitleW(0); // Set the width of the title box
  // tdrStyle->SetTitleX(0); // Set the position of the title box
  // tdrStyle->SetTitleY(0.985); // Set the position of the title box
  // tdrStyle->SetTitleStyle(Style_t style = 1001);
  // tdrStyle->SetTitleBorderSize(2);

  // For the axis titles:

  tdrStyle->SetTitleColor(1, "XYZ");
  tdrStyle->SetTitleFont(42, "XYZ");
  tdrStyle->SetTitleSize(0.06, "XYZ");
  // tdrStyle->SetTitleXSize(Float_t size = 0.02); // Another way to set the size?
  // tdrStyle->SetTitleYSize(Float_t size = 0.02);
  tdrStyle->SetTitleXOffset(0.9);
  tdrStyle->SetTitleYOffset(1.05);
  // tdrStyle->SetTitleOffset(1.1, "Y"); // Another way to set the Offset

  // For the axis labels:

  tdrStyle->SetLabelColor(1, "XYZ");
  tdrStyle->SetLabelFont(42, "XYZ");
  tdrStyle->SetLabelOffset(0.007, "XYZ");
  tdrStyle->SetLabelSize(0.05, "XYZ");

  // For the axis:

  tdrStyle->SetAxisColor(1, "XYZ");
  tdrStyle->SetStripDecimals(kTRUE);
  tdrStyle->SetTickLength(0.03, "XYZ");
  tdrStyle->SetNdivisions(510, "XYZ");
  tdrStyle->SetPadTickX(1);  // To get tick marks on the opposite side of the frame
  tdrStyle->SetPadTickY(1);

  // Change for log plots:
  tdrStyle->SetOptLogx(0);
  tdrStyle->SetOptLogy(0);
  tdrStyle->SetOptLogz(0);

  // Postscript options:
  // tdrStyle->SetPaperSize(15.,15.);
  // tdrStyle->SetLineScalePS(Float_t scale = 3);
  // tdrStyle->SetLineStyleString(Int_t i, const char* text);
  // tdrStyle->SetHeaderPS(const char* header);
  // tdrStyle->SetTitlePS(const char* pstitle);

  // tdrStyle->SetBarOffset(Float_t baroff = 0.5);
  // tdrStyle->SetBarWidth(Float_t barwidth = 0.5);
  // tdrStyle->SetPaintTextFormat(const char* format = "g");
  // tdrStyle->SetPalette(Int_t ncolors = 0, Int_t* colors = 0);
  // tdrStyle->SetTimeOffset(Double_t toffset);
  // tdrStyle->SetHistMinimumZero(kTRUE);

#define M_PI           3.14159265358979323846

  tdrStyle->cd();



  using namespace std;

TH1 *data;
TH1 *data2; 
TFile *f00 = new TFile("plotsCSA14_UEAna_3.root");
TFile *f01 = new TFile("plots_UETrackJet_lowPU.root");
//f00->Cd("MinBias_TuneMonash13_13TeV_pythia8");

//nTrans_SisCon5->Draw();

    TH2F *da=(TH2F*) f01->Get("Run2015B_4/ptTrans_SisCone5");
    TH2F *da_1=(TH2F*) f01->Get("Run2015B_5/ptTrans_SisCone5");
     TH2F *da_2=(TH2F*) f01->Get("Run2015B_6/ptTrans_SisCone5");
TH2F *da_3=(TH2F*) f01->Get("Run2015B_7/ptTrans_SisCone5");
TH2F *da_4=(TH2F*) f01->Get("Run2015B_8/ptTrans_SisCone5");
TH2F *da_5=(TH2F*) f01->Get("Run2015B_1/ptTrans_SisCone5");
TH2F *da_6=(TH2F*) f01->Get("Run2015B_2/ptTrans_SisCone5");
TH2F *da_7=(TH2F*) f01->Get("Run2015B_3/ptTrans_SisCone5");
TH2F *da_8=(TH2F*) f01->Get("Run2015B/ptTrans_SisCone5");

 	
    TH2F *sum = (TH2F*) da->Clone();
    sum->Add(da_1);
    sum->Add(da_2);	 
    sum->Add(da_3);
sum->Add(da_4);
sum->Add(da_5);
sum->Add(da_6);
sum->Add(da_7);
sum->Add(da_8);

cout << sum->GetEntries() << endl;
//MinBias_TuneCUETHS1_13TeV-herwigpp
//MinBias_TuneCUETP8M1_13TeV-pythia8
//MinBias_TuneMonash13_13TeV_pythia8->Draw(nTrans_SisCon5);

//TFile *f01 = new TFile("plotsCSA14_UEAna_4M.root");
//TFile *f01 = new TFile("/afs/cern.ch/work/d/dciangot/CMSSW_7_0_5/src/MNTriggerStudies/MNTriggerAna/test/CSA14/plotsCSA14_UEAna_old.root");
    TH2F *da2=(TH2F*) f00->Get("MinBias_TuneCUETP8M1_13TeV-pythia8/nTrans_SisCone5");
//TH2F* da2=(TH2F*) f01->Get("MinBias_TuneMonash13_13TeV_pythia8/gen_nTrans_SisCone5");
    TH2F *da3=(TH2F*) f00->Get("MinBias_TuneCUETHS1_13TeV-herwigpp/nTrans_SisCone5");

    //TProfile datap = da->ProfileY("d");

     data=(TH1*)  sum->ProfileY()->ProjectionX();
     data2=(TH1*)  da2->ProfileY()->ProjectionX();
     data3=(TH1*)  da3->ProfileY()->ProjectionX();

    //data2= gen_nTrans_SisCon5->ProfileY()->DrawCopy();

   //data->Draw(); 
   
   TH1F *d= (TH1F*) data->Clone(); 
   TH1F *g= (TH1F*) data2->Clone();	
   TH1F *g2= (TH1F*) data3->Clone();

   d->Sumw2();
   g->Sumw2();
   g2->Sumw2();	

 
   d->Scale(3./(2.*4*M_PI));
   g->Scale(3./(2.*4*M_PI)); 
   g2->Scale(3./(2.*4*M_PI));

    g->SetLineWidth(2);
    g->SetFillColor(0);
    g2->SetLineWidth(2);
    g2->SetFillColor(0);
    g2->SetLineColor(kMagenta);

    d->SetLineColor(kBlue);
    d->SetLineWidth(2);
    d->SetMarkerStyle(20);   
    d->SetMarkerSize(1); 
    d->SetMarkerColor(kBlue);	
	
TH1F *ERR = (TH1F *) g->Clone();
    ERR->Sumw2();

 TH1F *ERR2 = (TH1F *) g2->Clone();
    ERR2->Sumw2();




TH1D *RATIO = new TH1D("","",ERR->GetNbinsX(),ERR->GetXaxis()->GetXmin(),ERR->GetXaxis()->GetXmax());
TH1D *RATIO2 = new TH1D("","",ERR->GetNbinsX(),ERR->GetXaxis()->GetXmin(),ERR->GetXaxis()->GetXmax());

for(int m=1; m<ERR->GetNbinsX()+1; m++){
      if(ERR->GetBinContent(m)!=0) {
        RATIO->SetBinContent(m,d->GetBinContent(m)/ERR->GetBinContent(m));

}

if(ERR2->GetBinContent(m)!=0) {
RATIO2->SetBinContent(m,d->GetBinContent(m)/ERR2->GetBinContent(m));
}
}

TLine* line = new TLine(0.,1,30.,1);
    line->SetLineColor(2);
    line->SetLineWidth(2);


    //Plots 
    TCanvas* c1 = new TCanvas("c1","c1",0,0,800,600);

TPad *c1_2 = new TPad("c1_2", "newpad",0.01,0.01,0.99,0.32);

    c1_2->Draw();
    c1_2->cd();
    c1_2->SetTopMargin(0.05);
    c1_2->SetBottomMargin(0.28);
    c1_2->SetRightMargin(0.02);
    c1_2->SetLeftMargin(0.1);
    RATIO->SetLineWidth(2);
    RATIO->GetYaxis()->SetLabelSize(0.060);
    RATIO->GetYaxis()->SetTitleSize(0.12);
    RATIO->GetYaxis()->SetTitleOffset(0.25);
    RATIO->GetYaxis()->SetTitle("data/MC");
    RATIO->SetFillStyle(0);
    RATIO->SetMinimum(0.5);
    RATIO->SetMaximum(1.5);
    RATIO->Draw("histo");
    RATIO->GetXaxis()->SetRangeUser(0.,30.);
    RATIO2->SetLineWidth(2);
    RATIO2->SetFillStyle(0);
    RATIO2->SetLineColor(kMagenta);
    RATIO2->Draw("histosame");
    line->Draw("same");
    c1_2->SetLogy(0);
    c1->cd();


//
    TPad *c1_1 = new TPad("c1_1", "newpad",0.01,0.33,.99,.99);

	
    c1_1->Draw();
    c1_1->cd();
    c1_1->SetTopMargin(0.1);
    c1_1->SetBottomMargin(0.15);
    c1_1->SetRightMargin(0.02);
    c1_1->SetLeftMargin(0.15);
   // nTrans_SisCon5->Draw();	

    d->GetXaxis()->SetTitleOffset(1.);
    d->GetXaxis()->SetLabelSize(0.045);
    d->GetXaxis()->SetTitleSize(0.06);
    d->GetYaxis()->SetTitleOffset(0.75);
    d->GetYaxis()->SetTitle("<d^{2}N_{ch} / (d#eta d#phi)>");
    d->GetXaxis()->SetTitle("p_{T} [GeV]");
    d->GetYaxis()->SetLabelSize(0.045);
    d->GetYaxis()->SetTitleSize(0.06);
    d->GetXaxis()->SetRangeUser(0.,30); 		
    d->Draw();	
    g->Draw("histosame");	
    g2->Draw("histosame");
	

    TLatex latexLabel2;
    latexLabel2.SetTextSize(0.04);
    latexLabel2.SetTextFont(32);
    latexLabel2.SetNDC();
    latexLabel2.DrawLatex(0.4, 0.93, "CMS preliminary");//, pp L = 19.7 fb^{-1} at #sqrt{s} = 8 TeV");
    
    TLegend *pl = new TLegend(0.6,0.20,0.95,0.45);
    pl->SetTextSize(0.05); 
    pl->SetFillColor(0);
    pl-> SetNColumns(1);
    TLegendEntry *ple = pl->AddEntry(d, "Run2015B ZeroBias",  "P");
    TLegendEntry *plee = pl->AddEntry(g, "CUETP8M1 pythia8",  "L");	
    TLegendEntry *pleee = pl->AddEntry(g2, "CUETPHS1 herwig++",  "L");
    pl->Draw();
    //gPad->RedrawAxis();
    c1->SaveAs("UE_ptTrans.png");
//    gSystem->Exit(0);
}
    

