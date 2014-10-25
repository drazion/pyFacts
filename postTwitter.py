import twitter
from keys import privateKeys

class TwitterAPI:
    def __init__(self, text):
        keys = privateKeys()
        self.api = twitter.Api(consumer_key=keys.consumer_key,
                                     consumer_secret=keys.consumer_secret,
                                     access_token_key=keys.access_token_key,
                                     access_token_secret=keys.access_token_secret)
        self.text = text

    def postStatus(self):
        self.api.PostUpdate(self.text)

