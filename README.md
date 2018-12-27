# FITProject

The repository contains work related to FIT (Functionnality Isolation Test) project

## 0. Abbreviations and definitions

RPC : Reactor Physics Code

FCC : Fuel Cycle Code

FLM : Fuel Loading Model

A FLM aims to adapt the fresh fuel composition according to the reactor requirements. For instance, the fissile fraction is calculated from the fissile stock quality in order to reach the required burnup of the reactor. FLM could be based on neural network, Plutonium equivalent, etc. This relation is usually built from physics constraint and upstream reactor calculation. It is possible to increase the complexity of the FLM according to the level of physics constraints. Here, FLM means there is a process that connect the fresh fuel composition to the available materials, whatever the complexity is.

Recipe : 

The fresh fuel composition in the reactor at Beginning Of Cycle (BOC) is always the same. For instance, the reactor load a MOX fuel with 7% (mass) of plutonium with always the same isotopic composition. It is possible to use recipe interpolation, closest composition, etc.  

## 1. Use the github repository

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

## 2. Codes

### 2.a. RPC

Each institution describes RPC that they use with main publications.

### 2.b. FCC

Each institution describes FCC that they use with main publications.

## 3. List of features to test

In this part, we list all the features we want to test and we write an associated description.

## 4. Exercices Nomenclature and small description

Nomenclature has three informations : 

- The tested feature number Feat_I
- The exercise number Ex_J
- The case number Case_K

Example : Feat1_Ex1_Case1

This will define the tree in the FIT repository.

