from src import quasi_mc

def test_qmc_price():
    p = quasi_mc.price_european_call_qmc(100,100,0.02,0.2,1.0,n_sims=2048,seed=42)
    assert p>0
