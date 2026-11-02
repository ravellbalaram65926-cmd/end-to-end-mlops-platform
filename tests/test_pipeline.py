import unittest
from pathlib import Path

from src.main import build_features


class ChurnPipelineTests(unittest.TestCase):
    def test_features_are_normalized_and_deduplicated(self):
        sample = Path(__file__).resolve().parents[1] / "data/raw/sample_churn.csv"
        rows = build_features(sample)
        self.assertEqual(len(rows), 5)
        self.assertEqual(rows[0]["churn_label"], "1")
        self.assertEqual(rows[0]["tenure_bucket"], "new")
        self.assertEqual(rows[1]["tenure_bucket"], "established")


if __name__ == "__main__":
    unittest.main()
