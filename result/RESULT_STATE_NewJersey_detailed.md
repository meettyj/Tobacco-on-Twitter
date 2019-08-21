# Number

```
# Number

# ----------------------------- NewJersey -----------------------------
# NewJersey_allECigarette
NewJersey_allECigarette = [394, 377, 464, 718, 522, 317, 310, 313, 327, 297, 247, 220]
print('length of NewJersey_allECigarette: ', len(NewJersey_allECigarette))

# not_NewJersey_allECigarette
not_NewJersey_allECigarette = [16854, 15165, 15839, 18152, 16876, 18851, 14797, 18746, 17343, 18399, 16048, 13468]
print('length of not_NewJersey_allECigarette: ', len(not_NewJersey_allECigarette))

# allECigarette
allECigarette = []
for i in range(12):
    allECigarette.append(NewJersey_allECigarette[i]+not_NewJersey_allECigarette[i])
print('length of allECigarette: ', len(allECigarette))


# allNewJersey
allNewJersey = [950771, 901259, 936500, 987062, 831611, 912493, 796119, 883162, 871125, 926252, 795728, 678771]
print('length of allNewJersey: ', len(allNewJersey))


# Number of users that tweets ecig in NewJersey.
users_NewJersey_ecig = [247, 242, 269, 298, 215, 250, 191, 244, 240, 243, 204, 179]
print('length of users_NewJersey_ecig: ', len(users_NewJersey_ecig))


# average number of per person tweets about ecig in NewJersey.
average_num_per_person_tweets_NewJersey_ecig = []
for i in range(12):
    average_num_per_person_tweets_NewJersey_ecig.append(NewJersey_allECigarette[i]/users_NewJersey_ecig[i])
print('length of average_num_per_person_tweets_NewJersey_ecig: ', len(average_num_per_person_tweets_NewJersey_ecig))


# Number of users that tweets in NewJersey
users_NewJersey = [61237, 59945, 66088, 70886, 63909, 61401, 53816, 58553, 58506, 52533, 48259, 47165]
print('length of users_NewJersey: ', len(users_NewJersey))

# allTweets
allTweets = [45660765, 44166238, 44212483, 45858463, 39900707, 45395994, 37985764, 42937313, 41362576, 44209494, 38750216, 32702554]
print('length of allTweets: ', len(allTweets))

# Sentiment analysis
vader_positive_NewJersey = [110, 107, 134, 212, 121, 111, 98, 106, 102, 96, 78, 62]
vader_neutral_NewJersey = [209, 203, 244, 395, 314, 146, 134, 121, 148, 120, 110, 96]
vader_negative_NewJersey = [75, 67, 86, 111, 87, 60, 78, 86, 77, 81, 59, 62]
print('length of vader_positive_NewJersey: ', len(vader_positive_NewJersey))
print('length of vader_neutral_NewJersey: ', len(vader_neutral_NewJersey))
print('length of vader_negative_NewJersey: ', len(vader_negative_NewJersey))

print('----------------------------------')
# ----------------------------- NewYork -----------------------------

# NewYork_allECigarette
NewYork_allECigarette = [1121, 997, 1019, 1133, 1027, 1114, 960, 1061, 1015, 1079, 958, 872]
print('length of NewYork_allECigarette: ', len(NewYork_allECigarette))

# not_NewYork_allECigarette
not_NewYork_allECigarette = [16127, 14545, 15284, 17737, 16371, 18054, 14147, 17998, 16655, 17617, 15337, 12816]
print('length of not_NewYork_allECigarette: ', len(not_NewYork_allECigarette))

# allNewYork
allNewYork = [2704196, 2527171, 2603542, 2664648, 2370655, 2669574, 2294618, 2504632, 2469827, 2660919, 2363006, 2092840]
print('length of allNewYork: ', len(allNewYork))


# Number of users that tweets ecig in NewYork.
users_NewYork_ecig = [807, 734, 745, 816, 762, 822, 715, 808, 757, 768, 666, 580]
print('length of users_NewYork_ecig: ', len(users_NewYork_ecig))


# average number of per person tweets about ecig in NewYork.
average_num_per_person_tweets_NewYork_ecig = []
for i in range(12):
    average_num_per_person_tweets_NewYork_ecig.append(NewYork_allECigarette[i]/users_NewYork_ecig[i])
print('length of average_num_per_person_tweets_NewYork_ecig: ', len(average_num_per_person_tweets_NewYork_ecig))


# Number of users that tweets in NewYork
users_NewYork = [162489, 151919, 162487, 165668, 155984, 165051, 150540, 155580, 155211, 144775, 134813, 134313]
print('length of users_NewYork: ', len(users_NewYork))

# Sentiment analysis
vader_positive_NewYork = [343, 305, 302, 365, 345, 369, 323, 315, 315, 321, 275, 265]
vader_neutral_NewYork = [570, 465, 512, 509, 464, 485, 404, 473, 469, 504, 447, 419]
vader_negative_NewYork = [208, 227, 205, 259, 218, 260, 233, 273, 231, 254, 236, 188]
print('length of vader_positive_NewYork: ', len(vader_positive_NewYork))
print('length of vader_neutral_NewYork: ', len(vader_neutral_NewYork))
print('length of vader_negative_NewYork: ', len(vader_negative_NewYork))



print('----------------------------------')
# ----------------------------- Pennsylvania -----------------------------

# Pennsylvania_allECigarette
Pennsylvania_allECigarette = [448, 345, 362, 383, 349, 711, 433, 570, 437, 506, 495, 411]
print('length of Pennsylvania_allECigarette: ', len(Pennsylvania_allECigarette))

# not_Pennsylvania_allECigarette
not_Pennsylvania_allECigarette = [16800, 15197, 15941, 18487, 17049, 18457, 14674, 18489, 17233, 18190, 15800, 13277]
print('length of not_Pennsylvania_allECigarette: ', len(not_Pennsylvania_allECigarette))

# allPennsylvania
allPennsylvania = [1074942, 963058, 927204, 985919, 868872, 1048747, 847043, 975967, 992347, 1092174, 945646, 783152]
print('length of allPennsylvania: ', len(allPennsylvania))


# Number of users that tweets ecig in Pennsylvania.
users_Pennsylvania_ecig = [352, 282, 269, 276, 263, 362, 276, 334, 320, 321, 272, 199]
print('length of users_Pennsylvania_ecig: ', len(users_Pennsylvania_ecig))


# average number of per person tweets about ecig in Pennsylvania.
average_num_per_person_tweets_Pennsylvania_ecig = []
for i in range(12):
    average_num_per_person_tweets_Pennsylvania_ecig.append(Pennsylvania_allECigarette[i]/users_Pennsylvania_ecig[i])
print('length of average_num_per_person_tweets_Pennsylvania_ecig: ', len(average_num_per_person_tweets_Pennsylvania_ecig))


# Number of users that tweets in Pennsylvania
users_Pennsylvania = [70020, 64301, 65451, 67932, 64035, 68726, 62597, 65962, 64809, 58783, 56594, 54897]
print('length of users_Pennsylvania: ', len(users_Pennsylvania))

# Sentiment analysis
vader_positive_Pennsylvania = [122, 98, 96, 123, 119, 139, 146, 141, 132, 158, 121, 85]
vader_neutral_Pennsylvania = [247, 163, 176, 172, 155, 451, 200, 307, 195, 245, 290, 277]
vader_negative_Pennsylvania = [79, 84, 90, 88, 75, 121, 87, 122, 110, 103, 84, 49]
print('length of vader_positive_Pennsylvania: ', len(vader_positive_Pennsylvania))
print('length of vader_neutral_Pennsylvania: ', len(vader_neutral_Pennsylvania))
print('length of vader_negative_Pennsylvania: ', len(vader_negative_Pennsylvania))


print('----------------------------------')
# ----------------------------- Connecticut -----------------------------

# Connecticut_allECigarette
Connecticut_allECigarette = [106, 119, 99, 119, 100, 122, 124, 154, 116, 143, 156, 82]
print('length of Connecticut_allECigarette: ', len(Connecticut_allECigarette))

# not_Connecticut_allECigarette
not_Connecticut_allECigarette = [17142, 15423, 16204, 18751, 17298, 19046, 14983, 18905, 17554, 18553, 16139, 13606]
print('length of not_Connecticut_allECigarette: ', len(not_Connecticut_allECigarette))

# allConnecticut
allConnecticut = [370847, 348013, 346166, 370594, 304720, 339855, 305354, 335913, 318357, 346063, 290734, 242881]
print('length of allConnecticut: ', len(allConnecticut))


# Number of users that tweets ecig in Connecticut.
users_Connecticut_ecig = [90, 91, 71, 96, 85, 97, 92, 118, 91, 118, 100, 61]
print('length of users_Connecticut_ecig: ', len(users_Connecticut_ecig))


# average number of per person tweets about ecig in Connecticut.
average_num_per_person_tweets_Connecticut_ecig = []
for i in range(12):
    average_num_per_person_tweets_Connecticut_ecig.append(Connecticut_allECigarette[i]/users_Connecticut_ecig[i])
print('length of average_num_per_person_tweets_Connecticut_ecig: ', len(average_num_per_person_tweets_Connecticut_ecig))


# Number of users that tweets in Connecticut
users_Connecticut = [20893, 19874, 20574, 21762, 19990, 20300, 18618, 20145, 19466, 17873, 16795, 16483]
print('length of users_Connecticut: ', len(users_Connecticut))

# Sentiment analysis
vader_positive_Connecticut = [37, 44, 30, 32, 23, 41, 33, 50, 33, 39, 64, 25]
vader_neutral_Connecticut = [51, 54, 41, 61, 48, 52, 60, 57, 53, 61, 55, 45]
vader_negative_Connecticut = [18, 21, 28, 26, 29, 29, 31, 47, 30, 43, 37, 12]
print('length of vader_positive_Connecticut: ', len(vader_positive_Connecticut))
print('length of vader_neutral_Connecticut: ', len(vader_neutral_Connecticut))
print('length of vader_negative_Connecticut: ', len(vader_negative_Connecticut))


print('----------------------------------')
# ----------------------------- Delaware -----------------------------

# Delaware_allECigarette
Delaware_allECigarette = [23, 15, 32, 23, 28, 12, 17, 22, 17, 13, 13, 20]
print('length of Delaware_allECigarette: ', len(Delaware_allECigarette))

# not_Delaware_allECigarette
not_Delaware_allECigarette = [17225, 15527, 16271, 18847, 17370, 19156, 15090, 19037, 17653, 18683, 16282, 13668]
print('length of not_Delaware_allECigarette: ', len(not_Delaware_allECigarette))

# allDelaware
allDelaware = [62067, 56398, 49702, 53516, 49699, 61044, 48584, 53582, 48999, 52770, 44956, 34793]
print('length of allDelaware: ', len(allDelaware))


# Number of users that tweets ecig in Delaware.
users_Delaware_ecig = [14, 13, 14, 14, 22, 12, 16, 10, 15, 13, 10, 15]
print('length of users_Delaware_ecig: ', len(users_Delaware_ecig))


# average number of per person tweets about ecig in Delaware.
average_num_per_person_tweets_Delaware_ecig = []
for i in range(12):
    average_num_per_person_tweets_Delaware_ecig.append(Delaware_allECigarette[i]/users_Delaware_ecig[i])
print('length of average_num_per_person_tweets_Delaware_ecig: ', len(average_num_per_person_tweets_Delaware_ecig))


# Number of users that tweets in Delaware
users_Delaware = [4162, 4430, 4755, 5226, 4789, 4304, 3907, 3890, 3770, 3269, 3231, 3164]
print('length of users_Delaware: ', len(users_Delaware))

# Sentiment analysis
vader_positive_Delaware = [5, 9, 8, 6, 13, 2, 6, 5, 4, 5, 4, 6]
vader_neutral_Delaware = [12, 3, 20, 15, 12, 6, 8, 4, 8, 5, 7, 8]
vader_negative_Delaware = [6, 3, 4, 2, 3, 4, 3, 13, 5, 3, 2, 6]
print('length of vader_positive_Delaware: ', len(vader_positive_Delaware))
print('length of vader_neutral_Delaware: ', len(vader_neutral_Delaware))
print('length of vader_negative_Delaware: ', len(vader_negative_Delaware))


print('----------------------------------')
# ----------------------------- Maryland -----------------------------

# Maryland_allECigarette
Maryland_allECigarette = [243, 206, 241, 256, 222, 230, 184, 266, 236, 245, 280, 206]
print('length of Maryland_allECigarette: ', len(Maryland_allECigarette))

# not_Maryland_allECigarette
not_Maryland_allECigarette = [17005, 15336, 16062, 18614, 17176, 18938, 14923, 18793, 17434, 18451, 16015, 13482]
print('length of not_Maryland_allECigarette: ', len(not_Maryland_allECigarette))

# allMaryland
allMaryland = [817365, 848671, 815445, 825020, 704656, 814361, 675225, 783357, 789550, 824539, 700529, 559635]
print('length of allMaryland: ', len(allMaryland))


# Number of users that tweets ecig in Maryland.
users_Maryland_ecig = [176, 169, 190, 199, 160, 182, 144, 196, 178, 195, 194, 128]
print('length of users_Maryland_ecig: ', len(users_Maryland_ecig))


# average number of per person tweets about ecig in Maryland.
average_num_per_person_tweets_Maryland_ecig = []
for i in range(12):
    average_num_per_person_tweets_Maryland_ecig.append(Maryland_allECigarette[i]/users_Maryland_ecig[i])
print('length of average_num_per_person_tweets_Maryland_ecig: ', len(average_num_per_person_tweets_Maryland_ecig))


# Number of users that tweets in Maryland
users_Maryland = [45044, 44801, 48064, 49120, 44624, 44605, 40522, 44459, 43044, 39977, 37018, 36482]
print('length of users_Maryland: ', len(users_Maryland))

# Sentiment analysis
vader_positive_Maryland = [87, 77, 61, 81, 69, 66, 55, 77, 74, 87, 101, 51]
vader_neutral_Maryland = [103, 85, 119, 113, 92, 119, 86, 113, 99, 100, 113, 118]
vader_negative_Maryland = [53, 44, 61, 62, 61, 45, 43, 76, 63, 58, 66, 37]
print('length of vader_positive_Maryland: ', len(vader_positive_Maryland))
print('length of vader_neutral_Maryland: ', len(vader_neutral_Maryland))
print('length of vader_negative_Maryland: ', len(vader_negative_Maryland))


```



