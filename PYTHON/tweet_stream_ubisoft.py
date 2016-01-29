#!/usr/bin/python

#-----------------------------------------------------------------------
# twitter-stream-format:
#  - ultra-real-time stream of twitter's public timeline.
#    does some fancy output formatting.
#-----------------------------------------------------------------------

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
import json



atoken = '3353343353-8Nodrqq0HHCcRnhbDA4jvURGri9nlC7wM1FKJJ2'
asecret = 'SwtszRwD70YtYbphjkvhsFAPQMMUiqIFJSxnTSn3Mdxad'
ckey = 'WqfYFRoB7d65rrarF6NXB0pNc'
csecret = 'lDRoeTEhgyR1Hpkd5wHUrkZCx2JRwtV4HTS607o6OsTpnXOCPt'

class listener(StreamListener):
    def on_data(self, data):
        all_data= json.loads(data)

        tweet = all_data["text"]
        print((tweet))
        time.sleep
        return True
def on_error(self, status):
    print(status)

        
auth= OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth,listener())
twitterStream.filter(track=["sarko"])



