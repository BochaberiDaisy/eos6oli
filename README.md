# Model: eos60li - Aqueous Solubility Prediction

## Overview
This repository contains the model validation task for the Outreachy Summer Internship 2024 contributions to Ersilia.


## Model Information
- Input: `Compound`
- Input Shape: `Single`
- Task: git add`Regression`
- Output: `Experimental value`
- Output Type: `Float`
- Output Shape: `Single`
- Interpretation: `Predicted LogS (log of the solubility)`


## Steps to Reproduce
### 1. Install Ersilia Model Hub
Install Ersilia Model Hub on your system [here](https://ersilia.gitbook.io/ersilia-book/ersilia-model-hub/installation).

### 2. Download Model and Run
Run the following commands on your terminal to download and run the model on your system.

```
ersilia -v fetch eos6oli
ersilia -v serve eoso6oli
ersilia api run -i data/input.csv -o data/output.csv
```

## Dataset
The dataset used on the model for checking for model bias was downloaded from [here](https://raw.githubusercontent.com/dataprofessor/data/master/delaney.csv). The dataset was from the research conducted by John S. Delaney on [ESOL:  Estimating Aqueous Solubility Directly from Molecular Structure](https://pubs.acs.org/doi/10.1021/ci034243x).

# References
- [Ersilia Model Hub](https://ersilia.gitbook.io/ersilia-book/ersilia-model-hub/installation)
- [ESOL:  Estimating Aqueous Solubility Directly from Molecular Structure](https://pubs.acs.org/doi/10.1021/ci034243x)
- [SolTraNet](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8900744/)