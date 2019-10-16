#!/usr/bin/python2.7

import sys
import numpy as np
import os


def print_limits( name, data, mass_indices, pu_indices ):
    """
       Print the distribution limits of the Pu+Am241 initial sampling isotopic weights
           name          Code name
           data          np.array containing the raw data
           mass_indices  Column indices of the Pu and Am total mass at BOC (normalization)
           pu_indices    Column indices of the Pu isotopic vector at BOC (238,239,240,241,242,241)
  
       The limits are estimated as:
           lim_inf[iso] =  100 * MIN( mass[iso]/(mass[Pu]+mass[Am]) )
           lim_sup[iso] =  100 * MAX( mass[iso]/(mass[Pu]+mass[Am]) )
    """
       
    if mass_indices == None:
        initial_mass = np.ones( len(a) )
    else:
       initial_mass = np.sum( a[:,mass_indices],axis=1 ) 
  
    pu = 100.*data[:,pu_indices]/initial_mass[:,None]
    am241 = 100.-np.sum( pu, axis=1 )
  
    fraction = np.c_[pu,am241]
    isotopes = [ 'Pu238', 'Pu239', 'Pu240', 'Pu241', 'Pu242', 'Am241' ]
  
    for i, iso in enumerate(isotopes):
        lmin = int( round( np.min(fraction[:,i]) ) )
        lmax = int( round( np.max(fraction[:,i]) ) )
        print '{0:s} {1:10s} [{2:3d},{3:3d}]'.format( iso, name, lmin, lmax ) 
    print



path='./'

a = np.loadtxt(path+'DOE/doe.txt')
print_limits( 'DOE', a, None, [0,1,2,3,4] )

a = np.loadtxt(path+'ANICCA_SCK/PWR_MOX_FF_BOC.dat') 
print_limits( 'anicca', a, [2,3], [6,7,8,9,10] )

a = np.loadtxt(path+'CLASS_CNRS_PWR/PWR_MOX_FF.dat')
print_limits( 'class_pwr', a, [5], [13,15,17,19,21] )


a = np.loadtxt(path+'CLASS_CNRS_RNR/RawData.dat', dtype='string')
a = a[ np.logical_and( a[:,1] == "FF", a[:,2] == "BOC") ][:,3:].astype(np.float)
print_limits( 'class_rnr', a, [2], [6,7,8,9,10] )


a = np.loadtxt(path+'CYCLUS_UWM/eq.csv', delimiter=',')
print_limits( 'cyclus', a, None, [1,2,3,4,5] )


a = np.loadtxt(path+'DYMOND_PWR_MOX/DYMOND_PWR_FF_BOC.csv', delimiter=',',skiprows=1)
print_limits( 'dymond_pwr', a, [3,4], [6,7,8,9,10] )


a = np.loadtxt(path+'DYMOND_SFR_V2B/DYMOND_SFR_V2B_FF_BOC.csv', delimiter=',',skiprows=1)
print_limits( 'dymond_sfr', a, [3,4], [6,7,8,9,10] )


a = np.loadtxt(path+'JOSETTE_BME/FF_BOC.txt')
print_limits( 'josette', a, [3,4], [7,8,9,10,11] )


a = np.loadtxt(path+'TREVOL_CIEMAT/MOX_raw.txt')
print_limits( 'trevol', a, [3,4], [6,7,8,9,10] )
