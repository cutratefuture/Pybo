#!/usr/bin/env python
# tweepy-bots/bots/favretweet.py

import tweepy  # import twitter python api
import logging  # Python module to inform errors and info messages that help you debug them if any issue arise
from config import create_api  # import user credentials
from time import sleep 


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

SLEEP_TIME = 60 # time in sec

class FavRetweetListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet): # The on_status() of FavRetweetListener processes tweets from the stream.
        #  This method receives a status object and uses favorite() and retweet() to mark the tweet as Liked and retweet.
        logger.info(f"Processing tweet id {tweet.id}")
      # To avoid retweeting and liking tweets that are replies to other tweets, on_status() uses an if to see if in_reply_to_status_id is not None. Also, the code checks if you’re the tweet author to avoid retweeting and liking your own content.
        sleep(SLEEP_TIME) #time between retweets
        if tweet.in_reply_to_status_id is not None or \
                tweet.user.id == self.me.id:
            # This tweet is a reply or I'm its author so, ignore it
            return
        if not tweet.favorited:
            # Mark it as Liked, since we have not done it yet
            try:
                tweet.favorite()
            except Exception as e:
                logger.error("Error on fav", exc_info=True)
        if not tweet.retweeted:
            # Retweet, since we have not retweeted it yet
            try:
                tweet.retweet()
            except Exception as e:
                logger.error("Error on fav and retweet", exc_info=True)

    def on_error(self, status):
        logger.error(status)


def main(keywords):
    # the main function uses create_api() from the config module to create a Tweepy API object.
    api = create_api()
   # You declared a new class, FavRetweetListener. This class is used for the stream listener tweets_listener. By extending Tweepy’s StreamLister, we reused code that is common to all stream listeners.
    sleep(3) #time between retweets
    # Streaming allows you to actively watch for tweets that match certain criteria in real time.
    tweets_listener = FavRetweetListener(api)
    # We created the stream using tweepy.Stream, passing the authentication credentials and our stream listener
    stream = tweepy.Stream(api.auth, tweets_listener)
    # To start getting tweets from the stream, you have to call the stream’s filter(), passing the criteria to use to filter tweets. Then, for each new tweet that matches the criteria, the stream object invokes the stream listener’s on_status().
    stream.filter(track=keywords, languages=["en"])

    # A Tweepy stream is created to filter tweets that are in the English language and include some of the keywords specified in the main function argument, "Python" or "Tweepy" in this case.
if __name__ == "__main__":
    main(["apples", "oranges"])


