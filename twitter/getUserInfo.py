import tweepy
import json
from __private import CONSUMER_API_KEY
from __private import CONSUMER_API_KEY_SECRET
from __private import ACCESS_TOKEN
from __private import ACCESS_TOKEN_SECRET


def get_user_info(user_id):
    auth = tweepy.OAuthHandler(CONSUMER_API_KEY, CONSUMER_API_KEY_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)

    # Only get the data in json format.
    userInfo = api.get_user(user_id=user_id)._json
    # print(userInfo)

    with open('../result/%s_userInfo.json' % user_id, 'w') as f:
        json.dump(userInfo, f)
        # f.write(userInfo)


if __name__ == '__main__':
    # Read ID from file.
    # with open('e:/file/userID.csv', 'rb') as f:
    #     ID = csv.reader(f)
    #     for row in ID:

    # When the program encounters error, it will ignore and continue crawl following user ID
    userID = "133158564"
    try:
        get_user_info(userID)
    except tweepy.TweepError:
        print('Failed to run the command on that user, Skipping...')
    except IndexError:
        print('List index out of range, Skipping...')
        # continue