# Proportion

```
# Propotion

# ----------------------------- NewJersey -----------------------------
propotion_NewJersey_ecig_in_all_ecig = []
propotion_NewJersey_ecig_in_all_NewJersey_tweets = []
propotion_NewJersey_in_all_tweets = []
propotion_NewJersey_ecig_users_in_all_NewJersey_users = []
propotion_positive_ecig_NewJersey = []
propotion_neutral_ecig_NewJersey = []
propotion_negative_ecig_NewJersey = []


# propotion of NewJersey e-cig tweets in all e-cig tweets.
for i in range(12):
    propotion_NewJersey_ecig_in_all_ecig.append((NewJersey_allECigarette[i]/allECigarette[i])*100)
print('length of propotion_NewJersey_ecig_in_all_ecig: ', len(propotion_NewJersey_ecig_in_all_ecig))


# propotion of NewJersey e-cig tweets in all NewJersey tweets.
for i in range(12):
    propotion_NewJersey_ecig_in_all_NewJersey_tweets.append((NewJersey_allECigarette[i]/allNewJersey[i])*100)
print('length of propotion_NewJersey_ecig_in_all_NewJersey_tweets: ', len(propotion_NewJersey_ecig_in_all_NewJersey_tweets))


# propotion of NewJersey tweets in total tweets.
for i in range(12):
    propotion_NewJersey_in_all_tweets.append((allNewJersey[i]/allTweets[i])*100)
print('length of propotion_NewJersey_in_all_tweets: ', len(propotion_NewJersey_in_all_tweets))


# propotion of users post NewJersey e-cig in all NewJersey users.
for i in range(12):
    propotion_NewJersey_ecig_users_in_all_NewJersey_users.append((users_NewJersey_ecig[i]/users_NewJersey[i])*100)
print('length of propotion_NewJersey_ecig_users_in_all_NewJersey_users: ', len(propotion_NewJersey_ecig_users_in_all_NewJersey_users))


# Sentiment analysis
for i in range(12):
    propotion_positive_ecig_NewJersey.append((vader_positive_NewJersey[i]/NewJersey_allECigarette[i])*100)
print('length of propotion_positive_ecig_NewJersey: ', len(propotion_positive_ecig_NewJersey))

for i in range(12):
    propotion_neutral_ecig_NewJersey.append((vader_neutral_NewJersey[i]/NewJersey_allECigarette[i])*100)
print('length of propotion_neutral_ecig_NewJersey: ', len(propotion_neutral_ecig_NewJersey))

for i in range(12):
    propotion_negative_ecig_NewJersey.append((vader_negative_NewJersey[i]/NewJersey_allECigarette[i])*100)
print('length of propotion_negative_ecig_NewJersey: ', len(propotion_negative_ecig_NewJersey))


print('----------------------------------')
# ----------------------------- NewYork -----------------------------
propotion_NewYork_ecig_in_all_ecig = []
propotion_NewYork_ecig_in_all_NewYork_tweets = []
propotion_NewYork_in_all_tweets = []
propotion_NewYork_ecig_users_in_all_NewYork_users = []
propotion_positive_ecig_NewYork = []
propotion_neutral_ecig_NewYork = []
propotion_negative_ecig_NewYork = []


# propotion of NewYork e-cig tweets in all e-cig tweets.
for i in range(12):
    propotion_NewYork_ecig_in_all_ecig.append((NewYork_allECigarette[i]/allECigarette[i])*100)
print('length of propotion_NewYork_ecig_in_all_ecig: ', len(propotion_NewYork_ecig_in_all_ecig))


# propotion of NewYork e-cig tweets in all NewYork tweets.
for i in range(12):
    propotion_NewYork_ecig_in_all_NewYork_tweets.append((NewYork_allECigarette[i]/allNewYork[i])*100)
print('length of propotion_NewYork_ecig_in_all_NewYork_tweets: ', len(propotion_NewYork_ecig_in_all_NewYork_tweets))


# propotion of NewYork tweets in total tweets.
for i in range(12):
    propotion_NewYork_in_all_tweets.append((allNewYork[i]/allTweets[i])*100)
print('length of propotion_NewYork_in_all_tweets: ', len(propotion_NewYork_in_all_tweets))


# propotion of users post NewYork e-cig in all NewYork users.
for i in range(12):
    propotion_NewYork_ecig_users_in_all_NewYork_users.append((users_NewYork_ecig[i]/users_NewYork[i])*100)
print('length of propotion_NewYork_ecig_users_in_all_NewYork_users: ', len(propotion_NewYork_ecig_users_in_all_NewYork_users))


# Sentiment analysis
for i in range(12):
    propotion_positive_ecig_NewYork.append((vader_positive_NewYork[i]/NewYork_allECigarette[i])*100)
print('length of propotion_positive_ecig_NewYork: ', len(propotion_positive_ecig_NewYork))

for i in range(12):
    propotion_neutral_ecig_NewYork.append((vader_neutral_NewYork[i]/NewYork_allECigarette[i])*100)
print('length of propotion_neutral_ecig_NewYork: ', len(propotion_neutral_ecig_NewYork))

for i in range(12):
    propotion_negative_ecig_NewYork.append((vader_negative_NewYork[i]/NewYork_allECigarette[i])*100)
print('length of propotion_negative_ecig_NewYork: ', len(propotion_negative_ecig_NewYork))


print('----------------------------------')
# ----------------------------- Pennsylvania -----------------------------
propotion_Pennsylvania_ecig_in_all_ecig = []
propotion_Pennsylvania_ecig_in_all_Pennsylvania_tweets = []
propotion_Pennsylvania_in_all_tweets = []
propotion_Pennsylvania_ecig_users_in_all_Pennsylvania_users = []
propotion_positive_ecig_Pennsylvania = []
propotion_neutral_ecig_Pennsylvania = []
propotion_negative_ecig_Pennsylvania = []


# propotion of Pennsylvania e-cig tweets in all e-cig tweets.
for i in range(12):
    propotion_Pennsylvania_ecig_in_all_ecig.append((Pennsylvania_allECigarette[i]/allECigarette[i])*100)
print('length of propotion_Pennsylvania_ecig_in_all_ecig: ', len(propotion_Pennsylvania_ecig_in_all_ecig))


# propotion of Pennsylvania e-cig tweets in all Pennsylvania tweets.
for i in range(12):
    propotion_Pennsylvania_ecig_in_all_Pennsylvania_tweets.append((Pennsylvania_allECigarette[i]/allPennsylvania[i])*100)
print('length of propotion_Pennsylvania_ecig_in_all_Pennsylvania_tweets: ', len(propotion_Pennsylvania_ecig_in_all_Pennsylvania_tweets))


# propotion of Pennsylvania tweets in total tweets.
for i in range(12):
    propotion_Pennsylvania_in_all_tweets.append((allPennsylvania[i]/allTweets[i])*100)
print('length of propotion_Pennsylvania_in_all_tweets: ', len(propotion_Pennsylvania_in_all_tweets))


# propotion of users post Pennsylvania e-cig in all Pennsylvania users.
for i in range(12):
    propotion_Pennsylvania_ecig_users_in_all_Pennsylvania_users.append((users_Pennsylvania_ecig[i]/users_Pennsylvania[i])*100)
print('length of propotion_Pennsylvania_ecig_users_in_all_Pennsylvania_users: ', len(propotion_Pennsylvania_ecig_users_in_all_Pennsylvania_users))


# Sentiment analysis
for i in range(12):
    propotion_positive_ecig_Pennsylvania.append((vader_positive_Pennsylvania[i]/Pennsylvania_allECigarette[i])*100)
print('length of propotion_positive_ecig_Pennsylvania: ', len(propotion_positive_ecig_Pennsylvania))

for i in range(12):
    propotion_neutral_ecig_Pennsylvania.append((vader_neutral_Pennsylvania[i]/Pennsylvania_allECigarette[i])*100)
print('length of propotion_neutral_ecig_Pennsylvania: ', len(propotion_neutral_ecig_Pennsylvania))

for i in range(12):
    propotion_negative_ecig_Pennsylvania.append((vader_negative_Pennsylvania[i]/Pennsylvania_allECigarette[i])*100)
print('length of propotion_negative_ecig_Pennsylvania: ', len(propotion_negative_ecig_Pennsylvania))


print('----------------------------------')
# ----------------------------- Connecticut -----------------------------
propotion_Connecticut_ecig_in_all_ecig = []
propotion_Connecticut_ecig_in_all_Connecticut_tweets = []
propotion_Connecticut_in_all_tweets = []
propotion_Connecticut_ecig_users_in_all_Connecticut_users = []
propotion_positive_ecig_Connecticut = []
propotion_neutral_ecig_Connecticut = []
propotion_negative_ecig_Connecticut = []


# propotion of Connecticut e-cig tweets in all e-cig tweets.
for i in range(12):
    propotion_Connecticut_ecig_in_all_ecig.append((Connecticut_allECigarette[i]/allECigarette[i])*100)
print('length of propotion_Connecticut_ecig_in_all_ecig: ', len(propotion_Connecticut_ecig_in_all_ecig))


# propotion of Connecticut e-cig tweets in all Connecticut tweets.
for i in range(12):
    propotion_Connecticut_ecig_in_all_Connecticut_tweets.append((Connecticut_allECigarette[i]/allConnecticut[i])*100)
print('length of propotion_Connecticut_ecig_in_all_Connecticut_tweets: ', len(propotion_Connecticut_ecig_in_all_Connecticut_tweets))


# propotion of Connecticut tweets in total tweets.
for i in range(12):
    propotion_Connecticut_in_all_tweets.append((allConnecticut[i]/allTweets[i])*100)
print('length of propotion_Connecticut_in_all_tweets: ', len(propotion_Connecticut_in_all_tweets))


# propotion of users post Connecticut e-cig in all Connecticut users.
for i in range(12):
    propotion_Connecticut_ecig_users_in_all_Connecticut_users.append((users_Connecticut_ecig[i]/users_Connecticut[i])*100)
print('length of propotion_Connecticut_ecig_users_in_all_Connecticut_users: ', len(propotion_Connecticut_ecig_users_in_all_Connecticut_users))


# Sentiment analysis
for i in range(12):
    propotion_positive_ecig_Connecticut.append((vader_positive_Connecticut[i]/Connecticut_allECigarette[i])*100)
print('length of propotion_positive_ecig_Connecticut: ', len(propotion_positive_ecig_Connecticut))

for i in range(12):
    propotion_neutral_ecig_Connecticut.append((vader_neutral_Connecticut[i]/Connecticut_allECigarette[i])*100)
print('length of propotion_neutral_ecig_Connecticut: ', len(propotion_neutral_ecig_Connecticut))

for i in range(12):
    propotion_negative_ecig_Connecticut.append((vader_negative_Connecticut[i]/Connecticut_allECigarette[i])*100)
print('length of propotion_negative_ecig_Connecticut: ', len(propotion_negative_ecig_Connecticut))



print('----------------------------------')
# ----------------------------- Delaware -----------------------------
propotion_Delaware_ecig_in_all_ecig = []
propotion_Delaware_ecig_in_all_Delaware_tweets = []
propotion_Delaware_in_all_tweets = []
propotion_Delaware_ecig_users_in_all_Delaware_users = []
propotion_positive_ecig_Delaware = []
propotion_neutral_ecig_Delaware = []
propotion_negative_ecig_Delaware = []


# propotion of Delaware e-cig tweets in all e-cig tweets.
for i in range(12):
    propotion_Delaware_ecig_in_all_ecig.append((Delaware_allECigarette[i]/allECigarette[i])*100)
print('length of propotion_Delaware_ecig_in_all_ecig: ', len(propotion_Delaware_ecig_in_all_ecig))


# propotion of Delaware e-cig tweets in all Delaware tweets.
for i in range(12):
    propotion_Delaware_ecig_in_all_Delaware_tweets.append((Delaware_allECigarette[i]/allDelaware[i])*100)
print('length of propotion_Delaware_ecig_in_all_Delaware_tweets: ', len(propotion_Delaware_ecig_in_all_Delaware_tweets))


# propotion of Delaware tweets in total tweets.
for i in range(12):
    propotion_Delaware_in_all_tweets.append((allDelaware[i]/allTweets[i])*100)
print('length of propotion_Delaware_in_all_tweets: ', len(propotion_Delaware_in_all_tweets))


# propotion of users post Delaware e-cig in all Delaware users.
for i in range(12):
    propotion_Delaware_ecig_users_in_all_Delaware_users.append((users_Delaware_ecig[i]/users_Delaware[i])*100)
print('length of propotion_Delaware_ecig_users_in_all_Delaware_users: ', len(propotion_Delaware_ecig_users_in_all_Delaware_users))


# Sentiment analysis
for i in range(12):
    propotion_positive_ecig_Delaware.append((vader_positive_Delaware[i]/Delaware_allECigarette[i])*100)
print('length of propotion_positive_ecig_Delaware: ', len(propotion_positive_ecig_Delaware))

for i in range(12):
    propotion_neutral_ecig_Delaware.append((vader_neutral_Delaware[i]/Delaware_allECigarette[i])*100)
print('length of propotion_neutral_ecig_Delaware: ', len(propotion_neutral_ecig_Delaware))

for i in range(12):
    propotion_negative_ecig_Delaware.append((vader_negative_Delaware[i]/Delaware_allECigarette[i])*100)
print('length of propotion_negative_ecig_Delaware: ', len(propotion_negative_ecig_Delaware))



print('----------------------------------')
# ----------------------------- Maryland -----------------------------
propotion_Maryland_ecig_in_all_ecig = []
propotion_Maryland_ecig_in_all_Maryland_tweets = []
propotion_Maryland_in_all_tweets = []
propotion_Maryland_ecig_users_in_all_Maryland_users = []
propotion_positive_ecig_Maryland = []
propotion_neutral_ecig_Maryland = []
propotion_negative_ecig_Maryland = []


# propotion of Maryland e-cig tweets in all e-cig tweets.
for i in range(12):
    propotion_Maryland_ecig_in_all_ecig.append((Maryland_allECigarette[i]/allECigarette[i])*100)
print('length of propotion_Maryland_ecig_in_all_ecig: ', len(propotion_Maryland_ecig_in_all_ecig))


# propotion of Maryland e-cig tweets in all Maryland tweets.
for i in range(12):
    propotion_Maryland_ecig_in_all_Maryland_tweets.append((Maryland_allECigarette[i]/allMaryland[i])*100)
print('length of propotion_Maryland_ecig_in_all_Maryland_tweets: ', len(propotion_Maryland_ecig_in_all_Maryland_tweets))


# propotion of Maryland tweets in total tweets.
for i in range(12):
    propotion_Maryland_in_all_tweets.append((allMaryland[i]/allTweets[i])*100)
print('length of propotion_Maryland_in_all_tweets: ', len(propotion_Maryland_in_all_tweets))


# propotion of users post Maryland e-cig in all Maryland users.
for i in range(12):
    propotion_Maryland_ecig_users_in_all_Maryland_users.append((users_Maryland_ecig[i]/users_Maryland[i])*100)
print('length of propotion_Maryland_ecig_users_in_all_Maryland_users: ', len(propotion_Maryland_ecig_users_in_all_Maryland_users))


# Sentiment analysis
for i in range(12):
    propotion_positive_ecig_Maryland.append((vader_positive_Maryland[i]/Maryland_allECigarette[i])*100)
print('length of propotion_positive_ecig_Maryland: ', len(propotion_positive_ecig_Maryland))

for i in range(12):
    propotion_neutral_ecig_Maryland.append((vader_neutral_Maryland[i]/Maryland_allECigarette[i])*100)
print('length of propotion_neutral_ecig_Maryland: ', len(propotion_neutral_ecig_Maryland))

for i in range(12):
    propotion_negative_ecig_Maryland.append((vader_negative_Maryland[i]/Maryland_allECigarette[i])*100)
print('length of propotion_negative_ecig_Maryland: ', len(propotion_negative_ecig_Maryland))



```









