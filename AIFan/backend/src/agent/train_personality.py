import pandas as pd
import json
import tweepy
from datetime import datetime
import openai
import os
from dotenv import load_dotenv
from typing import List, Dict

load_dotenv()

class PersonalityTrainer:
    def __init__(self):
        self.openai = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.setup_twitter_client()
        
    def setup_twitter_client(self):
        auth = tweepy.OAuthHandler(
            os.getenv("TWITTER_API_KEY"),
            os.getenv("TWITTER_API_SECRET")
        )
        auth.set_access_token(
            os.getenv("TWITTER_ACCESS_TOKEN"),
            os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
        )
        self.twitter = tweepy.API(auth)
    
    def collect_tweets(self, username: str, count: int = 3200) -> List[Dict]:
        """Collect tweets for training"""
        tweets = []
        for tweet in tweepy.Cursor(self.twitter.user_timeline, 
                                screen_name=username, 
                                tweet_mode="extended").items(count):
            tweets.append({
                'text': tweet.full_text,
                'created_at': tweet.created_at.isoformat(),
                'engagement': tweet.favorite_count + tweet.retweet_count
            })
        return tweets
    
    def prepare_training_data(self, tweets: List[Dict]) -> List[Dict]:
        """Prepare tweets for fine-tuning"""
        return [{
            "messages": [
                {"role": "system", "content": "You are a Twitter bot that tweets like @affaanmustafa"},
                {"role": "assistant", "content": tweet['text']}
            ]
        } for tweet in tweets]
    
    def save_training_data(self, data: List[Dict], filename: str = "training_data.jsonl") -> None:
        """Save training data in JSONL format"""
        with open(filename, 'w') as f:
            for entry in data:
                json.dump(entry, f)
                f.write('\n')
    
    def create_fine_tune(self, training_file: str):
        """Create fine-tuning job"""
        return self.openai.fine_tuning.jobs.create(
            training_file=training_file,
            model="gpt-3.5-turbo"
        )
    
    def train(self, username: str) -> str:
        """Complete training pipeline"""
        print("Collecting tweets...")
        tweets = self.collect_tweets(username)
        
        print("Preparing training data...")
        training_data = self.prepare_training_data(tweets)
        
        print("Saving training data...")
        self.save_training_data(training_data)
        
        print("Creating fine-tuning job...")
        fine_tune = self.create_fine_tune("training_data.jsonl")
        
        print(f"Fine-tuning job created: {fine_tune.id}")
        return fine_tune.id

if __name__ == "__main__":
    trainer = PersonalityTrainer()
    trainer.train("affaanmustafa") 