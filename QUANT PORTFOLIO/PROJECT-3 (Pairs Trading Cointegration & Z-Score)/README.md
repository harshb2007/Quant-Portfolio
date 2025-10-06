# Pairs Trading with Cointegration & Z-Score (Upload-Ready)

**Author:** HARSH BYJESH | Generated: 2025-10-06

This project demonstrates a **Pairs Trading strategy** using cointegration tests and z-score thresholds.  
It identifies synthetic cointegrated asset pairs and trades spread mean-reversions.

---

## What's Included
- `data/` → synthetic cointegrated price series  
- `notebook.ipynb` → ready-to-run notebook for cointegration test, z-score calculation, and backtest  
- `results/metrics.json` → performance summary (returns, vol, Sharpe, drawdowns)  
- `results/zscore_plot.png` → z-score chart of the spread  
- `results/equity_curve.png` → strategy equity curve  
- `report.docx` / `report.pdf` → 2-page research brief (editable DOCX + final PDF)

---

## Quickstart
1. (Optional) Install dependencies:  
   ```bash
   pip install numpy pandas statsmodels matplotlib
   ```
2. Open and run `notebook.ipynb` in Jupyter/Colab/VS Code.  
3. Generated results will appear in `results/`.  
4. Replace author name if needed and push to GitHub.

---

## Key Results
- Identified a cointegrated synthetic pair with stable long-term relationship.  
- Trading the z-score spread captured mean-reversions effectively.  
- Equity curve showed steady profits with controlled drawdowns.  

---

## Notes
- This project uses synthetic data for reproducibility.  
- Replace `data/` with real stock/ETF pairs to replicate the strategy on live markets.  
