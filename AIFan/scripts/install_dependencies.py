import subprocess
import sys

def install_in_order():
    """Install dependencies in specific order to avoid conflicts"""
    try:
        # First, install blockchain deps
        blockchain_deps = [
            "websockets==10.3",
            "solana==0.28.1",
            "anchorpy==0.14.0"
        ]
        for dep in blockchain_deps:
            subprocess.run([sys.executable, "-m", "pip", "install", dep], check=True)
            print(f"Installed {dep}")

        # Then install other dependencies
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], check=True)
        print("Successfully installed all dependencies!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error installing dependencies: {e}")
        return False

if __name__ == "__main__":
    install_in_order() 