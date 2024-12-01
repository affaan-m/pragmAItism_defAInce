import os
import sys
import logging

# Setup logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Add project root to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def test_simple_tweet():
    try:
        logger.debug("Importing TweetGenerator")
        from src.tweet_generator import TweetGenerator
        
        logger.debug("Creating TweetGenerator instance")
        generator = TweetGenerator()
        
        logger.debug("Generating test tweet")
        tweet = generator.generate_tweet("technology")
        
        print(f"\nGenerated tweet: {tweet}")
        
    except Exception as e:
        logger.error(f"Error in test: {e}")
        raise e

if __name__ == "__main__":
    test_simple_tweet() 