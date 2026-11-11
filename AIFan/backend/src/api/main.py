from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from ..social.tweet_generator import generate_personality_tweet
from ..blockchain.token_tracking import TokenTracker
from ..social.twitter_client import TwitterClient

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/generate-tweet")
async def generate_tweet():
    tweet = generate_personality_tweet()
    return {"tweet": tweet}

@app.post("/api/post-tweet")
async def post_tweet(tweet: str):
    client = TwitterClient()
    success = client.post_tweet(tweet)
    return {"success": success}

@app.get("/api/token-stats")
async def get_token_stats():
    tracker = TokenTracker()
    stats = tracker.get_token_price()
    return stats