# Student Performance Analysis Using Python and R

## Research objective
Investigate whether weekly study-time category (`studytime`) is associated with final mathematics grade (`G3`) in the UCI Student Performance Mathematics dataset.

This is an observational analysis. An association does not establish that study time causes a change in grades.

## Dataset
- Source: UCI Machine Learning Repository, Student Performance
- File: `student-mat.csv`
- Expected separator: semicolon (`;`)
- Main variables: `studytime` (ordinal categories 1–4), `G3` (final grade, 0–20)
- Official dataset page: https://archive.ics.uci.edu/dataset/320/student+performance

Download `student-mat.csv` from the official source and place it in `data/raw/`. Do not edit the original file.

## Project structure
- `data/raw/`: original downloaded dataset (not committed by default)
- `data/interim/`: intermediate outputs
- `data/processed/`: cleaned analysis data
- `notebooks/`: analysis notebooks
- `src/`: Python analysis and synthetic pipeline
- `R/`: R analysis and synthetic pipeline test
- `reports/`: generated reports and test evidence
- `preregistration.md`: analysis plan written before inspecting the relationship
- `requirements.txt`: pinned Python dependencies

## Setup (Python)
```bash
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
```

## Run the synthetic pipeline test first
```bash
python -m unittest discover -s tests -v
```
This test uses generated example data only. It does not use real student records and is not evidence of a research finding.

## Run the real-data analysis
1. Download `student-mat.csv` from the official UCI page.
2. Save it as `data/raw/student-mat.csv`.
3. Run:
```bash
python src/analyze.py
```
4. Run the R equivalent from the project root:
```bash
Rscript R/analyze.R
```

Outputs are written to `data/processed/` and `reports/`.

## Reproducibility notes
Record your Python and R versions and package versions when you run the project. If your actual installed versions differ from the pinned Python requirements, update the environment record and document the change. Keep any changes to the preregistered analysis in the `Deviations` section with a date and reason.

## Privacy
The dataset is a public educational dataset. Do not add private student records or personally identifying information to this repository.
