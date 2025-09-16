import os
import sys
import matplotlib.pyplot as plt

# Import src
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))
from mc_pricing import price_european_mc, bs_price, relative_error  # noqa: E402


def run_validation(
    opt_type="call",
    S0=100.0, K=100.0, r=0.02, sigma=0.2, T=1.0,
    Ns=(1000, 3000, 10000, 30000, 100000),
    use_antithetic=True, use_control=False, seed=42
):
    """
    Run a convergence study vs. Black–Scholes and save plots under assets/.
    """
    rel_errors = []
    stderr_list = []
    for i, N in enumerate(Ns):
        price, stderr, ci_low, ci_high = price_european_mc(
            opt_type, S0, K, r, sigma, T,
            n_sims=N, antithetic=use_antithetic, control_variate=use_control, seed=seed + i
        )
        ref = bs_price(opt_type, S0, K, r, sigma, T)
        rel_errors.append(relative_error(price, ref))
        stderr_list.append(stderr)

    # Plot relative error vs N
    plt.figure()
    plt.plot(Ns, rel_errors, marker="o")
    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel("Number of simulations (N)")
    plt.ylabel("Relative error |MC - BS| / BS")
    plt.title("MC vs BS: Relative Error Convergence")
    os.makedirs(os.path.join(os.path.dirname(__file__), "..", "assets"), exist_ok=True)
    fig1 = os.path.join(os.path.dirname(__file__), "..", "assets", "deviation_vs_bs.png")
    plt.savefig(fig1, dpi=160, bbox_inches="tight")
    plt.close()

    # Plot stderr vs N (should scale ~ 1/sqrt(N))
    plt.figure()
    plt.plot(Ns, stderr_list, marker="o")
    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel("Number of simulations (N)")
    plt.ylabel("Standard error of estimator")
    plt.title("MC Standard Error vs N")
    fig2 = os.path.join(os.path.dirname(__file__), "..", "assets", "convergence_plot.png")
    plt.savefig(fig2, dpi=160, bbox_inches="tight")
    plt.close()

    print("Saved:", fig1)
    print("Saved:", fig2)


if __name__ == "__main__":
    run_validation()
