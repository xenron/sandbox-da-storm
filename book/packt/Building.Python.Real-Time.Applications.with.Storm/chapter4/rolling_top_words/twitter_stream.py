from __future__ import absolute_import

import json

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

# Go to http://apps.twitter.com and create an app.
# The consumer key and secret will be generated for you after
consumer_key="2L0uJN9JTxzn7SCMLuJvrDZmL"
consumer_secret="VMZwGqRQTDhqLg9pxwTIwUte58qJBuWZ1pmwwPw940V3MZaXHi"

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token="69186439-FryIR5qHH15IKQZcnbVrsv4JDXL4rXCupg2EBhdlr"
access_token_secret="wNrbcJg8THSu0qf8QSmVGnkxfF2rxPVhiCNwQgFcThqLO"

class StdOutListener(StreamListener):
    """ A listener handles tweets are the received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    def on_data(self, data):
        print json.loads(data)['text']
        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.filter(track=['basketball'])
