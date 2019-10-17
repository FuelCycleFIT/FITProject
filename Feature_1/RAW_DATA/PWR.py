#######################################################################
# 
# Libraries and plotting options
# 
#######################################################################

import matplotlib.pyplot as plt
import numpy as np

np.set_printoptions(precision=6)
plt.style.use('seaborn-white')

from sklearn.linear_model import LinearRegression


SMALL_SIZE = 14
MEDIUM_SIZE = SMALL_SIZE +2
BIGGER_SIZE = MEDIUM_SIZE +2

plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title

#######################################################################
# 
# Codes to plot
# 
#######################################################################

codes = ['ANICCA', 'CLASS', 'COSI6', 'CYCLUS', 'DYMOND', 'ORION', 'TrEvol']

#######################################################################
# 
# Reactor descriptions
# 
#######################################################################

# CLASS
#### Reactor
#    - 17x17 infinite assembly
#    - Neural network prediction of the k$_{inf}$
#    - k$_{threshold}$ is 1.034
#    - Heavy mass: 72 tons
#    - Thermal power: 3 GWth
#    - Loading factor: 75%
#    - Irradiation time: 3 years that correspond to a burn-up closed to 34 GWd/t
#### FLM
#    - 17x17 infinite assembly
#    - Neural network prediction of the k$_{inf}$
#    - k$_{threshold}$ is 1.034

# Tr_Evol
#### Reactor
#    - Thermal_power_(GW) : 3.0
#    - Electrical_power_(GW) : 1.0
#    - Load_factor : 0.9
#    - Core_mass_(tHM) : 72.0
#    - Burn_up_(GWd/tHM) : 41
#### FLM
#    - Baker \& Ross

# ANICCA
#### Reactor
#    - Fuel Heavy Mass: 22.2908 t / year  from 1 GW*0.85*365.25/41 GWd/t
#    - BU : 41 GWd/t (this one from the reference library, so I set this like a reference for all simulations to calculate the annual loading masses)
#    - Load Factor : 85% (I changed this to be more representative)
#    - Electric Power : 1.02 GWth
#    - Thermal Power : 3 GWth
#    - Cycle Time : 1390 EFPD
#    - Core Mass : 101.7 tHM (1390*3/41… right?)
#### FLM
#    - Baker \& Ross
 
# CYCLUS
#### Reactor
#    - Heavy mass: 72 tons
#    - Thermal power: 2.7 GWth
#    - Loading factor: 100%
#    - BurnUp: 41.09 GWd/t
#### FLM
#    - Baker \& Ross

# DYMOND

# COSI

#######################################################################
# 
# Loading Data Functions => Add one function for any new data set
# 
#######################################################################

# CLASS
def load_class_pwr_data(fml_file = 'CLASS_CNRS_PWR/PWR_MOX_FLM.dat',  ff_file = 'CLASS_CNRS_PWR/PWR_MOX_FF.dat'):
    M_CLASS_FLM = np.loadtxt(fml_file)
    M_CLASS_FF = np.loadtxt(ff_file)
    
    total_mass = 72
    M_CLASS_FLM_BOC_FPu = M_CLASS_FLM[:,5]/total_mass
    M_CLASS_FLM_EOC_FPu = M_CLASS_FLM[:,6]/total_mass
        
    M_CLASS_FF_BOC_FPu = M_CLASS_FF[:,5]/total_mass
    M_CLASS_FF_EOC_FPu = M_CLASS_FF[:,6]/total_mass
    
    a1 = M_CLASS_FLM[:, [13, 15, 17, 19, 21, 7]]
    a2 = M_CLASS_FF[:, [13, 15, 17, 19, 21, 7]]

    M_CLASS_FLM_BOC_PuDOE = a1/np.sum(a1,axis=1,keepdims=True)
    M_CLASS_FF_BOC_PuDOE =  a2/np.sum(a2,axis=1,keepdims=True)

    return M_CLASS_FLM_BOC_FPu, M_CLASS_FLM_EOC_FPu, M_CLASS_FF_BOC_FPu, M_CLASS_FF_EOC_FPu, M_CLASS_FLM_BOC_PuDOE, M_CLASS_FF_BOC_PuDOE

