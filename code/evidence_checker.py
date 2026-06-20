from data_loader import DataLoader


class EvidenceChecker:

    def __init__(self):
        loader = DataLoader()
        self.requirements = loader.load_evidence_requirements()

    def get_requirements(self, claim_object):

        rows = self.requirements[
            (self.requirements["claim_object"] == claim_object)
            |
            (self.requirements["claim_object"] == "all")
        ]

        return rows