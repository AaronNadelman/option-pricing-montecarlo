import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))

from asian_option import price_asian_call_mc

if __name__ == "__main__":
    S0, K, r, sigma, T = 100, 100, 0.02, 0.2, 1.0
    price = price_asian_call_mc(S0, K, r, sigma, T, n_sims=20000, n_steps=50, seed=42)
    print("Asian Call Option Price:", price)
