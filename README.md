# 📊 Quant Portfolio

A collection of **ten quantitative finance research projects** demonstrating applied skills in **trading strategies, portfolio optimization, options modeling, risk management, and machine learning for markets**.

Each project includes **data, code (Jupyter notebooks), and results**.

---

## 🔹 Projects (ordered)

### [PROJECT-01 — Momentum vs Mean-Reversion](./PROJECT-01-Momentum-vs-Mean-Reversion)
- Compares **momentum (moving-average crossover)** and **mean-reversion (RSI)** strategies on equity data.
- Uses **volatility targeting** and **transaction costs**; evaluates Sharpe, drawdown, turnover.
- Includes: strategy logic, backtests, equity curves, summary metrics.

---

### [PROJECT-02 — Portfolio Optimization (Efficient Frontier & Risk Parity)](./PROJECT-02-Portfolio-Optimization)
- Implements **Markowitz MPT**, **tangency portfolio**, **minimum variance**, and **risk parity**.
- Plots the **efficient frontier**; analyzes allocation stability and sensitivity.
- Includes: optimizer, constraints, weights, frontier & allocation visuals.

---

### [PROJECT-03 — Pairs Trading (Cointegration & Z-Score)](./PROJECT-03-Pairs-Trading)
- Finds **cointegrated pairs**, trades the spread using **z-score thresholds** with stop/exit logic.
- Evaluates hit-rate, average trade P&L, holding period, and slippage impact.
- Includes: Engle–Granger tests, spread/entry/exit plots, backtest metrics.

---

### [PROJECT-04 — Options Volatility & Surfaces](./PROJECT-04-Options-Volatility)
- Builds **implied volatility smiles/surfaces** from option chains.
- Compares **Black–Scholes** vs empirical IV, explores **skew** and **term structure**.
- Includes: smile/surface plots, moneyness/tenor analysis, basic strategies (e.g., covered calls).

---

### [PROJECT-05 — Machine Learning for Markets](./PROJECT-05-ML-for-Markets)
- Predicts market direction using **Logistic Regression** and **Random Forests**.
- Feature set: lagged returns, MA/RSI, volatility, and simple macro proxies.
- Includes: train/test split, cross-validation, confusion matrix, feature importance.

---

### [PROJECT-06 — Sharpe Ratio Optimization](./PROJECT-06-Sharpe-Ratio-Optimization)
- Optimizes portfolio weights to **maximize Sharpe** under budget and no-short constraints.
- Benchmarks against **equal-weight** and **volatility-scaled** allocations.
- Includes: optimizer, frontier slice, weights and performance comparison.

---

### [PROJECT-07 — Monte Carlo Option Pricing](./PROJECT-07-Monte-Carlo-Option-Pricing)
- Prices **European options** via Monte Carlo under **GBM**, compares to **Black–Scholes**.
- Demonstrates path simulation, pricing convergence, and variance reduction ideas.
- Includes: simulated paths, pricing distributions, error vs. paths analysis.

---

### [PROJECT-08 — Value at Risk (VaR) & Expected Shortfall](./PROJECT-08-Value-at-Risk)
- Implements **Historical**, **Parametric (Normal/Student-t)**, and **Monte Carlo VaR**.
- Extends to **Expected Shortfall (CVaR)** for tail-risk assessment.
- Includes: loss distributions, VaR/ES comparison, stress-style scenarios.

---

### [PROJECT-09 — CAPM & Factor Models](./PROJECT-09-CAPM-Factor-Models)
- Estimates **beta, alpha, R²** using CAPM; extends to **Fama-French** factor regressions.
- Interprets factor exposures and residual risk; compares assets/sectors.
- Includes: regressions, factor loadings, attribution summaries.

---

### [PROJECT-10 — Daily Returns & Volatility](./PROJECT-10-Daily-Returns-Volatility)
- Computes **daily log returns**, **rolling volatility**, and **autocorrelations**.
- Highlights stylized facts (fat tails, volatility clustering).
- Includes: return histograms, rolling stats, ACF/PACF, drawdown analysis.

---

## 🛠️ Tech Stack
- **Python**: `numpy`, `pandas`, `matplotlib`, `scikit-learn`, `statsmodels`, `scipy`, `yfinance`
- **Analysis**: Jupyter Notebooks, CSV datasets, PNG charts
- **Focus**: Backtesting, risk, optimization, options, ML

---

## ✨ Author
**Harsh Byjesh** — Aspiring Quantitative Trader | Princeton ORFE Applicant
