import math
import numpy as np
from paths import simulate_gbm_paths

def _phi(x):
    return np.stack([np.ones_like(x), x, x*x], axis=1)

def price_american_mc_ls(option_type,S0,K,r,sigma,T,n_steps=50,n_sims=100000,seed=None):
    paths = simulate_gbm_paths(S0,r,sigma,T,n_steps,n_sims,method='exact',seed=seed)
    dt=T/n_steps; df=math.exp(-r*dt)
    payoff = (lambda s: np.maximum(s-K,0.0)) if option_type=='call' else (lambda s: np.maximum(K-s,0.0))
    cf = payoff(paths[:,-1])
    for t in range(n_steps-1,0,-1):
        St = paths[:,t]
        itm = payoff(St)>0
        X = St[itm]
        if X.size==0:
            cf *= df
            continue
        Y = cf[itm]*df
        Phi = _phi(X)
        beta, *_ = np.linalg.lstsq(Phi, Y, rcond=None)
        cont = beta[0] + beta[1]*St + beta[2]*St*St
        ex_now = payoff(St)>=cont
        exercise = ex_now & itm
        cf = np.where(exercise, payoff(St), cf*df)
    return float(np.mean(cf)*math.exp(-r*dt))
