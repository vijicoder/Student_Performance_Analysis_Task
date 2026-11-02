# Synthetic-only pipeline check; no real student data is used.
synthetic <- data.frame(
  studytime = c(1, 2, 4, NA, 5, 3, 2),
  G3 = c(10, 15, 18, 12, 14, 25, 15)
)
cleaned <- unique(synthetic)
cleaned$studytime <- suppressWarnings(as.numeric(cleaned$studytime))
cleaned$G3 <- suppressWarnings(as.numeric(cleaned$G3))
cleaned <- cleaned[complete.cases(cleaned), ]
cleaned <- cleaned[cleaned$studytime %in% 1:4 & cleaned$G3 >= 0 & cleaned$G3 <= 20, ]

stopifnot(nrow(cleaned) == 3)
stopifnot(identical(cleaned$studytime, c(1, 2, 4)))
stopifnot(identical(cleaned$G3, c(10, 15, 18)))
cat("PASS: synthetic pipeline produced the expected 3 valid rows.\n")
