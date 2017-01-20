#include "../interface/LineFitter.h"

#include <iostream>
#include <cmath>

#include "TVectorD.h"
#include "TMatrixD.h"
#include "TDecompLU.h"

using namespace std;

#define sqr(x) ((x) * (x))

/*****************************************************************************/
double LineFitter::value(const vector<TVector3> & points,
                         const vector<double> & x)
{
  const double & z0    = x[0];
  const double & d0    = x[1];
  const double & theta = x[2];
  const double & phi   = x[3];

  double sumd2 = 0.;

  for(vector<TVector3>::const_iterator p = points.begin();
                                       p!= points.end(); p++)
  if(p < points.begin() + nHitsForSum)
  {
    TVector3 V(-d0*sin(theta), d0*cos(phi), z0);
    TVector3 u(sin(theta)*cos(phi), sin(theta)*sin(phi), cos(theta));

    TVector3 x = u.Cross(*p - V);

    sumd2 += x.Mag2();
  }

  return sumd2;
}


/*****************************************************************************/
LineFit LineFitter::fit(const vector<TVector3> & points, bool isD0Fix)
{
  // find best straight line, with d0=0 constraint or d0 free
  vector<double> x(4);
  const int nPars = x.size();
 
  // number of Newtonian steps to do
  const int nIter = 5;

  // use only the three closest hits to the beam-line
  nHitsForSum = 3;

  const TVector3 & a = points.front();
  const TVector3 & b = points.back();

  double ra = a.Perp();
  double rb = b.Perp();
  
  // Initial guess
  /* z0    */ x[0] = a.z() - ra/(rb-ra) * (b.z() - a.z());
  /* d0    */ x[1] = 0.;
  /* theta */ x[2] = (b-a).Theta();
  /* phi   */ x[3] = (b-a).Phi();

  for(int k = 0; k < nIter; k++)
  { 
    // step size for calculation
    const double de = 1e-3;

    // gradient
    TVectorD F(nPars);
    for(int i = 0; i < nPars; i++)
    {
      vector<double> v(2);
      x[i] +=   de; v[1] = value(points, x);
      x[i] -= 2*de; v[0] = value(points, x);
      x[i] +=   de;
  
      if(i != 1 || !isD0Fix) // zero for d0
        F(i) = (v[1] - v[0])/(2*de);
      else
        F(i) = 0.;
    }

    // Jaocbian
    TMatrixD J(nPars,nPars);
    for(int i = 0; i < nPars; i++)
    for(int j = 0; j < nPars; j++)
    if((i != 1 && j != 1) || !isD0Fix)
    {
      double v00,v10,v01,v11;
      x[i] +=   de; x[j] +=   de; v11 = value(points, x);
                    x[j] -= 2*de; v10 = value(points, x);
      x[i] -= 2*de;               v00 = value(points, x);
                    x[j] += 2*de; v01 = value(points, x);
      x[i] +=   de; x[j] -=   de;

      J(i,j) = (v11 + v00 - v10 - v01) / (2*de) / (2*de);
    }
    else
      J(i,j) = (i==j ? 1 : 0);

    // solve
    TDecompLU lu; lu.SetMatrix(J);

    bool decomp_flag = false;

    try {
        lu.Decompose();}
    catch (...){
        decomp_flag = true;}

    TVectorD dx(F);
    if (!decomp_flag){ 
        try{
            lu.Solve(dx);}
        catch (...){
            decomp_flag = true;}
        dx *= -1.;
    }

    if (decomp_flag) throw(1);

    // try Newtonian step
    vector<double> x_new(nPars);
    for(int i = 0; i < nPars; i++) x_new[i] = x[i] + dx(i);

    if(value(points, x_new) < value(points, x))
      for(int i = 0; i < nPars; i++) x[i] += dx(i);
    else
      for(int i = 0; i < nPars; i++) x[i] -= 1e-4*F(i);
  }

  LineFit pars;
  pars.z0    = x[0];
  pars.d0    = x[1];
  pars.theta = x[2];
  pars.phi   = x[3];

  nHitsForSum = 4;
  pars.delta  = sqrt(value(points, x) / min(nHitsForSum, int(points.size())));

  pars.sigma_z = pars.delta / sin(pars.theta);

  return pars;
}