# ANICCA
def load_anica_pwr_data(fml_file = 'ANICCA_SCK/PWR_MOX_FLM',  ff_file = 'ANICCA_SCK/PWR_MOX_FF'):

    M_ANICCA_FLM_BOC = np.loadtxt( fml_file + '_BOC.dat')
    M_ANICCA_FLM_EOC = np.loadtxt( fml_file + '_EOC.dat')
    M_ANICCA_FF_BOC = np.loadtxt( ff_file + '_BOC.dat')
    M_ANICCA_FF_EOC = np.loadtxt( ff_file + '_EOC.dat')

    M_ANICCA_FLM_BOC_FPu = M_ANICCA_FLM_BOC[:,2]
    M_ANICCA_FLM_EOC_FPu = M_ANICCA_FLM_EOC[:,2]

    M_ANICCA_FF_BOC_FPu = M_ANICCA_FF_BOC[:,2]
    M_ANICCA_FF_EOC_FPu = M_ANICCA_FF_EOC[:,2]
    
    a1 = M_ANICCA_FLM_BOC[:,[6,7,8,9,10,3]]
    a2 = M_ANICCA_FF_BOC[:,[6,7,8,9,10,3]]

    M_ANICCA_FLM_BOC_PuDOE = a1/np.sum(a1,axis=1,keepdims=True)
    M_ANICCA_FF_BOC_PuDOE =  a2/np.sum(a2,axis=1,keepdims=True)

    return M_ANICCA_FLM_BOC_FPu, M_ANICCA_FLM_EOC_FPu, M_ANICCA_FF_BOC_FPu, M_ANICCA_FF_EOC_FPu, M_ANICCA_FLM_BOC_PuDOE, M_ANICCA_FF_BOC_PuDOE

# TR_EVOL
def load_TrEvol_pwr_data(file = 'TREVOL_CIEMAT/MOX_raw.txt'):
   
    M_TrEvol = np.loadtxt(file)
    total_mass =  24

    M_TrEvol = M_TrEvol[(M_TrEvol[:,21] > 0.8*total_mass)]

    M_TrEvol_FLM_BOC_FPu = M_TrEvol[:,23] / total_mass
    M_TrEvol_FLM_EOC_FPu = M_TrEvol[:,33] / total_mass

    M_TrEvol_FF_BOC_FPu = M_TrEvol[:,3] / total_mass
    M_TrEvol_FF_EOC_FPu = M_TrEvol[:,13] / total_mass
    
    a1 = M_TrEvol[:,[26,27,28,29,30,24]]
    a2 = M_TrEvol[:,[26,27,28,29,30,24]]
    
    M_TrEvol_FLM_BOC_PuDOE = a1/np.sum(a1,axis=1,keepdims=True)
    M_TrEvol_FF_BOC_PuDOE =  a2/np.sum(a2,axis=1,keepdims=True)

    return M_TrEvol_FLM_BOC_FPu, M_TrEvol_FLM_EOC_FPu, M_TrEvol_FF_BOC_FPu, M_TrEvol_FF_EOC_FPu, M_TrEvol_FLM_BOC_PuDOE, M_TrEvol_FF_BOC_PuDOE

# CYCLUS
def load_cyclus_pwr_data(file = 'CYCLUS_UWM'):
        
    M_Cyclus_FLM = np.loadtxt(file + '/eq.csv', delimiter=',')
    M_Cyclus_FF = np.loadtxt(file + '/fix.csv', delimiter=',')

    M_Cyclus_FLM_BOC_FPu = M_Cyclus_FLM[:,13]
    M_Cyclus_FLM_EOC_FPu = M_Cyclus_FLM[:,14]

    M_Cyclus_FF_BOC_FPu = M_Cyclus_FF[:,13]
    M_Cyclus_FF_EOC_FPu = M_Cyclus_FF[:,14]

    a1 = M_Cyclus_FLM[:,[1,2,3,4,5,6]]
    a2 = M_Cyclus_FF[:,[1,2,3,4,5,6]]
    
    M_Cyclus_FLM_BOC_PuDOE = a1/np.sum(a1,axis=1,keepdims=True)
    M_Cyclus_FF_BOC_PuDOE =  a2/np.sum(a2,axis=1,keepdims=True)
    
    return M_Cyclus_FLM_BOC_FPu, M_Cyclus_FLM_EOC_FPu, M_Cyclus_FF_BOC_FPu, M_Cyclus_FF_EOC_FPu, M_Cyclus_FLM_BOC_PuDOE, M_Cyclus_FF_BOC_PuDOE

