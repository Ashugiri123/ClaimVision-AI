from pathlib import Path
import pandas as pd


class DataLoader:
    def __init__(self):
        self.dataset_dir = Path(__file__).parent.parent / "dataset"

    def load_claims(self):
        return pd.read_csv(self.dataset_dir / "claims.csv")

    def load_sample_claims(self):
        return pd.read_csv(self.dataset_dir / "sample_claims.csv")

    def load_user_history(self):
        return pd.read_csv(self.dataset_dir / "user_history.csv")

    def load_evidence_requirements(self):
        return pd.read_csv(self.dataset_dir / "evidence_requirements.csv")