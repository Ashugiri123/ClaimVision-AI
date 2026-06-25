from data_loader import DataLoader


class EvidenceChecker:

    def __init__(self):
        loader = DataLoader()
        self.requirements = loader.load_evidence_requirements()

    def check_evidence(self, claim_object, uploaded_images=1):

        rows = self.requirements[
            (self.requirements["claim_object"] == claim_object)
            | (self.requirements["claim_object"] == "all")
        ]

        if rows.empty:

            return {
                "evidence_complete": True,
                "missing_evidence": "None",
                "requirements": []
            }

        return {
            "evidence_complete": uploaded_images >= 1,
            "missing_evidence": "None" if uploaded_images >= 1 else "Upload at least one image.",
            "requirements": rows["minimum_image_evidence"].tolist()
        }