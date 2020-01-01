# 1. Conclusion
- I used Empath and LIWC (2015) to analyze the topics in reddit and ecig tweets in three months (proposal, approval, enforcement).
- This document shows the intersection (same topics) in most common N topics (topN) between reddit and ecig tweets.
- You can find more specific topics information for reddit and ecig tweets individually in [topic_analyse_reddit_comments.ipynb](https://github.com/meettyj/Alcohol-on-Twitter/blob/master/reddit/topic_analyse_reddit_comments.ipynb) 
and [topic_analyse_ecig_tweets.ipynb](https://github.com/meettyj/Alcohol-on-Twitter/blob/master/reddit/topic_analyse_ecig_tweets.ipynb)
- Topics extracted by Empath is kind of simple, while topics extracted by LIWC contains part of speech (e.g. verb, prepositions).
For LIWC, I was thinking maybe we should remove the part of speech, but same, I didn't see a lot of meaningful topics.
- Explaination: in ('negative_emotion', 232.0), 'negative_emotion' is the topic, 232.0 is the value that this topic has appeared in reddit data and ecig tweets data for 232 times.

# 2. Empath
## Proposal
- topN:  10
  - intersection:  [('negative_emotion', 232.0), ('business', 199.0), ('speaking', 195.0)]
- topN:  20
  - intersection:  [('negative_emotion', 232.0), ('business', 199.0), ('speaking', 195.0), ('positive_emotion', 117.0), ('giving', 101.0), ('work', 101.0), ('violence', 96.0)]
- topN:  30
  - intersection:  [('negative_emotion', 232.0), ('communication', 220.0), ('business', 199.0), ('speaking', 195.0), ('economics', 174.0), ('positive_emotion', 117.0), ('giving', 101.0), ('work', 101.0), ('violence', 96.0), ('social_media', 93.0), ('messaging', 93.0), ('writing', 89.0), ('optimism', 77.0)]
- topN:  40
  - intersection:  [('negative_emotion', 232.0), ('smell', 222.0), ('communication', 220.0), ('business', 199.0), ('speaking', 195.0), ('economics', 174.0), ('money', 120.0), ('positive_emotion', 117.0), ('giving', 101.0), ('work', 101.0), ('violence', 96.0), ('social_media', 93.0), ('messaging', 93.0), ('writing', 89.0), ('optimism', 77.0), ('traveling', 77.0), ('gain', 72.0)]

## Approval
- topN:  10
  - intersection:  [('negative_emotion', 204.0), ('shopping', 126.0), ('eating', 118.0), ('money', 102.0)]
- topN:  20
  - intersection:  [('negative_emotion', 204.0), ('business', 144.0), ('shopping', 126.0), ('eating', 118.0), ('money', 102.0), ('positive_emotion', 95.0)]
- topN:  30
  - intersection:  [('negative_emotion', 204.0), ('business', 144.0), ('speaking', 135.0), ('shopping', 126.0), ('eating', 118.0), ('money', 102.0), ('positive_emotion', 95.0), ('real_estate', 94.0), ('internet', 66.0), ('children', 62.0)]
- topN:  40
  - intersection:  [('negative_emotion', 204.0), ('communication', 151.0), ('business', 144.0), ('economics', 136.0), ('speaking', 135.0), ('shopping', 126.0), ('eating', 118.0), ('money', 102.0), ('positive_emotion', 95.0), ('real_estate', 94.0), ('violence', 72.0), ('internet', 66.0), ('traveling', 63.0), ('children', 62.0), ('optimism', 57.0), ('work', 57.0), ('computer', 55.0)]
  
## Enforcement
- topN:  10
  - intersection:  [('negative_emotion', 58.0), ('communication', 38.0), ('business', 37.0)]
- topN:  20
  - intersection:  [('negative_emotion', 58.0), ('communication', 38.0), ('money', 37.0), ('speaking', 37.0), ('business', 37.0), ('economics', 34.0), ('positive_emotion', 25.0)]
- topN:  30
  - intersection:  [('negative_emotion', 58.0), ('communication', 38.0), ('money', 37.0), ('speaking', 37.0), ('business', 37.0), ('economics', 34.0), ('shopping', 30.0), ('positive_emotion', 25.0), ('giving', 24.0), ('trust', 20.0), ('internet', 19.0), ('reading', 19.0), ('family', 19.0)]
- topN:  40
  - intersection:  [('negative_emotion', 58.0), ('communication', 38.0), ('money', 37.0), ('speaking', 37.0), ('business', 37.0), ('economics', 34.0), ('shopping', 30.0), ('children', 28.0), ('positive_emotion', 25.0), ('giving', 24.0), ('alcohol', 20.0), ('trust', 20.0), ('home', 20.0), ('eating', 20.0), ('school', 19.0), ('internet', 19.0), ('reading', 19.0), ('family', 19.0), ('writing', 19.0), ('pain', 17.0)]

# 3. LIWC
## Proposal
- topN:  20
  - intersection:  [('function (Function Words)', 13015), ('verb (Verbs)', 3801), ('prep (Prepositions)', 3712), ('cogproc (Cognitive Processes)', 3517), ('relativ (Relativity)', 3172), ('pronoun (Pronouns)', 2992), ('focuspresent (Present Focus)', 2509), ('social (Social)', 2250), ('auxverb (Auxiliary Verbs)', 1925), ('article (Articles)', 1740), ('ipron (Impersonal Pronouns)', 1682), ('space (Space)', 1650), ('drives (Drives)', 1648), ('conj (Conjunctions)', 1612), ('ppron (Personal Pronouns)', 1310), ('adj (Adjectives)', 1277), ('time (Time)', 1118)]

- topN:  40
  - intersection:  [('function (Function Words)', 13015), ('verb (Verbs)', 3801), ('prep (Prepositions)', 3712), ('cogproc (Cognitive Processes)', 3517), ('relativ (Relativity)', 3172), ('pronoun (Pronouns)', 2992), ('focuspresent (Present Focus)', 2509), ('social (Social)', 2250), ('auxverb (Auxiliary Verbs)', 1925), ('article (Articles)', 1740), ('ipron (Impersonal Pronouns)', 1682), ('space (Space)', 1650), ('drives (Drives)', 1648), ('conj (Conjunctions)', 1612), ('adverb (Adverbs)', 1373), ('affect (Affect)', 1343), ('ppron (Personal Pronouns)', 1310), ('adj (Adjectives)', 1277), ('time (Time)', 1118), ('bio (Biological Processes)', 986), ('differ (Differentiation)', 971), ('tentat (Tentative)', 886), ('percept (Perceptual Processes)', 871), ('focuspast (Past Focus)', 830), ('work (Work)', 796), ('compare (Comparisons)', 782), ('posemo (Positive Emotions)', 758), ('quant (Quantifiers)', 654), ('ingest (Ingest)', 612), ('you (You)', 457), ('discrep (Discrepancies)', 422), ('interrog (Interrogatives)', 419), ('motion (Motion)', 397)]

- topN:  60
  - intersection:  [('function (Function Words)', 13015), ('verb (Verbs)', 3801), ('prep (Prepositions)', 3712), ('cogproc (Cognitive Processes)', 3517), ('relativ (Relativity)', 3172), ('pronoun (Pronouns)', 2992), ('focuspresent (Present Focus)', 2509), ('social (Social)', 2250), ('auxverb (Auxiliary Verbs)', 1925), ('article (Articles)', 1740), ('ipron (Impersonal Pronouns)', 1682), ('space (Space)', 1650), ('drives (Drives)', 1648), ('conj (Conjunctions)', 1612), ('adverb (Adverbs)', 1373), ('affect (Affect)', 1343), ('ppron (Personal Pronouns)', 1310), ('adj (Adjectives)', 1277), ('time (Time)', 1118), ('bio (Biological Processes)', 986), ('differ (Differentiation)', 971), ('tentat (Tentative)', 886), ('percept (Perceptual Processes)', 871), ('focuspast (Past Focus)', 830), ('work (Work)', 796), ('compare (Comparisons)', 782), ('posemo (Positive Emotions)', 758), ('cause (Causal)', 683), ('quant (Quantifiers)', 654), ('ingest (Ingest)', 612), ('insight (Insight)', 601), ('power (Power)', 582), ('negemo (Negative Emotions)', 568), ('certain (Certainty)', 478), ('you (You)', 457), ('money (Money)', 440), ('discrep (Discrepancies)', 422), ('interrog (Interrogatives)', 419), ('motion (Motion)', 397), ('they (They)', 366), ('achieve (Achievement)', 364), ('negate (Negations)', 357), ('informal (Informal Language)', 353), ('affiliation (Affiliation)', 337), ('reward (Reward)', 335), ('leisure (Leisure)', 309), ('focusfuture (Future Focus)', 283), ('i (I)', 272), ('anger (Anger)', 262), ('see (See)', 219), ('number (Numbers)', 174), ('body (Body)', 170), ('hear (Hear)', 158), ('we (We)', 157), ('feel (Feel)', 95)]
  
## Approval
- topN:  20
  - intersection:  [('function (Function Words)', 10303), ('verb (Verbs)', 3008), ('prep (Prepositions)', 2954), ('relativ (Relativity)', 2671), ('cogproc (Cognitive Processes)', 2634), ('pronoun (Pronouns)', 2224), ('focuspresent (Present Focus)', 1965), ('social (Social)', 1645), ('space (Space)', 1584), ('auxverb (Auxiliary Verbs)', 1537), ('drives (Drives)', 1470), ('article (Articles)', 1462), ('conj (Conjunctions)', 1249), ('ipron (Impersonal Pronouns)', 1241), ('affect (Affect)', 1129), ('adverb (Adverbs)', 1083), ('adj (Adjectives)', 1035), ('ppron (Personal Pronouns)', 981), ('time (Time)', 751)]

- topN:  40
  - intersection:  [('function (Function Words)', 10303), ('verb (Verbs)', 3008), ('prep (Prepositions)', 2954), ('relativ (Relativity)', 2671), ('cogproc (Cognitive Processes)', 2634), ('pronoun (Pronouns)', 2224), ('focuspresent (Present Focus)', 1965), ('social (Social)', 1645), ('space (Space)', 1584), ('auxverb (Auxiliary Verbs)', 1537), ('drives (Drives)', 1470), ('article (Articles)', 1462), ('conj (Conjunctions)', 1249), ('ipron (Impersonal Pronouns)', 1241), ('affect (Affect)', 1129), ('adverb (Adverbs)', 1083), ('adj (Adjectives)', 1035), ('ppron (Personal Pronouns)', 981), ('time (Time)', 751), ('differ (Differentiation)', 723), ('focuspast (Past Focus)', 682), ('power (Power)', 676), ('tentat (Tentative)', 615), ('work (Work)', 608), ('posemo (Positive Emotions)', 601), ('percept (Perceptual Processes)', 596), ('compare (Comparisons)', 584), ('bio (Biological Processes)', 556), ('quant (Quantifiers)', 523), ('negemo (Negative Emotions)', 516), ('cause (Causal)', 474), ('you (You)', 338), ('motion (Motion)', 331), ('informal (Informal Language)', 313), ('ingest (Ingest)', 298)]

- topN:  60
  - intersection:  [('function (Function Words)', 10303), ('verb (Verbs)', 3008), ('prep (Prepositions)', 2954), ('relativ (Relativity)', 2671), ('cogproc (Cognitive Processes)', 2634), ('pronoun (Pronouns)', 2224), ('focuspresent (Present Focus)', 1965), ('social (Social)', 1645), ('space (Space)', 1584), ('auxverb (Auxiliary Verbs)', 1537), ('drives (Drives)', 1470), ('article (Articles)', 1462), ('conj (Conjunctions)', 1249), ('ipron (Impersonal Pronouns)', 1241), ('affect (Affect)', 1129), ('adverb (Adverbs)', 1083), ('adj (Adjectives)', 1035), ('ppron (Personal Pronouns)', 981), ('time (Time)', 751), ('differ (Differentiation)', 723), ('focuspast (Past Focus)', 682), ('power (Power)', 676), ('tentat (Tentative)', 615), ('work (Work)', 608), ('posemo (Positive Emotions)', 601), ('percept (Perceptual Processes)', 596), ('compare (Comparisons)', 584), ('bio (Biological Processes)', 556), ('quant (Quantifiers)', 523), ('negemo (Negative Emotions)', 516), ('cause (Causal)', 474), ('insight (Insight)', 462), ('money (Money)', 364), ('certain (Certainty)', 364), ('you (You)', 338), ('motion (Motion)', 331), ('discrep (Discrepancies)', 321), ('informal (Informal Language)', 313), ('ingest (Ingest)', 298), ('achieve (Achievement)', 285), ('interrog (Interrogatives)', 280), ('negate (Negations)', 275), ('anger (Anger)', 256), ('affiliation (Affiliation)', 249), ('reward (Reward)', 242), ('leisure (Leisure)', 233), ('focusfuture (Future Focus)', 208), ('health (Health)', 172), ('risk (Risk)', 166), ('i (I)', 162), ('number (Numbers)', 152), ('swear (Swear)', 141), ('see (See)', 140), ('hear (Hear)', 133), ('body (Body)', 104), ('feel (Feel)', 98), ('netspeak (Netspeak)', 89), ('male (Male)', 75)]
  
## Enforcement
- topN:  20
  - intersection:  [('function (Function Words)', 2494), ('verb (Verbs)', 791), ('prep (Prepositions)', 697), ('cogproc (Cognitive Processes)', 662), ('relativ (Relativity)', 634), ('pronoun (Pronouns)', 538), ('focuspresent (Present Focus)', 532), ('auxverb (Auxiliary Verbs)', 420), ('social (Social)', 401), ('drives (Drives)', 382), ('article (Articles)', 339), ('space (Space)', 329), ('conj (Conjunctions)', 298), ('ipron (Impersonal Pronouns)', 272), ('ppron (Personal Pronouns)', 266), ('affect (Affect)', 261), ('adj (Adjectives)', 235), ('time (Time)', 234)]

- topN:  40
  - intersection:  [('function (Function Words)', 2494), ('verb (Verbs)', 791), ('prep (Prepositions)', 697), ('cogproc (Cognitive Processes)', 662), ('relativ (Relativity)', 634), ('pronoun (Pronouns)', 538), ('focuspresent (Present Focus)', 532), ('auxverb (Auxiliary Verbs)', 420), ('social (Social)', 401), ('drives (Drives)', 382), ('article (Articles)', 339), ('space (Space)', 329), ('conj (Conjunctions)', 298), ('ipron (Impersonal Pronouns)', 272), ('ppron (Personal Pronouns)', 266), ('affect (Affect)', 261), ('adverb (Adverbs)', 257), ('adj (Adjectives)', 235), ('time (Time)', 234), ('bio (Biological Processes)', 204), ('differ (Differentiation)', 184), ('work (Work)', 174), ('focuspast (Past Focus)', 166), ('tentat (Tentative)', 148), ('cause (Causal)', 133), ('posemo (Positive Emotions)', 131), ('negemo (Negative Emotions)', 125), ('quant (Quantifiers)', 122), ('compare (Comparisons)', 120), ('insight (Insight)', 116), ('ingest (Ingest)', 109), ('percept (Perceptual Processes)', 107), ('discrep (Discrepancies)', 86), ('motion (Motion)', 86)]

- topN:  60
  - intersection:  [('function (Function Words)', 2494), ('verb (Verbs)', 791), ('prep (Prepositions)', 697), ('cogproc (Cognitive Processes)', 662), ('relativ (Relativity)', 634), ('pronoun (Pronouns)', 538), ('focuspresent (Present Focus)', 532), ('auxverb (Auxiliary Verbs)', 420), ('social (Social)', 401), ('drives (Drives)', 382), ('article (Articles)', 339), ('space (Space)', 329), ('conj (Conjunctions)', 298), ('ipron (Impersonal Pronouns)', 272), ('ppron (Personal Pronouns)', 266), ('affect (Affect)', 261), ('adverb (Adverbs)', 257), ('adj (Adjectives)', 235), ('time (Time)', 234), ('bio (Biological Processes)', 204), ('differ (Differentiation)', 184), ('work (Work)', 174), ('focuspast (Past Focus)', 166), ('tentat (Tentative)', 148), ('power (Power)', 143), ('cause (Causal)', 133), ('posemo (Positive Emotions)', 131), ('negemo (Negative Emotions)', 125), ('quant (Quantifiers)', 122), ('compare (Comparisons)', 120), ('insight (Insight)', 116), ('ingest (Ingest)', 109), ('i (I)', 109), ('money (Money)', 108), ('percept (Perceptual Processes)', 107), ('leisure (Leisure)', 100), ('certain (Certainty)', 99), ('health (Health)', 93), ('informal (Informal Language)', 87), ('discrep (Discrepancies)', 86), ('motion (Motion)', 86), ('achieve (Achievement)', 83), ('affiliation (Affiliation)', 77), ('reward (Reward)', 72), ('negate (Negations)', 69), ('focusfuture (Future Focus)', 68), ('they (They)', 65), ('interrog (Interrogatives)', 61), ('anger (Anger)', 48), ('you (You)', 45), ('body (Body)', 39), ('netspeak (Netspeak)', 39), ('see (See)', 33), ('number (Numbers)', 32), ('feel (Feel)', 27), ('hear (Hear)', 26), ('sad (Sad)', 25)]
  






