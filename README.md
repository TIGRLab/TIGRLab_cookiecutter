TIGRLab Analysis Cookie-Cutter
==================================

For use in tigrlab projects. 


install or module load cookiecutter, then type in `cookiecutter https://github.com/TIGRLab/TIGRLab_cookiecutter.git` to get started.


Cookiecutter is a way to create the directory structure and even some automatic documentation for a project. We created this to help structure our projects in a consistent, reproducible manner that other lab members can interpret easily.

If you are setting up an analysis project in the lab (or remoting in), you can `module load cookiecutter`. Then, simply navigate to your scratch/ or projects/ and type in `cookiecutter $tigrlab_default_template` to get started. This will create a cookiecutter template in your current working directory. 

Here is an example of responding to the prompts.


```
full_name [Tigrlab User]: Gabrielle Herman
email [email@gmail.com]: fakeemail@domain.com
project_name [My Analysis Project]: Creating a Sample Project
short_description [Analysing TIGR roar waveforms]: This project aims to create a sample cookiecutter.
project_folder_name [my_repo_and_folder]: tigr_sample_proj
github_username [tigr_usr]: gabiherman
```

Alternatively, you can install cookiecutter at home and use cookiecutter based on the github repo. `cookiecutter https://github.com/TIGRLab/TIGRLab_cookiecutter.git`.


After setup, please take a look at the README file for instructions on how to initialize your project in a git repo. 

Here are instructions for installing cookiecutter: https://cookiecutter.readthedocs.io/en/1.7.0/installation.html#install-cookiecutter


Project Organization
-----------------------------------

    .
    ├── README.md          <- The top-level README
    ├── .gitignore         <- Files to not upload to github - by default includes /data
    ├── LICENSE            <- usage license if applicable
    ├── data
    │   ├── processed      <- The final dataset (can include subfolders etc)
    │   └── raw            <- The original dataset, generally a link to minimally preprocessed data
    │
    ├── notebooks          <- Jupyter/R notebooks for analysis workflow - Naming should begin with a number, followed by an underscore and a description (e.g. 01_compile_demographics.Rmd)
    │
    ├── docs/references    <- Data dictionaries, manuals, and all other explanatory materials
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc. Summaries, tather than code.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment (if applicable)
    │
    ├── code/src           <- Source code for use in this project (virtual environments, bash scripts, etc)

All the best,
Gabi
