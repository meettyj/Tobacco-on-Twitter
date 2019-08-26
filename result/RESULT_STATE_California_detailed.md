# Number

```
# Number

# ----------------------------- California -----------------------------
# California_allECigarette_2017
California_allECigarette_2017 = [2367, 1988, 2092, 1805, 1737, 1771, 1909, 2033, 976, 1174, 1961, 2008]
print('length of California_allECigarette_2017: ', len(California_allECigarette_2017))

# not_California_allECigarette_2017
not_California_allECigarette_2017 = [15672, 11836, 12673, 12472, 11343, 11850, 11658, 12056, 5957, 8171, 13678, 13673]
print('length of not_California_allECigarette_2017: ', len(not_California_allECigarette_2017))

# allECigarette_2017
allECigarette_2017 = []
for i in range(12):
    allECigarette_2017.append(California_allECigarette_2017[i]+not_California_allECigarette_2017[i])
print('length of allECigarette_2017: ', len(allECigarette_2017))


# allCalifornia_2017
allCalifornia_2017 = [7688806, 5950614, 6130864, 5623066, 5542298, 5872374, 6284243, 6242231, 2686895, 3874158, 5584508, 5218406]
print('length of allCalifornia_2017: ', len(allCalifornia_2017))


# Number of users that tweets ecig in California.
users_California_ecig_2017 = [1313, 1131, 1230, 1097, 1084, 1149, 1264, 1246, 647, 852, 1351, 1397]
print('length of users_California_ecig_2017: ', len(users_California_ecig_2017))


# average number of per person tweets about ecig in California.
average_num_per_person_tweets_California_ecig = []
for i in range(12):
    average_num_per_person_tweets_California_ecig.append(California_allECigarette_2017[i]/users_California_ecig_2017[i])
print('length of average_num_per_person_tweets_California_ecig: ', len(average_num_per_person_tweets_California_ecig))


# Number of users that tweets in California
users_California_2017 = [333885, 307678, 325899, 312275, 309270, 323365, 336303, 330514, 231445, 271542, 316768, 300338]
print('length of users_California_2017: ', len(users_California_2017))

# average number of per person tweets in California.
average_num_per_person_tweets_California = []
for i in range(12):
    average_num_per_person_tweets_California.append(allCalifornia_2017[i]/users_California_2017[i])
print('length of average_num_per_person_tweets_California: ', len(average_num_per_person_tweets_California))

# allTweets
allTweets_2017 = [64761879, 49292002, 51379810, 46841051, 45592367, 46897952, 50163222, 51079160, 22112648, 31365136, 46232294, 43487766]
print('length of allTweets_2017: ', len(allTweets_2017))

# Sentiment analysis
vader_positive_California_2017 = [775, 667, 719, 580, 590, 565, 605, 693, 328, 378, 645, 672]
vader_neutral_California_2017 = [1187, 1025, 1058, 942, 874, 891, 975, 991, 500, 582, 936, 891]
vader_negative_California_2017 = [405, 296, 315, 283, 273, 315, 329, 349, 148, 214, 380, 445]
print('length of vader_positive_California_2017: ', len(vader_positive_California_2017))
print('length of vader_neutral_California_2017: ', len(vader_neutral_California_2017))
print('length of vader_negative_California_2017: ', len(vader_negative_California_2017))

print('----------------------------------')
# ----------------------------- Oregon -----------------------------

# Oregon_allECigarette_2017
Oregon_allECigarette_2017 = [261, 195, 233, 221, 258, 263, 273, 257, 119, 152, 237, 284]
print('length of Oregon_allECigarette_2017: ', len(Oregon_allECigarette_2017))

# not_Oregon_allECigarette_2017
not_Oregon_allECigarette_2017 = [17778, 13629, 14532, 14056, 12822, 13358, 13294, 13832, 6814, 9193, 15402, 15397]
print('length of not_Oregon_allECigarette_2017: ', len(not_Oregon_allECigarette_2017))

# allOregon_2017
allOregon_2017 = [576389, 451267, 489471, 432418, 409505, 414368, 441048, 460374, 209586, 283148, 430226, 383564]
print('length of allOregon_2017: ', len(allOregon_2017))


# Number of users that tweets ecig in Oregon.
users_Oregon_ecig_2017 = [121, 93, 118, 123, 103, 106, 124, 139, 64, 98, 156, 164]
print('length of users_Oregon_ecig_2017: ', len(users_Oregon_ecig_2017))


# average number of per person tweets about ecig in Oregon.
average_num_per_person_tweets_Oregon_ecig = []
for i in range(12):
    average_num_per_person_tweets_Oregon_ecig.append(Oregon_allECigarette_2017[i]/users_Oregon_ecig_2017[i])
print('length of average_num_per_person_tweets_Oregon_ecig: ', len(average_num_per_person_tweets_Oregon_ecig))


# Number of users that tweets in Oregon
users_Oregon_2017 = [28914, 26389, 27777, 26903, 26769, 28342, 29185, 31473, 20171, 23160, 27581, 25123]
print('length of users_Oregon_2017: ', len(users_Oregon_2017))

# average number of per person tweets in Oregon.
average_num_per_person_tweets_Oregon = []
for i in range(12):
    average_num_per_person_tweets_Oregon.append(allOregon_2017[i]/users_Oregon_2017[i])
print('length of average_num_per_person_tweets_Oregon: ', len(average_num_per_person_tweets_Oregon))

# Sentiment analysis
vader_positive_Oregon_2017 = [107, 82, 100, 87, 94, 105, 103, 72, 39, 43, 78, 84]
vader_neutral_Oregon_2017 = [108, 85, 97, 106, 139, 127, 137, 148, 60, 84, 108, 139]
vader_negative_Oregon_2017 = [46, 28, 36, 28, 25, 31, 33, 37, 20, 25, 51, 61]
print('length of vader_positive_Oregon_2017: ', len(vader_positive_Oregon_2017))
print('length of vader_neutral_Oregon_2017: ', len(vader_neutral_Oregon_2017))
print('length of vader_negative_Oregon_2017: ', len(vader_negative_Oregon_2017))


print('----------------------------------')
# ----------------------------- Nevada -----------------------------

# Nevada_allECigarette_2017
Nevada_allECigarette_2017 = [481, 518, 516, 546, 487, 436, 417, 336, 92, 128, 245, 253]
print('length of Nevada_allECigarette_2017: ', len(Nevada_allECigarette_2017))

# not_Nevada_allECigarette_2017
not_Nevada_allECigarette_2017 = [17558, 13306, 14249, 13731, 12593, 13185, 13150, 13753, 6841, 9217, 15394, 15428]
print('length of not_Nevada_allECigarette_2017: ', len(not_Nevada_allECigarette_2017))

# allNevada_2017
allNevada_2017 = [681641, 511694, 559172, 508382, 503636, 544346, 580917, 585303, 241846, 363262, 539410, 487596]
print('length of allNevada_2017: ', len(allNevada_2017))


# Number of users that tweets ecig in Nevada.
users_Nevada_ecig_2017 = [123, 117, 130, 134, 111, 135, 160, 139, 68, 93, 185, 177]
print('length of users_Nevada_ecig_2017: ', len(users_Nevada_ecig_2017))


# average number of per person tweets about ecig in Nevada.
average_num_per_person_tweets_Nevada_ecig = []
for i in range(12):
    average_num_per_person_tweets_Nevada_ecig.append(Nevada_allECigarette_2017[i]/users_Nevada_ecig_2017[i])
print('length of average_num_per_person_tweets_Nevada_ecig: ', len(average_num_per_person_tweets_Nevada_ecig))


# Number of users that tweets in Nevada
users_Nevada_2017 = [43055, 35526, 42399, 39318, 38744, 43377, 46753, 44795, 25326, 31593, 38779, 37093]
print('length of users_Nevada_2017: ', len(users_Nevada_2017))

# average number of per person tweets in Nevada.
average_num_per_person_tweets_Nevada = []
for i in range(12):
    average_num_per_person_tweets_Nevada.append(allNevada_2017[i]/users_Nevada_2017[i])
print('length of average_num_per_person_tweets_Nevada: ', len(average_num_per_person_tweets_Nevada))


# Sentiment analysis
vader_positive_Nevada_2017 = [154, 322, 328, 350, 305, 291, 253, 194, 33, 52, 81, 83]
vader_neutral_Nevada_2017 = [288, 157, 146, 163, 152, 106, 117, 109, 38, 53, 112, 111]
vader_negative_Nevada_2017 = [39, 39, 42, 33, 30, 39, 47, 33, 21, 23, 52, 59]
print('length of vader_positive_Nevada_2017: ', len(vader_positive_Nevada_2017))
print('length of vader_neutral_Nevada_2017: ', len(vader_neutral_Nevada_2017))
print('length of vader_negative_Nevada_2017: ', len(vader_negative_Nevada_2017))


print('----------------------------------')
# ----------------------------- Arizona -----------------------------

# Arizona_allECigarette_2017
Arizona_allECigarette_2017 = [422, 293, 336, 411, 302, 230, 292, 325, 162, 253, 409, 382]
print('length of Arizona_allECigarette_2017: ', len(Arizona_allECigarette_2017))

# not_Arizona_allECigarette_2017
not_Arizona_allECigarette_2017 = [17617, 13531, 14429, 13866, 12778, 13391, 13275, 13764, 6771, 9092, 15230, 15299]
print('length of not_Arizona_allECigarette_2017: ', len(not_Arizona_allECigarette_2017))

# allArizona_2017
allArizona_2017 = [1086204, 852986, 864083, 773664, 715142, 726453, 798319, 851711, 376349, 527391, 764080, 704562]
print('length of allArizona_2017: ', len(allArizona_2017))


# Number of users that tweets ecig in Arizona.
users_Arizona_ecig_2017 = [290, 210, 256, 260, 200, 161, 229, 261, 132, 215, 330, 296]
print('length of users_Arizona_ecig_2017: ', len(users_Arizona_ecig_2017))


# average number of per person tweets about ecig in Arizona.
average_num_per_person_tweets_Arizona_ecig = []
for i in range(12):
    average_num_per_person_tweets_Arizona_ecig.append(Arizona_allECigarette_2017[i]/users_Arizona_ecig_2017[i])
print('length of average_num_per_person_tweets_Arizona_ecig: ', len(average_num_per_person_tweets_Arizona_ecig))


# Number of users that tweets in Arizona
users_Arizona_2017 = [50460, 46956, 53007, 47507, 44051, 43259, 45744, 47430, 33200, 39831, 48491, 46966]
print('length of users_Arizona_2017: ', len(users_Arizona_2017))

# average number of per person tweets in Arizona.
average_num_per_person_tweets_Arizona = []
for i in range(12):
    average_num_per_person_tweets_Arizona.append(allArizona_2017[i]/users_Arizona_2017[i])
print('length of average_num_per_person_tweets_Arizona: ', len(average_num_per_person_tweets_Arizona))

# Sentiment analysis
vader_positive_Arizona_2017 = [121, 89, 113, 156, 100, 74, 81, 102, 59, 74, 137, 104]
vader_neutral_Arizona_2017 = [224, 137, 155, 185, 135, 95, 149, 148, 73, 124, 154, 172]
vader_negative_Arizona_2017 = [77, 67, 68, 70, 67, 61, 62, 75, 30, 55, 118, 106]
print('length of vader_positive_Arizona_2017: ', len(vader_positive_Arizona_2017))
print('length of vader_neutral_Arizona_2017: ', len(vader_neutral_Arizona_2017))
print('length of vader_negative_Arizona_2017: ', len(vader_negative_Arizona_2017))



```


