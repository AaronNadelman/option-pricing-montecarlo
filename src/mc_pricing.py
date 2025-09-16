import math
import numpy as np
from typing import Literal

import black_scholes as bs
from paths import simulate_gbm_terminal, simulate_gbm_paths

OptionType = Literal["call", "put"]


def _payoff(ST: np.ndarray, K: float, opt_type: OptionType) -> np.ndarray:
    """
    Compute European payoff at maturity for each terminal price.

    Parameters
    ----------
    ST : np.ndarray
        Terminal prices, shape (n_sims,).
    K : float
        Strike price.
    opt_type : Literal["call", "put"]
        Option type.

    Returns
    -------
    np.ndarray
        Payoff array, shape (n_sims,).
    """
    if opt_type == "call":
        return np.maximum(ST - K, 0.0)
    elif opt_type == "put":
        return np.maximum(K - ST, 0.0)
    else:
        raise ValueError("opt_type must be 'call' or 'put'")


def price_european_mc(
    opt_type: OptionType,
    S0: float,
    K: float,
    r: float,
    sigma: float,
    T: float,
    n_sims: int = 100_000,
    n_steps: int = 1,
    antithetic: bool = False,
    control_variate: bool = False,
    seed: int | None = None,
    path_method: str = "exact",
) -> tuple[float, float, float, float]:
    """
    Monte Carlo pricing for a European option under GBM.

    The estimator optionally uses antithetic variates (to reduce variance) and a
    control variate based on S_T, whose expectation is known: E[S_T] = S0 * exp(rT).

    Parameters
    ----------
    opt_type : Literal["call", "put"]
        Option type to price.
    n_steps : int
        If >1, simulate multi-step paths; otherwise sample S_T directly.
    antithetic : bool
        If True, use antithetic variates for terminal sampling.
    control_variate : bool
        If True, apply control variate using S_T.
    seed : int | None
        Random seed for reproducibility.
    path_method : str
        "exact" or "euler" for multi-step simulation.

    Returns
    -------
    tuple[float, float, float, float]
        (price, stderr, ci_low, ci_high) with 95% confidence interval.
    """
    df = math.exp(-r * T)

    if n_steps <= 1:
        ST = simulate_gbm_terminal(S0, r, sigma, T, n_sims, antithetic=antithetic, seed=seed)
    else:
        paths = simulate_gbm_paths(S0, r, sigma, T, n_steps, n_sims, method=path_method, seed=seed)
        ST = paths[:, -1]

    X = _payoff(ST, K, opt_type)  # payoff at T (undiscounted)

    if control_variate:
        # Control variate: use C = S_T with known E[C] = S0 * exp(rT).
        C = ST
        C_mean_known = S0 * math.exp(r * T)
        cov = np.cov(X, C, ddof=1)[0, 1]
        varC = np.var(C, ddof=1)
        beta = cov / varC if varC > 0 else 0.0
        Y = X - beta * (C - C_mean_known)
        disc_samples = df * Y
    else:
        disc_samples = df * X

    price = float(np.mean(disc_samples))
    # Unbiased sample standard deviation of the discounted samples
    s = float(np.std(disc_samples, ddof=1)) if disc_samples.size > 1 else 0.0
    stderr = s / math.sqrt(disc_samples.size) if disc_samples.size > 1 else 0.0

    ci_low = price - 1.96 * stderr
    ci_high = price + 1.96 * stderr
    return price, stderr, ci_low, ci_high


def relative_error(estimate: float, truth: float) -> float:
    """
    Relative error |estimate - truth| / truth.

    Returns
    -------
    float
        Relative error in [0, +inf).
    """
    return abs(estimate - truth) / abs(truth)


def bs_price(opt_type: OptionType, S0: float, K: float, r: float, sigma: float, T: float) -> float:
    """
    Helper that dispatches to closed-form Black–Scholes price.
    """
    if opt_type == "call":
        return bs.call_price(S0, K, r, sigma, T)
    elif opt_type == "put":
        return bs.put_price(S0, K, r, sigma, T)
    else:
        raise ValueError("opt_type must be 'call' or 'put'")
