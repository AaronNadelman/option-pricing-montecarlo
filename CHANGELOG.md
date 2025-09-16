# Changelog

## v0.2.0
- Added Greeks (Delta, Gamma, Vega, Theta, Rho) with closed-form and MC estimation.
- Implemented arithmetic-average Asian call option pricing via Monte Carlo.
- Introduced Quasi-Monte Carlo using Sobol sequences.
- Added new notebooks: Greeks + Asian options, Quasi-MC.
- Extended test suite to cover new modules.

## v0.1.0
- Initial release.
- Black–Scholes closed-form pricing (calls, puts, Delta).
- Monte Carlo pricing engine with variance reduction (antithetic, control variates).
- Validation scripts and plots (relative error, convergence).
- Unit tests and CI setup.
