# For crawling data from Server (Twitter Pull Data):
Please follow the step below:

Download Twitter Pull Data from server: **downloadTwitterPullData.ipynb**

Extract Json file from Tar file: **unzipTarFile.ipynb**

Get Specific city tweets (e.g. San Francisco): **getSpecificCity.ipynb**

## Some other processing
Extract hookah related tweets and location information from our data based on the method described in [this paper](https://www.jmir.org/2019/7/e12443/): **getHookahAndLocation.ipynb**

If you want to compact all month (or say, weeks) data in one file and you do have enough space in your disk: **getMonthTweets.ipynb**


## Results
- There are 87764 tweets posted in San Francisco in January 2017.
- There are 3739 hookah related tweets appeared in January 2017, while the location information in this month contains 14045 different cities.
  
  I thought the reason why we get this low number of hookah related tweets is, all tweets data we collect are based on they have geo information, while the data they (the authors of the paper) collected are every tweets in the designated time period, ignoring the geo information.



# For crawling data from Twitter API:
Please see **getUserInfo.py** and **getUserTweets.py**

# TODO
1. Get percentage information.
2. Get nearby city information.
