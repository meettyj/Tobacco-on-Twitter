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
  The data is available at the vidaserver1 machine:
  
  - /san_data/tuananh/tweets/geo/data (Jan-Sept 2016)
  
  - /san_scratch/tuananh/tweets/geo/data (Oct 2016 to May 2019)

- prince: 
  ```
  ssh gw.hpc.nyu.edu
  ssh prince.hpc.nyu.edu
  ```

## Jupyter Notebook
Running the following script in **/scratch/yt1506/** directory:
```
jupyter notebook --no-browser
```

Sometimes the tunnel didn't work, please check the port number and process with keyword 'jupyter'. Most time is because there are someone else are running notebook and make your port number lag. Setting tunnel in Xshell is always great. If this situation happens a lot, suggest setting specific port number in jupyter notebook.

```
ps -ef | grep jupyter
```


## TODO
Filter out those e-cigarette related tweets in prince server.
  
  
  
