from elevenlabs import clone, generate
import os

class VoiceGenerator:
    def __init__(self):
        self.api_key = os.getenv("ELEVENLABS_API_KEY")
        self.voice_id = None
        
    def create_voice_profile(self, name, files):
        """Create voice profile from sample files"""
        try:
            voice = clone(
                name=name,
                files=files,
                api_key=self.api_key
            )
            self.voice_id = voice.voice_id
            return self.voice_id
        except Exception as e:
            print(f"Error creating voice profile: {e}")
            return None
            
    def generate_speech(self, text):
        """Generate speech from text"""
        try:
            audio = generate(
                text=text,
                voice=self.voice_id,
                api_key=self.api_key
            )
            return audio
        except Exception as e:
            print(f"Error generating speech: {e}")
            return None 