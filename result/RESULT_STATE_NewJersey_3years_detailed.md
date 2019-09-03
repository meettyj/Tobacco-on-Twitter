# Number

```
# Number

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

# allTweets
allTweets = [70798094, 76153908, 77039352, 79730585, 75060717, 63144176, 68592777, 68306197, 60640789, 64761879, 49292002, 51379810, 46841051, 45592367, 46897952, 50163222, 51079160, 22112648, 31365136, 46232294, 43487766, 46059070, 40432909, 47289301, 45660765, 44166238, 44212483, 45858463, 39900707, 45395994, 37985764, 42937313, 41362576, 44209494, 38750216, 32702554, 33860264]
print('length of allTweets: ', len(allTweets))

print('----------------------------------')
# ----------------------------- NewYork -----------------------------

# NewYork_allECigarette
NewYork_allECigarette = [2073, 2234, 1699, 1849, 1370, 1243, 1523, 1209, 1041, 1911, 1539, 1190, 1623, 1019, 1249, 891, 1120, 789, 826, 1256, 960, 1183, 1023, 1151, 1121, 997, 1019, 1133, 1027, 1114, 960, 1061, 1015, 1079, 958, 872,923]
print('length of NewYork_allECigarette: ', len(NewYork_allECigarette))


# allNewYork
allNewYork = [3626674, 3861629, 3941920, 4060979, 3866119, 3376082, 3674126, 3717329, 3278175, 549723, 2865709, 2993131, 2715434, 2701304, 2771639, 2903591, 3003344, 1326427, 1920550, 2705189, 2528332, 2722419, 2383430, 2769473, 2704196, 2527171, 2603542, 2664648, 2370655, 2669574, 2294618, 2504632, 2469827, 2660919, 2363006, 2092840,2142446]
print('length of allNewYork: ', len(allNewYork))


# Number of users that tweets ecig in NewYork.
users_NewYork_ecig = [939, 941, 761, 900, 727, 661, 721, 680, 594, 613, 514, 665, 610, 573, 584, 562, 609, 335,445, 738, 690, 781, 653, 783, 807, 734, 745, 816, 762, 822, 715, 808, 757, 768, 666, 580,627]
print('length of users_NewYork_ecig: ', len(users_NewYork_ecig))


# average number of per person tweets about ecig in NewYork.
average_num_per_person_tweets_NewYork_ecig = []
for i in range(37):
    average_num_per_person_tweets_NewYork_ecig.append(NewYork_allECigarette[i]/users_NewYork_ecig[i])
print('length of average_num_per_person_tweets_NewYork_ecig: ', len(average_num_per_person_tweets_NewYork_ecig))


# Number of users that tweets in NewYork
users_NewYork = [198472, 204189, 219945, 224921, 216745, 205584, 206468, 206397, 197269, 187634, 171851, 184050, 176663, 177543, 182446, 184666, 185744, 128686,148851, 180787, 175832, 160125, 149672, 168996, 162489, 151919, 162487, 165668, 155984, 165051, 150540, 155580, 155211, 144775, 134813, 134313, 124152]
print('length of users_NewYork: ', len(users_NewYork))

# average number of per person tweets in NewYork.
average_num_per_person_tweets_NewYork = []
for i in range(37):
    average_num_per_person_tweets_NewYork.append(allNewYork[i]/users_NewYork[i])
print('length of average_num_per_person_tweets_NewYork: ', len(average_num_per_person_tweets_NewYork))

# Sentiment analysis
vader_positive_NewYork = [675, 1109, 827, 803, 472, 432, 622, 375, 333, 1027, 584, 446, 352, 310, 309, 333, 515, 263,211, 376, 351, 406, 325, 343, 343, 305, 302, 365, 345, 369, 323, 315, 315, 321, 275, 265,285]
vader_neutral_NewYork = [1129, 852, 663, 796, 711, 595, 711, 661, 540, 703, 809, 561, 1121, 552, 808, 415, 433, 439,495, 670, 430, 553, 476, 585, 570, 465, 512, 509, 464, 485, 404, 473, 469, 504, 447, 419,435]
vader_negative_NewYork = [269, 273, 209, 250, 187, 216, 190, 173, 168, 181, 146, 183, 150, 157, 132, 143, 172, 87,120, 210, 179, 224, 222, 223, 208, 227, 205, 259, 218, 260, 233, 273, 231, 254, 236, 188,203]
print('length of vader_positive_NewYork: ', len(vader_positive_NewYork))
print('length of vader_neutral_NewYork: ', len(vader_neutral_NewYork))
print('length of vader_negative_NewYork: ', len(vader_negative_NewYork))



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
# ----------------------------- Connecticut -----------------------------

# Connecticut_allECigarette
Connecticut_allECigarette = [161, 193, 178, 146, 143, 98, 129, 121, 116, 97, 84, 139, 67, 63, 95, 101, 84, 44, 59, 138, 123, 134, 151, 109, 106, 119, 99, 119, 100, 122, 124, 154, 116, 143, 156, 82, 90]
print('length of Connecticut_allECigarette: ', len(Connecticut_allECigarette))


# allConnecticut
allConnecticut = [546162, 610388, 584132, 619326, 581300, 481498, 504906, 505755, 453787, 496551, 392276, 406015, 375136, 374616, 375955, 389407, 389068, 162785, 232408, 341011, 336207, 374371, 336945, 399568, 370847, 348013, 346166, 370594, 304720, 339855, 305354, 335913, 318357, 346063, 290734, 242881, 244552]
print('length of allConnecticut: ', len(allConnecticut))


# Number of users that tweets ecig in Connecticut.
users_Connecticut_ecig = [118, 120, 101, 111, 102, 74, 86, 87, 73, 70, 54, 87, 57, 58, 71, 74, 68, 39,51, 103, 110, 115, 89, 98, 90, 91, 71, 96, 85, 97, 92, 118, 91, 118, 100, 61, 67]
print('length of users_Connecticut_ecig: ', len(users_Connecticut_ecig))


# average number of per person tweets about ecig in Connecticut.
average_num_per_person_tweets_Connecticut_ecig = []
for i in range(37):
    average_num_per_person_tweets_Connecticut_ecig.append(Connecticut_allECigarette[i]/users_Connecticut_ecig[i])
print('length of average_num_per_person_tweets_Connecticut_ecig: ', len(average_num_per_person_tweets_Connecticut_ecig))


# Number of users that tweets in Connecticut
users_Connecticut = [26719, 28215, 29339, 31232, 29540, 25671, 27415, 27653, 25141, 23888, 21860, 22709, 22452, 22664, 23023, 24371, 24409, 15346,18454, 23128, 21833, 19551, 18621, 20848, 20893, 19874, 20574, 21762, 19990, 20300, 18618, 20145, 19466, 17873, 16795, 16483,14849]
print('length of users_Connecticut: ', len(users_Connecticut))

# average number of per person tweets in Connecticut.
average_num_per_person_tweets_Connecticut = []
for i in range(37):
    average_num_per_person_tweets_Connecticut.append(allConnecticut[i]/users_Connecticut[i])
print('length of average_num_per_person_tweets_Connecticut: ', len(average_num_per_person_tweets_Connecticut))

# Sentiment analysis
vader_positive_Connecticut = [52, 48, 45, 50, 50, 36, 47, 44, 42, 40, 22, 41, 24, 22, 25, 35, 23, 13,14, 49, 42, 43, 48, 37, 37, 44, 30, 32, 23, 41, 33, 50, 33, 39, 64, 25, 32]
vader_neutral_Connecticut = [80, 114, 105, 73, 66, 43, 55, 57, 52, 37, 49, 75, 35, 30, 50, 49, 45, 24, 31, 58, 48, 55, 60, 50, 51, 54, 41, 61, 48, 52, 60, 57, 53, 61, 55, 45, 48]
vader_negative_Connecticut = [29, 31, 28, 23, 27, 19, 27, 20, 22, 20, 13, 23, 8, 11, 20, 17, 16, 7, 14, 31, 33, 36, 43, 22, 18, 21, 28, 26, 29, 29, 31, 47, 30, 43, 37, 12, 10]
print('length of vader_positive_Connecticut: ', len(vader_positive_Connecticut))
print('length of vader_neutral_Connecticut: ', len(vader_neutral_Connecticut))
print('length of vader_negative_Connecticut: ', len(vader_negative_Connecticut))


print('----------------------------------')
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


# Sentiment analysis
vader_positive_Delaware = [3, 12, 5, 13, 3, 4, 6, 5, 0,3, 2, 4, 2, 2, 3, 6, 2, 0, 2, 4, 3, 5, 1, 5, 5, 9, 8, 6, 13, 2, 6, 5, 4, 5, 4, 6, 3]
vader_neutral_Delaware = [3, 12, 14, 11, 5, 7, 3, 6, 5, 2, 4, 7, 3, 2, 5, 8, 1, 7, 1, 8, 9, 10, 7, 3, 12, 3, 20, 15, 12, 6, 8, 4, 8, 5, 7, 8, 7]
vader_negative_Delaware = [3, 5, 4, 4, 1, 4, 4, 4, 1,2, 0, 2, 0, 1, 1, 2, 2, 3, 4, 5, 5, 2, 4, 5, 6, 3, 4,2, 3, 4, 3, 13, 5, 3, 2, 6, 4]
print('length of vader_positive_Delaware: ', len(vader_positive_Delaware))
print('length of vader_neutral_Delaware: ', len(vader_neutral_Delaware))
print('length of vader_negative_Delaware: ', len(vader_negative_Delaware))


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
# ----------------------------- NewYork -----------------------------
propotion_NewYork_ecig_in_all_ecig = []
propotion_NewYork_ecig_in_all_NewYork_tweets = []
propotion_NewYork_in_all_tweets = []
propotion_NewYork_ecig_users_in_all_NewYork_users = []
propotion_positive_ecig_NewYork = []
propotion_neutral_ecig_NewYork = []
propotion_negative_ecig_NewYork = []


# propotion of NewYork e-cig tweets in all e-cig tweets.
for i in range(37):
    propotion_NewYork_ecig_in_all_ecig.append((NewYork_allECigarette[i]/allECigarette[i])*100)
print('length of propotion_NewYork_ecig_in_all_ecig: ', len(propotion_NewYork_ecig_in_all_ecig))


# propotion of NewYork e-cig tweets in all NewYork tweets.
for i in range(37):
    propotion_NewYork_ecig_in_all_NewYork_tweets.append((NewYork_allECigarette[i]/allNewYork[i])*100)
print('length of propotion_NewYork_ecig_in_all_NewYork_tweets: ', len(propotion_NewYork_ecig_in_all_NewYork_tweets))


# propotion of NewYork tweets in total tweets.
for i in range(37):
    propotion_NewYork_in_all_tweets.append((allNewYork[i]/allTweets[i])*100)
print('length of propotion_NewYork_in_all_tweets: ', len(propotion_NewYork_in_all_tweets))


# propotion of users post NewYork e-cig in all NewYork users.
for i in range(37):
    propotion_NewYork_ecig_users_in_all_NewYork_users.append((users_NewYork_ecig[i]/users_NewYork[i])*100)
print('length of propotion_NewYork_ecig_users_in_all_NewYork_users: ', len(propotion_NewYork_ecig_users_in_all_NewYork_users))


# Sentiment analysis
for i in range(37):
    propotion_positive_ecig_NewYork.append((vader_positive_NewYork[i]/NewYork_allECigarette[i])*100)
print('length of propotion_positive_ecig_NewYork: ', len(propotion_positive_ecig_NewYork))

for i in range(37):
    propotion_neutral_ecig_NewYork.append((vader_neutral_NewYork[i]/NewYork_allECigarette[i])*100)
print('length of propotion_neutral_ecig_NewYork: ', len(propotion_neutral_ecig_NewYork))

for i in range(37):
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
# ----------------------------- Connecticut -----------------------------
propotion_Connecticut_ecig_in_all_ecig = []
propotion_Connecticut_ecig_in_all_Connecticut_tweets = []
propotion_Connecticut_in_all_tweets = []
propotion_Connecticut_ecig_users_in_all_Connecticut_users = []
propotion_positive_ecig_Connecticut = []
propotion_neutral_ecig_Connecticut = []
propotion_negative_ecig_Connecticut = []


# propotion of Connecticut e-cig tweets in all e-cig tweets.
for i in range(37):
    propotion_Connecticut_ecig_in_all_ecig.append((Connecticut_allECigarette[i]/allECigarette[i])*100)
print('length of propotion_Connecticut_ecig_in_all_ecig: ', len(propotion_Connecticut_ecig_in_all_ecig))


# propotion of Connecticut e-cig tweets in all Connecticut tweets.
for i in range(37):
    propotion_Connecticut_ecig_in_all_Connecticut_tweets.append((Connecticut_allECigarette[i]/allConnecticut[i])*100)
print('length of propotion_Connecticut_ecig_in_all_Connecticut_tweets: ', len(propotion_Connecticut_ecig_in_all_Connecticut_tweets))


# propotion of Connecticut tweets in total tweets.
for i in range(37):
    propotion_Connecticut_in_all_tweets.append((allConnecticut[i]/allTweets[i])*100)
print('length of propotion_Connecticut_in_all_tweets: ', len(propotion_Connecticut_in_all_tweets))


# propotion of users post Connecticut e-cig in all Connecticut users.
for i in range(37):
    propotion_Connecticut_ecig_users_in_all_Connecticut_users.append((users_Connecticut_ecig[i]/users_Connecticut[i])*100)
print('length of propotion_Connecticut_ecig_users_in_all_Connecticut_users: ', len(propotion_Connecticut_ecig_users_in_all_Connecticut_users))


# Sentiment analysis
for i in range(37):
    propotion_positive_ecig_Connecticut.append((vader_positive_Connecticut[i]/Connecticut_allECigarette[i])*100)
print('length of propotion_positive_ecig_Connecticut: ', len(propotion_positive_ecig_Connecticut))

for i in range(37):
    propotion_neutral_ecig_Connecticut.append((vader_neutral_Connecticut[i]/Connecticut_allECigarette[i])*100)
print('length of propotion_neutral_ecig_Connecticut: ', len(propotion_neutral_ecig_Connecticut))

for i in range(37):
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


```


