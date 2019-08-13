We can do experiments on all states that has tax since 2017, which is California (4/1/2017), Kansas (7/1/2017) Delaware (1/1/2018) and New Jersey (9/29/2018). 

For states that has tax since 2016, for example, West Virginia (7/1/2016) and Pennsylvania (7/13/2016), since the data from January to March in 2016 is not complete, we don't have enough data to run experiments on these two states.

# California (4/1/2017)

- Oregon
- Nevada
- Arizona

# Kansas (7/1/2017)

- Nebraska
- Missouri
- Oklahoma
- Colorado

# Delaware (1/1/2018)
- New Jersey
- Pennsylvania
- Maryland
- Washington D.C.

# New Jersey (9/29/2018)
- New York
- pennsylvania
- connecticut
- Delaware
- Maryland

# Experiments
## For getting states name
Running on test file which contains 160,577 tweets. we can successfully recognize 156,375 tweets that posted in specific state. Exception are:
- Those only with coordinates but no place name: 17
- Those with irregular place name (e.g. HEAVEN/Williamsburg, Brooklyn): 653
- Those not in United States: 3532

# Note
## States features
These features are used for analyzing the result after Bayes' theorem. 
- population
- number of tweets poster
- number of tweets

## Population Estimation of U.S. states:
- Wikipedia (July, 2019. Couldn't find reference): https://simple.wikipedia.org/wiki/List_of_U.S._states_by_population#cite_note-2
- United States Census Bureau (July, 2018): https://www.census.gov/newsroom/press-kits/2018/pop-estimates-national-state.html



