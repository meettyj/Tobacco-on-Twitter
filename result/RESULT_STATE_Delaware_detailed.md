# Number


```
# Number

# ----------------------------- Delaware -----------------------------
# Delaware_allECigarette
Delaware_allECigarette = [16, 5, 10, 7, 17, 17, 17, 12, 13, 23, 15, 32]
print('length of Delaware_allECigarette: ', len(Delaware_allECigarette))

# not_Delaware_allECigarette
not_Delaware_allECigarette = [13551, 14084, 6923, 9338, 15622, 15664, 17339, 15397, 17309, 17225, 15527, 16271]
print('length of not_Delaware_allECigarette: ', len(not_Delaware_allECigarette))

# allECigarette
allECigarette = []
for i in range(12):
    allECigarette.append(Delaware_allECigarette[i]+not_Delaware_allECigarette[i])
print('length of allECigarette: ', len(allECigarette))


# allDelaware
allDelaware = [53764, 56830, 26115, 39980, 55502, 47932, 56502, 52335, 62645, 62067, 56398, 49702]
print('length of allDelaware: ', len(allDelaware))


# Number of users that tweets ecig in Delaware.
users_Delaware_ecig = [13, 5, 10, 6, 15, 15, 15, 11, 12, 14, 13, 14]
print('length of users_Delaware_ecig: ', len(users_Delaware_ecig))


# average number of per person tweets about ecig in Delaware.
average_num_per_person_tweets_Delaware_ecig = []
for i in range(12):
    average_num_per_person_tweets_Delaware_ecig.append(Delaware_allECigarette[i]/users_Delaware_ecig[i])
print('length of average_num_per_person_tweets_Delaware_ecig: ', len(average_num_per_person_tweets_Delaware_ecig))


# Number of users that tweets in Delaware
users_Delaware = [6128, 6001, 3244, 3621, 4531, 4326, 3694, 3806, 4239, 4162, 4430, 4755]
print('length of users_Delaware: ', len(users_Delaware))

# allTweets
allTweets = [50163222, 51079160, 22112648, 31365136, 46232294, 43487766, 46059070, 40432909, 47289301, 45660765, 44166238, 44212483]
print('length of allTweets: ', len(allTweets))

# Sentiment analysis
vader_positive_Delaware = [6, 2, 0, 2, 4, 3, 5, 1, 5, 5, 9, 8]
vader_neutral_Delaware = [8, 1, 7, 1, 8, 9, 10, 7, 3, 12, 3, 20]
vader_negative_Delaware = [2, 2, 3, 4, 5, 5, 2, 4, 5, 6, 3, 4]
print('length of vader_positive_Delaware: ', len(vader_positive_Delaware))
print('length of vader_neutral_Delaware: ', len(vader_neutral_Delaware))
print('length of vader_negative_Delaware: ', len(vader_negative_Delaware))

print('----------------------------------')
# ----------------------------- NewJersey -----------------------------

# NewJersey_allECigarette
NewJersey_allECigarette = [290, 318, 159, 230, 379, 407, 431, 515, 352, 394, 377, 464]
print('length of NewJersey_allECigarette: ', len(NewJersey_allECigarette))

# not_NewJersey_allECigarette
not_NewJersey_allECigarette = [13277, 13771, 6774, 9115, 15260, 15274, 16925, 14894, 16970, 16854, 15165, 15839]
print('length of not_NewJersey_allECigarette: ', len(not_NewJersey_allECigarette))

# allNewJersey
allNewJersey = [1114713, 1124508, 456279, 662423, 975345, 972957, 1020021, 863451, 994925, 950771, 901259, 936500]
print('length of allNewJersey: ', len(allNewJersey))


# Number of users that tweets ecig in NewJersey.
users_NewJersey_ecig = [200, 235, 118, 144, 252, 235, 291, 270, 253, 247, 242, 269]
print('length of users_NewJersey_ecig: ', len(users_NewJersey_ecig))


# average number of per person tweets about ecig in NewJersey.
average_num_per_person_tweets_NewJersey_ecig = []
for i in range(12):
    average_num_per_person_tweets_NewJersey_ecig.append(NewJersey_allECigarette[i]/users_NewJersey_ecig[i])
print('length of average_num_per_person_tweets_NewJersey_ecig: ', len(average_num_per_person_tweets_NewJersey_ecig))


# Number of users that tweets in NewJersey
users_NewJersey = [79201, 76977, 46205, 54198, 67462, 67514, 59971, 56012, 63296, 61237, 59945, 66088]
print('length of users_NewJersey: ', len(users_NewJersey))

# Sentiment analysis
vader_positive_NewJersey = [93, 108, 44, 58, 98, 141, 138, 124, 102, 110, 107, 134]
vader_neutral_NewJersey = [139, 127, 89, 133, 217, 206, 196, 321, 174, 209, 203, 244]
vader_negative_NewJersey = [58, 83, 26, 39, 64, 60, 97, 70, 76, 75, 67, 86]
print('length of vader_positive_NewJersey: ', len(vader_positive_NewJersey))
print('length of vader_neutral_NewJersey: ', len(vader_neutral_NewJersey))
print('length of vader_negative_NewJersey: ', len(vader_negative_NewJersey))



print('----------------------------------')
# ----------------------------- Pennsylvania -----------------------------

# Pennsylvania_allECigarette
Pennsylvania_allECigarette = [300, 285, 177, 246, 429, 473, 468, 540, 473, 448, 345, 362]
print('length of Pennsylvania_allECigarette: ', len(Pennsylvania_allECigarette))

# not_Pennsylvania_allECigarette
not_Pennsylvania_allECigarette = [13267, 13804, 6756, 9099, 15210, 15208, 16888, 14869, 16849, 16800, 15197, 15941]
print('length of not_Pennsylvania_allECigarette: ', len(not_Pennsylvania_allECigarette))

# allPennsylvania
allPennsylvania = [1066400, 1117120, 503333, 743855, 1088504, 1040445, 1115812, 1014250, 1081833, 1074942, 963058, 927204]
print('length of allPennsylvania: ', len(allPennsylvania))


# Number of users that tweets ecig in Pennsylvania.
users_Pennsylvania_ecig = [190, 193, 121, 175, 300, 300, 323, 337, 310, 352, 282, 269]
print('length of users_Pennsylvania_ecig: ', len(users_Pennsylvania_ecig))


# average number of per person tweets about ecig in Pennsylvania.
average_num_per_person_tweets_Pennsylvania_ecig = []
for i in range(12):
    average_num_per_person_tweets_Pennsylvania_ecig.append(Pennsylvania_allECigarette[i]/users_Pennsylvania_ecig[i])
print('length of average_num_per_person_tweets_Pennsylvania_ecig: ', len(average_num_per_person_tweets_Pennsylvania_ecig))


# Number of users that tweets in Pennsylvania
users_Pennsylvania = [74318, 76297, 52856, 62347, 76226, 72069, 67390, 67943, 70107, 70020, 64301, 65451]
print('length of users_Pennsylvania: ', len(users_Pennsylvania))

# Sentiment analysis
vader_positive_Pennsylvania = [97, 109, 62, 76, 143, 163, 171, 181, 161, 122, 98, 96]
vader_neutral_Pennsylvania = [151, 134, 78, 114, 208, 213, 199, 232, 228, 247, 163, 176]
vader_negative_Pennsylvania = [52, 42, 37, 56, 78, 97, 98, 127, 84, 79, 84, 90]
print('length of vader_positive_Pennsylvania: ', len(vader_positive_Pennsylvania))
print('length of vader_neutral_Pennsylvania: ', len(vader_neutral_Pennsylvania))
print('length of vader_negative_Pennsylvania: ', len(vader_negative_Pennsylvania))


print('----------------------------------')
# ----------------------------- Maryland -----------------------------

# Maryland_allECigarette
Maryland_allECigarette = [151, 147, 72, 99, 202, 196, 243, 191, 229, 243, 206, 241]
print('length of Maryland_allECigarette: ', len(Maryland_allECigarette))

# not_Maryland_allECigarette
not_Maryland_allECigarette = [13416, 13942, 6861, 9246, 15437, 15485, 17113, 15218, 17093, 17005, 15336, 16062]
print('length of not_Maryland_allECigarette: ', len(not_Maryland_allECigarette))

# allMaryland
allMaryland = [913206, 910536, 375999, 543010, 821829, 807107, 820085, 696106, 837322, 817365, 848671, 815445]
print('length of allMaryland: ', len(allMaryland))


# Number of users that tweets ecig in Maryland.
users_Maryland_ecig = [116, 122, 60, 75, 165, 165, 200, 151, 181, 176, 169, 190]
print('length of users_Maryland_ecig: ', len(users_Maryland_ecig))


# average number of per person tweets about ecig in Maryland.
average_num_per_person_tweets_Maryland_ecig = []
for i in range(12):
    average_num_per_person_tweets_Maryland_ecig.append(Maryland_allECigarette[i]/users_Maryland_ecig[i])
print('length of average_num_per_person_tweets_Maryland_ecig: ', len(average_num_per_person_tweets_Maryland_ecig))


# Number of users that tweets in Maryland
users_Maryland = [52472, 52172, 32874, 38400, 48576, 45742, 41852, 40300, 46474, 45044, 44801, 48064]
print('length of users_Maryland: ', len(users_Maryland))

# Sentiment analysis
vader_positive_Maryland = [44, 60, 29, 23, 65, 57, 85, 56, 78, 87, 77, 61]
vader_neutral_Maryland = [70, 59, 24, 51, 88, 92, 111, 83, 110, 103, 85, 119]
vader_negative_Maryland = [37, 28, 19, 25, 49, 47, 47, 52, 41, 53, 44, 61]
print('length of vader_positive_Maryland: ', len(vader_positive_Maryland))
print('length of vader_neutral_Maryland: ', len(vader_neutral_Maryland))
print('length of vader_negative_Maryland: ', len(vader_negative_Maryland))


print('----------------------------------')
# ----------------------------- DC -----------------------------

# DC_allECigarette
DC_allECigarette = [77, 82, 38, 36, 75, 58, 80, 64, 98, 155, 118, 84]
print('length of DC_allECigarette: ', len(DC_allECigarette))

# not_DC_allECigarette
not_DC_allECigarette = [13490, 14007, 6895, 9309, 15564, 15623, 17276, 15345, 17224, 17093, 15424, 16219]
print('length of not_DC_allECigarette: ', len(not_DC_allECigarette))

# allDC
allDC = [416015, 405251, 184175, 279285, 393599, 323480, 377268, 332743, 399649, 386906, 357477, 378537]
print('length of allDC: ', len(allDC))


# Number of users that tweets ecig in DC.
users_DC_ecig = [54, 67, 36, 33, 59, 48, 60, 50, 70, 86, 83, 63]
print('length of users_DC_ecig: ', len(users_DC_ecig))


# average number of per person tweets about ecig in DC.
average_num_per_person_tweets_DC_ecig = []
for i in range(12):
    average_num_per_person_tweets_DC_ecig.append(DC_allECigarette[i]/users_DC_ecig[i])
print('length of average_num_per_person_tweets_DC_ecig: ', len(average_num_per_person_tweets_DC_ecig))


# Number of users that tweets in DC
users_DC = [35488, 32560, 21064, 27727, 33955, 28311, 28878, 27560, 36587, 34803, 30131, 33677]
print('length of users_DC: ', len(users_DC))

# Sentiment analysis
vader_positive_DC = [30, 20, 12, 15, 29, 18, 25, 13, 30, 52, 40, 28]
vader_neutral_DC = [38, 42, 15, 18, 41, 24, 43, 39, 53, 72, 54, 39]
vader_negative_DC = [9, 20, 11, 3, 5, 16, 12, 12, 15, 31, 24, 17]
print('length of vader_positive_DC: ', len(vader_positive_DC))
print('length of vader_neutral_DC: ', len(vader_neutral_DC))
print('length of vader_negative_DC: ', len(vader_negative_DC))

```






