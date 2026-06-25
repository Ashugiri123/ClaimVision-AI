import json
import time
from pathlib import Path

from google import genai
from google.genai import types

from config import GEMINI_API_KEY


class ImageAnalyzer:

    def __init__(self):
        self.client = genai.Client(api_key=GEMINI_API_KEY)

    def _build_prompt(self, conversation, claim_object):

        return f"""
You are an insurance damage inspection AI.

Claim Object:
{claim_object}

Customer Conversation:
{conversation}

Analyze ONLY the uploaded insurance claim image.

Compare the visible damage with the customer's description.

Do not guess anything that is not visible.

If the conversation and image contradict each other, mention the contradiction in the reason.

If the uploaded image is not related to the selected claim object, mark valid_image as false.

Return ONLY valid JSON.

Schema:

{{
    "valid_image": true,
    "issue_type": "",
    "object_part": "",
    "severity": "",
    "visible_damage": true,
    "confidence": 0,
    "multiple_damages": false,
    "fraud_suspicion": "low",
    "recommended_action": "",
    "reason": ""
}}

Decision Rules:

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
Additional Rules:

- confidence must be an integer from 0 to 100.

- multiple_damages should be true if more than one damaged area is visible.

- fraud_suspicion must be one of:
low
medium
high

- recommended_action must be one of:
Approve Claim
Reject Claim
Manual Review

- Only use visible evidence from the image.
- Never assume damage that cannot be seen.
- If the image quality is poor, recommend Manual Review.
- If damage contradicts the customer's description, mention it in the reason.

- severity:
none
low
medium
high
unknown

- If image is blurry or unrelated,
valid_image = false

Important:

Think like a professional insurance surveyor.

Never exaggerate damage.

Never assume hidden damage.

Base every decision only on visible evidence.

Use conservative judgement.
Return JSON only.
"""

    def analyze_image(self, image_path, conversation, claim_object):

        image = Path(__file__).parent.parent / "dataset" / image_path

        uploaded = self.client.files.upload(file=image)

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=[
                uploaded,
                self._build_prompt(conversation, claim_object)
            ],
            config=types.GenerateContentConfig(
                temperature=0
            )
        )

        clean_json = (
            response.text
            .replace("```json", "")
            .replace("```", "")
            .strip()
        )

        return json.loads(clean_json)

    def analyze_uploaded_image(
    self,
    uploaded_file,
    conversation,
    claim_object
    ):

        for attempt in range(3):

            try:

                response = self.client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=[
                        types.Part.from_bytes(
                            data=uploaded_file.getvalue(),
                            mime_type=uploaded_file.type
                        ),
                        self._build_prompt(conversation, claim_object)
                    ],
                    config=types.GenerateContentConfig(
                        temperature=0
                    )
                )
                print("=" * 80)
                print(response.text)
                print("=" * 80)
                clean_json = (
                    response.text
                    .replace("```json", "")
                    .replace("```", "")
                    .strip()
                )

                return json.loads(clean_json)

            except json.JSONDecodeError:

                if attempt == 2:
                    raise Exception("Gemini returned invalid JSON.")

                time.sleep(2)

            except Exception as e:

                error = str(e)

                if "429" in error or "503" in error:

                    if attempt == 2:
                        raise Exception(
                            "Gemini is currently unavailable. Please try again in a few moments."
                        )

                    time.sleep(5)

                else:
                    raise Exception(error)