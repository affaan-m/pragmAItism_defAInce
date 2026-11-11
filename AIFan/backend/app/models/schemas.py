from pydantic import BaseModel
from typing import Optional

class GenerationRequest(BaseModel):
    prompt: str
    user_id: int
    
class GenerationResponse(BaseModel):
    success: bool
    result: str
    generation_id: int 