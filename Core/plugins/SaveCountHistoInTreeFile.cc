// -*- C++ -*-
//
// Package:    SaveCountHistoInTreeFile
// Class:      SaveCountHistoInTreeFile
// 
/**\class SaveCountHistoInTreeFile SaveCountHistoInTreeFile.cc MNTriggerStudies/SaveCountHistoInTreeFile/plugins/SaveCountHistoInTreeFile.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Tomasz Fruboes
//         Created:  Fri, 11 Apr 2014 08:34:20 GMT
// $Id$
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/LuminosityBlock.h"


#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "DataFormats/Common/interface/MergeableCounter.h"
#include "TH1D.h"
//
// class declaration
//

class SaveCountHistoInTreeFile : public edm::EDAnalyzer {
   public:
      explicit SaveCountHistoInTreeFile(const edm::ParameterSet&);
      ~SaveCountHistoInTreeFile();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);


   private:
      virtual void beginJob();
      virtual void analyze(const edm::Event&, const edm::EventSetup&);
      virtual void endJob();

      //virtual void beginRun(edm::Run const&, edm::EventSetup const&) override;
      //virtual void endRun(edm::Run const&, edm::EventSetup const&) override;
      //virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;
      virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);

      // ----------member data ---------------------------
        TH1D * m_cntHisto;
        int m_evCnt;
        int m_evCntSeenByTreeProducers;


};

//
// constants, enums and typedefs
//

//
// static data member definitions
//

//
// constructors and destructor
//
SaveCountHistoInTreeFile::SaveCountHistoInTreeFile(const edm::ParameterSet& iConfig):
m_evCnt(0),
m_evCntSeenByTreeProducers(0)
{
   //now do what ever initialization is needed
    edm::Service<TFileService> tFileService;
    m_cntHisto = tFileService->make<TH1D>("cntHisto", "cntHisto", 10, -0.5, 9.5);
    m_cntHisto->GetXaxis()->SetBinLabel(1, "this should be equal to one, consult doc if otherwise");
    m_cntHisto->SetBinContent(1, 1);
    m_cntHisto->SetBinError(1, 0);

    m_cntHisto->GetXaxis()->SetBinLabel(2, "XS"); 
    m_cntHisto->GetXaxis()->SetBinLabel(3, "evCnt");
    m_cntHisto->GetXaxis()->SetBinLabel(4, "evCntSeenByTreeProducers");

}


SaveCountHistoInTreeFile::~SaveCountHistoInTreeFile()
{
    m_cntHisto->SetBinContent(3, m_evCnt);
    m_cntHisto->SetBinContent(4, m_evCntSeenByTreeProducers);
}


//
// member functions
//

// ------------ method called for each event  ------------
void
SaveCountHistoInTreeFile::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
    using namespace edm;
    m_evCntSeenByTreeProducers += 1;

    static bool runOnce = true;
    if (runOnce){
        runOnce = false;
        Handle<double> pIn;
        iEvent.getByLabel("XS",pIn);
        m_cntHisto->SetBinContent(2, *pIn); // dataset specific, fetch only once
        m_cntHisto->SetBinError(2, 0);
    }

   
}


// ------------ method called once each job just before starting event loop  ------------
void 
SaveCountHistoInTreeFile::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
SaveCountHistoInTreeFile::endJob() 
{
}

// ------------ method called when starting to processes a run  ------------
/*
void 
SaveCountHistoInTreeFile::beginRun(edm::Run const&, edm::EventSetup const&)
{
}
*/

// ------------ method called when ending the processing of a run  ------------
/*
void 
SaveCountHistoInTreeFile::endRun(edm::Run const&, edm::EventSetup const&)
{
}
*/

// ------------ method called when starting to processes a luminosity block  ------------
/*
void 
SaveCountHistoInTreeFile::beginLuminosityBlock(edm::LuminosityBlock const& lumi, edm::EventSetup const&)
{


}
*/

// ------------ method called when ending the processing of a luminosity block  ------------
void 
SaveCountHistoInTreeFile::endLuminosityBlock(edm::LuminosityBlock const& lumi, edm::EventSetup const&)
{
    edm::Handle<edm::MergeableCounter> hCnt;
    lumi.getByLabel("initialCntr", hCnt);
    double val = hCnt->value;
    std::cout << "LumiCnt " <<  val << std::endl;
    m_evCnt += val;
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
SaveCountHistoInTreeFile::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(SaveCountHistoInTreeFile);
