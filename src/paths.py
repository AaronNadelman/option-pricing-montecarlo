import math
import numpy as np

def simulate_gbm_terminal(
    S0: float,
    r: float,
    sigma: float,
    T: float,
    n_sims: int,
    antithetic: bool = False,
    seed: int | None = None,
) -> np.ndarray:
    """
    Simulate terminal prices S_T for GBM under the risk-neutral measure.

    Uses the exact one-step lognormal solution:
        S_T = S0 * exp((r - 0.5*sigma^2) * T + sigma * sqrt(T) * Z), Z ~ N(0,1).

    Parameters
    ----------
    S0, r, sigma, T : float
        Model parameters (see Black–Scholes).
    n_sims : int
        Number of Monte Carlo paths.
    antithetic : bool
        If True, use antithetic variates (pair Z with -Z).
    seed : int | None
        Random seed for reproducibility.

    Returns
    -------
    np.ndarray
        Array of shape (n_sims,) with terminal prices.
    """
    if seed is not None:
        np.random.seed(seed)

    if antithetic:
        # Generate half the normals and mirror them.
        m = (n_sims + 1) // 2  # ceiling division for odd n_sims
        Z = np.random.standard_normal(size=m)
        Z_full = np.concatenate([Z, -Z])[:n_sims]
    else:
        Z_full = np.random.standard_normal(size=n_sims)

    drift = (r - 0.5 * sigma * sigma) * T
    diff = sigma * math.sqrt(T) * Z_full
    ST = S0 * np.exp(drift + diff)
    return ST


def simulate_gbm_paths(
    S0: float,
    r: float,
    sigma: float,
    T: float,
    n_steps: int,
    n_sims: int,
    method: str = "euler",
    seed: int | None = None,
) -> np.ndarray:
    """
    Simulate full GBM paths on a regular grid.

    Parameters
    ----------
    method : str
        "euler" uses Euler–Maruyama (shows discretization bias).
        "exact" uses exact per-step lognormal updates (no discretization bias).

    Returns
    -------
    np.ndarray
        Array with shape (n_sims, n_steps + 1), including S_0.
    """
    if seed is not None:
        np.random.seed(seed)
    dt = T / n_steps
    paths = np.empty((n_sims, n_steps + 1), dtype=float)
    paths[:, 0] = S0

    if method == "exact":
        mu = (r - 0.5 * sigma * sigma) * dt
        s = sigma * math.sqrt(dt)
        for t in range(1, n_steps + 1):
            Z = np.random.standard_normal(size=n_sims)
            paths[:, t] = paths[:, t - 1] * np.exp(mu + s * Z)
    elif method == "euler":
        for t in range(1, n_steps + 1):
            Z = np.random.standard_normal(size=n_sims)
            paths[:, t] = paths[:, t - 1] + r * paths[:, t - 1] * dt + sigma * paths[:, t - 1] * math.sqrt(dt) * Z
            # Clip to avoid negative values due to Euler discretization noise
            np.maximum(paths[:, t], 1e-12, out=paths[:, t])
    else:
        raise ValueError("Unknown method. Use 'euler' or 'exact'.")

    return paths
