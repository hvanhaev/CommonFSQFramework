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

  tdrStyle->cd();



  using namespace std;


vector<TString> name;   vector<TString> axis; vector<int> rebin;  vector<int> logy; vector<double> mini; vector<double> maxi;

name.push_back("tracksPt_post");  axis.push_back("p_{T} [Gev] "); rebin.push_back(1); logy.push_back(1); mini.push_back(0.); maxi.push_back(10);

name.push_back("tracksDeltaPhi");              axis.push_back("#Delta#phi");   rebin.push_back(628); logy.push_back(1); mini.push_back(-3.14); maxi.push_back(3.14); 
name.push_back("tracksDeltaPhi_post");              axis.push_back("#Delta#phi");   rebin.push_back(628); logy.push_back(1); mini.push_back(-3.14); maxi.push_back(3.14);
name.push_back("tracksDzSignificance");              axis.push_back("dz/#sigma_{dz} ");   rebin.push_back(1); logy.push_back(1); mini.push_back(-20); maxi.push_back(20);
name.push_back("tracksD0Significance");              axis.push_back("dxy/#sigma_{dxy} ");   rebin.push_back(1); logy.push_back(1); mini.push_back(-20); maxi.push_back(20);

name.push_back("pt_SisCone5"); 	                 axis.push_back("p_{T} [Gev] "); rebin.push_back(1); logy.push_back(1); mini.push_back(0.); maxi.push_back(40);
name.push_back("f_pt_SisCone5");                   axis.push_back("p_{T} [Gev] "); rebin.push_back(1); logy.push_back(1); mini.push_back(0.); maxi.push_back(40);

name.push_back("eta_SisCone5");                   axis.push_back("#eta "); rebin.push_back(1); logy.push_back(0); mini.push_back(-2); maxi.push_back(2);
name.push_back("f_eta_SisCone5");                   axis.push_back("#eta "); rebin.push_back(1); logy.push_back(0); mini.push_back(-5.); maxi.push_back(5);

name.push_back("phi_SisCone5");                   axis.push_back("#phi "); rebin.push_back(10); logy.push_back(0); mini.push_back(-3.14); maxi.push_back(3.14);
name.push_back("f_phi_SisCone5");                   axis.push_back("#phi "); rebin.push_back(10); logy.push_back(0); mini.push_back(-3.14); maxi.push_back(3.14);

name.push_back("nVtx");                   axis.push_back("# Vertices "); rebin.push_back(1); logy.push_back(1); mini.push_back(0.); maxi.push_back(50);


name.push_back("tracksPtSigma");                   axis.push_back("#sigma_{p_{T}}/p_{T} "); rebin.push_back(1); logy.push_back(1); mini.push_back(0.); maxi.push_back(0.2);
name.push_back("ndfVtx");                   axis.push_back("ndf Vertices "); rebin.push_back(2); logy.push_back(1); mini.push_back(0.); maxi.push_back(100);
name.push_back("nTracks_SisCone5");                   axis.push_back("# Tracks "); rebin.push_back(1); logy.push_back(1); mini.push_back(0.); maxi.push_back(50);

name.push_back("tracksPhi");                   axis.push_back("#phi "); rebin.push_back(4); logy.push_back(0); mini.push_back(-3.14); maxi.push_back(3.14);

name.push_back("tracksPhi_post");                   axis.push_back("#phi "); rebin.push_back(10); logy.push_back(0); mini.push_back(-3.14); maxi.push_back(3.14);

name.push_back("tracksEta");                   axis.push_back("#eta "); rebin.push_back(1); logy.push_back(0); mini.push_back(-5.); maxi.push_back(5);

name.push_back("tracksEta_post");                   axis.push_back("#eta "); rebin.push_back(1); logy.push_back(0); mini.push_back(-2.); maxi.push_back(2);

name.push_back("nJets");                   axis.push_back("# Tracks "); rebin.push_back(1); logy.push_back(1); mini.push_back(0.); maxi.push_back(10);

  TFile *f00 = new TFile("plotsCSA14_UEAna_3.root");
TFile *f01 = new TFile("plotsCSA14_UEAna_lowPU.root");
//    MinBias_TuneZ2star_13TeV_pythia6->cd();

