from openai import OpenAI
import random
import os
from dotenv import load_dotenv

class TweetInteraction:
    def __init__(self):
        load_dotenv()
        self.openai = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.interaction_types = ["reply", "quote", "like", "retweet"]
        
    def should_interact(self, tweet):
        """Decide if we should interact with a tweet"""
        # Check tweet content relevance
        relevant_topics = ["AI", "ML", "crypto", "philosophy", "tech", "coding"]
        return any(topic.lower() in tweet.text.lower() for topic in relevant_topics)
        
    def generate_reply(self, tweet):
        """Generate a contextual reply"""
        prompt = f"""Tweet: {tweet.text}
        Generate a thoughtful reply that:
        1. Shows deep understanding
        2. Adds value to the conversation
        3. Maintains my philosophical-technical style
        4. May include relevant emojis
        Reply:"""
        
        try:
            response = self.openai.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are Affaan, a deep thinker who combines technical AI concepts with philosophical musings."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=100,
                temperature=0.9
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            print(f"Error generating reply: {e}")
            return None
            
    def decide_interaction(self, tweet):
        """Decide how to interact with a tweet"""
        if not self.should_interact(tweet):
            return None, None
            
        interaction = random.choice(self.interaction_types)
        
        if interaction == "reply":
            reply_text = self.generate_reply(tweet)
            return "reply", reply_text
        elif interaction == "quote":
            quote_text = self.generate_reply(tweet)
            return "quote", quote_text
        else:
            return interaction, None 