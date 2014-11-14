// run  scram tool info roofitcore for include path
//
#include "/cvmfs/cms.cern.ch/slc6_amd64_gcc481/lcg/roofit/5.34.09-cms11/include/RooTFnBinding.h"
#include "TF1.h"
#include "TF2.h"
//  bindFunction(TF1* func, RooAbsReal& x, const RooArgList& params)
//        #f = RooFit.bindFunction(myTF1, pt,  RooArgList(a,b))
double  TF_linear(double *x, double *par)
{
   return (par[0]+x[0]*par[1]);
}

double TF_2d(double *x, double *par){
    double ret = 0;
    // 1. linear correction for a whole jet. Use only jet pt
    ret = (par[0]+x[0]*par[1]); // x[0] - pt
    ret += par[2]*x[1]; // x[1] - rho*area
    return ret;

}

double TF_2dPUptLinear(double *x, double *par){
    // x[0] - pt
    // x[1] - rho*area
    double ptSignalAndPU = (par[0]+x[0]*par[1]);
    double ptSignal = ptSignalAndPU + (par[2]+par[3]*ptSignalAndPU)* x[1];
    return ptSignal;
}

double TF_2dPUptLinearCorrected(double *x, double *par){
    // x[0] - pt
    // x[1] - rho*area
    double ptSignalAndPU  = (par[0]+x[0]*par[1]);
    double pu1 = par[2];
    double pu2 = par[3];
    double pu3 = par[4];
    double pu4 = par[5];
    double pu5 = par[6];
    double pu6 = par[7];
    double PUcorrection = (pu1+pu2*ptSignalAndPU +   pu3/(pu4+pu5*ptSignalAndPU))*x[1]+pu6;
    return ptSignalAndPU+PUcorrection;
}

RooAbsReal* getTF(RooAbsReal &var, RooArgList & args, float xmin=0, float xmax=10000){
    TF1 * myTF1 = new TF1("myfunc", TF_linear, xmin, xmax, 2);
    return RooFit::bindFunction(myTF1, var,  args);
}


RooAbsReal* getTF2d(RooAbsReal &var1, RooAbsReal &var2, RooArgList & args, 
            float xmin=0, float xmax=10000,
            float ymin=0, float ymax=10000 )
{
    TF2 * myTF2 = new TF2("tf2d", TF_2d, xmin, xmax, ymin, ymax, 3);
    return RooFit::bindFunction(myTF2, var1, var2, args);
}



RooAbsReal* getTF2d_PUptlinear(RooAbsReal &var1, RooAbsReal &var2, RooArgList & args, 
            float xmin=0, float xmax=10000,
            float ymin=0, float ymax=10000 )
{
    TF2 * myTF2 = new TF2("TF2d_2dPUptLinear", TF_2dPUptLinear, xmin, xmax, ymin, ymax, 4);
    return RooFit::bindFunction(myTF2, var1, var2, args);
}

// TF_2dPUptLinearCorrected
RooAbsReal* getTF2d_PUptlinearCorrected(RooAbsReal &var1, RooAbsReal &var2, RooArgList & args, 
            float xmin=0, float xmax=10000,
            float ymin=0, float ymax=10000 )
{
    TF2 * myTF2 = new TF2("TF_2dPUptLinearCorrected", TF_2dPUptLinearCorrected, xmin, xmax, ymin, ymax, 8);
    return RooFit::bindFunction(myTF2, var1, var2, args);
}
