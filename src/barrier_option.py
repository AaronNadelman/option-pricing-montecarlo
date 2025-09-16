import math
import numpy as np
from typing import Literal
from paths import simulate_gbm_paths

def price_barrier_knock_out_mc(S0,K,r,sigma,T,barrier,barrier_type:Literal['up-and-out','down-and-out']='up-and-out',option_type:Literal['call','put']='call',n_sims=100000,n_steps=252,seed=None):
    """Price knock-out barrier options via MC with discrete monitoring."""
    paths = simulate_gbm_paths(S0,r,sigma,T,n_steps,n_sims,method='exact',seed=seed)
    inner = paths[:,1:]
    if barrier_type=='up-and-out':
        knocked = (inner>=barrier).any(axis=1)
    else:
        knocked = (inner<=barrier).any(axis=1)
    ST = inner[:,-1]
    payoff = np.maximum(ST-K,0.0) if option_type=='call' else np.maximum(K-ST,0.0)
    alive = np.where(knocked,0.0,payoff)
    return math.exp(-r*T)*float(np.mean(alive))
