import tweepy, random, schedule, time
from data import advices, hashtags
from auth import(
    consumer_key, consumer_secret, access_token, access_token_secret, bearer_token
)

client = tweepy.Client(
    consumer_key=consumer_key, consumer_secret=consumer_secret,
    access_token=access_token, access_token_secret=access_token_secret
)

# POSTING SOMETHING ----
# client.create_tweet(text='this is test 3')

# RETWEETING A POST ----
# client.retweet(1982342611764453882)

# REPLYING TO A POST ----
# client.create_tweet(
#     text="Nice post!",
#     in_reply_to_tweet_id=1982342611764453882
# )

count = int(1)
def job():
    global count
    try:
        print('im here')
        client.create_tweet(text=f'Post {count}\n' + random.choice(advices) + '\n\n' + random.choice(hashtags))
        count += 1
        print("posted something")
    except Exception as e:
        print("Error:", e)


schedule.every().day.at("00:16:00").do(job)
# schedule.every(10).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)