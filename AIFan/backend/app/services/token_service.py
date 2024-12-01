from src.blockchain.token_tracking import TokenTracker
from src.blockchain.token_marketing import TokenMarketing
from fastapi import HTTPException
import os

class TokenService:
    def __init__(self):
        self.tracker = TokenTracker()
        self.marketing = TokenMarketing({
            "symbol": "AIFAN",
            "name": "AI Fan Token"
        })

    async def get_price(self):
        try:
            return await self.tracker.get_token_price()
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Price fetch failed: {str(e)}")

    async def get_holders(self):
        try:
            return await self.tracker.get_holder_stats()
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Holder stats failed: {str(e)}")

    async def generate_marketing_tweet(self):
        try:
            return await self.marketing.generate_launch_tweets()
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Tweet generation failed: {str(e)}") 