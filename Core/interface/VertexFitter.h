#ifndef _VertexFitter_
#define _VertexFitter_

#include <vector>

#include "TVector3.h"

class LineFit;

class VertexFitter
{
 public:
  VertexFitter() {}

  double run(const std::vector<LineFit> & lineFits,
                   std::vector<double> & x);

 private:
  double value(const std::vector<LineFit> & lineFits,
               const std::vector<double>  & x);
};

#endif
