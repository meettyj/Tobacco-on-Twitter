# Number

```
# Number

# ----------------------------- Kansas -----------------------------
# Kansas_allECigarette_2017
Kansas_allECigarette_2017 = [78, 70, 57, 47, 41, 60, 55, 44, 29, 37, 59, 71]
print('length of Kansas_allECigarette_2017: ', len(Kansas_allECigarette_2017))

# not_Kansas_allECigarette_2017
not_Kansas_allECigarette_2017 = [17961, 13754, 14708, 14230, 13039, 13561, 13512, 14045, 6904, 9308, 15580, 15610]
print('length of not_Kansas_allECigarette_2017: ', len(not_Kansas_allECigarette_2017))

# allECigarette_2017
allECigarette_2017 = []
for i in range(12):
    allECigarette_2017.append(Kansas_allECigarette_2017[i]+not_Kansas_allECigarette_2017[i])
print('length of allECigarette_2017: ', len(allECigarette_2017))


# allKansas_2017
allKansas_2017 = [357524, 270774, 271470, 249062, 218047, 219729, 242020, 254155, 118373, 169210, 238239, 217463]
print('length of allKansas_2017: ', len(allKansas_2017))


# Number of users that tweets ecig in Kansas.
users_Kansas_ecig_2017 = [55, 52, 49, 36, 30, 43, 39, 37, 29, 34, 54, 65]
print('length of users_Kansas_ecig_2017: ', len(users_Kansas_ecig_2017))


# average number of per person tweets about ecig in Kansas.
average_num_per_person_tweets_Kansas_ecig = []
for i in range(12):
    average_num_per_person_tweets_Kansas_ecig.append(Kansas_allECigarette_2017[i]/users_Kansas_ecig_2017[i])
print('length of average_num_per_person_tweets_Kansas_ecig: ', len(average_num_per_person_tweets_Kansas_ecig))


# Number of users that tweets in Kansas
users_Kansas_2017 = [19051, 17639, 18512, 17676, 17917, 17325, 18080, 18897, 13543, 15774, 18978, 17866]
print('length of users_Kansas_2017: ', len(users_Kansas_2017))

# allTweets
allTweets_2017 = [64761879, 49292002, 51379810, 46841051, 45592367, 46897952, 50163222, 51079160, 22112648, 31365136, 46232294, 43487766]
print('length of allTweets_2017: ', len(allTweets_2017))

# Sentiment analysis
vader_positive_Kansas_2017 = [30, 27, 17, 14, 19, 22, 25, 16, 10, 16, 25, 20]
vader_neutral_Kansas_2017 = [34, 35, 33, 22, 15, 27, 17, 16, 14, 16, 26, 41]
vader_negative_Kansas_2017 = [14, 8, 7, 11, 7, 11, 13, 12, 5, 5, 8, 10]
print('length of vader_positive_Kansas_2017: ', len(vader_positive_Kansas_2017))
print('length of vader_neutral_Kansas_2017: ', len(vader_neutral_Kansas_2017))
print('length of vader_negative_Kansas_2017: ', len(vader_negative_Kansas_2017))

print('----------------------------------')
# ----------------------------- Nebraska -----------------------------

# Nebraska_allECigarette_2017
Nebraska_allECigarette_2017 = [68, 51, 48, 36, 49, 42, 48, 77, 33, 40, 86, 79]
print('length of Nebraska_allECigarette_2017: ', len(Nebraska_allECigarette_2017))

# not_Nebraska_allECigarette_2017
not_Nebraska_allECigarette_2017 = [17971, 13773, 14717, 14241, 13031, 13579, 13519, 14012, 6900, 9305, 15553, 15602]
print('length of not_Nebraska_allECigarette_2017: ', len(not_Nebraska_allECigarette_2017))

# allNebraska_2017
allNebraska_2017 = [274503, 213059, 212459, 199089, 181708, 187624, 186031, 197235, 93444, 127876, 184320, 172064]
print('length of allNebraska_2017: ', len(allNebraska_2017))


# Number of users that tweets ecig in Nebraska.
users_Nebraska_ecig_2017 = [55, 35, 33, 27, 33, 33, 37, 52, 26, 37, 74, 61]
print('length of users_Nebraska_ecig_2017: ', len(users_Nebraska_ecig_2017))


# average number of per person tweets about ecig in Nebraska.
average_num_per_person_tweets_Nebraska_ecig = []
for i in range(12):
    average_num_per_person_tweets_Nebraska_ecig.append(Nebraska_allECigarette_2017[i]/users_Nebraska_ecig_2017[i])
print('length of average_num_per_person_tweets_Nebraska_ecig: ', len(average_num_per_person_tweets_Nebraska_ecig))


# Number of users that tweets in Nebraska
users_Nebraska_2017 = [14180, 13338, 13522, 13196, 13214, 14152, 13427, 14914, 10603, 11919, 14224, 13251]
print('length of users_Nebraska_2017: ', len(users_Nebraska_2017))

# Sentiment analysis
vader_positive_Nebraska_2017 = [25, 20, 13, 9, 24, 18, 18, 27, 9, 21, 38, 22]
vader_neutral_Nebraska_2017 = [34, 21, 26, 18, 17, 16, 13, 35, 17, 13, 29, 35]
vader_negative_Nebraska_2017 = [9, 10, 9, 9, 8, 8, 17, 15, 7, 6, 19, 22]
print('length of vader_positive_Nebraska_2017: ', len(vader_positive_Nebraska_2017))
print('length of vader_neutral_Nebraska_2017: ', len(vader_neutral_Nebraska_2017))
print('length of vader_negative_Nebraska_2017: ', len(vader_negative_Nebraska_2017))



print('----------------------------------')
# ----------------------------- Missouri -----------------------------

# Missouri_allECigarette_2017
Missouri_allECigarette_2017 = [226, 177, 188, 193, 162, 167, 142, 202, 91, 144, 217, 203]
print('length of Missouri_allECigarette_2017: ', len(Missouri_allECigarette_2017))

# not_Missouri_allECigarette_2017
not_Missouri_allECigarette_2017 = [17813, 13647, 14577, 14084, 12918, 13454, 13425, 13887, 6842, 9201, 15422, 15478]
print('length of not_Missouri_allECigarette_2017: ', len(not_Missouri_allECigarette_2017))

# allMissouri_2017
allMissouri_2017 = [657901, 492511, 532392, 501033, 466911, 453202, 504714, 506856, 221538, 318322, 463272, 459553]
print('length of allMissouri_2017: ', len(allMissouri_2017))


# Number of users that tweets ecig in Missouri.
users_Missouri_ecig_2017 = [121, 95, 89, 105, 99, 99, 90, 96, 56, 85, 113, 118]
print('length of users_Missouri_ecig_2017: ', len(users_Missouri_ecig_2017))


# average number of per person tweets about ecig in Missouri.
average_num_per_person_tweets_Missouri_ecig = []
for i in range(12):
    average_num_per_person_tweets_Missouri_ecig.append(Missouri_allECigarette_2017[i]/users_Missouri_ecig_2017[i])
print('length of average_num_per_person_tweets_Missouri_ecig: ', len(average_num_per_person_tweets_Missouri_ecig))


# Number of users that tweets in Missouri
users_Missouri_2017 = [35469, 32138, 36115, 36105, 35273, 34994, 37272, 37535, 23867, 28494, 35090, 33914]
print('length of users_Missouri_2017: ', len(users_Missouri_2017))

# Sentiment analysis
vader_positive_Missouri_2017 = [81, 55, 55, 52, 46, 56, 40, 52, 36, 40, 58, 61]
vader_neutral_Missouri_2017 = [120, 98, 112, 119, 103, 92, 84, 131, 47, 80, 117, 109]
vader_negative_Missouri_2017 = [25, 24, 21, 22, 13, 19, 18, 19, 8, 24, 42, 33]
print('length of vader_positive_Missouri_2017: ', len(vader_positive_Missouri_2017))
print('length of vader_neutral_Missouri_2017: ', len(vader_neutral_Missouri_2017))
print('length of vader_negative_Missouri_2017: ', len(vader_negative_Missouri_2017))


print('----------------------------------')
# ----------------------------- Oklahoma -----------------------------

# Oklahoma_allECigarette_2017
Oklahoma_allECigarette_2017 = [132, 90, 128, 102, 96, 69, 71, 84, 89, 92, 154, 117]
print('length of Oklahoma_allECigarette_2017: ', len(Oklahoma_allECigarette_2017))

# not_Oklahoma_allECigarette_2017
not_Oklahoma_allECigarette_2017 = [17907, 13734, 14637, 14175, 12984, 13552, 13496, 14005, 6844, 9253, 15485, 15564]
print('length of not_Oklahoma_allECigarette_2017: ', len(not_Oklahoma_allECigarette_2017))

# allOklahoma_2017
allOklahoma_2017 = [548229, 410113, 414572, 397302, 360865, 360432, 379006, 406638, 181723, 257285, 393807, 354681]
print('length of allOklahoma_2017: ', len(allOklahoma_2017))


# Number of users that tweets ecig in Oklahoma.
users_Oklahoma_ecig_2017 = [87, 66, 75, 59, 63, 55, 63, 74, 37, 55, 105, 87]
print('length of users_Oklahoma_ecig_2017: ', len(users_Oklahoma_ecig_2017))


# average number of per person tweets about ecig in Oklahoma.
average_num_per_person_tweets_Oklahoma_ecig = []
for i in range(12):
    average_num_per_person_tweets_Oklahoma_ecig.append(Oklahoma_allECigarette_2017[i]/users_Oklahoma_ecig_2017[i])
print('length of average_num_per_person_tweets_Oklahoma_ecig: ', len(average_num_per_person_tweets_Oklahoma_ecig))


# Number of users that tweets in Oklahoma
users_Oklahoma_2017 = [25186, 23553, 24834, 23512, 23667, 23160, 23958, 25278, 18446, 22040, 26429, 23882]
print('length of users_Oklahoma_2017: ', len(users_Oklahoma_2017))

# Sentiment analysis
vader_positive_Oklahoma_2017 = [55, 33, 59, 39, 36, 30, 31, 36, 9, 23, 54, 45]
vader_neutral_Oklahoma_2017 = [42, 39, 47, 42, 41, 30, 23, 24, 69, 54, 73, 49]
vader_negative_Oklahoma_2017 = [35, 18, 22, 21, 19, 9, 17, 24, 11, 15, 27, 23]
print('length of vader_positive_Oklahoma_2017: ', len(vader_positive_Oklahoma_2017))
print('length of vader_neutral_Oklahoma_2017: ', len(vader_neutral_Oklahoma_2017))
print('length of vader_negative_Oklahoma_2017: ', len(vader_negative_Oklahoma_2017))


print('----------------------------------')
# ----------------------------- Colorado -----------------------------

# Colorado_allECigarette_2017
Colorado_allECigarette_2017 = [194, 175, 201, 185, 141, 158, 193, 190, 75, 150, 221, 206]
print('length of Colorado_allECigarette_2017: ', len(Colorado_allECigarette_2017))

# not_Colorado_allECigarette_2017
not_Colorado_allECigarette_2017 = [17845, 13649, 14564, 14092, 12939, 13463, 13374, 13899, 6858, 9195, 15418, 15475]
print('length of not_Colorado_allECigarette_2017: ', len(not_Colorado_allECigarette_2017))

# allColorado_2017
allColorado_2017 = [653691, 495008, 508845, 457593, 437237, 466033, 506474, 526491, 233532, 326061, 465585, 422692]
print('length of allColorado_2017: ', len(allColorado_2017))


# Number of users that tweets ecig in Colorado.
users_Colorado_ecig_2017 = [130, 118, 130, 138, 101, 108, 135, 127, 61, 101, 136, 141]
print('length of users_Colorado_ecig_2017: ', len(users_Colorado_ecig_2017))


# average number of per person tweets about ecig in Colorado.
average_num_per_person_tweets_Colorado_ecig = []
for i in range(12):
    average_num_per_person_tweets_Colorado_ecig.append(Colorado_allECigarette_2017[i]/users_Colorado_ecig_2017[i])
print('length of average_num_per_person_tweets_Colorado_ecig: ', len(average_num_per_person_tweets_Colorado_ecig))


# Number of users that tweets in Colorado
users_Colorado_2017 = [36737, 31899, 36284, 32098, 32904, 35167, 38950, 37087, 23859, 28341, 33114, 32429]
print('length of users_Colorado_2017: ', len(users_Colorado_2017))

# Sentiment analysis
vader_positive_Colorado_2017 = [96, 53, 64, 69, 53, 61, 58, 75, 25, 42, 82, 64]
vader_neutral_Colorado_2017 = [76, 94, 94, 86, 66, 71, 101, 77, 33, 86, 96, 100]
vader_negative_Colorado_2017 = [22, 28, 43, 30, 22, 26, 34, 38, 17, 22, 43, 42]
print('length of vader_positive_Colorado_2017: ', len(vader_positive_Colorado_2017))
print('length of vader_neutral_Colorado_2017: ', len(vader_neutral_Colorado_2017))
print('length of vader_negative_Colorado_2017: ', len(vader_negative_Colorado_2017))


```


