# Option Pricing with Monte Carlo Simulation (v0.2.0)

## Overview
This project provides a full implementation of **European option pricing** using both the closed-form **Black–Scholes model** and **Monte Carlo simulation techniques**. It further extends to Greeks, path-dependent options, and quasi-Monte Carlo.

## Core Features (from v0.1.0)
- Black–Scholes closed-form formulas for European calls and puts.
- Monte Carlo simulation of Geometric Brownian Motion under the risk-neutral measure.
- Variance reduction: antithetic variates, control variates.
- Error and convergence analysis with plots.
- Unit tests and CI integration.

## Extended Features (new in v0.2.0)
- **Greeks**: Delta, Gamma, Vega, Theta, Rho (closed-form and MC approximations).
- **Asian options**: Monte Carlo pricing of arithmetic-average Asian calls.
- **Quasi-Monte Carlo**: Sobol sequence sampling for faster convergence.
- New Jupyter notebooks demonstrating these extensions.

---

## Quick Start

### 1. Create a virtual environment and install dependencies
```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

pip install -r requirements.txt
```

### 2. Run a simple CLI example (European option)
```bash
python examples/cli_example.py --type call --S0 100 --K 100 --r 0.02 --sigma 0.2 --T 1 --n_sims 100000 --antithetic
```

### 3. Generate error and convergence plots
```bash
python scripts/validate.py
```

### 4. Try extended features
Run the following examples:
```bash
python examples/example_greeks.py
python examples/example_asian.py
python examples/example_quasi_mc.py
```

### 5. Run tests
```bash
pytest -q
```

### 6. Explore notebooks
- `notebooks/01_validate_mc_vs_bs.ipynb` — validation baseline  
- `notebooks/02_greeks_and_asian.ipynb` — Greeks and Asian option demo  
- `notebooks/03_quasi_mc.ipynb` — Quasi-MC demo  

---

## Repository Structure
- `src/black_scholes.py` — Closed-form BS model
- `src/mc_pricing.py` — Monte Carlo pricing engine
- `src/greeks.py` — Greeks calculations
- `src/asian_option.py` — Asian option MC pricing
- `src/quasi_mc.py` — Sobol quasi-MC pricing
- `examples/cli_example.py` — CLI usage example
- `examples/example_greeks.py` — Greeks demo
- `examples/example_asian.py` — Asian option demo
- `examples/example_quasi_mc.py` — Quasi-MC demo
- `scripts/validate.py` — validation and convergence plots
- `tests/` — unit tests for all modules
- `notebooks/` — reproducibility demos

---

## Resume Highlights
- Implemented Monte Carlo simulation for option pricing, with deviation <2% from Black–Scholes benchmark.
- Extended to compute Greeks analytically and numerically.
- Demonstrated path-dependent Asian option pricing via Monte Carlo.
- Applied quasi-Monte Carlo (Sobol sequences) to accelerate convergence.

---

## License
MIT License
