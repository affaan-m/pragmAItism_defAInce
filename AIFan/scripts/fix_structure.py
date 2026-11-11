import os
import shutil
from pathlib import Path

class ProjectFixer:
    def __init__(self):
        self.root = Path(__file__).parent.parent

    def fix_structure(self):
        print("Fixing project structure...")

        # 1. Create missing directories
        self.create_directories()
        
        # 2. Move files to correct locations
        self.move_files()
        
        # 3. Create missing files
        self.create_missing_files()
        
        # 4. Clean up duplicate/incorrect locations
        self.cleanup_duplicates()

    def create_directories(self):
        directories = [
            'frontend/src/pages',
            'frontend/src/styles',
            'frontend/public/images',
            'backend/src/agent',
            'backend/src/social',
            'backend/api',
        ]
        
        for dir_path in directories:
            full_path = self.root / dir_path
            full_path.mkdir(parents=True, exist_ok=True)
            print(f"Created directory: {dir_path}")

    def move_files(self):
        moves = {
            # Move components
            'pragmAItism/components/art-gallery.tsx': 'frontend/src/components/',
            'pragmAItism/app/providers.tsx': 'frontend/src/components/',
            'src/components/dashboard.tsx': 'frontend/src/components/',
            'src/components/digital-rain.tsx': 'frontend/src/components/',
            'src/components/analytics.tsx': 'frontend/src/components/',
            
            # Move configuration
            'src/lib/config.ts': 'frontend/src/lib/',
            
            # Move Python files
            'src/api/main.py': 'backend/api/',
        }
        
        for src, dest in moves.items():
            src_path = self.root / src
            dest_path = self.root / dest
            if src_path.exists():
                dest_path.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src_path, dest_path / src_path.name)
                print(f"Moved: {src} -> {dest}")

    def create_missing_files(self):
        # Create globals.css
        css_content = """
@tailwind base;
@tailwind components;
@tailwind utilities;

:root {
  --foreground-rgb: 255, 255, 255;
  --background-start-rgb: 0, 0, 0;
  --background-end-rgb: 0, 0, 0;
}

body {
  color: rgb(var(--foreground-rgb));
  background: linear-gradient(
    to bottom,
    transparent,
    rgb(var(--background-end-rgb))
  )
  rgb(var(--background-start-rgb));
}
"""
        with open(self.root / 'frontend/src/styles/globals.css', 'w') as f:
            f.write(css_content)
            print("Created: frontend/src/styles/globals.css")

        # Create ai_agent.py
        agent_content = """
from openai import OpenAI
import os
from dotenv import load_dotenv

class AIAgent:
    def __init__(self):
        load_dotenv()
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    def generate_response(self, prompt):
        try:
            response = self.client.chat.completions.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}]
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"Error generating response: {e}")
            return None
"""
        with open(self.root / 'backend/src/agent/ai_agent.py', 'w') as f:
            f.write(agent_content)
            print("Created: backend/src/agent/ai_agent.py")

        # Create twitter_bot.py
        bot_content = """
import tweepy
import os
from dotenv import load_dotenv

class TwitterBot:
    def __init__(self):
        load_dotenv()
        auth = tweepy.OAuthHandler(
            os.getenv("TWITTER_API_KEY"),
            os.getenv("TWITTER_API_SECRET")
        )
        auth.set_access_token(
            os.getenv("TWITTER_ACCESS_TOKEN"),
            os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
        )
        self.api = tweepy.API(auth)
    
    def post_tweet(self, text):
        try:
            self.api.update_status(text)
            return True
        except Exception as e:
            print(f"Error posting tweet: {e}")
            return False
"""
        with open(self.root / 'backend/src/social/twitter_bot.py', 'w') as f:
            f.write(bot_content)
            print("Created: backend/src/social/twitter_bot.py")

        # Create __init__.py files
        init_files = [
            'backend/api/__init__.py',
            'backend/src/agent/__init__.py',
            'backend/src/social/__init__.py',
        ]
        for init_file in init_files:
            with open(self.root / init_file, 'w') as f:
                f.write("")
            print(f"Created: {init_file}")

    def cleanup_duplicates(self):
        to_remove = [
            'src/frontend',
            'app',
            'pragmAItism'
        ]
        
        for path in to_remove:
            full_path = self.root / path
            if full_path.exists():
                if full_path.is_dir():
                    shutil.rmtree(full_path)
                else:
                    os.remove(full_path)
                print(f"Removed: {path}")

if __name__ == "__main__":
    fixer = ProjectFixer()
    fixer.fix_structure() 