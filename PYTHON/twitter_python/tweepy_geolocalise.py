from tweepy import *
import time
import csv
import sys

OAUTH_TOKEN = '3353343353-8Nodrqq0HHCcRnhbDA4jvURGri9nlC7wM1FKJJ2'
OAUTH_SECRET = 'SwtszRwD70YtYbphjkvhsFAPQMMUiqIFJSxnTSn3Mdxad'
CONSUMER_KEY = 'WqfYFRoB7d65rrarF6NXB0pNc'
CONSUMER_SECRET = 'lDRoeTEhgyR1Hpkd5wHUrkZCx2JRwtV4HTS607o6OsTpnXOCPt'


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_SECRET)
api = tweepy.API(auth)


#search = "#MyHashtag"

latitude = 48.8588589	# geographical centre of search
longitude = 2.3470599	# geographical centre of search
max_range = 20			# search range in kilometres
num_results = 100000		# minimum results to obtain

csvfile = open('tweets_geolocalises3.txt', "w")
csvwriter = csv.writer(csvfile)
row = [ "user", "latitude", "longitude" ]
csvwriter.writerow(row)

result_count = 0
last_id = None

while result_count <  num_results:

    for tweet in tweepy.Cursor(api.search,
                           q=search,
                           include_entities=True).items():
        
        while True: 
            try:
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
            except tweepy.TweepError:
                time.sleep(60 * 15)
                continue        
            break
            #-----------------------------------------------------------------------
            # let the user know where we're up to
            #-----------------------------------------------------------------------
            print ("got %d results" % result_count)
            print(shall_i_sleep)

#-----------------------------------------------------------------------
# we're all finished, clean up and go home.
#-----------------------------------------------------------------------
csvfile.close()

print ("written to %s" % 'tweets_geolocalises3.txt')
