#!/usr/bin/env python

import tweepy  # import twitter api python wrapper
import logging  # Python module to inform errors and info messages that help you debug them if any issue arise
from config import create_api  # import user credentials
from time import sleep  # import time.sleep

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()
QUERY = ["cats"]  # search term, can be hashtag or keyword
# Set to 'True' to like retweets, Set to 'False', to not like retweets.
LIKE = False
# Set to 'True' to follow retweets, Set to 'False', to not follow retweets.
FOLLOW = False
# Ex: SLEEP_TIME = 300 means 5 minutes sleep time.
# This will put the bot to sleep to avoid too many API requests and being banned.
SLEEP_TIME = 90

print("pybo for retweets, likes and follows")
print("pybo Settings")
print("Like Tweets :", LIKE)
print("Follow users :", FOLLOW)


def auto_retweet(api):
    # Read in your text Tweets
    for tweet in tweepy.Cursor(api.search, q=QUERY).items():
        try:
            print('\nTweet by: @' + tweet.user.screen_name)

            tweet.retweet()
            print('pybo has retweeted the tweet')

            # Favorite the tweet
            if LIKE:
                tweet.favorite()
                print('pybo has favorited the tweet')

            # Follow the user who tweeted
            if FOLLOW:
                if not tweet.user.following:
                    tweet.user.follow()
                    print('pybo has followed the user')

            sleep(SLEEP_TIME)

        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break


def main():  # main() creates a Tweepy API object using create_api() from the config module you previously created.
    api = create_api()
    while True:
        auto_retweet(api)


if __name__ == "__main__":
    main()
