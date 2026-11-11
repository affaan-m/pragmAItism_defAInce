from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text
from sqlalchemy.sql import func
from app.db.base import Base

class User(Base):
    __tablename__ = "users"
    __table_args__ = {'schema': 'public'}
    
    id = Column(Integer, primary_key=True)
    wallet_address = Column(String, unique=True)
    twitter_handle = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
class Generation(Base):
    __tablename__ = "generations"
    __table_args__ = {'schema': 'public'}
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("public.users.id"))
    type = Column(String)  # "text", "image", or "voice"
    prompt = Column(Text)
    result = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now()) 