#ifndef _Tracking_
#define _Tracking_

#include <utility>
#include <vector>

#include "TVectorD.h"
#include "TVector3.h"

class HitCluster;
class LineTrack;

class Tracking
{
 public:
  Tracking(const double & dMax_, const std::vector<double> & z0_);

  void run(const std::vector<TVector3> & points,
           const std::vector<std::pair<unsigned long int, unsigned long int> > & detids,
           std::vector<LineTrack> & lines);

 private:
  bool findClosest(std::vector<HitCluster> & clusters,
                   std::vector<HitCluster>::iterator c1);
  double dMax;
  std::vector<double> z0;
};

#endif
