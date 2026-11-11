import os
from dotenv import load_dotenv

load_dotenv()

def get_required_env(key: str) -> str:
    value = os.getenv(key)
    if value is None:
        raise ValueError(f"{key} not found in environment variables")
    return value

# Supabase
SUPABASE_URL = get_required_env("SUPABASE_URL")
SUPABASE_KEY = get_required_env("SUPABASE_KEY")
SUPABASE_SERVICE_ROLE = get_required_env("SUPABASE_SERVICE_ROLE")

# AI Services
OPENAI_API_KEY = get_required_env("OPENAI_API_KEY")
ELEVENLABS_API_KEY = get_required_env("ELEVENLABS_API_KEY")

# Frontend
FRONTEND_URL = os.getenv("FRONTEND_URL", "http://localhost:3000")

# Database
DATABASE_URL = get_required_env("DATABASE_URL") 