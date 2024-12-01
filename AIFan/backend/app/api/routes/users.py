from fastapi import APIRouter, Depends, HTTPException
from app.db.database import get_supabase
from supabase import Client
from typing import List

router = APIRouter()

@router.get("/users")
async def get_users(supabase: Client = Depends(get_supabase)):
    try:
        response = supabase.table('users').select("*").execute()
        return response.data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/users")
async def create_user(user_data: dict, supabase: Client = Depends(get_supabase)):
    try:
        response = supabase.table('users').insert(user_data).execute()
        return response.data[0]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 