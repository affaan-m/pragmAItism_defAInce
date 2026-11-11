from solana.rpc.api import Client
from solana.transaction import Transaction
from solana.system_program import create_account, CreateAccountParams
from spl.token.instructions import (
    initialize_mint, InitializeMintParams,
    create_associated_token_account,
    mint_to, MintToParams
)
import os
from dotenv import load_dotenv
import base58

load_dotenv()

class SolanaClient:
    def __init__(self):
        self.client = Client(os.getenv("RPC_URL"))
        self.wallet_private_key = os.getenv("WALLET_PRIVATE_KEY")
        self.wallet_public_key = os.getenv("WALLET_PUBLIC_KEY")
        self.helius_api_key = os.getenv("HELIUS_API_KEY")
        
    def create_token(self, name, symbol, decimals=9, initial_supply=1000000000):
        """Create a new Solana token"""
        try:
            # Create mint account
            mint_account = create_account(
                CreateAccountParams(
                    from_pubkey=self.wallet_public_key,
                    lamports=self.client.get_minimum_balance_for_rent_exemption()["result"],
                    space=82,
                    program_id=TOKEN_PROGRAM_ID
                )
            )
            
            # Initialize mint
            init_mint_ix = initialize_mint(
                InitializeMintParams(
                    mint=mint_account.pubkey(),
                    decimals=decimals,
                    mint_authority=self.wallet_public_key,
                    freeze_authority=self.wallet_public_key
                )
            )
            
            # Create associated token account
            ata = create_associated_token_account(
                payer=self.wallet_public_key,
                owner=self.wallet_public_key,
                mint=mint_account.pubkey()
            )
            
            # Mint initial supply
            mint_to_ix = mint_to(
                MintToParams(
                    mint=mint_account.pubkey(),
                    dest=ata,
                    mint_authority=self.wallet_public_key,
                    amount=initial_supply * (10 ** decimals)
                )
            )
            
            # Build and send transaction
            transaction = Transaction()
            transaction.add(init_mint_ix)
            transaction.add(mint_to_ix)
            
            result = self.client.send_transaction(
                transaction,
                self.wallet_private_key
            )
            
            return {
                "success": True,
                "mint_address": str(mint_account.pubkey()),
                "transaction_id": result["result"]
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }
    
    def get_token_balance(self, token_address):
        """Get token balance for wallet"""
        try:
            balance = self.client.get_token_account_balance(token_address)
            return {
                "success": True,
                "balance": balance["result"]["value"]["uiAmount"]
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }
    
    def get_token_price(self, token_address):
        """Get token price using Birdeye API"""
        import requests
        
        url = f"https://public-api.birdeye.so/public/price?address={token_address}"
        headers = {"X-API-KEY": os.getenv("BIRDEYE_API_KEY")}
        
        try:
            response = requests.get(url, headers=headers)
            data = response.json()
            return {
                "success": True,
                "price": data["data"]["value"]
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }
        
    def transfer_tokens(self, to_address, amount):
        # Transfer tokens
        pass 
    
    def create_liquidity_pool(self, token_mint, initial_sol_amount, initial_token_amount):
        """Create liquidity pool on Raydium"""
        try:
            # Implementation for creating LP on Raydium
            pass
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }
