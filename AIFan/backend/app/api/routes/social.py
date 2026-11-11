from fastapi import APIRouter, Depends
from app.services.twitter_service import TwitterService
from app.db.session import get_db
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/tweet/generate")
async def generate_tweet(db: Session = Depends(get_db)):
    twitter_service = TwitterService()
    tweet = await twitter_service.generate_tweet()
    return {"tweet": tweet}

@router.post("/tweet/post")
async def post_tweet(tweet: str, db: Session = Depends(get_db)):
    twitter_service = TwitterService()
    success = await twitter_service.post_tweet(tweet)
    return {"success": success} 