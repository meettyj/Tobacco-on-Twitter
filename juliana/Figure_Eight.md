## First 1000 labeling result
- Total: 961
- ECIG: 546
- NOT-ECIG: 413
- FLAVOR: 81
- NOT-FLAVOR: 465

Among those not-ecig (actually is 431 rows when I import it by python), there are 155 tweets are from flavor keywords and 276 are from e-cig keywords. Among those 276, the problem are listed below:


- word 'krave' appeared many times.
- Some of them may not familiar with the synonym/brand of e-cig (vape, juul, ejuice)
- We only use 2 labelers per question. Most of the false positive got 50% confidence.

However, some of them are necessary:
- vape in name.
- vapor


## TODO in instruction
- synonym/brand of e-cig
- if you see any keyword in hashtag, then we assume this text is e-cig relevant.
- mention vaporub, vaporwave


## TODO for the data
- Remove the link in data.
- remove krave, kryst
- space before e swisher



## Note

- Overview:

Further, if Tweet is labelled as "E-Cigarette relevant", determine if it flavorrelated or not. A Tweet is flavor relevant if it is mentioning any flavor in the E-Cigarette (e.g. XYZ...


- Step:

If the Tweet is labelled "E-Cigarette relevant", determine if the Tweet contains anything about the flavor or not.

- question:
Is this posting relevant to flavor in E-Cigarette?

- The Tweets can be classified as E-Cigarette relevant if:

Directly mentioning anything about E-Cigarette.
Indicating the state of using E-Cigarette (wanting, doing, finished) or any feeling about E-Cigarette.
Including any E-Cigarette brand 
Talking about any policy that related to E-Cigarette.
Including any device, pods, accessories of E-Cigarette.

- Note:
The last one will also be labelled asflavor relevant.

