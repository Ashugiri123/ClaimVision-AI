import os
from pathlib import Path

from dotenv import load_dotenv

# Locate the project root
BASE_DIR = Path(__file__).resolve().parent.parent

# Load the .env file
load_dotenv(BASE_DIR / ".env")

# Read the API key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env")