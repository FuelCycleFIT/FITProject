#######################################################################
# 
# Libraries and plotting options
# 
#######################################################################

import matplotlib.pyplot as plt
import numpy as np

plt.style.use('seaborn-white')

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

codes = ['CLASS','JOSETTE','TR_EVOL', 'DYMOND']

#######################################################################
# 
# Reactor descriptions
# 
#######################################################################
"""
### CLASS
#### Reactor
    - Heavy mass: 72 tons
    - Thermal power: 3 GWth
    - Irradiation time: 7 years that correspond to a burn-up closed to 80 GWd/t
    - Loading factor: 75%

#### FLM
    - 17x17 infinite assembly
    - Neural network prediction of the k$_{inf}$
    - k$_{threshold}$ is 1.034

### Tr_Evol
#### Reactor
    - Thermal_power_(GW) : 3.6
    - Electrical_power_(GW) : 1.44
    - Load_factor : 0.9
    - Core_mass_(tHM) : 45.0
    - Burn_up_(GWd/tHM) : 136
#### FLM
    - Baker \& Ross

### Josette
#### Reactor
    - Thermal_power_(GW) : 3.6
    - Load_factor : 1 ??
    - Core_mass_(tHM) : 71.4
    - Burn_up_(GWd/tHM) : 100
#### FLM
    - Baker \& Ross
"""

#######################################################################
# 
# Loading Data Functions => Add one function for any new data set
# 
#######################################################################

# CLASS
def load_class_data(file = 'CLASS_CNRS_RNR/Data.dat'):
    M_CLASS = np.loadtxt(file)
    M_CLASS_FF_BOC = M_CLASS[::4]
    M_CLASS_FF_EOC = M_CLASS[1::4]
    M_CLASS_FLM_BOC = M_CLASS[2::4]
    M_CLASS_FLM_EOC = M_CLASS[3::4]
    
    total_mass = 72    
    
    M_CLASS_FLM_BOC_FPu = M_CLASS_FLM_BOC[:,3]/total_mass
    M_CLASS_FLM_EOC_FPu = M_CLASS_FLM_EOC[:,3]/total_mass
    M_CLASS_FF_BOC_FPu = M_CLASS_FF_BOC[:,3]/total_mass
    M_CLASS_FF_EOC_FPu = M_CLASS_FF_EOC[:,3]/total_mass
    
    return M_CLASS_FLM_BOC_FPu, M_CLASS_FLM_EOC_FPu, M_CLASS_FF_BOC_FPu, M_CLASS_FF_EOC_FPu

# BME
def load_josette_data(file = 'JOSETTE_BME/'):
    M_FF_BOC = np.loadtxt(file + "FF_BOC.txt")
    M_FF_EOC = np.loadtxt(file + "FF_EOC.txt")

    M_FLM_BOC = np.loadtxt(file + "FLM_BOC.txt")
    M_FLM_EOC = np.loadtxt(file + "FLM_EOC.txt")


    total_mass = 7.15E+01
    M_jos_FLM_BOC_FPu = M_FLM_BOC[:,3]/1e6 / total_mass
    M_jos_FLM_EOC_FPu = M_FLM_EOC[:,3]/1e6 / total_mass

    M_jos_FF_BOC_FPu = M_FF_BOC[:,3]/1e6 / total_mass
    M_jos_FF_EOC_FPu = M_FF_EOC[:,3]/1e6 / total_mass

    return M_jos_FLM_BOC_FPu, M_jos_FLM_EOC_FPu, M_jos_FF_BOC_FPu, M_jos_FF_EOC_FPu

# TR_EVOL
def load_TR_EVOL_data(file = 'TREVOL_CIEMAT/SFR_raw.txt'):
    M_TR_EVOL = np.loadtxt(file)
    total_mass = 8.7
    M_TR_EVOL_FLM_BOC_FPu = M_TR_EVOL[:,23] / total_mass
    M_TR_EVOL_FLM_EOC_FPu = M_TR_EVOL[:,33] / total_mass

    M_TR_EVOL_FF_BOC_FPu = M_TR_EVOL[:,3] / total_mass
    M_TR_EVOL_FF_EOC_FPu = M_TR_EVOL[:,13] / total_mass

    return M_TR_EVOL_FLM_BOC_FPu, M_TR_EVOL_FLM_EOC_FPu, M_TR_EVOL_FF_BOC_FPu, M_TR_EVOL_FF_EOC_FPu

# DYMOND
def load_dymond_sfr_data(file = 'DYMOND_SFR_V2B'):
        
    M_Dymond_FF_BOC = np.loadtxt(file + '/DYMOND_SFR_V2B_FF_BOC.csv', delimiter=',', skiprows =1)
    M_Dymond_FF_EOC = np.loadtxt(file + '/DYMOND_SFR_V2B_FF_EOC.csv', delimiter=',', skiprows =1)
    M_Dymond_FLM_BOC = np.loadtxt(file + '/DYMOND_SFR_V2B_FLM_BOC.csv', delimiter=',', skiprows =1)
    M_Dymond_FLM_EOC = np.loadtxt(file + '/DYMOND_SFR_V2B_FLM_EOC.csv', delimiter=',', skiprows =1)

    total_mass = 72
    M_Dymond_FLM_BOC_FPu = M_Dymond_FLM_BOC[:1000,3]/total_mass
    M_Dymond_FLM_EOC_FPu = M_Dymond_FLM_EOC[:1000,3]/total_mass

    M_Dymond_FF_BOC_FPu = M_Dymond_FF_BOC[:1000,3]/total_mass
    M_Dymond_FF_EOC_FPu = M_Dymond_FF_EOC[:1000,3]/total_mass

    a1 = M_Dymond_FLM_BOC[:1000,[6,7,8,9,10,11]]
    a2 = M_Dymond_FF_BOC[:1000,[6,7,8,9,10,11]]
    
    M_Dymond_FLM_BOC_PuDOE = a1/np.sum(a1,axis=1,keepdims=True)
    M_Dymond_FF_BOC_PuDOE =  a2/np.sum(a2,axis=1,keepdims=True)
            
    #return M_Dymond_FLM_BOC_FPu, M_Dymond_FLM_EOC_FPu, M_Dymond_FF_BOC_FPu, M_Dymond_FF_EOC_FPu, M_Dymond_FLM_BOC_PuDOE, M_Dymond_FF_BOC_PuDOE
    return M_Dymond_FLM_BOC_FPu, M_Dymond_FLM_EOC_FPu, M_Dymond_FF_BOC_FPu, M_Dymond_FF_EOC_FPu

