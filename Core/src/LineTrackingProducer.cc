#include "../interface/LineTrackingProducer.h"

#include "../interface/Seeding.h"
#include "../interface/Tracking.h"
#include "../interface/LineFitter.h"
#include "../interface/VertexFinder.h"
#include "../interface/VertexFitter.h"

#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <cmath>
#include <vector>
#include <algorithm>

#include "TVectorD.h"

using namespace std;

#define sqr(x) ((x) * (x))

/*****************************************************************************/
LineTrackingProducer::LineTrackingProducer
 (bool usePixelHits_, double  beamSpotX, double beamSpotY) : usePixelHits(usePixelHits_)
{

  maxAbsoluteZ0       = 20.;

  if(usePixelHits)
  {
    dMaxForVertexFinder = 50.;

    maxClusterWidthDiff = 5;
    maxAngle     = 0.02;
    minAngle     = 0.01;

    nRounds = 1;
  }
  else
  {
    dMaxForVertexFinder = 50.;
 
    maxClusterWidthDiff = 2;
    maxFirstHitRadius   = 31.;
    maxSharedDets       = 3;

    nRounds = 2;
  }

/*
  // read masks
  ifstream file;
  file.open("data/diffids.dat");
  while(!file.eof())
  {
    string type, s;
    unsigned long int id;
    int n;

    file >> type >> s >> s >> s;
    file >> hex >> id;
    file >> dec >> n;

    if(!file.eof()) {
        if( ( usePixelHits && type == "pixel") ||
            (!usePixelHits && type == "strip") ) {
            mask.push_back(id);
        }
    }
  }
  file.close();
*/
  sort(mask.begin(), mask.end());


  if(usePixelHits)
    theSeeding = new Seeding(maxAngle);

  // beam spot
  beam_x = beamSpotX;
  beam_y = beamSpotY;

}

/*****************************************************************************/
LineTrackingProducer::~LineTrackingProducer()
{
  if(usePixelHits)
    delete theSeeding;
}

/*****************************************************************************/
int LineTrackingProducer::readHits(std::vector<RawPixelRecHit> RawPixelRecHits,
                                   vector<LineFit> & simLines)
{
    int i=0;
    for(std::vector<RawPixelRecHit>::iterator RecHit = RawPixelRecHits.begin(); RecHit != RawPixelRecHits.end(); ++RecHit){

        // wrt beam
        double x = RecHit->x - beam_x;
        double y = RecHit->y - beam_y;
        double z = RecHit->z;

        //int nx = RecHit->nx;
        int ny = RecHit->ny;
        unsigned long id = RecHit->id;
        int sub = ((id >> 25) & 0x7);

        double r = sqrt(sqr(x) + sqr(y));

        if(usePixelHits)
        if(sub == 2 ||                                   // all PXF
           fabs(ny - 2*fabs(z/r)) < maxClusterWidthDiff) // selected PXB
        if(find(mask.begin(), mask.end(), id) == mask.end())
        {
          TVector3 hit(x,y,z);
          points.push_back(hit);
        }
    }
  return i; // return number of processed RecHits
}

/*****************************************************************************/
int LineTrackingProducer::readHits(std::vector<RawStripRecHit> RawStripRecHits,
                                   vector<LineFit> & simLines)
{
    int i=0;
    for(std::vector<RawStripRecHit>::iterator RecHit = RawStripRecHits.begin(); RecHit != RawStripRecHits.end(); ++RecHit){

        // wrt beam
        double x = RecHit->x - beam_x;
        double y = RecHit->y - beam_y;
        double z = RecHit->z;

        int monoSize = RecHit->monoSize;
        int stereoSize = RecHit->stereoSize;
        unsigned long monoId = RecHit->monoId;
        unsigned long stereoId = RecHit->stereoId;

        if( !usePixelHits )
        if(abs(monoSize-stereoSize) <= maxClusterWidthDiff) // check clusters
        if(find(mask.begin(), mask.end(), monoId) == mask.end()) // not in 
        if(find(mask.begin(), mask.end(), stereoId) == mask.end()) // not in
        {
          TVector3 hit(x,y,z);
          points.push_back(hit);
          detids.push_back(pair<unsigned long int, unsigned long int>(monoId,stereoId));
        }
    }
  return i; // return number of processed RecHits
}

