# Daily Returns & Volatility Analysis (Upload-Ready)

**Author:** Harsh Byjesh | **Generated:** 2025-10-16

This project explores a SPY-like synthetic price series to analyze **daily returns, volatility, rolling risk metrics, and drawdowns**.

## What's Included
- `data/spy_synth.csv` – synthetic daily price & log return series (~5 years)
- `results/metrics.json` – summary stats (annual return/vol, Sharpe, VaR, max drawdown)
- `results/price_series.png` – price chart
- `results/returns_histogram.png` – histogram of daily log returns
- `results/rolling_vol_30d.png` – rolling annualized volatility (30d window)
- `results/rolling_sharpe_30d.png` – rolling Sharpe (30d window, annualized)
- `results/drawdown_curve.png` – drawdown over time
- `report.docx` – 2–3 page report with charts embedded

## Key Numbers (Synthetic)
- Annual Return: -0.30%
- Annual Volatility: 18.91%
- Annual Sharpe: -0.02
- Max Drawdown: -42.41%
- 95% Historical VaR (daily): -0.0201

## Quickstart
1. Open `report.docx` to review the findings.
2. Replace `data/spy_synth.csv` with real SPY data to replicate on live markets.
3. Export report to PDF and push the project to GitHub.
