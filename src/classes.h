#include "FWCore/ParameterSet/interface/FileInPath.h"
#include "TH1.h"
#include "TFile.h"
#include <cmath>
#include <string>
#include <boost/shared_ptr.hpp>
#include <vector>
#define constexpr static
#include "PhysicsTools/Utilities/interface/LumiReWeighting.h"


namespace {
  struct dictionary {
    edm::FileInPath v1;
    edm::LumiReWeighting v2;


  };
}

