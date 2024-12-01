import tweepy
import os
from dotenv import load_dotenv
import logging
import webbrowser

logger = logging.getLogger(__name__)

class TwitterClient:
    def __init__(self):
        load_dotenv()
        
        # OAuth 1.0a Handler
        self.auth = tweepy.OAuthHandler(
            os.getenv("TWITTER_API_KEY"),
            os.getenv("TWITTER_API_SECRET"),
            callback="http://127.0.0.1:8000/callback"
        )
        
        # If we don't have tokens, get them
        if not os.getenv("TWITTER_ACCESS_TOKEN") or not os.getenv("TWITTER_ACCESS_TOKEN_SECRET"):
            self.handle_oauth_flow()
        else:
            self.auth.set_access_token(
                os.getenv("TWITTER_ACCESS_TOKEN"),
                os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
            )
        
        self.client = tweepy.Client(
            consumer_key=os.getenv("TWITTER_API_KEY"),
            consumer_secret=os.getenv("TWITTER_API_SECRET"),
            access_token=os.getenv("TWITTER_ACCESS_TOKEN"),
            access_token_secret=os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
        )
        logger.info("Twitter client initialized")
    
    def handle_oauth_flow(self):
        """Handle OAuth flow to get access tokens"""
        try:
            # Get authorization URL
            auth_url = self.auth.get_authorization_url()
            print(f"\nPlease visit this URL to authorize the app:\n{auth_url}")
            
            # Open browser automatically
            webbrowser.open(auth_url)
            
            # Get the verifier code from user
            verifier = input('\nEnter the verification code: ')
            
            # Get the access token
            self.auth.get_access_token(verifier)
            
            print("\nAdd these tokens to your .env file:")
            print(f"TWITTER_ACCESS_TOKEN={self.auth.access_token}")
            print(f"TWITTER_ACCESS_TOKEN_SECRET={self.auth.access_token_secret}")
            
        except Exception as e:
            logger.error(f"Error in OAuth flow: {e}")
            raise e
        
    def post_tweet(self, text):
        """Post a tweet using Twitter API v2"""
        try:
            response = self.client.create_tweet(text=text)
            logger.info(f"Tweet posted successfully: {text}")
            return True
        except Exception as e:
            logger.error(f"Error posting tweet: {e}")
            return False
            
    def monitor_timeline(self):
        """Monitor home timeline for interaction opportunities"""
        try:
            timeline = self.api.home_timeline(count=50)
            for tweet in timeline:
                interaction_type, content = self.interaction_handler.decide_interaction(tweet)
                
                if interaction_type == "reply":
                    self.api.update_status(
                        status=content,
                        in_reply_to_status_id=tweet.id,
                        auto_populate_reply_metadata=True
                    )
                elif interaction_type == "quote":
                    self.api.update_status(
                        f"{content}\nhttps://twitter.com/user/status/{tweet.id}"
                    )
                elif interaction_type == "like":
                    self.api.create_favorite(tweet.id)
                elif interaction_type == "retweet":
                    self.api.retweet(tweet.id)
                    
        except Exception as e:
            print(f"Error monitoring timeline: {e}") 