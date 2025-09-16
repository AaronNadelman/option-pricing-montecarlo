import math, numpy as np
from paths import simulate_gbm_paths

def price_asian_call_mc(S0, K, r, sigma, T, n_sims=100000, n_steps=50, seed=None):
    """Monte Carlo pricing of an arithmetic-average Asian call option."""
    if seed: np.random.seed(seed)
    paths = simulate_gbm_paths(S0,r,sigma,T,n_steps,n_sims,method="exact")
    A = np.mean(paths[:,1:],axis=1)
    payoff = np.maximum(A-K,0.0)
    return math.exp(-r*T)*np.mean(payoff)
