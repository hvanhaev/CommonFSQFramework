# based on https://root.cern.ch/phpBB3/viewtopic.php?f=3&t=1147

#   Example of a fitting program
#   ============================
#
#   The fitting function fcn is a simple chisquare function
#   The data consists of 5 data points (arrays x,y,z) + the errors in errorsz
#   More details on the various functions or parameters for these functions
#   can be obtained in an interactive ROOT session with:
#    Root > TMinuit *minuit = new TMinuit(10);
#    Root > minuit->mnhelp("*",0)  to see the list of possible keywords
#    Root > minuit->mnhelp("SET",0) explains most parameters


import ROOT
import sys
ROOT.gROOT.SetBatch(True)
from array import array;

Error = 0;
z = array( 'f', ( 1., 0.96, 0.89, 0.85, 0.78 ) )
errorz = array( 'f', 5*[0.01] )

x = array( 'f', ( 1.5751, 1.5825,  1.6069,  1.6339,   1.6706  ) )
y = array( 'f', ( 1.0642, 0.97685, 1.13168, 1.128654, 1.44016 ) )

ncount = 0

##______________________________________________________________________________
def testfit():

   gMinuit = ROOT.TMinuit(5)
   gMinuit.SetFCN( fcn )

   arglist = array( 'd', 10*[0.] )
   ierflg = ROOT.Long(1982)

   arglist[0] = 1
   gMinuit.mnexcm( "SET ERR", arglist, 1, ierflg )

 # Set starting values and step sizes for parameters
   vstart = array( 'd', ( 3,  1,  0.1,  0.01  ) )
   step   = array( 'd', ( 0.1, 0.1, 0.01, 0.001 ) )
   gMinuit.mnparm( 0, "a1", vstart[0], step[0], 0, 0, ierflg )
   gMinuit.mnparm( 1, "a2", vstart[1], step[1], 0, 0, ierflg )
   gMinuit.mnparm( 2, "a3", vstart[2], step[2], 0, 0, ierflg )
   gMinuit.mnparm( 3, "a4", vstart[3], step[3], 0, 0, ierflg )

 # Now ready for minimization step
   arglist[0] = 500 # max calls 
   arglist[1] = 1.  # tolerance - how far from minimum
   gMinuit.mnexcm( "MIGRAD", arglist, 2, ierflg )

 # Print results
   amin, edm, errdef = ROOT.Double(0.18), ROOT.Double(0.19), ROOT.Double(0.20)
   nvpar, nparx, icstat = ROOT.Long(1983), ROOT.Long(1984), ROOT.Long(1985)
   print "AAA" 
   sys.stdout.flush()
   gMinuit.mnstat( amin, edm, errdef, nvpar, nparx, icstat )
    
   print "VVV" 
   sys.stdout.flush()
   gMinuit.mnprin( 3, amin )
   print amin
   for i in xrange(4):
        val = ROOT.Double(0)
        err = ROOT.Double(0)
        gMinuit.GetParameter(i, val, err)

        print "res", i, val, err



##______________________________________________________________________________
# 
# 
# f - return value
# par - parameters
#
def fcn( npar, gin, f, par, iflag ):
   global ncount
   nbins = 5

 # calculate chisquare
   chisq, delta = 0., 0.
   for i in range(nbins):
      delta  = (z[i]-func(x[i],y[i],par))/errorz[i]
      chisq += delta*delta

   f[0] = chisq
   ncount += 1

def func( x, y, par ):
   value = ( (par[0]*par[0])/(x*x)-1)/ ( par[1]+par[2]*y-par[3]*y*y)
   return value


##______________________________________________________________________________
if __name__ == '__main__':
   testfit()

