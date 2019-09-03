# Number

```
# ----------------------------- California -----------------------------
# California_allECigarette_2017
California_allECigarette_2017 = [3406, 3295, 3464, 3785, 3115, 2627, 2688, 2537, 2516, 2367, 1988, 2092, 1805, 1737, 1771, 1909, 2033, 976, 1174, 1961, 2008, 2166, 1834, 2160, 2174, 1757, 1938, 2211, 1932, 2011, 1690, 2034, 2031, 2165, 1971, 1596, 1544]
print('length of California_allECigarette_2017: ', len(California_allECigarette_2017))

# not_California_allECigarette_2017
not_California_allECigarette_2017 = [19380, 21312, 17787, 19894, 17102, 13671, 14918, 14216, 13899, 15672, 11836, 12673, 12472, 11343, 11850, 11658, 12056, 5957, 8171, 13678, 13673, 15190, 13575, 15162, 15074, 13785, 14365, 16659, 15466, 17157, 13417, 17025, 15639, 16531, 14324, 12092, 11782]
print('length of not_California_allECigarette_2017: ', len(not_California_allECigarette_2017))

# allECigarette_2017
allECigarette_2017 = []
for i in range(37):
    allECigarette_2017.append(California_allECigarette_2017[i]+not_California_allECigarette_2017[i])
print('length of allECigarette_2017: ', len(allECigarette_2017))


# allCalifornia_2017
allCalifornia_2017 = [8735704, 9439283, 10060029, 10166810, 9452532, 7724895, 8270415, 8050048, 7065826, 7688806, 5950614, 6130864, 5623066, 5542298, 5872374, 6284243, 6242231, 2686895, 3874158, 5584508, 5218406, 5561829, 4905649, 5727563, 5502914, 5377620, 5627578, 5879980, 5000225, 5381725, 4592721, 5047163, 4900812, 5342015, 4795218, 3958389, 4210282]
print('length of allCalifornia_2017: ', len(allCalifornia_2017))


# Number of users that tweets ecig in California.
users_California_ecig_2017 = [2065, 2205, 2054, 2264, 1817, 1521, 1507, 1366, 1293, 1313, 1131, 1230, 1097, 1084, 1149, 1264, 1246, 647, 852, 1351, 1397, 1494, 1285, 1497, 1507, 1325, 1388, 1476, 1356, 1382, 1196, 1458, 1371, 1568, 1427, 1105, 1048]
print('length of users_California_ecig_2017: ', len(users_California_ecig_2017))


# average number of per person tweets about ecig in California.
average_num_per_person_tweets_California_ecig = []
for i in range(37):
    average_num_per_person_tweets_California_ecig.append(California_allECigarette_2017[i]/users_California_ecig_2017[i])
print('length of average_num_per_person_tweets_California_ecig: ', len(average_num_per_person_tweets_California_ecig))


# Number of users that tweets in California
# 04, 05,06,07,08,09,10,
# 360175, 365369, 395811, 409394, 387877, 351081, 361695,351973, 326733, 
# 293996, 281709,309755, 300606,279575, 295525,309587,285522,283311,270281,278072,268812,270915,256192,251221, 229056

users_California_2017 = [360175, 365369, 395811, 409394, 387877, 351081, 361695,351973, 326733, 333885, 307678, 325899, 312275, 309270, 323365, 336303, 330514, 231445, 271542, 316768, 300338,293996, 281709,309755, 300606,279575, 295525,309587,285522,283311,270281,278072,268812,270915,256192,251221, 229056]
print('length of users_California_2017: ', len(users_California_2017))

# average number of per person tweets in California.
average_num_per_person_tweets_California = []
for i in range(37):
    average_num_per_person_tweets_California.append(allCalifornia_2017[i]/users_California_2017[i])
print('length of average_num_per_person_tweets_California: ', len(average_num_per_person_tweets_California))

# allTweets
allTweets_2017 = [70798094, 76153908, 77039352, 79730585, 75060717, 63144176, 68592777, 68306197, 60640789, 64761879, 49292002, 51379810, 46841051, 45592367, 46897952, 50163222, 51079160, 22112648, 31365136, 46232294, 43487766, 46059070, 40432909, 47289301, 45660765, 44166238, 44212483, 45858463, 39900707, 45395994, 37985764, 42937313, 41362576, 44209494, 38750216, 32702554, 33860264]
print('length of allTweets_2017: ', len(allTweets_2017))

# Sentiment analysis
vader_positive_California_2017 = [1109, 1114, 1084, 1261, 1036, 876, 944, 853, 853, 775, 667, 719, 580, 590, 565, 605, 693, 328, 378, 645, 672, 667, 543, 680, 683, 520, 625, 735, 625, 678, 528, 670, 665, 653, 629, 540, 516]
vader_neutral_California_2017 = [1727, 1572, 1803, 1919, 1563, 1330, 1307, 1281, 1274, 1187, 1025, 1058, 942, 874, 891, 975, 991, 500, 582, 936, 891, 1034, 911, 995, 1092, 835, 903, 1013, 902, 903, 778, 895, 900, 1001, 893, 712, 700]
vader_negative_California_2017 = [570, 609, 577, 605, 516, 421, 437, 403, 389, 405, 296, 315, 283, 273, 315, 329, 349, 148, 214, 380, 445,465, 380, 485, 399, 402, 410, 463, 405, 430, 384, 469, 466, 511, 449, 344, 328]
print('length of vader_positive_California_2017: ', len(vader_positive_California_2017))
print('length of vader_neutral_California_2017: ', len(vader_neutral_California_2017))
print('length of vader_negative_California_2017: ', len(vader_negative_California_2017))

print('----------------------------------')
# ----------------------------- Oregon -----------------------------

# Oregon_allECigarette_2017
Oregon_allECigarette_2017 = [274, 302, 240, 307, 225, 244, 281, 325, 281, 261, 195, 233, 221, 258, 263, 273, 257, 119, 152, 237, 284, 263, 209, 212, 214, 192, 192, 207, 229, 233, 153, 222, 183, 223, 166, 148, 146]
print('length of Oregon_allECigarette_2017: ', len(Oregon_allECigarette_2017))


# allOregon_2017
allOregon_2017 = [599777, 644250, 612666, 618797, 575851, 512339, 565743, 570314, 495921, 576389, 451267, 489471, 432418, 409505, 414368, 441048, 460374, 209586, 283148, 430226, 383564, 417210, 379330, 425150, 401396, 385676, 404462, 408670, 369111, 411442, 345204, 394339, 364140, 406922, 368350, 309742, 325747]
print('length of allOregon_2017: ', len(allOregon_2017))


# Number of users that tweets ecig in Oregon.
users_Oregon_ecig_2017 = [163, 178, 154, 202, 143, 121, 135, 145, 111, 121, 93, 118, 123, 103, 106, 124, 139, 64, 98, 156, 164, 164, 138, 116, 129, 134, 135, 150, 137, 148, 111, 153, 130, 149, 132, 94, 94]
print('length of users_Oregon_ecig_2017: ', len(users_Oregon_ecig_2017))


# average number of per person tweets about ecig in Oregon.
average_num_per_person_tweets_Oregon_ecig = []
for i in range(37):
    average_num_per_person_tweets_Oregon_ecig.append(Oregon_allECigarette_2017[i]/users_Oregon_ecig_2017[i])
print('length of average_num_per_person_tweets_Oregon_ecig: ', len(average_num_per_person_tweets_Oregon_ecig))


# Number of users that tweets in Oregon
users_Oregon_2017 = [30984, 32054, 34350, 36517, 34460, 31271, 31934, 30752, 28886,28914, 26389, 27777, 26903, 26769, 28342, 29185, 31473, 20171, 23160, 27581, 25123, 23666, 23408, 25586, 24886, 23210, 25547, 26353, 24030, 24797, 22385, 23075, 21674, 21182, 20600, 20306, 18434]
print('length of users_Oregon_2017: ', len(users_Oregon_2017))

# average number of per person tweets in Oregon.
average_num_per_person_tweets_Oregon = []
for i in range(37):
    average_num_per_person_tweets_Oregon.append(allOregon_2017[i]/users_Oregon_2017[i])
print('length of average_num_per_person_tweets_Oregon: ', len(average_num_per_person_tweets_Oregon))

# Sentiment analysis
vader_positive_Oregon_2017 = [99, 111, 85, 129, 84, 92, 120, 117, 128, 107, 82, 100, 87, 94, 105, 103, 72, 39, 43, 78, 84, 94, 75, 66, 72, 57, 67, 69, 74, 91, 51, 73, 54, 83, 50, 42, 49]
vader_neutral_Oregon_2017 = [137, 130, 106, 136, 108, 117, 127, 173, 129,108, 85, 97, 106, 139, 127, 137, 148, 60, 84, 108, 139, 114, 84, 113, 105, 101, 89, 93, 107, 103, 64, 91, 94, 95, 78, 79, 68]
vader_negative_Oregon_2017 = [38, 61, 49, 42, 33, 35, 34, 35, 24,46, 28, 36, 28, 25, 31, 33, 37, 20, 25, 51, 61, 55, 50, 33, 37, 34, 36, 45, 48, 39, 38, 58, 35, 45, 38, 27, 29]
print('length of vader_positive_Oregon_2017: ', len(vader_positive_Oregon_2017))
print('length of vader_neutral_Oregon_2017: ', len(vader_neutral_Oregon_2017))
print('length of vader_negative_Oregon_2017: ', len(vader_negative_Oregon_2017))


print('----------------------------------')
# ----------------------------- Nevada -----------------------------

# Nevada_allECigarette_2017
Nevada_allECigarette_2017 = [492, 371, 316, 388, 429, 319, 380, 427, 320, 481, 518, 516, 546, 487, 436, 417, 336, 92, 128, 245, 253, 236, 221, 221, 208, 240, 214, 276, 241, 264, 228, 288, 271, 295, 258, 198, 184]
print('length of Nevada_allECigarette_2017: ', len(Nevada_allECigarette_2017))


# allNevada_2017
allNevada_2017 = [728432, 794363, 859419, 921170, 797947, 671803, 719944, 715447, 641579, 681641, 511694, 559172, 508382, 503636, 544346, 580917, 585303, 241846, 363262, 539410, 487596, 546049, 483434, 582721, 568494, 568432, 558238, 596718, 480559, 546846, 439811, 481335, 490998, 553409, 480211, 413775, 426641]
print('length of allNevada_2017: ', len(allNevada_2017))


# Number of users that tweets ecig in Nevada.
users_Nevada_ecig_2017 = [181, 206, 200, 199, 175, 130, 158, 149, 135, 123, 117, 130, 134, 111, 135, 160, 139, 68, 93, 185, 177,175, 168, 165, 151, 178, 164, 201, 149, 166, 134, 183, 182, 191, 170, 135, 129]
print('length of users_Nevada_ecig_2017: ', len(users_Nevada_ecig_2017))


# average number of per person tweets about ecig in Nevada.
average_num_per_person_tweets_Nevada_ecig = []
for i in range(37):
    average_num_per_person_tweets_Nevada_ecig.append(Nevada_allECigarette_2017[i]/users_Nevada_ecig_2017[i])
print('length of average_num_per_person_tweets_Nevada_ecig: ', len(average_num_per_person_tweets_Nevada_ecig))


# Number of users that tweets in Nevada
users_Nevada_2017 = [43980, 44552, 51813, 57165, 49885, 42041, 44345, 42735, 40257, 43055, 35526, 42399, 39318, 38744, 43377, 46753, 44795, 25326, 31593, 38779, 37093, 38441, 33971, 41728, 38627, 37988, 37442, 43248, 37931, 38681, 34131, 36964, 35012, 37538, 32326, 34087, 30886]
print('length of users_Nevada_2017: ', len(users_Nevada_2017))

# average number of per person tweets in Nevada.
average_num_per_person_tweets_Nevada = []
for i in range(37):
    average_num_per_person_tweets_Nevada.append(allNevada_2017[i]/users_Nevada_2017[i])
print('length of average_num_per_person_tweets_Nevada: ', len(average_num_per_person_tweets_Nevada))


# Sentiment analysis
vader_positive_Nevada_2017 = [212, 133, 122, 111, 141, 138, 175, 229, 96, 154, 322, 328, 350, 305, 291, 253, 194, 33, 52, 81, 83, 75, 73, 67, 74, 82, 63, 94, 82, 90, 76, 113, 91, 89, 95, 65, 53]
vader_neutral_Nevada_2017 = [214, 181, 164, 211, 230, 142, 169, 166, 183, 288, 157, 146, 163, 152, 106, 117, 109, 38, 53, 112, 111, 105, 97, 103, 86, 99, 110, 134, 125, 117, 110, 125, 113, 149, 116, 82, 96]
vader_negative_Nevada_2017 = [66, 57, 30, 66, 58, 39, 36, 32, 41, 39, 39, 42, 33, 30, 39, 47, 33, 21, 23, 52, 59, 56, 51, 51, 48, 59, 41, 48, 34, 57, 42, 50, 67, 57, 47, 51, 35]
print('length of vader_positive_Nevada_2017: ', len(vader_positive_Nevada_2017))
print('length of vader_neutral_Nevada_2017: ', len(vader_neutral_Nevada_2017))
print('length of vader_negative_Nevada_2017: ', len(vader_negative_Nevada_2017))


print('----------------------------------')
# ----------------------------- Arizona -----------------------------

# Arizona_allECigarette_2017
Arizona_allECigarette_2017 = [568, 636, 450, 453, 630, 362, 430, 419, 353, 422, 293, 336, 411, 302, 230, 292, 325, 162, 253, 409, 382, 442, 412, 416, 360, 405, 381, 358, 371, 382, 320, 426, 413, 406, 389, 283, 286]
print('length of Arizona_allECigarette_2017: ', len(Arizona_allECigarette_2017))


# allArizona_2017
allArizona_2017 = [1262589, 1285618, 1298666, 1334544, 1280635, 1132938, 1217316, 1167490, 982169, 1086204, 852986, 864083, 773664, 715142, 726453, 798319, 851711, 376349, 527391, 764080, 704562, 776647, 695828, 795739, 779177, 726661, 715880, 736675, 662689, 758293, 625817, 703006, 660777, 742468, 653478, 554828, 549231]
print('length of allArizona_2017: ', len(allArizona_2017))


# Number of users that tweets ecig in Arizona.
users_Arizona_ecig_2017 = [397, 450, 320, 350, 314, 275, 334, 293, 248, 290, 210, 256, 260, 200, 161, 229, 261, 132, 215, 330, 296,330, 304, 329, 282, 291, 291, 284, 307, 297, 251, 304, 292, 318, 280, 220, 196]
print('length of users_Arizona_ecig_2017: ', len(users_Arizona_ecig_2017))


# average number of per person tweets about ecig in Arizona.
average_num_per_person_tweets_Arizona_ecig = []
for i in range(37):
    average_num_per_person_tweets_Arizona_ecig.append(Arizona_allECigarette_2017[i]/users_Arizona_ecig_2017[i])
print('length of average_num_per_person_tweets_Arizona_ecig: ', len(average_num_per_person_tweets_Arizona_ecig))


# Number of users that tweets in Arizona
users_Arizona_2017 = [52763, 53112, 53964, 56318, 55317, 51738, 53956, 53488, 51121, 50460, 46956, 53007, 47507, 44051, 43259, 45744, 47430, 33200, 39831, 48491, 46966, 44665, 44570, 50916, 45998, 42231, 40754, 42731, 41412, 42470, 40395, 42791, 42693, 43481, 40832, 40712, 33816]
print('length of users_Arizona_2017: ', len(users_Arizona_2017))

# average number of per person tweets in Arizona.
average_num_per_person_tweets_Arizona = []
for i in range(37):
    average_num_per_person_tweets_Arizona.append(allArizona_2017[i]/users_Arizona_2017[i])
print('length of average_num_per_person_tweets_Arizona: ', len(average_num_per_person_tweets_Arizona))

# Sentiment analysis
vader_positive_Arizona_2017 = [201, 242, 159, 173, 198, 128, 136, 148, 110, 121, 89, 113, 156, 100, 74, 81, 102, 59, 74, 137, 104, 146, 117, 136, 116, 107, 110, 107, 140, 103, 105, 117, 143, 121, 117, 84, 100]
vader_neutral_Arizona_2017 = [264, 277, 218, 198, 298, 151, 205, 186, 169, 224, 137, 155, 185, 135, 95, 149, 148, 73, 124, 154, 172, 197, 184, 195, 153, 195, 180, 143, 139, 159, 138, 183, 184, 177, 181, 133, 115]
vader_negative_Arizona_2017 = [103, 117, 73, 82, 134, 83, 89, 85, 74, 77, 67, 68, 70, 67, 61, 62, 75, 30, 55, 118, 106, 99, 111, 85, 91, 103, 91, 108, 92, 120, 77, 126, 86, 108, 91, 66, 71]
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
for i in range(37):
    propotion_California_ecig_in_all_ecig.append((California_allECigarette_2017[i]/allECigarette_2017[i])*100)
print('length of propotion_California_ecig_in_all_ecig: ', len(propotion_California_ecig_in_all_ecig))


# propotion of California e-cig tweets in all California tweets.
for i in range(37):
    propotion_California_ecig_in_all_California_tweets.append((California_allECigarette_2017[i]/allCalifornia_2017[i])*100)
print('length of propotion_California_ecig_in_all_California_tweets: ', len(propotion_California_ecig_in_all_California_tweets))


# propotion of California tweets in total tweets.
for i in range(37):
    propotion_California_in_all_tweets.append((allCalifornia_2017[i]/allTweets_2017[i])*100)
print('length of propotion_California_in_all_tweets: ', len(propotion_California_in_all_tweets))


# propotion of users post California e-cig in all California users.
# for i in range(37):
#     propotion_California_ecig_users_in_all_California_users.append((users_California_ecig_2017[i]/users_California_2017[i])*100)
# print('length of propotion_California_ecig_users_in_all_California_users: ', len(propotion_California_ecig_users_in_all_California_users))


# Sentiment analysis
for i in range(37):
    propotion_positive_ecig_California.append((vader_positive_California_2017[i]/California_allECigarette_2017[i])*100)
print('length of propotion_positive_ecig_California: ', len(propotion_positive_ecig_California))

for i in range(37):
    propotion_neutral_ecig_California.append((vader_neutral_California_2017[i]/California_allECigarette_2017[i])*100)
print('length of propotion_neutral_ecig_California: ', len(propotion_neutral_ecig_California))

for i in range(37):
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
for i in range(37):
    propotion_Oregon_ecig_in_all_ecig.append((Oregon_allECigarette_2017[i]/allECigarette_2017[i])*100)
print('length of propotion_Oregon_ecig_in_all_ecig: ', len(propotion_Oregon_ecig_in_all_ecig))


# propotion of Oregon e-cig tweets in all Oregon tweets.
for i in range(37):
    propotion_Oregon_ecig_in_all_Oregon_tweets.append((Oregon_allECigarette_2017[i]/allOregon_2017[i])*100)
print('length of propotion_Oregon_ecig_in_all_Oregon_tweets: ', len(propotion_Oregon_ecig_in_all_Oregon_tweets))


# propotion of Oregon tweets in total tweets.
for i in range(37):
    propotion_Oregon_in_all_tweets.append((allOregon_2017[i]/allTweets_2017[i])*100)
print('length of propotion_Oregon_in_all_tweets: ', len(propotion_Oregon_in_all_tweets))


# propotion of users post Oregon e-cig in all Oregon users.
for i in range(37):
    propotion_Oregon_ecig_users_in_all_Oregon_users.append((users_Oregon_ecig_2017[i]/users_Oregon_2017[i])*100)
print('length of propotion_Oregon_ecig_users_in_all_Oregon_users: ', len(propotion_Oregon_ecig_users_in_all_Oregon_users))


# Sentiment analysis
for i in range(37):
    propotion_positive_ecig_Oregon.append((vader_positive_Oregon_2017[i]/Oregon_allECigarette_2017[i])*100)
print('length of propotion_positive_ecig_Oregon: ', len(propotion_positive_ecig_Oregon))

for i in range(37):
    propotion_neutral_ecig_Oregon.append((vader_neutral_Oregon_2017[i]/Oregon_allECigarette_2017[i])*100)
print('length of propotion_neutral_ecig_Oregon: ', len(propotion_neutral_ecig_Oregon))

for i in range(37):
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
for i in range(37):
    propotion_Nevada_ecig_in_all_ecig.append((Nevada_allECigarette_2017[i]/allECigarette_2017[i])*100)
print('length of propotion_Nevada_ecig_in_all_ecig: ', len(propotion_Nevada_ecig_in_all_ecig))


# propotion of Nevada e-cig tweets in all Nevada tweets.
for i in range(37):
    propotion_Nevada_ecig_in_all_Nevada_tweets.append((Nevada_allECigarette_2017[i]/allNevada_2017[i])*100)
print('length of propotion_Nevada_ecig_in_all_Nevada_tweets: ', len(propotion_Nevada_ecig_in_all_Nevada_tweets))


# propotion of Nevada tweets in total tweets.
for i in range(37):
    propotion_Nevada_in_all_tweets.append((allNevada_2017[i]/allTweets_2017[i])*100)
print('length of propotion_Nevada_in_all_tweets: ', len(propotion_Nevada_in_all_tweets))


# propotion of users post Nevada e-cig in all Nevada users.
for i in range(37):
    propotion_Nevada_ecig_users_in_all_Nevada_users.append((users_Nevada_ecig_2017[i]/users_Nevada_2017[i])*100)
print('length of propotion_Nevada_ecig_users_in_all_Nevada_users: ', len(propotion_Nevada_ecig_users_in_all_Nevada_users))


# Sentiment analysis
for i in range(37):
    propotion_positive_ecig_Nevada.append((vader_positive_Nevada_2017[i]/Nevada_allECigarette_2017[i])*100)
print('length of propotion_positive_ecig_Nevada: ', len(propotion_positive_ecig_Nevada))

for i in range(37):
    propotion_neutral_ecig_Nevada.append((vader_neutral_Nevada_2017[i]/Nevada_allECigarette_2017[i])*100)
print('length of propotion_neutral_ecig_Nevada: ', len(propotion_neutral_ecig_Nevada))

for i in range(37):
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
for i in range(37):
    propotion_Arizona_ecig_in_all_ecig.append((Arizona_allECigarette_2017[i]/allECigarette_2017[i])*100)
print('length of propotion_Arizona_ecig_in_all_ecig: ', len(propotion_Arizona_ecig_in_all_ecig))


# propotion of Arizona e-cig tweets in all Arizona tweets.
for i in range(37):
    propotion_Arizona_ecig_in_all_Arizona_tweets.append((Arizona_allECigarette_2017[i]/allArizona_2017[i])*100)
print('length of propotion_Arizona_ecig_in_all_Arizona_tweets: ', len(propotion_Arizona_ecig_in_all_Arizona_tweets))


# propotion of Arizona tweets in total tweets.
for i in range(37):
    propotion_Arizona_in_all_tweets.append((allArizona_2017[i]/allTweets_2017[i])*100)
print('length of propotion_Arizona_in_all_tweets: ', len(propotion_Arizona_in_all_tweets))


# propotion of users post Arizona e-cig in all Arizona users.
for i in range(37):
    propotion_Arizona_ecig_users_in_all_Arizona_users.append((users_Arizona_ecig_2017[i]/users_Arizona_2017[i])*100)
print('length of propotion_Arizona_ecig_users_in_all_Arizona_users: ', len(propotion_Arizona_ecig_users_in_all_Arizona_users))


# Sentiment analysis
for i in range(37):
    propotion_positive_ecig_Arizona.append((vader_positive_Arizona_2017[i]/Arizona_allECigarette_2017[i])*100)
print('length of propotion_positive_ecig_Arizona: ', len(propotion_positive_ecig_Arizona))

for i in range(37):
    propotion_neutral_ecig_Arizona.append((vader_neutral_Arizona_2017[i]/Arizona_allECigarette_2017[i])*100)
print('length of propotion_neutral_ecig_Arizona: ', len(propotion_neutral_ecig_Arizona))

for i in range(37):
    propotion_negative_ecig_Arizona.append((vader_negative_Arizona_2017[i]/Arizona_allECigarette_2017[i])*100)
print('length of propotion_negative_ecig_Arizona: ', len(propotion_negative_ecig_Arizona))



```