# Proportion

```
# Propotion

# ----------------------------- California -----------------------------
propotion_California_ecig_in_all_ecig = []
propotion_California_ecig_in_all_California_tweets = []
propotion_California_in_all_tweets = []
propotion_California_ecig_users_in_all_California_users = []
propotion_positive_ecig_California = []
propotion_neutral_ecig_California = []
propotion_negative_ecig_California = []


# propotion of California e-cig tweets in all e-cig tweets.
for i in range(12):
    propotion_California_ecig_in_all_ecig.append((California_allECigarette_2017[i]/allECigarette_2017[i])*100)
print('length of propotion_California_ecig_in_all_ecig: ', len(propotion_California_ecig_in_all_ecig))


# propotion of California e-cig tweets in all California tweets.
for i in range(12):
    propotion_California_ecig_in_all_California_tweets.append((California_allECigarette_2017[i]/allCalifornia_2017[i])*100)
print('length of propotion_California_ecig_in_all_California_tweets: ', len(propotion_California_ecig_in_all_California_tweets))


# propotion of California tweets in total tweets.
for i in range(12):
    propotion_California_in_all_tweets.append((allCalifornia_2017[i]/allTweets_2017[i])*100)
print('length of propotion_California_in_all_tweets: ', len(propotion_California_in_all_tweets))


# propotion of users post California e-cig in all California users.
for i in range(12):
    propotion_California_ecig_users_in_all_California_users.append((users_California_ecig_2017[i]/users_California_2017[i])*100)
print('length of propotion_California_ecig_users_in_all_California_users: ', len(propotion_California_ecig_users_in_all_California_users))


# Sentiment analysis
for i in range(12):
    propotion_positive_ecig_California.append((vader_positive_California_2017[i]/California_allECigarette_2017[i])*100)
print('length of propotion_positive_ecig_California: ', len(propotion_positive_ecig_California))

for i in range(12):
    propotion_neutral_ecig_California.append((vader_neutral_California_2017[i]/California_allECigarette_2017[i])*100)
print('length of propotion_neutral_ecig_California: ', len(propotion_neutral_ecig_California))

for i in range(12):
    propotion_negative_ecig_California.append((vader_negative_California_2017[i]/California_allECigarette_2017[i])*100)
print('length of propotion_negative_ecig_California: ', len(propotion_negative_ecig_California))


print('----------------------------------')
# ----------------------------- Oregon -----------------------------
propotion_Oregon_ecig_in_all_ecig = []
propotion_Oregon_ecig_in_all_Oregon_tweets = []
propotion_Oregon_in_all_tweets = []
propotion_Oregon_ecig_users_in_all_Oregon_users = []
propotion_positive_ecig_Oregon = []
propotion_neutral_ecig_Oregon = []
propotion_negative_ecig_Oregon = []


# propotion of Oregon e-cig tweets in all e-cig tweets.
for i in range(12):
    propotion_Oregon_ecig_in_all_ecig.append((Oregon_allECigarette_2017[i]/allECigarette_2017[i])*100)
print('length of propotion_Oregon_ecig_in_all_ecig: ', len(propotion_Oregon_ecig_in_all_ecig))


# propotion of Oregon e-cig tweets in all Oregon tweets.
for i in range(12):
    propotion_Oregon_ecig_in_all_Oregon_tweets.append((Oregon_allECigarette_2017[i]/allOregon_2017[i])*100)
print('length of propotion_Oregon_ecig_in_all_Oregon_tweets: ', len(propotion_Oregon_ecig_in_all_Oregon_tweets))


# propotion of Oregon tweets in total tweets.
for i in range(12):
    propotion_Oregon_in_all_tweets.append((allOregon_2017[i]/allTweets_2017[i])*100)
print('length of propotion_Oregon_in_all_tweets: ', len(propotion_Oregon_in_all_tweets))


# propotion of users post Oregon e-cig in all Oregon users.
for i in range(12):
    propotion_Oregon_ecig_users_in_all_Oregon_users.append((users_Oregon_ecig_2017[i]/users_Oregon_2017[i])*100)
print('length of propotion_Oregon_ecig_users_in_all_Oregon_users: ', len(propotion_Oregon_ecig_users_in_all_Oregon_users))


# Sentiment analysis
for i in range(12):
    propotion_positive_ecig_Oregon.append((vader_positive_Oregon_2017[i]/Oregon_allECigarette_2017[i])*100)
print('length of propotion_positive_ecig_Oregon: ', len(propotion_positive_ecig_Oregon))

for i in range(12):
    propotion_neutral_ecig_Oregon.append((vader_neutral_Oregon_2017[i]/Oregon_allECigarette_2017[i])*100)
print('length of propotion_neutral_ecig_Oregon: ', len(propotion_neutral_ecig_Oregon))

for i in range(12):
    propotion_negative_ecig_Oregon.append((vader_negative_Oregon_2017[i]/Oregon_allECigarette_2017[i])*100)
print('length of propotion_negative_ecig_Oregon: ', len(propotion_negative_ecig_Oregon))


print('----------------------------------')
# ----------------------------- Nevada -----------------------------
propotion_Nevada_ecig_in_all_ecig = []
propotion_Nevada_ecig_in_all_Nevada_tweets = []
propotion_Nevada_in_all_tweets = []
propotion_Nevada_ecig_users_in_all_Nevada_users = []
propotion_positive_ecig_Nevada = []
propotion_neutral_ecig_Nevada = []
propotion_negative_ecig_Nevada = []


# propotion of Nevada e-cig tweets in all e-cig tweets.
for i in range(12):
    propotion_Nevada_ecig_in_all_ecig.append((Nevada_allECigarette_2017[i]/allECigarette_2017[i])*100)
print('length of propotion_Nevada_ecig_in_all_ecig: ', len(propotion_Nevada_ecig_in_all_ecig))


# propotion of Nevada e-cig tweets in all Nevada tweets.
for i in range(12):
    propotion_Nevada_ecig_in_all_Nevada_tweets.append((Nevada_allECigarette_2017[i]/allNevada_2017[i])*100)
print('length of propotion_Nevada_ecig_in_all_Nevada_tweets: ', len(propotion_Nevada_ecig_in_all_Nevada_tweets))


# propotion of Nevada tweets in total tweets.
for i in range(12):
    propotion_Nevada_in_all_tweets.append((allNevada_2017[i]/allTweets_2017[i])*100)
print('length of propotion_Nevada_in_all_tweets: ', len(propotion_Nevada_in_all_tweets))


# propotion of users post Nevada e-cig in all Nevada users.
for i in range(12):
    propotion_Nevada_ecig_users_in_all_Nevada_users.append((users_Nevada_ecig_2017[i]/users_Nevada_2017[i])*100)
print('length of propotion_Nevada_ecig_users_in_all_Nevada_users: ', len(propotion_Nevada_ecig_users_in_all_Nevada_users))


# Sentiment analysis
for i in range(12):
    propotion_positive_ecig_Nevada.append((vader_positive_Nevada_2017[i]/Nevada_allECigarette_2017[i])*100)
print('length of propotion_positive_ecig_Nevada: ', len(propotion_positive_ecig_Nevada))

for i in range(12):
    propotion_neutral_ecig_Nevada.append((vader_neutral_Nevada_2017[i]/Nevada_allECigarette_2017[i])*100)
print('length of propotion_neutral_ecig_Nevada: ', len(propotion_neutral_ecig_Nevada))

for i in range(12):
    propotion_negative_ecig_Nevada.append((vader_negative_Nevada_2017[i]/Nevada_allECigarette_2017[i])*100)
print('length of propotion_negative_ecig_Nevada: ', len(propotion_negative_ecig_Nevada))


print('----------------------------------')
# ----------------------------- Arizona -----------------------------
propotion_Arizona_ecig_in_all_ecig = []
propotion_Arizona_ecig_in_all_Arizona_tweets = []
propotion_Arizona_in_all_tweets = []
propotion_Arizona_ecig_users_in_all_Arizona_users = []
propotion_positive_ecig_Arizona = []
propotion_neutral_ecig_Arizona = []
propotion_negative_ecig_Arizona = []


# propotion of Arizona e-cig tweets in all e-cig tweets.
for i in range(12):
    propotion_Arizona_ecig_in_all_ecig.append((Arizona_allECigarette_2017[i]/allECigarette_2017[i])*100)
print('length of propotion_Arizona_ecig_in_all_ecig: ', len(propotion_Arizona_ecig_in_all_ecig))


# propotion of Arizona e-cig tweets in all Arizona tweets.
for i in range(12):
    propotion_Arizona_ecig_in_all_Arizona_tweets.append((Arizona_allECigarette_2017[i]/allArizona_2017[i])*100)
print('length of propotion_Arizona_ecig_in_all_Arizona_tweets: ', len(propotion_Arizona_ecig_in_all_Arizona_tweets))


# propotion of Arizona tweets in total tweets.
for i in range(12):
    propotion_Arizona_in_all_tweets.append((allArizona_2017[i]/allTweets_2017[i])*100)
print('length of propotion_Arizona_in_all_tweets: ', len(propotion_Arizona_in_all_tweets))


# propotion of users post Arizona e-cig in all Arizona users.
for i in range(12):
    propotion_Arizona_ecig_users_in_all_Arizona_users.append((users_Arizona_ecig_2017[i]/users_Arizona_2017[i])*100)
print('length of propotion_Arizona_ecig_users_in_all_Arizona_users: ', len(propotion_Arizona_ecig_users_in_all_Arizona_users))


# Sentiment analysis
for i in range(12):
    propotion_positive_ecig_Arizona.append((vader_positive_Arizona_2017[i]/Arizona_allECigarette_2017[i])*100)
print('length of propotion_positive_ecig_Arizona: ', len(propotion_positive_ecig_Arizona))

for i in range(12):
    propotion_neutral_ecig_Arizona.append((vader_neutral_Arizona_2017[i]/Arizona_allECigarette_2017[i])*100)
print('length of propotion_neutral_ecig_Arizona: ', len(propotion_neutral_ecig_Arizona))

for i in range(12):
    propotion_negative_ecig_Arizona.append((vader_negative_Arizona_2017[i]/Arizona_allECigarette_2017[i])*100)
print('length of propotion_negative_ecig_Arizona: ', len(propotion_negative_ecig_Arizona))



```









