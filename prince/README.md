## Description

prince is the name of server we run experiment, which is also the HPC server provided by NYU.

## To copy data from vidaserver to prince

Run on prince (**juliana directory**): 

```
screen
scp -r yijun@vidaserver1.poly.edu:/san_scratch/tuananh/tweets/geo/data/2019-01* .
```

## Unzip the files copied from vidaserver:

On prince server: 

```
./unzipFilesInDirectories.sh
```


## Note
- vidaserver: 
  ```
  ssh vidaserver1.poly.edu
  ```
- prince: 
  ```
  ssh gw.hpc.nyu.edu
  ssh prince.hpc.nyu.edu
  ```
  
## TODO
Filter out those e-cigarette related tweets in prince server.
  
  
  
