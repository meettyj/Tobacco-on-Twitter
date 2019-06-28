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
    
  **Question: When people know their tweet violates the rule, are they tends to retweet it or leave it?**
  
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
  
  Worldwide alcohol/tobacco use?

- [140 character -> 280 character (September 2017)](https://blog.twitter.com/official/en_us/topics/product/2017/Giving-you-more-characters-to-express-yourself.html)

  [Survey about this change (November 2017)](https://blog.twitter.com/en_us/topics/product/2017/tweetingmadeeasier.html)

- [Remove trolls to improve healthy conversation environment (May 2018)](https://blog.twitter.com/en_us/topics/product/2018/Serving_Healthy_Conversation.html)

- Several safety actions (e.g. remove abuse):
  [(July 2017)](https://blog.twitter.com/en_us/topics/product/2017/Our-Safety-Work-Results-Update.html)
  [(March 2017)](https://blog.twitter.com/en_us/topics/product/2017/our-latest-update-on-safety.html)
  [(February 2017)](https://blog.twitter.com/en_us/topics/product/2017/an-update-on-safety.html)

- [Twitter rules](https://help.twitter.com/en/rules-and-policies/twitter-rules): 

  I was trying to find some history rules that Twitter declared, trying to find where the change is, and how they may influence people habits. However, it seems hard to find those past rule. All I find is a [general description of the change happened before 2016](https://www.vice.com/en_us/article/z43xw3/the-history-of-twitters-rules). Since the data we collected now are based on 2017 and the time after, even if we cannot get the specific changed sentence, we can get some view about how it changed [here on November 2017](https://blog.twitter.com/en_us/topics/company/2017/Clarifying_The_Twitter_Rules.html) and [here on December 2017](https://blog.twitter.com/en_us/topics/company/2017/safetypoliciesdec2017.html). I thought if we want to do some research based on the changing of twitter rule, we can trying to match it current rules, but currently I have no idea how to use it.



## Law (The Interrupted Time-Series Design)

Meaning of The Interrupted Time-Series Design: Some interruption occurs, based on time to evaluate the casual relationship.

Basically, if we want to find out how these kind of laws influence our daily use of tobacco, we need to build the relationship between 'the frequency we tweet tobacco' and 'how often we use tobacco in our daily life'. We cannot simply assume the more we tweet, the more we use. Can we?

Or if we want to find how people think of tobacco after some specific law, we gonna take a NLP analysis of the tweet content. 

### San Francisco banned flavored tobacco sales
[Initial proposal (June 20, 2017)](https://www.cnn.com/2017/06/22/health/san-francisco-vaping-menthols-ban-bn/index.html). 
[Proposal File](http://sfelections.sfgov.org/sites/default/files/Documents/candidates/Legal_Text_Repeal_of_Flavored_Tobacco_Products_Ban.pdf)

[Ban approved (June 5, 2018)](https://www.cnbc.com/2018/06/06/san-francisco-approves-ban-on-menthol-cigarettes-and-flavored-e-cigarette-liquids.html)

[Full enforcement of that law began (Jan 1, 2019)](https://www.kalw.org/post/san-francisco-banned-flavored-tobacco-sales-now-what#stream/0)

I thought maybe we can use Interrupted Time-Series experiment to evaluate the influence of this law brings to people's life. 

**Question1: Does this law decrease the use of tobacco in San Francisco? What are the people's attitudes towards tobacco at different stages of the law?**

Treatment: The time seperated by three time points (proposal, approval, enforcement). 

Outcome: The frequency of tweets posting related to tobacco within N days. 


Here we set the time of proposal as *t1*, the time of approval as *t2* and the time of enforcement as *t3*. In this case, we have

![](http://latex.codecogs.com/gif.latex?T<t1,Treat\=0;t1\\leq{T}<t2,Treat\=1;)
![](http://latex.codecogs.com/gif.latex?t2\\leq{T}<t3,Treat\=2;T\\geq{t3},Treat\=3)

Here T indicates Time. Given ![](http://latex.codecogs.com/gif.latex?N\\in\\{1,3,5,10,15,20,25,30\\}) and a specific time point ![](http://latex.codecogs.com/gif.latex?t\\in\\{t1,t2,t3\\}), we have

![](http://latex.codecogs.com/gif.latex?freq_{before_t}\=\\frac{\\sum_{i\=t-N}^{t}num_i(posting)}{N}),  ![](http://latex.codecogs.com/gif.latex?freq_{after_t}\=\\frac{\\sum_{i\=t}^{t+N}num_i(posting)}{N})

![](http://latex.codecogs.com/gif.latex?diff_t\=freq_{before_t}-freq_{after_t})

Here ![](http://latex.codecogs.com/gif.latex?freq_{before_t}) indicates frequency before Time t. ![](http://latex.codecogs.com/gif.latex?freq_{after_t}) indicates frequency after Time t. 
If ![](http://latex.codecogs.com/gif.latex?diff_t<0), indicates the use of tobacco has decreased. 
If ![](http://latex.codecogs.com/gif.latex?diff_t>0), indicates the use of tobacco has increased. 
If ![](http://latex.codecogs.com/gif.latex?diff_t\\to0), indicates the law at time point *t* has no influence. 



**Question2: Does this law increase the use of alcohol in San Francisco?**

Treatment: Three time points (proposal, approval, enforcement). 

Outcome: The frequency of tweets posting related to alchol within N days. 

**Question3: Does this law increase the use of tobacco in nearby city?**

Treatment: Three time points (proposal, approval, enforcement). 

Outcome: The frequency of tweets posting related to tobacco within N days. 


### Laws regarding indoor e-cigarette use and smoking in restaurants, bars, and worksites

[State Laws Regarding Indoor Public Use, Retail Sales, and Prices of Electronic Cigarettes](https://www.cdc.gov/mmwr/volumes/66/wr/mm6649a1.htm)

[List of vaping bans in the United States](https://en.wikipedia.org/wiki/List_of_vaping_bans_in_the_United_States)

Not too many state proposed the law in 2017, 2018 and 2019. Most state band vaping before 2017.

**New York (November 22, 2017)**: Statewide vaping ban. A law went into effect prohibiting vaping everywhere that smoking is banned, including all enclosed workplaces, bars and restaurants.

**Rhode Island (2018)**: Statewide vaping ban.

### Does taxing on e-cigarette prevent people to use them?

[related law effective time](https://publichealthlawcenter.org/sites/default/files/States-with-Laws-Taxing-ECigarettes-March2019.pdf)

The evaluation method is same as before. Use frequency to determine the influence. Can incorporate geographic information. States that has related laws are California, Delaware, Kansas, New Jersey. The law in these four states are effective since 2017.