/*****************************************************************************/
void LineTrackingProducer::cleanTracks(vector<LineTrack> & tracks)
{
  if(usePixelHits)
  { // pixels
    // track cleaning based on angle between unit vectors
    for(vector<LineTrack>::iterator track1 = tracks.begin();
                                    track1!= tracks.end(); )
    {
      LineFit & f1 = track1->pars;

      TVector3 u1(sin(f1.theta) * cos(f1.phi),
                  sin(f1.theta) * sin(f1.phi),
                  cos(f1.theta));

      bool erase1 = false;
  
      for(vector<LineTrack>::iterator track2 = track1 + 1;
                                               track2!= tracks.end(); )
      {
        LineFit & f2 = track2->pars;

        TVector3 u2(sin(f2.theta) * cos(f2.phi),
                    sin(f2.theta) * sin(f2.phi),
                    cos(f2.theta));

        double dAngle = acos(u1*u2);

        if(dAngle < minAngle)
        {
          // which to erase? the one with larger <d>
          if(f1.delta <= f2.delta)
            track2 = tracks.erase(track2);
          else
          { erase1 = true; break; } // go to outer loop
        }
        else
          track2++;
      }

      if(erase1)
        track1 = tracks.erase(track1);
      else
        track1++;
    }
  }
  else
  { // strips
    // track filtering based on number of shared detids
    for(vector<LineTrack>::iterator track1 = tracks.begin();
                                    track1!= tracks.end(); track1++)
    for(vector<LineTrack>::iterator track2 = track1 + 1;
                                    track2!= tracks.end(); )
    {
      int nshared = 0;
      for(vector<int>::const_iterator i1 = track1->hits.begin();
                                      i1!= track1->hits.end(); i1++)
      for(vector<int>::const_iterator i2 = track2->hits.begin();
                                      i2!= track2->hits.end(); i2++)
        if(detids[*i1] == detids[*i2])
          nshared++;

      if(nshared > maxSharedDets) // remove track2, anyway order is random
        track2 = tracks.erase(track2);
      else
        track2++;
    }
  }
}

/*****************************************************************************/
void LineTrackingProducer::findAndFitVertices
 (vector<LineTrack> & lines, vector<LineVertex> & vertices, int round)
{
  if(round >= 0)
  {
    // first round
    VertexFinder theVertexFinder(dMaxForVertexFinder);
    theVertexFinder.run(lines, vertices);
  }
  else
  {
    // strip-only, second round
    for(vector<LineTrack>::const_iterator line = lines.begin();
                                          line!= lines.end(); line++)
    {
      int iv = line->favoredVertex;

      vertices[iv].tracks.push_back(line - lines.begin()); 
    }
  }

  // clean vertices 
  if(vertices.size() > 0)
  {
    // look at all found vertices
    for(vector<LineVertex>::iterator vertex = vertices.begin();
                                     vertex!= vertices.end(); )
    if(vertices.size() == 1 || vertex->tracks.size() >= 3)
    {
      // look for beam spot, 3D vertex fit
      if(vertex->tracks.size() >= 3)
      {
        vector<LineFit> lineFits;
        for(vector<int>::const_iterator track = vertex->tracks.begin();
                                        track!= vertex->tracks.end();
                                        track++)
          lineFits.push_back(lines[*track].pars);
  
        VertexFitter theVertexFitter;
        vector<double> vtx(3);
        try {
          theVertexFitter.run(lineFits, vtx);
        }
        catch(...) {
          vtx[0] = vertex->x0;
          vtx[1] = vertex->y0;

        }

        vertex->x0 = vtx[0];
        vertex->y0 = vtx[1];
      }

      vertex++;
    }
    else
      vertex = vertices.erase(vertex);
  }

  for(vector<LineVertex>::const_iterator vertex = vertices.begin();
                                         vertex!= vertices.end(); vertex++)
  {
    for(vector<int>::const_iterator track = vertex->tracks.begin();
                                    track!= vertex->tracks.end(); track++)
    {
      LineFit p = lines[*track].pars;

      lines[*track].pars.eta = -log(tan(p.theta/2));

      p = lines[*track].pars;
    }
  }
}

/*****************************************************************************/
void LineTrackingProducer::sortByRadius(vector<int> & hits)
{
  int n = hits.size();

  do
  {
    int newn = 0;

    for(int i = 1; i <= n-1; i++)
    if(points[hits[i-1]].Perp2() > points[hits[i]].Perp2())
    {
      swap(hits[i-1],hits[i]);
      newn = i;
    }

    n = newn;
  }
  while(n > 0);
}

