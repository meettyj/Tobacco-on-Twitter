# Number

```
# Number

# ----------------------------- Kansas -----------------------------
# Kansas_allECigarette_2017
Kansas_allECigarette_2017 = [115, 132, 85, 98, 88, 75, 54, 70, 73, 78, 70, 57, 47, 41, 60, 55, 44, 29, 37, 59, 71, 58, 85, 80, 79, 67, 108, 91, 92, 126, 105, 105, 103, 122, 92, 47, 63]
print('length of Kansas_allECigarette_2017: ', len(Kansas_allECigarette_2017))

# not_Kansas_allECigarette_2017
not_Kansas_allECigarette_2017 = [22671, 24475, 21166, 23581, 20129, 16223, 17552, 16683, 16342, 17961, 13754, 14708, 14230, 13039, 13561, 13512, 14045, 6904, 9308, 15580, 15610,17298, 15324, 17242, 17169, 15475, 16195, 18779, 17306, 19042, 15002, 18954, 17567, 18574, 16203, 13641, 13263]
print('length of not_Kansas_allECigarette_2017: ', len(not_Kansas_allECigarette_2017))

# allECigarette_2017
allECigarette_2017 = []
for i in range(37):
    allECigarette_2017.append(Kansas_allECigarette_2017[i]+not_Kansas_allECigarette_2017[i])
print('length of allECigarette_2017: ', len(allECigarette_2017))


# allKansas_2017
allKansas_2017 = [381317, 395199, 382231, 389340, 400510, 361346, 371409, 369717, 325160, 357524, 270774, 271470, 249062, 218047, 219729, 242020, 254155, 118373, 169210, 238239, 217463,245159, 216073, 251016, 233912, 216562, 204834, 211363, 197013, 231538, 202786, 222545, 196385, 219403, 193762, 151218, 151878]
print('length of allKansas_2017: ', len(allKansas_2017))


# Number of users that tweets ecig in Kansas.
users_Kansas_ecig_2017 = [82, 89, 55, 84, 65, 52, 48, 47, 52,55, 52, 49, 36, 30, 43, 39, 37, 29, 34, 54, 65, 48, 55, 63, 59, 54, 70, 70, 80, 95, 80, 80, 65, 71, 75, 40, 49]
print('length of users_Kansas_ecig_2017: ', len(users_Kansas_ecig_2017))


# average number of per person tweets about ecig in Kansas.
average_num_per_person_tweets_Kansas_ecig = []
for i in range(37):
    average_num_per_person_tweets_Kansas_ecig.append(Kansas_allECigarette_2017[i]/users_Kansas_ecig_2017[i])
print('length of average_num_per_person_tweets_Kansas_ecig: ', len(average_num_per_person_tweets_Kansas_ecig))


# Number of users that tweets in Kansas
users_Kansas_2017 = [20381, 21505, 21378, 22497, 21944, 21090, 21566, 21622, 20192,19051, 17639, 18512, 17676, 17917, 17325, 18080, 18897, 13543, 15774, 18978, 17866,16820, 16432, 18543, 17121, 17191, 16551, 16972, 16760, 17459, 16238, 17106, 16135, 15713, 15046, 13895, 12218]
print('length of users_Kansas_2017: ', len(users_Kansas_2017))

# average number of per person tweets in Kansas.
average_num_per_person_tweets_Kansas = []
for i in range(37):
    average_num_per_person_tweets_Kansas.append(allKansas_2017[i]/users_Kansas_2017[i])
print('length of average_num_per_person_tweets_Kansas: ', len(average_num_per_person_tweets_Kansas))

# allTweets
allTweets_2017 = [70798094, 76153908, 77039352, 79730585, 75060717, 63144176, 68592777, 68306197, 60640789, 64761879, 49292002, 51379810, 46841051, 45592367, 46897952, 50163222, 51079160, 22112648, 31365136, 46232294, 43487766, 46059070, 40432909, 47289301, 45660765, 44166238, 44212483, 45858463, 39900707, 45395994, 37985764, 42937313, 41362576, 44209494, 38750216, 32702554, 33860264]
print('length of allTweets_2017: ', len(allTweets_2017))

# Sentiment analysis
vader_positive_Kansas_2017 = [42, 35, 26, 38, 37, 29, 17, 23, 25,30, 27, 17, 14, 19, 22, 25, 16, 10, 16, 25, 20,18, 24, 27, 24, 23, 30, 29, 29, 33, 38, 29, 26, 42, 25, 15, 20]
vader_neutral_Kansas_2017 = [50, 72, 44, 41, 33, 32, 30, 33, 39,34, 35, 33, 22, 15, 27, 17, 16, 14, 16, 26, 41,20, 45, 40, 33, 30, 47, 37, 41, 61, 34, 40, 52, 56, 44, 25, 29]
vader_negative_Kansas_2017 = [23, 25, 15, 19, 18, 14, 7, 14, 9,14, 8, 7, 11, 7, 11, 13, 12, 5, 5, 8, 10,20, 16, 13, 22, 14, 31, 25, 22, 32, 33, 36, 25, 24, 23, 7, 14]
print('length of vader_positive_Kansas_2017: ', len(vader_positive_Kansas_2017))
print('length of vader_neutral_Kansas_2017: ', len(vader_neutral_Kansas_2017))
print('length of vader_negative_Kansas_2017: ', len(vader_negative_Kansas_2017))

print('----------------------------------')
# ----------------------------- Nebraska -----------------------------

# Nebraska_allECigarette_2017
Nebraska_allECigarette_2017 = [91, 126, 61, 81, 73, 57, 46, 56, 63, 68, 51, 48, 36, 49, 42, 48, 77, 33, 40, 86, 79, 101, 67, 63, 48, 60, 90, 74, 73, 79, 67, 88, 81, 77, 58, 59, 35]
print('length of Nebraska_allECigarette_2017: ', len(Nebraska_allECigarette_2017))


# allNebraska_2017
allNebraska_2017 = [283642, 299681, 285351, 269939, 287109, 262236, 277981, 280936, 250608, 274503, 213059, 212459, 199089, 181708, 187624, 186031, 197235, 93444, 127876, 184320, 172064,185342, 161087, 174894, 167365, 161172, 166606, 155404, 147023, 176945, 147170, 162308, 147688, 159905, 143559, 117803, 108597]
print('length of allNebraska_2017: ', len(allNebraska_2017))


# Number of users that tweets ecig in Nebraska.
users_Nebraska_ecig_2017 = [75, 96, 44, 67, 58, 47, 38, 48, 45,55, 35, 33, 27, 33, 33, 37, 52, 26, 37, 74, 61,83, 57, 55, 42, 56, 63, 58, 59, 65, 58, 74, 64, 62, 53, 47, 27]
print('length of users_Nebraska_ecig_2017: ', len(users_Nebraska_ecig_2017))


# average number of per person tweets about ecig in Nebraska.
average_num_per_person_tweets_Nebraska_ecig = []
for i in range(37):
    average_num_per_person_tweets_Nebraska_ecig.append(Nebraska_allECigarette_2017[i]/users_Nebraska_ecig_2017[i])
print('length of average_num_per_person_tweets_Nebraska_ecig: ', len(average_num_per_person_tweets_Nebraska_ecig))


# Number of users that tweets in Nebraska
users_Nebraska_2017 = [15125, 15749, 17587, 16683, 16380, 15945, 16100, 15871, 14756,14180, 13338, 13522, 13196, 13214, 14152, 13427, 14914, 10603, 11919, 14224, 13251,12556, 12283, 13393, 12822, 12613, 13641, 12440, 12485, 13111, 11968, 12494, 11803, 11334, 11065, 10352, 9063]
print('length of users_Nebraska_2017: ', len(users_Nebraska_2017))

# average number of per person tweets in Nebraska.
average_num_per_person_tweets_Nebraska = []
for i in range(37):
    average_num_per_person_tweets_Nebraska.append(allNebraska_2017[i]/users_Nebraska_2017[i])
print('length of average_num_per_person_tweets_Nebraska: ', len(average_num_per_person_tweets_Nebraska))

# Sentiment analysis
vader_positive_Nebraska_2017 = [28, 37, 24, 31, 30, 28, 13, 20, 19,25, 20, 13, 9, 24, 18, 18, 27, 9, 21, 38, 22,28, 26, 22, 14, 15, 35, 31, 20, 17, 22, 29, 27, 31, 18, 20, 15]
vader_neutral_Nebraska_2017 = [50, 59, 27, 40, 29, 22, 21, 26, 25,34, 21, 26, 18, 17, 16, 13, 35, 17, 13, 29, 35,45, 25, 29, 19, 29, 33, 23, 27, 34, 33, 34, 28, 32, 25, 25, 17]
vader_negative_Nebraska_2017 = [13, 30, 10, 10, 14, 7, 12, 10, 19,9, 10, 9, 9, 8, 8, 17, 15, 7, 6, 19, 22,28, 16, 12, 15, 16, 22, 20, 26, 28, 12, 25, 26, 14, 15, 14, 3]
print('length of vader_positive_Nebraska_2017: ', len(vader_positive_Nebraska_2017))
print('length of vader_neutral_Nebraska_2017: ', len(vader_neutral_Nebraska_2017))
print('length of vader_negative_Nebraska_2017: ', len(vader_negative_Nebraska_2017))



print('----------------------------------')
# ----------------------------- Missouri -----------------------------

# Missouri_allECigarette_2017
Missouri_allECigarette_2017 = [254, 252, 257, 224, 221, 177, 193, 178, 266, 226, 177, 188, 193, 162, 167, 142, 202, 91, 144, 217, 203,263, 171, 203, 247, 160, 182, 213, 190, 196, 148, 191, 145, 140, 136, 124, 112]
print('length of Missouri_allECigarette_2017: ', len(Missouri_allECigarette_2017))


# allMissouri_2017
allMissouri_2017 = [659402, 710516, 670794, 726710, 682607, 588181, 621671, 643718, 615393, 657901, 492511, 532392, 501033, 466911, 453202, 504714, 506856, 221538, 318322, 463272, 459553,474033, 410610, 471223, 428469, 416661, 428335, 445008, 392171, 435906, 367954, 419090, 399001, 439319, 388607, 323493, 323169]
print('length of allMissouri_2017: ', len(allMissouri_2017))


# Number of users that tweets ecig in Missouri.
users_Missouri_ecig_2017 = [180, 179, 140, 156, 158, 105, 130, 101, 101,121, 95, 89, 105, 99, 99, 90, 96, 56, 85, 113, 118,148, 111, 140, 122, 120, 146, 155, 134, 144, 112, 135, 112, 113, 107, 96, 98]
print('length of users_Missouri_ecig_2017: ', len(users_Missouri_ecig_2017))


# average number of per person tweets about ecig in Missouri.
average_num_per_person_tweets_Missouri_ecig = []
for i in range(37):
    average_num_per_person_tweets_Missouri_ecig.append(Missouri_allECigarette_2017[i]/users_Missouri_ecig_2017[i])
print('length of average_num_per_person_tweets_Missouri_ecig: ', len(average_num_per_person_tweets_Missouri_ecig))


# Number of users that tweets in Missouri
users_Missouri_2017 = [40117, 42496, 42958, 47689, 42806, 38915, 40224, 39379, 37723,35469, 32138, 36115, 36105, 35273, 34994, 37272, 37535, 23867, 28494, 35090, 33914,30342, 29684, 34370, 33424, 31754, 33180, 35057, 32777, 32539, 29476, 31688, 30576, 28827, 26837, 26835, 24204]
print('length of users_Missouri_2017: ', len(users_Missouri_2017))

# average number of per person tweets in Missouri.
average_num_per_person_tweets_Missouri = []
for i in range(37):
    average_num_per_person_tweets_Missouri.append(allMissouri_2017[i]/users_Missouri_2017[i])
print('length of average_num_per_person_tweets_Missouri: ', len(average_num_per_person_tweets_Missouri))

# Sentiment analysis
vader_positive_Missouri_2017 = [86, 82, 95, 76, 87, 47, 69, 58, 85,81, 55, 55, 52, 46, 56, 40, 52, 36, 40, 58, 61,84, 49, 67, 69, 50, 68, 76, 66, 73, 41, 61, 49, 47, 50, 39, 42]
vader_neutral_Missouri_2017 = [122, 114, 140, 117, 86, 97, 97, 90, 161,120, 98, 112, 119, 103, 92, 84, 131, 47, 80, 117, 109,128, 94, 95, 130, 75, 83, 103, 79, 81, 71, 84, 52, 52, 57, 54, 49]
vader_negative_Missouri_2017 = [46, 56, 22, 31, 48, 33, 27, 30, 20,25, 24, 21, 22, 13, 19, 18, 19, 8, 24, 42, 33,51, 28, 41, 48, 35, 31, 34, 45, 42, 36, 46, 44, 41, 29, 31, 21]
print('length of vader_positive_Missouri_2017: ', len(vader_positive_Missouri_2017))
print('length of vader_neutral_Missouri_2017: ', len(vader_neutral_Missouri_2017))
print('length of vader_negative_Missouri_2017: ', len(vader_negative_Missouri_2017))


print('----------------------------------')
# ----------------------------- Oklahoma -----------------------------

# Oklahoma_allECigarette_2017
Oklahoma_allECigarette_2017 = [168, 225, 188, 165, 164, 123, 126, 124, 139, 132, 90, 128, 102, 96, 69, 71, 84, 89, 92, 154, 117,153, 126, 127, 136, 108, 129, 150, 190, 178, 129, 158, 168, 169, 169, 111, 108]
print('length of Oklahoma_allECigarette_2017: ', len(Oklahoma_allECigarette_2017))


# allOklahoma_2017
allOklahoma_2017 = [625342, 656059, 618532, 641144, 660085, 597092, 604378, 619002, 521409, 548229, 410113, 414572, 397302, 360865, 360432, 379006, 406638, 181723, 257285, 393807, 354681,373182, 341904, 376281, 382204, 345696, 341769, 351789, 311920, 362146, 310138, 349089, 323238, 349959, 298672, 235028, 245770]
print('length of allOklahoma_2017: ', len(allOklahoma_2017))


# Number of users that tweets ecig in Oklahoma.
users_Oklahoma_ecig_2017 = [117, 148, 121, 134, 112, 98, 104, 95, 91,87, 66, 75, 59, 63, 55, 63, 74, 37, 55, 105, 87,112, 100, 107, 111, 92, 113, 117, 140, 154, 102, 126, 123, 123, 119, 78, 75]
print('length of users_Oklahoma_ecig_2017: ', len(users_Oklahoma_ecig_2017))


# average number of per person tweets about ecig in Oklahoma.
average_num_per_person_tweets_Oklahoma_ecig = []
for i in range(37):
    average_num_per_person_tweets_Oklahoma_ecig.append(Oklahoma_allECigarette_2017[i]/users_Oklahoma_ecig_2017[i])
print('length of average_num_per_person_tweets_Oklahoma_ecig: ', len(average_num_per_person_tweets_Oklahoma_ecig))


# Number of users that tweets in Oklahoma
users_Oklahoma_2017 = [27260, 28575, 28510, 30242, 29795, 29563, 29961, 29286, 26829,25186, 23553, 24834, 23512, 23667, 23160, 23958, 25278, 18446, 22040, 26429, 23882,22326, 21516, 24116, 23651, 22685, 21977, 22244, 21926, 23089, 21751, 22937, 21363, 20242, 19145, 18461, 15915]
print('length of users_Oklahoma_2017: ', len(users_Oklahoma_2017))

# average number of per person tweets in Oklahoma.
average_num_per_person_tweets_Oklahoma = []
for i in range(37):
    average_num_per_person_tweets_Oklahoma.append(allOklahoma_2017[i]/users_Oklahoma_2017[i])
print('length of average_num_per_person_tweets_Oklahoma: ', len(average_num_per_person_tweets_Oklahoma))

# Sentiment analysis
vader_positive_Oklahoma_2017 = [59, 91, 68, 61, 57, 44, 50, 51, 53,55, 33, 59, 39, 36, 30, 31, 36, 9, 23, 54, 45,53, 43, 45, 55, 35, 40, 41, 64, 54, 37, 39, 54, 64, 58, 40, 34]
vader_neutral_Oklahoma_2017 = [82, 100, 88, 69, 76, 51, 43, 53, 52,42, 39, 47, 42, 41, 30, 23, 24, 69, 54, 73, 49,70, 52, 57, 60, 41, 62, 64, 77, 78, 53, 65, 64, 62, 64, 44, 48]
vader_negative_Oklahoma_2017 = [27, 34, 32, 35, 31, 28, 33, 20, 34,35, 18, 22, 21, 19, 9, 17, 24, 11, 15, 27, 23,30, 31, 25, 21, 32, 27, 45, 49, 46, 39, 54, 50, 43, 47, 27, 26]
print('length of vader_positive_Oklahoma_2017: ', len(vader_positive_Oklahoma_2017))
print('length of vader_neutral_Oklahoma_2017: ', len(vader_neutral_Oklahoma_2017))
print('length of vader_negative_Oklahoma_2017: ', len(vader_negative_Oklahoma_2017))


print('----------------------------------')
# ----------------------------- Colorado -----------------------------

# Colorado_allECigarette_2017
Colorado_allECigarette_2017 = [273, 233, 260, 289, 225, 176, 237, 204, 209, 194, 175, 201, 185, 141, 158, 193, 190, 75, 150, 221, 206,234, 223, 267, 291, 181, 186, 244, 259, 254, 190, 232, 211, 222, 201, 203, 227]
print('length of Colorado_allECigarette_2017: ', len(Colorado_allECigarette_2017))


# allColorado_2017
allColorado_2017 = [612293, 636741, 662599, 678806, 649855, 585015, 638956, 640021, 578135, 653691, 495008, 508845, 457593, 437237, 466033, 506474, 526491, 233532, 326061, 465585, 422692,475108, 424930, 494057, 479934, 438637, 450589, 477530, 408113, 463421, 385803, 423631, 404863, 448372, 391850, 334020, 347829]
print('length of allColorado_2017: ', len(allColorado_2017))


# Number of users that tweets ecig in Colorado.
users_Colorado_ecig_2017 = [167, 160, 182, 179, 157, 133, 164, 142, 121,130, 118, 130, 138, 101, 108, 135, 127, 61, 101, 136, 141,155, 150, 171, 182, 140, 143, 167, 185, 196, 144, 179, 172, 174, 146, 128, 131]
print('length of users_Colorado_ecig_2017: ', len(users_Colorado_ecig_2017))


# average number of per person tweets about ecig in Colorado.
average_num_per_person_tweets_Colorado_ecig = []
for i in range(37):
    average_num_per_person_tweets_Colorado_ecig.append(Colorado_allECigarette_2017[i]/users_Colorado_ecig_2017[i])
print('length of average_num_per_person_tweets_Colorado_ecig: ', len(average_num_per_person_tweets_Colorado_ecig))


# Number of users that tweets in Colorado
users_Colorado_2017 = [34410, 35724, 42796, 46508, 41553, 37046, 37714, 36201, 36439,36737, 31899, 36284, 32098, 32904, 35167, 38950, 37087, 23859, 28341, 33114, 32429,31455, 29506, 34003, 30839, 29145, 33046, 35421, 31945, 32067, 29307, 29667, 30288, 30002, 27461, 27233, 25037]
print('length of users_Colorado_2017: ', len(users_Colorado_2017))


# average number of per person tweets in Colorado.
average_num_per_person_tweets_Colorado = []
for i in range(37):
    average_num_per_person_tweets_Colorado.append(allColorado_2017[i]/users_Colorado_2017[i])
print('length of average_num_per_person_tweets_Colorado: ', len(average_num_per_person_tweets_Colorado))

# Sentiment analysis
vader_positive_Colorado_2017 = [81, 77, 98, 112, 87, 57, 90, 73, 57,96, 53, 64, 69, 53, 61, 58, 75, 25, 42, 82, 64,70, 61, 85, 84, 58, 66, 97, 82, 77, 62, 81, 76, 80, 75, 77, 77]
vader_neutral_Colorado_2017 = [153, 115, 125, 129, 102, 91, 110, 98, 108,76, 94, 94, 86, 66, 71, 101, 77, 33, 86, 96, 100,119, 123, 123, 157, 77, 84, 99, 114, 119, 95, 91, 78, 95, 81, 82, 92]
vader_negative_Colorado_2017 = [39, 41, 37, 48, 36, 28, 37, 33, 44,22, 28, 43, 30, 22, 26, 34, 38, 17, 22, 43, 42,45, 39, 59, 50, 46, 36, 48, 63, 58, 33, 60, 57, 47, 45, 44, 58]
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
for i in range(37):
    propotion_Kansas_ecig_in_all_ecig.append((Kansas_allECigarette_2017[i]/allECigarette_2017[i])*100)
print('length of propotion_Kansas_ecig_in_all_ecig: ', len(propotion_Kansas_ecig_in_all_ecig))


# propotion of Kansas e-cig tweets in all Kansas tweets.
for i in range(37):
    propotion_Kansas_ecig_in_all_Kansas_tweets.append((Kansas_allECigarette_2017[i]/allKansas_2017[i])*100)
print('length of propotion_Kansas_ecig_in_all_Kansas_tweets: ', len(propotion_Kansas_ecig_in_all_Kansas_tweets))


# propotion of Kansas tweets in total tweets.
for i in range(37):
    propotion_Kansas_in_all_tweets.append((allKansas_2017[i]/allTweets_2017[i])*100)
print('length of propotion_Kansas_in_all_tweets: ', len(propotion_Kansas_in_all_tweets))


# propotion of users post Kansas e-cig in all Kansas users.
for i in range(37):
    propotion_Kansas_ecig_users_in_all_Kansas_users.append((users_Kansas_ecig_2017[i]/users_Kansas_2017[i])*100)
print('length of propotion_Kansas_ecig_users_in_all_Kansas_users: ', len(propotion_Kansas_ecig_users_in_all_Kansas_users))


# Sentiment analysis
for i in range(37):
    propotion_positive_ecig_Kansas.append((vader_positive_Kansas_2017[i]/Kansas_allECigarette_2017[i])*100)
print('length of propotion_positive_ecig_Kansas: ', len(propotion_positive_ecig_Kansas))

for i in range(37):
    propotion_neutral_ecig_Kansas.append((vader_neutral_Kansas_2017[i]/Kansas_allECigarette_2017[i])*100)
print('length of propotion_neutral_ecig_Kansas: ', len(propotion_neutral_ecig_Kansas))

for i in range(37):
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
for i in range(37):
    propotion_Nebraska_ecig_in_all_ecig.append((Nebraska_allECigarette_2017[i]/allECigarette_2017[i])*100)
print('length of propotion_Nebraska_ecig_in_all_ecig: ', len(propotion_Nebraska_ecig_in_all_ecig))


# propotion of Nebraska e-cig tweets in all Nebraska tweets.
for i in range(37):
    propotion_Nebraska_ecig_in_all_Nebraska_tweets.append((Nebraska_allECigarette_2017[i]/allNebraska_2017[i])*100)
print('length of propotion_Nebraska_ecig_in_all_Nebraska_tweets: ', len(propotion_Nebraska_ecig_in_all_Nebraska_tweets))


# propotion of Nebraska tweets in total tweets.
for i in range(37):
    propotion_Nebraska_in_all_tweets.append((allNebraska_2017[i]/allTweets_2017[i])*100)
print('length of propotion_Nebraska_in_all_tweets: ', len(propotion_Nebraska_in_all_tweets))


# propotion of users post Nebraska e-cig in all Nebraska users.
for i in range(37):
    propotion_Nebraska_ecig_users_in_all_Nebraska_users.append((users_Nebraska_ecig_2017[i]/users_Nebraska_2017[i])*100)
print('length of propotion_Nebraska_ecig_users_in_all_Nebraska_users: ', len(propotion_Nebraska_ecig_users_in_all_Nebraska_users))


# Sentiment analysis
for i in range(37):
    propotion_positive_ecig_Nebraska.append((vader_positive_Nebraska_2017[i]/Nebraska_allECigarette_2017[i])*100)
print('length of propotion_positive_ecig_Nebraska: ', len(propotion_positive_ecig_Nebraska))

for i in range(37):
    propotion_neutral_ecig_Nebraska.append((vader_neutral_Nebraska_2017[i]/Nebraska_allECigarette_2017[i])*100)
print('length of propotion_neutral_ecig_Nebraska: ', len(propotion_neutral_ecig_Nebraska))

for i in range(37):
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
for i in range(37):
    propotion_Missouri_ecig_in_all_ecig.append((Missouri_allECigarette_2017[i]/allECigarette_2017[i])*100)
print('length of propotion_Missouri_ecig_in_all_ecig: ', len(propotion_Missouri_ecig_in_all_ecig))


# propotion of Missouri e-cig tweets in all Missouri tweets.
for i in range(37):
    propotion_Missouri_ecig_in_all_Missouri_tweets.append((Missouri_allECigarette_2017[i]/allMissouri_2017[i])*100)
print('length of propotion_Missouri_ecig_in_all_Missouri_tweets: ', len(propotion_Missouri_ecig_in_all_Missouri_tweets))


# propotion of Missouri tweets in total tweets.
for i in range(37):
    propotion_Missouri_in_all_tweets.append((allMissouri_2017[i]/allTweets_2017[i])*100)
print('length of propotion_Missouri_in_all_tweets: ', len(propotion_Missouri_in_all_tweets))


# propotion of users post Missouri e-cig in all Missouri users.
for i in range(37):
    propotion_Missouri_ecig_users_in_all_Missouri_users.append((users_Missouri_ecig_2017[i]/users_Missouri_2017[i])*100)
print('length of propotion_Missouri_ecig_users_in_all_Missouri_users: ', len(propotion_Missouri_ecig_users_in_all_Missouri_users))


# Sentiment analysis
for i in range(37):
    propotion_positive_ecig_Missouri.append((vader_positive_Missouri_2017[i]/Missouri_allECigarette_2017[i])*100)
print('length of propotion_positive_ecig_Missouri: ', len(propotion_positive_ecig_Missouri))

for i in range(37):
    propotion_neutral_ecig_Missouri.append((vader_neutral_Missouri_2017[i]/Missouri_allECigarette_2017[i])*100)
print('length of propotion_neutral_ecig_Missouri: ', len(propotion_neutral_ecig_Missouri))

for i in range(37):
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
for i in range(37):
    propotion_Oklahoma_ecig_in_all_ecig.append((Oklahoma_allECigarette_2017[i]/allECigarette_2017[i])*100)
print('length of propotion_Oklahoma_ecig_in_all_ecig: ', len(propotion_Oklahoma_ecig_in_all_ecig))


# propotion of Oklahoma e-cig tweets in all Oklahoma tweets.
for i in range(37):
    propotion_Oklahoma_ecig_in_all_Oklahoma_tweets.append((Oklahoma_allECigarette_2017[i]/allOklahoma_2017[i])*100)
print('length of propotion_Oklahoma_ecig_in_all_Oklahoma_tweets: ', len(propotion_Oklahoma_ecig_in_all_Oklahoma_tweets))


# propotion of Oklahoma tweets in total tweets.
for i in range(37):
    propotion_Oklahoma_in_all_tweets.append((allOklahoma_2017[i]/allTweets_2017[i])*100)
print('length of propotion_Oklahoma_in_all_tweets: ', len(propotion_Oklahoma_in_all_tweets))


# propotion of users post Oklahoma e-cig in all Oklahoma users.
for i in range(37):
    propotion_Oklahoma_ecig_users_in_all_Oklahoma_users.append((users_Oklahoma_ecig_2017[i]/users_Oklahoma_2017[i])*100)
print('length of propotion_Oklahoma_ecig_users_in_all_Oklahoma_users: ', len(propotion_Oklahoma_ecig_users_in_all_Oklahoma_users))


# Sentiment analysis
for i in range(37):
    propotion_positive_ecig_Oklahoma.append((vader_positive_Oklahoma_2017[i]/Oklahoma_allECigarette_2017[i])*100)
print('length of propotion_positive_ecig_Oklahoma: ', len(propotion_positive_ecig_Oklahoma))

for i in range(37):
    propotion_neutral_ecig_Oklahoma.append((vader_neutral_Oklahoma_2017[i]/Oklahoma_allECigarette_2017[i])*100)
print('length of propotion_neutral_ecig_Oklahoma: ', len(propotion_neutral_ecig_Oklahoma))

for i in range(37):
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
for i in range(37):
    propotion_Colorado_ecig_in_all_ecig.append((Colorado_allECigarette_2017[i]/allECigarette_2017[i])*100)
print('length of propotion_Colorado_ecig_in_all_ecig: ', len(propotion_Colorado_ecig_in_all_ecig))


# propotion of Colorado e-cig tweets in all Colorado tweets.
for i in range(37):
    propotion_Colorado_ecig_in_all_Colorado_tweets.append((Colorado_allECigarette_2017[i]/allColorado_2017[i])*100)
print('length of propotion_Colorado_ecig_in_all_Colorado_tweets: ', len(propotion_Colorado_ecig_in_all_Colorado_tweets))


# propotion of Colorado tweets in total tweets.
for i in range(37):
    propotion_Colorado_in_all_tweets.append((allColorado_2017[i]/allTweets_2017[i])*100)
print('length of propotion_Colorado_in_all_tweets: ', len(propotion_Colorado_in_all_tweets))


# propotion of users post Colorado e-cig in all Colorado users.
for i in range(37):
    propotion_Colorado_ecig_users_in_all_Colorado_users.append((users_Colorado_ecig_2017[i]/users_Colorado_2017[i])*100)
print('length of propotion_Colorado_ecig_users_in_all_Colorado_users: ', len(propotion_Colorado_ecig_users_in_all_Colorado_users))


# Sentiment analysis
for i in range(37):
    propotion_positive_ecig_Colorado.append((vader_positive_Colorado_2017[i]/Colorado_allECigarette_2017[i])*100)
print('length of propotion_positive_ecig_Colorado: ', len(propotion_positive_ecig_Colorado))

for i in range(37):
    propotion_neutral_ecig_Colorado.append((vader_neutral_Colorado_2017[i]/Colorado_allECigarette_2017[i])*100)
print('length of propotion_neutral_ecig_Colorado: ', len(propotion_neutral_ecig_Colorado))

for i in range(37):
    propotion_negative_ecig_Colorado.append((vader_negative_Colorado_2017[i]/Colorado_allECigarette_2017[i])*100)
print('length of propotion_negative_ecig_Colorado: ', len(propotion_negative_ecig_Colorado))

```
