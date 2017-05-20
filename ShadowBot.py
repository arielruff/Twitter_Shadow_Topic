'''

Twitter Shadow Topic - A Topic Promoting Twitter Bot

This is a topic promoting twitter bot. All that is needed is a twitter accounts
api information and 3 topic hashtags. The bot skims for tweets with any of the topic hashtags located
in the program code or entered at the prompt and then retweets them after adding a trending hashtag to the end of
the tweet in order to inject them into popular streams.

- You can run the app and enter your credentials at the prompt, or you can
insert them below to avoid entering them everytime the app is run. The same goes
for the needed topic hashtags. They can be entered into code or at the prompt.

<<<<WARNING>>>> It is not suggested that you use this bot with your main
Twitter account credentials. Twitter might see it as spam and lock down
the twitter account used.

- Miso_S00P

---------------- RESIST ---------------- <3 <3 <3 <3 <3 <3
'''

import tweepy
import time
import json
import urllib
import random
import sys

# List of Topic Hashtags
# This list can be customized and change in size without worry
# ----------------------------------------
# ENTER YOUR TOPIC HASHTAGS BELOW
# ----------------------------------------
book = ['#default','#default','#default']

# Get a list of trending hashtags
def get_trending_hashtag(rank):
    trends_grab = api.trends_place(23424977)
    trend_raw_data = trends_grab[0]
    trending_tags_meta = trend_raw_data['trends']
    top_trend = trending_tags_meta[rank]['name']
    return top_trend

# Get a recent tweet using one of the Hashtags in the "book" list
def get_tweet(random):
    for tweet in tweepy.Cursor(api.search,q=random).items(1):
        t = tweet.text
        return t

# Get tweet from "get_tweet" and bundle it with a trending Hashtag 
def make_tweet():
    trend_text = get_trending_hashtag(random.randint(0,4))
    tweet_text = get_tweet(random.choice(book))
    if (len(tweet_text)+len(trend_text)) <= 138:
        final_tweet = " ".join((tweet_text,trend_text))
    else:
        final_tweet = tweet_text
    return final_tweet

# A function which puts the app to sleep and displays a countdown
def sleep_count(seconds):
    for i in range(seconds,0,-1):
        time.sleep(1)
        sys.stdout.write("---- "+str(i)+" Seconds Till Next Tweet!\r",)
        sys.stdout.flush()

# Run the tweetbot (Send out a bundled tweet via Twitter)
def run_tweetbot():
    count = 0
    while True:
        try:
            new_tweet = make_tweet()
            api.update_status(new_tweet)
            print ("Tweet: "+new_tweet)
            count += 1
            seconds = 900 #Runs the bot every 15 minutes
        except tweepy.TweepError as e:
            print(e.reason)
            seconds = 5
        print ("You Have Sent " + str(count) + " Tweets")
        sleep_count(seconds)


# ----------------------------------------
# ENTER YOUR TWITTER API CREDENTIALS BELOW
# ----------------------------------------

#--------------------------
# PROGRAM START
#--------------------------

print ("-------- Twitter Shadow Topic v1.0 --------")
print ("API Twitter credentials can be entered directly into the python code or at prompt!")
consumer_key = 'ENTER YOUR CONSUMER KEY HERE'
consumer_secret = 'ENTER YOUR CONSUMER SECRET HERE'
access_token = 'ENTER YOUR ACCESS TOKEN HERE'
access_secret = 'ENTER YOUR ACCESS TOKEN SECRET HERE'
if consumer_key == "ENTER YOUR CONSUMER KEY HERE":
    consumer_key = input("Enter your Twitter Consumer Key: ")
    consumer_secret = input("Enter your Twitter Consumer Secret: ")
    access_token = input("Enter your Twitter Access Token: ")
    access_secret = input("Enter your Twitter Access Secret: ")
if book[0] == "#default":
    print ("Enter the topics you wish to promote EX: #Cats")
    hash1 = input("Enter your first hashtag: ")
    hash2 = input("Enter your second hashtag: ")
    hash3 = input("Enter your third hashtag: ")
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

run_tweetbot()

############### Miso_S00P #################