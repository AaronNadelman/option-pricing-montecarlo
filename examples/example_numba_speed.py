import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
import perf

if __name__=='__main__':
    print(perf.benchmark(n_sims=1_000_000))
