import sys
from pathlib import Path
import unittest
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from pipeline import clean_student_data

class TestSyntheticPipeline(unittest.TestCase):
    def test_cleaning_keeps_valid_rows_and_removes_invalid_rows(self):
        synthetic = pd.DataFrame({
            "studytime": [1, 2, 4, None, 5, 3, 2],
            "G3": [10, 15, 18, 12, 14, 25, 15]
        })
        result = clean_student_data(synthetic)
        self.assertEqual(len(result), 3)
        self.assertEqual(result["studytime"].tolist(), [1, 2, 4])
        self.assertEqual(result["G3"].tolist(), [10, 15, 18])

    def test_missing_required_column_raises_error(self):
        with self.assertRaises(ValueError):
            clean_student_data(pd.DataFrame({"studytime": [1, 2]}))

if __name__ == "__main__":
    unittest.main()
