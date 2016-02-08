#ifndef _LineFitter_
#define _LineFitter_

#include <vector>

#include "TVector3.h"

#include "Structures.h"

class LineFitter
{
 public:
  LineFitter() { }

  LineFit fit(const std::vector<TVector3> & points, bool isD0Fix);

 private:
  double value(const std::vector<TVector3> & points,
               const std::vector<double> & x);

  int nHitsForSum;
};

#endif
