# FITProject

The repository contains work related to FIT (Functionnality Isolation Test) project.

[//]: # (-------------------------------------------------------------------------------------------------------)
[//]: # (-------------------------------------------------------------------------------------------------------)
## Introduction
[//]: # (-------------------------------------------------------------------------------------------------------)
[//]: # (-------------------------------------------------------------------------------------------------------)

Since the 90’s, a lot of different fuel cycle tools have been developed by several institutions (industrial, engineering, academic, etc.). Several level of complexity could be reached, from the simple spread sheet to the complex simulation framework. Also, all the tools can reach different level of capabilities and flexibility and could be adapted for one specific problem to any problems related to the fuel cycle.

Dynamic fuel cycle simulators are used for several applications. they are part of the technical evaluation of innovative systems deployment. Also, they help to identify drivers / parameters interactions in fuel cycle fleet physics. Finally, this kind of tools produces data for further assessments (economy, safety, non-proliferation, etc.). For thoses reasons, fuel cycle simulators can be viewed as decision support helping tool.

The FIT project aims to **improve the confidence in fuel cycle simulators output**. For this purpose, several technics are available : 
- Uncertainty assessement and propagation
- Comparison with experimental data
- Code testing or comparison

FIT project is based on code feature testing. The purpose of the FIT Benchmarks is to **test the impact of FCC functionality** and how this **impact is propagated** in the fuel cycle calculation.

[//]: # (-------------------------------------------------------------------------------------------------------)
[//]: # (-------------------------------------------------------------------------------------------------------)
## Abbreviations and definitions
[//]: # (-------------------------------------------------------------------------------------------------------)
[//]: # (-------------------------------------------------------------------------------------------------------)

RPC : Reactor Physics Code

A Reactor Physics Code is used to simulate the neutron behavior in a unit cell, a fuel assembly or a nuclear core. It can be deterministic or stochastic and is also plugged with a Bateman Solver for solving evolution equations. The input is the description of the system and the initial fuel composition. The output is the evolution of the isotopic composition or other data, such as reactivity or mean cross sections. 

FCC : Fuel Cycle Code

A Fuel Cycle Code is a dynamic fuel cycle simulation tool. The aim is to model an evolving electro-nuclear fleet. The main output is the evolution of isotopes everywhere in all facilities.

FLM : Fuel Loading Model

A FLM aims to adapt the fresh fuel composition according to the reactor requirements. For instance, the fissile fraction is calculated from the fissile stock quality in order to reach the required burnup of the reactor. FLM could be based on neural network, Plutonium equivalent, etc. This relation is usually built from physics constraint and upstream reactor calculation. It is possible to increase the complexity of the FLM according to the level of physics constraints. Here, FLM means there is a process that connect the fresh fuel composition to the available materials, whatever the complexity is.

Recipe : 

A recipe approach aims to tune the fuel cycle calculation in order to have a well known isotopic vector already precisely calculated from a RPC. The fresh fuel composition in the reactor at Beginning Of Cycle (BOC) is always the same. For instance, the reactor load a MOX fuel with 7% (mass) of plutonium with always the same isotopic composition. It is possible to use recipe interpolation, closest composition, etc.  

FF : Fixed Fraction

We call Fixed Fraction approach a fuel cycle calculation for which each fresh fuel loading is based on the same constant fissile fraction, whatever the isotopic vector is. For instance, a PWR MOX is always loading a fresh fuel at 7% of plutonium. This approach is of course a strong approximation for recyled fuels.

[//]: # (-------------------------------------------------------------------------------------------------------)
[//]: # (-------------------------------------------------------------------------------------------------------)
## List of features to be tested
[//]: # (-------------------------------------------------------------------------------------------------------)
[//]: # (-------------------------------------------------------------------------------------------------------)

In this part, the features to be tested in the framework of FIT project are listed and described. The list is not exhaustive and all participants can add new features. 

### Update the fuel composition vs. Fixed Fraction

This specification aims to compare the impact of the fuel composition update according to fissile isotopic composition. This can be done via a FLM or a Recipe approach. This approach is compared to a Fixed Fraction (FF) fuel, which means the fissile fraction is constant whatever the composition is.

### Fuel Shortage Response

Here, we'll try to assess the impact of the fuel shortage response in the FCC. Usually, the response would be : 
- An emty cycle
- Reactor is shut down until there is enough material
- Needed material is created
- ETC.

### Variable Capacity Factor vs. Constant Capacity Factor

This item is connected to economic evaluation. Variable capacity factor could be due to actual outage modeled, seasonal changes in demand, etc.

### Accurate physics of mixed cores vs. Assuming constant core
### Exact startup composition   vs. Single composition at beginning of operation
### Reprocessing As-Needed  vs. Constant Reprocessing   if decay modeled, it may matter
### Isotopic Decay  vs. No Decay First in First Out for all materials
### Constant XS vs. Updated XS
### Fuel type switching method

Smooth Transition, brutal transition, etc.                                 
                                            
### Constrained Processing (Fab, Enr, Rep, etc.) vs. Unconstrained Processing
### Coarse time steps   vs. Fine time steps
### Fleet-based reactors vs. Agent-based reactors
### Batchwise fuel management vs. Simulated continuous reloading related to MSRs maybe
### Batchwise fuel management vs. Continuous reloading vs 1 batch reloading

[//]: # (-------------------------------------------------------------------------------------------------------)
[//]: # (-------------------------------------------------------------------------------------------------------)
## The github repository
[//]: # (-------------------------------------------------------------------------------------------------------)
[//]: # (-------------------------------------------------------------------------------------------------------)

You can download the github repository from the following command : 

    git clone https://github.com/FuelCycleFIT/FITProject.git
    cd FITProject

From that point you can fork the repository from github web site and define upstream and origin remotes. 

    git remote set-url origin https://github.com/[YourAccount]/FITProject.git
    git remote add upstream https://github.com/FuelCycleFIT/FITProject.git

If your repo is properly defined, you should have folowing remotes :

    git remote -v
    origin  https://github.com/[YourAccount]/FITProject.git (fetch)
    origin  https://github.com/[YourAccount]/FITProject.git (fetch)
    upstream    https://github.com/FuelCycleFIT/FITProject.git (fetch)
    upstream    https://github.com/FuelCycleFIT/FITProject.git (push)

From this point, you should be able to push modifications on your fork and to request merge on the upstream repository.

[//]: # (-------------------------------------------------------------------------------------------------------)
[//]: # (-------------------------------------------------------------------------------------------------------)
## Codes
[//]: # (-------------------------------------------------------------------------------------------------------)
[//]: # (-------------------------------------------------------------------------------------------------------)

Each institution describes RPC and FCC that they use with main publications.

### RPC

#### SMURE - Developped by CNRS/IN2P3 : 

There is two online sources for the SMURE code, the [official web page of SMURE](http://lpsc.in2p3.fr/MURE/html/SMURE/UserGuide/UserGuide.html) and the [NEA dedicated page](https://www.oecd-nea.org/tools/abstract/detail/nea-1845)

The main aim of the SMURE package is to perform nuclear reactor time-evolution using the widely-used particle transport code MCNP (a Monte Carlo code which is mostly written in FORTRAN) or SERPENT. In SMURE, due to the Object-oriented programming, any user can define his own way to interact with evolution. Moreover, SMURE provides a simple graphical interface to visualize the results. It also provides a way to couple the neutronics (with or without fuel burn-up) and thermohydraulics using either an open source simple code developed in SMURE (BATH, Basic Approach of Thermal Hydraulics) or a sub-channel 3D code, COBRA-EN. But SMURE can also be used just as an interface to MCNP or Serpent to build geometries (e.g. for neutronics experiments simulation).

You can also refer to following publication : 

    *Méplan O., Nuttin A., Laulan O., David S., Michel-Sendis F. et al.:
    MURE : MCNP Utility for Reactor Evolution - Description of the methods,
    first applications and results, Proceedings of the ENC 2005 (CD-Rom)
    ENC 2005 - European Nuclear Conference. 
    Nuclear Power for the XXIst Century : From basic research to high-tech industry, France*

### FCC

#### CLASS - Developped by CNRS/IN2P3 :

The code CLASS is a dynamic fuel cycle simulation tool developed by CNRS/IN2P3 (Centre National de la Recherche Scientifique / Institut National de Physique Nucléaire et de Physique des Particules) in collaboration with IRSN (Institut de Radioprotection et de Sûreté Nucléaire). The aim of CLASS is to model an evolving electro-nuclear fleet. The main output is the evolution of isotopes everywhere in the fleet.
The CLASS model is a collection of C++ classes that describes facilities in a nuclear fleet. The CLASS model has been built around the reactor class that drives radioactive material flows from reactor front to back end.

The latest shared version is the [official Version 5.1](https://gitlab.in2p3.fr/sens/CLASS/tree/CLASS_V5_Official_Release).

[//]: # (-------------------------------------------------------------------------------------------------------)
[//]: # (-------------------------------------------------------------------------------------------------------)
## Exercices Nomenclature and small description
[//]: # (-------------------------------------------------------------------------------------------------------)
[//]: # (-------------------------------------------------------------------------------------------------------)






For each tested features, the FIT benchmark is based on a set of RPC and FCC calculations. The roadmap is presented from the first tested feature : 
    
    Update the fuel composition vs. Fixed Fraction

1. Reference calculation from RPC run 

The participant/institution (e.g., Hawaii National Laboratory) needs a reference model of the reactor (e.g., 1000 MWt metallic fuel SFR with 1.2 breeding ratio) and its fuel compositions (loaded and discharged) during the equilibrium cycle. This should be generated by an RPC (e.g., ERANOS). Let’s say the Pu content of this reference loaded fuel composition is 10 wt% and the discharged Pu content is 12 wt% (this is a breeder reactor; these are mass-weighted values across driver fuel and blankets). These are the reference values for the equilibrium SFR core using the equilibrium SFR Pu vectors in the recycled fresh fuel.

For this part, each participant/institution have to precisely describe criteria that drives the reactor calculation. For instance, it could be reactivity based for a PWR or a targeted breeding ratio for a SFR modelization. **The reference calculation is freely designed** by each participant/institution so that it can be run easily.

2. Reference calculation from FCC run

For the FCC (e.g., ORION) calculation of this reference model, this data should be easy inputs to the code. This is what we should be calling the “recipe approach”. There is no need to turn on any functionality that updates the fuel composition because the charge and discharge compositions are already provided as recipes.

For this part, each participant/institution have then to ensure that **the FCC calculation exactly fits the RPC calculation**. 

After this step, we consider that the FCC is tuned to produce the same result whatever the feature is.

3. Process tested compositions from FCC and RPC run

Now we switch the fresh fuel composition to be built from the tested isotopic vector which are specified in the specifications, so that all participants use the same Pu vector(s) in the perturbed calculations. Then, Hawaii National Laboratory needs to produce the new loaded and discharged Pu contents using the same RPC (ERANOS) and the functionality within their FCC (e.g., ORION) that they are using (e.g., Pu equivalence model with weight factors, neural network, etc.) to produce the following figure:

!!! PUT A FIGURE !!!

4. Deviation impact on a 100 years time range FCC calculation

Finally, a FCC long term calculation (up to 100 years) is done in order to have a connexion between results and « real scientific question ».   



Nomenclature has three informations : 

- The tested feature number Feat_I
- The exercise number Ex_J
- The case number Case_K

Example : Feat1_Ex1_Case1

This will define the tree in the FIT repository.

Feat_1

The scheme of the scenario is as following :

![alt text](https://github.com/thiollie/FITProject/blob/master/FIG/Feat_1.png)


Ex1

The first exercice is related to a PWR loaded with MOX fuel.

Ex2

The first exercice is related to a SFR loaded with MOX fuel.
