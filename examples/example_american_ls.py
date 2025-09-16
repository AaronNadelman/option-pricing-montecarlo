import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
import american_ls

if __name__=='__main__':
    p = american_ls.price_american_mc_ls('put',100,100,0.02,0.2,1.0,n_steps=50,n_sims=100000,seed=42)
    print(f'American put (LS) price: {p:.6f}')
