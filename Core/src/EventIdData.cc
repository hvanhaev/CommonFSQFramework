#include "CommonFSQFramework/Core/interface/EventIdData.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "SimDataFormats/GeneratorProducts/interface/GenEventInfoProduct.h"
#include "SimDataFormats/GeneratorProducts/interface/HepMCProduct.h"
#include "SimDataFormats/PileupSummaryInfo/interface/PileupSummaryInfo.h"
#include "DataFormats/Luminosity/interface/LumiSummary.h"
#include "DataFormats/Luminosity/interface/LumiDetails.h"
#include "DataFormats/Scalers/interface/LumiScalers.h"
#include "SimDataFormats/Vertex/interface/SimVertexContainer.h"
#include "TLorentzVector.h"

EventIdData::EventIdData(const edm::ParameterSet& iConfig, TTree * tree, edm::ConsumesCollector && iC):
EventViewBase(iConfig, tree)
{

    // register data access
    iC.consumes< GenEventInfoProduct >(edm::InputTag("generator"));
    iC.consumes< reco::GenParticleCollection >(edm::InputTag("genParticles"));
    iC.consumes< edm::SimVertexContainer >(edm::InputTag("g4SimHits"));
    iC.consumes< std::vector<PileupSummaryInfo> >(edm::InputTag("addPileupInfo"));
    iC.consumes< std::vector<LumiScalers> >(edm::InputTag("scalersRawToDigi"));

    // register branches
    registerInt("run", tree);
    registerInt("lumi", tree);
    registerInt("event", tree);
    registerInt("bx",tree);
    
    registerFloat("genWeight", tree);
    registerFloat("alphaQCD", tree);
    registerFloat("qScale", tree);
    
    registerInt("processID", tree);
    registerFloat("Xix", tree);
    registerFloat("Xiy", tree);
    registerFloat("XiSD", tree);
    registerFloat("XiDD", tree);
    registerFloat("cmenergy", tree);
    
    registerFloat("instLumiPerBX",tree);
    registerFloat("puTrueNumInteractions", tree);
    registerFloat("PUNumInteractions", tree);
    
    registerFloat("simvtxx",tree);
    registerFloat("simvtxy",tree);
    registerFloat("simvtxz",tree);

    localcount = 0;

}


