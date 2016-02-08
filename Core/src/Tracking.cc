#include "../interface/Structures.h"
#include "../interface/Tracking.h"

#include <fstream>
#include <iostream>
#include <cmath>

#include "TMatrixD.h"

#define sqr(x) ((x) * (x))

using namespace std;

/*****************************************************************************/
class HitCluster
{
 public:
  vector<double> eta;  //eta
  double phi;  // phi
  int    n;    // number of attached points
  vector<HitCluster>::iterator minCluster;  // closest HitCluster
  double       minDistance; // smallest distance
  unsigned int minVertex;   // primary vertex favored
  
  vector<int> list; // list of points

  bool use;

  pair<unsigned long int, unsigned long int> detids;
};

/*****************************************************************************/
Tracking::Tracking
  (const double & dMax_, const vector<double> & z0_) : dMax(dMax_), z0(z0_)
{
}

/*****************************************************************************/
bool Tracking::findClosest
  (vector<HitCluster> & HitClusters, vector<HitCluster>::iterator c1)
{
  bool isFirst = true;

  for(vector<HitCluster>::iterator c2 = HitClusters.begin();
                                   c2!= HitClusters.end(); c2++)
  if(c2->use)
  if(c1 != c2)
  for(unsigned int j = 0; j < z0.size(); j++) // try all primary vertices
  if(c1->n == 1 || c1->minVertex == j)
  if(c2->n == 1 || c2->minVertex == j)
  if(c1->detids != c2->detids) // fIXME
  {
    double dphi = fabs(c1->phi - c2->phi);
    if(dphi > M_PI) dphi -= 2*M_PI;

    double dist = sqr(c1->eta[j]  - c2->eta[j]) + sqr(dphi);

    if(dist < c1->minDistance || isFirst)
    {
      c1->minCluster  = c2;
      c1->minDistance = dist;
      c1->minVertex   = j;

      isFirst = false;
    }
  }

  return !isFirst;
}

/*****************************************************************************/
void Tracking::run
  (const vector<TVector3> & points,
   const vector<pair<unsigned long int, unsigned long int> > & detids,
   vector<LineTrack> & lines)
{
  vector<HitCluster> HitClusters;

  // Initialize HitClusters
  for(vector<TVector3>::const_iterator p = points.begin();
                                       p!= points.end(); p++)
  {
    HitCluster HitCluster;

    for(vector<double>::const_iterator z = z0.begin();
                                       z!= z0.end(); z++)
    {
      TVector3 V(0,0,*z);
      HitCluster.eta.push_back((*p - V).Eta());
    }

    HitCluster.phi = p->Phi();
    HitCluster.n   = 1;
    HitCluster.use = true;

    HitCluster.detids = detids[int(p - points.begin())];

    vector<int> l;
    l.push_back(p - points.begin());

    HitCluster.list = l;

    HitClusters.push_back(HitCluster);
  }

  lines.clear();

  for(vector<HitCluster>::iterator c1 = HitClusters.begin();
                                   c1!= HitClusters.end(); c1++)
  if(c1->use)
  {
    LineTrack line;
    line.hits = c1->list;
    lines.push_back(line);
  }

  unsigned int nUse = HitClusters.size() - 1;

  // Find nearest neighbors
  bool ok = false;
  for(vector<HitCluster>::iterator c1 = HitClusters.begin();
                                   c1!= HitClusters.end(); c1++)
    if(findClosest(HitClusters, c1)) ok = true;

  // return if there are no pairs to look at
  if(!ok) return;

  while(nUse > 0)
  {
    vector<HitCluster>::iterator c[2];
    double minDistance = 0;
    bool isFirst = true;
    unsigned int cv = 0;

    // Find smallest distance
    for(vector<HitCluster>::iterator c1 = HitClusters.begin();
                                     c1!= HitClusters.end(); c1++)
    if(c1->use)
    if(c1->minDistance < minDistance || isFirst)
    {
      minDistance = c1->minDistance;

      c[0] = c1 ;
      c[1] = c1->minCluster;
      cv   = c1->minVertex;

      isFirst = false;
    }

    // Join 
    double eta = (c[0]->n*c[0]->eta[cv] + c[1]->n*c[1]->eta[cv])/
                 (c[0]->n + c[1]->n);

    double phi = atan2(c[0]->n*sin(c[0]->phi) + c[1]->n*sin(c[1]->phi),
                       c[0]->n*cos(c[0]->phi) + c[1]->n*cos(c[1]->phi));

    // Update
    c[0]->eta[cv] = eta;
    c[0]->phi = phi;     
    c[0]->n   = c[0]->n + c[1]->n;
    c[0]->minVertex = cv;

    for(vector<int>::iterator il = c[1]->list.begin();
                              il!= c[1]->list.end(); il++) 
      c[0]->list.push_back(*il);

    // Remove c[1]
    c[1]->use  = false;

    // Fill list if we are still ok
    if(minDistance < sqr(dMax))
    {
      lines.clear();

      for(vector<HitCluster>::iterator c1 = HitClusters.begin();
                                       c1!= HitClusters.end(); c1++)
      if(c1->use)
      {
        LineTrack line;
        line.hits = c1->list;

        line.favoredVertex = c1->minVertex;

        lines.push_back(line);
      }
    }

    for(vector<HitCluster>::iterator c1 = HitClusters.begin();
                                     c1!= HitClusters.end(); c1++)
    if(c1->use && (c1->minCluster == c[0] ||
                   c1->minCluster == c[1]))
      findClosest(HitClusters, c1);

    nUse--;
  }
}

