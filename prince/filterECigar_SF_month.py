import os
# os.chdir('C:/Users/eddie/Desktop/Prof. Rumi Chunara/alcohol')
import json
import pandas as pd

# def writeECigaretteToFile(eCigaretteList):
#     allECigarette_FileName = '/scratch/yt1506/juliana_allECigarette_2019_01.txt'
#     with open(allECigarette_FileName, "a", encoding="utf-8") as f:
#         for line in eCigaretteList:
#             f.write(line+'\n')

ECigar_keywords = ['smokestiks', 'v2 cig', 'v2 cigs', 'v2cigs', 'v2cig', 'mistic',
                   '21st century smoke', 'logic black label', 'finiti', 'nicotek',
                   'cigirex', 'logic platinum', 'cigalectric', 'xhale o2', 'cig2o',
                   'green smart living', 'krave', 'secondhand vape', 'secondhand vaping',
                   'second-hand vape', 'second-hand vaping', 'vape smoke', 'ecig smoke',
                   'e-cig smoke', 'e-cigarette smoke', 'vape shs', 'ecig shs',
                   'vape secondhand smoke', 'vape second-hand smoke', 'esmoke', 'esmoke',
                   'stillblowingsmoke', 'still blowing smoke', 'notblowingsmoke',
                   'not blowing smoke', 'capublichealth', 'tobaccofreekids', 'notareplacement',
                   'trulyfree', 'truly free', 'sb140', 'sb 140', 'sb24', 'sb 24',
                   'cherry tip cigarillos', 'mini-cigarillos', 'tip cigarillos',
                   'king edward cigars', 'royal gold cigars', 'sweet coronella',
                   'swisher blk', 'swisher sweets', 'vapercon', 'vapercon west',
                   'grimmgreen', 'vapor', 'electronic cigarette', 'vape meet',
                   'ecigssavelive', 'ecigssavelives', 'ecigssaveslives']


def checkECigaretteInLine(line):
    # lineInJson = json.loads(line)
    # textInLine = lineInJson["text"]
    line = str(line)
    # lowercaseLine = textInLine.lower()
    lowercaseLine = line.lower()

    flagForECigar = True  # assume true at first step.

    if 'electronic-cigarette' in lowercaseLine:
        return True
    elif 'electronic cigarette' in lowercaseLine:
        return True
    elif 'electronic cig' in lowercaseLine:
        return True
    elif ' e-cig' in lowercaseLine:
        return True
    elif ' ecig' in lowercaseLine:
        return True
    elif ' e cig' in lowercaseLine:
        return True
    elif ' e-cigarette' in lowercaseLine:
        return True
    elif ' ecigarette' in lowercaseLine:
        return True
    elif ' e cigarette' in lowercaseLine:
        return True

    elif 'e-juice' in lowercaseLine:
        return True
    # lots of False positive. grapejuice, creativejuice ...
    elif ' ejuice' in lowercaseLine:
        #         print(line)
        return True
