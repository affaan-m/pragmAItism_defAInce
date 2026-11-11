import subprocess
import sys
import os
from pathlib import Path

class Setup:
    def __init__(self):
        self.root_dir = Path(__file__).parent.parent
        
    def install_dependencies(self):
        """Install dependencies in the correct order"""
        try:
            # First, upgrade pip
            subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", "pip"], check=True)
            
            # Install core dependencies first
            core_deps = [
                "tweepy==4.14.0",
                "openai==1.3.0",
                "pyyaml==6.0.1",
                "schedule==1.2.0",
                "python-dotenv==1.0.0"
            ]
            subprocess.run([sys.executable, "-m", "pip", "install"] + core_deps, check=True)
            
            # Install Solana dependencies in correct order
            blockchain_deps = [
                "solana==0.28.1",
                "anchorpy==0.14.0"
            ]
            for dep in blockchain_deps:
                subprocess.run([sys.executable, "-m", "pip", "install", dep], check=True)
            
            # Install remaining dependencies
            subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], check=True)
            
            print("Successfully installed all dependencies!")
            return True
            
        except subprocess.CalledProcessError as e:
            print(f"Error installing dependencies: {e}")
            return False

    def setup_solana(self):
        """Setup Solana CLI tools"""
        try:
            # Check if Solana is installed
            subprocess.run(['solana', '--version'], capture_output=True)
            print("Solana CLI already installed")
        except FileNotFoundError:
            print("Installing Solana CLI...")
            install_script = 'sh -c "$(curl -sSfL https://release.solana.com/v1.17.0/install)"'
            subprocess.run(install_script, shell=True)
            
            # Add Solana to PATH
            home = str(Path.home())
            solana_path = f'{home}/.local/share/solana/install/active_release/bin'
            os.environ['PATH'] = f"{solana_path}:{os.environ['PATH']}"
            
            print("Please run: source ~/.zprofile")
            print("Then run this script again")
            sys.exit(0)

    def verify_installation(self):
        """Verify key packages are installed correctly"""
        try:
            import solana
            import anchorpy
            import streamlit
            print("Verification successful! All key packages are installed.")
            return True
        except ImportError as e:
            print(f"Verification failed: {e}")
            return False

def main():
    setup = Setup()
    
    print("Setting up development environment...")
    
    # Install dependencies
    if setup.install_dependencies():
        if setup.verify_installation():
            # Setup Solana
            setup.setup_solana()
            
            print("\nSetup complete! Next steps:")
            print("1. Update your .env file with API keys")
            print("2. Run 'solana-keygen new' to create a wallet")
            print("3. Start the app with 'streamlit run src/frontend/main.py'")
    else:
        print("\nSetup failed. Please check the error messages above.")

if __name__ == "__main__":
    main() 