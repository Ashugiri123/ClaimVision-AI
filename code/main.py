import pandas as pd

from config import GEMINI_API_KEY
from data_loader import DataLoader
from claim_parser import ClaimParser
from image_analyzer import ImageAnalyzer
from evidence_checker import EvidenceChecker
from history_checker import HistoryChecker
from decision_engine import DecisionEngine


def main():

    print("=" * 60)
    print("Processing Claims")
    print("=" * 60)

    loader = DataLoader()

    claims = loader.load_claims()

    analyzer = ImageAnalyzer()
    evidence_checker = EvidenceChecker()
    history_checker = HistoryChecker()
    decision_engine = DecisionEngine()

    output_rows = []

    total = len(claims)

    for index, row in claims.iterrows():

        print(f"Processing {index + 1}/{total}")

        conversation = row["user_claim"]

        clean_text = ClaimParser.clean_conversation(conversation)

        claim_object = row["claim_object"]

        image_paths = row["image_paths"].split(";")

        image_path = image_paths[0]

        import time

        while True:
            try:
                gemini = analyzer.analyze_image(
                    image_path=image_path,
                    conversation=clean_text,
                    claim_object=claim_object
                )
                break

            except Exception as e:
                print(e)

                if "429" in str(e):
                    print("Quota exceeded. Waiting 40 seconds...")
                    time.sleep(40)
                else:
                    raise
           
        


        history = history_checker.get_user_history(
            row["user_id"]
        )

        history = history_checker.get_user_history(
            row["user_id"]
        )

        evidence = evidence_checker.check_evidence(
            claim_object,
            uploaded_images=len(image_paths)
        )

        decision = decision_engine.decide(
            gemini,
            history,
            evidence
        )

        output_rows.append({

            "evidence_standard_met":
                decision["evidence_standard_met"],

            "evidence_standard_met_reason":
                gemini["reason"],

            "risk_flags":
                "none",

            "issue_type":
                decision["issue_type"],

            "object_part":
                decision["object_part"],

            "claim_status":
                decision["claim_status"],

            "claim_status_justification":
                decision["claim_status_justification"],

            "supporting_image_ids":
                image_paths[0].split("/")[-1].replace(".jpg", ""),

            "valid_image":
                str(gemini["valid_image"]).lower(),

            "severity":
                decision["severity"]

        })

    output = pd.DataFrame(output_rows)

    output.to_csv(
        "output.csv",
        index=False
    )

    print("\n")
    print("=" * 60)
    print("SUCCESS")
    print("=" * 60)
    print("output.csv generated successfully")


if __name__ == "__main__":
    main()