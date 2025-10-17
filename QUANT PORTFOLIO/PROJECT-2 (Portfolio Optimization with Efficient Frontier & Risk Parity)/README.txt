# Portfolio Optimization with Efficient Frontier & Risk Parity 

**Author:** HARSH BYJESH | Generated: 2025-10-06

This project explores **Modern Portfolio Theory (MPT)** and **Risk Parity** approaches using a synthetic multi-asset dataset.  
It compares **Maximum Sharpe**, **Minimum Volatility**, and **Risk Parity** portfolios, and visualizes the **Efficient Frontier**.

---

## What's Included
- `data/` → synthetic dataset of 5 assets (StockA, StockB, StockC, Bond, Gold)  
- `notebook.ipynb` → ready-to-run notebook that builds efficient frontier and portfolio allocations  
- `results/metrics.json` → JSON summary of weights, return, vol, Sharpe for each strategy  
- `results/efficient_frontier.png` → plotted efficient frontier  
- `results/weights_table.csv` → allocation table for all methods  
- `report.docx` / `report.pdf` → 2-page research brief (editable DOCX + final PDF)

---

## Quickstart
1. (Optional) Install dependencies:  
   ```bash
   pip install numpy pandas matplotlib
   ```
2. Open and run `notebook.ipynb` in Jupyter/Colab/VS Code.  
3. Generated results will appear in `results/`.  
4. Replace author name if needed and push to GitHub.

---

## Key Results
- **Max Sharpe Portfolio**  
  - Higher returns, concentrated allocations  
- **Min Volatility Portfolio**  
  - Lower drawdowns, lower returns  
- **Risk Parity Portfolio**  
  - Balanced exposures across all assets  

---

## Notes
- This project uses synthetic data for reproducibility.  
- Replace `data/` with real asset returns (e.g., from Yahoo Finance) to replicate on live markets.  


