# tweepy-bots/bots/config.py
import tweepy
import logging

logger = logging.getLogger()


def create_api():
    # create_api(), a function that reads authentication credentials from environment variables and creates the Tweepy API object:
    # This code uses os.getenv() to read environment variables and then creates the Tweepy auth object. Then the API object is created.
    consumer_key = " "
    consumer_secret = " "
    access_token = " "
    access_token_secret = " "

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    # Passing wait_on_rate_limit and wait_on_rate_limit_notify in the creation of the tweepy.API object makes Tweepy wait and print a message when the rate limit is exceeded.
    api = tweepy.API(auth, wait_on_rate_limit=True,
                     wait_on_rate_limit_notify=True)
    # Before returning the API object, create_api() calls verify_credentials() to check that the credentials are valid.
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api
