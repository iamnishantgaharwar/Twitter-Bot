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
api = tweepy.API(auth)
# Creating a function to delete bulk Messages
def bulk_delete():
    # Here you can define specific count in item(10) if you want to control the number of tweet deleted
    for status in tweepy.Cursor(api.user_timeline).items():
        try:
            api.destroy_status(status.id)
            print("Tweet Deleted")
            sleep(2)  # You can disable the timer also but for good practice keep it as it is rather than abusing
        except tweepy.TweepyException as e:
            print("Fail to delete tweets try again..")
            print(e)
bulk_delete()
