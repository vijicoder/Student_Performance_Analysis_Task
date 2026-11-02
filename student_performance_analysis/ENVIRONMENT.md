# Environment record

Python dependencies are pinned in `requirements.txt`.

Record the actual runtime versions after setup:
- Python version: fill in after running `python --version`
- pip version: fill in after running `pip --version`
- R version: fill in after running `R --version`
- Operating system: fill in when running the project

For a fully captured R package environment, use `renv` after installing any R packages:
```r
install.packages("renv")
renv::init()
renv::snapshot()
```
Commit the generated `renv.lock` file if you use renv. The R analysis script above uses base R functions only.
