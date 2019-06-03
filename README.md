# Alcohol-on-Twitter

Exetension of previous work: [jxnl/nyu-twipsy](https://github.com/jxnl/nyu-twipsy) and [tj2huang/nyu-research](https://github.com/tj2huang/nyu-research)

## Environment Requirement

Strongly Suggest using [Anaconda](https://docs.anaconda.com/anaconda/install/) to configure your environment.
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
For those who are sick of constantly installing specific versions of packages, complete environment information that supports all of the experiments can be found in [environment.yml](). You can simply create the exactly same environment by following the instruction of [Creating an environment from an environment.yml file](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file)


## Test your setup
```
import pandas
import numpy as np
import sklearn

for module in (pandas, np, sklearn):
    print(module.__name__, module.__version__)
```
E.g., on my computer, I see:
```
pandas 0.23.0
numpy 1.16.3
sklearn 0.17
```

## How to run
Directories start with `'level_'` contain the related code of classifiers within different level. Follow the [jupyter instruction](https://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/execute.html) to run notebook and open the one you are interested.

## Classifiers
The structure of classfiers can be seen in [compareStructure.md](https://github.com/meettyj/Alcohol-on-Twitter/blob/master/compareStructure.md). If you want to check it yourself, make sure you are in the latest version of sklearn (e.g. 0.21 works well currently). sklearn 0.17 doesn't support complete structure visualization.

## Records
Specific information can be seen in [log.md](https://github.com/meettyj/Alcohol-on-Twitter/blob/master/log.md)
