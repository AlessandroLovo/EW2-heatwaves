# EW2-heatwaves
One of the exercises for the second Critical Earth ESR Workshop (April 2022, Berg en Dal, Netherlands)

# Description

# Installation

## Local
Depending on which operating system you are using there is a possibility to use Anaconda and/or homebrew (on Mac).
In some cases path variable must be provided.

It is highly suggested to create a conda environment and work from that, so you don't mess up your own base environment.

Start by creating a new python 3.9 environment, let's call it `ew2`
```
conda create -n ew2 python=3.9
conda activate ew2
```

Then install the required packages
```
conda install -c conda-forge numpy pandas xarray matplotlib tqdm json optuna
```
Install machine learning package
```
conda install -c conda-forge tensorflow
```


## Online
Open the notebook `ew2.ipynb` in google colab and run from there
