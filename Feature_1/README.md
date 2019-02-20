In this part, the feature **Update the fuel composition vs. Fixed Fraction** is assessed. Specifications details are low in order to let a high degree of freedom in the solving. 

[//]: # (-------------------------------------------------------------------------------------------------------)
[//]: # (-------------------------------------------------------------------------------------------------------)
# Abbreviations and definitions
[//]: # (-------------------------------------------------------------------------------------------------------)
[//]: # (-------------------------------------------------------------------------------------------------------)

## Reactor Physics Code (RPC)

A Reactor Physics Code is used to simulate the neutron behavior in a unit cell, a fuel assembly or a nuclear core. It can be deterministic or stochastic and is also plugged with a Bateman Solver for solving evolution equations. The input is the description of the system and the initial fuel composition. The output is the evolution of the isotopic composition or other data, such as reactivity or mean cross sections. 

## Fuel Cycle Code (FCC)

A Fuel Cycle Code is a dynamic fuel cycle simulation tool. The aim is to model an evolving electro-nuclear fleet. The main output is the evolution of isotopes everywhere in all facilities.

## Fuel Loading Model (FLM)

A FLM aims to adapt the fresh fuel composition according to the reactor requirements. For instance, the fissile fraction is calculated from the fissile stock quality in order to reach the required burnup of the reactor. FLM could be based on neural network, Plutonium equivalent, etc. This relation is usually built from physics constraint and upstream reactor calculation. It is possible to increase the complexity of the FLM according to the level of physics constraints. Here, FLM means there is a process that connect the fresh fuel composition to the available materials, whatever the complexity is.

## Recipe

A recipe approach aims to tune the fuel cycle calculation in order to have a well known isotopic vector already precisely calculated from a RPC. The fresh fuel composition in the reactor at Beginning Of Cycle (BOC) is always the same. For instance, the reactor load a MOX fuel with 7% (mass) of plutonium with always the same isotopic composition. It is possible to use recipe interpolation, closest composition, etc.  

## Fixed Fraction (FF)

We call Fixed Fraction approach a fuel cycle calculation for which each fresh fuel loading is based on the same constant fissile fraction, whatever the isotopic vector is. For instance, a PWR MOX is always loading a fresh fuel at 7% of plutonium. This approach is of course a strong approximation for recyled fuels.

[//]: # (-------------------------------------------------------------------------------------------------------)
[//]: # (-------------------------------------------------------------------------------------------------------)
# Specifications
[//]: # (-------------------------------------------------------------------------------------------------------)
[//]: # (-------------------------------------------------------------------------------------------------------)

# Simulations requirements

For running this exercise, you have to be able to run a reference calculation based on a physics Fuel Loading Model (i.e. Using a physics relation between fissile fraction and reactor technical requirement, such as Burn-Up). This reference calculation may be obtained from following ways:

- An FCC with FLM 
- An RPC with a methodology to connect fissile content and Burn-Up

On the other hand, those reference calculations will be compared to an FF approach that supposes the FCC model could be bypassed. In this case, the fissile fraction is provided by the user. 

# Reactor design and fuel

Given the different tools, methods, and specialization of each institution, it will not be possible for every institution to model the same reactor exactly the same way and fairly compare results across different codes (this would be a code-to-code comparison, which is not the purpose of the FIT Benchmarks). This is why we will allow each participant to model the specific reactor/fuel design(s) with which they are more familiar and for which they may already have models, as long as they fit the general guideline (specification) that one of these models is for a fast spectrum (e.g., metallic fuel in SFR) and another one is for a thermal spectrum (e.g., MOX fuel in PWR).

# Facilities 

For this exercise, following facilities are required : 

- A fissile stock with a plutonium vector
- A fertile stock with a depleted uranium vector
- A fabrication plant
- A reactor
- a storage for the spent fuel

The scheme of the scenario is as following :

![alt text](https://github.com/thiollie/FITProject/blob/master/FIG/Feat_1.png)

# Time frame

The simulation has to be run on a full reactor cycle duration. The relation between the fuel cycle time Dt, the reactor power Pth, heavy nuclide mass M and the burn-up BU is then given by : 

BU = Pth x Dt / M

At t = 0, the fabrication plant build the fresh fuel according to reactor requirements. The fabrication time is zero and the reactor is loaded instantaneously. A complete fuel cycle is run and the spent fuel is sent to storage when the required BU is reached.

# Plutonium vector range

The plutonium vectors that could be tested in the framework of this exercise have to be "realistic". We propose the following table with minimum and maximum isotopic fraction and total fraction in the fuel. 

| Isotope   | Min. Fraction  | Max. Fraction |
|-----------|----------------|---------------|
| Pu in Fuel @ T0 (PWR) | 5  | 10            |
| Pu in Fuel @ T0 (SFR) | 13 | 22            |
|-----------|----------------|---------------|
| Pu-238    | 0              | 10            |
| Pu-239    | 25             | 90            |
| Pu-240    | 10             | 40            |
| Pu-241    | 0              | 25            |
| Pu-242    | 0              | 30            |
| Am-241    | 0              | 10            |
|-----------|----------------|---------------|

Each user can use plutonium vector as long as it is included inside this range.

# Methodology 

The methodology is totally open. Each participant can define its own methodology according to the specificity of the FCC. The only constraint is to define a method that produce a comparison between FCM or Recipe approach (that supposes there is an algorithm used to calculate Pu fraction in the fresh fuel) and FF approach.

Of course, all methodology will be public and it is possible for each participant to use a methodology already defined by another participants.

# Input Data Template

- Reactor description
- Stock Pu Composition @ Beginning Of Cycle
- Methodology description

# Ouput Data Template

