import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
import barrier_option

if __name__=='__main__':
    p = barrier_option.price_barrier_knock_out_mc(100,100,0.02,0.2,1.0,barrier=120.0,barrier_type='up-and-out',option_type='call',n_sims=100000,n_steps=252,seed=7)
    print(f'Up-and-out call price: {p:.6f}')