#     elif 'e juice' in lowercaseLine:
#         print(line)
#         return True
    elif 'e-liquid' in lowercaseLine:
        return True
    elif 'eliquid' in lowercaseLine:
        return True
    elif ' e liquid' in lowercaseLine:
        return True
    # Just for thoughtfulness, put it in front of 'vape' incase future use.
    elif 'vaper' in lowercaseLine:
        return True
    elif 'vape' in lowercaseLine:
        return True
    elif 'vaping' in lowercaseLine:
        return True
    elif 'vape-juice' in lowercaseLine:  # Just for thoughtfulness
        return True
    elif 'vape-liquid' in lowercaseLine:  # Just for thoughtfulness
        return True
    elif 'vaporizer' in lowercaseLine:
        return True
    elif 'boxmod' in lowercaseLine:
        return True

    elif 'e-smoke' in lowercaseLine:
        return True
    elif 'esmoke' in lowercaseLine:
        return True

    # Brand
    elif 'juul' in lowercaseLine:
        return True
    elif 'vaporfi' in lowercaseLine:
        return True
    elif 'vype pebble' in lowercaseLine:  # Just for thoughtfulness
        return True
    elif 'v2cigs' in lowercaseLine:  # Just for thoughtfulness
        return True
    elif 'halocigs' in lowercaseLine:
        return True

    #
    elif 'cloud chaser' in lowercaseLine:
        return True
    elif 'cloudchaser' in lowercaseLine:
        return True
    elif 'ciga' in lowercaseLine and 'blu' in lowercaseLine:
        return True
    elif 'cig' in lowercaseLine and 'blu' in lowercaseLine:
        return True
    elif 'e-swisher' in lowercaseLine:
        return True
    elif 'ezsmoker' in lowercaseLine:
        return True

    # It turns out it mainly because of this.
    elif ' fin ' in lowercaseLine:
        # finList.append(line)
        # label_finList.append(row[0])
        return True
    elif ' njoy' in lowercaseLine:
        # njoyList.append(line)
        # label_njoyList.append(row[0])
        return True

    # 0 more
    elif 'smoke assist' in lowercaseLine:
        return True
    elif 'v2 cigs' in lowercaseLine:
        return True
    elif 'markten' in lowercaseLine:
        return True
    elif 'vuse' in lowercaseLine:
        return True
    elif 'tryst' in lowercaseLine:
        return True
    elif 'atomizer' in lowercaseLine:
        return True
    elif 'cartomizer' in lowercaseLine:
        return True
    elif 'v2 cigs' in lowercaseLine:
        return True

#     1 more
    elif 'ehookah' in lowercaseLine:
        return True
    elif 'e-hookah' in lowercaseLine:
        return True
    elif ' e hookah' in lowercaseLine:
        return True
    elif 'green smoke' in lowercaseLine:
        return True
    elif 'south beach smoke' in lowercaseLine:
        return True
    elif 'eversmoke' in lowercaseLine:
        return True
    elif 'joye510' in lowercaseLine:
        return True

    elif 'joye 510' in lowercaseLine:
        return True
    elif 'joyetech' in lowercaseLine:
        return True
    elif 'logicecig' in lowercaseLine:
        return True
    elif 'smartsmoker' in lowercaseLine:
        return True
    else:
        flagForECigar = False

    # only give us 7 more.
    if flagForECigar == False:
        for keyword in ECigar_keywords:
            if keyword in lowercaseLine:
                return True
                # flagForECigar = True
                # break
    return False


#     if 'electronic-cigarette' in lowercaseLine:
#         return True
#     elif 'electronic cigarette' in lowercaseLine:
#         return True
#     elif 'electronic cig' in lowercaseLine:
#         return True
#     elif 'e-cig' in lowercaseLine:
#         return True
#     elif 'ecig' in lowercaseLine:
#         return True
#     elif 'e cig' in lowercaseLine:
#         return True
#     elif 'e-cigarette' in lowercaseLine:
#         return True
#     elif 'ecigarette' in lowercaseLine:
#         return True
#     elif 'e cigarette' in lowercaseLine:
#         return True

#     elif 'e-juice' in lowercaseLine:
#         return True
# #     elif 'ejuice' in lowercaseLine: # lots of False positive. grapejuice, creativejuice ...
# #         print(line)
# #         eCigarList.append(line)
# #     elif 'e juice' in lowercaseLine:
# #         print(line)
# #         eCigarList.append(line)
#     elif 'e-liquid' in lowercaseLine:
#         return True
#     elif 'eliquid' in lowercaseLine:
#         return True
# #     elif 'e liquid' in lowercaseLine: # False positive. the liquid ...
# #         eCigarList.append(line)
#     elif 'vaper' in lowercaseLine: # Just for thoughtfulness, put it in front of 'vape' incase future use.
#         return True
#     elif 'vape' in lowercaseLine:
#         return True
#     elif 'vaping' in lowercaseLine:
#         return True
#     elif 'vape-juice' in lowercaseLine: # Just for thoughtfulness
#         return True
#     elif 'vape-liquid' in lowercaseLine:  # Just for thoughtfulness
#         return True
#     elif 'vaporizer' in lowercaseLine:
#         return True
#     elif 'boxmod' in lowercaseLine:
#         return True


