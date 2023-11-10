# EW2-heatwaves
One of the exercises for the second Critical Earth ESR Workshop (April 2022, Berg en Dal, Netherlands)

# Description
In this exercise you will deal with machine learning prediction of heatwaves. For instructions please view [the exercises pdf](GM_Assignment.pdf).

# Running the code
There are two main option to perform this exercise: either on your local machine, or on google Colab.

## Data:
There are instruction on how to download the data within the jupyter notebooks, alternative the data is available from [500 years of Plasim](https://zenodo.org/records/10102506)

## Online (suggested)
1. Click on [this link](https://drive.google.com/drive/folders/1Y748L_hgFt3uQJcQRUp5z_oT0D_oAYvL?usp=sharing). It is a google drive folder with the data you will need.
2. Right click on `ew2.ipynb` and then on `Make a Copy`
3. Go in the folder `data` and for every file in the folder add a shortcut to your drive following these steps

    1. Right click on the file
    2. Click on `Add a shortcut to Drive`
    3. Select `My Drive`
    4. Click `ADD SHORTCUT`

4. Go to your own drive and right click on `ew2.ipynb`
5. Click `Open with` and select `Google Colaboratory`. If the option doesn't show follow these steps:

    1. Click on `Connect more apps`
    2. Go to `Search apps`
    3. Type `Colaboratory`
    4. Click on it and follow the installation

6. Once you manage to open the notebook with Google Colaboratory, go to `Runtime` -> `Change Runtime Type` and select GPU.

### Tutorial
https://user-images.githubusercontent.com/44053982/164013879-530c1715-463a-46a3-8066-bdfe0e9d5840.mp4

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
conda install -c conda-forge numpy pandas xarray matplotlib plotly tqdm optuna cartopy nc-time-axis ipykernel netcdf4 ipympl scikit-learn
```

Install machine learning package: either tensorflow (suggested if you don't have much experience with deep learning. Also the examples are implemented in tensorflow)
```
conda install -c conda-forge tensorflow
```
or pytorch (lower level programming with respect to tensorflow, but allows a more capillar and versatile control of what you are doing)
```
conda install pytorch torchvision cudatoolkit -c pytorch
```
