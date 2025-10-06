# Machine Learning for Markets (Upload-Ready)

**Author:** HARSH BYJESH | Generated: 2025-10-06

This project applies **Machine Learning models** (Logistic Regression and Random Forest)  
to predict **next-day market direction** using engineered technical indicators.

---

## What's Included
- `data/` → `SPY_synth.csv` (synthetic SPY-like daily series, 2018–2024)  
- `notebook.ipynb` → ready-to-run notebook for feature engineering, model training, and backtest  
- `results/metrics.json` → cross-validation metrics (AUC, accuracy)  
- `results/roc_curve.png` → ROC curve on holdout set  
- `results/equity_ml.png` → equity curve of probability-threshold trading strategy  
- `report.docx` / `report.pdf` → 2-page research brief (editable DOCX + final PDF)

---

## Quickstart
1. (Optional) Install dependencies:  
   ```bash
   pip install numpy pandas matplotlib scikit-learn
   ```
2. Open and run `notebook.ipynb` in Jupyter/Colab/VS Code.  
3. Generated results will appear in `results/`.  
4. Replace author name if needed and push to GitHub.

---

## Key Results
- Both models beat random guessing (AUC > 0.5).  
- Random Forest outperformed Logistic Regression on the test set.  
- Trading on probability thresholds (>0.55) improved equity but would face slippage/costs in live markets.  

---

## Notes
- Data is synthetic for reproducibility. Replace with real SPY returns to validate results.  
- Future improvements: gradient boosting models, feature selection, and walk-forward validation.  