#######################################################################
# 
# Loading the data
# 
#######################################################################

M_FLM_BOC_FPu = {}
M_FLM_EOC_FPu = {}
M_FF_BOC_FPu = {}
M_FF_EOC_FPu = {}

M_FLM_BOC_MUPu = {}

M_FLM_BOC_FPu['CLASS'], M_FLM_EOC_FPu['CLASS'], M_FF_BOC_FPu['CLASS'], M_FF_EOC_FPu['CLASS'] = load_class_data()
M_FLM_BOC_FPu['TR_EVOL'], M_FLM_EOC_FPu['TR_EVOL'], M_FF_BOC_FPu['TR_EVOL'], M_FF_EOC_FPu['TR_EVOL'] = load_TR_EVOL_data()
M_FLM_BOC_FPu['JOSETTE'], M_FLM_EOC_FPu['JOSETTE'], M_FF_BOC_FPu['JOSETTE'], M_FF_EOC_FPu['JOSETTE'] = load_josette_data()
M_FLM_BOC_FPu['DYMOND'], M_FLM_EOC_FPu['DYMOND'], M_FF_BOC_FPu['DYMOND'], M_FF_EOC_FPu['DYMOND'] = load_dymond_sfr_data()


SFR_MASS = {}
SFR_MASS['CLASS'] = 72
SFR_MASS['TR_EVOL'] = 8.7
SFR_MASS['JOSETTE'] = 7.14E+01
SFR_MASS['DYMOND'] = 73.8



SFR_CYCLE = {}
SFR_CYCLE['CLASS'] =  80 / (3*0.75) * SFR_MASS['CLASS'] /365.25
SFR_CYCLE['TR_EVOL'] = 135 / (3.6*0.9) * SFR_MASS['TR_EVOL'] /365.25
SFR_CYCLE['JOSETTE'] = 100 / (3.6) * SFR_MASS['JOSETTE'] /365.25
SFR_CYCLE['DYMOND'] = 6.60


colors = {}
colors['CLASS'] = "red"
colors['TR_EVOL'] = "green"
colors['JOSETTE'] = "chartreuse"
colors['DYMOND'] = "violet"

#######################################################################
# 
# Estimators calculation
# 
#######################################################################

ESTIMATOR_1 = {}
_codes = codes
for code in _codes:
    ESTIMATOR_1[code] = (M_FLM_BOC_FPu[code] - M_FF_BOC_FPu[code] ) /M_FF_BOC_FPu[code]

ESTIMATOR_2b = {}
_codes = codes
for code in _codes:
    _fml = (M_FLM_BOC_FPu[code] -  M_FLM_EOC_FPu[code])/M_FLM_BOC_FPu[code]
    _ff = (M_FF_BOC_FPu[code] -  M_FF_EOC_FPu[code])/M_FF_BOC_FPu[code]
    ESTIMATOR_2b[code] = (_fml - _ff)

ESTIMATOR_3 = {}
_codes = codes
for code in _codes:
    _fml = (M_FLM_BOC_FPu[code] -  M_FLM_EOC_FPu[code])* SFR_MASS[code]/SFR_CYCLE[code]
    _ff = (M_FF_BOC_FPu[code] -  M_FF_EOC_FPu[code])* SFR_MASS[code]/SFR_CYCLE[code]
    ESTIMATOR_3[code] = (_fml - _ff)

#######################################################################
# 
# Plotting functions
# 
#######################################################################

def plot_pu(datas_boc, datas_eoc, labels=[], bins=[], x_label='Mass Fraction', y_label='Density', title_label='SFR MOX FLM - Pu distribution', range=(0,0.20)):
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
    fig.savefig("FIG/SFR_MOX_FLM_Pu.pdf",bbox_inches='tight')

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

bins = [75, 75, 75, 75]
plot_pu(M_FLM_BOC_FPu, M_FLM_EOC_FPu, bins=bins, labels=codes, range=(0.10,0.30))

bins = [75, 75, 75, 75]
plot_estimator(ESTIMATOR_1, bins=bins, labels=codes, title_label='SFR_Estimator_1', x_label='$\delta F(Pu)$', range=(-1.,1.))

bins = [75, 75, 75, 75]
plot_estimator(ESTIMATOR_2b, bins=bins, labels=codes, title_label='SFR_Estimator_2b', x_label='$\delta F(Pu)$', range=(-0.4,0.4))

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
    print_means_estimator(code,ESTIMATOR_2b)

for code in codes:
    print_std_estimator(code,ESTIMATOR_2b)    


