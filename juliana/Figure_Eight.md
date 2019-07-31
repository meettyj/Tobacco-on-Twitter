## First 1000 labeling result
- Total: 961
- ECIG: 546
- NOT-ECIG: 413
- FLAVOR: 81
- NOT-FLAVOR: 465

Among those not-ecig (actually is 431 rows when I import it by python), there are 155 tweets are from flavor keywords and 276 are from e-cig keywords. Among those 276, the problem are listed below:




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

