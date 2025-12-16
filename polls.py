import tweepy, random, schedule, time
from data import poll_options, poll_questions, hashtags
from auth import(
    consumer_key, consumer_secret, access_token, access_token_secret
)

client = tweepy.Client(
    consumer_key=consumer_key, consumer_secret=consumer_secret,
    access_token=access_token, access_token_secret=access_token_secret
)

def conduct_polls():
    try:
        print('im here')
        number = int(random.randint(1,200))
        client.create_tweet(
        text=poll_questions[number] + '\n\n' + random.choice(hashtags),
        poll_options=poll_options[number],
        poll_duration_minutes=1440
        )  
        print("posted something")
    except Exception as e:
        print("Error:", e)

while True:
    schedule.run_pending()
    time.sleep(random.randint(5,25))