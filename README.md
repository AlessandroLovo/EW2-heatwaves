# EW2-heatwaves
One of the exercises for the second Critical Earth ESR Workshop (April 2022, Berg en Dal, Netherlands)

# Description
In this exercise you will deal with machine learning prediction of heatwaves.

# Running the code
There are two main option to perform this exercise: either on your local machine, or on google Colab.

## Local
This makes sense if your personal computer has a decent GPU, otherwise, it is easier to run the code online. See below

### Install `conda` (optional but highly recommended)

Depending on which operating system you are using there is a possibility to use Anaconda and/or homebrew (on Mac).
In some cases path variable must be provided.

It is highly suggested to create a conda environment and work from that, so you don't mess up your own base environment. For details on how to work with conda environments see the following link [how to manage environments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)

### Create new environment and install required packages

Start by creating a new python 3.9 environment, let's call it `ew2`
```
conda create -n ew2 python=3.9
conda activate ew2
```

Then install the required packages
```
conda install -c conda-forge numpy pandas xarray matplotlib plotly tqdm json optuna cartopy nc-time-axis
```

You may have remove json from this list if the package manager complains, and install it separately via
```
conda install json
```

Install machine learning package
```
conda install -c conda-forge tensorflow
```


## Online
1. Upload the notebook `ew2.ipynb` to your google drive and open it with google colab
2. Go to Runtime -> Change runtime type
3. Select GPU. This will allow you to run your code on a remote google GPU, making it considerably faster than using a CPU
