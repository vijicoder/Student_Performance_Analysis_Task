from pathlib import Path
import sys
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import spearmanr, kendalltau
from pipeline import clean_student_data, load_uci_math_csv

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw" / "student-mat.csv"
PROCESSED = ROOT / "data" / "processed"
REPORTS = ROOT / "reports"

def main():
    if not RAW.exists():
        sys.exit(
            "Dataset not found. Download student-mat.csv from the official UCI "
            "Student Performance page and place it in data/raw/."
        )

    original = load_uci_math_csv(RAW)
    cleaned = clean_student_data(original)
    PROCESSED.mkdir(parents=True, exist_ok=True)
    REPORTS.mkdir(parents=True, exist_ok=True)
    cleaned.to_csv(PROCESSED / "student-mat-cleaned.csv", index=False)

    rho, p_spearman = spearmanr(cleaned["studytime"], cleaned["G3"], alternative="greater")
    tau, p_kendall = kendalltau(cleaned["studytime"], cleaned["G3"], variant="b", alternative="greater")

    summary = [
        "Student Performance Analysis",
        f"Rows in original dataset: {len(original)}",
        f"Rows in cleaned dataset: {len(cleaned)}",
        f"Rows excluded: {len(original) - len(cleaned)}",
        f"Spearman rho: {rho:.4f}",
        f"Spearman one-sided p-value: {p_spearman:.6g}",
        f"Kendall tau-b: {tau:.4f}",
        f"Kendall one-sided p-value: {p_kendall:.6g}",
        "Interpretation: association only; this observational analysis does not establish causation.",
    ]
    (REPORTS / "analysis_summary.txt").write_text("\n".join(summary), encoding="utf-8")

    plt.figure(figsize=(7, 5))
    jitter = cleaned["studytime"] + 0  # keep categories unchanged in analysis
    plt.scatter(jitter, cleaned["G3"], alpha=0.45)
    plt.xlabel("Weekly study-time category (1–4)")
    plt.ylabel("Final mathematics grade (G3, 0–20)")
    plt.title("Study-time category and final mathematics grade")
    plt.xticks([1, 2, 3, 4])
    plt.tight_layout()
    plt.savefig(REPORTS / "studytime_vs_G3.png", dpi=150)
    print("\n".join(summary))

if __name__ == "__main__":
    main()
