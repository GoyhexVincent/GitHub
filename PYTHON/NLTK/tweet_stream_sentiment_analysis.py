

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import sentiment_mod_1 as s



#consumer key, consumer secret, access token, access secret.
atoken = '3353343353-8Nodrqq0HHCcRnhbDA4jvURGri9nlC7wM1FKJJ2'
asecret = 'SwtszRwD70YtYbphjkvhsFAPQMMUiqIFJSxnTSn3Mdxad'
ckey = 'WqfYFRoB7d65rrarF6NXB0pNc'
csecret = 'lDRoeTEhgyR1Hpkd5wHUrkZCx2JRwtV4HTS607o6OsTpnXOCPt'


class listener(StreamListener):

    def on_data(self, data):
        try:
            all_data = json.loads(data)

            tweet = all_data["text"]
            sentiment_value, confidence = s.sentiment(tweet)
            print(tweet, sentiment_value, confidence)

            if confidence*100 >= 80:
                output = open("twitter-out.txt","a")
                output.write(sentiment_value)
                output.write('\n')
                output.close()

            return True
        except:
            return True

    def on_error(self, status):
        print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["ubisoft"])
