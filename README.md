# Generative Molecular Design for Novel Drug Cancer Candidates

## Project Overview

This project aims to accelerate drug discovery by generating novel molecules that exhibit desired properties. As such, this repository contains a comprehensive pipeline for generative molecular design using the ATOM GMD Framework. The project leverages two deep learning based modes, JT-VAE and Autogrow4, for molecular optimization. To evaluate the molecules optimized by both models, we employed optimization parameter manipulation, initial population fine tuning, and extensive visualization techniques to provide detailed comparisons between different models. 

## Team Structure

1. Gauri Samith<sup>*</sup> (gs3280@columbia.edu)
2. Arjun Bhan (ab5666@columbia.edu)
3. Nicole Brye (nab2217@columbia.edu)
4. Elie Chemouni (ec3778@columbia.edu)

<sup>*</sup> Team Leader

## Repository Structure

```
├── code/                       # Code files 
│   ├── FNLGMD/                 # Main GMD repository contained as a sub-module. This repository was forked from here: https://github.com/SeanTBlack/FNLGMD
│   └── results/                # Results files 
│   └── data/                   # Data files to run Autogrow4 and JTVAE models
│   └── config/                 # Config files
│   └── notebooks/              # Notebooks containing our personal work
├── README.md                   # Project README (this file)
```

## About the Repository
This repository contains the submodule / framework that we used to run both JTVAE and AutoGrow models, the configuration files with the parameters used to run the models, the data, and notebooks containing our personal work. Please refer to the `notebooks` folder, as well as the individual branches with our names labeled to see our personal work on this project and the results and figures generation process.

## Acknowledgements

We would like to express our gratitude and appreciation to our industry mentors <b>Pinyi Lu</b>, <b>Naomi Ohashi</b>, and <b>Justin Overhulse</b> for the guidance and professional support. We would additionally like to thank <b>Sining Chen</b>, <b>Swasthi P. Rao</b>, and <b>Savannah Thais</b> for an excellent semester. Finally, we would also like to thank the following organizations for their support:

* Columbia University
* Frederick National Laboratory
* Atom Consortium
