# Tobacco-on-Twitter

This repository contains source code for ICWSM 2020 paper: 

[Quasi-experimental Designs for Assessing Response on Social Media to Policy Changes](https://arxiv.org/abs/2003.13783)

## Directories Explanation
- Analysis: analysis of the first stage of our research ideas
- bkResearchCluster: data preprocessing in the brooklyn research cluster
- google_drive: data processing from google drive
- juliana: primary directory, including data processing, figure and table generation, regression, qualitative checking and sentiment analysis for the data from juliana group
- prince: data preprocessing in the server "prince"
- reddit: everying relevant to reddit data
- result: detailed record and explanation of the results
- twitter: preprocessing of the Twitter API data
- tobaocco: extraction of relevant tobacco data


## Environment Requirement

Strongly Suggest using [Anaconda](https://docs.anaconda.com/anaconda/install/) to configure your environment. Each required package is indicate in front of the code. Simple requirement examples are 
- Python 3
  - `pandas` >= 0.18
  - `numpy` >= 1.11
  - `sklearn` = 0.17
- Jupyter
  The experiments are written in Jupyter notebooks. Please follow the [Jupyter installation instructions](https://jupyter.org/install), and ensure you have version 4 or later:
  ```bash
  $ jupyter --version
  4.2.0
  ```

## Citation
Conference preprint coming soon.