#     elif 'e-smoke' in lowercaseLine:
#         return True
#     elif 'esmoke' in lowercaseLine:
#         return True

#     # Brand
#     elif 'juul' in lowercaseLine:
#         return True
#     elif 'vaporfi' in lowercaseLine:
#         return True
#     elif 'vype pebble' in lowercaseLine: # Just for thoughtfulness
#         return True
#     elif 'v2cigs' in lowercaseLine:  # Just for thoughtfulness
#         return True
#     elif 'halocigs' in lowercaseLine:
#         return True
#     else:
#         return False


def getPlaceName(jsonLine):
    #     print(jsonLine['place']['name'])
    return jsonLine['place']['name']


def checkLocationInLine(line):
    try:
        tweetInJson = json.loads(line)
        tweetPlace = getPlaceName(tweetInJson)
        tweetPlace_lowercase = tweetPlace.lower()
        if ('san francisco' in tweetPlace_lowercase) or (' SF ' in tweetPlace) or ('sfo' in tweetPlace_lowercase):
            return True
    except:
        return False


def checkECigaretteOfEachLineInFile(fileName):

    os.chdir('/scratch/yt1506/juliana/data')
    allECigaretteLine = set()
    allSF = set()
    allECigarette_SF_Line = set()
    with open(fileName, "r") as f:
        everyLines = f.readlines()
        for line in everyLines:
            #             try:
            if checkECigaretteInLine(line):
                allECigaretteLine.add(line)
            # Here we also need to make sure the tweet is posted in San Francisco.
            if checkLocationInLine(line):
                allSF.add(line)

                if checkECigaretteInLine(line):
                    allECigarette_SF_Line.add(line)

    os.chdir('/scratch/yt1506/result/')

    # Write E-Cigarette data to local file
    allECigarette_FileName = './juliana_allECigarette_2019_01_notText.json'
    # allLocation_FileName = './test_allECigarette_2019_01'
    with open(allECigarette_FileName, "a", encoding="utf-8") as f:
        for line in allECigaretteLine:
            f.write(str(line))

    # Write San Francisco data to local file
    # os.chdir('/scratch/yt1506/result/')
    # allSF_FileName = './juliana_allSF_2019_01.json'
    # with open(allSF_FileName, "a", encoding="utf-8") as f:
    #     for line in allSF:
    #         f.write(str(line))

    # Write E-Cigarette that happened in SF data to local file
    allECigarette_SF_FileName = './juliana_SF_allECigarette_2019_01_notText.json'
    # allLocation_FileName = './test_allECigarette_2019_01'
    with open(allECigarette_SF_FileName, "a", encoding="utf-8") as f:
        for line in allECigarette_SF_Line:
            f.write(str(line))


# Iterate the files in the directory you stored the data.
jsonFileDirectoryPath = "/scratch/yt1506/juliana/data"
dirNames = os.listdir(jsonFileDirectoryPath)

os.chdir('/scratch/yt1506/juliana/data')

for dirName in dirNames:
    #     print(dirName)
    files = os.listdir(dirName)
    for file in files:
        #         print(file)
        file = dirName + '/' + file
        if not os.path.isdir(file) and (os.path.splitext(file)[-1] == ".json"):

            checkECigaretteOfEachLineInFile(file)
            print('finish file: ', file)
    os.chdir('/scratch/yt1506/juliana/data')

print('Finished all the files.')


# Count lines of each file above.
print('juliana_allECigarette_2019_01.json: ', len(open(
    '/scratch/yt1506/result/juliana_allECigarette_2019_01_notText.json', 'rU').readlines()))
# print('juliana_allSF_2019_01.json: ', len(
#     open('/scratch/yt1506/result/juliana_allSF_2019_01.json', 'rU').readlines()))
print('juliana_SF_allECigarette_2019_01.json: ', len(open(
    '/scratch/yt1506/result/juliana_SF_allECigarette_2019_01_notText.json', 'rU').readlines()))
