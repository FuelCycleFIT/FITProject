In this part, the feature **Update the fuel composition vs. Fixed Fraction** is assessed. Specifications details are low in order to let a high degree of freedom in the solving. 

[//]: # (-------------------------------------------------------------------------------------------------------)
[//]: # (-------------------------------------------------------------------------------------------------------)
# Abbreviations and definitions
[//]: # (-------------------------------------------------------------------------------------------------------)
[//]: # (-------------------------------------------------------------------------------------------------------)

## Reactor Physics Code (RPC)

A Reactor Physics Code is used to simulate the neutron behavior in a unit cell, a fuel assembly or a nuclear core. It can be deterministic or stochastic and is also plugged with a Bateman Solver for solving evolution (a.k.a. burnup/depletion) equations. The input is the description of the system and the initial fuel composition. The output is the evolution of the isotopic composition or other data, such as reactivity or mean cross sections. 

## Fuel Cycle Code (FCC)

A Fuel Cycle Code is a dynamic fuel cycle simulation tool. The aim is to model an evolving electro-nuclear fleet. The main output is the evolution of isotopes everywhere in all facilities.

## Fuel Loading Model (FLM)

A FLM aims to adapt the fresh fuel composition according to the reactor requirements. For instance, the fissile fraction is calculated from the fissile stock quality in order to reach the required burnup of the reactor. A FLM could be based on neural network, Plutonium equivalence model, correlations, built-in depletion, etc. This relation is usually built from physics constraints and reactor physics calculations. It is possible to increase the complexity of the FLM according to the level of physics constraints. Here, FLM means there is a process that connects the fresh fuel composition to the available materials, whatever the complexity.

## Recipe

A recipe approach aims to tune the fuel cycle calculation in order to have a well-known isotopic vector already precisely calculated from an external RPC. The fresh fuel composition in the reactor at Beginning Of Cycle (BOC) is always the same. For instance, the reactor loads a MOX fuel with 7% (mass) of plutonium with always the same isotopic composition. It is possible to use recipe interpolation, closest composition, etc.  

## Fixed Fraction (FF)

We call Fixed Fraction approach a fuel cycle calculation for which each fresh fuel loading is based on the same constant fissile fraction, regardless of the isotopic vector of the fissile material. For instance, a PWR MOX is always loading a fresh fuel at 7% of plutonium regardless of whether the Pu is 50% Pu 239 or 95% Pu-239. This approach is of course a major approximation for recycled fuels.

[//]: # (-------------------------------------------------------------------------------------------------------)
[//]: # (-------------------------------------------------------------------------------------------------------)
# Specifications
[//]: # (-------------------------------------------------------------------------------------------------------)
[//]: # (-------------------------------------------------------------------------------------------------------)

In this part, the FCC functionality that updates the fuel composition is assessed by comparing against a fixed fraction approach. Specifications details are intentionally low in order to allow a high degree of freedom in the solutions for each participant. 

## Simulations requirements

For running this exercise, you have to be able to run a reference calculation based on a physics Fuel Loading Model (FLM), i.e., using a physics relation between fissile fraction and reactor technical requirement, such as burnup. The primary purpose of this test is for each participant to compare the results generated using the FCC’s FLM or recipe to those generated with the FF approach. The FF approach means that the FCC model is bypassed. In this case, the fissile fraction is provided by the user. 

An optional component is to also use a reactor physics code (RPC) outside of the FFC to perform the same calculation as the FCC’s FLM. This way there could be up to 3 different “solutions” for comparison purposes.

## Reactor design and fuel

Given the different tools, methods, and specialization of each institution, it will not be possible for every institution to model the same reactor exactly the same way and fairly compare results across different codes (this would be a code-to-code comparison, which is not the purpose of the FIT Benchmarks). This is why we will allow each participant to model the specific reactor/fuel design(s) with which they are more familiar and for which they may already have models, as long as they fit the general guideline (specification) that one of these models is for a fast spectrum (e.g., metallic fuel in SFR) and another one is for a thermal spectrum (e.g., MOX fuel in PWR).

## Facilities 

For this exercise, following facilities are required : 

- A fissile stock with a plutonium vector
- A fertile stock with a depleted uranium vector
- A fabrication plant
- A reactor
- a storage for the spent fuel

The scheme of the scenario is as following :

![alt text](https://github.com/thiollie/FITProject/blob/master/FIG/Feat_1.png)

## Time frame

The simulation has to be run on a full reactor cycle duration. The relation between the fuel cycle time Dt, the reactor power Pth, heavy nuclide mass M and the burn-up BU is then given by : 

BU = Pth x Dt / M

At t = 0, the fabrication plant build the fresh fuel according to reactor requirements. The fabrication time is zero and the reactor is loaded instantaneously. A complete fuel cycle is run and the spent fuel is sent to storage when the required BU is reached.

## Plutonium vector range

The plutonium vectors that could be tested in the framework of this exercise have to be "realistic". We propose the following table with minimum and maximum isotopic fraction and total fraction in the fuel. 

| Isotope       | Min. Fraction  | Max. Fraction |
|---------------|----------------|---------------|
| Pu/HM in Fuel @ T0 (PWR) | 5   | 10            |
| Pu/HM in Fuel @ T0 (SFR) | 13  | 22            |
|---------------|----------------|---------------|
| Pu-238/TRU    | 0              | 10            |
| Pu-239/TRU    | 25             | 90            |
| Pu-240/TRU    | 10             | 40            |
| Pu-241/TRU    | 0              | 25            |
| Pu-242/TRU    | 0              | 30            |
| Am-241/TRU    | 0              | 10            |
|---------------|----------------|---------------|

Each user can use plutonium vector as long as it is included inside this range.

## Methodology 

The methodology is totally open. Each participant can define its own methodology according to the specificity of the FCC. The only constraint is to define a method that produce a comparison between FCM or Recipe approach (that supposes there is an algorithm used to calculate Pu fraction in the fresh fuel) and FF approach.

Of course, all methodology will be public and it is possible for each participant to use a methodology already defined by another participants.

## Input Data template

This is mostly a text description of the input used by the participant.

-   Reactor description (text)
-   Stock Pu Composition @ Beginning Of Cycle
-   Methodology description (text)

## Output Data template

Output data should be presented for FLM and FF and as a comparison.

- Plutonium fraction @ BOC 
- Plutonium fraction @ EOC
- Fissile (Pu-239 + Pu-241) fraction in spent fuel @ EOC
- Isotopic fraction for each plutonium isotope
- Minor Actinide Production
- Other?
