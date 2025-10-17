PROJECT-01-Momentum-vs-Mean-Reversion

Author: HARSH BYJASH| Generated: 2025-10-01

This folder contains a complete, self-contained project comparing **Momentum** (MA crossover) vs **Mean-Reversion** (RSI) on a SPY-like series with **volatility targeting** and **transaction costs**.

## What's Included
- `data/SPY_sample.csv` — synthetic but realistic daily OHLCV (2020–2024)
- `src/` — helper code (if you want to modularize later)
- `notebooks/momentum_vs_meanreversion.ipynb` — ready-to-run notebook (uses yfinance if you add internet; falls back to the provided CSV)
- `results/metrics.json` — summary metrics for test period
- `results/equity_curves.png` — equity curves (Buy&Hold vs Momentum vs Mean-Reversion)
- `results/drawdown_momentum.png` — drawdown chart for momentum
- `report.docx` — 2-page research brief you can export to PDF

## Quickstart
1. (Optional) Install deps: `pip install numpy pandas matplotlib yfinance`
2. Run the notebook to regenerate results with your own data or yfinance.
3. Replace `<Your Name>` in report and push to GitHub.

## Key Results (Test)
- Momentum best params: (10, 50)
- Momentum metrics: {'CAGR': 0.11851252965317882, 'Vol': 0.11415152134883935, 'Sharpe': 1.0382036809742774, 'MaxDD': -0.08981329261586868}
- Mean-Reversion metrics: {'CAGR': -0.008702413767599948, 'Vol': 0.019985656826845416, 'Sharpe': -0.43543296289920125, 'MaxDD': -0.04162810784046389}
- Buy & Hold metrics: {'CAGR': 0.19057630791120617, 'Vol': 0.1778759407080469, 'Sharpe': 1.0714001407531824, 'MaxDD': -0.21546292232359177}

> Note: Results here are from the included synthetic dataset for reproducibility without internet. When you run with live SPY from yfinance, numbers will differ — that’s normal and expected.



