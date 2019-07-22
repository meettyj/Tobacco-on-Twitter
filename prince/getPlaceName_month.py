import os
# os.chdir('C:/Users/eddie/Desktop/Prof. Rumi Chunara/alcohol')
import json
import pandas as pd

def getPlaceName(jsonLine):
    return jsonLine['place']['name']

# return a set of location
def returnLocationOfEachLineInFile(fileName, allTweetPlace):
#     allTweetPlaceInFile = set()
    with open(fileName, "rb") as f:
        everyLines = f.readlines()
        for line in everyLines:
            try:
                tweetInJson = json.loads(line)
                tweetPlace = getPlaceName(tweetInJson)
#                 print(tweetPlace)
#                 allTweetPlaceInFile.add(tweetPlace)
                allTweetPlace.add(tweetPlace)
            except:
                continue
        return allTweetPlace


allTweetPlace = set()


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
            
            print('finish file: ', file)
            allTweetPlace = returnLocationOfEachLineInFile(file, allTweetPlace)
#             print(allTweetPlace)
print('How many different place name we got here: ', len(allTweetPlace))


# Write to some file in disk
os.chdir('/scratch/yt1506/result/')
allLocation_FileName = 'juliana_allLocation_2019_01.txt'
with open(allLocation_FileName, "w", encoding="utf-8") as f:
    for place in allTweetPlace:
        f.write(place+'\n')
# for i in allTweetPlace:
#     print(i)