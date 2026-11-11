import logging
from social.twitter_client import TwitterClient
from tweet_generator import generate_personality_tweet
import schedule
import time
import os
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class AIBot:
    def __init__(self):
        load_dotenv()
        self.twitter = TwitterClient()
        try:
            self.tweet_interval = int(os.getenv("TWEET_INTERVAL", "120").strip())
        except (ValueError, TypeError) as e:
            logger.warning(f"Invalid TWEET_INTERVAL value, using default of 120: {e}")
            self.tweet_interval = 120
        
    def post_tweet(self):
        """Generate and post a tweet"""
        try:
            # Generate tweet using our personality tweet generator
            tweet = generate_personality_tweet()
            if tweet:
                # Post to Twitter
                success = self.twitter.post_tweet(tweet)
                if success:
                    logger.info(f"Successfully posted tweet: {tweet}")
                else:
                    logger.error("Failed to post tweet")
            else:
                logger.error("Failed to generate tweet")
        except Exception as e:
            logger.error(f"Error in post_tweet: {e}")
            
    def run(self, mode="prod"):
        """Run the bot"""
        logger.info(f"Starting bot in {mode} mode")
        
        if mode == "test":
            # Just post one tweet for testing
            self.post_tweet()
        else:
            # Schedule regular tweets
            schedule.every(self.tweet_interval).minutes.do(self.post_tweet)
            
            while True:
                schedule.run_pending()
                time.sleep(60)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["test", "prod"], default="test")
    args = parser.parse_args()
    
    bot = AIBot()
    bot.run(mode=args.mode) 