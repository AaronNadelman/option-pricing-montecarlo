# Option Pricing with Monte Carlo & Black–Scholes

[![CI](https://github.com/LinShuyue2003/option-pricing-montecarlo/actions/workflows/ci.yml/badge.svg)](https://github.com/LinShuyue2003/option-pricing-montecarlo/actions)
[![Docs](https://github.com/LinShuyue2003/option-pricing-montecarlo/actions/workflows/docs.yml/badge.svg)](https://linshuyue2003.github.io/option-pricing-montecarlo/)

A self-contained Python project showcasing **financial engineering techniques** for option pricing, implemented from scratch with **clear, well-documented code**.

---

## ✨ Features Overview

| Feature                        | Status | Example Script |
|--------------------------------|--------|----------------|
| Black–Scholes closed-form       | ✔      | `src/black_scholes.py` |
| European options (MC)           | ✔      | `examples/cli_example.py` |
| Variance reduction (antithetic, control variate) | ✔ | built-in |
| Asian options (MC)              | ✔      | `examples/example_asian.py` |
| Barrier options (knock-out)     | ✔      | `examples/example_barrier.py` |
| American options (Longstaff–Schwartz) | ✔ | `examples/example_american_ls.py` |
| Quasi-Monte Carlo (Sobol)       | ✔      | `examples/example_quasi_mc.py` |
| Greeks (Delta, Gamma, Vega, Theta, Rho) | ✔ | `examples/example_greeks.py` |
| Performance acceleration (Numba) | ✔     | `examples/example_numba_speed.py` |
| Visualization of GBM paths      | ✔      | `scripts/visualize_paths.py` |
| Docs website (MkDocs Material)  | ✔      | `docs/` |

---

## 🚀 Quick Start

```bash
# 1. Create virtual environment
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
# source .venv/bin/activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run a CLI example (European call with MC vs Black–Scholes)
python examples/cli_example.py --type call --S0 100 --K 100 --r 0.02 --sigma 0.2 --T 1 --n_sims 100000 --antithetic

# 4. Run extended examples
python examples/example_asian.py          # Asian option
python examples/example_greeks.py         # Greeks
python examples/example_quasi_mc.py       # Quasi-MC (Sobol)
python examples/example_barrier.py        # Barrier option
python examples/example_american_ls.py    # American option (LS)
python examples/example_numba_speed.py    # Numba acceleration

# 5. Generate validation plot
python scripts/validate.py

# 6. Preview documentation site locally
mkdocs serve
```

---

## 📖 Documentation

Full documentation with explanations for **non-finance readers** is available in [`docs/`](./docs).  
A live version is deployed on **GitHub Pages** via MkDocs + Material theme.

---

## 📝 Version Highlights

### v0.3.0
- Barrier options (knock-out) via Monte Carlo.
- American options using Longstaff–Schwartz regression.
- Numba acceleration with 10× potential speedup.
- Docs website with MkDocs Material.
- Visualization script for sample GBM paths.

### v0.2.0
- Asian options.
- Greeks.
- Quasi-Monte Carlo with Sobol sequences.
- Extended variance reduction examples.

### v0.1.0
- Black–Scholes closed-form pricing.
- Monte Carlo pricing for European options.
- Variance reduction techniques and validation notebook.

---

## 📊 Example Output

- **Convergence curve** (MC vs BS)  
- **GBM sample paths**  
- **Performance benchmark (NumPy vs Numba)**  

Plots and screenshots are generated in the `assets/` folder.

---

## 📜 License

MIT License.
