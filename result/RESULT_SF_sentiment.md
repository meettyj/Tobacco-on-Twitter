# Number
```
# Number
average_num_per_person_tweets_SF_ecig = []


# SF_allECigarette
SF_allECigarette_2017 = [59,65,90,59,67,88,74,89,47,50,76,122]
SF_allECigarette_2018 = [111,103,102,99,81,92,127,106,92,83,141,113]
SF_allECigarette_2019 = [130,105,74,92]
SF_allECigarette_total = []
SF_allECigarette_total.extend(SF_allECigarette_2017)
SF_allECigarette_total.extend(SF_allECigarette_2018)
SF_allECigarette_total.extend(SF_allECigarette_2019)
print('length of SF_allECigarette_total: ', len(SF_allECigarette_total))


# not_SF_allECigarette
not_SF_allECigarette_2017 = [17983, 13759, 14675, 14218, 13013, 13534, 13493, 14000, 6886, 9296, 15564, 15559]
not_SF_allECigarette_2018 = [16357, 14535, 16351, 15982, 15461, 16211, 18743, 17293, 19076, 15024, 18918, 17560]
not_SF_allECigarette_2019 = [18566, 16190, 13614, 13234]
not_SF_allECigarette_total = []
not_SF_allECigarette_total.extend(not_SF_allECigarette_2017)
not_SF_allECigarette_total.extend(not_SF_allECigarette_2018)
not_SF_allECigarette_total.extend(not_SF_allECigarette_2019)
print('length of not_SF_allECigarette_total: ', len(not_SF_allECigarette_total))


# allECigarette
allECigarette_total = []
for i in range(28):
    allECigarette_total.append(SF_allECigarette_total[i]+not_SF_allECigarette_total[i])
print('length of allECigarette: ', len(allECigarette_total))


# allSF
allSF_2017 = [404518, 350143, 358222, 326842, 326461, 332603, 312882, 323315, 148187, 205925, 296740, 257645]
allSF_2018 = [278884, 259869, 304292, 278291, 287698, 282691, 287065, 262239, 284484, 244884, 264046, 245877]
allSF_2019 = [274852, 253351, 225549, 252680]
allSF_total = []
allSF_total.extend(allSF_2017)
allSF_total.extend(allSF_2018)
allSF_total.extend(allSF_2019)
print('length of allSF_total: ', len(allSF_total))


# Number of users that tweets SF ecig.
users_SF_ecig_2017 = [50, 52, 73, 53, 53, 66, 67, 71, 38, 45, 65, 69]
users_SF_ecig_2018 = [75, 68, 68, 75, 73, 74, 87, 85, 76, 69, 119, 90]
users_SF_ecig_2019 = [110, 84, 60, 67]
users_SF_ecig_total = []
users_SF_ecig_total.extend(users_SF_ecig_2017)
users_SF_ecig_total.extend(users_SF_ecig_2018)
users_SF_ecig_total.extend(users_SF_ecig_2019)
print('length of users_SF_ecig_total: ', len(users_SF_ecig_total))


# average number of per person tweets about ecig.
for i in range(28):
    average_num_per_person_tweets_SF_ecig.append(SF_allECigarette_total[i]/users_SF_ecig_total[i])
print('length of average_num_per_person_tweets_SF_ecig: ', len(average_num_per_person_tweets_SF_ecig))


# allTweets
allTweets_2017 = [64761879, 49292002, 51379810, 46841051, 45592367, 46897952, 50163222, 51079160, 22112648, 31365136, 46232294, 43487766]
allTweets_2018 = [46059070, 40432909, 47289301, 45660765, 44166238, 44212483, 45858463, 39900707, 45395994, 37985764, 42937313, 41362576]
allTweets_2019 = [44209494, 38750216, 32702554, 33860264]
allTweets_total = []
allTweets_total.extend(allTweets_2017)
allTweets_total.extend(allTweets_2018)
allTweets_total.extend(allTweets_2019)
print('length of allTweets_total: ', len(allTweets_total))


# ---------------------- Sentiment analysis by vader ----------------------
# positive
vader_positive_2017 = [22, 23, 37, 21, 27, 32, 25, 33, 17, 12, 22, 40]
vader_positive_2018 = [38, 36, 29, 31, 26, 31, 33, 35, 39, 23, 42, 26]
vader_positive_2019 = [36, 35, 20, 39]
vader_positive_total = []
vader_positive_total.extend(vader_positive_2017)
vader_positive_total.extend(vader_positive_2018)
vader_positive_total.extend(vader_positive_2019)
print('length of vader_positive_total: ', len(vader_positive_total))

# neutral
vader_neutral_2017 = [29, 31, 38, 24, 29, 43, 38, 42, 23, 26, 42, 53]
vader_neutral_2018 = [44, 47, 55, 46, 35, 43, 73, 51, 35, 45, 62, 59]
vader_neutral_2019 = [68, 52, 35, 31]
vader_neutral_total = []
vader_neutral_total.extend(vader_neutral_2017)
vader_neutral_total.extend(vader_neutral_2018)
vader_neutral_total.extend(vader_neutral_2019)
print('length of vader_neutral_total: ', len(vader_neutral_total))

# negative
vader_negative_2017 = [8, 11, 15, 14, 11, 13, 11, 14, 7, 12, 12, 29]
vader_negative_2018 = [29, 20, 18, 22, 20, 18, 21, 20, 18, 15, 37, 28]
vader_negative_2019 = [26, 18, 19, 22]
vader_negative_total = []
vader_negative_total.extend(vader_negative_2017)
vader_negative_total.extend(vader_negative_2018)
vader_negative_total.extend(vader_negative_2019)
print('length of vader_negative_total: ', len(vader_negative_total))


```



# Proportion
```
# Proportion
propotion_SF_ecig_in_all_ecig = []
propotion_SF_ecig_in_all_SF_tweets = []
propotion_SF_in_all_tweets = []
propotion_positive_ecig = []
propotion_neutral_ecig = []
propotion_negative_ecig = []

# propotion of SF e-cig tweets in all e-cig tweets.
for i in range(28):
    propotion_SF_ecig_in_all_ecig.append((SF_allECigarette_total[i]/allECigarette_total[i])*100)
print('length of propotion_SF_ecig_in_all_ecig: ', len(propotion_SF_ecig_in_all_ecig))


# propotion of SF e-cig tweets in all SF tweets.
for i in range(28):
    propotion_SF_ecig_in_all_SF_tweets.append((SF_allECigarette_total[i]/allSF_total[i])*100)
print('length of propotion_SF_ecig_in_all_SF_tweets: ', len(propotion_SF_ecig_in_all_SF_tweets))


# propotion of SF tweets in total tweets.
for i in range(28):
    propotion_SF_in_all_tweets.append((allSF_total[i]/allTweets_total[i])*100)
print('length of propotion_SF_in_all_tweets: ', len(propotion_SF_in_all_tweets))


# ---------------------- Sentiment analysis by vader ----------------------
for i in range(28):
    propotion_positive_ecig.append((vader_positive_total[i]/SF_allECigarette_total[i])*100)
print('length of propotion_positive_ecig: ', len(propotion_positive_ecig))

for i in range(28):
    propotion_neutral_ecig.append((vader_neutral_total[i]/SF_allECigarette_total[i])*100)
print('length of propotion_neutral_ecig: ', len(propotion_neutral_ecig))

for i in range(28):
    propotion_negative_ecig.append((vader_negative_total[i]/SF_allECigarette_total[i])*100)
print('length of propotion_negative_ecig: ', len(propotion_negative_ecig))

```










