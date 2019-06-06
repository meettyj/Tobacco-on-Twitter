# Stuck?
If you stuck in grid search (e.g. gridSearchBehaviorLR.ipynb), try move it out of the current directory. Running in the root director would solve this problem. The reason is the grid search function within the sklearn need to import package (In this case, is pipelines etc.) directly from the current file path. 
