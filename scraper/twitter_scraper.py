import tweepy
from datetime import date

class TwitterScraper:
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        self.auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        self.auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(self.auth)

    def get_tweets(self, user):
        today = date.today()
        tweets = self.api.user_timeline(screen_name=user, count=200, tweet_mode='extended', include_entities=True)
        # Filter tweets to include only those from today
        today_tweets = [tweet for tweet in tweets if tweet.created_at.date() == today]
        return today_tweets

    def has_image(self, tweet):
        return 'media' in tweet.entities

    def get_image_url(self, tweet):
        if self.has_image(tweet):
            media = tweet.entities.get('media', [])
            if(len(media) > 0):
                return media[0]['media_url']
        return None
