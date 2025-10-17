# Options Volatility Analysis (Smile, Surface & Covered Call) 

**Author:** HARSH BYJESH | Generated: 2025-10-06

This project analyzes **Options Implied Volatility (IV)** by plotting volatility smiles and surfaces,  
and overlays a simple **Covered Call strategy** against buy-and-hold performance.

---

## What's Included
- `data/` → synthetic options chain dataset  
- `notebook.ipynb` → ready-to-run notebook for IV calculations, smile/surface visualization, and covered call overlay  
- `results/iv_smile.png` → implied volatility smile plot  
- `results/iv_surface.png` → 3D implied volatility surface  
- `results/covered_call.png` → covered call vs buy-and-hold chart  
- `report.docx` / `report.pdf` → 2-page research brief (editable DOCX + final PDF)

---

## Quickstart
1. (Optional) Install dependencies:  
   ```bash
   pip install numpy pandas matplotlib mpl_toolkits
   ```
2. Open and run `notebook.ipynb` in Jupyter/Colab/VS Code.  
3. Generated results will appear in `results/`.  
4. Replace author name if needed and push to GitHub.

---

## Key Results
- **Volatility Smile**: OTM options have higher implied vols than ATM.  
- **Volatility Surface**: 3D visualization shows skew across strikes and maturities.  
- **Covered Call Strategy**: Reduces drawdowns and smooths equity curve, but caps upside returns.  

---

## Notes
- This project uses synthetic options data for reproducibility.  
- Replace `data/` with real option chain data (from sources like Yahoo Finance or CBOE) to replicate on live markets.  
