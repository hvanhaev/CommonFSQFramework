#include <iostream>
#include <stdio.h>
using namespace std;
void xPrint()
{
cout << "XXXXXXXXXXXXXXXXXXXXXXXXXXXHello this is Print.C" << endl;

}
void PrintHistogram(TH1F* h, Double_t hnorm, Int_t goexl, const char *fname) {
 	FILE *file;
if((file = fopen(fname,"wt"))==NULL) return;
   int nplot = h->GetEntries();
   double mean = h ->GetMean();
   double rms = h->GetRMS();
   double sum = h->GetSum();
   double integral = h->Integral();
   double wtsum = h->GetSumOfWeights();
   double avewt = 1.0;
   if (nplot > 0) avewt = wtsum/nplot;
   int nx = h->GetXaxis()->GetNbins();
   double xmin = h->GetXaxis()->GetXmin();
   double xmax = h->GetXaxis()->GetXmax();
   double dx = fabs((xmin-xmax)/nx);
   double scale = hnorm/dx;
   h->Scale(scale);
   fprintf(file,"\nHistogram: %s  Title = *** %s *** goexl = %d\n",h->GetName(),h->GetTitle(),goexl);
   fprintf(file,"  Nplot = %i Mean = %g RMS = %g WTsum = %g AveWT = %g\n",nplot,mean,rms,wtsum,avewt);
   fprintf(file,"  Nxbin = %i Xmin = %g Xmax = %g Dx = %g Hnorm  = %g Scale Factor = %g\n",nx,xmin,xmax,dx,hnorm,scale);                                                                                                                  
   fprintf(file,"  Old: PlotSum = %g Integral = %g  New: Plotsum = %g Integral = %g\n",sum,integral,scale*sum,scale*integral);
   if (goexl) {
   int nsize = nx+2;
   int istart = -1;
   int iend = nsize-1;
   double yval = 0.0;
   double yerr = 0.0;
   int ibins = 0;
   for (int i=0; i<nsize; i++) {
   yval = h->GetBinContent(i);
     if (yval != 0.0 && istart == -1) istart = i;
     if (yval != 0.0) {
     ibins++;
     iend = i;
     }
   }  // End loop over bins
   if (ibins)
   {
     fprintf(file," Histogram %s has the following %i bins: \n",h->GetName(),ibins);
     fprintf(file,"   xlow, xhigh, yval, yerr\n");
     for (int i=istart; i<iend+1; i++) {
       yval = h->GetBinContent(i);
       yerr = h->GetBinError(i);
       if (i == 0)
       {
       fprintf(file,"   underflow, < %g, %g, %g\n",xmin,yval,yerr);
       }
       else if (i == nsize-1)
       {
       fprintf(file,"   overflow, >= %g, %g, %g\n",xmax,yval,yerr);
       }
       else
       {
       fprintf(file,"     %g, %g, %g, %g\n",xmin+dx*(i-1),xmin+dx*i,yval,yerr);
       }
     }  // End loop over bins
   }
   else
   {
    fprintf(file," Histogram %s has no non-zero bins!\n",h->GetName());
   }
   } // End goexl
       fclose(file);                                                                                                           
}


 void PrintProfile(TProfile* h, Double_t hnorm, Int_t goexl, const char *fname) {
   FILE *file;
   if((file = fopen(fname,"wt"))==NULL) return;
   double nplot = h->GetEntries();
   double mean = h ->GetMean();
   double rms = h->GetRMS();
   double sum = h->GetSum();
   double integral = h->Integral();
   double wtsum = h->GetSumOfWeights();
   double avewt = 1.0;
   if (nplot > 0) avewt = wtsum/nplot;
   //cout <<"MKZ mark..Line27" << avewt << endl;
   int nx = h->GetXaxis()->GetNbins();
   double xmin = h->GetXaxis()->GetXmin();
   double xmax = h->GetXaxis()->GetXmax();
   double dx = fabs((xmin-xmax)/nx);
   double scale = hnorm;
   if (scale != 1.0) h->Scale(scale);
   fprintf(file,"\nProfile: %s  Title = *** %s *** goexl = %d\n",h->GetName(),h->GetTitle(),goexl);
   fprintf(file,"  Nplot = %f Mean = %g RMS = %g WTsum = %g AveWT = %g\n",nplot,mean,rms,wtsum,avewt);
   fprintf(file,"  Nxbin = %i Xmin = %g Xmax = %g Dx = %g Scale Factor = %g\n",nx,xmin,xmax,dx,scale);
   fprintf(file,"  Old: PlotSum = %g Integral = %g  New: Plotsum = %g Integral = %g\n",sum,integral,scale*sum,scale*integral);
   if (goexl) {
   int nsize = nx+2;
   int istart = -1;
   int iend = nsize-1;
   double yval = 0.0;
   double yerr = 0.0;
   int ibins = 0;
   for (int i=0; i<nsize; i++) {
   yval = h->GetBinContent(i);
     if (yval != 0.0 && istart == -1) istart = i;
     if (yval != 0.0) {
     ibins++;
     iend = i;
     }
   }  // End loop over bins
   if (ibins)
   {
     fprintf(file," Profile %s has the following %i bins: \n",h->GetName(),ibins);
     fprintf(file,"   xlow, xhigh, yval, yerr, entries\n");
     for (int i=istart; i<iend+1; i++) {
       yval = h->GetBinContent(i);
       yerr = h->GetBinError(i);
       if (i == 0)
       {
       fprintf(file,"   underflow, < %g, %g, %g, %g\n",xmin,yval,yerr,h->GetBinEntries(i));
       }
       else if (i == nsize-1)
       {
       fprintf(file,"   overflow, >= %g, %g, %g, %g\n",xmax,yval,yerr,h->GetBinEntries(i));
       }
       else
       {
       fprintf(file,"     %g, %g, %g, %g, %g\n",xmin+dx*(i-1),xmin+dx*i,yval,yerr,h->GetBinEntries(i));
       }
     }  // End loop over bins
   }
   else
   {
    fprintf(file," Profile %s has no non-zero bins!\n",h->GetName());
   }
   } // End goexl

   fclose(file);
}


