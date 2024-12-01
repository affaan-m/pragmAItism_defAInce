from openai import OpenAI
import requests
from PIL import Image
from io import BytesIO

class AvatarGenerator:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        
    def generate_avatar(self, description):
        """Generate AI avatar"""
        try:
            response = self.client.images.generate(
                model="dall-e-3",
                prompt=f"Create a professional, artistic avatar: {description}",
                size="1024x1024",
                quality="hd",
                n=1,
            )
            
            image_url = response.data[0].url
            response = requests.get(image_url)
            img = Image.open(BytesIO(response.content))
            
            os.makedirs('output/avatars', exist_ok=True)
            avatar_path = f'output/avatars/avatar_{int(time.time())}.png'
            img.save(avatar_path)
            
            return avatar_path
            
        except Exception as e:
            print(f"Error generating avatar: {e}")
            return None 