import os
# os.chdir('C:/Users/eddie/Desktop/Prof. Rumi Chunara/alcohol')

import pandas as pd

# load the file.
with open('/scratch/yt1506/result/juliana_allSF_2019_01.json', 'r') as f:
    data = f.readlines()

# remove the trailing "\n" from each line
data = map(lambda x: x.rstrip(), data)

# each element of 'data' is an individual JSON object. I want to convert it into an *array* of JSON objects
# which, in and of itself, is one large JSON object basically... add square brackets to the beginning
# and end, and have all the individual business JSON objects separated by a comma.
data_json_str = "[" + ','.join(data) + "]"

df = pd.read_json(data_json_str)


allText = df.text
print(type(allText))
print(len(allText))


smokeList = []
# Include those start with 'smok' but not 'smoke' (e.g. smoking, smoky).
smokList = []
cigaList = []  # Result for cigar and ciga is same

marijuanaList = []
weedList = []
cocaineList = []
pillList = []
drugList = []

for line in allText:
    lowercaseLine = line.lower()
    if 'smoke' in lowercaseLine:
        #         print(line)
        smokeList.append(line)
    elif 'smok' in lowercaseLine:
        smokList.append(line)
    if 'ciga' in lowercaseLine:
        cigaList.append(line)

    if 'marijuana' in lowercaseLine:
        marijuanaList.append(line)
    if 'weed' in lowercaseLine:
        weedList.append(line)
    if 'cocaine' in lowercaseLine:
        cocaineList.append(line)
    if 'pill' in lowercaseLine and 'spill' not in lowercaseLine and 'pillow' not in lowercaseLine:
        pillList.append(line)
    if 'drug' in lowercaseLine:
        drugList.append(line)


# Output the result.
print('smokeList: %d items' % (len(smokeList)))
print('smokList: %d items' % (len(smokList)))
print('cigaList: %d items' % (len(cigaList)))

print()
print('marijuanaList: %d items' % (len(marijuanaList)))
print('weedList: %d items' % (len(weedList)))
print('cocaineList: %d items' % (len(cocaineList)))
print('pillList: %d items' % (len(pillList)))
print('drugList: %d items' % (len(drugList)))

# Take a look at the smokList and cigaList.
# print(fds)
print('Here is the smokList:')
for i in smokList:
    print(i)

print('Here is the cigaList:')
for i in cigaList:
    print(i)

allList = []
allList.extend(smokeList)
allList.extend(smokList)
allList.extend(cigaList)
allList.extend(smokeList)
allList.extend(marijuanaList)
allList.extend(weedList)
allList.extend(cocaineList)
allList.extend(pillList)
allList.extend(drugList)

# Remove duplicated item in allList
allList = list(set(allList))

print('allList: %d items' % (len(allList)))
percentage = len(allList)/len(allText)*100
print('The percentage of drug/smoke related tweets in entire %d tweets is %f%%' %
      (len(allText), percentage))
