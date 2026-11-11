from openai import OpenAI
import os
from dotenv import load_dotenv
import random
import requests
from PIL import Image
from io import BytesIO
import time

class TweetGenerator:
    def __init__(self):
        load_dotenv()
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.styler = TweetStyler()  # Your existing TweetStyler class
        
    def generate_image(self, tweet_text):
        """Generate an image based on tweet content"""
        try:
            # Create image prompt from tweet
            image_prompt = f"Create an abstract, artistic visualization of: {tweet_text}"
            
            response = self.client.images.generate(
                model="dall-e-3",
                prompt=image_prompt,
                size="1024x1024",
                quality="standard",
                n=1,
            )
            
            # Download and save image
            image_url = response.data[0].url
            response = requests.get(image_url)
            img = Image.open(BytesIO(response.content))
            
            # Save image
            os.makedirs('output/images', exist_ok=True)
            image_path = f'output/images/tweet_{int(time.time())}.png'
            img.save(image_path)
            
            return image_path
            
        except Exception as e:
            print(f"Error generating image: {e}")
            return None
            
    def generate_tweet_with_image(self):
        """Generate tweet with matching image"""
        tweet = self.generate_tweet()
        if tweet:
            image_path = self.generate_image(tweet)
            return tweet, image_path
        return None, None 