//    nTrans_SisCon5->ProfileY("d");
 
   // TH2F *data2;    data2 = nTrans_SisCon5->Clone();
    for(int i=0; i<name.size(); i++){

    //TH1F *data; data= name[i]->Clone();
TH1F *da=(TH1F*) f01->Get("Run2015B_4/"+name[i]);
    TH1F *da_1=(TH1F*) f01->Get("Run2015B_5/"+name[i]);
    TH1F *da_2=(TH1F*) f01->Get("Run2015B_6/"+name[i]);

    TH1F *data = (TH1F*) da->Clone();
    data->Add(da_1);
    data->Add(da_2);


  TH1F *da2=(TH1F*) f00->Get("MinBias_TuneCUETP8M1_13TeV-pythia8/"+name[i]);

   TH1F *d= (TH1F*) data->Clone(); 
   TH1F *g= (TH1F*) da2->Clone();

   g->Sumw2();          
   g->Scale(1/g->Integral());
   g->Rebin(rebin[i]);

   d->Sumw2();		
   d->Scale(1/d->Integral());
   d->Rebin(rebin[i]);

   tdrStyle->SetOptLogy(logy[i]);
 
    g->SetMarkerStyle(20);
    g->SetMarkerSize(0.7);
    d->SetLineColor(kBlue);
    d->SetLineWidth(2);
    d->SetMarkerStyle(20);   
    d->SetMarkerSize(1.1); 
    d->SetMarkerColor(kBlue);	


    TH1F *ERR = (TH1F *) g->Clone();
    ERR->Sumw2();


    Int_t n = ERR->GetNbinsX();
   Double_t x[n];
   Double_t y[n];
   Double_t exl[n];
   Double_t eyl[n];
   Double_t exh[n];
   Double_t eyh[n];

   double mino=d->GetXaxis()->GetXmin();
   double maxo=d->GetXaxis()->GetXmax();

   double temp=mino+(maxo-mino)/n/2;



TH1D *RATIO = new TH1D("","",ERR->GetNbinsX(),ERR->GetXaxis()->GetXmin(),ERR->GetXaxis()->GetXmax());
    for(int m=1; m<ERR->GetNbinsX()+1; m++){
      if(ERR->GetBinContent(m)!=0) {
        RATIO->SetBinContent(m,d->GetBinContent(m)/ERR->GetBinContent(m));

}
}
TLine* line = new TLine(mini[i],1,maxi[i],1);
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
    RATIO->GetXaxis()->SetRangeUser(mini[i],maxi[i]); 
    line->Draw("same");
    c1_2->SetLogy(0);
    c1->cd();


//TCanvas* c1 = new TCanvas("c1","c1",0,0,800,600);
	
    TPad *c1_1 = new TPad("c1_1", "newpad",0.01,0.33,.99,.99);
    c1_1->Draw();
    c1_1->cd();
    c1_1->SetTopMargin(0.1);
    c1_1->SetBottomMargin(0.15);
    c1_1->SetRightMargin(0.02);
    c1_1->SetLeftMargin(0.12);
   // nTrans_SisCon5->Draw();	


    d->GetXaxis()->SetTitleOffset(1.);
    d->GetXaxis()->SetLabelSize(0.045);
    d->GetXaxis()->SetTitleSize(0.05);
    d->GetYaxis()->SetTitleOffset(0.75);
    d->GetYaxis()->SetTitle("dN/N");
    d->GetXaxis()->SetTitle(axis[i]);
    d->GetYaxis()->SetLabelSize(0.045);
    d->GetYaxis()->SetTitleSize(0.06);
    d->GetXaxis()->SetRangeUser(mini[i],maxi[i]); 		
    d->SetMaximum(d->GetMaximum()*1.5);
    d->SetMinimum(max(d->GetMinimum()-.0000001,0.00000001));
    d->Draw("histo");	
    g->Draw("same");

tdrStyle->SetOptLogy(logy[i]); 
	

    TLatex latexLabel2;
    latexLabel2.SetTextSize(0.04);
    latexLabel2.SetTextFont(32);
    latexLabel2.SetNDC();
    latexLabel2.DrawLatex(0.4, 0.93, "CMS preliminary");//"CMS Preliminary, pp L = 19.7 fb^{-1} at #sqrt{s} = 8 TeV");
    
    TLegend *pl = new TLegend(0.6,0.75,0.9,0.85);
    pl->SetTextSize(0.03); 
    pl->SetFillColor(0);
    pl-> SetNColumns(1);
    TLegendEntry *ple = pl->AddEntry(d, "Run2015B ZeroBias",  "PL");
    TLegendEntry *plee = pl->AddEntry(g, "CUETP8M1 pythia8",  "PL"); 	
    pl->Draw();
    gPad->RedrawAxis();
    c1->SaveAs("UE_"+name[i]+".png");

}
//gSystem->Exit(0); 
}
