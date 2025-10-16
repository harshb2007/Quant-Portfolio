# CAPM Beta & Fama–French Factor Models (Upload-Ready)

**Author:** Harsh Byjesh | **Generated:** 2025-10-06

This project estimates **CAPM beta** and **Fama–French 3-factor loadings** for a synthetic stock using daily data.

## What's Included
- `data/factors_and_returns.csv` – synthetic daily factors (MKT-RF, SMB, HML, RF) and stock returns
- `results/metrics.json` – CAPM alpha/beta/R² and FF3 loadings with R²
- `results/capm_scatter_fit.png` – stock excess vs market excess with CAPM regression line
- `results/ff3_betas.png` – factor exposures (betas)
- `results/ff3_residuals_hist.png` – residual histogram (FF3 fit)
- `results/cumulative_returns.png` – cumulative return of stock vs market
- `report.docx` – 2–3 page report with figures

## Key Results (Synthetic)
- CAPM: alpha=-0.000130/day, beta=1.237, R²=0.674
- FF3: alpha=-0.000024/day, betas=[MKT 1.234, SMB 0.382, HML -0.232], R²=0.709

## Quickstart
1. Open the report to review methodology and results.
2. Swap in real factor data (e.g., Fama–French) and recompute regressions.
3. Export report to PDF and push to GitHub.
