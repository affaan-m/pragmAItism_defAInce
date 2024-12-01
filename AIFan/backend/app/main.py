from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import ai, auth, social, blockchain
from app.db.session import engine, init_db
from app.models import models
import os
from supabase import create_client, Client

# Initialize Supabase client
supabase: Client = create_client(
    os.getenv("SUPABASE_URL"),
    os.getenv("SUPABASE_KEY")
)

# Create database tables
init_db()

app = FastAPI(title="AIFan API")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[os.getenv("FRONTEND_URL", "http://localhost:3000")],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(ai.router, prefix="/api/v1/ai", tags=["AI"])
app.include_router(auth.router, prefix="/api/v1/auth", tags=["Auth"])
app.include_router(social.router, prefix="/api/v1/social", tags=["Social"])
app.include_router(blockchain.router, prefix="/api/v1/blockchain", tags=["Blockchain"])

@app.get("/")
async def root():
    return {"message": "Welcome to AIFan API"} 