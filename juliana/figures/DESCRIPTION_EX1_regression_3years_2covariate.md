The policy can be divided into three time points: **Proposal** (June 20, 2017), **Approval** (June 5, 2018) and **Enforcement** (Jan 1, 2019). In this case, the regression line before the first dotted line is based on 14 months (April 2016 - May 2017), the regression line before the second dotted line is based on 12 months (June 2017 - May 2018), the regression line before the third dotted line is based on 7 months (June 2018 - December 2018), while the last regression line is based on the remaining months (January 2019 - April 2019).

```
y = A*x1 + B*x2 + C

where x1 is [0,1,2,...,36] for 37 months,
x2 is [0,2,4,...,72] for positive (times 2), [0,3,6,...,108] for neutral (times 3) and [0,1,2,...,36] for negative (times 1).

In the figure below:
  month: A
  month*sentiment: B
  constant: C
```



# Sentiment Analysis

## ecig


<p align="center">
  <img src="https://github.com/meettyj/Alcohol-on-Twitter/raw/master/juliana/figures/screenshots/EX1_regression_3years_2covariate/sentiment_propotion_ecig_vader_description.png" />
</p>

<p align="center">
  <img src="https://github.com/meettyj/Alcohol-on-Twitter/raw/master/juliana/figures/screenshots/EX1_regression_3years_2covariate/sentiment_propotion_ecig_vader.png" />
</p>



## tobacco

<p align="center">
  <img src="https://github.com/meettyj/Alcohol-on-Twitter/raw/master/juliana/figures/screenshots/EX1_regression_3years_2covariate/sentiment_propotion_tobacco_vader_description.png" />
</p>

<p align="center">
  <img src="https://github.com/meettyj/Alcohol-on-Twitter/raw/master/juliana/figures/screenshots/EX1_regression_3years_2covariate/sentiment_propotion_tobacco_vader.png" />
</p>
