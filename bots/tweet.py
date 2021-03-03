import tweepy
import logging
from time import sleep 
from config import create_api  # import user credentials

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

# Ex: SLEEP_TIME = 300 means 5 minutes sleep time. 
# This will put the bot to sleep to avoid too many API requests and being banned.
SLEEP_TIME = 300

def auto_tweet(api):
    # Read in your text Tweets 
    my_file=open('tweets.txt','r')
    file_lines=my_file.readlines()
    my_file.close()
    # Create a loop to iterate over each line
    for line in file_lines:
    # Add try/except to flag any errors
        try:
            print(line)
            # Add if statement to make sure that blank lines are skipped
            if line != '\n':
                api.update_status(line)
            else:
                pass
        except tweepy.TweepError as e:
            print(e.reason)
        sleep(SLEEP_TIME) # Sleep time in seconds. This will put the bot to sleep before it goes to Tweet the next line in my_tweets.txt

def main(): #main() creates a Tweepy API object using create_api() from the config module you previously created. 
    api = create_api()
    while True:
        auto_tweet(api)
        logger.info("Waiting...")
#
if __name__ == "__main__":
    main()
    
