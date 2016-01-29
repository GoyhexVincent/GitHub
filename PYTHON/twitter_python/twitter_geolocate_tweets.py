from twitter import Twitter, OAuth, TwitterHTTPError

OAUTH_TOKEN = '3353343353-8Nodrqq0HHCcRnhbDA4jvURGri9nlC7wM1FKJJ2'
OAUTH_SECRET = 'SwtszRwD70YtYbphjkvhsFAPQMMUiqIFJSxnTSn3Mdxad'
CONSUMER_KEY = 'WqfYFRoB7d65rrarF6NXB0pNc'
CONSUMER_SECRET = 'lDRoeTEhgyR1Hpkd5wHUrkZCx2JRwtV4HTS607o6OsTpnXOCPt'

t = Twitter(auth=OAuth(OAUTH_TOKEN, OAUTH_SECRET,
            CONSUMER_KEY, CONSUMER_SECRET))

g = t.application.rate_limit_status()
print (g[u'resources'][u'statuses'][u'/statuses/retweets/:id'][u'remaining'])

#CREER UN BOT SOUS PYTHON, qui retweete ce qu'il trouve de correspondant à ses mots clés recherchés.
##def search_tweets(q, count=100):
##    return t.search.tweets(q=q, result_type='recent', count=count)
##def fav_tweet(tweet):
##    try:
##        result = t.favorites.create(_id=tweet['id'])
##        print "Favorited: %s" % (result['text'])
##        return result
##    # when you have already favourited a tweet
##    # this error is thrown
##    except TwitterHTTPError as e:
##        print "Error: ", e
##        return None
##
##def auto_fav(q, count=100):
##    result = search_tweets(q, count)
##    a = result['statuses'][0]['user']['screen_name']
##    print a
##    success = 0
##    for tweet in result['statuses']:
##        if fav_tweet(tweet) is not None:
##            success += 1
##    print "We Favorited a total of %i out of %i tweets" % (success,
##          len(result['statuses']))


#https://github.com/ideoforms/python-twitter-examples/blob/master/twitter-search-geo.py
from twitter import *
import sys
import csv
import time
import datetime

latitude = 48.8588589   # geographical centre of search
longitude = 2.3470599   # geographical centre of search
max_range = 20                  # search range in kilometres
num_results = 100000            # minimum results to obtain

csvfile = open('tweets_geolocalises3.txt', "w")
csvwriter = csv.writer(csvfile)
row = [ "user", "latitude", "longitude" ]
csvwriter.writerow(row)

#-----------------------------------------------------------------------
# the twitter API only allows us to query up to 100 tweets at a time.
# to search for more, we will break our search up into 10 "pages", each
# of which will include 100 matching tweets.
#-----------------------------------------------------------------------
result_count = 0
last_id = None
shall_i_sleep = 0

while result_count <  num_results:
        #-----------------------------------------------------------------------
        # perform a search based on latitude and longitude
        # twitter API docs: https://dev.twitter.com/docs/api/1/get/search
        #-----------------------------------------------------------------------
        query = t.search.tweets(q = "", geocode = "%f,%f,%dkm" % (latitude, longitude, max_range), count = 100, max_id = last_id)
        for result in query["statuses"]:
                #-----------------------------------------------------------------------
                # only process a result if it has a geolocation
                #-----------------------------------------------------------------------

                if result["geo"]:

                                        
                        user = result["user"]["screen_name"]
                        text = result["text"]
                        text = text.encode('ascii', 'replace')
                        latitude = result["geo"]["coordinates"][0]
                        longitude = result["geo"]["coordinates"][1]

                        # now write this row to our CSV file
                        row = [ user, text, latitude, longitude ]
                        csvwriter.writerow(row)
                        result_count += 1
                        

                last_id = result["id"]


        #-----------------------------------------------------------------------
        # let the user know where we're up to
        #-----------------------------------------------------------------------
        
        if shall_i_sleep < 50:
                
                print ("got %d results" % result_count)
                shall_i_sleep +=1
        else :
                        print("I'm going to sleep for 15 minutes, be right back:", datetime.datetime.now().time())
                        time.sleep(60*15)
                        shall_i_sleep = 0
                        
                        

#-----------------------------------------------------------------------
# we're all finished, clean up and go home.
#-----------------------------------------------------------------------
csvfile.close()

print ("written to %s" % 'tweets_geolocalises3.txt')




