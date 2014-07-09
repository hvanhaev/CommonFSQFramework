#include "FWCore/ParameterSet/interface/FileInPath.h"
#include "TH1.h"
#include "TFile.h"
#include <cmath>
#include <string>
#include <boost/shared_ptr.hpp>
#include <vector>
#define constexpr static const
#include "PhysicsTools/Utilities/interface/LumiReWeighting.h"
#include "MNTriggerStudies/MNTriggerAna/interface/TestTrackData.h"


namespace {
  struct dictionary {
    edm::FileInPath v1;
    edm::LumiReWeighting v2;

    tmf::TestTrackData v3;
    std::vector<tmf::TestTrackData> v4;

  };
}

