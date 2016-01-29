from twitter import Twitter, OAuth, TwitterHTTPError

OAUTH_TOKEN = '3353343353-8Nodrqq0HHCcRnhbDA4jvURGri9nlC7wM1FKJJ2'
OAUTH_SECRET = 'SwtszRwD70YtYbphjkvhsFAPQMMUiqIFJSxnTSn3Mdxad'
CONSUMER_KEY = 'your consumer key'
CONSUMER_SECRET = 'your consumer secret'

t = Twitter(auth=OAuth(, OAUTH_SECRET,
            CONSUMER_KEY, CONSUMER_SECRET))
