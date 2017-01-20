#ifndef _Structures_
#define _Structures_

#include <vector>

struct LineFit
{
  double z0,d0, theta,phi, delta, sigma_z, eta,pt;
  bool isPrimary;
};

struct LineTrack
{
  std::vector<int> hits; // indexing original points
  LineFit pars;     // result of straight-line fit, with d0 = 0 fix
  LineFit parsFree; // result of straight-line fit, all four variables free
  int favoredVertex;
};

struct LineCluster
{
  double pos;   // z position
  double sig2;  // sigma_z^2
  int    n;     // number of attached tracks
  std::vector<LineCluster>::iterator minCluster;  // closest cluster
  double                             minDistance; // smallest distance

  std::vector<int> list; // list of tracks

  bool use;
};

struct LineVertex
{
  std::vector<int> tracks; // indexing attached LineTracks, second
  double z0;       // first.first
  double sigma_z;  // first.second
  double x0;       // will only be filled after vertexFit
  double y0;       // will only be filled after vertexFit
};

struct RawPixelRecHit{
    double x;
    double y;
    double z;
    int nx;
    int ny;
    unsigned long int id;
};

struct RawStripRecHit{
    double x;
    double y;
    double z;
    int monoSize;
    int stereoSize;
    unsigned long int monoId;
    unsigned long int stereoId;
};
#endif
