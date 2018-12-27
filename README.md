# FITProject
The repository contains work related to FIT (Functionnality Isolation Test) project

## 0. Abbreviations

RPC : Reactor Physics Code
FCC : Fuel Cycle Code
FLM : Fuel Loading Model

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

### 1.a. RPC

Each institution describes RPC that they use with main publications.

### 1.b. FCC

Each institution describes FCC that they use with main publications.

## 2. List of features to test

In this part, we list all the features we want to test and we write an associated description.

## 3. Exercices Nomenclature and small description

Nomenclature has three informations : 

- The tested feature number FeatI
- The exercise number ExJ
- The case number CaseK

Example : Feat1_Ex1_Case1

This will define the tree in the FIT repository.

