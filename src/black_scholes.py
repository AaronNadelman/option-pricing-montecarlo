import math

def _norm_cdf(x: float) -> float:
    """
    Standard normal cumulative distribution function using math.erf.

    Parameters
    ----------
    x : float
        Evaluation point.

    Returns
    -------
    float
        Phi(x), the CDF of N(0, 1) at x.
    """
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


def d1_d2(S0: float, K: float, r: float, sigma: float, T: float):
    """
    Compute d1 and d2 terms used in the Black–Scholes formula.

    Parameters
    ----------
    S0 : float
        Spot price at time 0.
    K : float
        Strike price.
    r : float
        Risk-free (continuously compounded) annual rate.
    sigma : float
        Annualized volatility.
    T : float
        Time to maturity in years.

    Returns
    -------
    tuple[float, float]
        d1, d2 values.
    """
    if sigma <= 0.0 or T <= 0.0 or S0 <= 0.0 or K <= 0.0:
        raise ValueError("All inputs must be positive and sigma, T > 0.")
    numerator = math.log(S0 / K) + (r + 0.5 * sigma * sigma) * T
    denom = sigma * math.sqrt(T)
    d1 = numerator / denom
    d2 = d1 - sigma * math.sqrt(T)
    return d1, d2


def call_price(S0: float, K: float, r: float, sigma: float, T: float) -> float:
    """
    Black–Scholes price of a European call option.

    Returns
    -------
    float
        Theoretical call price under the Black–Scholes model.
    """
    d1, d2 = d1_d2(S0, K, r, sigma, T)
    return S0 * _norm_cdf(d1) - K * math.exp(-r * T) * _norm_cdf(d2)


def put_price(S0: float, K: float, r: float, sigma: float, T: float) -> float:
    """
    Black–Scholes price of a European put option.

    Returns
    -------
    float
        Theoretical put price under the Black–Scholes model.
    """
    d1, d2 = d1_d2(S0, K, r, sigma, T)
    return K * math.exp(-r * T) * _norm_cdf(-d2) - S0 * _norm_cdf(-d1)


def call_delta(S0: float, K: float, r: float, sigma: float, T: float) -> float:
    """
    Black–Scholes Delta for a European call option.

    Returns
    -------
    float
        Sensitivity of the call price to the underlying (dC/dS0).
    """
    d1, _ = d1_d2(S0, K, r, sigma, T)
    return _norm_cdf(d1)


def put_delta(S0: float, K: float, r: float, sigma: float, T: float) -> float:
    """
    Black–Scholes Delta for a European put option.

    Returns
    -------
    float
        Sensitivity of the put price to the underlying (dP/dS0).
    """
    d1, _ = d1_d2(S0, K, r, sigma, T)
    return _norm_cdf(d1) - 1.0