# ORION with EFMC
def load_efmc_pwr_data(file = 'ORION_ORNL'):
    
    M_efmc = np.loadtxt(file + '/PWR.txt', delimiter=' ')

    M_efmc_FLM_BOC_FPu = M_efmc[:,0]
    M_efmc_FLM_EOC_FPu = M_efmc[:,1]

    M_efmc_FF_BOC_FPu = np.ones(np.size(M_efmc[:,0]))
    M_efmc_FF_BOC_FPu *= 0.05634
    M_efmc_FF_EOC_FPu = M_efmc[:,2]

    a1 = M_efmc[:,[3,4,5,6,7,8]]
    a2 = M_efmc[:,[3,4,5,6,7,8]]
    
    M_efmc_FLM_BOC_PuDOE = a1/np.sum(a1,axis=1,keepdims=True)
    M_efmc_FF_BOC_PuDOE =  a2/np.sum(a2,axis=1,keepdims=True)
    
    return M_efmc_FLM_BOC_FPu, M_efmc_FLM_EOC_FPu, M_efmc_FF_BOC_FPu, M_efmc_FF_EOC_FPu, M_efmc_FLM_BOC_PuDOE, M_efmc_FF_BOC_PuDOE

# DYMOND
def load_dymond_pwr_data(file = 'DYMOND_PWR_MOX'):
        
    M_Dymond_FF_BOC = np.loadtxt(file + '/DYMOND_PWR_FF_BOC.csv', delimiter=',', skiprows =1)
    M_Dymond_FF_EOC = np.loadtxt(file + '/DYMOND_PWR_FF_EOC.csv', delimiter=',', skiprows =1)
    M_Dymond_FLM_BOC = np.loadtxt(file + '/DYMOND_PWR_FLM_BOC.csv', delimiter=',', skiprows =1)
    M_Dymond_FLM_EOC = np.loadtxt(file + '/DYMOND_PWR_FLM_EOC.csv', delimiter=',', skiprows =1)

    total_mass = 72
    M_Dymond_FLM_BOC_FPu = M_Dymond_FLM_BOC[:1000,3]/total_mass
    M_Dymond_FLM_EOC_FPu = M_Dymond_FLM_EOC[:1000,3]/total_mass

    M_Dymond_FF_BOC_FPu = M_Dymond_FF_BOC[:1000,3]/total_mass
    M_Dymond_FF_EOC_FPu = M_Dymond_FF_EOC[:1000,3]/total_mass

    a1 = M_Dymond_FLM_BOC[:1000,[6,7,8,9,10,11]]
    a2 = M_Dymond_FF_BOC[:1000,[6,7,8,9,10,11]]
    
    M_Dymond_FLM_BOC_PuDOE = a1/np.sum(a1,axis=1,keepdims=True)
    M_Dymond_FF_BOC_PuDOE =  a2/np.sum(a2,axis=1,keepdims=True)
            
    return M_Dymond_FLM_BOC_FPu, M_Dymond_FLM_EOC_FPu, M_Dymond_FF_BOC_FPu, M_Dymond_FF_EOC_FPu, M_Dymond_FLM_BOC_PuDOE, M_Dymond_FF_BOC_PuDOE

