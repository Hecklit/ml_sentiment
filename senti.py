from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
import os

import tweepy
from textblob import TextBlob

consumer_key =  os.environ.get("consumer_key")
consumer_secret = os.environ.get("consumer_secret")

access_token = os.environ.get("access_token")
access_token_secret = os.environ.get("access_token_secret")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
searchTerm = input()
public_tweets = api.search(searchTerm)

import csv
with open(searchTerm+'.csv', 'w') as csvfile:
    spamwriter = csv.writer(csvfile, dialect='excel')
    for tweet in public_tweets:
        analysis = TextBlob(tweet.text)
        result = 'negative'
        if analysis.sentiment.polarity >= 0:
            result = 'positive'
        spamwriter.writerow([result, tweet.text])