# Proportion

```
# Propotion

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


print('----------------------------------')
# ----------------------------- DC -----------------------------
propotion_DC_ecig_in_all_ecig = []
propotion_DC_ecig_in_all_DC_tweets = []
propotion_DC_in_all_tweets = []
propotion_DC_ecig_users_in_all_DC_users = []
propotion_positive_ecig_DC = []
propotion_neutral_ecig_DC = []
propotion_negative_ecig_DC = []


# propotion of DC e-cig tweets in all e-cig tweets.
for i in range(12):
    propotion_DC_ecig_in_all_ecig.append((DC_allECigarette[i]/allECigarette[i])*100)
print('length of propotion_DC_ecig_in_all_ecig: ', len(propotion_DC_ecig_in_all_ecig))


# propotion of DC e-cig tweets in all DC tweets.
for i in range(12):
    propotion_DC_ecig_in_all_DC_tweets.append((DC_allECigarette[i]/allDC[i])*100)
print('length of propotion_DC_ecig_in_all_DC_tweets: ', len(propotion_DC_ecig_in_all_DC_tweets))


# propotion of DC tweets in total tweets.
for i in range(12):
    propotion_DC_in_all_tweets.append((allDC[i]/allTweets[i])*100)
print('length of propotion_DC_in_all_tweets: ', len(propotion_DC_in_all_tweets))


# propotion of users post DC e-cig in all DC users.
for i in range(12):
    propotion_DC_ecig_users_in_all_DC_users.append((users_DC_ecig[i]/users_DC[i])*100)
print('length of propotion_DC_ecig_users_in_all_DC_users: ', len(propotion_DC_ecig_users_in_all_DC_users))


# Sentiment analysis
for i in range(12):
    propotion_positive_ecig_DC.append((vader_positive_DC[i]/DC_allECigarette[i])*100)
print('length of propotion_positive_ecig_DC: ', len(propotion_positive_ecig_DC))

for i in range(12):
    propotion_neutral_ecig_DC.append((vader_neutral_DC[i]/DC_allECigarette[i])*100)
print('length of propotion_neutral_ecig_DC: ', len(propotion_neutral_ecig_DC))

for i in range(12):
    propotion_negative_ecig_DC.append((vader_negative_DC[i]/DC_allECigarette[i])*100)
print('length of propotion_negative_ecig_DC: ', len(propotion_negative_ecig_DC))


```