# COSI
def load_cosi6_pwr_data(fml_file = 'COSI6_PWR_MOX/COSI6_PWR_MOX_FLM.dat', ff_file = 'COSI6_PWR_MOX/COSI6_PWR_MOX_FF.dat'):
    M_COSI6_FLM = np.loadtxt(fml_file)
    M_COSI6_FF = np.loadtxt(ff_file)
    
    M_COSI6_FLM_BOC_FPu = M_COSI6_FLM[:,26]
    M_COSI6_FLM_EOC_FPu = M_COSI6_FLM[:,27]
    
    M_COSI6_FF_BOC_FPu = M_COSI6_FF[:,26]
    M_COSI6_FF_EOC_FPu = M_COSI6_FF[:,27]
    
    a1 = M_COSI6_FLM[:,[0,1,5,2,3,4]]
    a2 = M_COSI6_FF[:,[0,1,5,2,3,4]]
    
    M_COSI6_FLM_BOC_PuDOE = a1/np.sum(a1,axis=1,keepdims=True)
    M_COSI6_FF_BOC_PuDOE = a2/np.sum(a2,axis=1,keepdims=True)
    
    return M_COSI6_FLM_BOC_FPu, M_COSI6_FLM_EOC_FPu, M_COSI6_FF_BOC_FPu, M_COSI6_FF_EOC_FPu, M_COSI6_FLM_BOC_PuDOE, M_COSI6_FF_BOC_PuDOE

#######################################################################
# 
# Loading the data
# 
#######################################################################

M_FLM_BOC_FPu = {}
M_FLM_EOC_FPu = {}
M_FF_BOC_FPu = {}
M_FF_EOC_FPu = {}

M_FLM_BOC_PuDOE = {}
M_FF_BOC_PuDOE = {}

M_FLM_BOC_MUPu = {}

M_FLM_BOC_FPu['ANICCA'], M_FLM_EOC_FPu['ANICCA'], M_FF_BOC_FPu['ANICCA'], M_FF_EOC_FPu['ANICCA'], M_FLM_BOC_PuDOE['ANICCA'], M_FF_BOC_PuDOE['ANICCA'] = load_anica_pwr_data()
M_FLM_BOC_FPu['CLASS'], M_FLM_EOC_FPu['CLASS'], M_FF_BOC_FPu['CLASS'], M_FF_EOC_FPu['CLASS'], M_FLM_BOC_PuDOE['CLASS'], M_FF_BOC_PuDOE['CLASS'] = load_class_pwr_data()    
M_FLM_BOC_FPu['TrEvol'], M_FLM_EOC_FPu['TrEvol'], M_FF_BOC_FPu['TrEvol'], M_FF_EOC_FPu['TrEvol'], M_FLM_BOC_PuDOE['TrEvol'], M_FF_BOC_PuDOE['TrEvol'] = load_TrEvol_pwr_data()
M_FLM_BOC_FPu['CYCLUS'], M_FLM_EOC_FPu['CYCLUS'], M_FF_BOC_FPu['CYCLUS'], M_FF_EOC_FPu['CYCLUS'], M_FLM_BOC_PuDOE['CYCLUS'], M_FF_BOC_PuDOE['CYCLUS'] = load_cyclus_pwr_data()
M_FLM_BOC_FPu['ORION'], M_FLM_EOC_FPu['ORION'], M_FF_BOC_FPu['ORION'], M_FF_EOC_FPu['ORION'], M_FLM_BOC_PuDOE['ORION'], M_FF_BOC_PuDOE['ORION'] = load_efmc_pwr_data()
M_FLM_BOC_FPu['DYMOND'], M_FLM_EOC_FPu['DYMOND'], M_FF_BOC_FPu['DYMOND'], M_FF_EOC_FPu['DYMOND'], M_FLM_BOC_PuDOE['DYMOND'], M_FF_BOC_PuDOE['DYMOND'] = load_dymond_pwr_data()
M_FLM_BOC_FPu['COSI6'], M_FLM_EOC_FPu['COSI6'], M_FF_BOC_FPu['COSI6'], M_FF_EOC_FPu['COSI6'], M_FLM_BOC_PuDOE['COSI6'], M_FF_BOC_PuDOE['COSI6'] = load_cosi6_pwr_data()

PWR_MASS = {}
PWR_MASS['CLASS'] = 72
PWR_MASS['ANICCA'] = 101.7
PWR_MASS['TrEvol'] = 23
PWR_MASS['CYCLUS'] = 72
PWR_MASS['ORION'] = 1
PWR_MASS['DYMOND'] = 72
PWR_MASS['COSI6'] = 1

