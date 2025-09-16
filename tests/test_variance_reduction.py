import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from mc_pricing import price_european_mc


def test_antithetic_reduces_stderr():
    S0, K, r, sigma, T = 100.0, 100.0, 0.02, 0.2, 1.0
    # Use a moderate N to see the effect
    p1, se1, _, _ = price_european_mc("call", S0, K, r, sigma, T, n_sims=20_000, antithetic=False, seed=777)
    p2, se2, _, _ = price_european_mc("call", S0, K, r, sigma, T, n_sims=20_000, antithetic=True, seed=777)
    assert se2 < se1


def test_control_variate_runs():
    # Smoke test to ensure control variate code path executes.
    S0, K, r, sigma, T = 100.0, 100.0, 0.02, 0.2, 1.0
    p, se, _, _ = price_european_mc("call", S0, K, r, sigma, T, n_sims=10_000, control_variate=True, seed=42)
    assert p > 0.0 and se >= 0.0
