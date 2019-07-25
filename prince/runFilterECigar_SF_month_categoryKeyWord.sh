#!/bin/bash
#SBATCH --nodes=4
#SBATCH --ntasks-per-node=2
#SBATCH --cpus-per-task=2
#SBATCH --time=6:00:00
#SBATCH --mail-type=END
#SBATCH --mail-user=eddie.tian@nyu.edu


python filterECigar_SF_month_categoryKeyWord.py