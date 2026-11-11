import os
from dotenv import load_dotenv
import requests
import pandas as pd
from datetime import datetime, timedelta
import plotly.graph_objects as go

class TokenTracker:
    def __init__(self):
        load_dotenv()
        self.token_address = os.getenv("TOKEN_ADDRESS")
        self.birdeye_api_key = os.getenv("BIRDEYE_API_KEY")
        self.helius_api_key = os.getenv("HELIUS_API_KEY")
        
    def get_token_price(self):
        """Get current token price from Birdeye"""
        url = f"https://public-api.birdeye.so/public/price?address={self.token_address}"
        headers = {"x-api-key": self.birdeye_api_key}
        
        try:
            response = requests.get(url, headers=headers)
            data = response.json()
            return {
                "price": data["data"]["value"],
                "change_24h": data["data"]["priceChange24h"]
            }
        except Exception as e:
            print(f"Error getting price: {e}")
            return None
            
    def get_price_history(self, timeframe="24h"):
        """Get price history from Birdeye"""
        url = f"https://public-api.birdeye.so/public/history?address={self.token_address}&timeframe={timeframe}"
        headers = {"x-api-key": self.birdeye_api_key}
        
        try:
            response = requests.get(url, headers=headers)
            data = response.json()
            return pd.DataFrame(data["data"]["items"])
        except Exception as e:
            print(f"Error getting history: {e}")
            return None
            
    def get_token_holders(self):
        """Get token holder information"""
        url = f"https://api.helius.xyz/v0/token-metadata?api-key={self.helius_api_key}"
        
        try:
            response = requests.post(url, json={"mintAccounts": [self.token_address]})
            data = response.json()
            return data[0]["onChainMetadata"]["holders"]
        except Exception as e:
            print(f"Error getting holders: {e}")
            return None
            
    def create_price_chart(self, df):
        """Create interactive price chart"""
        fig = go.Figure()
        
        # Candlestick chart
        fig.add_trace(go.Candlestick(
            x=df['timestamp'],
            open=df['open'],
            high=df['high'],
            low=df['low'],
            close=df['close'],
            name='Price'
        ))
        
        # Volume bars
        fig.add_trace(go.Bar(
            x=df['timestamp'],
            y=df['volume'],
            name='Volume',
            yaxis='y2'
        ))
        
        fig.update_layout(
            title='Token Price History',
            yaxis_title='Price',
            yaxis2=dict(
                title='Volume',
                overlaying='y',
                side='right'
            ),
            xaxis_title='Date',
            height=600
        )
        
        return fig 