PWR_CYCLE = {}
PWR_CYCLE['CLASS'] = 3
PWR_CYCLE['ANICCA'] = 1390/0.85/365.25
PWR_CYCLE['TrEvol'] = 41 / (3*0.9) *72.0 /365.25
PWR_CYCLE['CYCLUS'] = 41.09 /2.7 *72 /365.25
PWR_CYCLE['ORION'] = 3.6
PWR_CYCLE['DYMOND'] = 3
PWR_CYCLE['COSI6'] = 4

colors = {}
colors['CLASS'] = "black"
colors['ANICCA'] = "crimson"
colors['CYCLUS'] = "royalblue"
colors['TrEvol'] = "limegreen"
colors['ORION'] = "darkorange"
colors['DYMOND'] = "violet"
colors['COSI6'] = "cyan"

#######################################################################
# 
# Estimators calculation
# 
#######################################################################

ESTIMATOR_1 = {}
# _codes = ['ANICCA', 'CLASS', 'COSI6', 'CYCLUS', 'DYMOND', 'ORION', 'TrEvol']
_codes = codes
for code in _codes:
    ESTIMATOR_1[code] = (M_FLM_BOC_FPu[code] - M_FF_BOC_FPu[code] ) / M_FF_BOC_FPu[code]

ESTIMATOR_2 = {}
# _codes = ['ANICCA', 'CLASS', 'COSI6', 'CYCLUS', 'DYMOND', 'ORION', 'TrEvol']
_codes = codes
for code in _codes:
    _fml = (M_FLM_BOC_FPu[code] -  M_FLM_EOC_FPu[code])/M_FLM_BOC_FPu[code]
    _ff = (M_FF_BOC_FPu[code] -  M_FF_EOC_FPu[code])/M_FF_BOC_FPu[code]
    ESTIMATOR_2[code] = (_fml - _ff)/_ff

ESTIMATOR_3 = {}
# _codes = ['ANICCA', 'CLASS', 'COSI6', 'CYCLUS', 'DYMOND', 'ORION', 'TrEvol']
_codes = codes
for code in _codes:
    _fml = (M_FLM_BOC_FPu[code] -  M_FLM_EOC_FPu[code])* PWR_MASS[code]/PWR_CYCLE[code]
    _ff = (M_FF_BOC_FPu[code] -  M_FF_EOC_FPu[code])* PWR_MASS[code]/PWR_CYCLE[code]
    ESTIMATOR_3[code] = (_fml - _ff)/_ff

#######################################################################
# 
# Plotting functions
# 
#######################################################################

# Plutonium @ BOC and EOC
def plot_pu(datas_boc, datas_eoc, labels=[], bins=[], x_label='Mass Fraction', y_label='Norm. D.', title_label='PWR MOX FLM - Pu distribution', range=(0,0.20)):

    fig, axs = plt.subplots(len(labels), 1, sharex=True, figsize=(16, 10))
    fig.subplots_adjust(hspace=0.0)

    #plt.title(title_label,fontsize=20)
    axs[0].set_title(title_label)
    plt.xlabel(x_label)

    #plt.ylabel('Number of Occurences')
    for i, label in enumerate(labels):
        bin = 0
        if len(bins) >0:
            bin = bins[i]
        data_boc = datas_boc[label]
        data_eoc = datas_eoc[label]

        axs[i].grid(True)
        axs[i].set_ylabel(y_label)
        axs[i].hist(data_boc,bins=bin,range=range,histtype='stepfilled', alpha=1.0, density=True,lw=2,label='B.O.C.', color="black")
        axs[i].hist(data_eoc,bins=bin,range=range,histtype='stepfilled', alpha=0.4, density=True,lw=2,label='E.O.C.', color="red")
        axs[i].text(0.8, 0.8,label,horizontalalignment='center',verticalalignment='center',transform = axs[i].transAxes, fontsize=15)
        axs[i].legend(loc='upper right',prop={'size': 12})
    plt.show()
    fig.savefig("FIG/PWR_MOX_FLM_Pu.pdf",bbox_inches='tight')

