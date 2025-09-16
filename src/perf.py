import math
import time
import numpy as np
try:
    from numba import njit, prange
    NUMBA_AVAILABLE=True
except Exception:
    NUMBA_AVAILABLE=False
    def njit(*a,**k):
        def d(f): return f
        return d
    prange=range

def simulate_terminal_numpy(S0,r,sigma,T,n_sims,seed=None):
    if seed is not None:
        np.random.seed(seed)
    Z=np.random.standard_normal(n_sims)
    return S0*np.exp((r-0.5*sigma*sigma)*T + sigma*math.sqrt(T)*Z)

if NUMBA_AVAILABLE:
    @njit(parallel=True, fastmath=True)
    def simulate_terminal_numba(S0, r, sigma, T, n_sims, seed=0):
        np.random.seed(seed)
        out = np.empty(n_sims)
        for i in prange(n_sims):
            z = np.random.normal(0.0, 1.0)
            out[i] = S0 * math.exp((r - 0.5 * sigma * sigma) * T + sigma * math.sqrt(T) * z)
        return out
else:
    def simulate_terminal_numba(S0, r, sigma, T, n_sims, seed=0):
        return simulate_terminal_numpy(S0, r, sigma, T, n_sims, seed)


def benchmark(n_sims=100_000):
    S0, r, sigma, T = 100.0, 0.02, 0.2, 1.0

    # NumPy baseline
    t0 = time.time()
    simulate_terminal_numpy(S0, r, sigma, T, n_sims, 42)
    numpy_time = time.time() - t0

    # Warmup Numba (don't time this call)
    simulate_terminal_numba(S0, r, sigma, T, 10_000, 42)

    # Real Numba timing
    t1 = time.time()
    simulate_terminal_numba(S0, r, sigma, T, n_sims, 42)
    numba_time = time.time() - t1

    return {
        'numpy_sec': numpy_time,
        'numba_sec': numba_time,
        'speedup_x': numpy_time / numba_time if numba_time > 0 else float('inf'),
        'numba_available': NUMBA_AVAILABLE,
    }
