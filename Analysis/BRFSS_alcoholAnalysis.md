# Features
## Questions
- **ALCDAY5:** During the past 30 days, how many days per week or per month did you have at least one drink of any alcoholic beverage such as beer, wine, a malt beverage or liquor?
- **AVEDRNK2:** One drink is equivalent to a 12-ounce beer, a 5-ounce glass of wine, or a drink with one shot of liquor. During the past 30 days, on the days when you drank, about how many drinks did you drink on the average? 
- **DRNK3GE5:** Considering all types of alcoholic beverages, how many times during the past 30 days did you have 5 or more drinks for men or 4 or more drinks for women on an occasion?
- **MAXDRNKS:** During the past 30 days, what is the largest number of drinks you had on any occasion?

## Statistics
- **DRNKANY5:** Adults who reported having had at least one drink of alcohol in the past 30 days. (based on ALCDAY5)
- **DROCDY3_:** Drink-occasions-per-day. (based on ALCDAY5, result in percentage)
- **_RFBING5:** Binge drinkers.  (males having five or more drinks on one occasion, females having four or more drinks on one
occasion) (based on ALCDAY5 and DRNK3GE5)
- **_DRNKWEK:** Total number of alcoholic beverages consumed per week. (AVEDRNK2 * DROCDY3_ * 7, result in percentage)
- **_RFDRHV5:** Heavy drinkers. (adult men having more than 14 drinks per week and adult women having more than 7 drinks per week) (based on _DRNKWEK and sex)

## Example
Take id=20001 as an example. 

**Questions:**
During the past 30 days, he/she drinks twice a week, each time have one drink(e.g. 12-ounce beer). Didn't have 5 or 4 drinks within one occasion. Have 2 drinks at most for one occasion. 

**Statistics:**
He/She had at least 1 drink during the past 30 days. Got 29% for drink occasions per day. Isn't a binge drinker. Consumed 2 alcoholic beverages in total per week. Isn't a heavy drinker.


# Data

<img src="https://github.com/meettyj/Alcohol-on-Twitter/raw/master/result/BRFSS_alcohol.png" />

It contains 450,016 rows of data in total.


# Appendix
Specific calculation formula of statistic features can be found in: [BRFSS Calculated Variables](https://www.cdc.gov/brfss/annual_data/2015/pdf/2015_calculated_variables_version4.pdf)





