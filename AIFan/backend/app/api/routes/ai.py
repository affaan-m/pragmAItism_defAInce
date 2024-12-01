from fastapi import APIRouter, Depends, HTTPException
from app.services.openai_service import OpenAIService
from app.services.elevenlabs_service import ElevenLabsService
from app.models.schemas import GenerationRequest, GenerationResponse
from app.db.session import get_db
from sqlalchemy.orm import Session
from app.models.models import Generation
from typing import Optional
from fastapi.responses import StreamingResponse
import io

router = APIRouter()

@router.post("/generate/text", response_model=GenerationResponse)
async def generate_text(
    request: GenerationRequest,
    db: Session = Depends(get_db),
    openai_service: OpenAIService = Depends(OpenAIService)
):
    try:
        result = await openai_service.generate_text(request.prompt)
        
        # Save generation to database
        generation = Generation(
            user_id=request.user_id,
            type="text",
            prompt=request.prompt,
            result=result
        )
        db.add(generation)
        db.commit()
        
        return GenerationResponse(
            success=True,
            result=result,
            generation_id=generation.id
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/generate/image", response_model=GenerationResponse)
async def generate_image(
    request: GenerationRequest,
    db: Session = Depends(get_db),
    openai_service: OpenAIService = Depends(OpenAIService)
):
    try:
        image_url = await openai_service.generate_image(request.prompt)
        
        generation = Generation(
            user_id=request.user_id,
            type="image",
            prompt=request.prompt,
            result=image_url
        )
        db.add(generation)
        db.commit()
        
        return GenerationResponse(
            success=True,
            result=image_url,
            generation_id=generation.id
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/generate/voice")
async def generate_voice(
    request: GenerationRequest,
    db: Session = Depends(get_db),
    elevenlabs_service: ElevenLabsService = Depends(ElevenLabsService)
):
    try:
        audio_bytes = await elevenlabs_service.generate_voice(request.prompt)
        
        # Save metadata to database
        generation = Generation(
            user_id=request.user_id,
            type="voice",
            prompt=request.prompt,
            result="audio_generated"  # We store the audio in a separate storage service
        )
        db.add(generation)
        db.commit()
        
        return StreamingResponse(
            io.BytesIO(audio_bytes),
            media_type="audio/mpeg",
            headers={"Content-Disposition": f"attachment; filename=generation_{generation.id}.mp3"}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 