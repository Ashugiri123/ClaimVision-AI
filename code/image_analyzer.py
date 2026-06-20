

import json
from pathlib import Path

from google import genai
from google.genai import types

from config import GEMINI_API_KEY


class ImageAnalyzer:

    def __init__(self):
        self.client = genai.Client(api_key=GEMINI_API_KEY)

    def analyze_image(self, image_path, conversation, claim_object):

        image = Path(__file__).parent.parent / "dataset" / image_path
       

        prompt = f"""
You are an insurance damage inspection AI.

Claim Object:
{claim_object}

Customer Conversation:
{conversation}

Analyze ONLY the uploaded image.

Return ONLY valid JSON.

Schema:

{{
    "valid_image": true,
    "issue_type": "",
    "object_part": "",
    "severity": "",
    "visible_damage": true,
    "reason": ""
}}

Rules:

- issue_type can be:
dent
scratch
crack
broken_part
water_damage
stain
torn_packaging
crushed_packaging
none
unknown

- severity:
none
low
medium
high
unknown

- If image is blurry or unrelated,
valid_image = false

Do not explain anything.

Return JSON only.
"""

        uploaded = self.client.files.upload(file=image)

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=[
                uploaded,
                prompt
            ],
            config=types.GenerateContentConfig(
                temperature=0
            )
        )

        print("\n========== RAW GEMINI RESPONSE ==========\n")
        print(response.text)
        print("\n=========================================\n")

        clean_json = (
            response.text
            .replace("```json", "")
            .replace("```", "")
            .strip()
        )

        return json.loads(clean_json)