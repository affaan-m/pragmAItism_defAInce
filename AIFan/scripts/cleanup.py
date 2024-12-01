import os
import shutil
from pathlib import Path

def cleanup_project():
    # Project root directory
    root = Path(__file__).parent.parent
    
    # Create new directory structure
    directories = [
        'frontend/public/images',
        'frontend/src/components',
        'frontend/src/lib',
        'frontend/src/types',
        'frontend/src/styles',
        'backend/src/agent',
        'backend/src/blockchain',
        'backend/src/social',
        'backend/api',
        'shared/types',
    ]
    
    for dir_path in directories:
        os.makedirs(root / dir_path, exist_ok=True)
    
    # Move frontend files
    frontend_moves = {
        'src/components/*.tsx': 'frontend/src/components/',
        'app/globals.css': 'frontend/src/styles/',
        'app/layout.tsx': 'frontend/src/pages/',
        'app/page.tsx': 'frontend/src/pages/',
        'app/providers.tsx': 'frontend/src/components/',
        'pragmAItism/public/images/*': 'frontend/public/images/',
    }
    
    # Move backend files
    backend_moves = {
        'src/agent/*': 'backend/src/agent/',
        'src/blockchain/*': 'backend/src/blockchain/',
        'src/social/*': 'backend/src/social/',
        'src/api/*': 'backend/api/',
    }
    
    # Files to delete (duplicates or obsolete)
    files_to_delete = [
        'src/frontend/main.py',
        'src/frontend/token_management.py',
        'src/frontend/__init__.py',
        'app',
        'pragmAItism',
    ]
    
    try:
        # Execute moves
        for source_pattern, dest_dir in {**frontend_moves, **backend_moves}.items():
            for source in root.glob(source_pattern):
                if source.exists():
                    dest = root / dest_dir / source.name
                    if not dest.exists():
                        shutil.move(str(source), str(dest))
                        print(f"Moved {source} to {dest}")
        
        # Delete obsolete files
        for file_path in files_to_delete:
            full_path = root / file_path
            if full_path.exists():
                if full_path.is_dir():
                    shutil.rmtree(full_path)
                else:
                    os.remove(full_path)
                print(f"Deleted {file_path}")
        
        print("Cleanup completed successfully!")
        
    except Exception as e:
        print(f"Error during cleanup: {e}")

if __name__ == "__main__":
    cleanup_project() 