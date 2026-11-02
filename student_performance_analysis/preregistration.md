# Analysis Preregistration

## Research question
Is there an association between students' weekly study-time category (`studytime`) and their final mathematics grade (`G3`) in the UCI Student Performance Mathematics dataset?

## Hypotheses
- **Null hypothesis (H0):** There is no monotonic association between weekly study-time category and final mathematics grade in the target sample (Spearman's rho = 0).
- **Alternative hypothesis (H1):** There is a positive monotonic association between weekly study-time category and final mathematics grade (Spearman's rho > 0).

A positive direction is specified in advance. The primary test will be one-sided at alpha = 0.05. The estimate and a 95% confidence interval will also be reported. If the software used cannot calculate a suitable interval directly, the limitation and method will be documented.

## Population, sample, and exclusions
- **Target population:** Students similar to those represented by the two Portuguese schools in the source dataset; findings should not be generalized automatically to all students.
- **Dataset sample:** All records in the UCI Mathematics file (`student-mat.csv`) that meet the eligibility rules below.
- **Unit of analysis:** One student record.
- **Inclusion rules:** Records with valid `studytime` values in {1, 2, 3, 4} and valid `G3` values in the documented grade range 0–20.
- **Exclusion rules:** Exact duplicate rows; records with missing or invalid values in either primary variable. Counts and reasons will be reported.
- **Stopping rule:** Use all eligible records in the downloaded Mathematics file; no optional stopping or additional data collection.

## Variables and measures
- **Predictor:** `studytime`, an ordinal category: 1 = less than 2 hours; 2 = 2–5 hours; 3 = 5–10 hours; 4 = more than 10 hours of weekly study time.
- **Outcome:** `G3`, final mathematics grade, on a 0–20 scale.
- **Controls:** No covariates are included in the primary analysis. This is a bivariate association analysis.
- **Transformations:** Retain the original ordinal category codes and grade values. Do not interpret category codes as exact hours.
- **Missing data:** Exclude records missing either primary variable; report the number excluded. No imputation will be used.

## Analysis plan
- **Primary method:** Spearman rank correlation between `studytime` and `G3`.
- **Direction:** Positive association expected; one-sided test.
- **Alpha:** 0.05.
- **Effect size:** Spearman's rho.
- **Uncertainty:** Report a 95% confidence interval where supported by the analysis software/method; state the method used.
- **Descriptive summaries:** Sample size, frequency of each studytime category, and grade summaries.
- **Visualisation:** Jittered scatter plot of studytime category against G3, with clear axis labels.
- **Robustness check:** Kendall's tau-b correlation. Compare direction and broad conclusion with the primary analysis.
- **Assumptions/limitations:** The observations are treated as independent student records. The study is observational and may be affected by confounding, measurement limitations, and the dataset's limited school context. Correlation does not establish causation.

## Deviations
No deviations have been made at the time this plan was written. Any later deviation will be recorded with a timestamp, description, reason, and impact on interpretation.
