import argparse
import os
import sys

# Make 'src' importable when running this example as a script
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))

from mc_pricing import price_european_mc, bs_price, relative_error  # noqa: E402


def main():
    """
    Simple CLI to price a European option via Monte Carlo and compare to Black–Scholes.
    """
    parser = argparse.ArgumentParser(description="Monte Carlo pricing for European options (GBM).")
    parser.add_argument("--type", choices=["call", "put"], default="call", help="Option type")
    parser.add_argument("--S0", type=float, default=100.0, help="Spot price")
    parser.add_argument("--K", type=float, default=100.0, help="Strike price")
    parser.add_argument("--r", type=float, default=0.02, help="Risk-free rate (cc)")
    parser.add_argument("--sigma", type=float, default=0.2, help="Volatility (annualized)")
    parser.add_argument("--T", type=float, default=1.0, help="Maturity in years")
    parser.add_argument("--n_sims", type=int, default=100000, help="Number of Monte Carlo samples")
    parser.add_argument("--n_steps", type=int, default=1, help="Number of steps for path simulation")
    parser.add_argument("--antithetic", action="store_true", help="Use antithetic variates")
    parser.add_argument("--control_variate", action="store_true", help="Use control variate (S_T)")
    parser.add_argument("--seed", type=int, default=42, help="Random seed")
    parser.add_argument("--path_method", choices=["exact", "euler"], default="exact", help="Path method if n_steps>1")
    args = parser.parse_args()

    price, stderr, ci_low, ci_high = price_european_mc(
        args.type, args.S0, args.K, args.r, args.sigma, args.T,
        n_sims=args.n_sims, n_steps=args.n_steps, antithetic=args.antithetic,
        control_variate=args.control_variate, seed=args.seed, path_method=args.path_method
    )
    bs_ref = bs_price(args.type, args.S0, args.K, args.r, args.sigma, args.T)
    rel_err = 100.0 * relative_error(price, bs_ref)

    print(f"MC {args.type} price: {price:.6f}")
    print(f"95% CI: [{ci_low:.6f}, {ci_high:.6f}], stderr={stderr:.6f}")
    print(f"BS {args.type} price: {bs_ref:.6f}")
    print(f"Relative error: {rel_err:.3f}%")


if __name__ == "__main__":
    main()
