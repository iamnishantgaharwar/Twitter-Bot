#This code is for deleting Single Tweet Using Python


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
delete = api.destroy_status(id="Paste Your Id here without inverted commas")
print(delete.text)
print("Tweet Deleted Successfully")
