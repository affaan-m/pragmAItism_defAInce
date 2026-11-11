from elevenlabs import Voice, VoiceSettings, generate, play, stream, save
import os
from fastapi import HTTPException

class ElevenLabsService:
    def __init__(self):
        self.api_key = os.getenv("ELEVENLABS_API_KEY")
        if not self.api_key:
            raise ValueError("ELEVENLABS_API_KEY not found in environment variables")
        
        os.environ["ELEVEN_API_KEY"] = self.api_key

    async def generate_voice(self, text: str) -> bytes:
        try:
            voice = Voice(
                voice_id="21m00Tcm4TlvDq8ikWAM",  # Default voice ID (Rachel)
                settings=VoiceSettings(stability=0.5, similarity_boost=0.75)
            )
            
            audio = generate(
                text=text,
                voice=voice,
                model="eleven_monolingual_v1"
            )
            
            return audio
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Voice generation failed: {str(e)}") 