from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from kafka import SimpleProducer, SimpleClient

CONSUMER_KEY = '#####################'
CONSUMER_SECRET = '#####################'
ACCESS_TOKEN_KEY = '#####################'
ACCESS_TOKEN_SECRET = '#####################'


class StdOutListener(StreamListener):

    def on_data(self, data):
        producer.send_messages("twitter_topic", data.encode('utf-8'))
        print(data)
        return True

    def on_error(self, status):
        print(status)


kafka = SimpleClient("localhost:9092")
producer = SimpleProducer(kafka)
stream_listener = StdOutListener()

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)

stream = Stream(auth, stream_listener)
stream.filter(track=['NBA'])


