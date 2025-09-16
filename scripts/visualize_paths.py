import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
import numpy as np
import matplotlib.pyplot as plt
from paths import simulate_gbm_paths

def visualize_paths(S0=100.0,r=0.02,sigma=0.2,T=1.0,n_steps=252,n_sims=20,seed=7,barrier=None):
    paths = simulate_gbm_paths(S0,r,sigma,T,n_steps,n_sims,method='exact',seed=seed)
    t = np.linspace(0,T,n_steps+1)
    for i in range(min(n_sims,50)):
        plt.plot(t, paths[i], alpha=0.7)
    if barrier is not None:
        plt.axhline(barrier, linestyle='--')
    plt.xlabel('Time (years)'); plt.ylabel('Price'); plt.title('Sample GBM Paths'); plt.tight_layout()
    out = os.path.join(os.path.dirname(__file__), '..', 'assets', 'sample_paths.png')
    os.makedirs(os.path.join(os.path.dirname(__file__), '..', 'assets'), exist_ok=True)
    plt.savefig(out, dpi=160); print('Saved', out)

if __name__=='__main__':
    visualize_paths()
