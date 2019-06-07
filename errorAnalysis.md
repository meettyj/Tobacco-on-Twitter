
# Result
<p align="center">
  <img src="https://github.com/meettyj/Alcohol-on-Twitter/raw/master/result/resultOfRetraining.png" />
</p>

# Explanation
First table is what paper state. 

In the second table, just to make it clear, for the initial model, I mean the three models left by Jason. I retrain it and test it in test set to achieve the results. The blank I leave is not for unfinished experiment. It's only because the initial model only contains one specific classifier each time. For example, the alcohol classifier only use LR and first person classifier only use SVM.

Third table and fourth table are exactly the same, I make it a copy just to make comparison eaiser. In the fourth table, the data under green means the performance is higher or equal than the data in same position of first table. Similarly, yellow means the performance I achieve is lower, but the difference is lower or equal to 0.03 (difference ≤ 0.03). Red means the difference is bigger than 0.03 (difference ＞ 0.03).

# Conclusion
In general, I achieve almost satisfactory results. For the place where most yellow and red occurs (LR model in current, looking and reflecting), I have successfully made the performance same as the initial one (second table), but still much lower than the paper statement (first table). I have no idea how Jason generate the result in paper. Using the model he leaved and retraining, only got the same performance as what I did in grid search.
