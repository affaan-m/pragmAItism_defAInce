import os
from pathlib import Path
import sys

class ProjectVerifier:
    def __init__(self):
        self.root = Path(__file__).parent.parent
        self.issues = []
        
        # Define expected structure
        self.expected_structure = {
            'frontend': {
                'public': ['images'],
                'src': {
                    'components': [
                        'digital-rain.tsx',
                        'dashboard.tsx',
                        'tweet-generator.tsx',
                        'glitch-text.tsx',
                        'analytics.tsx',
                        'token-stats.tsx'
                    ],
                    'lib': ['config.ts'],
                    'pages': ['_app.tsx', 'index.tsx'],
                    'styles': ['globals.css'],
                    'types': ['index.d.ts']
                },
                'files': [
                    'next.config.js',
                    'package.json',
                    'tsconfig.json',
                    '.eslintrc.json'
                ]
            },
            'backend': {
                'src': {
                    'agent': [
                        '__init__.py',
                        'ai_agent.py',
                        'personality.py',
                        'train_personality.py'
                    ],
                    'blockchain': [
                        '__init__.py',
                        'solana_client.py',
                        'raydium_client.py'
                    ],
                    'social': [
                        '__init__.py',
                        'twitter_bot.py',
                        'twitter_client.py',
                        'database.py'
                    ]
                },
                'api': [
                    '__init__.py',
                    'main.py'
                ],
                'files': [
                    'requirements.txt'
                ]
            }
        }

    def check_directory(self, current_path, structure):
        """Recursively check directory structure"""
        if not current_path.exists():
            self.issues.append(f"Missing directory: {current_path}")
            return

        # Check directories
        for dir_name, contents in structure.items():
            if dir_name != 'files':
                dir_path = current_path / dir_name
                if isinstance(contents, list):
                    if not dir_path.exists():
                        self.issues.append(f"Missing directory: {dir_path}")
                    else:
                        for file_name in contents:
                            file_path = dir_path / file_name
                            if not file_path.exists():
                                self.issues.append(f"Missing file: {file_path}")
                else:
                    self.check_directory(dir_path, contents)

        # Check files
        if 'files' in structure:
            for file_name in structure['files']:
                file_path = current_path / file_name
                if not file_path.exists():
                    self.issues.append(f"Missing file: {file_path}")

    def check_for_duplicates(self):
        """Check for duplicate files and incorrect locations"""
        # Check for duplicate frontend implementations
        streamlit_files = list(self.root.glob("**/streamlit*.py"))
        if streamlit_files:
            self.issues.append(f"Found Streamlit files that should be removed: {streamlit_files}")

        # Check for files in wrong locations
        wrong_locations = [
            "src/frontend",
            "app",
            "pragmAItism"
        ]
        for location in wrong_locations:
            path = self.root / location
            if path.exists():
                self.issues.append(f"Found files in incorrect location: {location}")

    def verify(self):
        """Run all verifications"""
        print("Verifying project structure...")
        
        # Check main structure
        for main_dir, structure in self.expected_structure.items():
            self.check_directory(self.root / main_dir, structure)
        
        # Check for duplicates and wrong locations
        self.check_for_duplicates()
        
        # Report results
        if self.issues:
            print("\n❌ Found issues:")
            for issue in self.issues:
                print(f"  - {issue}")
            print("\nSuggested fixes:")
            self.suggest_fixes()
        else:
            print("\n✅ Project structure is correct!")

    def suggest_fixes(self):
        """Suggest fixes for common issues"""
        print("\nTo fix these issues:")
        print("1. Run the cleanup script first:")
        print("   python scripts/cleanup.py")
        print("\n2. Manually verify these locations:")
        print("   - frontend/public/images/ (should contain all images)")
        print("   - frontend/src/components/ (should contain all React components)")
        print("   - backend/src/ (should contain all Python code)")
        print("\n3. Remove any duplicate implementations:")
        print("   - Delete src/frontend/")
        print("   - Delete app/")
        print("   - Delete pragmAItism/")
        print("\n4. Create any missing files noted above")

if __name__ == "__main__":
    verifier = ProjectVerifier()
    verifier.verify() 