/*****************************************************************************/
// use points and detids
void LineTrackingProducer::processHits(vector<LineTrack> & lines,
                                       vector<LineVertex> & vertices)
{
  // for strip-only, list of vertices
  vector<double> z0(1, 0.);

  for(int round = 0; round < nRounds; round++)
  {
    // for strip-only
    double dMax;
    unsigned int minHits;
    if(round == 0) { dMax = 0.10; minHits = 3; }
              else { dMax = 0.05; minHits = 4; }

    // find lines
    if(usePixelHits){
      theSeeding->run(points, lines);
    }
    else
    {
      Tracking theTracking(dMax, z0);
      theTracking.run(points,detids, lines);

      for(vector<LineTrack>::iterator line = lines.begin();
                                      line!= lines.end(); )
      {
        sortByRadius(line->hits);

        if(line->hits.size() >= minHits &&
           points[line->hits[0]].Perp() < maxFirstHitRadius)
          line++;
        else
          line = lines.erase(line);
      }
    }

    // fit lines to a straight line model
    LineFitter theLineFitter;
    for(vector<LineTrack>::iterator line = lines.begin();
                                    line!= lines.end(); )
    {
      vector<TVector3> ps;
      for(vector<int>::const_iterator hit = line->hits.begin();
                                      hit!= line->hits.end(); hit++)
        ps.push_back(points[*hit]);

      try {
      line->parsFree = theLineFitter.fit(ps, false); // d0 free
      }
      catch (...) {
      }

      bool fitFailure = false;
      try {
      line->pars     = theLineFitter.fit(ps, true ); // d0 = 0 fix
      }
      catch (int i) {
      fitFailure = true;
      }
          
      //double eta = -log(tan(line->pars.theta/2));

      if(fabs(line->pars.z0) > maxAbsoluteZ0  || fitFailure)//|| (!usePixelHits && fabs(eta) > 1 && line->hits.size() <= minHits + 1) || fitFailure)
        line = lines.erase(line);
      else
        line++;
    }
    // clean tracks
    cleanTracks(lines);

    // find and fit vertices, and get vertex z
    if(round >= 0) // fIXME
      vertices.clear();
    else
      for(vector<LineVertex>::iterator vertex = vertices.begin();
                                       vertex!= vertices.end(); vertex++)
        vertex->tracks.clear();

    if(lines.size() > 0)
      findAndFitVertices(lines, vertices, round);

    if(vertices.size() > 0) // only if vertices found, otherwise keep z0 = 0
    {
      z0.clear();

      for(vector<LineVertex>::const_iterator vertex = vertices.begin();
                                             vertex!= vertices.end(); vertex++)
      {
        z0.push_back(vertex->z0);
      }
    }
  }
}
/*****************************************************************************/
void LineTrackingProducer::saveResults(vector<LineTrack> & lines, vector<LineVertex> & vertices)
{
      linesResult = lines;
      verticesResult = vertices;
}

/*****************************************************************************/
bool LineTrackingProducer::run(std::vector<RawPixelRecHit> RawPixelRecHits)
{
  // clear
  points.clear();
  detids.clear();

  // read hits
  vector<LineFit> simLines;
  readHits(RawPixelRecHits, simLines);

  // do track finding and fitting, vertex finding and fitting
  vector<LineTrack> lines;
  vector<LineVertex> vertices;

  if(points.size() > 0) {
    processHits(lines, vertices);
  }
  saveResults(lines, vertices);

  return true;
}

/*****************************************************************************/
bool LineTrackingProducer::run(std::vector<RawStripRecHit> RawStripRecHits)
{
  // clear
  points.clear();
  detids.clear();

  // read hits
  vector<LineFit> simLines;
  readHits(RawStripRecHits, simLines);

  // do track finding and fitting, vertex finding and fitting
  vector<LineTrack> lines;
  vector<LineVertex> vertices;

  if(points.size() > 0) {
    processHits(lines, vertices);
  }
  saveResults(lines, vertices);

  return true;
}

/*****************************************************************************/
int LineTrackingProducer::getVertices(std::vector<double> & VerticesX, std::vector<double> & VerticesY, std::vector<double> & VerticesZ, std::vector<int> & nTracks)
{
   for(vector<LineVertex>::const_iterator vertex = verticesResult.begin();
                                             vertex!= verticesResult.end(); vertex++) {
        VerticesX.push_back(vertex->x0);
        VerticesY.push_back(vertex->y0);
        VerticesZ.push_back(vertex->z0);
        nTracks.push_back(vertex->tracks.size());
  }
  return verticesResult.size();
}

int LineTrackingProducer::getTracks(std::vector<double> & TracksTheta, std::vector<double> & TracksPhi, std::vector<double> & TracksZ0, std::vector<double> & TracksD0, std::vector<double> & TracksSigmaZ, std::vector<int> & TracksiVertex)
{
   for(vector<LineTrack>::const_iterator line = linesResult.begin();
                                             line!= linesResult.end(); line++) {
        TracksTheta.push_back(line->parsFree.theta);
        TracksPhi.push_back(line->parsFree.phi);
        TracksD0.push_back(line->parsFree.d0);
        TracksZ0.push_back(line->parsFree.z0);
        TracksSigmaZ.push_back(line->parsFree.sigma_z);

        int vertexCheck = -1;
        int iVertex = 0;
        // loop over vertices
        for(vector<LineVertex>::const_iterator vertex = verticesResult.begin();
                                               vertex!= verticesResult.end(); vertex++) {

          // loop over tracks in vertices
          for(std::vector<int>::const_iterator ivtx_trk = vertex->tracks.begin(); 
                                               ivtx_trk!= vertex->tracks.end(); ivtx_trk++) {

            // check if vertex track id is same as stand alone track id
            if ((line-linesResult.begin()) == *ivtx_trk) {
              // if a track belongs to more than one vertex give error message
              if (vertexCheck>=0) {
                std::cerr << "LineTrackingProducer: ERROR. Track is part of several vertices!!" << std::endl;
              }
              vertexCheck = iVertex;  
            }
          } // loop over tracks in vertices
          iVertex++;
        } // loop over vertices

        TracksiVertex.push_back(vertexCheck);
  }
  return linesResult.size();
}

