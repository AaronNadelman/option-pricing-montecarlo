import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from src import asian_option

def test_asian_call_mc():
    p = asian_option.price_asian_call_mc(100,100,0.02,0.2,1.0,n_sims=2000,n_steps=10,seed=42)
    assert p>0
