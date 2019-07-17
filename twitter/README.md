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

- All locations related to San Francisco in January 2017 is:

  San Francisco, San Francisco Downtown Hostel, South San Francisco, San Francisco de Borja, San Francisco International Airport (SFO), 'The Ritz-Carlton, San Francisco', Hilton San Francisco Union Square, San Francisco-Oakland-San Jose CA, Nordstrom San Francisco Centre, 
San Francisco del Oro, Pullman San Francisco Bay, SF Moto, SFO Airport - Arrival Hall.


  Among them, a lot is some hotel name and some are location in Mexico. **Those real in San Francisco are:**

  San Francisco, San Francisco Downtown Hostel, San Francisco International Airport (SFO), The Ritz-Carlton, 'The Ritz-Carlton, San Francisco', Hilton San Francisco Union Square, Nordstrom San Francisco Centre, SF Moto, SFO Airport - Arrival Hall.




# For crawling data from Twitter API:
Please see **getUserInfo.py** and **getUserTweets.py**


