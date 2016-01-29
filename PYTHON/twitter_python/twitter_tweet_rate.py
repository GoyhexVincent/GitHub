#!/usr/bin/python

#-----------------------------------------------------------------------
# twitter-tweet-rate
#-----------------------------------------------------------------------

from twitter import *
from datetime import datetime

created_at_format = '%a %b %d %H:%M:%S +0000 %Y'


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
terms = "sarkozy"
query = twitter.search.tweets(q = terms, lang='fr', result_type='recent')
results = query["statuses"]
                  
#-----------------------------------------------------------------------
# take the timestamp of the first and last tweets in these results,
# and calculate the average time between tweets.
#-----------------------------------------------------------------------
first_timestamp = datetime.strptime(results[0]["created_at"], created_at_format)
last_timestamp = datetime.strptime(results[-1]["created_at"], created_at_format)
total_dt = (first_timestamp - last_timestamp).total_seconds()
mean_dt = total_dt / len(results)

#-----------------------------------------------------------------------
# print the average of the differences
#-----------------------------------------------------------------------
print ("Average tweeting rate for '%s' between %s and %s: %.3fs" % (terms, results[-1]["created_at"], results[ 0]["created_at"], mean_dt))
