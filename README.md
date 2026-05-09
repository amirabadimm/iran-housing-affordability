# Housing Affordability and Tenure in Iran

This repository contains a reproducible notebook workflow for analyzing housing affordability, tenure composition, and inflation exposure using cleaned Iranian Household Budget Survey files.

The analysis treats the survey years as repeated annual cross-sections. It estimates survey-weighted housing shares, renter-to-owner ratios, housing pressure, real income and housing costs, housing-poverty thresholds, disposable income after housing, and selected expenditure-inflation exposure measures.

## Data Sources

- Cleaned Iranian Household Budget Survey files, 1394-1403: <https://d-learn.ir/iran-hbs/>
- CPI indicator for Iran, World Bank `FP.CPI.TOTL.ZG`: <https://data.worldbank.org/indicator/FP.CPI.TOTL.ZG?end=2024&locations=IR&start=1960>

The large survey files are not included in this repository by default. The CPI workbook is small and is included as `data/cleaned/CPI.xlsx` so the analysis can be reproduced after the HBS files are added.

## Repository Structure

```text
.
|-- notebooks/
|   |-- 00_prepare_master.ipynb
|   `-- 01_housing_affordability_analysis.ipynb
|-- data/
|   |-- README.md
|   `-- cleaned/
|       `-- CPI.xlsx
|-- docs/
|   `-- methodology.md
|-- requirements.txt
|-- LICENSE
`-- README.md
```

## Reproduction

1. Download the cleaned yearly HBS files from D-Learn.
2. Place the yearly CSV files in `data/cleaned/`.
3. Confirm that `data/cleaned/CPI.xlsx` is present.
4. Run `notebooks/00_prepare_master.ipynb` to create `data/cleaned/master.csv`.
5. Run `notebooks/01_housing_affordability_analysis.ipynb` to produce the analysis tables inside the notebook.

The expected yearly files are:

```text
94.csv, 95.csv, 96.csv, 97.csv, 98.csv, 99.csv,
400.csv, 401.csv, 402.csv, 403.csv
```

The included CPI workbook contains annual Persian-year observations from 1339 to 1403. Its `data` sheet includes year, CPI index, and annual inflation rate; its metadata sheet identifies World Bank/IMF as the underlying source.

## Notes

`housing_cost_adj` is constructed from the COICOP housing category after subtracting imputed ownership or mortgage rent where applicable. Tenure groups are derived from the `Tenure` field: values containing `own` are classified as owners, while values containing `rent` or `mortg` are classified as renters.
