# Import statements
import unittest
import sqlite3
import requests
import json
import re
import tweepy
import twitter_info # still need this in the same directory, filled out

consumer_key = twitter_info.consumer_key
consumer_secret = twitter_info.consumer_secret
access_token = twitter_info.access_token
access_token_secret = twitter_info.access_token_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

"""fname = 'twitter_cache.json'

try:
	cache_file = open(fname, 'r', encoding = 'utf-8') # Try to read the data from the file
	cache_contents = cache_file.read()  # If it's there, get it into a string
	CACHE_DICTION = json.loads(cache_file) # And then load it into a dictionary
	cache_file.close() # Close the file, we're good, we got the data in a dictionary.

except:
    CACHE_DICTION = {}"""

fname = "twitter_cache.json"
try:
	cache_file = open(fname,'r')	
	cache_contents = cache_file.read()
	cache_file.close()
	cacheDict1 = json.loads(cache_contents)
	cache_file.close()
	cacheDict = json.loads(cacheDict1)
except:
	cacheDict = {}

## [PART 1]
# Finish the function get_tweets that searches for all tweets created by the user "umsi" and 
# all tweets that mention "umsi"
# It takes as input the api object, the cache dictionary, and the cache file name
# It caches the data and will use the cached data if it exists
def get_tweets(api, cacheDict, fname):

    # if the data is in the dictionary return it
    searchTerm = "umsi"
    if searchTerm in cacheDict:
        print("Using data from cache")
        return(cacheDict[searchTerm])
        
    # otherwise get the data, add it the dictionary, and write it to a file
    else:
        print("Fetching tweets")

        # get tweets by the umsi user
        userTweets = api.user_timeline(id=searchTerm)

        # get tweets that mention umsi
        umsiTweets = api.search(q=searchTerm)
        umsiTweets = umsiTweets['statuses']

        # add both to the dictionary
        cacheDict[searchTerm] = umsiTweets + userTweets

        cache_file = open(fname, 'w')
        cache_file.write(json.dumps(cacheDict))
        cache_file.close()

        return(umsiTweets + userTweets)
        
get_tweets(api, cacheDict, fname)
test = get_tweets(api, cacheDict, fname)
# part 2
# Finish the function setUpTweetTable that takes a list of tweets, a sqlite connection object, and a cursor and inserts the tweet information in the database
"""tweetList = get_tweets(api, cacheDict, fname)
conn = sqlite3.connect('tweets.sqlite')
cur = conn.cursor()

def setUpTweetTable(tweetList, conn, cur):
	# Fist create a database: tweets.sqlite,
	cur.execute('DROP TABLE IF EXISTS Tweets')
	cur.execute('CREATE TABLE Tweets(tweet_id TEXT, author TEXT, time_posted TIMESTAMP, tweet_text TEXT, retweets INTEGER)')
	for tweet in tweetList:
		_tweet_id = tweet['id_str']
		author = tweet['user']
		_author = author['screen_name']
		_time_posted = tweet['created_at']
		_tweet_text = tweet['text']
		_retweets = tweet['retweet_count']
		cur.execute('INSERT INTO Tweets (tweet_id, author, time_posted, tweet_text, retweets) VALUES (?,?,?,?,?)', 
			(_tweet_id, _author, _time_posted, _tweet_text, _retweets))
	conn.commit()

setUpTweetTable(tweetList, conn, cur)

## [PART 3]
# Finish the function getTimeAndText that returns a list of strings that contain the 
# time_posted and the text of the tweets.  It takes a database cursor as input.
# Select the time_posted and tweet_text from the Tweets table in tweets.sqlite and return a list 
# of strings that contain the date/time and text of each tweet in the form: date/time - text as shown below
# Mon Oct 09 16:02:03 +0000 2017 - #MondayMotivation https://t.co/vLbZpH390b
def getTimeAndText(cur):
	cur.execute('SELECT time_posted, tweet_text FROM Tweets')
	lst = []
	for row in cur:
		phrase = str(row[0]) + ' - ' + str(row[1])
		lst.append(phrase)
	return(lst)

## [Part 4]
# Finish the function getAuthorAndNumRetweets that returns a list of strings for the tweets that have been retweeted MORE than 2 times
# It takes a database cursor as input.
# Select the author (screen name) and number of retweets for of all of the tweets that have been retweeted MORE than 2 times
# Return a list of strings that are in the form: author - # retweets as shown below
# umsi - 5

def getAuthorAndNumRetweets(cur):
	cur.execute('SELECT author, retweets FROM Tweets WHERE retweets > 2')
	lst = []
	for row in cur:
		phrase = str(row[0]) + " - " + str(row[1])
		lst.append(phrase)
	return(lst)"""






































