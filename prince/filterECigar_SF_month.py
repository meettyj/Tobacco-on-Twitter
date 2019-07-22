import os
# os.chdir('C:/Users/eddie/Desktop/Prof. Rumi Chunara/alcohol')
import json
import pandas as pd

def writeECigaretteToFile(eCigaretteList):
    allECigarette_FileName = '/scratch/yt1506/juliana_allECigarette_2019_01.txt'
    with open(allECigarette_FileName, "a", encoding="utf-8") as f:
        for line in eCigaretteList:
            f.write(line+'\n')


def checkECigaretteInLine(line):
#     print(type(line))
    line = str(line)
    lowercaseLine = line.lower()
    if 'electronic-cigarette' in lowercaseLine:
        return True
    elif 'electronic cigarette' in lowercaseLine:
        return True
    elif 'electronic cig' in lowercaseLine:
        return True
    elif 'e-cig' in lowercaseLine:
        return True
    elif 'ecig' in lowercaseLine:
        return True
    elif 'e cig' in lowercaseLine:
        return True
    elif 'e-cigarette' in lowercaseLine:
        return True
    elif 'ecigarette' in lowercaseLine:
        return True
    elif 'e cigarette' in lowercaseLine:
        return True
    
    elif 'e-juice' in lowercaseLine:
        return True
#     elif 'ejuice' in lowercaseLine: # lots of False positive. grapejuice, creativejuice ...
#         print(line)
#         eCigarList.append(line)
#     elif 'e juice' in lowercaseLine:
#         print(line)
#         eCigarList.append(line)
    elif 'e-liquid' in lowercaseLine:
        return True
    elif 'eliquid' in lowercaseLine:
        return True
#     elif 'e liquid' in lowercaseLine: # False positive. the liquid ...
#         eCigarList.append(line)
    elif 'vaper' in lowercaseLine: # Just for thoughtfulness, put it in front of 'vape' incase future use.
        return True
    elif 'vape' in lowercaseLine: 
        return True
    elif 'vaping' in lowercaseLine:
        return True
    elif 'vape-juice' in lowercaseLine: # Just for thoughtfulness
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
    elif 'vype pebble' in lowercaseLine: # Just for thoughtfulness
        return True
    elif 'v2cigs' in lowercaseLine:  # Just for thoughtfulness
        return True
    elif 'halocigs' in lowercaseLine:
        return True
    else:
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
    with open(fileName, "r") as f:
        everyLines = f.readlines()
        for line in everyLines:
#             try:
            # Here we also need to make sure the tweet is posted in San Francisco.
            if checkLocationInLine(line):
                if checkECigaretteInLine(line):
                    # print(line)
                    allECigaretteLine.add(line)
#             except:
#                 continue
#     print(allECigaretteLine)
    
    
    # Write to local file
    os.chdir('/scratch/yt1506/result/')
    allECigarette_FileName = './juliana_allECigarette_2019_01'
    # allLocation_FileName = './test_allECigarette_2019_01'
    with open(allECigarette_FileName, "a", encoding="utf-8") as f:
        for line in allECigaretteLine:
            f.write(str(line))



# Iterate the files in the directory you stored the data.
jsonFileDirectoryPath = "/scratch/yt1506/juliana/data"
dirNames= os.listdir(jsonFileDirectoryPath)

os.chdir('/scratch/yt1506/juliana/data')

for dirName in dirNames:
#     print(dirName)
    files= os.listdir(dirName)
    for file in files:
#         print(file)
        file = dirName + '/' +file
        if not os.path.isdir(file) and (os.path.splitext(file)[-1] == ".json"):
            
            checkECigaretteOfEachLineInFile(file)
            print('finish file: ', file)
    os.chdir('/scratch/yt1506/juliana/data')

print('Finished all the files.')




