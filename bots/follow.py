#!/usr/bin/env python
# tweepy-bots/bots/followfollowers.py

import tweepy
import logging
from config import create_api
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def follow_followers(api):
    #follow_followers() uses a Tweepy cursor and the Tweepy API method followers() to get your list of followers. This list contains a Tweepy user model for each user that is following you.
    logger.info("Retrieving and following followers")
    for follower in tweepy.Cursor(api.followers).items():
        if not follower.following:
            logger.info(f"Following {follower.name}")
            follower.follow()
    #Then the bot iterates through the list and uses following to check if you are already following each user. Users that are not already being followed are followed using follow().

def main(): #main() creates a Tweepy API object using create_api() from the config module you previously created. 
    api = create_api()
    #Then, inside a loop, follow_followers() is called once every minute.
    while True:
        follow_followers(api)
        logger.info("Waiting...")
        time.sleep(60)
#
if __name__ == "__main__":
    main()