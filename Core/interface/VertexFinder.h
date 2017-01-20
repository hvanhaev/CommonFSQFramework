#ifndef _VertexFinder_
#define _VertexFinder_

#include <utility>
#include <vector>

#include "TVectorD.h"

class LineTrack;
class LineCluster;
class LineVertex;

class VertexFinder
{
 public:
  VertexFinder(double dMax);

  void run(const std::vector<LineTrack> & lines,
                 std::vector<LineVertex> & vertices);

 private:
  void findClosest(std::vector<LineCluster> & clusters,
                   std::vector<LineCluster>::iterator c1);
  double dMax;
};

#endif
