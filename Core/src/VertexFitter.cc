#include "../interface/Structures.h"
#include "../interface/VertexFitter.h"

#include <iostream>
#include <cmath>

#include "TVectorD.h"
#include "TMatrixD.h"

#include "TDecompLU.h"

using namespace std;

#define sqr(x) ((x) * (x))

/*****************************************************************************/
double VertexFitter::value(const vector<LineFit> & lineFits,
                           const vector<double>  & x) // vertex pos
{
  TVector3 V(x[0],x[1],x[2]);

  double sumd2 = 0.;

  for(vector<LineFit>::const_iterator p = lineFits.begin();
                                      p!= lineFits.end(); p++)
  {
    const double z0    = p->z0;
    const double d0    = p->d0;
    const double theta = p->theta;
    const double phi   = p->phi;
    const double delta = p->delta;

    TVector3 P(-d0*sin(theta), d0*cos(phi), z0);
    TVector3 u(sin(theta)*cos(phi), sin(theta)*sin(phi), cos(theta));

    TVector3 x = u.Cross(P - V);

    sumd2 += x.Mag2() / sqr(delta);
  }

  return sumd2;
}


/*****************************************************************************/
double VertexFitter::run(const vector<LineFit> & lineFits,
                               vector<double>  & x)
{
  // find best vertex position in 3D
  const int nPars = x.size();
  x[0] = 0.; x[1] = 0.; x[2] = 0.;

  // number of Newtonian steps to do
  const int nIter = 5;

  for(int k = 0; k < nIter; k++)
  {
    // step size for calculation
    const double de = 1e-3;

    // gradient
    TVectorD F(nPars);
    for(int i = 0; i < nPars; i++)
    {
      vector<double> v(2);
      x[i] +=   de; v[1] = value(lineFits, x);
      x[i] -= 2*de; v[0] = value(lineFits, x);
      x[i] +=   de;

      F(i) = (v[1] - v[0])/(2*de);
    }

    // Jacobian
    TMatrixD J(nPars,nPars);
    for(int i = 0; i < nPars; i++)
    for(int j = 0; j < nPars; j++)
    {
      double v00,v10,v01,v11;
  
      x[i] +=   de; x[j] +=   de; v11 = value(lineFits, x);
                    x[j] -= 2*de; v10 = value(lineFits, x);
      x[i] -= 2*de;               v00 = value(lineFits, x);
                    x[j] += 2*de; v01 = value(lineFits, x);
      x[i] +=   de; x[j] -=   de;

      J(i,j) = (v11 + v00 - v10 - v01) / (2*de) / (2*de);
    }

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

    if(value(lineFits, x_new) < value(lineFits, x))
      for(int i = 0; i < nPars; i++) x[i] += dx(i);
    else
      for(int i = 0; i < nPars; i++) x[i] -= 1e-4*F(i);
  }

  // return goodness-of-fit
  return sqrt(value(lineFits, x) / int(lineFits.size()));
}

