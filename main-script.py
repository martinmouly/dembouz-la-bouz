import tweepy
from dotenv import load_dotenv
import os
from bing_image_downloader import downloader
import json
import random

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

# Open and read all players from db
json_file = open('db.json')
data = json.load(json_file)
json_file.close()

# Select a player randomly
player_name = data['footballers'][random.randint(0,len(data['footballers']) - 1)]["name"]
print("Selected player : " + player_name)

# Download image from Bing
search_query= player_name + " playing football jpg"
downloader.download(search_query, limit=1, verbose=False)
print("Download done :D")
# input("Press Enter to continue...")

""" # Create tweet with player name + image
mediaId = client_v1.media_upload("dataset/" + search_query + "/Image_1.jpg")
client_v2.create_tweet(
    text=player_name,
    media_ids=[mediaId.media_id_string]
) 
print("Tweet done :D")
print("Press Enter to continue...")

# Delete image from local storage
os.remove(dataset) """
