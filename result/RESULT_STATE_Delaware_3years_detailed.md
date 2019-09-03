# Number
```
# Number

# ----------------------------- Delaware -----------------------------
# Delaware_allECigarette
Delaware_allECigarette = [9, 29, 23, 28, 9, 15, 13, 15, 6, 7, 6, 13, 5, 5, 9, 16, 5, 10, 7, 17, 17, 17, 12, 13, 23, 15, 32,23, 28, 12, 17, 22, 17, 13, 13, 20, 14]
print('length of Delaware_allECigarette: ', len(Delaware_allECigarette))

# not_Delaware_allECigarette
not_Delaware_allECigarette = [22777, 24578, 21228, 23651, 20208, 16283, 17593, 16738, 16409, 18032, 13818, 14752, 14272, 13075, 13612, 13551, 14084, 6923, 9338, 15622, 15664, 17339, 15397, 17309, 17225, 15527, 16271,18847, 17370, 19156, 15090, 19037, 17653, 18683, 16282, 13668, 13312]
print('length of not_Delaware_allECigarette: ', len(not_Delaware_allECigarette))

# allECigarette
allECigarette = []
for i in range(37):
    allECigarette.append(Delaware_allECigarette[i]+not_Delaware_allECigarette[i])
print('length of allECigarette: ', len(allECigarette))


# allDelaware
allDelaware = [99731, 101037, 95872, 90802, 92265, 87661, 96660, 93238, 77539, 82828, 66600, 66786, 59285, 53608, 52341, 53764, 56830, 26115, 39980, 55502, 47932, 56502, 52335, 62645, 62067, 56398, 49702,53516, 49699, 61044, 48584, 53582, 48999, 52770, 44956, 34793, 38503]
print('length of allDelaware: ', len(allDelaware))


# Number of users that tweets ecig in Delaware.
users_Delaware_ecig = [9, 14, 15, 19, 8, 12, 11, 14, 5, 7, 6, 11, 5, 5, 9, 13, 5, 10, 6, 15, 15, 15, 11, 12, 14, 13, 14,14, 22, 12, 16, 10, 15, 13, 10, 15, 11]
print('length of users_Delaware_ecig: ', len(users_Delaware_ecig))


# average number of per person tweets about ecig in Delaware.
average_num_per_person_tweets_Delaware_ecig = []
for i in range(37):
    average_num_per_person_tweets_Delaware_ecig.append(Delaware_allECigarette[i]/users_Delaware_ecig[i])
print('length of average_num_per_person_tweets_Delaware_ecig: ', len(average_num_per_person_tweets_Delaware_ecig))


# Number of users that tweets in Delaware
users_Delaware = [5547, 6712, 8319, 8558, 8052, 5770, 6015, 5592, 5117,4687, 4309, 4484, 4555, 4827, 5676, 6128, 6001, 3244, 3621, 4531, 4326, 3694, 3806, 4239, 4162, 4430, 4755,5226, 4789, 4304, 3907, 3890, 3770, 3269, 3231, 3164, 2950]
print('length of users_Delaware: ', len(users_Delaware))

# average number of per person tweets in Delaware.
average_num_per_person_tweets_Delaware = []
for i in range(37):
    average_num_per_person_tweets_Delaware.append(allDelaware[i]/users_Delaware[i])
print('length of average_num_per_person_tweets_Delaware: ', len(average_num_per_person_tweets_Delaware))

# allTweets
allTweets = [70798094, 76153908, 77039352, 79730585, 75060717, 63144176, 68592777, 68306197, 60640789, 64761879, 49292002, 51379810, 46841051, 45592367, 46897952, 50163222, 51079160, 22112648, 31365136, 46232294, 43487766, 46059070, 40432909, 47289301, 45660765, 44166238, 44212483, 45858463, 39900707, 45395994, 37985764, 42937313, 41362576, 44209494, 38750216, 32702554, 33860264]
print('length of allTweets: ', len(allTweets))

# Sentiment analysis
vader_positive_Delaware = [3, 12, 5, 13, 3, 4, 6, 5, 0,3, 2, 4, 2, 2, 3, 6, 2, 0, 2, 4, 3, 5, 1, 5, 5, 9, 8, 6, 13, 2, 6, 5, 4, 5, 4, 6, 3]
vader_neutral_Delaware = [3, 12, 14, 11, 5, 7, 3, 6, 5, 2, 4, 7, 3, 2, 5, 8, 1, 7, 1, 8, 9, 10, 7, 3, 12, 3, 20, 15, 12, 6, 8, 4, 8, 5, 7, 8, 7]
vader_negative_Delaware = [3, 5, 4, 4, 1, 4, 4, 4, 1,2, 0, 2, 0, 1, 1, 2, 2, 3, 4, 5, 5, 2, 4, 5, 6, 3, 4,2, 3, 4, 3, 13, 5, 3, 2, 6, 4]
print('length of vader_positive_Delaware: ', len(vader_positive_Delaware))
print('length of vader_neutral_Delaware: ', len(vader_neutral_Delaware))
print('length of vader_negative_Delaware: ', len(vader_negative_Delaware))

print('----------------------------------')
# ----------------------------- NewJersey -----------------------------

# NewJersey_allECigarette
NewJersey_allECigarette = [421, 520, 471, 509, 437, 315, 365, 351, 288, 336, 280, 364, 256, 291, 310, 290, 318, 159, 230, 379, 407, 431, 515, 352, 394, 377, 464,718, 522, 317, 310, 313, 327, 297, 247, 220, 189]
print('length of NewJersey_allECigarette: ', len(NewJersey_allECigarette))


# allNewJersey
allNewJersey = [1640985, 1831517, 1849522, 1965775, 1815107, 1437392, 1527071, 1535928, 1363440, 1444572, 1076167, 1140128, 1005554, 999074, 1048626, 1114713, 1124508, 456279, 662423, 975345, 972957, 1020021, 863451, 994925, 950771, 901259, 936500,987062, 831611, 912493, 796119, 883162, 871125, 926252, 795728, 678771, 687775]
print('length of allNewJersey: ', len(allNewJersey))


# Number of users that tweets ecig in NewJersey.
users_NewJersey_ecig = [289, 361, 339, 342, 273, 208, 226, 211, 196,203, 173, 221, 176, 176, 206, 200, 235, 118, 144, 252, 235, 291, 270, 253, 247, 242, 269,298, 215, 250, 191, 244, 240, 243, 204, 179, 146]
print('length of users_NewJersey_ecig: ', len(users_NewJersey_ecig))


# average number of per person tweets about ecig in NewJersey.
average_num_per_person_tweets_NewJersey_ecig = []
for i in range(37):
    average_num_per_person_tweets_NewJersey_ecig.append(NewJersey_allECigarette[i]/users_NewJersey_ecig[i])
print('length of average_num_per_person_tweets_NewJersey_ecig: ', len(average_num_per_person_tweets_NewJersey_ecig))


# Number of users that tweets in NewJersey
users_NewJersey = [77022, 85994, 96261, 105613, 95283, 76686, 78880, 79642, 74867,70472, 62031, 65919, 65308, 69170, 74451, 79201, 76977, 46205, 54198, 67462, 67514, 59971, 56012, 63296, 61237, 59945, 66088,70886, 63909, 61401, 53816, 58553, 58506, 52533, 48259, 47165, 44841]
print('length of users_NewJersey: ', len(users_NewJersey))

# average number of per person tweets in NewJersey.
average_num_per_person_tweets_NewJersey = []
for i in range(37):
    average_num_per_person_tweets_NewJersey.append(allNewJersey[i]/users_NewJersey[i])
print('length of average_num_per_person_tweets_NewJersey: ', len(average_num_per_person_tweets_NewJersey))

# Sentiment analysis
vader_positive_NewJersey = [136, 181, 147, 152, 137, 94, 114, 121, 97,121, 102, 115, 109, 85, 111, 93, 108, 44, 58, 98, 141, 138, 124, 102, 110, 107, 134,212, 121, 111, 98, 106, 102, 96, 78, 62, 70]
vader_neutral_NewJersey = [206, 243, 229, 260, 206, 157, 185, 178, 149,144, 128, 172, 108, 144, 137, 139, 127, 89, 133, 217, 206, 196, 321, 174, 209, 203, 244,395, 314, 146, 134, 121, 148, 120, 110, 96, 86]
vader_negative_NewJersey = [79, 96, 95, 97, 94, 64, 66, 52, 42,71, 50, 77, 39, 62, 62, 58, 83, 26, 39, 64, 60, 97, 70, 76, 75, 67, 86,111, 87, 60, 78, 86, 77, 81, 59, 62, 33]
print('length of vader_positive_NewJersey: ', len(vader_positive_NewJersey))
print('length of vader_neutral_NewJersey: ', len(vader_neutral_NewJersey))
print('length of vader_negative_NewJersey: ', len(vader_negative_NewJersey))



print('----------------------------------')
# ----------------------------- Pennsylvania -----------------------------

# Pennsylvania_allECigarette
Pennsylvania_allECigarette = [608, 551, 448, 566, 461, 468, 404, 344, 306,301, 240, 255, 256, 221, 217, 300, 285, 177, 246, 429, 473, 468, 540, 473, 448, 345, 362,383, 349, 711, 433, 570, 437, 506, 495, 411, 667]
print('length of Pennsylvania_allECigarette: ', len(Pennsylvania_allECigarette))


# allPennsylvania
allPennsylvania = [1789157, 1814176, 1743177, 1823654, 1723617, 1577605, 1690383, 1657002, 1446995, 1536200, 1184100, 1177434, 1101369, 1042755, 1031138, 1066400, 1117120, 503333, 743855, 1088504, 1040445, 1115812, 1014250, 1081833, 1074942, 963058, 927204,985919, 868872, 1048747, 847043, 975967, 992347, 1092174, 945646, 783152, 811483]
print('length of allPennsylvania: ', len(allPennsylvania))


# Number of users that tweets ecig in Pennsylvania.
users_Pennsylvania_ecig = [403, 373, 307, 391, 333, 313, 293, 259, 232,225, 174, 210, 208, 178, 165, 190, 193, 121, 175, 300, 300, 323, 337, 310, 352, 282, 269,276, 263, 362, 276, 334, 320, 321, 272, 199, 229]
print('length of users_Pennsylvania_ecig: ', len(users_Pennsylvania_ecig))


# average number of per person tweets about ecig in Pennsylvania.
average_num_per_person_tweets_Pennsylvania_ecig = []
for i in range(37):
    average_num_per_person_tweets_Pennsylvania_ecig.append(Pennsylvania_allECigarette[i]/users_Pennsylvania_ecig[i])
print('length of average_num_per_person_tweets_Pennsylvania_ecig: ', len(average_num_per_person_tweets_Pennsylvania_ecig))


# Number of users that tweets in Pennsylvania
users_Pennsylvania = [88676, 90074, 94320, 99925, 94028, 88266, 91999, 90135, 82334,78742, 72819, 75114, 75989, 73545, 72275, 74318, 76297, 52856, 62347, 76226, 72069, 67390, 67943, 70107, 70020, 64301, 65451,67932, 64035, 68726, 62597, 65962, 64809, 58783, 56594, 54897, 50568]
print('length of users_Pennsylvania: ', len(users_Pennsylvania))

# average number of per person tweets in Pennsylvania.
average_num_per_person_tweets_Pennsylvania = []
for i in range(37):
    average_num_per_person_tweets_Pennsylvania.append(allPennsylvania[i]/users_Pennsylvania[i])
print('length of average_num_per_person_tweets_Pennsylvania: ', len(average_num_per_person_tweets_Pennsylvania))

# Sentiment analysis
vader_positive_Pennsylvania = [182, 167, 158, 195, 156, 177, 137, 129, 106,87, 84, 78, 85, 67, 86, 97, 109, 62, 76, 143, 163, 171, 181, 161, 122, 98, 96,123, 119, 139, 146, 141, 132, 158, 121, 85, 91]
vader_neutral_Pennsylvania = [325, 293, 215, 294, 214, 221, 194, 151, 148,153, 113, 123, 121, 121, 95, 151, 134, 78, 114, 208, 213, 199, 232, 228, 247, 163, 176,172, 155, 451, 200, 307, 195, 245, 290, 277, 522]
vader_negative_Pennsylvania = [101, 91, 75, 77, 91, 70, 73, 64, 52,61, 43, 54, 50, 33, 36, 52, 42, 37, 56, 78, 97, 98, 127, 84, 79, 84, 90,88, 75, 121, 87, 122, 110, 103, 84, 49, 54]
print('length of vader_positive_Pennsylvania: ', len(vader_positive_Pennsylvania))
print('length of vader_neutral_Pennsylvania: ', len(vader_neutral_Pennsylvania))
print('length of vader_negative_Pennsylvania: ', len(vader_negative_Pennsylvania))


print('----------------------------------')
# ----------------------------- Maryland -----------------------------

# Maryland_allECigarette
Maryland_allECigarette = [381, 330, 266, 360, 340, 267, 251, 269, 239,310, 177, 160, 165, 127, 148, 151, 147, 72, 99, 202, 196, 243, 191, 229, 243, 206, 241,256, 222, 230, 184, 266, 236, 245, 280, 206, 196]
print('length of Maryland_allECigarette: ', len(Maryland_allECigarette))


# allMaryland
allMaryland = [1336293, 1527105, 1455242, 1466647, 1372734, 1100402, 1200834, 1270371, 1165689, 1201569, 888383, 929124, 832248, 838373, 860648, 913206, 910536, 375999, 543010, 821829, 807107, 820085, 696106, 837322, 817365, 848671, 815445,825020, 704656, 814361, 675225, 783357, 789550, 824539, 700529, 559635, 585748]
print('length of allMaryland: ', len(allMaryland))


# Number of users that tweets ecig in Maryland.
users_Maryland_ecig = [180, 201, 152, 231, 179, 135, 133, 151, 121,140, 111, 119, 123, 96, 116, 116, 122, 60, 75, 165, 165, 200, 151, 181, 176, 169, 190,199, 160, 182, 144, 196, 178, 195, 194, 128, 130]
print('length of users_Maryland_ecig: ', len(users_Maryland_ecig))


# average number of per person tweets about ecig in Maryland.
average_num_per_person_tweets_Maryland_ecig = []
for i in range(37):
    average_num_per_person_tweets_Maryland_ecig.append(Maryland_allECigarette[i]/users_Maryland_ecig[i])
print('length of average_num_per_person_tweets_Maryland_ecig: ', len(average_num_per_person_tweets_Maryland_ecig))


# Number of users that tweets in Maryland
users_Maryland = [52890, 56856, 61771, 64392, 61229, 51890, 53662, 54115, 51635,50816, 43913, 46441, 46621, 47776, 50047, 52472, 52172, 32874, 38400, 48576, 45742, 41852, 40300, 46474, 45044, 44801, 48064,49120, 44624, 44605, 40522, 44459, 43044, 39977, 37018, 36482, 34020]
print('length of users_Maryland: ', len(users_Maryland))

# average number of per person tweets in Maryland.
average_num_per_person_tweets_Maryland = []
for i in range(37):
    average_num_per_person_tweets_Maryland.append(allMaryland[i]/users_Maryland[i])
print('length of average_num_per_person_tweets_Maryland: ', len(average_num_per_person_tweets_Maryland))

# Sentiment analysis
vader_positive_Maryland = [118, 106, 86, 121, 133, 95, 102, 98, 97,125, 72, 61, 58, 42, 50, 44, 60, 29, 23, 65, 57, 85, 56, 78, 87, 77, 61,81, 69, 66, 55, 77, 74, 87, 101, 51, 58]
vader_neutral_Maryland = [197, 163, 137, 185, 145, 124, 112, 116, 108,139, 71, 76, 75, 64, 72, 70, 59, 24, 51, 88, 92, 111, 83, 110, 103, 85, 119,113, 92, 119, 86, 113, 99, 100, 113, 118, 88]
vader_negative_Maryland = [66, 61, 43, 54, 62, 48, 37, 55, 34, 46, 34, 23, 32, 21, 26, 37, 28, 19, 25, 49, 47, 47, 52, 41, 53, 44, 61, 62, 61, 45, 43, 76, 63, 58, 66, 37, 50]
print('length of vader_positive_Maryland: ', len(vader_positive_Maryland))
print('length of vader_neutral_Maryland: ', len(vader_neutral_Maryland))
print('length of vader_negative_Maryland: ', len(vader_negative_Maryland))


print('----------------------------------')
# ----------------------------- DC -----------------------------

# DC_allECigarette
DC_allECigarette = [85, 101, 120, 87, 60, 62, 101, 80, 107, 88, 73, 98, 86, 149, 60, 77, 82, 38, 36, 75, 58, 80, 64, 98, 155, 118, 84,108, 117, 109, 106, 114, 127, 97, 93, 94, 110]
print('length of DC_allECigarette: ', len(DC_allECigarette))


# allDC
allDC = [495712, 489237, 528290, 526050, 478299, 452592, 507273, 505881, 416684, 561879, 418441, 446522, 425394, 403578, 415853, 416015, 405251, 184175, 279285, 393599, 323480, 377268, 332743, 399649, 386906, 357477, 378537,382960, 327654, 381864, 326346, 361666, 339518, 397796, 353538, 308972, 340837]
print('length of allDC: ', len(allDC))


# Number of users that tweets ecig in DC.
users_DC_ecig = [68, 76, 76, 74, 55, 42, 66, 58, 55, 56, 51, 63, 66, 64, 55, 54, 67, 36, 33, 59, 48, 60, 50, 70, 86, 83, 63, 71, 67, 74, 59, 75, 62, 53, 70, 59, 64]
print('length of users_DC_ecig: ', len(users_DC_ecig))


# average number of per person tweets about ecig in DC.
average_num_per_person_tweets_DC_ecig = []
for i in range(37):
    average_num_per_person_tweets_DC_ecig.append(DC_allECigarette[i]/users_DC_ecig[i])
print('length of average_num_per_person_tweets_DC_ecig: ', len(average_num_per_person_tweets_DC_ecig))


# Number of users that tweets in DC
users_DC = [37449, 35711, 39215, 39180, 34580, 34581, 37051, 36896, 31891,47629, 32477, 37703, 37248, 34376, 35986, 35488, 32560, 21064, 27727, 33955, 28311, 28878, 27560, 36587, 34803, 30131, 33677,33165, 28191, 30745, 29287, 29969, 27471, 27855, 26338, 27991, 27209]
print('length of users_DC: ', len(users_DC))

# average number of per person tweets in DC.
average_num_per_person_tweets_DC = []
for i in range(37):
    average_num_per_person_tweets_DC.append(allDC[i]/users_DC[i])
print('length of average_num_per_person_tweets_DC: ', len(average_num_per_person_tweets_DC))

# Sentiment analysis
vader_positive_DC = [30, 39, 39, 30, 16, 23, 28, 13, 24, 33, 29, 30, 32, 51, 27, 30, 20, 12, 15, 29, 18, 25, 13, 30, 52, 40, 28, 42, 57, 45, 42, 43, 35, 39, 35, 35, 36]
vader_neutral_DC = [40, 44, 59, 37, 34, 26, 56, 49, 54, 36, 29, 52, 38, 60, 28, 38, 42, 15, 18, 41, 24, 43, 39, 53, 72, 54, 39, 41, 42, 47, 32, 42, 69, 39, 38, 37, 40]
vader_negative_DC = [15, 18, 22, 20, 10, 13, 17, 18, 29, 19, 15, 16, 16, 38, 5, 9, 20, 11, 3, 5, 16, 12, 12, 15, 31, 24, 17, 25, 18, 17, 32, 29, 23, 19, 20, 22, 34]
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
for i in range(37):
    propotion_Delaware_ecig_in_all_ecig.append((Delaware_allECigarette[i]/allECigarette[i])*100)
print('length of propotion_Delaware_ecig_in_all_ecig: ', len(propotion_Delaware_ecig_in_all_ecig))


# propotion of Delaware e-cig tweets in all Delaware tweets.
for i in range(37):
    propotion_Delaware_ecig_in_all_Delaware_tweets.append((Delaware_allECigarette[i]/allDelaware[i])*100)
print('length of propotion_Delaware_ecig_in_all_Delaware_tweets: ', len(propotion_Delaware_ecig_in_all_Delaware_tweets))


# propotion of Delaware tweets in total tweets.
for i in range(37):
    propotion_Delaware_in_all_tweets.append((allDelaware[i]/allTweets[i])*100)
print('length of propotion_Delaware_in_all_tweets: ', len(propotion_Delaware_in_all_tweets))


# propotion of users post Delaware e-cig in all Delaware users.
for i in range(37):
    propotion_Delaware_ecig_users_in_all_Delaware_users.append((users_Delaware_ecig[i]/users_Delaware[i])*100)
print('length of propotion_Delaware_ecig_users_in_all_Delaware_users: ', len(propotion_Delaware_ecig_users_in_all_Delaware_users))


# Sentiment analysis
for i in range(37):
    propotion_positive_ecig_Delaware.append((vader_positive_Delaware[i]/Delaware_allECigarette[i])*100)
print('length of propotion_positive_ecig_Delaware: ', len(propotion_positive_ecig_Delaware))

for i in range(37):
    propotion_neutral_ecig_Delaware.append((vader_neutral_Delaware[i]/Delaware_allECigarette[i])*100)
print('length of propotion_neutral_ecig_Delaware: ', len(propotion_neutral_ecig_Delaware))

for i in range(37):
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
for i in range(37):
    propotion_NewJersey_ecig_in_all_ecig.append((NewJersey_allECigarette[i]/allECigarette[i])*100)
print('length of propotion_NewJersey_ecig_in_all_ecig: ', len(propotion_NewJersey_ecig_in_all_ecig))


# propotion of NewJersey e-cig tweets in all NewJersey tweets.
for i in range(37):
    propotion_NewJersey_ecig_in_all_NewJersey_tweets.append((NewJersey_allECigarette[i]/allNewJersey[i])*100)
print('length of propotion_NewJersey_ecig_in_all_NewJersey_tweets: ', len(propotion_NewJersey_ecig_in_all_NewJersey_tweets))


# propotion of NewJersey tweets in total tweets.
for i in range(37):
    propotion_NewJersey_in_all_tweets.append((allNewJersey[i]/allTweets[i])*100)
print('length of propotion_NewJersey_in_all_tweets: ', len(propotion_NewJersey_in_all_tweets))


# propotion of users post NewJersey e-cig in all NewJersey users.
for i in range(37):
    propotion_NewJersey_ecig_users_in_all_NewJersey_users.append((users_NewJersey_ecig[i]/users_NewJersey[i])*100)
print('length of propotion_NewJersey_ecig_users_in_all_NewJersey_users: ', len(propotion_NewJersey_ecig_users_in_all_NewJersey_users))


# Sentiment analysis
for i in range(37):
    propotion_positive_ecig_NewJersey.append((vader_positive_NewJersey[i]/NewJersey_allECigarette[i])*100)
print('length of propotion_positive_ecig_NewJersey: ', len(propotion_positive_ecig_NewJersey))

for i in range(37):
    propotion_neutral_ecig_NewJersey.append((vader_neutral_NewJersey[i]/NewJersey_allECigarette[i])*100)
print('length of propotion_neutral_ecig_NewJersey: ', len(propotion_neutral_ecig_NewJersey))

for i in range(37):
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
for i in range(37):
    propotion_Pennsylvania_ecig_in_all_ecig.append((Pennsylvania_allECigarette[i]/allECigarette[i])*100)
print('length of propotion_Pennsylvania_ecig_in_all_ecig: ', len(propotion_Pennsylvania_ecig_in_all_ecig))


# propotion of Pennsylvania e-cig tweets in all Pennsylvania tweets.
for i in range(37):
    propotion_Pennsylvania_ecig_in_all_Pennsylvania_tweets.append((Pennsylvania_allECigarette[i]/allPennsylvania[i])*100)
print('length of propotion_Pennsylvania_ecig_in_all_Pennsylvania_tweets: ', len(propotion_Pennsylvania_ecig_in_all_Pennsylvania_tweets))


# propotion of Pennsylvania tweets in total tweets.
for i in range(37):
    propotion_Pennsylvania_in_all_tweets.append((allPennsylvania[i]/allTweets[i])*100)
print('length of propotion_Pennsylvania_in_all_tweets: ', len(propotion_Pennsylvania_in_all_tweets))


# propotion of users post Pennsylvania e-cig in all Pennsylvania users.
for i in range(37):
    propotion_Pennsylvania_ecig_users_in_all_Pennsylvania_users.append((users_Pennsylvania_ecig[i]/users_Pennsylvania[i])*100)
print('length of propotion_Pennsylvania_ecig_users_in_all_Pennsylvania_users: ', len(propotion_Pennsylvania_ecig_users_in_all_Pennsylvania_users))


# Sentiment analysis
for i in range(37):
    propotion_positive_ecig_Pennsylvania.append((vader_positive_Pennsylvania[i]/Pennsylvania_allECigarette[i])*100)
print('length of propotion_positive_ecig_Pennsylvania: ', len(propotion_positive_ecig_Pennsylvania))

for i in range(37):
    propotion_neutral_ecig_Pennsylvania.append((vader_neutral_Pennsylvania[i]/Pennsylvania_allECigarette[i])*100)
print('length of propotion_neutral_ecig_Pennsylvania: ', len(propotion_neutral_ecig_Pennsylvania))

for i in range(37):
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
for i in range(37):
    propotion_Maryland_ecig_in_all_ecig.append((Maryland_allECigarette[i]/allECigarette[i])*100)
print('length of propotion_Maryland_ecig_in_all_ecig: ', len(propotion_Maryland_ecig_in_all_ecig))


# propotion of Maryland e-cig tweets in all Maryland tweets.
for i in range(37):
    propotion_Maryland_ecig_in_all_Maryland_tweets.append((Maryland_allECigarette[i]/allMaryland[i])*100)
print('length of propotion_Maryland_ecig_in_all_Maryland_tweets: ', len(propotion_Maryland_ecig_in_all_Maryland_tweets))


# propotion of Maryland tweets in total tweets.
for i in range(37):
    propotion_Maryland_in_all_tweets.append((allMaryland[i]/allTweets[i])*100)
print('length of propotion_Maryland_in_all_tweets: ', len(propotion_Maryland_in_all_tweets))


# propotion of users post Maryland e-cig in all Maryland users.
for i in range(37):
    propotion_Maryland_ecig_users_in_all_Maryland_users.append((users_Maryland_ecig[i]/users_Maryland[i])*100)
print('length of propotion_Maryland_ecig_users_in_all_Maryland_users: ', len(propotion_Maryland_ecig_users_in_all_Maryland_users))


# Sentiment analysis
for i in range(37):
    propotion_positive_ecig_Maryland.append((vader_positive_Maryland[i]/Maryland_allECigarette[i])*100)
print('length of propotion_positive_ecig_Maryland: ', len(propotion_positive_ecig_Maryland))

for i in range(37):
    propotion_neutral_ecig_Maryland.append((vader_neutral_Maryland[i]/Maryland_allECigarette[i])*100)
print('length of propotion_neutral_ecig_Maryland: ', len(propotion_neutral_ecig_Maryland))

for i in range(37):
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
for i in range(37):
    propotion_DC_ecig_in_all_ecig.append((DC_allECigarette[i]/allECigarette[i])*100)
print('length of propotion_DC_ecig_in_all_ecig: ', len(propotion_DC_ecig_in_all_ecig))


# propotion of DC e-cig tweets in all DC tweets.
for i in range(37):
    propotion_DC_ecig_in_all_DC_tweets.append((DC_allECigarette[i]/allDC[i])*100)
print('length of propotion_DC_ecig_in_all_DC_tweets: ', len(propotion_DC_ecig_in_all_DC_tweets))


# propotion of DC tweets in total tweets.
for i in range(37):
    propotion_DC_in_all_tweets.append((allDC[i]/allTweets[i])*100)
print('length of propotion_DC_in_all_tweets: ', len(propotion_DC_in_all_tweets))


# propotion of users post DC e-cig in all DC users.
for i in range(37):
    propotion_DC_ecig_users_in_all_DC_users.append((users_DC_ecig[i]/users_DC[i])*100)
print('length of propotion_DC_ecig_users_in_all_DC_users: ', len(propotion_DC_ecig_users_in_all_DC_users))


# Sentiment analysis
for i in range(37):
    propotion_positive_ecig_DC.append((vader_positive_DC[i]/DC_allECigarette[i])*100)
print('length of propotion_positive_ecig_DC: ', len(propotion_positive_ecig_DC))

for i in range(37):
    propotion_neutral_ecig_DC.append((vader_neutral_DC[i]/DC_allECigarette[i])*100)
print('length of propotion_neutral_ecig_DC: ', len(propotion_neutral_ecig_DC))

for i in range(37):
    propotion_negative_ecig_DC.append((vader_negative_DC[i]/DC_allECigarette[i])*100)
print('length of propotion_negative_ecig_DC: ', len(propotion_negative_ecig_DC))

```
