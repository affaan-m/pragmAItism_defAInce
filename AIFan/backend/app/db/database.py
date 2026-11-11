from supabase import create_client, Client
from app.core.config import get_required_env

supabase_url = get_required_env("SUPABASE_URL")
supabase_key = get_required_env("SUPABASE_KEY")

supabase: Client = create_client(supabase_url, supabase_key)

def get_supabase() -> Client:
    return supabase 