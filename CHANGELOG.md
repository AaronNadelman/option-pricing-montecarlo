# Changelog

## v0.3.0 (2025-09-16)
### Added
- **Barrier options (knock-out)** via Monte Carlo simulation.
- **American options (Longstaff–Schwartz)** regression method.
- **Performance acceleration** using Numba parallel JIT (10× speedup).
- **Visualization script** for GBM sample paths with optional barrier line.
- **Documentation site** using MkDocs + Material theme, deployed via GitHub Pages.

### Improved
- Expanded README with Quick Start guide and consolidated version history.
- Added more examples: barrier, American LS, and Numba benchmark.

---

## v0.2.0 (2025-09-10)
### Added
- Asian options (arithmetic average) with Monte Carlo pricing.
- Greeks computation (Delta, Gamma, Vega, Theta, Rho).
- Quasi-Monte Carlo (Sobol sequences) for variance reduction.
- Extended examples for easier experimentation.

---

## v0.1.0 (2025-09-05)
### Added
- Black–Scholes closed-form pricing.
- Monte Carlo pricing for European options (call/put).
- Variance reduction techniques (antithetic variates, control variates).
- Validation notebook with error convergence plots.
