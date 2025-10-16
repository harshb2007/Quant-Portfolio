# Monte Carlo Option Pricing (Upload-Ready)

**Author:** Harsh Byjesh | **Generated:** 2025-10-06

This project prices a **European call option** using **Monte Carlo simulation** on a Geometric Brownian Motion (GBM) model and compares the estimate with the **Black–Scholes** closed form.

## What's Included
- `data/sample_paths.csv` – sample of simulated GBM price paths
- `results/metrics.json` – parameters, Monte Carlo price, SE, and Black–Scholes price
- `results/mc_convergence.png` – convergence of MC price to Black–Scholes with more paths
- `results/terminal_distribution.png` – histogram of terminal prices
- `results/sample_paths.png` – example GBM paths
- `report.docx` – 2–3 page report with figures

## Key Numbers
- **Monte Carlo price:** 6.9277 ± 0.0884
- **Black–Scholes price:** 6.7048
- **Paths:** 20,000 | **Steps per path:** 252
- **Parameters:** S0=100.0, K=105.0, r=0.02, sigma=0.2, T=1.0

## Quickstart
1. Open `report.docx` to review the study.
2. Adjust parameters in code or notebook (coming soon) to re-run.
3. Export report to PDF and push to GitHub.
