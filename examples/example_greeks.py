import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))

from greeks import call_greeks, put_greeks

if __name__ == "__main__":
    S0, K, r, sigma, T = 100, 100, 0.02, 0.2, 1.0
    print("Call Greeks:", call_greeks(S0, K, r, sigma, T))
    print("Put Greeks:", put_greeks(S0, K, r, sigma, T))
