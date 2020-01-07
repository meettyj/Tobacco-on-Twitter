## Conclusion
- average confidence (aggrement) for 1st question (ecig): 91.41%
- average confidence (aggrement) for 2nd question (flavor): 89.91%

## Calculation process
For the labeling task in Figure Eight, we have two hierarchical questions, so we have two confidence score:
- **ecig_confidence**: Is this posting relevant to E-Cigarette?
- **flavor_confidence**: Is this posting relevant to flavor in E-Cigarette?

For each labeled tweet, we have ecig_confidence. if this tweet is relavant to E-Cigarette, then we goes to the second question.
In this case, this tweet has flavor_confidence.

I average all ecig_confidence and flavor_confidence to get
- avg_ecig_confidence = 91.41%
- avg_flavor_confidence = 89.91%

## Explanation for confidence
- confidence is the score provided by Figure Eight for each labeled tweets.
- it "represent the level of agreement between contributors" (cited from [here](https://success.figure-eight.com/hc/en-us/articles/202703075-Guide-to-Reports-Page-and-Options-Page)).
and it "weighted by the contributors’ trust scores" (cited from [here](https://success.figure-eight.com/hc/en-us/articles/201855939-Get-Results-How-to-Calculate-a-Confidence-Score), 
you can also find the way they calculate the confidence score in this page)

## Paper that used Figure Eight
- https://ieeexplore.ieee.org/abstract/document/8561283
- https://acl-bg.org/proceedings/2019/RANLPStud%202019/pdf/RANLPStud002.pdf

