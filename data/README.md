# Data

Place the cleaned input files in this folder before running the notebooks.

Expected files:

```text
data/cleaned/94.csv
data/cleaned/95.csv
data/cleaned/96.csv
data/cleaned/97.csv
data/cleaned/98.csv
data/cleaned/99.csv
data/cleaned/400.csv
data/cleaned/401.csv
data/cleaned/402.csv
data/cleaned/403.csv
```

The HBS files can be obtained from <https://d-learn.ir/iran-hbs/>.

`CPI.xlsx` is included in this repository because it is small and needed for reproducibility. The workbook has two sheets:

- `data`: Persian year, CPI index, and annual inflation rate
- `metadata`: source and definition notes

The CPI workbook covers 1339-1403. Its metadata identifies World Bank/IMF as the underlying source. The corresponding World Bank CPI/inflation indicator is `FP.CPI.TOTL.ZG`: <https://data.worldbank.org/indicator/FP.CPI.TOTL.ZG?end=2024&locations=IR&start=1960>.

## CPI Workbook Preparation

`data/cleaned/CPI.xlsx` is the local CPI file used for real-value adjustments. The analysis reads the `data` sheet, standardizes the year column as `Year`, standardizes the CPI index column as `CPI`, and merges the CPI series to household records by year.

No additional rebasing is performed in the analysis notebooks. Nominal income and housing-cost variables are deflated by dividing them by the CPI index available in this workbook.

The notebooks create `data/cleaned/master.csv`. The generated master file is ignored by git because it is large and reproducible from the source files.

For local work on the original machine, `scripts/copy_local_data.py` can copy the required files from the previous working folder into `data/cleaned/`.