# Estimators
def plot_estimator(datas,labels=[], bins=[], x_label='X', y_label='Y', title_label='Title', range=(0,1)):

    fig, axs = plt.subplots(len(labels), 1, sharex=True, figsize=(16, 10))
    fig.subplots_adjust(hspace=0.0)

    #plt.title(title_label,fontsize=20)
    axs[0].set_title(title_label)
    plt.xlabel(x_label)

    #plt.ylabel('Number of Occurences')
    for i, label in enumerate(labels):
        bin = 0
        if len(bins) >0:
            bin = bins[i]
        data = datas[label]

        axs[i].grid(True)
        axs[i].set_ylabel(y_label)
        axs[i].hist(data,bins=bin,range=range,histtype='step', alpha=1.0, density=True,lw=3,color="black")
        axs[i].text(0.8, 0.8,label,horizontalalignment='center',verticalalignment='center',transform = axs[i].transAxes, fontsize=15)
    plt.show()
    fig.savefig("FIG/"+title_label+".pdf",bbox_inches='tight')

#######################################################################
# 
# Printing functions
# 
#######################################################################

def print_means_pu(code):
    print("----------------------------------------")
    print("Mean value")
    print("----------------------------------------")
    print("-----",code,"-----")
    print("FLM : ")      
    print("Pu @BOC : ",np.mean(M_FLM_BOC_FPu[code])," - Pu @EOC : ",np.mean(M_FLM_EOC_FPu[code]))
    print ("FF : ")      
    print("Pu @BOC : ",np.mean(M_FF_BOC_FPu[code])," - Pu @EOC : ",np.mean(M_FF_EOC_FPu[code]))
    print("\n")
    
def print_std_pu(code):
    print("----------------------------------------")
    print("Standard Deviation")
    print("----------------------------------------")
    print("-----",code,"-----")
    print("FLM : ")      
    print("Pu @BOC : ",np.std(M_FLM_BOC_FPu[code])," - Pu @EOC : ",np.std(M_FLM_EOC_FPu[code]))
    print ("FF : ")      
    print("Pu @BOC : ",np.std(M_FF_BOC_FPu[code])," - Pu @EOC : ",np.std(M_FF_EOC_FPu[code]))
    print("\n")

def print_means_estimator(code,est):
    print("----------------------------------------")
    print("Mean value")
    print("----------------------------------------")
    print("-----",code,"-----")
    print("estimator : ",np.mean(est[code]))
    print("\n")
    
def print_std_estimator(code,est):
    print("----------------------------------------")
    print("Standard Deviation")
    print("----------------------------------------")
    print("-----",code,"-----")
    print("estimator : ",np.std(est[code]))
    print("\n")

#######################################################################
# 
# Plotting
# 
#######################################################################

# Plutonium
bins = [75, 75, 75, 75, 75, 75, 75]

plot_pu(M_FLM_BOC_FPu, M_FLM_EOC_FPu, bins=bins, labels=codes, range=(0,0.20))

# Estimators

bins = [50, 50, 50, 50, 50, 50, 50]
plot_estimator(ESTIMATOR_1, bins=bins, labels=codes, title_label='PWR_MOX_Estimator_1', x_label='$\delta F(Pu)$', y_label='Density',range=(-1.4,1.4))

bins = [50, 50, 50, 50, 50, 50, 50]
plot_estimator(ESTIMATOR_2, bins=bins, labels=codes, title_label='PWR_MOX_Estimator_2', x_label='$\delta F(Pu)$', y_label='Density',range=(-2.0,1.4))

bins = [50, 50, 50, 50, 50, 50, 50]
plot_estimator(ESTIMATOR_3, bins=bins, labels=codes, title_label='PWR_MOX_Estimator_3', x_label='$\delta F(Pu)$', y_label='Density',range=(-2.0,3.0))

#######################################################################
# 
# Priting
# 
#######################################################################

for code in codes:
    print_means_pu(code)
for code in codes:
    print_std_pu(code)

for code in codes:
    print_means_estimator(code,ESTIMATOR_1)
for code in codes:
    print_std_estimator(code,ESTIMATOR_1)    

for code in codes:
    print_means_estimator(code,ESTIMATOR_2)
for code in codes:
    print_std_estimator(code,ESTIMATOR_2)    

for code in codes:
    print_means_estimator(code,ESTIMATOR_3)
for code in codes:
    print_std_estimator(code,ESTIMATOR_3)    