# Proportion

```
# Propotion

# ----------------------------- Kansas -----------------------------
propotion_Kansas_ecig_in_all_ecig = []
propotion_Kansas_ecig_in_all_Kansas_tweets = []
propotion_Kansas_in_all_tweets = []
propotion_Kansas_ecig_users_in_all_Kansas_users = []
propotion_positive_ecig_Kansas = []
propotion_neutral_ecig_Kansas = []
propotion_negative_ecig_Kansas = []


# propotion of Kansas e-cig tweets in all e-cig tweets.
for i in range(12):
    propotion_Kansas_ecig_in_all_ecig.append((Kansas_allECigarette_2017[i]/allECigarette_2017[i])*100)
print('length of propotion_Kansas_ecig_in_all_ecig: ', len(propotion_Kansas_ecig_in_all_ecig))


# propotion of Kansas e-cig tweets in all Kansas tweets.
for i in range(12):
    propotion_Kansas_ecig_in_all_Kansas_tweets.append((Kansas_allECigarette_2017[i]/allKansas_2017[i])*100)
print('length of propotion_Kansas_ecig_in_all_Kansas_tweets: ', len(propotion_Kansas_ecig_in_all_Kansas_tweets))


# propotion of Kansas tweets in total tweets.
for i in range(12):
    propotion_Kansas_in_all_tweets.append((allKansas_2017[i]/allTweets_2017[i])*100)
print('length of propotion_Kansas_in_all_tweets: ', len(propotion_Kansas_in_all_tweets))


# propotion of users post Kansas e-cig in all Kansas users.
for i in range(12):
    propotion_Kansas_ecig_users_in_all_Kansas_users.append((users_Kansas_ecig_2017[i]/users_Kansas_2017[i])*100)
print('length of propotion_Kansas_ecig_users_in_all_Kansas_users: ', len(propotion_Kansas_ecig_users_in_all_Kansas_users))


# Sentiment analysis
for i in range(12):
    propotion_positive_ecig_Kansas.append((vader_positive_Kansas_2017[i]/Kansas_allECigarette_2017[i])*100)
print('length of propotion_positive_ecig_Kansas: ', len(propotion_positive_ecig_Kansas))

for i in range(12):
    propotion_neutral_ecig_Kansas.append((vader_neutral_Kansas_2017[i]/Kansas_allECigarette_2017[i])*100)
print('length of propotion_neutral_ecig_Kansas: ', len(propotion_neutral_ecig_Kansas))

for i in range(12):
    propotion_negative_ecig_Kansas.append((vader_negative_Kansas_2017[i]/Kansas_allECigarette_2017[i])*100)
print('length of propotion_negative_ecig_Kansas: ', len(propotion_negative_ecig_Kansas))


print('----------------------------------')
# ----------------------------- Nebraska -----------------------------
propotion_Nebraska_ecig_in_all_ecig = []
propotion_Nebraska_ecig_in_all_Nebraska_tweets = []
propotion_Nebraska_in_all_tweets = []
propotion_Nebraska_ecig_users_in_all_Nebraska_users = []
propotion_positive_ecig_Nebraska = []
propotion_neutral_ecig_Nebraska = []
propotion_negative_ecig_Nebraska = []


# propotion of Nebraska e-cig tweets in all e-cig tweets.
for i in range(12):
    propotion_Nebraska_ecig_in_all_ecig.append((Nebraska_allECigarette_2017[i]/allECigarette_2017[i])*100)
print('length of propotion_Nebraska_ecig_in_all_ecig: ', len(propotion_Nebraska_ecig_in_all_ecig))


# propotion of Nebraska e-cig tweets in all Nebraska tweets.
for i in range(12):
    propotion_Nebraska_ecig_in_all_Nebraska_tweets.append((Nebraska_allECigarette_2017[i]/allNebraska_2017[i])*100)
print('length of propotion_Nebraska_ecig_in_all_Nebraska_tweets: ', len(propotion_Nebraska_ecig_in_all_Nebraska_tweets))


# propotion of Nebraska tweets in total tweets.
for i in range(12):
    propotion_Nebraska_in_all_tweets.append((allNebraska_2017[i]/allTweets_2017[i])*100)
print('length of propotion_Nebraska_in_all_tweets: ', len(propotion_Nebraska_in_all_tweets))


# propotion of users post Nebraska e-cig in all Nebraska users.
for i in range(12):
    propotion_Nebraska_ecig_users_in_all_Nebraska_users.append((users_Nebraska_ecig_2017[i]/users_Nebraska_2017[i])*100)
print('length of propotion_Nebraska_ecig_users_in_all_Nebraska_users: ', len(propotion_Nebraska_ecig_users_in_all_Nebraska_users))


# Sentiment analysis
for i in range(12):
    propotion_positive_ecig_Nebraska.append((vader_positive_Nebraska_2017[i]/Nebraska_allECigarette_2017[i])*100)
print('length of propotion_positive_ecig_Nebraska: ', len(propotion_positive_ecig_Nebraska))

for i in range(12):
    propotion_neutral_ecig_Nebraska.append((vader_neutral_Nebraska_2017[i]/Nebraska_allECigarette_2017[i])*100)
print('length of propotion_neutral_ecig_Nebraska: ', len(propotion_neutral_ecig_Nebraska))

for i in range(12):
    propotion_negative_ecig_Nebraska.append((vader_negative_Nebraska_2017[i]/Nebraska_allECigarette_2017[i])*100)
print('length of propotion_negative_ecig_Nebraska: ', len(propotion_negative_ecig_Nebraska))


print('----------------------------------')
# ----------------------------- Missouri -----------------------------
propotion_Missouri_ecig_in_all_ecig = []
propotion_Missouri_ecig_in_all_Missouri_tweets = []
propotion_Missouri_in_all_tweets = []
propotion_Missouri_ecig_users_in_all_Missouri_users = []
propotion_positive_ecig_Missouri = []
propotion_neutral_ecig_Missouri = []
propotion_negative_ecig_Missouri = []


# propotion of Missouri e-cig tweets in all e-cig tweets.
for i in range(12):
    propotion_Missouri_ecig_in_all_ecig.append((Missouri_allECigarette_2017[i]/allECigarette_2017[i])*100)
print('length of propotion_Missouri_ecig_in_all_ecig: ', len(propotion_Missouri_ecig_in_all_ecig))


# propotion of Missouri e-cig tweets in all Missouri tweets.
for i in range(12):
    propotion_Missouri_ecig_in_all_Missouri_tweets.append((Missouri_allECigarette_2017[i]/allMissouri_2017[i])*100)
print('length of propotion_Missouri_ecig_in_all_Missouri_tweets: ', len(propotion_Missouri_ecig_in_all_Missouri_tweets))


# propotion of Missouri tweets in total tweets.
for i in range(12):
    propotion_Missouri_in_all_tweets.append((allMissouri_2017[i]/allTweets_2017[i])*100)
print('length of propotion_Missouri_in_all_tweets: ', len(propotion_Missouri_in_all_tweets))


# propotion of users post Missouri e-cig in all Missouri users.
for i in range(12):
    propotion_Missouri_ecig_users_in_all_Missouri_users.append((users_Missouri_ecig_2017[i]/users_Missouri_2017[i])*100)
print('length of propotion_Missouri_ecig_users_in_all_Missouri_users: ', len(propotion_Missouri_ecig_users_in_all_Missouri_users))


# Sentiment analysis
for i in range(12):
    propotion_positive_ecig_Missouri.append((vader_positive_Missouri_2017[i]/Missouri_allECigarette_2017[i])*100)
print('length of propotion_positive_ecig_Missouri: ', len(propotion_positive_ecig_Missouri))

for i in range(12):
    propotion_neutral_ecig_Missouri.append((vader_neutral_Missouri_2017[i]/Missouri_allECigarette_2017[i])*100)
print('length of propotion_neutral_ecig_Missouri: ', len(propotion_neutral_ecig_Missouri))

for i in range(12):
    propotion_negative_ecig_Missouri.append((vader_negative_Missouri_2017[i]/Missouri_allECigarette_2017[i])*100)
print('length of propotion_negative_ecig_Missouri: ', len(propotion_negative_ecig_Missouri))


print('----------------------------------')
# ----------------------------- Oklahoma -----------------------------
propotion_Oklahoma_ecig_in_all_ecig = []
propotion_Oklahoma_ecig_in_all_Oklahoma_tweets = []
propotion_Oklahoma_in_all_tweets = []
propotion_Oklahoma_ecig_users_in_all_Oklahoma_users = []
propotion_positive_ecig_Oklahoma = []
propotion_neutral_ecig_Oklahoma = []
propotion_negative_ecig_Oklahoma = []


# propotion of Oklahoma e-cig tweets in all e-cig tweets.
for i in range(12):
    propotion_Oklahoma_ecig_in_all_ecig.append((Oklahoma_allECigarette_2017[i]/allECigarette_2017[i])*100)
print('length of propotion_Oklahoma_ecig_in_all_ecig: ', len(propotion_Oklahoma_ecig_in_all_ecig))


# propotion of Oklahoma e-cig tweets in all Oklahoma tweets.
for i in range(12):
    propotion_Oklahoma_ecig_in_all_Oklahoma_tweets.append((Oklahoma_allECigarette_2017[i]/allOklahoma_2017[i])*100)
print('length of propotion_Oklahoma_ecig_in_all_Oklahoma_tweets: ', len(propotion_Oklahoma_ecig_in_all_Oklahoma_tweets))


# propotion of Oklahoma tweets in total tweets.
for i in range(12):
    propotion_Oklahoma_in_all_tweets.append((allOklahoma_2017[i]/allTweets_2017[i])*100)
print('length of propotion_Oklahoma_in_all_tweets: ', len(propotion_Oklahoma_in_all_tweets))


# propotion of users post Oklahoma e-cig in all Oklahoma users.
for i in range(12):
    propotion_Oklahoma_ecig_users_in_all_Oklahoma_users.append((users_Oklahoma_ecig_2017[i]/users_Oklahoma_2017[i])*100)
print('length of propotion_Oklahoma_ecig_users_in_all_Oklahoma_users: ', len(propotion_Oklahoma_ecig_users_in_all_Oklahoma_users))


# Sentiment analysis
for i in range(12):
    propotion_positive_ecig_Oklahoma.append((vader_positive_Oklahoma_2017[i]/Oklahoma_allECigarette_2017[i])*100)
print('length of propotion_positive_ecig_Oklahoma: ', len(propotion_positive_ecig_Oklahoma))

for i in range(12):
    propotion_neutral_ecig_Oklahoma.append((vader_neutral_Oklahoma_2017[i]/Oklahoma_allECigarette_2017[i])*100)
print('length of propotion_neutral_ecig_Oklahoma: ', len(propotion_neutral_ecig_Oklahoma))

for i in range(12):
    propotion_negative_ecig_Oklahoma.append((vader_negative_Oklahoma_2017[i]/Oklahoma_allECigarette_2017[i])*100)
print('length of propotion_negative_ecig_Oklahoma: ', len(propotion_negative_ecig_Oklahoma))


print('----------------------------------')
# ----------------------------- Colorado -----------------------------
propotion_Colorado_ecig_in_all_ecig = []
propotion_Colorado_ecig_in_all_Colorado_tweets = []
propotion_Colorado_in_all_tweets = []
propotion_Colorado_ecig_users_in_all_Colorado_users = []
propotion_positive_ecig_Colorado = []
propotion_neutral_ecig_Colorado = []
propotion_negative_ecig_Colorado = []


# propotion of Colorado e-cig tweets in all e-cig tweets.
for i in range(12):
    propotion_Colorado_ecig_in_all_ecig.append((Colorado_allECigarette_2017[i]/allECigarette_2017[i])*100)
print('length of propotion_Colorado_ecig_in_all_ecig: ', len(propotion_Colorado_ecig_in_all_ecig))


# propotion of Colorado e-cig tweets in all Colorado tweets.
for i in range(12):
    propotion_Colorado_ecig_in_all_Colorado_tweets.append((Colorado_allECigarette_2017[i]/allColorado_2017[i])*100)
print('length of propotion_Colorado_ecig_in_all_Colorado_tweets: ', len(propotion_Colorado_ecig_in_all_Colorado_tweets))


# propotion of Colorado tweets in total tweets.
for i in range(12):
    propotion_Colorado_in_all_tweets.append((allColorado_2017[i]/allTweets_2017[i])*100)
print('length of propotion_Colorado_in_all_tweets: ', len(propotion_Colorado_in_all_tweets))


# propotion of users post Colorado e-cig in all Colorado users.
for i in range(12):
    propotion_Colorado_ecig_users_in_all_Colorado_users.append((users_Colorado_ecig_2017[i]/users_Colorado_2017[i])*100)
print('length of propotion_Colorado_ecig_users_in_all_Colorado_users: ', len(propotion_Colorado_ecig_users_in_all_Colorado_users))


# Sentiment analysis
for i in range(12):
    propotion_positive_ecig_Colorado.append((vader_positive_Colorado_2017[i]/Colorado_allECigarette_2017[i])*100)
print('length of propotion_positive_ecig_Colorado: ', len(propotion_positive_ecig_Colorado))

for i in range(12):
    propotion_neutral_ecig_Colorado.append((vader_neutral_Colorado_2017[i]/Colorado_allECigarette_2017[i])*100)
print('length of propotion_neutral_ecig_Colorado: ', len(propotion_neutral_ecig_Colorado))

for i in range(12):
    propotion_negative_ecig_Colorado.append((vader_negative_Colorado_2017[i]/Colorado_allECigarette_2017[i])*100)
print('length of propotion_negative_ecig_Colorado: ', len(propotion_negative_ecig_Colorado))



```