void EventIdData::fillSpecific(const edm::Event& iEvent, const edm::EventSetup& iSetup){

    localcount++;

    // common part
    setI("run", iEvent.eventAuxiliary().run());
    setI("lumi", iEvent.eventAuxiliary().luminosityBlock());
    setI("event", iEvent.eventAuxiliary().event());
    
    // data only part
    if (iEvent.isRealData()) {
    	setI("bx", iEvent.bunchCrossing());
	try {
	    // Get instantanious lumi information
	    edm::Handle<LumiScalersCollection> lumiScalers;
	    iEvent.getByLabel("scalersRawToDigi",lumiScalers);	
	    // This is the call to get the lumi per bx:
	    if (lumiScalers->size() != 0) {
	    	LumiScalersCollection::const_iterator it = lumiScalers->begin();
	    	setF("instLumiPerBX",it->instantLumi());
	    }
	} catch (...) {
	    if (localcount == 1) std::cout << " An exception was thrown when accessing the LumiDetails and/or the LumiSummary objects. This means they are not present and are not correctly filled in the ntuple" << std::endl;
	}
    }


    // start MC part
    if (iEvent.isRealData()) return;

    // MC only stuff below
    edm::Handle<GenEventInfoProduct> hGW; 
    iEvent.getByLabel(edm::InputTag("generator"), hGW);
    setF("genWeight", hGW->weight());
    setF("alphaQCD", hGW->alphaQCD());
    setF("qScale", hGW->qScale());
    setI("processID",hGW->signalProcessID());
    
   /* // calculate the Xi's of the event
    double xix = 100;
    double xiy = 100;
    double xisd = 100;
    double xidd = 10e10;
    
    // get the GenParticles information
    edm::Handle<reco::GenParticleCollection> genParticles;
    iEvent.getByLabel("prunedGenParticles", genParticles);
    
    std::vector<TLorentzVector> myTempParticles;
    std::vector<TLorentzVector> myRapiditySortedParticles;
    
    // copy only final state particles from the genParticles collection
    double cmenergy = 0.0;
    int bpcnt = 0;
    for(reco::GenParticleCollection::const_iterator p = genParticles->begin(); p != genParticles->end(); ++ p) {
    	if (p->px() == 0.0 && p->py() == 0.0 && abs(p->pz()) > 0.0 && p->pdgId() == 2212) {
		// add pz of beam particles to get cmenergy, only add two!
		bpcnt++;
		if (bpcnt < 3) cmenergy += abs(p->pz());
	}	
    	if (p->status() != 1) continue;
	TLorentzVector vp;
	vp.SetPxPyPzE(p->px(),p->py(),p->pz(),p->energy());
    	myTempParticles.push_back(vp);
    }
    // save the centre of mass energy in the tree - so one can cross check its value
    setF("cmenergy",cmenergy);
    		
    // sort genParticles in y, from y_min to y_max
    while (myTempParticles.size() != 0) {
    	double min_y = 10000;
	int min_y_pos = -1;
	for (unsigned int ipart = 0;ipart<myTempParticles.size();ipart++) {
		if (myTempParticles[ipart].Rapidity() < min_y) {
			min_y = myTempParticles[ipart].Rapidity();
			min_y_pos = ipart;
		}
	}
	myRapiditySortedParticles.push_back(myTempParticles[min_y_pos]);
	myTempParticles.erase(myTempParticles.begin()+min_y_pos);
    }
			
    // find deltaymax
    double deltaymax = 0;
    int deltaymax_pos = -1;
    for (unsigned int ipart=0;ipart<myRapiditySortedParticles.size()-1;ipart++) {
    	double deltay = myRapiditySortedParticles[ipart+1].Rapidity() - myRapiditySortedParticles[ipart].Rapidity();
	if (deltay > deltaymax) {
		deltaymax = deltay;
		deltaymax_pos = ipart;
	}
    }
			
    // calculate Mx2 and My2
    long double XEtot = 0;
    long double XPxtot = 0;
    long double XPytot = 0;
    long double XPztot = 0;
    long double YEtot = 0;
    long double YPxtot = 0;
    long double YPytot = 0;
    long double YPztot = 0;
			
    for (int ipart=0;ipart<=deltaymax_pos;ipart++) {
    	XEtot += myRapiditySortedParticles[ipart].E();
	XPxtot += myRapiditySortedParticles[ipart].Px();
	XPytot += myRapiditySortedParticles[ipart].Py();
	XPztot += myRapiditySortedParticles[ipart].Pz();
    }
    long double Mx2 = -1.;
    Mx2 = XEtot*XEtot - XPxtot*XPxtot - XPytot*XPytot - XPztot*XPztot;
			
    for (unsigned int ipart=deltaymax_pos+1;ipart<myRapiditySortedParticles.size();ipart++) {
    	YEtot += myRapiditySortedParticles[ipart].E();
	YPxtot += myRapiditySortedParticles[ipart].Px();
	YPytot += myRapiditySortedParticles[ipart].Py();
	YPztot += myRapiditySortedParticles[ipart].Pz();
    }
    long double My2 = -1.;
    My2 = YEtot*YEtot - YPxtot*YPxtot - YPytot*YPytot - YPztot*YPztot;
			    
    // set Mx2, My2 to zero if negative (i.e. the X,Y system is a photon)
    if (Mx2 < 0) Mx2 = 0;
    if (My2 < 0) My2 = 0;
    			
    // calculate xix and xiy
    if (cmenergy > 0) xix = Mx2/(cmenergy*cmenergy);
    if (cmenergy > 0) xiy = My2/(cmenergy*cmenergy);
			
    // xisd and xidd
    xisd = std::max(xix,xiy);
    if (cmenergy > 0) xidd = xix*xiy*cmenergy*cmenergy/(0.938*0.938);
    
    // fill tree
    setF("Xix",xix);
    setF("Xiy",xiy);
    setF("XiSD",xisd);
    setF("XiDD",xidd);*/
    
    // pile-up stuff

    try {
    	edm::Handle< std::vector<PileupSummaryInfo> > hPU;
    	iEvent.getByLabel(edm::InputTag("addPileupInfo"), hPU);
    	for (unsigned int i = 0; i< hPU->size();++i){
        	/*
        	std::cout << hPU->at(i).getBunchCrossing() 
                  << " " << hPU->at(i).getTrueNumInteractions() 
                  << " " << hPU->at(i).getPU_NumInteractions() << std::endl;
        	*/
        	if (hPU->at(i).getBunchCrossing() == 0) {
            		setF("puTrueNumInteractions",  hPU->at(i).getTrueNumInteractions());
            		setF("PUNumInteractions",  hPU->at(i).getPU_NumInteractions());
            		break;
        	}
    	}
    } catch (...) {
    	if (localcount == 1) std::cout << " An exception was thrown when accessing the PileupSummaryInfo object. This means we are probably running on GEN-SIM samples that do not have this information." << std::endl;
    }
    
    
    // get the first (primary?) simulated vertex from Geant4
    /*edm::Handle<edm::SimVertexContainer> simVertexCollection;
    iEvent.getByLabel("g4SimHits", simVertexCollection);
    const SimVertex simPVh = *(simVertexCollection->begin());
    setF("simvtxx",simPVh.position().x());
    setF("simvtxy",simPVh.position().y());
    setF("simvtxz",simPVh.position().z());*/

}
