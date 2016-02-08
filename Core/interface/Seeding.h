#ifndef _Seeding_
#define _Seeding_

#include <fstream>
#include <utility>
#include <vector>

#include "TVector3.h"

class LineTrack;

class Seeding
{
 public:
  Seeding(double maxAngle_);
  ~Seeding();

  void run(const std::vector<TVector3> & points,
                 std::vector<LineTrack> & tracks);

 private:
  void fill(std::vector<int> & histo, double x);
  void print(const std::vector<int> & histo, std::ofstream & file);

  int getLayer(const TVector3 & p);

  double maxAngle;

  static const int nAngle = 1000;
  std::vector<int> dphi12, dphi23, dtheta12_23, dangle;

//  int npoints;
};

#endif
