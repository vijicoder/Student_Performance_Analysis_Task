# Run from the project root with: Rscript R/analyze.R
raw_file <- "data/raw/student-mat.csv"
if (!file.exists(raw_file)) {
  stop("Dataset not found. Download student-mat.csv from UCI and place it in data/raw/.")
}

df <- read.csv(raw_file, sep = ";", stringsAsFactors = FALSE)
required <- c("studytime", "G3")
if (!all(required %in% names(df))) stop("Required columns are missing.")

n_original <- nrow(df)
df <- unique(df)
df$studytime <- suppressWarnings(as.numeric(df$studytime))
df$G3 <- suppressWarnings(as.numeric(df$G3))
df <- df[complete.cases(df[, required]), ]
df <- df[df$studytime %in% 1:4 & df$G3 >= 0 & df$G3 <= 20, ]

dir.create("data/processed", recursive = TRUE, showWarnings = FALSE)
dir.create("reports", recursive = TRUE, showWarnings = FALSE)
write.csv(df, "data/processed/student-mat-cleaned-R.csv", row.names = FALSE)

spearman <- cor.test(df$studytime, df$G3, method = "spearman", alternative = "greater", exact = FALSE)
kendall <- cor.test(df$studytime, df$G3, method = "kendall", alternative = "greater", exact = FALSE)

sink("reports/R_analysis_summary.txt")
cat("Student Performance Analysis (R)\n")
cat("Rows in original dataset:", n_original, "\n")
cat("Rows in cleaned dataset:", nrow(df), "\n")
cat("Rows excluded:", n_original - nrow(df), "\n\n")
print(spearman)
print(kendall)
cat("\nInterpretation: association only; this observational analysis does not establish causation.\n")
sink()

png("reports/R_studytime_vs_G3.png", width = 900, height = 650)
plot(jitter(df$studytime), df$G3,
     xlab = "Weekly study-time category (1-4)",
     ylab = "Final mathematics grade (G3, 0-20)",
     main = "Study-time category and final mathematics grade",
     pch = 19, col = grDevices::rgb(0, 0, 0, 0.35))
axis(1, at = 1:4, labels = 1:4)
dev.off()
