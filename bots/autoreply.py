#!/usr/bin/env python
# tweepy-bots/bots/autoreply.py

import tweepy
import logging
from config import create_api
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()
# check_mentions() returns the greatest processed tweet id. This information will be used as the since_id in the next call to look only for tweets more recent than the ones already fetched
def check_mentions(api, keywords, since_id):
    logger.info("Retrieving mentions")
    new_since_id = since_id
    #This function uses a Tweepy cursor and mentions_timeline() to get all the tweets mentioning you that have an id greater than the since_id variable
    for tweet in tweepy.Cursor(api.mentions_timeline,
        since_id=since_id).items():
        new_since_id = max(tweet.id, new_since_id)
        if tweet.in_reply_to_status_id is not None:
            continue
        if any(keyword in tweet.text.lower() for keyword in keywords):
            logger.info(f"Answering to {tweet.user.name}")
            #For each tweet mentioning you, its author is followed using tweet.user.follow() if you are not already following them.
            if not tweet.user.following:
                tweet.user.follow()
            #Then a reply to the tweet is created using update_status(), passing the id of the original tweet as in_reply_to_status_id.
            api.update_status(
                status= ( api.get_user(id) + ' :y'),
                in_reply_to_status_id=tweet.id,
            )
    return new_since_id
#the main function creates a Tweepy API object. 
def main():
    api = create_api()
    since_id = 1 #initializes the variable since_id with the value 1. 
    #This variable is used to only fetch mentions created after those already processed.
    while True: #Inside a loop, check_mentions() is called once every minute.
        since_id = check_mentions(api, ["fuck"], since_id)
        #This function uses a Tweepy cursor and mentions_timeline() to get all the tweets mentioning you that have an id greater than the since_id variable.
        logger.info("Waiting...")
        time.sleep(60)

if __name__ == "__main__":
    main()