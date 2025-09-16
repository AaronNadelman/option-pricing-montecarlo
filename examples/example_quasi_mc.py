import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))

from quasi_mc import price_european_call_qmc

if __name__ == "__main__":
    S0, K, r, sigma, T = 100, 100, 0.02, 0.2, 1.0
    price = price_european_call_qmc(S0, K, r, sigma, T, n_sims=8192, seed=42)
    print("Quasi-MC European Call Option Price:", price)
