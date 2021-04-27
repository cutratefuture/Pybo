#!/usr/bin/env python3
import tweepy
import logging
from config import create_api
from time import sleep

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def unfollow_nonfollowers(api):
    logger.info("Retrieving and unfollowing nonfollowers")
    followers = api.followers_ids(api.me().id)
    print("Followers", len(followers))
    friends = api.friends_ids(api.me().id)
    print("You follow:", len(friends))
    print( "You unfollowed:", (len(friends) - len(followers)))
    for friend in friends:
        if friend not in followers:
            api.destroy_friendship(friend)
#main() creates a Tweepy API object using create_api() from the config module you previously created.Then, inside a loop, unfollow_nonfollowers() is called once every minute.
def main():  
    api = create_api()

    while True:
        unfollow_nonfollowers(api)
        exit  ("Till Next Round!")

if __name__ == "__main__":
    main()
