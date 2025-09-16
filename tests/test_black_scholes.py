import os, sys, math
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
import black_scholes as bs


def test_call_put_values():
    """
    Compare against known values for S0=100, K=100, r=0.02, sigma=0.2, T=1.
    Reference computed via the BS closed-form.
    """
    S0, K, r, sigma, T = 100.0, 100.0, 0.02, 0.2, 1.0
    call_ref = 8.916037278572539
    put_ref = 6.93590460924807
    call = bs.call_price(S0, K, r, sigma, T)
    put = bs.put_price(S0, K, r, sigma, T)
    assert abs(call - call_ref) < 1e-9
    assert abs(put - put_ref) < 1e-9


def test_put_call_parity():
    S0, K, r, sigma, T = 100.0, 100.0, 0.02, 0.2, 1.0
    call = bs.call_price(S0, K, r, sigma, T)
    put = bs.put_price(S0, K, r, sigma, T)
    lhs = call - put
    rhs = S0 - K * math.exp(-r * T)
    assert abs(lhs - rhs) < 1e-9
