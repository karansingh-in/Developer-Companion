import tweepy
import os
import dotenv

dotenv.load_dotenv()
bearer_token = os.getenv('bearer_token')
consumer_key = os.getenv('X_API_KEY')
consumer_secret = os.getenv('X_API_SECRET')
access_token = os.getenv('X_ACCESS_TOKEN')
access_token_secret = os.getenv('X_ACCESS_SECRET')
client = tweepy.Client(bearer_token=bearer_token)
client = tweepy.Client(
    consumer_key=consumer_key, consumer_secret=consumer_secret,
    access_token=access_token, access_token_secret=access_token_secret
)