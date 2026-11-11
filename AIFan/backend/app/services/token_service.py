from src.blockchain.token_tracking import TokenTracker
from fastapi import HTTPException
import os

class TokenService:
    def __init__(self):
        self.tracker = TokenTracker()

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

