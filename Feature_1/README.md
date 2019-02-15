In this part, the feature **Update the fuel composition vs. Fixed Fraction** is assessed. Specifications details are low in order to let a high degree of freedom in the solving. 

0. FCC requirements

For running this exercise, the FCC should have a Fuel Loading Model (FLM) that could be enabled and disabled easily. The FLM is calculating the appropriate fissile fraction in the fuel according to reactor specifications. When the FLM is disabled, the fissile fraction is provided by the user. 

1. Reactor design and fuel

Given the different tools, methods, and specialization of each institution, it will not be possible for every institution to model the same reactor exactly the same way and fairly compare results across different codes (this would be a code-to-code comparison, which is not the purpose of the FIT Benchmarks). This is why we will allow each participant to model the specific reactor/fuel design(s) with which they are more familiar and for which they may already have models, as long as they fit the general guideline (specification) that one of these models is for a fast spectrum (e.g., metallic fuel in SFR) and another one is for a thermal spectrum (e.g., MOX fuel in PWR).

2. Facilities 

For this exercise, following facilities are required : 

- A fissile stock with a plutonium vector
- A fertile stock with a depleted uranium vector
- A fabrication plant
- A reactor
- a storage for the spent fuel

The scheme of the scenario is as following :

![alt text](https://github.com/thiollie/FITProject/blob/master/FIG/Feat_1.png)

3. Time frame

The simulation has to be run on a full reactor cycle duration. The relation between the fuel cycle time Dt, the reactor power Pth, heavy nuclide mass M and the burn-up BU is then given by : 

BU = Pth x Dt / M

At t = 0, the fabrication plant build the fresh fuel according to reactor requirements. The fabrication time is zero and the reactor is loaded instantaneously. A complete fuel cycle is run and the spent fuel is sent to storage when the required BU is reached.

4. Plutonium vector range

The plutonium vectors that could be tested in the framework of this exercise have to be "realistic". We propose the following table with minimum and maximum isotopic fraction and total fraction in the fuel. 

| Isotope   | Min. Fraction |  Max. Fraction |
|-----------|:-------------:|---------------:|
| Pu / Fuel |               |                |
|-----------|:-------------:|---------------:|
| Pu-238    |               |                |
| Pu-239    |               |                |
| Pu-240    |               |                |
| Pu-241    |               |                |
| Pu-242    |               |                |
| Am-241    |               |                |
|-----------|:-------------:|---------------:|

Each user can use plutonium vector as long as it is included inside this range.

5. Methodology 

The methodology is totally open. Each participant can define its own methodology according to the specificity of the FCC. The only constraint is to define a method that produce a comparison between FCM or Recipe approach (that supposes there is an algorithm used to calculate Pu fraction in the fresh fuel) and FF approach.

Of course, all methodology will be public and it is possible for each participant to use a methodology already defined by another participants.

6. Data formatting

## input 

## output

