import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

print("=" * 80)
print("API KEY FOUND:", GEMINI_API_KEY is not None)
print("API PREFIX:", GEMINI_API_KEY[:10] if GEMINI_API_KEY else "NONE")
print("=" * 80)

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found")