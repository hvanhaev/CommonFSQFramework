#include "../interface/Structures.h"

#include "../interface/VertexFinder.h"

#include "TMatrixD.h"
#include <iostream>
#include <cmath>

#define sqr(x) ((x) * (x))

using namespace std;

/*****************************************************************************/
VertexFinder::VertexFinder(double dMax_) : dMax(dMax_)
{
}

/*****************************************************************************/
void VertexFinder::findClosest
  (vector<LineCluster> & clusters, vector<LineCluster>::iterator c1)
{
  bool isFirst = true;

  for(vector<LineCluster>::iterator c2 = clusters.begin();
                                    c2!= clusters.end(); c2++)
  if(c2->use)
  if(c1 != c2)
  {
    double dist = sqr(c1->pos  - c2->pos ) /
                     (c1->sig2 + c2->sig2);

    if(dist < c1->minDistance || isFirst)
    {
      c1->minCluster  = c2;
      c1->minDistance = dist;

      isFirst = false;
    }
  }
}

/*****************************************************************************/
void VertexFinder::run
  (const vector<LineTrack> & lines,
         vector<LineVertex> & vertices)
{
  // internal containers
  vector<LineCluster> clusters;

  // initialize clusters, each with a single LineTrack
  for(vector<LineTrack>::const_iterator l = lines.begin();
                                        l!= lines.end(); l++)
  {
    LineCluster cluster;

    cluster.pos   =     l->pars.z0;
    cluster.sig2  = sqr(l->pars.sigma_z);
    cluster.n     = 1;
    cluster.use   = true;

    vector<int> list;
    list.push_back(l - lines.begin());

    cluster.list = list;

    clusters.push_back(cluster);
  }

  unsigned int nUse = clusters.size();

  double minDistance = 0.;

  while(nUse > 1 && minDistance < sqr(dMax))
  {
    vector<LineCluster>::iterator c[2];

    // find nearest neighbors
    for(vector<LineCluster>::iterator c1 = clusters.begin();
                                      c1!= clusters.end(); c1++)
      findClosest(clusters, c1);

    // find smallest distance
    bool isFirst = true;
    for(vector<LineCluster>::iterator c1 = clusters.begin();
                                      c1!= clusters.end(); c1++)
    if(c1->use)
    if(c1->minDistance < minDistance || isFirst)
    {
      minDistance = c1->minDistance;

      c[0] = c1 ;
      c[1] = c1->minCluster ;

      isFirst = false;
    }

    // if still ok, join, save and overwrite list
    if(minDistance < sqr(dMax))
    {
      // join 
      double sig2 = 1 /
                    (        1 / c[0]->sig2 +         1 / c[1]->sig2);
      double pos  = (c[0]->pos / c[0]->sig2 + c[1]->pos / c[1]->sig2) * sig2;

      // update
      c[0]->pos  = pos;     
      c[0]->sig2 = sig2;     
      c[0]->n    = c[0]->n + c[1]->n;

      for(vector<int>::iterator il = c[1]->list.begin();
                                il!= c[1]->list.end(); il++) 
        c[0]->list.push_back(*il);
  
      // remove c[1]
      c[1]->use  = false;
      nUse--;  
    }
  }

  // copy back to vertices
  for(vector<LineCluster>::const_iterator c = clusters.begin();
                                          c!= clusters.end(); c++)
  if(c->use)
  {
    LineVertex vertex;
   
    vertex.z0      = c->pos;
    vertex.sigma_z = sqrt(c->sig2);

    vertex.tracks  = c->list;

    vertices.push_back(vertex);
  }
}

