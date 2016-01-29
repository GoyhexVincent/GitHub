#!/usr/bin/python

#-----------------------------------------------------------------------
# twitter-retweets
#  - print who has retweeted tweets from a given user's timeline
#-----------------------------------------------------------------------

from twitter import *

OAUTH_TOKEN = '3353343353-8Nodrqq0HHCcRnhbDA4jvURGri9nlC7wM1FKJJ2'
OAUTH_SECRET = 'SwtszRwD70YtYbphjkvhsFAPQMMUiqIFJSxnTSn3Mdxad'
CONSUMER_KEY = 'WqfYFRoB7d65rrarF6NXB0pNc'
CONSUMER_SECRET = 'lDRoeTEhgyR1Hpkd5wHUrkZCx2JRwtV4HTS607o6OsTpnXOCPt'

twitter = Twitter(auth=OAuth(OAUTH_TOKEN, OAUTH_SECRET,
            CONSUMER_KEY, CONSUMER_SECRET))

#-----------------------------------------------------------------------
# perform a basic search 
# twitter API docs: https://dev.twitter.com/docs/api/1/get/search
#-----------------------------------------------------------------------
results = twitter.statuses.user_timeline(screen_name = 'ubisoft')

#-----------------------------------------------------------------------
# loop through each of my statuses, and print its content
#-----------------------------------------------------------------------
for status in results:
	print ("@%s %s" % ('ubisoft', status["text"]))

	#-----------------------------------------------------------------------
	# do a new query: who has RT'd this tweet?
	#-----------------------------------------------------------------------
	retweets = twitter.statuses.retweets._id(_id = status["id"])
	for retweet in retweets:
		print (" - retweeted by %s" % (retweet["user"]["screen_name"]))
