import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.tweet_generator import TweetGenerator

def test_generation():
    generator = TweetGenerator()
    
    # Test different themes
    themes = ["philosophical", "technical", "emotional"]
    
    for theme in themes:
        print(f"\nTesting theme: {theme}")
        tweet = generator.generate_tweet(theme)
        print(f"Generated tweet: {tweet}")
        print("-" * 50)  # Separator between tweets

if __name__ == "__main__":
    test_generation() 