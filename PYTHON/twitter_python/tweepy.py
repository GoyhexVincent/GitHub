from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

ckey = 'WqfYFRoB7d65rrarF6NXB0pNc'
csecret = 'lDRoeTEhgyR1Hpkd5wHUrkZCx2JRwtV4HTS607o6OsTpnXOCPt'
atoken = '3353343353-8Nodrqq0HHCcRnhbDA4jvURGri9nlC7wM1FKJJ2'
asecret = 'SwtszRwD70YtYbphjkvhsFAPQMMUiqIFJSxnTSn3Mdxad'

class listener(StreamListener):
    def on_data(self_data):
        print(data)
        return True
    def on_error(self_status):
        print(status)
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
twitterStream.filter (track=["valls"])
