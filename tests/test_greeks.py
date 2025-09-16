import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from src import greeks, black_scholes

def test_call_greeks_runs():
    g = greeks.call_greeks(100,100,0.02,0.2,1.0)
    assert len(g)==5
