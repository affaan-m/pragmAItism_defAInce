from fastapi import APIRouter, Depends, HTTPException
from app.db.session import get_db
from sqlalchemy.orm import Session
from app.services.solana_service import SolanaService
from app.services.token_service import TokenService
from typing import Optional

router = APIRouter()

@router.get("/token/price")
async def get_token_price(
    db: Session = Depends(get_db),
    token_service: TokenService = Depends(TokenService)
):
    try:
        price_data = await token_service.get_price()
        return price_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/token/holders")
async def get_token_holders(
    db: Session = Depends(get_db),
    token_service: TokenService = Depends(TokenService)
):
    try:
        holders = await token_service.get_holders()
        return holders
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/token/transfer")
async def transfer_tokens(
    recipient: str,
    amount: float,
    solana_service: SolanaService = Depends(SolanaService)
):
    try:
        tx = await solana_service.transfer_tokens(recipient, amount)
        return {"success": True, "transaction": tx}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 