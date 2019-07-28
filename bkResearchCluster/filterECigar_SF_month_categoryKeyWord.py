import os
# os.chdir('C:/Users/eddie/Desktop/Prof. Rumi Chunara/alcohol')
import json
import pandas as pd

# def writeECigaretteToFile(eCigaretteList):
#     allECigarette_FileName = '/scratch/yt1506/juliana_allECigarette_2019_01.txt'
#     with open(allECigarette_FileName, "a", encoding="utf-8") as f:
#         for line in eCigaretteList:
#             f.write(line+'\n')


def checkECigaretteInLine(line):
    lineInJson = json.loads(line)
    textInLine = lineInJson["text"]
    lowercaseLine = textInLine.lower()

    # line = str(line)
    # lowercaseLine = line.lower()

    # Category keyword
    # synonym_ecig = ['electronic-cigarette', 'electronic cigarette', 'electronic cig', ' e-cig', ' ecig', ' e cig', 'e-cigarette', 'ecigarette', ' e cigarette', 'e-juice', ' ejuice', ' e juice', 'e-liquid', ' eliquid', ' e liquid', 'e-smoke', 'esmoke',
    #                 ' e smoke', 'vape', 'vaper', 'vaping', 'vape-juice', 'vape-liquid', ' vapor', 'vaporizer', 'boxmod', 'cloud chaser', 'cloudchaser', 'smoke assist', 'ehookah', 'e-hookah', ' e hookah', 'stillblowingsmoke', 'still blowing smoke', 'cherry tip cigarillo']
    # brand_ecig = ['juul', 'vaporfi', 'vype pebble', 'v2 cig', 'v2cigs', 'v2 cigs', 'halocigs', ' njoy', 'markten', 'vuse', 'tryst', 'atomizer', 'cartomizer', 'south beach smoke', 'eversmoke', 'joye510', 'joye 510', 'joyetech', 'logicecig', 'smartsmoker', ' mistic', 'smokestiks', '21st century smoke',
    #               'logic black label', ' fin ', ' finiti', 'nicotek', 'cigirex', 'ciga&blu', 'cig&blu', 'logic&cig', 'e-swisher', 'e swisher', 'eswisher', 'ezsmoker', 'ez&cig', 'green smoke', 'cigalectric', 'xhale o2', 'xhaleo2', 'cig2o', 'green smart living', 'greensmartliving', 'krave', 'swisher blk', 'grimmgreen']
    # policy_ecig = ['sb140', 'sb 140', 'sb24', 'sb 24']
    # cessation_ecig = ['notblowingsmoke', 'not blowing smoke',
    #                   'tobaccofreekids', 'notareplacement']

    # Category keyword
    synonym_ecig = ['electronic-cigarette', 'electronic cigarette', 'electronic cig', ' e-cig', ' ecig', ' e cig', 'e-cigarette', 'ecigarette', ' e cigarette', 'e-juice', ' ejuice', ' e juice', 'e-liquid', ' eliquid', ' e liquid', 'e-smoke', 'esmoke', ' e smoke', 'vape', 'vaper', 'vaping', 'vape-juice',
                    'vape-liquid', ' vapor', 'vaporizer', 'boxmod', 'cloud chaser', 'cloudchaser', 'smoke assist', 'ehookah', 'e-hookah', ' e hookah', 'stillblowingsmoke', 'still blowing smoke', 'cherry tip cigarillo', '#e-cig', '#ecig', '#e cigar', '#ejuice', '#e juice', '#eliquid', '#e liquid', '#vapor', '#ehookah', '#e hookah']
    brand_ecig = ['juul', 'vaporfi', 'vype pebble', 'v2 cig', 'v2cigs', 'v2 cigs', 'halocigs', ' njoy', 'markten', 'vuse', 'tryst', 'atomizer', 'cartomizer', 'south beach smoke', 'eversmoke', 'joye510', 'joye 510', 'joyetech', 'logicecig', 'smartsmoker', ' mistic', 'smokestiks', '21st century smoke', 'logic black label',
                  ' fin ', ' finiti', 'nicotek', 'cigirex', 'ciga&blu', 'cig&blu', 'logic&cig', 'e-swisher', 'e swisher', 'eswisher', 'ezsmoker', 'ez&cig', 'green smoke', 'cigalectric', 'xhale o2', 'xhaleo2', 'cig2o', 'green smart living', 'greensmartliving', 'krave', 'swisher blk', 'grimmgreen', '#njoy', '#fin ', '#finiti']
    policy_ecig = ['sb140', 'sb 140', 'sb24', 'sb 24']
    cessation_ecig = ['notblowingsmoke', 'not blowing smoke',
                      'tobaccofreekids', 'notareplacement']

    # test for synonym
    for keyword in synonym_ecig:
        #         print(keyword)
        if '&' not in keyword and keyword in lowercaseLine:
            return True
        elif '&' in keyword:
            k1, k2 = keyword.split('&')
            if k1 in lowercaseLine and k2 in lowercaseLine:
                return True

            # synonym_ecig_list.append(line)
            # flagHit = True
            # break

    # test for brand
    for keyword in brand_ecig:
        if keyword in lowercaseLine:
            return True
            # brand_ecig_list.append(line)
            # flagHit = True
            # break

    # test for policy
    for keyword in policy_ecig:
        if keyword in lowercaseLine:
            return True
            # policy_ecig_list.append(line)
            # flagHit = True
            # break

    # test for cessation
    for keyword in cessation_ecig:
        if keyword in lowercaseLine:
            return True
            # cessation_ecig_list.append(line)
            # flagHit = True
            # break

    return False


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
    allECigarette_FileName = './juliana_allECigarette_2019_01_categoryKeyWord.json'
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
    allECigarette_SF_FileName = './juliana_SF_allECigarette_2019_01_categoryKeyWord.json'
    # allLocation_FileName = './test_allECigarette_2019_01'
    with open(allECigarette_SF_FileName, "a", encoding="utf-8") as f:
        for line in allECigarette_SF_Line:
            f.write(str(line))


# Iterate the files in the directory you stored the data.
jsonFileDirectoryPath = "/mnt/volume/juliana/data"
dirNames = os.listdir(jsonFileDirectoryPath)

os.chdir('/mnt/volume/juliana/data')

for dirName in dirNames:
    #     print(dirName)
    files = os.listdir(dirName)
    for file in files:
        #         print(file)
        file = dirName + '/' + file
        if not os.path.isdir(file) and (os.path.splitext(file)[-1] == ".json"):

            checkECigaretteOfEachLineInFile(file)
            print('finish file: ', file)
    os.chdir('/mnt/volume/juliana/data')

print('Finished all the files.')


# Count lines of each file above.
print('juliana_allECigarette_2019_01.json: ', len(open(
    '/scratch/yt1506/result/juliana_allECigarette_2019_01_categoryKeyWord.json', 'rU').readlines()))
# print('juliana_allSF_2019_01.json: ', len(
#     open('/scratch/yt1506/result/juliana_allSF_2019_01.json', 'rU').readlines()))
print('juliana_SF_allECigarette_2019_01.json: ', len(open(
    '/scratch/yt1506/result/juliana_SF_allECigarette_2019_01_categoryKeyWord.json', 'rU').readlines()))
