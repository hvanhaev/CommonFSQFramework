#include "../interface/Structures.h"
#include "../interface/Seeding.h"

#include <fstream>
#include <iostream>
#include <cmath>

#define sqr(x) ((x) * (x))

using namespace std;

/*****************************************************************************/
Seeding::Seeding(double maxAngle_) : maxAngle(maxAngle_)
{
  dphi12.resize(nAngle);
  dphi23.resize(nAngle);

  dtheta12_23.resize(nAngle);

  dangle.resize(nAngle);
}

/*****************************************************************************/
Seeding::~Seeding()
{
  char name[256];

  sprintf(name,"../out/%s/angles.dat", "pixel");
  ofstream file(name);

  print(dphi12, file);
  print(dphi23, file);
  print(dtheta12_23, file);
  print(dangle, file);

  file.close();
}

/*****************************************************************************/
void Seeding::fill(vector<int> & histo, double x)
{
//  if(npoints < 100)
  if(x < 1.)
  {
    int i = x * histo.size();

    histo[i]++;
  }
}

/*****************************************************************************/
void Seeding::print(const vector<int> & histo, ofstream & file)
{
  double s = 0;
  for(vector<int>::const_iterator h = histo.begin();
                                  h!= histo.end(); h++) s += *h;

  for(vector<int>::const_iterator h = histo.begin();
                                  h!= histo.end(); h++)
    file << " " << float(h - histo.begin() + 0.5)/histo.size()
         << " " << *h/s << endl;

  file << endl << endl;
}

/*****************************************************************************/
int Seeding::getLayer(const TVector3 & p)
{
  double r2 = sqr(p.x()) + sqr(p.y());

  if(r2 > sqr(15)) return -3;

  if(fabs(p.z()) < 30) // barrel
  {
    if(r2 < sqr( 6)) return 1;
    if(r2 < sqr( 9)) return 2;
    if(r2 < sqr(12)) return 3;
  }
  else // endcap
  {
    if(fabs(p.z()) < 40) return -2; // -3 
    if(fabs(p.z()) < 50) return -3; // -4
  }

  return 0;
}

/*****************************************************************************/
void Seeding::run(const vector<TVector3> & points,
                  vector<LineTrack> & lines)
{
  // search for pixel triplets
  for(vector<TVector3>::const_iterator p1 = points.begin();
                                       p1!= points.end(); p1++)
  if(getLayer(*p1) == 1)
  // 2nd hit
  for(vector<TVector3>::const_iterator p2 = points.begin();
                                       p2!= points.end(); p2++)
  {
  int l2 = getLayer(*p2);
  if(abs(l2) == 2)
  {
    double dphi = fabs(p2->Phi() - p1->Phi());
    if(dphi >  M_PI) dphi -= 2*M_PI;
    if(dphi < -M_PI) dphi += 2*M_PI;

    fill(dphi12, fabs(dphi));

    if(fabs(dphi) < maxAngle)
    {
      double minAngle2 = 0;
      bool isFirst = true;

      // set up track
      LineTrack line;

      // 3rd hit
      for(vector<TVector3>::const_iterator p3 = points.begin();
                                           p3!= points.end(); p3++)
      {
      int l3 = getLayer(*p3);
      if(abs(l3) == 3 || (l2 == 2 && l3 == -2))
      {
        double dphi = fabs(p3->Phi() - p2->Phi());
        if(dphi >  M_PI) dphi -= 2*M_PI;
        if(dphi < -M_PI) dphi += 2*M_PI;

        fill(dphi23, fabs(dphi));

        if(fabs(dphi) < maxAngle)
        {
          double dtheta = fabs((*p3 - *p2).Theta() - (*p2 - *p1).Theta());
          if(dtheta >  M_PI) dtheta -= 2*M_PI;
          if(dtheta < -M_PI) dtheta += 2*M_PI;

          fill(dtheta12_23, fabs(dtheta));

          if(fabs(dtheta) < maxAngle)
          {
            double dAngle2 = sqr(dphi) + sqr(dtheta);

            // look for closest match
            if(dAngle2 < minAngle2 || isFirst)
            {
              minAngle2 = dAngle2;
              isFirst = false;

              line.hits.clear();
              line.hits.push_back(int(p1 - points.begin()));
              line.hits.push_back(int(p2 - points.begin()));
              line.hits.push_back(int(p3 - points.begin()));
            }
          }
        }
      }
      }

      if(!isFirst) // found good triplet
      {
        fill(dangle, sqrt(minAngle2));

        lines.push_back(line);
      }
    }
  }
  }
}

