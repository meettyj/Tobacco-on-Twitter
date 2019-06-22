# [Causal discovery in social media using quasi-experimental designs](https://dl.acm.org/citation.cfm?id=1964859)

## Matched Design
Identify pairs of units where one has received a treatment and the other has not but who are otherwise similar.

- Does xxx cause yyy to post tweet about drinking?

  Treatment: xxx

  output: post tweet about drinking.

- Does posting of drinking cause zzz to www?

  Treatment: posting of drinking.

  output: www
  
**Possible Topics:** 
  - Music
  - sex
  - Alcohol
  - Drug
  - Money
  - Food
  - Education
  - Sleeping
  - Crying
  - Fighting
  - Illegal acts (e.g. stealing)
  - Effect of alcohol on life quality
  - Disease
  - Male and Female
  - Body Weight
  - break up
  - **Does drinking alcohol cause people to smoking or taking (more) drug?**
  
    This is interesting, but how can we use what we have now (the data) to answer this question?
  - Does drinking alcohol cause people to post more tweets?
  - Does drinking alcohol cause people to be more offensive? (e.g. more dirty word)
  - Attitude towards life by annalyzing attitude towards alcohol?
  - the different possible dissease that may happened in male and female. (e.g. breast cancer & fetal alcohol spectrum disorder (FASD) in female) 

## The Natural Experiment Design
Based on the change of social media itself. I guess we need to check the updating history of Twitter. Here is the general updating history of Twitter: https://blog.twitter.com/en_us/topics/product.html

- [More clarity on reported Tweets and enforcement (October 2018)](https://blog.twitter.com/en_us/topics/product/2018/more-clarity-on-reported-tweets-and-enforcement.html)
    
  Question: When people know their tweet violates the rule, are they tends to retweet it or leave it?
  
  Treatment: They don't know (Treat = 0). They know (Treat = 1). 
  
  Outcome: The frequency of tweets posting within N days. 

  ![](http://latex.codecogs.com/gif.latex?T<t,Treat\=0;T\\geq{t},Treat\=1)

  Here T indicates Time. Given ![](http://latex.codecogs.com/gif.latex?N\\in\\{1,3,5,10,15,20,25,30\\}), we have
    
  ![](http://latex.codecogs.com/gif.latex?freq_{before}\=\\frac{\\sum_{i\=t-N}^{t}num_i(posting)}{N}),  ![](http://latex.codecogs.com/gif.latex?freq_{after}\=\\frac{\\sum_{i\=t}^{t+N}num_i(posting)}{N})
  

  ![](http://latex.codecogs.com/gif.latex?diff\=freq_{before}-freq_{after})

  Here ![](http://latex.codecogs.com/gif.latex?freq_{before}) indicates frequency before Time t. ![](http://latex.codecogs.com/gif.latex?freq_{after}) indicates frequency after Time t. 
  If ![](http://latex.codecogs.com/gif.latex?diff<0), indicates people tend to retweet when they know their tweets violate the rule. 
  If ![](http://latex.codecogs.com/gif.latex?diff>0), indicates people tend to leave their tweets when they know their tweets violate the rule. 
  If ![](http://latex.codecogs.com/gif.latex?diff\\to0), indicates the policy has no influence. 

  We also need to make sure, if we use frequency in a period of time to evaluate the difference, no other influential policy updating within that time.



- [Introducing Twitter Lite (April 2017)](https://blog.twitter.com/en_us/topics/product/2017/introducing-twitter-lite.html)
- [Twitter Lite available in 24 more countries (November 2017)](https://blog.twitter.com/en_us/topics/product/2017/twitter-lite-in-the-google-play-store-in-24-more-countries.html) 
- [140 character -> 280 character (September 2017)](https://blog.twitter.com/official/en_us/topics/product/2017/Giving-you-more-characters-to-express-yourself.html)

  [Survey about this change (November 2017)](https://blog.twitter.com/en_us/topics/product/2017/tweetingmadeeasier.html)

- [Remove trolls to improve healthy conversation environment (May 2018)](https://blog.twitter.com/en_us/topics/product/2018/Serving_Healthy_Conversation.html)

- Several safety actions (e.g. remove abuse):
  [(July 2017)](https://blog.twitter.com/en_us/topics/product/2017/Our-Safety-Work-Results-Update.html)
  [(March 2017)](https://blog.twitter.com/en_us/topics/product/2017/our-latest-update-on-safety.html)
  [(February 2017)](https://blog.twitter.com/en_us/topics/product/2017/an-update-on-safety.html)

- [Twitter rules](https://help.twitter.com/en/rules-and-policies/twitter-rules): 

  I was trying to find some history rules that Twitter declared, trying to find where the change is, and how they may influence people habits. However, it seems hard to find those past rule. All I find is a [general description of the change happened before 2016](https://www.vice.com/en_us/article/z43xw3/the-history-of-twitters-rules). Since the data we collected now are based on 2017 and the time after, even if we cannot get the specific changed sentence, we can get some view about how it changed [here on November 2017](https://blog.twitter.com/en_us/topics/company/2017/Clarifying_The_Twitter_Rules.html) and [here on December 2017](https://blog.twitter.com/en_us/topics/company/2017/safetypoliciesdec2017.html). I thought if we want to do some research based on the changing of twitter rule, we can trying to match it current rules, but currently I have no idea how to use it.




## The Interrupted Time-Series Design
Some interruption occurs, based on time to evaluate the casual relationship.


## Law





