import tweepy

from auth import(
    consumer_key, consumer_secret, access_token, access_token_secret, bearer_token
)

client = tweepy.Client(
    consumer_key=consumer_key, consumer_secret=consumer_secret,
    access_token=access_token, access_token_secret=access_token_secret
)

# reponse = client.search_recent_tweets(query='#python lang:en -is:retweet', max_results=10)
# print(reponse)

# CANT RETWEET AS TWITTER IS NO LONGER ALLOWING FOR SEARCH QUERIES ON FREE TIER DEV ACCOUNT
# THIS FUNCTION IS STOPPED UNTIL I FIND A SOLUTION TO THIS

