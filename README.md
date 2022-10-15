# Repository Description

* This repository was originally cloned and modified from [that of Obermeyer et. al's study](https://gitlab.com/labsysmed/dissecting-bias/-/tree/master). 
* First, we worked on reproducing Obermeyer et. al's results.
* Next, we made modifications and adding our own training labels to expand on and potentially even improve the results, namely the inclusion of Black patients in high-risk groups. We will be using a combination of techniques mentioned in the predictive healthcare algorithm papers we've read to build an improved model for predicting which patients require further healthcare resources.
* The synthetic dataset is included in this repository, and we plan on applying our new model to the dataset.

## Project Repository Structure

This repository contains data and code needed to reproduce the main results for Obermeyer et. al's [paper]() Dissecting Racial Bias in an Algorithm Used to Manage the Health of Populations, as well as our new code.

1. *data*: A synthetic master dataset that closely mirrors the dataset used to produce the original results. The real data is kept private due to patient confidentiality standards.
2. *code*: Code in R and Python that can be used to train and run the model, as well as replicate the figures and tables from the main manuscript.
3. *results*: Our replication of these results using the synthetic dataset, as well as new results generated from our new training label.
4. *ibm-fairness*: Code setup for future work with the IBM fairness model

## Synthetic Dataset Creation

Researchers used the [synthpop](https://cran.r-project.org/web/packages/synthpop/index.html) R package to create a synthetic version of the key variables needed to replicate all analyses in the paper, so we are working under the assumption that this data is highly representative of the dataset actually used in the study.

The original [data dictionary](./data/data_dictionary.md) describing each of the individual variables from the authors is included.


