from src.blockchain.solana_client import SolanaClient
from fastapi import HTTPException
import os

class SolanaService:
    def __init__(self):
        self.client = SolanaClient(
            private_key=os.getenv("SOLANA_WALLET_PRIVATE_KEY"),
            rpc_url=os.getenv("RPC_URL")
        )

    async def transfer_tokens(self, recipient: str, amount: float) -> str:
        try:
            tx = await self.client.transfer_tokens(recipient, amount)
            return tx
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Transfer failed: {str(e)}")

    async def get_balance(self, address: str) -> float:
        try:
            balance = await self.client.get_balance(address)
            return balance
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Balance check failed: {str(e)}") 