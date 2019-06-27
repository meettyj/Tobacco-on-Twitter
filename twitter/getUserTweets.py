import tweepy
import csv
from __private import CONSUMER_API_KEY
from __private import CONSUMER_API_KEY_SECRET
from __private import ACCESS_TOKEN
from __private import ACCESS_TOKEN_SECRET


def get_all_tweets(user_id):
    auth = tweepy.OAuthHandler(CONSUMER_API_KEY, CONSUMER_API_KEY_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)

    alltweets = []

    new_tweets = api.user_timeline(user_id=user_id, count=200)
    # save most recent tweets
    alltweets.extend(new_tweets)
    # save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1

    # keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
        print("getting tweets before %s" % (oldest))
        # all subsequent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(user_id=user_id, count=200, max_id=oldest)
        # save most recent tweets
        alltweets.extend(new_tweets)
        # update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1

        print("...%s tweets downloaded so far" % (len(alltweets)))

    # transform the tweepy tweets into a 2D array in order to write to csv
    outtweets = [(tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")) for tweet in alltweets]
    print('length of outtweets', len(outtweets))

    # write the csv
    with open('../result/%s_tweets.csv' % user_id, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["tweet_id", "created_at", "text"])
        writer.writerows(outtweets)
    pass


if __name__ == '__main__':
    # Read ID from file.
    # with open('e:/file/userID.csv', 'rb') as f:
    #     ID = csv.reader(f)
    #     for row in ID:

    # When the program encounters error, it will ignore and continue crawl following user ID
    userID = "133158564"
    try:
        get_all_tweets(userID)
    except tweepy.TweepError:
        print('Failed to run the command on that user, Skipping...')
    except IndexError:
        print('List index out of range, Skipping...')
        # continue


