from pathlib import Path
import pandas as pd

VALID_STUDYTIME = {1, 2, 3, 4}

def clean_student_data(df: pd.DataFrame) -> pd.DataFrame:
    required = {"studytime", "G3"}
    missing_columns = required - set(df.columns)
    if missing_columns:
        raise ValueError(f"Missing required columns: {sorted(missing_columns)}")

    cleaned = df.drop_duplicates().copy()
    cleaned["studytime"] = pd.to_numeric(cleaned["studytime"], errors="coerce")
    cleaned["G3"] = pd.to_numeric(cleaned["G3"], errors="coerce")
    cleaned = cleaned.dropna(subset=["studytime", "G3"])
    cleaned = cleaned[
        cleaned["studytime"].isin(VALID_STUDYTIME)
        & cleaned["G3"].between(0, 20)
    ].copy()
    cleaned["studytime"] = cleaned["studytime"].astype(int)
    cleaned["G3"] = cleaned["G3"].astype(int)
    return cleaned

def load_uci_math_csv(path: str | Path) -> pd.DataFrame:
    # UCI student-mat.csv is semicolon-separated.
    return pd.read_csv(path, sep=";")
