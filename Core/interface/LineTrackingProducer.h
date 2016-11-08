#ifndef _LineTrackingProducer_
#define _LineTrackingProducer_

#include "TVector3.h"
#include "../interface/Structures.h"

class Seeding;

class LineTrackingProducer
{
 public:
  LineTrackingProducer(bool usePixelHits_, double  beamSpotX, double beamSpotY);
  ~LineTrackingProducer();

  bool run(std::vector<RawPixelRecHit> RawPixelRecHits);
  bool run(std::vector<RawStripRecHit> RawStripRecHits);
  int getVertices(std::vector<double> & VerticesX, std::vector<double> & VerticesY, std::vector<double> & VerticesZ, std::vector<int> & nTracks);
  int getTracks(std::vector<double> & TracksTheta, std::vector<double> & TracksPhi, std::vector<double> & TracksZ0, std::vector<double> & TracksD0, std::vector<double> & TracksSigmaZ, std::vector<int> & iVertex);

 private:
  int readHits(std::vector<RawPixelRecHit> RawPixelRecHits, std::vector<LineFit> & simLines);
  int readHits(std::vector<RawStripRecHit> RawStripRecHits, std::vector<LineFit> & simLines);

  void cleanTracks(std::vector<LineTrack> & tracks);

  void findAndFitVertices(std::vector<LineTrack> & lines, std::vector<LineVertex> & vertices, int round);

  void sortByRadius(std::vector<int> & hits);

  void processHits(std::vector<LineTrack> & lines,
                   std::vector<LineVertex> & vertices);

  void saveResults(std::vector<LineTrack> & lines,
                   std::vector<LineVertex> & vertices);

  std::vector<LineTrack> linesResult;
  std::vector<LineVertex> verticesResult;


  Seeding * theSeeding;

  // beam spot
  double beam_x, beam_y;

  bool isMC;

  // simulated vertex or vertices
  std::vector<double> vz_sim, eventWeight;

  // container, for pixels or strips
  std::vector<TVector3> points;

  // container, for strips only
  std::vector<std::pair<unsigned long int, unsigned long int> > detids;

  // to be masked
  std::vector<unsigned long int> mask;

  bool usePixelHits;          // main switch

  double dMaxForVertexFinder; // when to stop track clustering into vertices
  double maxAbsoluteZ0;       // for track z
  int maxClusterWidthDiff;    // position-direction compatibility

  int nRounds;                // number of tracking-VertexFinder rounds to do

  // pixel
  double maxAngle;            // maximal angle for pair and triplet building
  double minAngle;            // minimal agnle for track cleaning

  // strips
  double maxFirstHitRadius;   // for strip hit on tracck closest to the beamline
  int maxSharedDets;          // maximal number of shared dets for two tracks
};
#endif
