#!/bin/bash
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=2000
#SBATCH --time=6:00:00
#SBATCH --mail-type=END
#SBATCH --mail-user=eddie.tian@nyu.edu


python detectTobacco.py