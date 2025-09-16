import math
from black_scholes import d1_d2, _norm_cdf, call_price, put_price

def call_greeks(S0, K, r, sigma, T):
    """Return Delta, Gamma, Vega, Theta, Rho for a European call."""
    d1, d2 = d1_d2(S0, K, r, sigma, T)
    delta = _norm_cdf(d1)
    gamma = math.exp(-0.5*d1*d1)/(S0*sigma*math.sqrt(2*math.pi*T))
    vega = S0*math.exp(-0.5*d1*d1)*math.sqrt(T)/math.sqrt(2*math.pi)
    theta = -(S0*sigma*math.exp(-0.5*d1*d1))/(2*math.sqrt(2*math.pi*T)) - r*K*math.exp(-r*T)*_norm_cdf(d2)
    rho = K*T*math.exp(-r*T)*_norm_cdf(d2)
    return delta, gamma, vega, theta, rho

def put_greeks(S0, K, r, sigma, T):
    """Return Delta, Gamma, Vega, Theta, Rho for a European put."""
    d1, d2 = d1_d2(S0, K, r, sigma, T)
    delta = _norm_cdf(d1) - 1
    gamma = math.exp(-0.5*d1*d1)/(S0*sigma*math.sqrt(2*math.pi*T))
    vega = S0*math.exp(-0.5*d1*d1)*math.sqrt(T)/math.sqrt(2*math.pi)
    theta = -(S0*sigma*math.exp(-0.5*d1*d1))/(2*math.sqrt(2*math.pi*T)) + r*K*math.exp(-r*T)*_norm_cdf(-d2)
    rho = -K*T*math.exp(-r*T)*_norm_cdf(-d2)
    return delta, gamma, vega, theta, rho
