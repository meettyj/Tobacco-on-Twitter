I randomly choose two month (January 2018, and June 2018) to analyze the distribution of ecig keywords results in different subreddits.

## Conclusion
- The reddits collection can be devided into 2 parts:
  - search the same keywords without specifying subreddit.
  - crawl all submissions under specific subreddit.

## Keywords
```
keywords = ['vape', 'e liquid', 'e juice', 'ejuice', 'electronic cigarette', 'eliquid', 'e cig', 'ecig', 'e hookah', 'electronic cig', 'ehookah']
```

## 2018.1.1 - 2018.1.31

| Search query | # of submissions in all subreddits  | # of submissions in specific subreddit  |
| ------------- | ----------------------- | ----------------------- |
| vape | 2952 | ('vaporents', 417), ('Vaping', 339), ('electronic_cigarette', 244), ('trees', 167), ('CBD', 85), ('ecig_vendors', 76), ('VapeBargainsUK', 64), ('ecigclassifieds', 54), ('h3h3productions', 48), ('VapePorn', 40), ('Vaping101', 40), ('Vaping_Deals', 30), ('EntExchange', 29), ('CanadianMOMs', 26), ('AskReddit', 24), ('Waxpen', 23), ('vape_deals', 23), ('funny', 22), ('Canadian_ecigarette', 19), ('Vape_Porn', 19) |
| e liquid | 299 | ('VapeBargainsUK', 41), ('ecig_vendors', 37), ('electronic_cigarette', 29), ('Vaping', 25), ('vape_deals', 19) |
| e juice | 254 | ('Vaping', 32), ('electronic_cigarette', 32), ('Vaping_Deals', 21), ('vape_deals', 18), ('ecig_vendors', 13) |
| ejuice | 164 | ('electronic_cigarette', 41), ('Vaping', 13), ('ecigclassifieds', 13), ('VapeBargainsUK', 9), ('ejuice', 8) |
| electronic cigarette | 118 | ('Vaping', 73), ('vape101', 15), ('VapeBargainsUK', 2), ('eCigarette', 2), ('business', 2)|
| eliquid | 71 | ('electronic_cigarette', 12), ('Vaping', 6), ('ecig_vendors', 5), ('CBD', 4), ('vape_deals', 3) |
| e cig | 71 | ('electronic_cigarette', 15), ('VapeBargainsUK', 4), ('trees', 2), ('vaporents', 2), ('stopsmoking', 2) |
| ecig | 36 | ('electronic_cigarette', 10), ('VapeBargainsUK', 5), ('Vaping', 3), ('DMT', 3), ('CouponProCanada', 2) |
| e hookah | 2 | ('hookah', 2) |
| electronic cig | 0 | None |
| ehookah | 0 | None |


## 2018.6.1 - 2018.6.30

| Search query | # of submissions in all subreddits  | # of submissions in specific subreddit  |
| ------------- | ----------------------- | ----------------------- |
| vape | 2837 | ('Vaping', 418), ('vaporents', 245), ('electronic_cigarette', 181), ('trees', 134), ('CBD', 85), ('ecig_vendors', 83), ('VapePorn', 76), ('ecigclassifieds', 64), ('Vaping101', 57), ('Ice_Poseidon', 52), ('h3h3productions', 38), ('oilpen', 34), ('weed', 29), ('EntExchange', 26), ('DMT', 26), ('teenagersnew', 25), ('Canadian_ecigarette', 22), ('Waxpen', 21), ('juul', 19), ('AskReddit', 19), ('333', 17), ('Drugs', 15) |
| e liquid | 257 | ('ecig_vendors', 53), ('VapeBargainsUK', 31), ('electronic_cigarette', 16), ('Vaping', 15), ('CBD', 9) |
| e juice | 216 | ('electronic_cigarette', 34), ('Vaping', 24), ('ecig_vendors', 19), ('ejuice', 13), ('CBD', 8) |
| ejuice | 140 | ('electronic_cigarette', 20), ('Vaping', 14), ('ecig_vendors', 14), ('BestOfVapeDeals', 13), ('vape_deals', 12) |
| electronic cigarette | 24 | ('Health', 6), ('electronic_cigarette', 4), ('eCigarette', 2), ('VAP', 2), ('u_soulblu1', 1)|
| eliquid | 60 | ('ejuice_reviews', 12), ('Vaping', 9), ('electronic_cigarette', 7), ('VapeBargainsUK', 5), ('ecig_vendors', 3) |
| e cig | 110 | ('electronic_cigarette', 25), ('VapeBargainsUK', 7), ('NBCauto', 7), ('AutoNewspaper', 7), ('ecigclassifieds', 5) |
| ecig | 27 | ('electronic_cigarette', 11), ('bonnaroo', 2), ('Vaping', 2), ('Stims', 1), ('VapeBargainsUK', 1) |
| e hookah | 3 | ('electronic_cigarette', 2), ('sanfrancisco', 1) |
| electronic cig | 1 | ('vaporents', 1)] |
| ehookah | 0 | None |


## API Explanation
- Words in the search query will not appear concatenated in the results.
  - Search '**electronic cigarettes**': results contain 'I smoke regular **cigarettes** and **electronic** ones'. However, most results contains 'electronic cigarettes' instead of each word separately. This depends on query.
  - This feature can be applied to search flavored ecig keywords (e.g. smoke + blueberry). 
- The hyphen(-) is not working in keywords. API will treat them as space and search each word individually.
- Each word in the search query should appear individually without being part of other words.
  - Search '**e juice**': results will contain 'we love **e juice**', but **will not** contain 'we lov**e juice**'.

## Problems
- **Too many requests limitation (Response 429)**. It seems we cannot send too many request in a short time, but we can solve this by separate the requests in different time period.


