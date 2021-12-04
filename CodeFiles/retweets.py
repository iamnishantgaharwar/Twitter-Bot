# Import Tweepy package. To install: pip install tweepy
import tweepy
from time import sleep

# Assigning keys into variable
consumer_key = "keys"
consumer_secret = "keys"
key = "keys"
secret = "keys"

# Fetching all the token
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

# Auth command. Which is an open authorization protocol to authenticate requests
api = tweepy.API(auth, wait_on_rate_limit=True)


def retweet_bulk():
    # Searching for tweets from Home Timeline of User
    # User rate limit: 50 requests per 15-minute window
    for tweets in tweepy.Cursor(api.home_timeline).items(10):  # Binded for 10 retweets only
        try:
            api.retweet(tweets.id)
            print("Retweet Done..")
            sleep(2)
        except tweepy.TweepyException as e:
            print(e)


retweet_bulk()
