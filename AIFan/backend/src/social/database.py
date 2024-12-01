from supabase import create_client
import os
from dotenv import load_dotenv

load_dotenv()

class SupabaseClient:
    def __init__(self):
        self.supabase = create_client(
            os.getenv("SUPABASE_URL"),
            os.getenv("SUPABASE_KEY")
        )
        
    def save_tweet(self, tweet_data):
        return self.supabase.table('tweets').insert(tweet_data).execute()
    
    def get_tweets(self, limit=10):
        return self.supabase.table('tweets').select("*").limit(limit).execute()
    
    def save_voice_generation(self, voice_data):
        return self.supabase.table('voice_generations').insert(voice_data).execute()
    
    def save_analytics(self, analytics_data):
        return self.supabase.table('analytics').insert(analytics_data).execute()
    
    def get_analytics(self, timeframe="7d"):
        return self.supabase.table('analytics').select("*").execute() 