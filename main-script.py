import tweepy
from dotenv import load_dotenv
import os

# load environment variables
load_dotenv()

# twitter API authentication
api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

auth = tweepy.OAuth1UserHandler(
   api_key, api_secret,
   access_token, access_token_secret
)

client_v1 = tweepy.API(auth)

client_v2 = tweepy.Client(
    consumer_key=api_key,
    consumer_secret=api_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
)

# fetch img from local storage and tweet 
mediaId = client_v1.media_upload("img/" + "dembele.jpg")
client_v2.create_tweet(
    text="Non.",
    media_ids=[mediaId.media_id_string]
) 
print("Tweet done :D")


