#!/usr/bin/env python3
"""
Setup script for Pong Game
"""

import subprocess
import sys
import os

def install_requirements():
    """Install Python dependencies"""
    print("Installing Python dependencies...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✓ Dependencies installed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ Error installing dependencies: {e}")
        return False

def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 7):
        print("✗ Python 3.7 or higher is required!")
        return False
    print(f"✓ Python {sys.version_info.major}.{sys.version_info.minor} detected")
    return True

def main():
    print("=== Pong Game Setup ===\n")
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Install dependencies
    if not install_requirements():
        sys.exit(1)
    
    print("\n=== Setup Complete! ===")
    print("\nNext steps:")
    print("1. Run the game: python pong_game.py")
    print("2. Analyze game statistics: python game_stats.py")
    print("3. Read the README.md for more information")
    print("\nHave fun playing Pong!")

if __name__ == "__main__":
    main() 