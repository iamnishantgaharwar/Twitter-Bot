# Import Tweepy package. To install: pip install tweepy
import tweepy

# Assigning keys into variable
consumer_key = "keys"
consumer_secret = "keys"
key = "keys"
secret = "keys"

# Fetching all the token
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

# Auth command. Which is an open authorization protocol to authenticate requests
api = tweepy.API(auth)
tweet = api.update_status("Bot is Live")
print(tweet.text)
print("Tweeted Successfully")
