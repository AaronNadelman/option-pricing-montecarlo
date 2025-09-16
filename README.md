# Option Pricing with Monte Carlo Simulation (Black–Scholes Benchmark)

This project implements **European option pricing** using both the closed-form **Black–Scholes model** and **Monte Carlo simulation**. The implementation is designed to be beginner-friendly yet rigorous enough to demonstrate key concepts in stochastic processes, numerical simulation, and variance reduction techniques.

---

## Key Features

- **Black–Scholes closed-form pricing** for European call and put options.
- **Monte Carlo pricing** based on Geometric Brownian Motion under the risk-neutral measure.
- **Variance reduction methods**: antithetic variates and control variates.
- **Error and convergence analysis**: compare Monte Carlo estimates with Black–Scholes theoretical values, including error plots and confidence intervals.
- **Statistical outputs**: estimated price, standard error, and 95% confidence intervals.
- **Unit tests and CI**: ensure correctness and reproducibility.

---

## Quick Start

### 1. Create a virtual environment and install dependencies

```bash
python -m venv .venv
source .venv/bin/activate
# Windows: .venv\Scripts\activate

pip install -r requirements.txt
```

### 2. Run a simple CLI example

```bash
python examples/cli_example.py --type call --S0 100 --K 100 --r 0.02 --sigma 0.2 --T 1 --n_sims 100000 --antithetic
```

Expected output (values may vary slightly due to randomness):

```
MC call price: 8.917071
95% CI: [8.831537, 9.002606], stderr=0.043640
BS call price: 8.916037
Relative error: 0.012%
```

### 3. Generate error and convergence plots

```bash
python scripts/validate.py
```

This produces two figures under `assets/`:

- `deviation_vs_bs.png`: relative error vs. sample size N
- `convergence_plot.png`: standard error vs. sample size N

### 4. Run the test suite

```bash
pytest -q
```

---

## Repository Structure

```
src/
  black_scholes.py   # Closed-form BS formulas and Greeks (Delta)
  paths.py           # GBM path and terminal simulations
  mc_pricing.py      # Monte Carlo pricing engine with variance reduction
examples/
  cli_example.py     # Command-line example comparing MC vs BS
scripts/
  validate.py        # Validation and convergence plots
notebooks/
  01_validate_mc_vs_bs.ipynb  # Jupyter notebook for reproducibility
tests/
  test_black_scholes.py
  test_mc_basic.py
  test_variance_reduction.py
assets/
  (Generated figures are saved here)
```

---

## Mathematical Background (Brief)

- **GBM dynamics**:  
  \( dS_t = r S_t dt + \sigma S_t dW_t \) under the risk-neutral measure.

- **Terminal distribution**:  
  \( S_T = S_0 \exp((r - 0.5\sigma^2)T + \sigma \sqrt{T} Z), \quad Z \sim N(0,1) \).

- **BS call option price**:  
  \( C = S_0 \Phi(d_1) - K e^{-rT} \Phi(d_2) \).

- **Monte Carlo estimator**:  
  \( \hat{C} = e^{-rT} \frac{1}{N} \sum_{i=1}^N \max(S_T^{(i)} - K, 0) \).

- **Variance reduction**:  
  - Antithetic variates: use both \(Z\) and \(-Z\).  
  - Control variates: exploit known expectation \(E[S_T] = S_0 e^{rT}\).

---

## Resume Highlights

- Implemented Monte Carlo simulation for option pricing, achieving deviation **<2%** from the Black–Scholes closed-form solution.
- Demonstrated the application of **stochastic simulation in financial modeling**, including error analysis and variance reduction.

---

## License

MIT License
