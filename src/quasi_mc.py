import math
import numpy as np
from scipy.stats import qmc

def sobol_normals(n_sims, dim=1, scramble=True, seed=None):
    """Generate Sobol quasi-random normal samples."""
    sampler = qmc.Sobol(d=dim, scramble=scramble, seed=seed)
    u = sampler.random(n_sims)
    return np.sqrt(2)*erfinv(2*u-1)

def erfinv(x):
    """Approximate inverse error function using numpy's special function if available."""
    from scipy.special import erfinv as sp_erfinv
    return sp_erfinv(x)

def price_european_call_qmc(S0,K,r,sigma,T,n_sims=16384,seed=None):
    """Quasi-MC pricing using Sobol sequences."""
    Z = sobol_normals(n_sims,1,seed=seed).flatten()
    ST = S0*np.exp((r-0.5*sigma*sigma)*T + sigma*math.sqrt(T)*Z)
    payoff = np.maximum(ST-K,0.0)
    return math.exp(-r*T)*np.mean(payoff)
