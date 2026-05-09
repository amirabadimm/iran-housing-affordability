# Methodology

The analysis uses cleaned Iranian Household Budget Survey files for 1394-1403. The survey years are analyzed as repeated cross-sections rather than a household panel. CPI data are read from the included workbook `data/cleaned/CPI.xlsx`, whose metadata identifies World Bank/IMF as the underlying source.

## CPI Preparation

The CPI workbook contains annual Persian-year observations from 1339 to 1403. The `data` sheet includes year, CPI index, and annual inflation rate; the `metadata` sheet records source and definition notes.

For the analysis, the year column is standardized as `Year`, the CPI index column is standardized as `CPI`, and the series is merged to household observations by year. No additional rebasing is performed in the notebooks. Real income and real housing costs are calculated by dividing nominal values by the CPI index.

## Weighting

Household-level estimates use the survey weight variable `Weight`. Weighted means are calculated after excluding missing values and non-positive weights. Weighted shares are estimated as weighted means of binary indicators.

## Tenure

Tenure is grouped into owners and renters using the `Tenure` field. Values containing `own` are classified as owners. Values containing `rent` or `mortg` are classified as renters. Other tenure categories are excluded from owner-renter comparisons.

## Housing Cost

Adjusted housing cost, `housing_cost_adj`, is constructed from `Housing, Water, Electricity, Gas and Other Fuels`. Imputed rent for ownership and mortgage tenure is subtracted when available. Negative adjusted values are clipped to zero.

## Housing Burden

Two burden measures are used:

- Housing share: `housing_cost_adj / Gross_Expenditure`
- Housing pressure: `housing_cost_adj / Income`

Housing poverty is reported for urban renters using 30 percent and 40 percent thresholds of income.

## Inflation Exposure

Selected household expenditure shares are combined with category-specific annual inflation rates for food, housing, transport, and health. The resulting measure approximates exposure to inflation through household budget composition.
