import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from mc_pricing import price_european_mc, bs_price, relative_error


def test_mc_converges_under_2pct():
    """
    With a fixed seed and 100k sims + antithetic, the MC estimate should be within 2% of BS.
    This keeps runtime small while ensuring numerical sanity.
    """
    S0, K, r, sigma, T = 100.0, 100.0, 0.02, 0.2, 1.0
    price, stderr, _, _ = price_european_mc("call", S0, K, r, sigma, T, n_sims=100_000, antithetic=True, seed=123)
    ref = bs_price("call", S0, K, r, sigma, T)
    assert relative_error(price, ref) < 0.02
