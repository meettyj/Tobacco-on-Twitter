#!/bin/bash

# ssh -L 9000:prince.hpc.nyu.edu:9000
ssh -R 9000:localhost:9000 yt1506@prince.hpc.nyu.edu # Not working

jupyter notebook --no-browser --port 9000