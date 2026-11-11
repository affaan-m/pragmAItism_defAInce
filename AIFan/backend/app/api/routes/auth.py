from fastapi import APIRouter, Depends
from app.services.auth_service import verify_wallet

router = APIRouter()

@router.post("/auth/wallet")
async def authenticate_wallet(signature: str, message: str):
    # Verify Solana wallet signature
    pass 