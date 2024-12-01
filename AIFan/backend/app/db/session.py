from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import get_required_env
import os
from dotenv import load_dotenv

load_dotenv()

# Get Supabase database URL
SUPABASE_URL = get_required_env("SUPABASE_URL")
SUPABASE_KEY = get_required_env("SUPABASE_KEY")
DB_PASSWORD = get_required_env("SUPABASE_DB_PASSWORD")  # Add this to your .env

# Construct PostgreSQL connection URL
DATABASE_URL = f"postgresql://postgres:{DB_PASSWORD}@db.{SUPABASE_URL.replace('https://', '')}/postgres"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def init_db():
    from app.models.models import Base
    Base.metadata.create_all(bind=engine) 